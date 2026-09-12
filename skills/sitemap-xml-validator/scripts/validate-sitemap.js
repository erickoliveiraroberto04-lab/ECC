#!/usr/bin/env node
/**
 * Validates a sitemap.xml file's structure using regex-based checks
 * (dependency-free — good enough for a pre-flight sanity check, not a
 * full XML schema validator).
 *
 * Usage: node validate-sitemap.js <path-to-sitemap.xml>
 */

const fs = require('fs');

function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node validate-sitemap.js <path-to-sitemap.xml>');
    process.exit(1);
  }

  const xml = fs.readFileSync(filePath, 'utf8');
  const issues = [];

  if (!/<\?xml[^>]*\?>/.test(xml)) {
    issues.push('Missing XML declaration (<?xml version="1.0" encoding="UTF-8"?>)');
  }

  if (!/<urlset[^>]*xmlns=["']http:\/\/www\.sitemaps\.org\/schemas\/sitemap\/0\.9["']/.test(xml)) {
    issues.push('Missing or incorrect <urlset> namespace declaration');
  }

  const urlBlocks = [...xml.matchAll(/<url>([\s\S]*?)<\/url>/g)].map((m) => m[1]);
  if (urlBlocks.length === 0) {
    issues.push('No <url> entries found');
  }

  const locs = [];
  urlBlocks.forEach((block, i) => {
    const locMatch = block.match(/<loc>([\s\S]*?)<\/loc>/);
    if (!locMatch) {
      issues.push(`<url> entry #${i + 1} is missing a <loc>`);
      return;
    }
    const loc = locMatch[1].trim();
    if (!/^https?:\/\//.test(loc)) {
      issues.push(`<loc> is not an absolute URL: "${loc}"`);
    }
    locs.push(loc);
  });

  const duplicates = locs.filter((loc, i) => locs.indexOf(loc) !== i);
  if (duplicates.length > 0) {
    issues.push(`Found ${new Set(duplicates).size} duplicate URL(s): ${[...new Set(duplicates)].slice(0, 5).join(', ')}${duplicates.length > 5 ? ', ...' : ''}`);
  }

  if (locs.length > 50000) {
    issues.push(`Sitemap has ${locs.length} URLs — exceeds the 50,000 URL limit per sitemap file`);
  }

  const sizeMb = fs.statSync(filePath).size / (1024 * 1024);
  if (sizeMb > 50) {
    issues.push(`Sitemap file is ${sizeMb.toFixed(1)}MB — exceeds the 50MB uncompressed limit`);
  }

  console.log(`Validated: ${filePath}`);
  console.log(`URLs found: ${locs.length}\n`);

  if (issues.length === 0) {
    console.log('No issues found.');
  } else {
    console.log(`Found ${issues.length} issue(s):`);
    for (const issue of issues) console.log(`  - ${issue}`);
  }
}

main();
