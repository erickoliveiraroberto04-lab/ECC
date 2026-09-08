---
name: landing-page-ab-test-readout
description: Decides whether an A/B result is a decision or a coincidence, and says plainly when the honest answer is that the test cannot conclude. Use when a test has run and someone wants to declare a winner.
---

# Landing Page Ab Test Readout

## Use this skill when

- an A/B test has finished or is being called early, and the per-variant sample sizes and conversion counts are available.
- somebody wants to declare a winner and ship it this week.
- a test was stopped early because the numbers looked good.

This skill reads a finished test and needs conversion counts per arm. It does not design tests or run them.

## Required input

- per variant: sessions or visitors, conversions, and the conversion definition. Rates alone are not enough; the readout needs the counts.
- runtime in days, and the days of the week it covered.
- what changed between variants, and whether anything else changed on the site during the window.
- optional but decisive: segment splits by device and source, with their own counts.
- tracking confidence: was the same event measured identically in both arms.
- If conversion counts per arm are missing, this skill does not run. Ask for them. A readout built on rates cannot compute anything.

Not for: deciding what to test next, or reading a test that has not finished. This skill reads a result that exists.

There is a deterministic helper next to this skill: `significance.py`. Run it. Do not assess significance by eye.

## Analysis workflow

1. Restate the hypothesis, variant difference, audience, dates, traffic source and success metric.
2. Check sample size, baseline CVR, absolute lift, relative lift, confidence and tracking quality.
3. Compare results by segment: device, source, campaign, new vs returning and lead quality where available.
4. Separate statistical signal from business significance and novelty effects.
5. Return ship, continue, stop, rerun or inconclusive with the next test question.

## Diagnostic rubric

Use this table when the user provides A/B test data:

| Segment | Variant A CVR | Variant B CVR | Absolute lift | Relative lift | Quality signal | Decision |
|---|---:|---:|---:|---:|---|---|
| All traffic / device / source / audience | Percent or missing-data marker | Percent or missing-data marker | Percentage points | Percent | SQL rate, form quality, revenue signal or missing-data marker | Ship / keep testing / segment / rerun / ignore |

Then call out:

- Trust level: sample size, tracking quality, runtime and segment consistency.
- Business readout: what changes for qualified leads, pipeline or revenue, if known.
- Follow-up test: the one next test if the result is useful but incomplete.

## Decision rules

- Run `significance.py` first and quote its numbers. A verdict about noise without a computed p-value or interval is a vibe, and this is the one skill where that is unforgivable.
- **Refusal thresholds, applied before any winner is named.** Under 100 conversions in either arm, or a runtime shorter than seven days, the verdict is `inconclusive` regardless of what the observed difference looks like. State which of the two conditions failed. **Both numbers are this pack's own working defaults with no external source**, including calling seven days one business cycle; say so whenever you quote them.
- A test that stopped the moment it looked significant did not measure what it appears to have measured. Ask when the decision to stop was made, and say the result is compromised if it was made on the strength of the numbers.
- Segment findings need their own counts. A device split quoted without sessions per device is not evidence and should be dropped from the readout rather than reported at medium confidence.
- Report the interval, not only the point estimate. A lift of 1.1 points with an interval spanning zero is a decision not to act, expressed honestly.
- Shipping a variant that did not reach significance is a legitimate business decision. Say so, and say plainly that it must not then be recorded as a validated lift.
- Never smooth an inconclusive result into a weak recommendation. The description of this skill promises it will say a test cannot conclude, and that promise is the point.

## Output format

Start with the helper's output, verbatim.

| Variant | Sessions | Conversions | Rate | Difference vs control | Interval | Significant |
|---|---|---|---|---|---|---|
| A / B | Count | Count | Computed | Percentage points | From the helper | Yes / no, at the stated level |

Then:

| Gate | Status |
|---|---|
| At least 100 conversions per arm | Pass / fail, with the counts |
| At least one full business cycle | Pass / fail, with the runtime |
| Same conversion definition in both arms | Pass / fail / unknown |
| Stop decision made before looking | Yes / no / unknown |

End with:

- `Verdict:` winner / inconclusive / compromised
- `If you ship it anyway:` the sentence that must go in the record instead of "validated lift"
- `Additional sample needed to decide:` the number from the helper, or not applicable
- `Missing data:` what would change the verdict

## Practical example

User: "Variant B wins. A: 1200 sessions, 36 conversions, 3.0 percent. B: 1180 sessions, 48 conversions, 4.07 percent. Ran 6 days. We want to ship B."

Assistant should run the helper first:

```bash
python3 significance.py --a 1200 36 --b 1180 48 --runtime-days 6
```

and quote what it printed: the observed gap is +1.07pp, z = 1.412, two-sided p = 0.1581 at alpha 0.05, and the 95 percent interval on the difference runs from -0.42pp to +2.55pp, so it contains zero and the direction of the effect is not established. Detecting a difference this size at 80 percent power would need 4693 visitors per arm against the 1180 on hand, a shortfall of 3513. Both refusal gates also fail independently: 36 and 48 conversions are under the 100 per arm minimum, and six days is under one full business cycle.

Then the verdict: inconclusive, not "B wins". Shipping B anyway is a legitimate business decision, and the sentence that goes in the record is that it was shipped without evidence of a lift, never as a validated lift. No segment consistency and no tracking confidence were supplied, so whether the instrumentation matched between arms is unknown and would change this readout if it did not.

## Guardrails

- Do not name a winner without running the helper.
- Do not name a winner below the refusal thresholds, whatever the observed difference.
- Do not report a segment result without that segment's counts.
- Do not soften inconclusive into a weak yes.
- Do not start, stop or configure a test.
