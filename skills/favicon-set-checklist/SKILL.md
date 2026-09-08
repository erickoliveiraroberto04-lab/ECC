---
name: favicon-set-checklist
description: Generates the complete checklist of favicon/app-icon files, sizes, and the head markup a website needs for correct display across browsers, iOS home screen, Android, and Windows tiles.
---

# Favicon Set Checklist

## When to Use

When setting up a new website's favicon/app-icon files, or auditing an existing site whose icon looks wrong on a phone home screen or browser tab.

## How It Works

Run the bundled script to print the full list of required files, their exact pixel sizes, and the corresponding `<link>`/`<meta>` tags to place in the document head. No image generation is performed — this is a checklist/spec generator, not an image resizer.

```bash
node skills/favicon-set-checklist/scripts/print-favicon-checklist.js
```

## Examples

- "What favicon sizes do I actually need for a modern website?"
- "Generate the head markup for our favicon files"
- "Our app icon looks wrong on iPhone home screen — what size are we missing?"
