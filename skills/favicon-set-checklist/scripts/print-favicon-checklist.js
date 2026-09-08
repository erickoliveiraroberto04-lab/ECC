#!/usr/bin/env node
/**
 * Prints the standard favicon/app-icon file set and the head markup
 * needed to reference it correctly.
 *
 * Usage: node print-favicon-checklist.js
 */

const FILES = [
  { file: 'favicon.ico', size: '16x16, 32x32, 48x48 (multi-size .ico)', purpose: 'Legacy browser tab icon' },
  { file: 'favicon-16x16.png', size: '16x16', purpose: 'Browser tab (small displays)' },
  { file: 'favicon-32x32.png', size: '32x32', purpose: 'Browser tab (standard)' },
  { file: 'apple-touch-icon.png', size: '180x180', purpose: 'iOS home screen icon' },
  { file: 'android-chrome-192x192.png', size: '192x192', purpose: 'Android home screen / PWA' },
  { file: 'android-chrome-512x512.png', size: '512x512', purpose: 'Android splash / PWA' },
  { file: 'mstile-150x150.png', size: '150x150', purpose: 'Windows Start tile' },
  { file: 'safari-pinned-tab.svg', size: 'vector, monochrome', purpose: 'Safari pinned tab icon' },
  { file: 'site.webmanifest', size: 'n/a (JSON)', purpose: 'PWA name/icons/theme-color manifest' },
];

const HEAD_MARKUP = `<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="mask-icon" href="/safari-pinned-tab.svg" color="#000000">
<link rel="manifest" href="/site.webmanifest">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="msapplication-config" content="/browserconfig.xml">
<meta name="theme-color" content="#ffffff">`;

console.log('Required favicon/app-icon files:\n');
for (const f of FILES) {
  console.log(`  ${f.file.padEnd(28)} ${f.size.padEnd(28)} ${f.purpose}`);
}

console.log('\nRequired <head> markup:\n');
console.log(HEAD_MARKUP);
