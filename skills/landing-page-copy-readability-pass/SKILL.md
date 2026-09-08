---
name: landing-page-copy-readability-pass
description: Measures how hard a landing page is to read and names the exact sentences that slow a visitor down. Use when page copy was written or reviewed by committee, when it is full of category jargon, or before shipping a rewrite.
---

# Landing Page Copy Readability Pass

This skill ships a deterministic helper next to it: `readability_report.py`. Run it rather than estimating sentence length or passive voice by eye.

```bash
python3 readability_report.py page.txt
python3 readability_report.py page.txt --long 30 --mean 18
python3 readability_report.py before.txt --compare after.txt
cat page.txt | python3 readability_report.py -
```

It takes plain text, one file. Exit code 2 means the input could not be read or
contained nothing measurable. Quote its numbers; do not restate them from memory.

## Use this skill when

- the page went through several reviewers and came out longer and vaguer than it started.
- the copy is full of category language that only someone who already works in the category understands.
- a rewrite is about to ship and nobody has checked whether it is actually easier to read than what it replaces.
- bounce is high on a page whose offer and traffic match, which points at the reading experience rather than the promise.

Do not use this skill to judge whether the offer is right. `offer-clarity-diagnosis` owns that. This one is about the mechanics of the sentences.

## Required input

- the full page copy as text: headline, subhead, body, bullets, CTA labels, form labels, footer microcopy.
- who the reader is and how much category knowledge they have on arrival.
- if a rewrite is being compared, both versions.
- If only a screenshot is available, transcribe it before running the helper, and say the transcription is the source.

## Analysis workflow

1. Run `readability_report.py` on the copy to get sentence count, mean and maximum sentence length, long-sentence positions, passive-voice candidates and the word-frequency table. Do not estimate these.
2. Read the headline and subhead alone. Decide whether a reader who knows nothing about the category learns what the thing does. Note the first unexplained term.
3. List every term that requires category knowledge, and mark each as: explained on the page, explainable in three words, or jargon to cut.
4. Find every sentence over the long threshold from the helper output and rewrite the worst three as a demonstration, not as a full rewrite.
5. Check the concrete-to-abstract ratio: count nouns a reader could photograph against nouns they could not. Abstraction concentrated in the hero is the expensive kind.
6. Check the CTA labels and form labels separately. These are the highest-stakes words on the page and they are usually the least reviewed.
7. If two versions were supplied, report both measurements side by side and say which is easier to read on the numbers, independent of which one anyone prefers.

## Decision rules

- **The thresholds are this pack's own defaults and have no external source.** A sentence over 35 words is flagged, a mean over 20 words is flagged, and a hero of more than 3 sentences is worth a look. Say that they are our defaults, not research, whenever you quote one, and defer to a measured comparison between two versions over any absolute number.
- Below 10 sentences the mean is not a stable measurement. The helper refuses to adjudicate it and so should the readout: report the raw counts and say the sample is too small for the mean to mean anything.
- Jargon that the audience uses about itself is not jargon. Jargon the vendor uses about its own category usually is. When in doubt, say which of the two you assumed.
- Do not confuse short with clear. A short sentence that says nothing is a worse defect than a long sentence that says something specific, and should be reported as vagueness rather than length.
- Never recommend a full rewrite as the finding. Name the defect class, demonstrate on the worst three examples, and leave the rest to the writer.
- Readability numbers do not predict conversion. Report them as a diagnosis of the reading experience and mark any conversion claim as a hypothesis.

## Output format

Start with the measurement block from the helper, verbatim.

| Defect | Location | Evidence | Rewrite or fix | Priority |
|---|---|---|---|---|
| Long sentence / jargon / abstraction / weak CTA label | Section and line | Quoted text plus the number from the helper | Demonstrated rewrite or the rule to apply | High / Medium / Low |

End with:

- `Decision:` ship / revise the flagged sections / rewrite the hero / ask for the audience definition
- `Hardest sentence on the page:` quoted, with its word count
- `Missing data:` what would change the verdict, usually the audience's real category knowledge

## Practical example

User pastes a hero: "Our AI-native, full-funnel orchestration layer unifies cross-channel signal into a single source of truth so revenue teams can operationalise decisioning at scale." They mention there are also about 400 words of body copy, but do not paste them.

Assistant should run the helper, then report exactly what it printed: 22 words, 1 sentence, mean 22.0, and no mean verdict, because the helper refuses to adjudicate a mean under 10 sentences and says so. Then the judgement: zero photographable nouns, and the first 6 words require the reader to already know what an orchestration layer is; "signal", "source of truth", "decisioning" and "at scale" are 4 category terms in one sentence, none explained on the page; the reader cannot say what the product does after reading the hero, which is the actual defect, and it is vagueness rather than length.

Then: a demonstrated rewrite of that one sentence. What this refuses to conclude: anything about the 400 words of body copy, which were named but never supplied, so no measurement is reported for them and the hero is the only measured section. The 35-word long-sentence flag it sits under is this pack's own default with no external source, and the assistant should say so rather than implying research.

## Guardrails

- Do not rewrite the whole page unless asked. Demonstrate on the worst examples.
- Do not claim a readability score predicts revenue.
- Do not flag a term as jargon without saying who the assumed audience is.
- Report the helper's numbers as measured and everything else as judgment.
