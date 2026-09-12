#!/usr/bin/env node
/**
 * Builds and validates UTM-tagged campaign URLs.
 *
 * Usage:
 *   node utm.js build <base-url> --source X --medium Y --campaign Z [--term T] [--content C]
 *   node utm.js check <utm-url>
 */

function parseFlags(args) {
  const flags = {};
  for (let i = 0; i < args.length; i++) {
    if (args[i].startsWith('--')) {
      flags[args[i].slice(2)] = args[i + 1];
      i++;
    }
  }
  return flags;
}

function build(args) {
  const baseUrl = args[0];
  const flags = parseFlags(args.slice(1));

  if (!baseUrl || !flags.source || !flags.medium || !flags.campaign) {
    console.error('Usage: node utm.js build <base-url> --source X --medium Y --campaign Z [--term T] [--content C]');
    process.exit(1);
  }

  const url = new URL(baseUrl);
  url.searchParams.set('utm_source', flags.source);
  url.searchParams.set('utm_medium', flags.medium);
  url.searchParams.set('utm_campaign', flags.campaign);
  if (flags.term) url.searchParams.set('utm_term', flags.term);
  if (flags.content) url.searchParams.set('utm_content', flags.content);

  console.log(url.toString());
}

function check(args) {
  const rawUrl = args[0];
  if (!rawUrl) {
    console.error('Usage: node utm.js check <utm-url>');
    process.exit(1);
  }

  const url = new URL(rawUrl);
  const params = url.searchParams;
  const issues = [];

  const required = ['utm_source', 'utm_medium', 'utm_campaign'];
  for (const key of required) {
    if (!params.has(key)) issues.push(`Missing required param: ${key}`);
  }

  for (const key of ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']) {
    const value = params.get(key);
    if (!value) continue;
    if (value !== value.toLowerCase()) {
      issues.push(`${key}="${value}" has mixed casing — analytics tools treat "Facebook" and "facebook" as different values`);
    }
    if (/\s/.test(value)) {
      issues.push(`${key}="${value}" contains raw spaces — use underscores or hyphens instead`);
    }
  }

  if (issues.length === 0) {
    console.log('No issues found.');
  } else {
    console.log(`Found ${issues.length} issue(s):`);
    for (const issue of issues) console.log(`  - ${issue}`);
  }
}

function main() {
  const [mode, ...rest] = process.argv.slice(2);
  if (mode === 'build') return build(rest);
  if (mode === 'check') return check(rest);
  console.error('Usage: node utm.js <build|check> ...');
  process.exit(1);
}

main();
