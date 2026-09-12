---
name: alt-text-coverage-checker
description: Scans an HTML file for <img> tags and reports which are missing alt attributes, have empty alt text, or use likely-placeholder alt text (filename, "image", "photo"), for accessibility and SEO review.
---

# Alt Text Coverage Checker

## When to Use

Before an accessibility audit, or when reviewing a page's images for both screen-reader support and image SEO.

## How It Works

Run the bundled script against an `.html` file. It finds every `<img>` tag, checks for a missing `alt` attribute, an empty `alt=""` (valid only for decorative images, flagged for review either way), and low-quality alt text that just repeats the filename or uses a generic placeholder word.

```bash
node skills/alt-text-coverage-checker/scripts/check-alt-text.js path/to/page.html
```

## Examples

- "Check this page for images missing alt text"
- "Audit our HTML for placeholder or low-quality alt attributes"
- "How many images on this page have no alt text at all?"
