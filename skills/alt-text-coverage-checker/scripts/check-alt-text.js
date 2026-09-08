#!/usr/bin/env node
/**
 * Scans an HTML file for <img> tags missing alt text, using empty alt
 * text, or using low-quality placeholder alt text.
 *
 * Usage: node check-alt-text.js path/to/page.html
 */

const fs = require('fs');
const path = require('path');

const PLACEHOLDER_WORDS = ['image', 'photo', 'picture', 'img', 'placeholder', 'untitled'];

function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node check-alt-text.js path/to/page.html');
    process.exit(1);
  }

  const html = fs.readFileSync(filePath, 'utf8');
  const imgTags = html.match(/<img\b[^>]*>/gi) || [];

  if (imgTags.length === 0) {
    console.log(`No <img> tags found in ${filePath}`);
    return;
  }

  const missing = [];
  const empty = [];
  const placeholder = [];
  const ok = [];

  for (const tag of imgTags) {
    const altMatch = tag.match(/\balt\s*=\s*(["'])(.*?)\1/i);
    const srcMatch = tag.match(/\bsrc\s*=\s*(["'])(.*?)\1/i);
    const src = srcMatch ? srcMatch[2] : '(no src)';

    if (!altMatch) {
      missing.push(src);
      continue;
    }

    const alt = altMatch[2].trim();
    if (alt === '') {
      empty.push(src);
      continue;
    }

    const filenameStem = path.basename(src, path.extname(src)).toLowerCase().replace(/[-_]/g, ' ');
    const altLower = alt.toLowerCase();
    const isPlaceholder =
      PLACEHOLDER_WORDS.some((w) => altLower === w) ||
      altLower === filenameStem;

    if (isPlaceholder) {
      placeholder.push(`${src} -> alt="${alt}"`);
    } else {
      ok.push(`${src} -> alt="${alt}"`);
    }
  }

  console.log(`Scanned: ${filePath}`);
  console.log(`Total <img> tags: ${imgTags.length}`);
  console.log(`  OK: ${ok.length}`);
  console.log(`  Missing alt attribute: ${missing.length}`);
  console.log(`  Empty alt="" (decorative-only, verify): ${empty.length}`);
  console.log(`  Placeholder/low-quality alt text: ${placeholder.length}`);

  if (missing.length) {
    console.log('\nMissing alt attribute:');
    missing.forEach((s) => console.log(`  ${s}`));
  }
  if (empty.length) {
    console.log('\nEmpty alt="" (confirm image is purely decorative):');
    empty.forEach((s) => console.log(`  ${s}`));
  }
  if (placeholder.length) {
    console.log('\nPlaceholder/low-quality alt text:');
    placeholder.forEach((s) => console.log(`  ${s}`));
  }
}

main();
