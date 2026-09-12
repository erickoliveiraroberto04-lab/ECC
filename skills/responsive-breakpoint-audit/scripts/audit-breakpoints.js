#!/usr/bin/env node
/**
 * Extracts min-width/max-width values from @media queries in a CSS file
 * and flags values that are close to (but not exactly) a common
 * breakpoint, suggesting an ad-hoc fix rather than a deliberate system.
 *
 * Usage: node audit-breakpoints.js path/to/styles.css
 */

const fs = require('fs');

const COMMON_BREAKPOINTS = [320, 375, 480, 576, 640, 768, 900, 992, 1024, 1200, 1280, 1440, 1920];

function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node audit-breakpoints.js path/to/styles.css');
    process.exit(1);
  }

  const css = fs.readFileSync(filePath, 'utf8');
  const mediaBlocks = css.match(/@media[^{]+/g) || [];

  const widths = [];
  for (const block of mediaBlocks) {
    const matches = [...block.matchAll(/(min-width|max-width)\s*:\s*([\d.]+)px/g)];
    for (const m of matches) {
      widths.push({ type: m[1], value: parseInt(m[2], 10) });
    }
  }

  if (widths.length === 0) {
    console.log(`No px-based min-width/max-width media queries found in ${filePath}`);
    return;
  }

  const distinct = [...new Set(widths.map((w) => w.value))].sort((a, b) => a - b);

  console.log(`Scanned: ${filePath}`);
  console.log(`Media query width conditions found: ${widths.length}`);
  console.log(`Distinct breakpoint values: ${distinct.length}\n`);

  console.log('Breakpoints in use:');
  distinct.forEach((v) => console.log(`  ${v}px`));

  console.log('\nValues close to a common breakpoint but not exact (possible ad-hoc fix):');
  let flaggedAny = false;
  for (const v of distinct) {
    if (COMMON_BREAKPOINTS.includes(v)) continue;
    const nearest = COMMON_BREAKPOINTS.reduce((best, bp) =>
      Math.abs(bp - v) < Math.abs(best - v) ? bp : best
    );
    const diff = Math.abs(nearest - v);
    if (diff > 0 && diff <= 8) {
      flaggedAny = true;
      console.log(`  ${v}px is ${diff}px away from common breakpoint ${nearest}px`);
    }
  }
  if (!flaggedAny) console.log('  None found.');
}

main();
