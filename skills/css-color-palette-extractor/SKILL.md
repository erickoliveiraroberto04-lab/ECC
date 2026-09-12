---
name: css-color-palette-extractor
description: Scans a CSS file and lists every distinct color value used (hex, rgb, hsl, named), surfacing near-duplicate colors that should probably be a single token.
---

# CSS Color Palette Extractor

## When to Use

When auditing a stylesheet for color consistency, or before consolidating raw color values into design tokens/CSS custom properties.

## How It Works

Run the bundled script against a `.css` file. It extracts every hex, `rgb()`/`rgba()`, `hsl()`/`hsla()`, and CSS named color it finds, deduplicates them, and flags hex values that are visually near-identical (small numeric distance) and likely accidental duplicates.

```bash
node skills/css-color-palette-extractor/scripts/extract-palette.js path/to/styles.css
```

## Examples

- "Extract every color used in this stylesheet so we can build a token system"
- "Find near-duplicate colors in our CSS that should probably be one token"
- "Audit this file — how many distinct colors are actually in use?"
