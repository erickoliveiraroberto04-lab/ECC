---
name: form-friction-finder
description: Finds the fields, validation rules, error states and steps that stop people finishing a form they intended to finish. Use when form starts are healthy and submits are not, or when a field was added and completion dropped.
---

# Form Friction Finder

## Use this skill when

- the form's fields, validation behaviour and step structure are available, and starts exceed submits by more than the team can explain.
- a field, a validation rule or a step was added and completion dropped.
- people submit the form with obviously fake values in one particular field.

This skill asks why people stop filling a form in. Whether a field should exist at all belongs to `lead-form-sales-handoff-check`.

## Required input

- the full field list with types, required flags, validation rules and order.
- the step structure: one page, multi-step, progressive, and what the progress indicator says.
- error behaviour: when errors appear, where, and what they say.
- numbers if they exist: form starts, submits, per-field drop-off, time to complete, device split.
- If starts and submits are both unavailable, say the ranking is structural rather than measured. The defects are still real; their order is not established.

### If the data does not exist

- **No form starts:** GA4 fires `form_start` and `form_submit` automatically for many forms under enhanced measurement. Reports, then Engagement, then Events. If they are there, you have both numbers already and did not know it.
- **If they are not:** the manual version is to fill the form yourself on a phone, wrongly on purpose. Submit with a blank required field, a locally formatted phone number, a plus-address email. Most of what this skill finds surfaces in that one pass, and it needs no analytics at all.
- **No per-field drop-off:** almost nobody has this. Say the ranking is structural and name the two candidates you would test first rather than pretending to an order you cannot see.
- **No device split on the form:** test it on a phone anyway. Form defects concentrate there.

Not for: whether a field should exist at all (`lead-form-sales-handoff-check`), or the hesitation right before submitting (`trust-signal-audit`).

## Analysis workflow

1. List fields, steps, required answers, validation, hidden fields, consent copy and submission behavior.
2. Classify each field as essential, qualification, routing, compliance or nice-to-have.
3. Compare friction level with traffic intent, offer value and buyer stage.
4. Check mobile input types, dropdown length, error messages, field order and visible privacy cues.
5. Recommend remove, reorder, make optional, split, prefill or explain fields.

## Decision rules

- Everyone who started intended to finish. Treat the gap between starts and submits as mechanics, not motivation, and look for the mechanical cause.
- Validation that rejects a correctly typed real value is the highest-severity class in this skill. A phone rule that refuses a locally formatted number fails the most common way a person types their own number.
- Errors surfaced only on submit, plus a scroll away from the field, is the most abandonment-heavy pattern there is. Rank it above field count every time.
- A placeholder is not a label. It disappears when typing starts, which produces wrong entries as well as abandonment.
- Field count matters less than field cost. One field asking for something the visitor must go and look up costs more than three they can answer from memory.
- Per-field drop-off data outranks every heuristic here. When it exists, rank by it and say so; when it does not, say the ranking is structural.
- Do not recommend a multi-step redesign as the first fix. It is a rebuild, and the cheap fixes usually have not been tried.

## Output format

| Field or behaviour | Defect class | Evidence | Severity | Fix |
|---|---|---|---|---|
| Field name or the rule | Validation / labelling / error handling / cost to answer / order | Quoted rule, number, or missing-data marker | High / medium / low | The smallest change |

End with:

- `Largest single defect:` which one, and what it is estimated to cost, or "cannot rank without per-field data"
- `Cheap fixes:` the ones deployable this week
- `Decision:` fix validation / fix error handling / add labels / reorder / ask for per-field data
- `Missing data:` what would turn the structural ranking into a measured one

## Practical example

User: "Form starts 610, submits 190. Fields: name, email, phone, company, website, how can we help. Phone validation rejects anything without a country code. Errors appear only after pressing submit and the page scrolls back to the top."

Assistant should note: 190 of 610 finishing means 420 people decided to fill this in and then stopped, which is a mechanics problem rather than an intent problem; validation that rejects a locally formatted phone number fails the most common way a person types their own number, and it fails silently until submit; errors surfacing only on submit, combined with a scroll to the top, means the user loses their place and has to hunt for what broke, which is the single most abandonment-heavy pattern in the list. Then: inline validation at field level and accepting local phone formats are the two fixes that address the largest share, and the field count question is secondary to them. The per-field drop-off data that would rank fields properly was not supplied.

## Guardrails

- Do not edit the form, validation rules or the CRM.
- Do not recommend a multi-step rebuild before the cheap fixes.
- Do not claim a completion-rate lift.
- Say when the severity ranking is structural rather than measured.
