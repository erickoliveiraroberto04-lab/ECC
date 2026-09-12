---
name: lead-form-sales-handoff-check
description: Checks every form field against what sales actually uses to qualify, so the form stops asking for data nobody reads. Use when lead volume is acceptable but sales calls leads unqualified, or when someone wants to add a field to a form.
---

# Lead Form Sales Handoff Check

## Use this skill when

- sales says the leads are weak while marketing says the volume is fine.
- someone proposes adding a field to the form, or removing one, and the argument is opinion against opinion.
- a form has grown field by field over a year and nobody has audited what the extra fields bought.
- the CRM has fields that are populated on every record and referenced in no conversation.

This is not the same job as finding completion friction. `form-friction-finder` asks why people stop filling the form in. This skill asks whether the fields earn their place at all.

## Required input

- the full field list: label, type, required or optional, validation, order.
- how sales actually qualifies: the questions asked on the first call, or the disqualification reasons in the CRM.
- per-field usage evidence if any exists: CRM fill rate, whether the field is used in routing, scoring, sequences or reporting.
- volume and outcome numbers: submissions, meetings booked, disqualification reasons and counts.
- If sales qualification criteria are unavailable, do not fall back on generic form advice. Use the degraded path below.

### If the data does not exist

Most operators do not have per-field CRM usage or a disqualification log, and a founder who sells personally has neither. That is a normal starting point, not a blocker.

- **No disqualification log:** paste the last 10 lost-deal notes, or answer one question from memory: what makes you say no on the first call? Two recurring reasons are enough to run this skill; say the evidence is recall rather than records, and mark every verdict as provisional.
- **No per-field CRM usage:** answer per field, from memory: has anyone read this field in the last month? A field nobody can remember reading is a candidate cut, marked as an assumption rather than a verified one.
- **You are the sales team:** that is the strongest version of this input, not the weakest. Your own qualification criteria are the criteria.
- **Nothing at all:** the output is not a form verdict. It is the request to send: start recording a disqualification reason on every lost deal, then run this again in three weeks.

## Analysis workflow

1. List every field and mark what consumes it downstream: routing, scoring, an automated sequence, a report, a human reading it before the call, or nothing.
2. For each qualification criterion sales uses, find the field that supplies it. Criteria with no field are the real gap.
3. Flag every field consumed by nothing. Those are pure cost: they lengthen the form and buy no decision.
4. Check whether any required field is one a genuine buyer would refuse or fake: phone number for a top-of-funnel asset, company revenue, team size at a founder-run company.
5. Compare the disqualification reasons against the form. A reason that appears often and has no matching field is a field the form should ask for, or a filter that belongs upstream in targeting.
6. Decide per field: keep, make optional, cut, move later in a multi-step flow, or enrich automatically instead of asking.

## Decision rules

- A field consumed by nothing is a cut, not a debate. Say which downstream system was checked and found empty.
- If a qualification criterion has no field and shows up in disqualification reasons, adding that field is the highest-value change on the form, even though it makes the form longer.
- Faked data is worse than missing data. If a required field invites a junk value, recommend optional or enrichment rather than required.
- Do not recommend enrichment as a fix without naming a tool the team already has. Otherwise it is a purchase disguised as a form change.
- If disqualification reasons are not recorded at all, that is the finding. Name it as the first fix and treat every field verdict below it as a hypothesis.
- Volume changes from field changes are hypotheses, not forecasts. No invented percentages.

## Output format

| Field | Consumed by | Sales criterion it serves | Verdict | Reason |
|---|---|---|---|---|
| Exact label | Routing / scoring / sequence / report / human / nothing | The criterion or none | Keep / optional / cut / move / enrich | One sentence |

Then a second table for the other direction:

| Sales criterion | Field that supplies it | Disqualification count | Recommended source |
|---|---|---|---|

End with:

- `Decision:` change the form / change targeting / record disqualification reasons first / ask for data
- `Net field change:` fields before and after, and which single addition matters most
- `Missing data:` only what would change a verdict

## Practical example

User: "Form has 9 fields: name, work email, company, phone required, company size, role, budget range, how did you hear about us, message. 140 submissions last quarter, 22 meetings. Sales disqualifies mostly for 'no paid traffic running' and 'agency, not advertiser'."

Assistant should note: neither disqualification reason has a field, so the form collects nine things and misses the only two that predict a bad fit; "how did you hear about us" is unused unless the team can name the report that reads it; a required phone number on a first-touch form invites junk values and is a friction cost with no matching qualification criterion. Then: the highest-value change is one new field that separates advertiser from agency and one that asks whether paid traffic is live, paid for by cutting or optionalising two unused fields so the form does not get longer. 140 submissions to 22 meetings is a 15.7 percent meeting rate on the supplied numbers; whether the new fields raise it is a hypothesis to measure, not a forecast.

## Guardrails

- Do not edit forms, CRM fields, routing rules or automations.
- Do not recommend buying an enrichment tool as the default fix.
- Do not treat a long form as automatically bad. Length is a cost, and some fields are worth it.
- Mark every unverified field verdict as an assumption when downstream usage could not be checked.
