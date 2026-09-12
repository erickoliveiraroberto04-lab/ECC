---
name: objection-map-builder
description: Pulls the real objections out of reviews, sales notes, support tickets and ad comments, then maps each one to the place on the page where it should be answered. Use when a page rewrite is being planned, or when the team is guessing at what stops people buying.
---

# Objection Map Builder

## Use this skill when

- raw customer language is available in any form: reviews, tickets, sales call notes, ad comments, lost-deal reasons, survey answers.
- the team is guessing at what stops people buying, and the guesses disagree.
- reviews, tickets or ad comments have piled up and nobody has read them as a set.

This skill reads customer language. Without verbatims it produces a list of sources to pull, not a map.

## Required input

- raw customer language, in any form: reviews, support tickets, sales call notes, ad comments, lost-deal reasons, survey answers, chat transcripts, subreddit threads about the category.
- roughly how many items were supplied, and over what period.
- the page, so each objection can be mapped to where it should be answered.
- optional: which objections the team believes matter, so belief can be compared against evidence.
- **With no customer verbatims, do not produce an objection map.** Produce the list of sources to pull first, in priority order, and stop. An objection map invented from the page is the team's assumptions with a table around them.

### If the data does not exist

No reviews and no disqualification log is common, and it does not have to be a dead end. What it rules out is inventing the map; what it leaves is collecting a thin one today.

Sources in order of how fast they produce usable language:

1. **Your own sent folder.** Search your replies for question marks. The questions you have answered more than twice are objections, in the prospect's own words, and you already have them.
2. **The last five sales calls, from memory, written down in the prospect's phrasing rather than yours.** Five is a small sample; say so and use it anyway.
3. **Comments and DMs on any ad or post about this product.** Even 20 comments beat a guess.
4. **Competitor reviews.** G2, Capterra, Trustpilot, the app stores, or a subreddit for the category. These are objections about the category rather than about you, which is a documented limitation to state in the output.
5. **A one-question email to ten recent lost prospects:** what made you decide against it? Two replies is enough to start.

If none of the five is available today, the honest output is that list, ordered, with the note that the map cannot be built from the page alone. Do not produce a table of assumed objections.

Not for: judging the proof already on the page (`social-proof-strength-audit`), or reviewing trust and risk-reversal signals (`trust-signal-audit`).

## Analysis workflow

1. List objections implied by the offer, price, effort, risk, switching cost, trust and implementation.
2. Mine page copy, FAQs, sales notes, comments or reviews for repeated objections.
3. Map each objection to the section that should answer it: hero, proof, FAQ, form, CTA or follow-up.
4. Flag unanswered objections that block conversion before form submit.
5. Recommend copy, proof or FAQ additions ranked by conversion impact.

## Decision rules

- Preserve the customer's wording. Paraphrasing an objection into marketing language is how it stops being usable as page copy.
- Separate objections by type: function, risk, price, payback, timing, internal politics. Pages routinely answer the function objections and ignore the other five.
- Frequency ranks the list, but say the sample size next to it. Four mentions out of 40 items and out of 4000 items are different findings.
- An objection that appears in lost-deal reasons outranks one that appears in comments. Proximity to money is the tiebreaker.
- Map each objection to a specific place on the page. An objection with no location is a note, not a recommendation.
- Do not merge two objections because they sound similar. "Does it work with Shopify" and "will this break my checkout" have different answers.
- If the team's believed objections do not appear in the evidence, say so plainly and name what does appear instead.

## Output format

| Objection, in the customer's words | Type | Mentions / sample | Source | Where it should be answered | Currently answered |
|---|---|---|---|---|---|
| Verbatim quote | Function / risk / price / payback / timing / politics | e.g. 7 of 52 | Reviews / tickets / calls / comments / lost deals | Named page section | Yes / no / partially |

End with:

- `Objections the page never answers:` the list, ranked
- `Believed but not evidenced:` what the team expected that the data does not show
- `Decision:` add sections / rewrite a section / pull more sources first
- `Sample caveat:` the total item count and what it does and does not support

## Practical example

User pastes 40 ad comments and 12 lost-deal reasons. Recurring items: does this work with Shopify, is my data used for training, how long until it pays back, we already have someone doing this.

Assistant should note: four distinct objections appear, and only one of them is about the product's function while three are about risk, payback and internal politics, which is where the page currently says nothing; the data-training question is a trust objection that belongs above the form, not in a privacy policy link, because it is asked before anyone submits; we already have someone doing this is a positioning objection and no page section answers it today. Then: each objection is mapped to the section that should carry it, with the exact customer wording preserved rather than paraphrased into marketing language. Frequency counts come from 52 supplied items, which is a small sample, so ranking by frequency is directional rather than reliable.

## Guardrails

- Do not build an objection map without customer verbatims.
- Do not paraphrase objections into brand voice.
- Do not invent a quote, a frequency or a source.
- Say the sample size every time a frequency is reported.
