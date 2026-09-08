---
name: utm-link-builder
description: Builds correctly-encoded UTM-tagged campaign URLs from a base URL plus source/medium/campaign parameters, and validates existing UTM URLs for common mistakes (missing params, inconsistent casing, spaces).
---

# UTM Link Builder

## When to Use

Before launching any ad or campaign that needs traceable link attribution, or when auditing a batch of existing campaign links for consistency mistakes.

## How It Works

Run the bundled script in build mode to generate a properly encoded UTM URL, or in check mode to validate an existing one against common mistakes (missing required params, mixed casing between campaigns, unencoded spaces).

```bash
# Build a new UTM URL
node skills/utm-link-builder/scripts/utm.js build "https://example.com/landing" \
  --source facebook --medium cpc --campaign summer_sale

# Validate an existing UTM URL
node skills/utm-link-builder/scripts/utm.js check "https://example.com/landing?utm_source=Facebook&utm_medium=cpc"
```

## Examples

- "Build a UTM link for our Instagram story ad pointing to the new landing page"
- "Check this campaign URL for UTM mistakes before we launch"
- "We have inconsistent casing across our UTM tags — help me spot it"
