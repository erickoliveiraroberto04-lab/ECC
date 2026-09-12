---
name: og-image-validator
description: Validates an Open Graph / Twitter Card image's dimensions and aspect ratio against social platform requirements, so link previews render correctly instead of cropped or blurry.
---

# OG Image Validator

## When to Use

Before shipping a website's `og:image` / `twitter:image`, or when a shared link's preview looks cropped, stretched, or missing entirely on social platforms.

## How It Works

Run the bundled script against a local image file. It reads the actual pixel dimensions and checks them against the recommended specs for Open Graph (1200x630, 1.91:1) and Twitter Card (1200x600, 2:1 for summary_large_image), flagging undersized images, wrong aspect ratios, and file sizes likely to be rejected or slow to fetch.

```bash
node skills/og-image-validator/scripts/check-og-image.js path/to/image.png
```

Output reports actual dimensions, computed aspect ratio, a pass/fail against each platform's recommendation, and file size in KB.

## Examples

- "Check if our social-share.png will render correctly as a link preview"
- "Our Twitter card image looks cropped — validate the dimensions"
- "Audit the OG image before we ship this landing page"
