---
name: accessibility-conversion-blocker-check
description: Finds the accessibility defects that also block conversion: unreadable contrast, tap targets too small to hit, form fields with no label, and error states nobody can perceive. Use when a page is being shipped, when mobile form completion is poor, or when an audit flagged accessibility and nobody knows which items matter commercially.
---

# Accessibility Conversion Blocker Check

This skill ships a deterministic helper next to it: `contrast_check.py`. Run it rather than judging contrast by eye. Eyes adapt; ratios do not.

Input is one pair per line, pipe separated, size and weight optional:

```text
label | foreground | background | font-size-px | font-weight
Primary button | #ffffff | #86FF1D | 15 | 600
Body copy | #9C9C9C | #151516 | 16 | 300
```

```bash
python3 contrast_check.py pairs.txt
printf 'Button|#ffffff|#86FF1D|15|600\n' | python3 contrast_check.py -
python3 contrast_check.py pairs.txt --level AAA
```

Exit 0 means everything passed, 1 means a pair failed its threshold, 2 means a
line could not be measured and the run is incomplete. Translucent colours and
`hsl()` are rejected on purpose: composite the colour over its background and
supply the opaque result, because discarding alpha is how invisible text passes
a gate at 21:1.

## Use this skill when

- a page is about to ship and nobody has checked contrast, labels or tap targets.
- mobile form completion is poor and the fields look fine on a designer's monitor.
- an accessibility tool produced a long report and the team needs the subset that also costs money today.
- a rebrand introduced a lighter grey, a thinner weight or a new accent colour on buttons.

This is the commercial subset of accessibility work, not a full compliance audit. It does not replace a WCAG audit and does not produce a compliance statement.

## Required input

- foreground and background colour pairs for body copy, secondary copy, button labels, placeholder text, error text and any text over an image.
- font sizes and weights for each of those pairs.
- tap target sizes for buttons, links and form controls on mobile, or a screenshot with known dimensions.
- form markup facts: does each field have a real label, is the label visible after typing, how are errors announced.
- If colours are only available as a screenshot, sample the hex values before running the helper and say the values were sampled rather than supplied.

### If the data does not exist

Nobody has the colour pairs written down. They take five minutes to collect.

- **To get the hex values:** open the page, right-click the element, Inspect, and read `color` and `background-color` from the Computed panel. Chrome shows them as hex when you click the swatch. Copy them straight into `pairs.txt` in the format above.
- **Faster, for a whole page:** in the Console, run something that lists the computed colour, background, size and weight for every text element, and paste the result into `pairs.txt`. Any snippet that reads `getComputedStyle` will do; the helper only needs five fields per line.
- **No tap target sizes:** Inspect the button and read the box dimensions from the Computed panel's box model, or use the device toolbar at a 390px width and read the element's size in the overlay.
- **Only a screenshot:** use a colour picker on the screenshot, and say the values were sampled from an image rather than read from the page, because compression shifts them slightly.
- **Nothing at all:** the structural half of this skill still runs from the markup: whether fields have real labels, whether errors are colour-only, whether the submit is reachable. Report that half and mark contrast as unmeasured.

## Analysis workflow

1. Run `contrast_check.py` on every colour pair with its font size and weight. Record the ratio and the pass or fail against the 4.5 to 1 threshold for normal text and 3 to 1 for large text and interface components.
2. Rank the failures by commercial position: button labels and form text first, error messages next, body copy after that, decorative last.
3. Check placeholder-as-label. A field whose only label is a placeholder loses its label the moment the user types, which produces wrong entries and abandoned forms.
4. Check tap targets against the 44 by 44 point heuristic, and check spacing between adjacent targets. Two correct-sized targets three pixels apart still produce mis-taps.
5. Check error states for perceivability without colour: does the message say what is wrong in words, is it next to the field, does it survive a screen reader reading the field.
6. Check text over images and video for a contrast floor across the whole area the text sits on, not just the darkest corner.
7. Separate defects that block a conversion outright from defects that degrade the experience, and say which is which.

## Decision rules

- Report measured ratios from the helper, never adjectives. "3.1 to 1 against a 4.5 requirement" is a finding; "a bit light" is not.
- Contrast on a button label or form field is a conversion blocker. Contrast on a footer legal line is not. Rank accordingly, and say that both are still accessibility defects.
- Placeholder-only labelling is a blocker, not a preference. It fails perception and it produces bad data.
- Heuristics, labelled as such: 4.5 to 1 for normal text and 3 to 1 for large text come from WCAG 2.1 AA; 44 by 44 points for tap targets is Apple's guidance and 48 by 48 density-independent pixels is Google's. Cite which one you used.
- Do not produce a compliance verdict, a conformance level or a legal opinion. This skill finds defects; conformance is a formal audit with a different scope.
- Do not recommend an accessibility overlay widget as a fix. It does not fix the underlying defects.

## Output format

Start with the helper's measurement table, verbatim.

| Element | Pair | Measured ratio | Requirement | Status | Commercial impact |
|---|---|---|---|---|---|
| Where it appears | Foreground on background | From the helper | 4.5 or 3 to 1, with which rule | Pass / fail | Blocks conversion / degrades / cosmetic |

Then a second table for structure: labels, tap targets, spacing, error perceivability.

End with:

- `Conversion blockers:` the short list that stops a submit today
- `Decision:` fix before ship / fix in the next pass / commission a full audit / ask for values
- `Out of scope:` conformance verdict, legal exposure
- `Missing data:` colour values or sizes that could not be obtained

## Practical example

User: "Buttons are #86FF1D background with white 15px labels. Body copy #9C9C9C on #151516. Placeholder text is the only label on all five form fields. Mobile submit button is 40px tall. Error messages turn the field border red."

Assistant should run the helper, then report: white on that lime measures 1.29 to 1, which fails 4.5 to 1 badly and sits on the single most important element on the page, so the button label is the first fix and dark text on the lime is the change; the grey body copy pair needs its measured ratio quoted rather than eyeballed; placeholder-only labelling on all five fields is a blocker and produces wrong entries as well as failing perception; the 40px submit is under both the 44 point and 48 dp heuristics, so cite which was used; a red border with no text is invisible to anyone not perceiving colour, and the fix is words next to the field. Conversion blockers: button label contrast, five missing labels, colour-only errors. No conformance verdict is given.

## Guardrails

- Do not claim conformance, compliance or legal safety.
- Do not recommend an overlay widget.
- Do not change styles, markup or the live page.
- Say when a colour value was sampled from a screenshot rather than supplied.
