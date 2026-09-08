#!/usr/bin/env node
/**
 * Parses a list of UTM-tagged URLs (one per line) and reports counts
 * grouped by campaign, source, and medium, plus which URLs are missing
 * required UTM parameters.
 *
 * Usage: node report-utm.js path/to/urls.txt
 */

const fs = require('fs');

const REQUIRED = ['utm_source', 'utm_medium', 'utm_campaign'];

function group(map, key) {
  map.set(key, (map.get(key) || 0) + 1);
}

function printGroup(title, map) {
  console.log(`\n${title}:`);
  if (map.size === 0) {
    console.log('  (none)');
    return;
  }
  [...map.entries()].sort((a, b) => b[1] - a[1]).forEach(([k, v]) => {
    console.log(`  ${k.padEnd(30)} ${v}`);
  });
}

function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node report-utm.js path/to/urls.txt');
    process.exit(1);
  }

  const lines = fs.readFileSync(filePath, 'utf8')
    .split('\n')
    .map((l) => l.trim())
    .filter(Boolean);

  const byCampaign = new Map();
  const bySource = new Map();
  const byMedium = new Map();
  const missing = [];

  for (const line of lines) {
    let url;
    try {
      url = new URL(line);
    } catch {
      missing.push(`${line}  (not a valid URL)`);
      continue;
    }
    const params = url.searchParams;
    const missingParams = REQUIRED.filter((p) => !params.get(p));
    if (missingParams.length > 0) {
      missing.push(`${line}  (missing: ${missingParams.join(', ')})`);
      continue;
    }
    group(byCampaign, params.get('utm_campaign'));
    group(bySource, params.get('utm_source'));
    group(byMedium, params.get('utm_medium'));
  }

  console.log(`Scanned: ${filePath}`);
  console.log(`Total URLs: ${lines.length}`);
  console.log(`Fully tagged: ${lines.length - missing.length}`);
  console.log(`Missing required tags: ${missing.length}`);

  printGroup('By campaign', byCampaign);
  printGroup('By source', bySource);
  printGroup('By medium', byMedium);

  if (missing.length > 0) {
    console.log('\nURLs with issues:');
    missing.forEach((m) => console.log(`  ${m}`));
  }
}

main();
