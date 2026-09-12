---
name: paid-traffic-message-match-audit
description: Compares what the ad promised with what the page delivers, element by element, and finds the first point where the visitor's expectation breaks. Use when clicks arrive but bounce is high or lead quality is poor, or after ad copy changed and nobody re-read the page.
---

# Paid Traffic Message Match Audit

## Use this skill when

- an ad and its landing page are both available and CVR, bounce or lead quality suggests the click and the page are telling different stories.
- ad copy was just changed, or a new ad set launched against a page nobody re-read.
- sales says the leads do not resemble what the ads promised.

This skill needs the ad and the page together. With only one of the two, it cannot run.

## Required input

- the ad or ads: headline, primary text, creative description, and the offer as the ad states it.
- the landing page: hero copy, first CTA, form fields, and the offer as the page states it.
- which ad points at which page, when more than one of each exists.
- any of: clicks, bounce rate, CVR, time on page, lead quality feedback from sales.
- If the ad copy is missing, this skill cannot run. Ask for it rather than reviewing the page alone; a page has no message match without the message.

Not for: judging whether the offer itself is any good (`offer-clarity-diagnosis`), or whether the page suits the audience temperature (`traffic-temperature-match-review`).

## Analysis workflow

1. Extract the ad promise, audience, pain, offer, proof, CTA and expected commitment from each ad or campaign.
2. Extract the same elements from the landing page hero, first CTA, form, proof and above-the-fold copy.
3. Score match severity for audience, outcome, mechanism, proof, CTA, pricing expectation and form commitment.
4. Estimate likely consequence: bounce, weak CVR, low-quality leads, form abandonment or sales confusion.
5. Recommend the smallest copy or flow change that restores continuity from click to conversion.

## Diagnostic rubric

Use this table when the user provides an ad and landing page:

| Element | Ad promise | Page promise | Match level | Severity | Fix |
|---|---|---|---|---|---|
| Audience / pain / outcome / mechanism / proof / CTA / form commitment | Exact ad wording or missing-data marker | Exact page wording or screenshot note | Strong / partial / weak / broken | High / Medium / Low | Rewrite, move, remove, test or ask for data |

Then call out:

- First mismatch: the earliest point where the visitor expectation changes.
- Conversion consequence: likely bounce, weak CVR, low lead quality, form abandonment or sales confusion.
- Smallest fix: the lowest-effort page or ad change that restores continuity.

## Decision rules

- The first mismatch outranks every later one. A visitor who loses the thread above the fold never reaches the mismatch in section four, so fix in page order, not in severity order.
- Audience, outcome and mechanism are the three that matter. A wording difference that preserves all three is a polish item; a change to any one of them is a break.
- If the ad promises a lighter commitment than the page asks for (free audit in the ad, budget field on the form), that is a break even when every word matches.
- Do not attribute low lead quality to message match without downstream data. A page can match its ad perfectly and attract the wrong people, which is a targeting finding, not a page finding.
- If several ads point at one page, report per ad. One page can match one ad and break three others, and the aggregate hides it.
- Never recommend rewriting the ad and the page at once. Name which side is wrong, and say what evidence made you pick that side.

## Output format

| Element | Ad says | Page says | Match | Position | Consequence |
|---|---|---|---|---|---|
| Audience / outcome / mechanism / proof / CTA / commitment | Exact ad wording | Exact page wording or missing-data marker | Strong / partial / broken | Where on the page it happens | Bounce / weak CVR / wrong-fit leads / form abandonment |

End with:

- `First mismatch:` the earliest break, quoted from both sides
- `Which side is wrong:` ad or page, and the evidence for choosing
- `Smallest fix:` the one change that restores continuity
- `Decision:` fix the page / fix the ad / test / ask for data
- `Missing data:` only inputs that would change which side is wrong

## Practical example

User: "Ad headline says Cut your Google Ads waste in 14 days, free audit. The page headline says The complete performance marketing platform for modern teams. 2100 clicks, 1.1 percent CVR, bounce 74 percent. Form asks for company size and budget."

Assistant should note: the ad promises a specific outcome with a time frame and a free audit, and the page opens with a category statement that names no outcome, so the first mismatch happens above the fold, before any other element gets a chance; the ad's commitment is a free audit while the form asks for budget, which is a heavier commitment than the click was sold on; audience and mechanism are unstated on the page, so a visitor cannot confirm they are in the right place. Then: 74 percent bounce with 1.1 percent CVR on message-match evidence this clear points at the hero as the first fix, and the smallest change is putting the ad's promise in the page headline verbatim before touching anything else. Lead quality cannot be assessed without downstream data, so it stays marked as missing.

## Guardrails

- Do not edit ads, pages or campaigns.
- Do not review a page for message match without the ad copy.
- Do not blame message match for lead quality without downstream evidence.
- Quote both sides verbatim. A paraphrased mismatch is unverifiable.
