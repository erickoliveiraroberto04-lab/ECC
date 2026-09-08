---
name: comparison-page-positioning-review
description: Reviews a "versus competitor" or alternatives page for claims that will not survive contact with the competitor's own page. Use when a comparison page is being written, when it ranks but does not convert, or when a competitor changed their pricing or feature set.
---

# Comparison Page Positioning Review

## Use this skill when

- a comparison or alternatives page is being drafted and someone needs to sanity-check the claims before it goes public.
- the page ranks for "competitor alternative" queries, gets traffic, and converts worse than the plain product page.
- a competitor changed pricing, packaging or a feature and nobody re-read the comparison table.
- sales gets pushback on a call that quotes the comparison page back at them.

Do not use this skill for message match against your own ads. `paid-traffic-message-match-audit` owns that.

## Required input

- the comparison page: table rows, claim wording, the verdict copy, CTAs.
- the competitor's current public pricing and feature pages, or pasted excerpts, with the date they were checked.
- who arrives on this page: someone already using the competitor, someone shortlisting both, or someone who has only heard of the competitor.
- conversion data if available: sessions, CTA clicks, trials or demos from this page, and the same numbers for the main product page.
- Every competitor claim needs a dated source. If a claim has no source, it is marked unverified and cannot ship.

## Analysis workflow

1. For each row in the table, classify the claim: verifiable from the competitor's public page, verifiable only from private testing, or opinion.
2. Check every verifiable claim against the competitor's live page and record the date. Flag anything that has changed since the page was written.
3. Find the rows where the competitor genuinely wins. A page with no honest losses reads as marketing and loses the reader who has used both.
4. Read the page as the competitor's current customer. Note the first sentence that would make them close the tab, usually an insult to a decision they already made.
5. Check that the page names the segment each product suits, instead of declaring a universal winner. The reader is trying to place themselves, not settle an argument.
6. Check legal and reputational exposure: trademark use, comparative claims stated as fact without a source, and any performance number attributed to the competitor without a citation.
7. Compare conversion against the main product page. A comparison page that converts worse is usually asking for the wrong next step for a reader still shortlisting.

## Decision rules

- An unsourced competitor claim does not ship. Replace it with a sourced narrower claim or cut the row.
- A dated source is part of the claim. "As of the date checked" belongs on the page, because the competitor will change it and the page will be wrong silently.
- If the page has no row where the competitor wins, that is the finding. Recommend adding the truest one, and say which segment it makes the competitor right for.
- Do not recommend claiming a feature the product does not have yet. Roadmap language on a comparison page is the fastest way to a refund conversation.
- If the reader is a current competitor customer, a hard trial or purchase CTA is likely wrong. Recommend the lower-commitment step and mark the lift as a hypothesis.
- Never restate a competitor's pricing without the currency, the billing basis and the date. That is where these pages get sued or ridiculed.

## Output format

| Row or claim | Type | Source and date | Status | Recommended wording |
|---|---|---|---|---|
| The claim as written | Public / private test / opinion | URL or pasted excerpt plus date, or none | Verified / stale / unverified / cut | Narrower true version |

Then:

- `Where the competitor genuinely wins:` the honest list, with the segment each applies to
- `Exposure:` claims stated as fact without a source, trademark issues, uncited numbers

End with:

- `Decision:` ship / fix the flagged rows first / do not ship / ask for sources
- `Missing data:` what would change the verdict

## Practical example

User: "Our alternatives page says: they charge 3x more, their onboarding takes months, and they have no API. We rank position 4 for their brand plus alternative, 300 sessions a month, 2 trials. Product page converts 4 percent."

Assistant should note: "3x more" needs the plan pair, the billing basis and a date, otherwise it is unverifiable and changes the moment they discount; "onboarding takes months" is opinion unless it comes from their own documentation or a sourced customer statement; "no API" is checkable in one minute and is the kind of claim that goes stale silently, so it needs a date on the page. The page has no row where the competitor wins, which is why a reader who already uses them closes the tab. Then: 2 trials from 300 sessions is too small a numerator to carry a rate, so it is reported as a small sample and not as 0.67 percent; the direction against the product page's 4 percent is still worth acting on, and it suggests the CTA asks for too much from a reader still shortlisting. A comparison-appropriate next step is the recommendation, marked as a hypothesis on a small sample. The three claims do not ship in their current wording.

## Guardrails

- Do not publish or edit the live page.
- Do not state a competitor claim without a dated source.
- Do not recommend claiming unbuilt features.
- Mark any claim that could not be verified as unverified rather than softening it into a hedge.
