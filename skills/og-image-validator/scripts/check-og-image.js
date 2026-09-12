#!/usr/bin/env node
/**
 * Validates an image's dimensions/aspect ratio against Open Graph and
 * Twitter Card recommendations. Dependency-free: parses PNG and JPEG
 * headers directly.
 *
 * Usage: node check-og-image.js <path-to-image>
 */

const fs = require('fs');
const path = require('path');

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
      const height = buf.readUInt16BE(offset + 5);
      const width = buf.readUInt16BE(offset + 7);
      return { width, height };
    }
    const segmentLength = buf.readUInt16BE(offset + 2);
    offset += 2 + segmentLength;
  }
  return null;
}

function getDimensions(filePath) {
  const buf = fs.readFileSync(filePath);
  if (buf.slice(0, 8).toString('hex') === '89504e470d0a1a0a') return getPngDimensions(buf);
  if (buf[0] === 0xff && buf[1] === 0xd8) return getJpegDimensions(buf);
  throw new Error('Unsupported format: only PNG and JPEG are supported');
}

function main() {
  const filePath = process.argv[2];
  if (!filePath) {
    console.error('Usage: node check-og-image.js <path-to-image>');
    process.exit(1);
  }

  const dims = getDimensions(filePath);
  if (!dims) {
    console.error('Could not determine image dimensions.');
    process.exit(1);
  }

  const { width, height } = dims;
  const ratio = width / height;
  const fileSizeKb = (fs.statSync(filePath).size / 1024).toFixed(1);

  console.log(`File: ${path.basename(filePath)}`);
  console.log(`Dimensions: ${width}x${height}`);
  console.log(`Aspect ratio: ${ratio.toFixed(3)} (1.91:1 = ${(1200 / 630).toFixed(3)}, 2:1 = 2.000)`);
  console.log(`File size: ${fileSizeKb} KB`);
  console.log('');

  const checks = [
    { name: 'Open Graph (1200x630, 1.91:1)', minW: 1200, minH: 630, ratio: 1200 / 630 },
    { name: 'Twitter summary_large_image (1200x600, 2:1)', minW: 1200, minH: 600, ratio: 2 },
  ];

  for (const check of checks) {
    const sizeOk = width >= check.minW && height >= check.minH;
    const ratioOk = Math.abs(ratio - check.ratio) < 0.05;
    const status = sizeOk && ratioOk ? 'PASS' : 'FAIL';
    console.log(`[${status}] ${check.name}`);
    if (!sizeOk) console.log(`  - too small: needs at least ${check.minW}x${check.minH}`);
    if (!ratioOk) console.log(`  - aspect ratio off: expected ~${check.ratio.toFixed(3)}, got ${ratio.toFixed(3)}`);
  }

  if (Number(fileSizeKb) > 5120) {
    console.log('\n[WARN] File is larger than 5MB — many platforms will reject or fail to fetch it in time.');
  }
}

main();
