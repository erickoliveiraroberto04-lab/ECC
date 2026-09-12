---
name: trial-vs-demo-path-decision
description: Decides whether the page should ask for a free trial, a demo call, or both, based on deal size, setup effort and who has to approve. Use when the primary CTA is being chosen or changed, or when one path produces volume and the other produces revenue.
---

# Trial Vs Demo Path Decision

## Use this skill when

- the primary CTA is up for debate and the argument is "self-serve is the future" against "our buyers need a call".
- trials sign up in volume and never activate, while the handful of demo requests close.
- the page offers both paths with equal weight and neither performs.
- setup effort or contract complexity changed and the CTA never moved with it.

Do not use this skill to write the CTA label. `cta-clarity-check` owns wording. This decides which ask the page is making.

## Required input

- what happens after each path today: trial length, whether a card is required, what setup the user must complete, and what a demo call actually covers.
- deal economics: average contract value, sales cycle length, and whether a human is needed to configure or approve anything.
- time to first value: how long from signup until the product does something the user can see.
- current numbers per path if both exist: starts, activation rate, close rate, and revenue.
- If time to first value is unknown, do not guess it. Measure it with the degraded path below; it takes one afternoon and it decides the whole question.

### If the data does not exist

- **No measured time to first value:** sign up for your own product with a clean account and a stopwatch. Record every step and how long it took, including waits for a sync and anything a human had to do. That walkthrough is the input, and it is better than any analytics report for this specific question.
- **No activation rate:** count how many of the last 20 signups reached the first useful outcome. Twenty is a small sample; say so, and it is still enough to tell 2 from 15.
- **No ACV or cycle length:** use the last five closed deals. Name the sample size.
- **Nothing at all:** the output is the walkthrough instruction above, not a path recommendation. Say plainly that recommending trial or demo without knowing time to first value would be a guess wearing a table.

## Analysis workflow

1. Measure the gap between signup and first visible value in the product, counting every step the user must complete alone: connect an account, import data, invite a colleague, wait for a sync.
2. Count the humans required before value appears. Any mandatory human step means an unassisted trial cannot deliver value, whatever the marketing site says.
3. Check who approves the purchase. If the person who would run the trial cannot sign, a trial produces an internal champion, not a sale, and the page should say so.
4. Compare deal size against the cost of a sales conversation. A deal that cannot pay for the call needs a self-serve path even if the product is complicated.
5. Read the current numbers per path. Volume on one and revenue on the other is the normal pattern and is not by itself an argument for cutting either.
6. Decide the primary ask, and decide what the secondary path is for: catching the wrong-fit visitor, catching the champion who cannot sign, or nothing.
7. If both stay, give them unequal weight on the page and say which visitor each one is for.

## Decision rules

- If first value requires a mandatory human step, an unassisted trial is a broken promise. Fix the promise or fix the step; do not fix the button.
- If time to first value exceeds the trial length, the trial is decoration. Say it plainly.
- Heuristic, labelled as such: deals small enough that one sales call costs a meaningful share of the contract value need a self-serve path; deals with a mandatory security, procurement or configuration step need a call. Use the supplied numbers, not the heuristic, whenever the numbers exist.
- Two equally weighted CTAs is a decision the page is refusing to make. Recommend a primary and a subordinate, never a tie.
- A trial that requires a card is a different ask from one that does not. Do not compare them as if they were the same path.
- Do not recommend building a self-serve onboarding flow as a page fix. Name it as a product dependency with an owner.

## Output format

| Input | Value | Source | Implication for the path |
|---|---|---|---|
| Time to first value, mandatory human steps, ACV, cycle length, approver | The number or a missing-data marker | Supplied, measured or assumed | What it rules in or out |

Then:

- `Primary ask:` trial or demo, and the one-sentence reason
- `Secondary path:` what it is for, or cut
- `Product dependencies:` steps that must change before the recommended ask is honest

End with:

- `Decision:` change the primary CTA / keep and reweight / fix the product step first / ask for data
- `Missing data:` what would change the verdict

## Practical example

User: "ACV 6000 a year, sales cycle about 5 weeks. Free trial is 14 days, no card. To see anything useful you connect an ad account and wait for a 24 hour sync, then our team configures the alerting rules. 300 trials last quarter, 11 activated, 4 closed. 18 demo requests, 9 closed."

Assistant should note: configuration by the team is a mandatory human step, so the 14 day unassisted trial promises something the product cannot deliver alone, and that is why 289 of 300 trials never activated; a 24 hour sync plus a configuration call means real time to first value is measured in days, not minutes; a 6000 ACV with a 5 week cycle comfortably pays for a call, and the demo path closes at 50 percent against 1.3 percent on trials. Then: the demo becomes the primary ask, the trial stays only as a subordinate path for the visitor who wants to look before talking, and the mandatory configuration step is named as a product dependency owned outside the page. Close rates on 18 and 300 are small samples, so the direction is strong and the exact rates are not forecasts.

## Guardrails

- Do not change the page, the CTA or the trial configuration.
- Do not recommend removing a sales team or hiring one.
- Do not treat activation as conversion. Say which one each number is.
- Mark small samples as small rather than quoting their rates as stable.
