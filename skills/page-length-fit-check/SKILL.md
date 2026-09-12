---
name: page-length-fit-check
description: Decides whether a landing page is too short or too long for the offer and the traffic hitting it. Use when someone argues about page length, when a short page underperforms on cold traffic, or when a long page loses people before the first CTA.
---

# Page Length Fit Check

## Use this skill when

- the team is arguing about page length and both sides are quoting somebody else's case study.
- a short page performs on branded or retargeting traffic and collapses on cold traffic, or the reverse.
- a long page has scroll data showing most people never reach the argument it was built to make.
- the offer changed, the commitment got bigger or smaller, and the page length never moved.

Do not use this skill to decide what the page should say. It decides how much the page has to say before it can ask.

## Required input

- the page structure in order: every section, its purpose, and where each CTA sits.
- the commitment being asked for: email, trial, card, call, purchase, and the price if money is involved.
- traffic temperature by source: cold prospecting, warm retargeting, branded search, email list, referral, and the rough split.
- scroll and engagement data if available: scroll depth percentiles, time on page, CTA clicks by position.
- If the traffic split is unknown, mark it as an assumption. Page length is only ever right relative to the traffic it receives.

### If the data does not exist

Scroll depth is the input people most often lack, and it is worth ten minutes to get.

- **No scroll data:** GA4 records a `scroll` event at 90 percent depth by default. Reports, then Engagement, then Events, and look for `scroll`. It only tells you who reached the bottom, which is a blunter version of the same signal and enough to rank sections into "most people saw this" and "most people did not".
- **Not even that:** open the page on your own phone and count how many thumb swipes it takes to reach the first ask. More than three and the ask is effectively below the fold for a cold visitor. Say the finding came from a manual walk, not from data.
- **No traffic split:** state the assumption in one line and run the analysis for cold traffic only, since that is the case a long page exists to serve.
- **Nothing at all:** the deliverable is the section inventory with each section marked as objection, proof, ask or nothing. That much needs no analytics, and the sections carrying nothing are cuttable on sight.

## Analysis workflow

1. Write down the commitment and its cost to the visitor in money, time and risk. This sets how much argument the page owes before it asks.
2. List the objections a cold visitor has to have answered before that commitment is reasonable. Each unanswered objection is a section the page still owes.
3. Walk the page in order and mark each section as: carries an objection, carries proof, carries the ask, or carries nothing.
4. Find the first CTA and count how many objections were answered above it. A hard ask above the argument is a length defect even on a short page.
5. Compare scroll depth against the position of the sections that do the persuading. Persuasion sitting below the 25th percentile of scroll depth is being paid for and read by under a quarter of visitors. The 25th percentile is the cutoff this pack uses to mean "most people never got here"; it is our own convention, not a researched threshold, so name the actual percentile from the data instead of the label wherever you can.
6. Split the verdict by traffic temperature: the same page can be correctly long for cold traffic and wastefully long for branded traffic. Say which segment each finding applies to.
7. Recommend either cutting sections that carry nothing, moving a section above the first CTA, or adding the single missing objection section, never a wholesale length change.

## Decision rules

- Length is not the variable. Answered objections per ask is the variable. Report it that way, and refuse the framing if the user insists on a word count target.
- A section carrying nothing is a cut regardless of total page length.
- If most of the persuasion sits below where most visitors stop scrolling, the fix is order, not length. This is the most common real finding.
- Heuristic, labelled as such: an email ask can precede the argument, a card or a call ask generally cannot. Treat it as a starting position, not a rule, and defer to the segment data whenever it exists.
- If different traffic temperatures need different lengths and the team runs one page, say that plainly and name the cost of each option rather than picking for them.
- Do not cite external benchmarks about long versus short pages. They are about somebody else's offer.

## Output format

| Section | Position | Carries | Objection answered | Verdict |
|---|---|---|---|---|
| Section name | Order and approximate scroll position | Objection / proof / ask / nothing | The specific objection or none | Keep / cut / move up / move down |

Then:

| Traffic temperature | Share | Objections it needs answered | Current page fit |
|---|---|---|---|

End with:

- `Decision:` cut sections / reorder / add one section / split the page by temperature / ask for data
- `Objections still unanswered above the first CTA:` the list
- `Missing data:` what would change the verdict

## Practical example

User: "Page is 11 sections, 2400 words, one CTA at the very bottom asking to book a 30 minute call. Traffic: 70 percent cold Meta prospecting, 30 percent branded search. Scroll: 50th percentile stops at section 4, 25th percentile reaches section 6."

Assistant should note: the only ask sits below where three quarters of visitors have already left, so the page is not too long, it is asked too late; sections 7 to 11 are being paid for and read by under a quarter of traffic; a 30 minute call is a high-commitment ask that legitimately needs the argument, so cutting the argument is the wrong move. Then: move a CTA above section 4 and repeat it, keep the long argument for the people who scroll, and mark the branded 30 percent as a separate case where the full argument is probably redundant. Whether the mid-page CTA lifts bookings is a hypothesis to test, and section-level cut decisions need per-section engagement data that was not supplied.

## Guardrails

- Do not set a word count target.
- Do not change the live page or run the test.
- Do not quote industry benchmarks for page length.
- Mark the traffic split as an assumption whenever it was not supplied.
