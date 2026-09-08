#!/usr/bin/env node
/**
 * Extracts every distinct color value from a CSS file (hex, rgb()/rgba(),
 * hsl()/hsla(), named colors) and flags hex colors that are visually
 * near-identical (small numeric distance) and likely accidental duplicates.
 *
 * Usage: node extract-palette.js path/to/styles.css
 */

const fs = require('fs');

const NAMED_COLORS = [
  'black', 'white', 'red', 'green', 'blue', 'yellow', 'orange', 'purple',
  'pink', 'brown', 'gray', 'grey', 'cyan', 'magenta', 'lime', 'navy',
  'teal', 'maroon', 'olive', 'silver', 'gold', 'coral', 'salmon', 'khaki',
  'indigo', 'violet', 'crimson', 'chocolate', 'tomato', 'orchid',
  'transparent', 'currentcolor',
];

function hexToRgb(hex) {
  let h = hex.replace('#', '');
  if (h.length === 3 || h.length === 4) {
    h = h.split('').map((c) => c + c).join('');
  }
  const r = parseInt(h.slice(0, 2), 16);
  const g = parseInt(h.slice(2, 4), 16);
  const b = parseInt(h.slice(4, 6), 16);
  return { r, g, b };
}

function colorDistance(hexA, hexB) {
  const a = hexToRgb(hexA);
  const b = hexToRgb(hexB);
  return Math.sqrt((a.r - b.r) ** 2 + (a.g - b.g) ** 2 + (a.b - b.b) ** 2);
}

function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node extract-palette.js path/to/styles.css');
    process.exit(1);
  }

  const css = fs.readFileSync(filePath, 'utf8');

  const hexMatches = css.match(/#(?:[0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b/g) || [];
  const rgbMatches = css.match(/rgba?\([^)]+\)/g) || [];
  const hslMatches = css.match(/hsla?\([^)]+\)/g) || [];

  const namedPattern = new RegExp(`(?<![\\w-])(${NAMED_COLORS.join('|')})(?![\\w-])`, 'gi');
  const namedMatches = css.match(namedPattern) || [];

  const hexSet = [...new Set(hexMatches.map((h) => h.toLowerCase()))];
  const rgbSet = [...new Set(rgbMatches.map((v) => v.replace(/\s+/g, ' ').trim()))];
  const hslSet = [...new Set(hslMatches.map((v) => v.replace(/\s+/g, ' ').trim()))];
  const namedSet = [...new Set(namedMatches.map((v) => v.toLowerCase()))];

  const total = hexSet.length + rgbSet.length + hslSet.length + namedSet.length;

  console.log(`Scanned: ${filePath}`);
  console.log(`Total distinct color values: ${total}\n`);

  console.log(`Hex (${hexSet.length}):`);
  hexSet.forEach((h) => console.log(`  ${h}`));

  console.log(`\nrgb()/rgba() (${rgbSet.length}):`);
  rgbSet.forEach((v) => console.log(`  ${v}`));

  console.log(`\nhsl()/hsla() (${hslSet.length}):`);
  hslSet.forEach((v) => console.log(`  ${v}`));

  console.log(`\nNamed colors (${namedSet.length}):`);
  namedSet.forEach((v) => console.log(`  ${v}`));

  const fullHex = hexSet.filter((h) => h.length === 7 || h.length === 9);
  const nearDuplicates = [];
  for (let i = 0; i < fullHex.length; i++) {
    for (let j = i + 1; j < fullHex.length; j++) {
      const dist = colorDistance(fullHex[i], fullHex[j]);
      if (dist > 0 && dist < 12) {
        nearDuplicates.push([fullHex[i], fullHex[j], dist.toFixed(1)]);
      }
    }
  }

  console.log(`\nNear-duplicate hex pairs (likely should be one token):`);
  if (nearDuplicates.length === 0) {
    console.log('  None found.');
  } else {
    nearDuplicates.forEach(([a, b, d]) => console.log(`  ${a} ~ ${b} (distance: ${d})`));
  }
}

main();
