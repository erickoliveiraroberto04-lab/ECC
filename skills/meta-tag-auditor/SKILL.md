---
name: meta-tag-auditor
description: Scans an HTML file for missing, empty, or duplicate SEO/social meta tags (title, description, canonical, Open Graph, Twitter Card) before a page ships.
---

# Meta Tag Auditor

## When to Use

Before publishing or deploying any HTML page, or when a page's search/social preview looks wrong and the cause might be a missing or malformed meta tag.

## How It Works

Run the bundled script against a local HTML file. It checks for the presence, non-emptiness, and single-occurrence of the meta tags that matter for SEO and social sharing: `title`, `meta description`, `canonical`, and the core Open Graph and Twitter Card tags.

```bash
node skills/meta-tag-auditor/scripts/audit-meta-tags.js path/to/page.html
```

## Examples

- "Audit this landing page's HTML for missing meta tags before we deploy"
- "Our page has two conflicting canonical tags — find where"
- "Check if this page is missing Open Graph tags for social sharing"
