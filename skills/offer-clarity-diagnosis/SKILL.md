---
name: offer-clarity-diagnosis
description: Tests whether the offer on the page is specific enough to be believed and acted on, or whether it is a category description wearing an offer's clothes. Use when traffic and message match are fine but the page still does not convert.
---

# Offer Clarity Diagnosis

## Use this skill when

- the page copy is available and the team suspects the problem is what is being offered rather than how the page looks.
- the copy was written by committee and every reviewer added a qualifier.
- the page reads like a description of a category rather than a thing you can buy.

Run message match first. An unclear offer and a mismatched offer look identical in the data and have opposite fixes.

## Required input

- the offer as the page states it: headline, subhead, the benefit copy, and what the visitor gets.
- the price or the commitment, if the page names one.
- who the offer is for, as the page says it, not as the team knows it internally.
- optional: CVR, and whether message match against the ad has already been ruled out.
- If message match has not been checked, run that first. An unclear offer and a mismatched offer look identical in the conversion data and have opposite fixes.

Not for: comparing ad to page (`paid-traffic-message-match-audit`), or measuring how the copy reads (`landing-page-copy-readability-pass`).

## Analysis workflow

1. Write the offer in one sentence: who gets what outcome, by what mechanism, with what commitment.
2. Check whether the page explains deliverable, timeline, eligibility, cost/risk cue and next step.
3. Identify missing specifics that make visitors unable to decide if the offer is for them.
4. Separate offer confusion from copy style, proof weakness and form friction.
5. Recommend stronger offer framing or proof needed to make the offer believable.

## Decision rules

- An offer that cannot be disbelieved cannot be believed. If no sentence on the page could be proven wrong, that is the finding.
- Test every noun for falsifiability. "Scale profitably with data-driven creative" survives being said about any competitor, which means it says nothing.
- A named audience beats an adjective. "For agencies running under 50k a month" is an offer; "for ambitious brands" is a mood.
- Count the photographable nouns in the hero. Abstraction concentrated where the visitor decides is the expensive kind.
- A booking, a call or a session is a cost to the visitor, not a benefit. If the only concrete thing on the page is the ask, say so.
- Do not propose a new offer. Diagnose the stated one and name the specific vagueness. Inventing an offer is a business decision, not a page fix.

## Output format

| Claim on the page | Falsifiable | Names an audience | Carries a number or mechanism | Verdict |
|---|---|---|---|---|
| Quoted sentence | Yes / no | Yes / no | Yes / no | Specific / vague / interchangeable |

End with:

- `Would this survive a competitor's name swapped in:` yes or no, with the sentence that proves it
- `The one concrete thing on the page:` quoted, or none
- `Decision:` sharpen the offer / test a specific variant / check message match first / ask for data
- `Missing data:` what would change the diagnosis, usually the real audience definition

## Practical example

User: "Copy reads: We help ambitious brands scale profitably with data-driven creative and full-funnel media buying. Book a strategy session. 1400 sessions, 0.6 percent CVR, message match with the ad is fine."

Assistant should note: every noun in that sentence is unfalsifiable, so the offer cannot be disbelieved and therefore cannot be believed either; there is no named audience, no mechanism a reader could repeat back, no time frame and no risk reversal, which leaves a strategy session as the only concrete thing on the page; a strategy session is a cost to the visitor, not a benefit, so the page asks for time and offers a category. Then: with message match already ruled out, the offer is the live hypothesis for 0.6 percent, and the smallest test is one specific outcome for one named audience with a number attached. Whether specificity lifts CVR is a hypothesis, and it needs the current baseline held for comparison.

## Guardrails

- Do not invent a new offer, price or positioning.
- Do not confuse vague with short. Report vagueness, not length.
- Do not diagnose the offer before message match has been ruled out; say so if it has not.
- Quote the page. An unquoted vagueness finding is an opinion.
