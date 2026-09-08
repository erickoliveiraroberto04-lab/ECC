---
name: landing-page-scale-readiness-check
description: Checks whether a page will hold up when budget goes up, before the budget goes up. Use when a campaign is about to scale, or when a page that worked at low spend stopped working at higher spend.
---

# Landing Page Scale Readiness Check

## Use this skill when

- a spend increase is planned or has just happened, and the page's current performance at current spend is known.
- a spend increase is planned and the page has only ever run at low budget.
- targeting is about to broaden, so the audience that produced the current rate is about to change.

This skill judges whether the page survives more spend. Whether one page suits several audiences belongs to `traffic-temperature-match-review`.

## Required input

- current spend and current performance: sessions, conversions, conversion rate, and the audience or targeting that produced them.
- the planned spend, the planned targeting, and how many ad sets or campaigns will point at the page.
- what happens downstream of a conversion: who handles the lead, and what volume that process absorbs today.
- optional: historical performance at a previous spend level, which is the only real evidence about how this page behaves under scale.
- If the current rate came from narrow targeting and the plan is to broaden, say that the current rate is not a baseline for the new traffic. That is usually the whole finding.

Not for: whether one page suits several traffic temperatures at once (`traffic-temperature-match-review`), or reading a finished test (`landing-page-ab-test-readout`).

## Analysis workflow

1. Check whether message match, page clarity, proof, form completion, mobile UX and tracking are stable enough for more traffic.
2. Compare conversion rate with qualified lead or revenue quality, not just form submissions.
3. Identify the bottleneck most likely to get worse when spend increases.
4. Flag false scale signals like strong desktop CVR with weak mobile or weak lead quality.
5. Return scale, hold, fix-first or collect-more-data with the gating metric.

## Decision rules

- A conversion rate measured on a narrow audience does not transfer to a broad one. Never forecast the scaled result from it, and say explicitly that no forecast is being given.
- Name the pre-conditions rather than issuing a verdict. Readiness is conditional, and the conditions are what the user can act on.
- Check downstream capacity as seriously as the page. A page that converts at scale into a process that cannot answer the leads produces refunds and bad reviews.
- One page serving several new ad sets means any latent message-match gap gets paid for at the new spend. Recommend per-ad-set message match before launch, not after.
- If historical data exists from a previous spend level, it outranks every heuristic here. Use it and say so.
- Do not describe a spend increase as safe. Say which conditions make it survivable and which are unverified.

## Output format

| Factor | Now | After the increase | Transfers to the new traffic | Pre-condition |
|---|---|---|---|---|
| Spend, targeting width, ad sets on the page, conversion rate, lead volume, downstream capacity | Value | Planned value | Yes / no / unknown | What must be true first |

End with:

- `Readiness:` conditional, with the numbered pre-conditions
- `Why the current rate is not a forecast:` one sentence naming what changes
- `Decision:` scale after the pre-conditions / stage the increase / hold / ask for data
- `Missing data:` usually downstream capacity and historical performance at higher spend

## Practical example

User: "Page does 3.2 percent at 40 a day on one ad set targeting a narrow interest. We want to go to 300 a day next week across three ad sets and broader targeting."

Assistant should note: the 3.2 percent was produced by a narrow audience, and broadening targeting changes who lands on the page, so the current rate is not a baseline for the new traffic and should not be used to forecast the scaled result; one page serving three ad sets at 7.5 times the spend means any message-match gap that is currently invisible will be paid for at scale; nothing was said about form or support capacity, so whether the downstream flow absorbs seven times the lead volume is unknown. Then: the readiness verdict is conditional, with the specific pre-conditions listed: a lower-commitment path for the broader audience, per-ad-set message match checked before launch, and downstream capacity confirmed. No forecast rate is offered, because a rate measured on a narrow audience does not transfer to a broad one.

## Guardrails

- Do not forecast a conversion rate at the new spend.
- Do not call a spend increase safe.
- Do not change budgets, campaigns or targeting.
- Say explicitly when the current rate came from targeting that is about to change.
