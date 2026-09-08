---
name: hero-section-diagnosis
description: Reads the headline, subhead, visual and primary CTA as one unit and finds where they contradict each other. Use when each hero element looks fine alone but the section as a whole does not land, or before a hero rewrite ships.
---

# Hero Section Diagnosis

## Use this skill when

- the hero elements are all available and the section reads as four separate decisions rather than one argument.
- each hero element looks fine reviewed alone, and the section still does not land.
- the headline and the subhead appear to be speaking to two different people.

This skill reads the four hero elements as one argument. For what is visible without scrolling, use `above-the-fold-clarity-review`.

## Required input

- all four hero elements together: headline, subhead, visual, primary CTA. Partial input produces a partial review, and this skill is specifically about the interaction between them.
- what the product does, in the team's own words, so the hero can be checked against it.
- who the hero is meant to address.
- optional: any variant of the hero that has run before, and how it performed.
- If the visual is described rather than supplied, say the visual findings are based on a description.

Not for: what is visible without scrolling (`above-the-fold-clarity-review`), or whether the offer is specific (`offer-clarity-diagnosis`).

## Analysis workflow

1. Assess headline, subheadline, primary CTA, visual, proof cue and form entry point as one decision unit.
2. Check whether the hero matches traffic intent and buyer stage.
3. Flag hero failures: vague headline, no concrete outcome, weak proof, no audience cue, buried CTA or visual noise.
4. Compare hero promise with downstream section content and form commitment.
5. Recommend a revised hero structure with exact message roles for each element.

## Decision rules

- The four elements have to support one argument. Name the argument each one makes; where two differ, that is the finding.
- An audience change between headline and subhead is the most common and most expensive contradiction. Check it first.
- The CTA has to match the buying motion the copy implies. "Get started free" under enterprise-grade language is a contradiction, not a preference.
- A visual that carries no information about the product wastes the largest element in the section. Say what it currently communicates, which is often nothing.
- Do not rank these findings by conversion impact without data. Say the ranking is judgement when it is.
- Never rewrite all four at once. Name which single element is off-argument, and fix that one.

## Output format

| Element | The argument it makes | Audience it addresses | Agrees with the others |
|---|---|---|---|
| Headline / subhead / visual / CTA | One line | Named audience | Yes, or which element it contradicts |

End with:

- `The section's actual argument:` one sentence, or "three different arguments" with the list
- `The off-argument element:` which one, and why it was chosen
- `Decision:` rewrite one element / choose the audience first / test / ask for data
- `Missing data:` what would move the ranking from judgement to measurement

## Practical example

User: "Headline: Stop guessing which ads work. Subhead: Enterprise-grade attribution infrastructure for modern data teams. Visual: a stock photo of a smiling team in an office. CTA: Get started free. This hero has been live 5 months and was never tested against anything."

Assistant should note: the headline speaks to an operator's frustration and the subhead speaks to a data team's procurement, so the section changes audience between line 1 and line 2; the visual carries no information about the product and could sit on any page in any category, which wastes the largest of the 4 elements; Get started free promises self-serve while enterprise-grade infrastructure implies a sales process, so the CTA and the subhead disagree about how buying works. Four elements, three different arguments.

Then: the fix is choosing which audience the hero addresses before rewriting a word, and the off-argument element is the subhead, because the headline and the CTA already agree on a self-serve operator. What this cannot conclude is the size of the cost, because 5 months live with no test and no conversion data supplied means there is no baseline to compare against; the ranking of the three defects is judgement, stated as judgement.

## Guardrails

- Do not rewrite the whole hero unless asked.
- Do not judge a visual from a description without saying so.
- Do not use taste language about the visual. Say what it communicates.
- Do not claim a conversion impact for a hero change.
