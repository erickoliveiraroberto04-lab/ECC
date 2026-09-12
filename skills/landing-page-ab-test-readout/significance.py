#!/usr/bin/env python3
"""Decide whether an A/B result is a decision or a coincidence, with arithmetic.

A model asked to judge "is 36/1200 versus 48/1180 inside the range noise
produces" will produce a confident sentence and no number. This helper produces
the number, so the skill can refuse a winner on evidence rather than on instinct.

Usage:
    python3 significance.py --a 1200 36 --b 1180 48
    python3 significance.py --a 4210 131 --b 4210 160 --alpha 0.05
    python3 significance.py --a 1200 36 --b 1180 48 --runtime-days 6

Each --a / --b takes two numbers: visitors, then conversions.

What it computes:
    two-proportion z-test, two-sided, pooled standard error
    Wilson score interval per variant
    confidence interval on the absolute difference
    visitors per arm required to detect the observed difference
    minimum detectable effect at the sample size you actually have

Refusal gates, applied before any winner is named, matching this pack's rules:
    fewer than 100 conversions in either arm    -> inconclusive
    runtime under 7 days, when supplied         -> inconclusive

Exit codes:
    0  a significant difference that also clears the refusal gates
    1  inconclusive
    2  bad input

These are frequentist results on a single comparison. Testing several variants or
peeking repeatedly changes the error rate, and this helper does not correct for
either; it says so in the output rather than pretending otherwise.

Stdlib only. No network.
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass

MIN_CONVERSIONS_PER_ARM = 100
MIN_RUNTIME_DAYS = 7

# Two-sided critical values, so no scipy dependency.
Z_CRIT = {0.10: 1.6449, 0.05: 1.9600, 0.01: 2.5758}
Z_POWER_80 = 0.8416  # one-sided z for 80 percent power


class InputError(ValueError):
    pass


def normal_cdf(z: float) -> float:
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def two_sided_p(z: float) -> float:
    return 2.0 * (1.0 - normal_cdf(abs(z)))


def wilson_interval(successes: int, n: int, z: float) -> tuple[float, float]:
    """Wilson score interval. Behaves at small n and at rates near zero, where
    the normal approximation returns intervals below zero."""
    if n == 0:
        return (0.0, 0.0)
    p = successes / n
    denom = 1.0 + z * z / n
    centre = (p + z * z / (2.0 * n)) / denom
    margin = (
        z * math.sqrt(p * (1.0 - p) / n + z * z / (4.0 * n * n))
    ) / denom
    return (max(0.0, centre - margin), min(1.0, centre + margin))


@dataclass
class Arm:
    name: str
    visitors: int
    conversions: int

    @property
    def rate(self) -> float:
        return self.conversions / self.visitors if self.visitors else 0.0


@dataclass
class Result:
    a: Arm
    b: Arm
    alpha: float
    runtime_days: int | None
    monthly_conversions: int | None = None

    @property
    def z_crit(self) -> float:
        return Z_CRIT[self.alpha]

    @property
    def pooled(self) -> float:
        total_v = self.a.visitors + self.b.visitors
        total_c = self.a.conversions + self.b.conversions
        return total_c / total_v if total_v else 0.0

    @property
    def standard_error(self) -> float:
        p = self.pooled
        return math.sqrt(p * (1.0 - p) * (1.0 / self.a.visitors + 1.0 / self.b.visitors))

    @property
    def z(self) -> float:
        se = self.standard_error
        return (self.b.rate - self.a.rate) / se if se else 0.0

    @property
    def p_value(self) -> float:
        return two_sided_p(self.z)

    @property
    def difference(self) -> float:
        return self.b.rate - self.a.rate

    @property
    def difference_interval(self) -> tuple[float, float]:
        se_unpooled = math.sqrt(
            self.a.rate * (1 - self.a.rate) / self.a.visitors
            + self.b.rate * (1 - self.b.rate) / self.b.visitors
        )
        margin = self.z_crit * se_unpooled
        return (self.difference - margin, self.difference + margin)

    @property
    def statistically_significant(self) -> bool:
        return self.p_value < self.alpha

    @property
    def required_visitors_per_arm(self) -> int | None:
        """Visitors per arm needed to detect the observed difference at this
        alpha with 80 percent power. None when there is no difference to size."""
        delta = abs(self.difference)
        if delta == 0:
            return None
        p1, p2 = self.a.rate, self.b.rate
        pbar = (p1 + p2) / 2.0
        if pbar in (0.0, 1.0):
            return None
        n = (
            (self.z_crit * math.sqrt(2 * pbar * (1 - pbar)) + Z_POWER_80 * math.sqrt(
                p1 * (1 - p1) + p2 * (1 - p2)
            ))
            ** 2
        ) / (delta**2)
        return math.ceil(n)

    @property
    def mde_at_current_size(self) -> float | None:
        """Smallest absolute difference detectable at the sample size on hand.

        None at a control rate of 0 or 100 percent, where the formula collapses to
        zero and would read as "any difference is detectable"."""
        p = self.a.rate
        n = min(self.a.visitors, self.b.visitors)
        if n == 0 or p in (0.0, 1.0):
            return None
        return (
            self.z_crit * math.sqrt(2 * p * (1 - p) / n)
            + Z_POWER_80 * math.sqrt(2 * p * (1 - p) / n)
        )

    @property
    def gate_failures(self) -> list[str]:
        failures = []
        for arm in (self.a, self.b):
            if arm.conversions < MIN_CONVERSIONS_PER_ARM:
                failures.append(
                    f"variant {arm.name} has {arm.conversions} conversions, under the "
                    f"{MIN_CONVERSIONS_PER_ARM} minimum per arm"
                )
        if self.runtime_days is not None and self.runtime_days < MIN_RUNTIME_DAYS:
            failures.append(
                f"runtime of {self.runtime_days} days is under one full business cycle "
                f"of {MIN_RUNTIME_DAYS} days"
            )
        return failures

    @property
    def verdict(self) -> str:
        if self.gate_failures:
            return "inconclusive"
        if not self.statistically_significant:
            return "inconclusive"
        return "winner" if self.difference > 0 else "control wins"


def pct(x: float) -> str:
    return f"{x * 100:.2f}%"


def points(x: float) -> str:
    return f"{x * 100:+.2f}pp"


def render(r: Result) -> str:
    lo_a, hi_a = wilson_interval(r.a.conversions, r.a.visitors, r.z_crit)
    lo_b, hi_b = wilson_interval(r.b.conversions, r.b.visitors, r.z_crit)
    d_lo, d_hi = r.difference_interval
    confidence = int(round((1 - r.alpha) * 100))

    out = [
        "## Significance",
        "",
        f"| Variant | Visitors | Conversions | Rate | {confidence}% interval |",
        "|---|---|---|---|---|",
        f"| {r.a.name} | {r.a.visitors} | {r.a.conversions} | {pct(r.a.rate)} | "
        f"{pct(lo_a)} to {pct(hi_a)} |",
        f"| {r.b.name} | {r.b.visitors} | {r.b.conversions} | {pct(r.b.rate)} | "
        f"{pct(lo_b)} to {pct(hi_b)} |",
        "",
        f"- Absolute difference: {points(r.difference)}",
        f"- {confidence}% interval on the difference: {points(d_lo)} to {points(d_hi)}",
        f"- z = {r.z:.3f}, two-sided p = {r.p_value:.4f}, alpha = {r.alpha}",
        f"- Statistically significant: {'yes' if r.statistically_significant else 'no'}",
    ]

    if d_lo <= 0 <= d_hi:
        out.append(
            "- The interval on the difference contains zero, so the direction of the "
            "effect is not established."
        )

    required = r.required_visitors_per_arm
    if required is not None:
        have = min(r.a.visitors, r.b.visitors)
        shortfall = max(0, required - have)
        out.append(
            f"- Visitors per arm needed to detect this difference at 80% power: "
            f"{required}. You have {have}."
            + (f" Shortfall: {shortfall} per arm." if shortfall else "")
        )
    mde = r.mde_at_current_size
    out.append(
        f"- Smallest difference detectable at your current size: {mde * 100:.2f}pp"
        if mde is not None
        else "- Smallest difference detectable at your current size: not computable "
             "at a control rate of 0 or 100 percent"
    )

    out += ["", "### Refusal gates", "", "| Gate | Status |", "|---|---|"]
    for arm in (r.a, r.b):
        ok = arm.conversions >= MIN_CONVERSIONS_PER_ARM
        out.append(
            f"| {MIN_CONVERSIONS_PER_ARM}+ conversions in {arm.name} | "
            f"{'pass' if ok else 'FAIL'} ({arm.conversions}) |"
        )
    if r.runtime_days is None:
        out.append("| At least one full business cycle | unknown, runtime not supplied |")
    else:
        ok = r.runtime_days >= MIN_RUNTIME_DAYS
        out.append(
            f"| At least {MIN_RUNTIME_DAYS} days of runtime | "
            f"{'pass' if ok else 'FAIL'} ({r.runtime_days}) |"
        )

    out += [
        "",
        "### In plain English",
        "",
        f"- `pp` means percentage points. The gap between the two pages is "
        f"{abs(r.difference) * 100:.2f} of them.",
        f"- `p = {r.p_value:.4f}` means that if the two pages were actually "
        f"identical, you would see a gap this big about "
        f"{r.p_value * 100:.1f} times in 100 tests. Anything above "
        f"{r.alpha * 100:.0f} is normally treated as too likely to be luck.",
        "- The interval is the range the true difference plausibly sits in. When it "
        "crosses zero, the better page might be either one.",
        f"- The sample number is how many visitors each version would need before a "
        f"gap this size stops looking like luck.",
        "",
    ]

    # A founder at low volume can hit "inconclusive" forever without being told
    # that it is permanent at their traffic level rather than a matter of waiting.
    if r.monthly_conversions:
        per_arm = r.monthly_conversions / 2.0
        if per_arm > 0:
            months = MIN_CONVERSIONS_PER_ARM / per_arm
            if months > 3:
                out += [
                    "### Volume reality check",
                    "",
                    f"At {r.monthly_conversions} conversions a month split across two "
                    f"arms, reaching {MIN_CONVERSIONS_PER_ARM} per arm takes about "
                    f"{months:.0f} months. **A/B testing cannot decide anything at "
                    "this volume**, and running longer will keep returning "
                    "inconclusive rather than eventually returning a winner.",
                    "",
                    "What to do instead: change one thing at a time, keep it for a "
                    "full month, and compare that month against the previous one. "
                    "That is a weaker form of evidence and it is the honest one "
                    "available at this traffic level. Say so out loud rather than "
                    "treating a period comparison as a test.",
                    "",
                ]

    out += ["", f"### Verdict: {r.verdict}", ""]
    if r.gate_failures:
        out.append("Blocked by:")
        out += [f"- {f}" for f in r.gate_failures]
        out.append("")
    if r.verdict == "inconclusive":
        out += [
            "Shipping a variant anyway is a legitimate business decision. Record it as "
            "a decision taken without evidence of a lift, never as a validated lift.",
            "",
        ]
    out += [
        "Frequentist result on a single comparison. Testing several variants at once, "
        "or stopping the moment the numbers looked good, changes the real error rate "
        "and is not corrected for here.",
        "",
    ]
    return "\n".join(out)


def parse_arm(name: str, values: list[int]) -> Arm:
    visitors, conversions = values
    if visitors <= 0:
        raise InputError(f"variant {name}: visitors must be greater than zero")
    if conversions < 0:
        raise InputError(f"variant {name}: conversions cannot be negative")
    if conversions > visitors:
        raise InputError(
            f"variant {name}: {conversions} conversions from {visitors} visitors is "
            "impossible; check which column is which"
        )
    return Arm(name, visitors, conversions)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Two-proportion significance test for an A/B landing page result."
    )
    ap.add_argument(
        "--a", nargs=2, type=int, required=True, metavar=("VISITORS", "CONVERSIONS"),
        help="control arm",
    )
    ap.add_argument(
        "--b", nargs=2, type=int, required=True, metavar=("VISITORS", "CONVERSIONS"),
        help="variant arm",
    )
    ap.add_argument(
        "--alpha", type=float, default=0.05, choices=sorted(Z_CRIT),
        help="significance level (default 0.05)",
    )
    ap.add_argument(
        "--runtime-days", type=int, default=None,
        help="days the test ran; enables the business-cycle refusal gate",
    )
    ap.add_argument(
        "--monthly-conversions", type=int, default=None,
        help="total conversions this page gets per month; enables the volume "
             "reality check, which says when A/B testing cannot decide anything at "
             "your traffic level rather than leaving you to wait forever",
    )
    ap.add_argument("--name-a", default="A")
    ap.add_argument("--name-b", default="B")
    args = ap.parse_args(argv)

    try:
        a = parse_arm(args.name_a, args.a)
        b = parse_arm(args.name_b, args.b)
    except InputError as exc:
        print(f"{exc}", file=sys.stderr)
        return 2

    if args.runtime_days is not None and args.runtime_days <= 0:
        print("runtime-days must be greater than zero", file=sys.stderr)
        return 2

    result = Result(a, b, args.alpha, args.runtime_days, args.monthly_conversions)
    print(render(result))
    return 0 if result.verdict not in {"inconclusive"} else 1


if __name__ == "__main__":
    sys.exit(main())
