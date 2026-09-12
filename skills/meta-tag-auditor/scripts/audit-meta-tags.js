#!/usr/bin/env node
/**
 * Audits an HTML file for missing/duplicate/empty SEO and social meta tags.
 * Dependency-free: uses regex against the raw HTML (good enough for a
 * pre-flight audit; not a full HTML parser).
 *
 * Usage: node audit-meta-tags.js <path-to-html>
 */

const fs = require('fs');

function findAll(regex, html) {
  return [...html.matchAll(regex)].map((m) => m[0]);
}

function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node audit-meta-tags.js <path-to-html>');
    process.exit(1);
  }

  const html = fs.readFileSync(filePath, 'utf8');
  const issues = [];

  const titles = findAll(/<title>([\s\S]*?)<\/title>/gi, html);
  if (titles.length === 0) issues.push('Missing <title> tag');
  else if (titles.length > 1) issues.push(`Found ${titles.length} <title> tags — should be exactly one`);
  else if (!/<title>\s*\S/.test(titles[0])) issues.push('<title> tag is empty');

  const checks = [
    { name: 'meta description', regex: /<meta\s+name=["']description["']\s+content=["']([^"']*)["']/gi },
    { name: 'canonical link', regex: /<link\s+rel=["']canonical["']\s+href=["']([^"']*)["']/gi },
    { name: 'og:title', regex: /<meta\s+property=["']og:title["']\s+content=["']([^"']*)["']/gi },
    { name: 'og:description', regex: /<meta\s+property=["']og:description["']\s+content=["']([^"']*)["']/gi },
    { name: 'og:image', regex: /<meta\s+property=["']og:image["']\s+content=["']([^"']*)["']/gi },
    { name: 'twitter:card', regex: /<meta\s+name=["']twitter:card["']\s+content=["']([^"']*)["']/gi },
  ];

  for (const check of checks) {
    const matches = [...html.matchAll(check.regex)];
    if (matches.length === 0) {
      issues.push(`Missing ${check.name}`);
    } else if (matches.length > 1) {
      issues.push(`Found ${matches.length} ${check.name} tags — should be exactly one`);
    } else if (!matches[0][1] || !matches[0][1].trim()) {
      issues.push(`${check.name} is present but empty`);
    }
  }

  console.log(`Audited: ${filePath}\n`);
  if (issues.length === 0) {
    console.log('No issues found — all core meta tags present, non-empty, and unique.');
  } else {
    console.log(`Found ${issues.length} issue(s):`);
    for (const issue of issues) console.log(`  - ${issue}`);
  }
}

main();
