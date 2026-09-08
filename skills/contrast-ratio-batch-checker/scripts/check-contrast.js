#!/usr/bin/env node
/**
 * Computes WCAG contrast ratios for a batch of foreground/background hex
 * color pairs and reports pass/fail against AA/AAA thresholds.
 *
 * Usage:
 *   node check-contrast.js path/to/pairs.json
 *   node check-contrast.js --pair "#333333" "#ffffff"
 */

const fs = require('fs');

function hexToRgb(hex) {
  let h = hex.replace('#', '');
  if (h.length === 3) h = h.split('').map((c) => c + c).join('');
  return {
    r: parseInt(h.slice(0, 2), 16),
    g: parseInt(h.slice(2, 4), 16),
    b: parseInt(h.slice(4, 6), 16),
  };
}

function relativeLuminance({ r, g, b }) {
  const channel = (c) => {
    const s = c / 255;
    return s <= 0.03928 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4;
  };
  const R = channel(r);
  const G = channel(g);
  const B = channel(b);
  return 0.2126 * R + 0.7152 * G + 0.0722 * B;
}

function contrastRatio(hexA, hexB) {
  const lumA = relativeLuminance(hexToRgb(hexA));
  const lumB = relativeLuminance(hexToRgb(hexB));
  const lighter = Math.max(lumA, lumB);
  const darker = Math.min(lumA, lumB);
  return (lighter + 0.05) / (darker + 0.05);
}

function evaluate(pair) {
  const ratio = contrastRatio(pair.fg, pair.bg);
  return {
    name: pair.name || `${pair.fg} on ${pair.bg}`,
    fg: pair.fg,
    bg: pair.bg,
    ratio,
    aaNormal: ratio >= 4.5,
    aaLarge: ratio >= 3,
    aaaNormal: ratio >= 7,
    aaaLarge: ratio >= 4.5,
  };
}

function printResult(r) {
  console.log(`\n${r.name} (${r.fg} on ${r.bg})`);
  console.log(`  Ratio: ${r.ratio.toFixed(2)}:1`);
  console.log(`  AA normal text (4.5:1):  ${r.aaNormal ? 'PASS' : 'FAIL'}`);
  console.log(`  AA large text (3:1):     ${r.aaLarge ? 'PASS' : 'FAIL'}`);
  console.log(`  AAA normal text (7:1):   ${r.aaaNormal ? 'PASS' : 'FAIL'}`);
  console.log(`  AAA large text (4.5:1):  ${r.aaaLarge ? 'PASS' : 'FAIL'}`);
}

function main() {
  const args = process.argv.slice(2);

  if (args[0] === '--pair') {
    const [, fg, bg] = args;
    if (!fg || !bg) {
      console.error('Usage: node check-contrast.js --pair "#foreground" "#background"');
      process.exit(1);
    }
    printResult(evaluate({ fg, bg }));
    return;
  }

  const filePath = args[0];
  if (!filePath) {
    console.error('Usage: node check-contrast.js path/to/pairs.json  (or --pair "#fg" "#bg")');
    process.exit(1);
  }

  const pairs = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  const results = pairs.map(evaluate);

  console.log(`Scanned: ${filePath}`);
  console.log(`Pairs checked: ${results.length}`);
  const failing = results.filter((r) => !r.aaNormal);
  console.log(`Failing AA normal text: ${failing.length}`);

  results.forEach(printResult);
}

main();
