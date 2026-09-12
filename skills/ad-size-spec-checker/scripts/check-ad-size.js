#!/usr/bin/env node
/**
 * Matches an image's pixel dimensions against standard ad placement specs.
 * Dependency-free: parses PNG and JPEG headers directly.
 *
 * Usage: node check-ad-size.js <path-to-image>
 */

const fs = require('fs');

function getPngDimensions(buf) {
  return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
}

function getJpegDimensions(buf) {
  let offset = 2;
  while (offset < buf.length) {
    if (buf[offset] !== 0xff) { offset++; continue; }
    const marker = buf[offset + 1];
    const isSofMarker = marker >= 0xc0 && marker <= 0xcf && marker !== 0xc4 && marker !== 0xc8 && marker !== 0xcc;
    if (isSofMarker) {
      return { height: buf.readUInt16BE(offset + 5), width: buf.readUInt16BE(offset + 7) };
    }
    offset += 2 + buf.readUInt16BE(offset + 2);
  }
  return null;
}

function getDimensions(filePath) {
  const buf = fs.readFileSync(filePath);
  if (buf.slice(0, 8).toString('hex') === '89504e470d0a1a0a') return getPngDimensions(buf);
  if (buf[0] === 0xff && buf[1] === 0xd8) return getJpegDimensions(buf);
  throw new Error('Unsupported format: only PNG and JPEG are supported');
}

const SPECS = [
  { platform: 'Meta (Facebook/Instagram)', name: 'Feed square', w: 1080, h: 1080 },
  { platform: 'Meta (Facebook/Instagram)', name: 'Feed portrait', w: 1080, h: 1350 },
  { platform: 'Meta (Facebook/Instagram)', name: 'Stories / Reels', w: 1080, h: 1920 },
  { platform: 'Meta (Facebook/Instagram)', name: 'Link ad landscape', w: 1200, h: 628 },
  { platform: 'Google Display (IAB)', name: 'Medium Rectangle', w: 300, h: 250 },
  { platform: 'Google Display (IAB)', name: 'Leaderboard', w: 728, h: 90 },
  { platform: 'Google Display (IAB)', name: 'Wide Skyscraper', w: 160, h: 600 },
  { platform: 'Google Display (IAB)', name: 'Mobile Banner', w: 320, h: 50 },
  { platform: 'Google Display (IAB)', name: 'Half Page', w: 300, h: 600 },
  { platform: 'Google Display (IAB)', name: 'Large Rectangle', w: 336, h: 280 },
  { platform: 'LinkedIn', name: 'Single image ad', w: 1200, h: 627 },
  { platform: 'LinkedIn', name: 'Square image ad', w: 1080, h: 1080 },
  { platform: 'Pinterest', name: 'Standard Pin', w: 1000, h: 1500 },
  { platform: 'YouTube', name: 'Thumbnail', w: 1280, h: 720 },
];

function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node check-ad-size.js <path-to-image>');
    process.exit(1);
  }

  const { width, height } = getDimensions(filePath);
  console.log(`Image dimensions: ${width}x${height}\n`);

  const exact = SPECS.filter((s) => s.w === width && s.h === height);
  if (exact.length) {
    console.log('Exact matches:');
    for (const s of exact) console.log(`  [OK] ${s.platform} — ${s.name} (${s.w}x${s.h})`);
  } else {
    console.log('No exact match found. Closest specs by aspect ratio:');
    const ratio = width / height;
    const scored = SPECS
      .map((s) => ({ ...s, diff: Math.abs(ratio - s.w / s.h) }))
      .sort((a, b) => a.diff - b.diff)
      .slice(0, 3);
    for (const s of scored) {
      console.log(`  ~ ${s.platform} — ${s.name} (${s.w}x${s.h}, ratio diff ${s.diff.toFixed(3)})`);
    }
  }
}

main();
