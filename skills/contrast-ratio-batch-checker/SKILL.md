---
name: contrast-ratio-batch-checker
description: Checks WCAG color contrast ratios for a batch of foreground/background color pairs at once, reporting pass/fail against AA and AAA thresholds for normal and large text.
---

# Contrast Ratio Batch Checker

## When to Use

When auditing a design system's text/background color combinations for accessibility compliance, especially across many pairs at once (e.g. every button variant, every text-on-surface combination).

## How It Works

Run the bundled script with a JSON file (or inline pairs) describing foreground/background hex color pairs. It computes the WCAG relative-luminance contrast ratio for each pair and reports pass/fail against AA (4.5:1 normal text, 3:1 large text) and AAA (7:1 normal text, 4.5:1 large text) thresholds.

```bash
node skills/contrast-ratio-batch-checker/scripts/check-contrast.js path/to/pairs.json
node skills/contrast-ratio-batch-checker/scripts/check-contrast.js --pair "#333333" "#ffffff"
```

`pairs.json` format:

```json
[
  { "name": "body text", "fg": "#333333", "bg": "#ffffff" },
  { "name": "button label", "fg": "#ffffff", "bg": "#2563eb" }
]
```

## Examples

- "Check contrast ratios for every text/background pair in our design tokens"
- "Does this button's white-on-blue combination pass WCAG AA?"
- "Batch-audit our color palette for accessibility compliance"
