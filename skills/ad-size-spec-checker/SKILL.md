---
name: ad-size-spec-checker
description: Checks an image's pixel dimensions against the standard ad size specs for Meta, Google Display, LinkedIn, and other major platforms, flagging the exact placement it matches or fails to match.
---

# Ad Size Spec Checker

## When to Use

Before uploading ad creative to a platform, or when a rejected/misrendered ad needs a quick dimension diagnosis.

## How It Works

Run the bundled script against an image file. It compares the pixel dimensions to a built-in table of standard placements (Meta feed 1:1/4:5, Stories/Reels 9:16, Google Display IAB sizes, LinkedIn single image/document) and reports every placement it matches exactly.

```bash
node skills/ad-size-spec-checker/scripts/check-ad-size.js path/to/creative.png
```

## Examples

- "Which ad placements does this 1080x1080 image actually fit?"
- "Our display ad got rejected — check if the dimensions match a standard IAB size"
- "Validate this creative before we upload it to Meta Ads Manager"
