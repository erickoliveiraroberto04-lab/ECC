#!/usr/bin/env node
/**
 * Checks ad copy text length against known per-platform field limits.
 *
 * Usage:
 *   node count-ad-copy.js --platform <key> "copy text"
 *   node count-ad-copy.js --list
 */

const LIMITS = {
  'google-headline': { label: 'Google Ads — Headline', limit: 30 },
  'google-description': { label: 'Google Ads — Description', limit: 90 },
  'meta-primary-text': { label: 'Meta Ads — Primary text (recommended, not hard cap)', limit: 125 },
  'meta-headline': { label: 'Meta Ads — Headline', limit: 40 },
  'meta-description': { label: 'Meta Ads — Link description', limit: 30 },
  'linkedin-headline': { label: 'LinkedIn Ads — Intro text (recommended)', limit: 150 },
  'linkedin-headline-short': { label: 'LinkedIn Ads — Headline', limit: 70 },
  'pinterest-title': { label: 'Pinterest Ads — Title', limit: 100 },
  'pinterest-description': { label: 'Pinterest Ads — Description', limit: 500 },
  'twitter-post': { label: 'X/Twitter — Post text', limit: 280 },
};

function list() {
  console.log('Supported platform/field keys:\n');
  for (const [key, spec] of Object.entries(LIMITS)) {
    console.log(`  ${key.padEnd(24)} ${spec.label} — ${spec.limit} chars`);
  }
}

function count(platform, text) {
  const spec = LIMITS[platform];
  if (!spec) {
    console.error(`Unknown platform key: "${platform}". Run with --list to see valid keys.`);
    process.exit(1);
  }
  const len = text.length;
  const status = len <= spec.limit ? 'OK' : 'OVER LIMIT';
  console.log(`${spec.label}`);
  console.log(`Limit: ${spec.limit} chars`);
  console.log(`Actual: ${len} chars`);
  console.log(`Status: ${status}`);
  if (len > spec.limit) {
    console.log(`Over by: ${len - spec.limit} chars`);
  }
}

function main() {
  const args = process.argv.slice(2);
  if (args.includes('--list')) return list();

  const platformIndex = args.indexOf('--platform');
  if (platformIndex === -1 || !args[platformIndex + 1]) {
    console.error('Usage: node count-ad-copy.js --platform <key> "copy text"  (or --list)');
    process.exit(1);
  }
  const platform = args[platformIndex + 1];
  const text = args.filter((_, i) => i !== platformIndex && i !== platformIndex + 1).join(' ');
  if (!text) {
    console.error('No copy text provided.');
    process.exit(1);
  }
  count(platform, text);
}

main();
