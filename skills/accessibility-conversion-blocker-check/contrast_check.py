#!/usr/bin/env python3
"""Compute WCAG contrast ratios for landing page colour pairs.

Eyes adapt to a screen; ratios do not. This helper does the arithmetic so the
skill reports a measured number instead of an adjective.

Input format, one pair per line, pipe separated:

    label | foreground | background | font-size-px | font-weight

Font size and weight are optional and default to 16 and 400. Colours accept
#RGB, #RRGGBB, rgb(r,g,b) and the names white and black. Anything that cannot be
resolved to an opaque sRGB triple is rejected rather than guessed at, including
hsl() and any rgba() whose alpha is below 1: composite the colour over its
background yourself and supply the result.

Usage:
    python3 contrast_check.py pairs.txt
    printf 'Button|#ffffff|#86FF1D|15|600\\n' | python3 contrast_check.py -
    python3 contrast_check.py pairs.txt --level AAA
    python3 contrast_check.py pairs.txt --max-rows 40

Thresholds are WCAG 2.1: AA needs 4.5:1 for normal text and 3:1 for large text
and user interface components; AAA needs 7:1 and 4.5:1. Large text means at
least 24px, or at least 18.66px when the weight is 700 or more.

Exit codes, so a build gate can tell a real failure from a typo:
    0  every pair measured and passed
    1  at least one pair failed its threshold
    2  input unreadable, or a line could not be measured

Stdlib only. No network.
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from dataclasses import dataclass

BOM = "﻿"

NAMED = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
}

UNMEASURABLE = {
    "transparent": "transparent has no contrast ratio; supply the colour that shows through",
    "currentcolor": "currentColor is not resolvable here; supply the computed colour",
    "inherit": "inherit is not resolvable here; supply the computed colour",
}

HEX = re.compile(r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")
RGB = re.compile(
    r"^rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([0-9.]+%?)\s*)?\)$", re.I
)
HSL = re.compile(r"^hsla?\(", re.I)

LARGE_PX = 24.0
LARGE_BOLD_PX = 18.66
BOLD_WEIGHT = 700
MIN_WEIGHT = 1
MAX_WEIGHT = 1000
MAX_SIZE_PX = 1000.0

THRESHOLDS = {
    "AA": {"normal": 4.5, "large": 3.0},
    "AAA": {"normal": 7.0, "large": 4.5},
}

DEFAULT_MAX_ROWS = 60


class ColourError(ValueError):
    pass


def parse_colour(value: str) -> tuple[int, int, int]:
    v = value.strip().lstrip(BOM)
    low = v.lower()
    if low in UNMEASURABLE:
        raise ColourError(UNMEASURABLE[low])
    if low in NAMED:
        return NAMED[low]
    if HSL.match(v):
        raise ColourError(
            f"hsl() is not supported: {value!r}. Convert it to hex or rgb() first"
        )
    m = HEX.match(v)
    if m:
        h = m.group(1)
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    m = RGB.match(v)
    if m:
        channels = tuple(int(g) for g in m.groups()[:3])
        for c in channels:
            if not 0 <= c <= 255:
                raise ColourError(f"channel out of range in {value!r}")
        alpha_raw = m.group(4)
        if alpha_raw is not None:
            alpha = (
                float(alpha_raw.rstrip("%")) / 100.0
                if alpha_raw.endswith("%")
                else float(alpha_raw)
            )
            # A translucent colour has no ratio of its own. Silently discarding
            # alpha is how invisible text passes a build gate at 21:1.
            if not 0.0 <= alpha <= 1.0:
                raise ColourError(
                    f"alpha {alpha:g} in {value!r} is outside 0 to 1"
                )
            if alpha < 1.0:
                raise ColourError(
                    f"{value!r} is translucent (alpha {alpha:g}); composite it over "
                    "its background and supply the resulting opaque colour"
                )
        return channels  # type: ignore[return-value]
    raise ColourError(f"cannot parse colour {value!r}")


def parse_size(raw: str) -> float:
    try:
        size = float(raw)
    except ValueError as exc:
        raise ColourError(f"font size {raw!r} is not a number") from exc
    if not math.isfinite(size):
        raise ColourError(
            f"font size {raw!r} is not finite; a non-finite size would silently "
            "relax the threshold from normal text to large text"
        )
    if size <= 0:
        raise ColourError(f"font size {size:g} must be greater than zero")
    if size > MAX_SIZE_PX:
        raise ColourError(f"font size {size:g}px is out of range (max {MAX_SIZE_PX:g})")
    return size


def parse_weight(raw: str) -> int:
    low = raw.lower()
    if low in {"bold", "bolder"}:
        return BOLD_WEIGHT
    if low in {"normal", "lighter"}:
        return 400
    try:
        weight = int(raw)
    except ValueError as exc:
        raise ColourError(f"font weight {raw!r} is not a number") from exc
    if not MIN_WEIGHT <= weight <= MAX_WEIGHT:
        raise ColourError(
            f"font weight {weight} is out of range ({MIN_WEIGHT}-{MAX_WEIGHT})"
        )
    return weight


def channel_luminance(c: int) -> float:
    s = c / 255.0
    return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    r, g, b = (channel_luminance(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg: tuple[int, int, int], bg: tuple[int, int, int]) -> float:
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def is_large(size_px: float, weight: int) -> bool:
    if weight >= BOLD_WEIGHT:
        return size_px >= LARGE_BOLD_PX
    return size_px >= LARGE_PX


@dataclass
class Pair:
    label: str
    fg_raw: str
    bg_raw: str
    size: float
    weight: int
    ratio: float
    required: float
    large: bool

    @property
    def passes(self) -> bool:
        return round(self.ratio, 2) >= self.required

    @property
    def status(self) -> str:
        return "pass" if self.passes else "FAIL"

    @property
    def rule(self) -> str:
        kind = "large text or UI component" if self.large else "normal text"
        return f"{self.required}:1 ({kind})"


def parse_line(line: str, level: str) -> Pair:
    parts = [p.strip() for p in line.lstrip(BOM).split("|")]
    if len(parts) < 3:
        raise ColourError(
            "need at least label|foreground|background, got: " + line.strip()
        )
    label, fg_raw, bg_raw = parts[0], parts[1], parts[2]
    if not label:
        raise ColourError("label is empty: " + line.strip())
    size = parse_size(parts[3]) if len(parts) > 3 and parts[3] else 16.0
    weight = parse_weight(parts[4]) if len(parts) > 4 and parts[4] else 400

    fg, bg = parse_colour(fg_raw), parse_colour(bg_raw)
    ratio = contrast_ratio(fg, bg)
    large = is_large(size, weight)
    required = THRESHOLDS[level]["large" if large else "normal"]
    return Pair(label, fg_raw, bg_raw, size, weight, ratio, required, large)


def render(
    pairs: list[Pair],
    errors: list[str],
    level: str,
    max_rows: int = DEFAULT_MAX_ROWS,
) -> str:
    failures = [p for p in pairs if not p.passes]
    passing = [p for p in pairs if p.passes]

    # This output lands in a model's context, so cap it. Failures are printed
    # first and never dropped to make room for passing rows.
    shown = failures[:max_rows]
    remaining = max_rows - len(shown)
    if remaining > 0:
        shown = shown + passing[:remaining]
        hidden_pass = max(0, len(passing) - remaining)
    else:
        hidden_pass = len(passing)
    hidden_fail = max(0, len(failures) - max_rows)

    out = [
        f"## Contrast measurement (WCAG 2.1 {level})",
        "",
        "| Element | Foreground on background | Size / weight | Ratio | Required | Status |",
        "|---|---|---|---|---|---|",
    ]
    for p in shown:
        out.append(
            f"| {p.label} | {p.fg_raw} on {p.bg_raw} | "
            f"{p.size:g}px / {p.weight} | {p.ratio:.2f}:1 | {p.rule} | {p.status} |"
        )
    out += ["", f"Pairs measured: {len(pairs)}. Failing: {len(failures)}."]
    if hidden_fail or hidden_pass:
        out.append(
            f"Rows shown: {len(shown)} of {len(pairs)}. Not shown: "
            f"{hidden_fail} failing, {hidden_pass} passing. Raise --max-rows to see them."
        )
    if failures:
        worst = min(failures, key=lambda p: p.ratio)
        out.append(
            f"Worst pair: {worst.label} at {worst.ratio:.2f}:1 against "
            f"{worst.required}:1."
        )
    if errors:
        out += ["", "### Lines that could not be measured", ""]
        out += [f"- {e}" for e in errors]
        out += [
            "",
            "These lines were not measured, so this run is incomplete. Fix them and "
            "run again before reporting a pass.",
        ]
    out += [
        "",
        "Thresholds are WCAG 2.1: AA 4.5:1 normal and 3:1 large or UI, AAA 7:1 "
        "and 4.5:1. Large means 24px, or 18.66px at weight 700 or more. This is "
        "a measurement, not a conformance verdict.",
        "",
    ]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="WCAG contrast ratios for colour pairs.")
    ap.add_argument("file", help="pairs file, or - for stdin")
    ap.add_argument(
        "--level", choices=sorted(THRESHOLDS), default="AA",
        help="WCAG level to check against (default AA)",
    )
    ap.add_argument(
        "--max-rows", type=int, default=DEFAULT_MAX_ROWS,
        help=f"maximum table rows to print (default {DEFAULT_MAX_ROWS}); failing rows "
             "print first and are never dropped for passing ones",
    )
    args = ap.parse_args(argv)

    try:
        raw = sys.stdin.read() if args.file == "-" else open(
            args.file, encoding="utf-8-sig"
        ).read()
    except (OSError, UnicodeDecodeError) as exc:
        print(f"Cannot read {args.file}: {exc}", file=sys.stderr)
        return 2

    pairs: list[Pair] = []
    errors: list[str] = []
    for line in raw.splitlines():
        stripped = line.lstrip(BOM).strip()
        # A comment has no pipes. "#1 Hero CTA|#fff|#fff" is a label, and treating
        # it as a comment silently dropped invisible text from the run.
        if not stripped or (stripped.startswith("#") and "|" not in stripped):
            continue
        try:
            pairs.append(parse_line(line, args.level))
        except (ColourError, ValueError) as exc:
            errors.append(str(exc))

    if not pairs and not errors:
        print("No pairs found. One per line: label|foreground|background|size|weight")
        return 2

    print(render(pairs, errors, args.level, max(1, args.max_rows)))
    if errors:
        return 2
    return 1 if any(not p.passes for p in pairs) else 0


if __name__ == "__main__":
    sys.exit(main())
