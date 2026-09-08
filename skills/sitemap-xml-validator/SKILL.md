---
name: sitemap-xml-validator
description: Validates a local XML sitemap file's structure — well-formed XML, required elements, URL limits, and common mistakes like relative URLs or duplicate entries.
---

# Sitemap XML Validator

## When to Use

Before submitting a sitemap to Google Search Console, or when a sitemap seems to be causing indexing issues.

## How It Works

Run the bundled script against a local `sitemap.xml` file. It checks the file is well-formed XML, uses the correct `<urlset>` namespace, every `<url>` has a `<loc>`, URLs are absolute (not relative), there are no duplicate URLs, and the sitemap doesn't exceed the 50,000 URL / 50MB uncompressed limits.

```bash
node skills/sitemap-xml-validator/scripts/validate-sitemap.js path/to/sitemap.xml
```

## Examples

- "Validate our sitemap.xml before we submit it to Search Console"
- "Check if our sitemap has any duplicate or relative URLs"
- "Is our sitemap within Google's size limits?"
