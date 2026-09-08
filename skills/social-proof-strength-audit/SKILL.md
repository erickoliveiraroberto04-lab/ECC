---
name: social-proof-strength-audit
description: Checks whether the proof on the page would convince a sceptic in the reader's own situation, or whether it is decoration. Use when a page has logos and testimonials and still feels unproven, or when proof was inherited from an older version of the business.
---

# Social Proof Strength Audit

## Use this skill when

- testimonials, logos, ratings, case numbers or reviews are present on the page and the team is unsure any of them are doing work.
- the page carries logos and testimonials and still feels unproven.
- the proof was collected years ago, for a product or an audience that has since changed.

This skill judges the proof that exists. To find which objections need proof in the first place, use `objection-map-builder`.

## Required input

- every proof element on the page: testimonials with whatever attribution they carry, logos, ratings, counts, case study links, certifications.
- where each one sits on the page relative to the offer and the ask.
- who the reader is, so proof relevance can be judged rather than proof volume.
- optional: which objection each proof element was meant to answer, if anyone decided that.
- If a claimed number (customers, users, businesses served) has no definition or date, treat it as unverified and say so.

Not for: finding the objections in the first place (`objection-map-builder`), or reviewing security and risk-reversal signals (`trust-signal-audit`).

## Analysis workflow

1. Inventory proof elements: logos, testimonials, case studies, metrics, reviews, screenshots, certifications and named customers.
2. Classify proof by relevance to the ICP, specificity, recency, credibility and proximity to the CTA.
3. Identify proof gaps for the main objection or risk on the page.
4. Flag fake-looking, generic or misaligned proof that may reduce trust.
5. Recommend where to add, move, rewrite or remove proof.

## Decision rules

- Relevance beats volume. One testimonial from the reader's own segment outperforms eight logos from companies they cannot relate to, so rank by resemblance to the reader.
- Attribution is the whole of a testimonial's value. First name only is discounted to zero by a sceptical reader; name, role and company is a claim someone could check.
- A count with no definition and no date is marketing, not proof. Say which of the two is missing.
- Proof placed away from the objection it answers is not doing work. Report position, not just presence.
- Proof above the fold competes with the offer for the first three seconds. That is a trade-off worth naming, not automatically a defect.
- Do not recommend inventing, embellishing or composing a testimonial. If the proof does not exist, the recommendation is to go and get it, and from whom.

## Output format

| Proof element | Attribution | Objection it answers | Position | Resembles the reader | Verdict |
|---|---|---|---|---|---|
| Quoted or named | Full / partial / none | The specific objection or none | Where on the page | Yes / no / unknown | Keep / re-attribute / move / replace / cut |

End with:

- `Strongest proof on the page:` which one, and why
- `Objections with no proof against them:` the list
- `Decision:` re-attribute / move / go and collect specific proof / ask for data
- `Missing data:` definitions and dates behind any claimed number

## Practical example

User: "We have 8 client logos above the fold, three testimonials with first names only, and a line saying Trusted by 500+ businesses."

Assistant should note: first-name-only testimonials carry no verifiable identity, so a sceptical reader discounts them entirely, and the fix is a full name, a role and a company on at least one of them; the 500+ number has no definition of what counts as a business or a date, so it reads as rounded marketing rather than a fact; eight logos above the fold compete with the headline for the first three seconds while telling the visitor nothing about whether those clients resemble them. Then: proof relevance beats proof volume, so the recommendation is one identified testimonial from the reader's own segment placed next to the objection it answers, and the logo wall moved below the offer. Whether that lifts CVR is a hypothesis; no per-section engagement data was supplied.

## Guardrails

- Never draft, embellish or invent a testimonial, a rating or a customer number.
- Do not treat a logo wall as proof of results. It is proof of a relationship.
- Do not claim a lift from a proof change.
- Mark undefined and undated numbers as unverified rather than softening them.
