---
name: pricing-page-clarity-review
description: Reviews whether a pricing page lets a visitor pick a plan without contacting anyone. Use when paid traffic reaches a pricing page and visitors read it, scroll it, then leave without starting a trial, a checkout or a demo request.
---

# Pricing Page Clarity Review

## Use this skill when

- the pricing page gets traffic and scroll depth but almost no plan selections, trial starts or checkout starts.
- sales keeps answering the same pricing question that the page was supposed to answer.
- a plan was renamed, repackaged or repriced and nobody checked whether the page still tells a coherent story.
- the page hides the number behind "Contact us" and the team is unsure whether that is costing more than it protects.

Do not use this skill to set prices or to judge whether a price is too high. It reviews whether the page communicates the price it already has.

## Required input

- the pricing page URL, screenshot or pasted copy: plan names, prices, billing periods, feature lists, footnotes.
- what a visitor has to decide: which plan, whether to talk to sales, whether to start free.
- any behavioural data available: sessions, scroll depth, clicks per plan, trial or checkout starts, drop-off after the page.
- the actual sales motion: self-serve, sales-assisted, or both, and the real average deal size if it exists.
- If the sales motion is unknown, mark it as an assumption. The same page is correct for self-serve and wrong for sales-assisted.

### If the data does not exist

Per-plan click data is nice and this skill's main findings do not need it.

- **No per-plan clicks:** the blockers this skill finds are read off the page, not the analytics: a price with no basis, a mandatory fee in a footnote, two plans nobody can tell apart. Run it without the data and say the choice-load question stays unexamined.
- **If you want the clicks:** GA4 will not have them unless someone tagged the plan buttons. The cheap version is a heatmap tool's click map, or giving each plan button a distinct link and reading the destination page's traffic.
- **No trial or checkout starts:** count them by hand from your billing tool for one month. A count is enough; a rate is not needed to find these defects.
- **Nothing at all:** run it on the copy alone. This is one of the skills that works fully from a paste.

## Analysis workflow

1. Read the page as a first-time visitor with a budget and a deadline. Write down the first question you cannot answer from the page alone.
2. Count the decisions the page asks for: number of plans, number of billing toggles, number of add-ons, number of CTAs. Report the count. Three per screen is this pack's own working ceiling, not a researched threshold, so quote the count and say the ceiling is ours.
3. Check every price for the four things that make a number unusable: currency, billing period, seat or usage basis, and what happens when you exceed it.
4. List every cost that appears only in a footnote, a tooltip, an asterisk or a link: setup fees, minimum terms, overage, onboarding, mandatory add-ons.
5. Test plan differentiation: for each adjacent pair of plans, name in one sentence who should pick the cheaper one. If you cannot, the pair is not differentiated.
6. Map each plan to a visitor the page has already described elsewhere. A plan with no matching visitor is a plan nobody selects.
7. Decide whether hiding a price is protecting a negotiation or blocking a self-serve buyer, using the stated sales motion, not preference.

## Decision rules

- If a price has no billing period or seat basis next to it, treat that as a blocker, not a polish item. A number a visitor cannot multiply is not a price.
- If adjacent plans cannot be told apart in one sentence, the fix is the plan boundary, not the copy.
- If a mandatory cost appears only in a footnote, treat it as a trust defect: the visitor finds out later, and later is on a sales call or a refund request.
- If the page offers more than three plans plus add-ons and the motion is self-serve, choice load is a live hypothesis for the drop-off. The three is our own working ceiling, not a researched number. Say hypothesis, not cause, unless there is per-plan click data.
- If "Contact us" replaces every number and the average deal is small enough to close self-serve, name the mismatch. If the deal genuinely needs negotiation, leave it alone and say so.
- Never recommend a price change. Recommend a clarity change and mark anything about the level of the price as out of scope.

## Output format

| Finding | Page evidence | What the visitor cannot decide | Recommended change | Confidence |
|---|---|---|---|---|
| Specific clarity defect | Exact wording, screenshot note or missing-data marker | The decision that stalls | Smallest copy, layout or packaging change | High / Medium / Low |

End with:

- `Decision:` fix now / test / leave as is / ask for data
- `Blockers:` the defects that stop a plan choice outright, separated from polish
- `Missing data:` only inputs that would change the recommendation

## Practical example

User: "Paid search sends 900 sessions a month to our pricing page. Scroll depth is fine, 71 percent reach the plan table. Trial starts from that page: 4. Here is the copy: Starter 29, Growth 79, Scale 199, Enterprise Contact us. Toggle for monthly and annual. Footnote says onboarding from 500."

Assistant should note: no seat or usage basis on any of the three numbers, so a visitor cannot work out what they will actually pay; a mandatory 500 onboarding fee sits in a footnote while the headline says 29, which is the trust defect that shows up on the sales call; Starter and Growth have no one-sentence separation in the supplied copy, so the pair is undifferentiated. Then: 71 percent reaching the table with 4 trial starts is a decision problem, not an attention problem, and the smallest fix is putting the basis next to each number and pulling the onboarding fee up into the table. Choice load across four tiers stays a hypothesis, because no per-plan click data was supplied.

## Guardrails

- Do not recommend a specific price, discount or margin change.
- Do not change the live page, the billing configuration or the plan structure.
- Do not claim a conversion lift number. Name the defect and the decision it blocks.
- Mark missing behavioural data clearly instead of inferring intent from a screenshot.
