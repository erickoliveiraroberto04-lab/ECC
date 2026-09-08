---
name: ad-copy-character-counter
description: Checks ad copy text against the character limits for each major platform's headline/description fields (Google Ads, Meta, LinkedIn), flagging what will be truncated before it ships.
---

# Ad Copy Character Counter

## When to Use

Before finalizing ad copy for any platform, or when an ad preview shows truncated text and the cause needs pinpointing.

## How It Works

Run the bundled script with a `--platform` flag and the copy text (or pipe it via stdin). It reports the character count against that platform's known field limits (headline, description, etc.) and flags anything over.

```bash
node skills/ad-copy-character-counter/scripts/count-ad-copy.js --platform google-headline "Best Running Shoes On Sale Now"
node skills/ad-copy-character-counter/scripts/count-ad-copy.js --list
```

Use `--list` to print every supported platform/field and its limit.

## Examples

- "Check if this Google Ads headline fits within the character limit"
- "What's the character limit for a Meta ad primary text field?"
- "Validate this LinkedIn ad headline before we launch"
