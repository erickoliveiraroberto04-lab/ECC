# three.js (vendored)

A self-contained, global-script build of [three.js](https://threejs.org) — vendored
here so artifacts and skills that need WebGL/3D can embed it without network access
(e.g. Claude Design canvases, which run in a sandbox with no CDN egress).

## Contents

- `three.bundle.min.js` — IIFE bundle exposing `window.THREE`, including the core
  library and the `OrbitControls` addon (`THREE.OrbitControls`). Minified with
  esbuild from the official `three` npm package.
- `LICENSE` — three.js's own MIT license, kept alongside per its terms.

## Provenance

- Source: [`three`](https://www.npmjs.com/package/three) npm package, version 0.185.1
  (upstream repo: [mrdoob/three.js](https://github.com/mrdoob/three.js)).
- Rebuilt as a global IIFE because current `three` releases ship ESM-only —
  no classic `<script>`-global build is published upstream anymore.
- Build command (from a checkout with `three` installed):

  ```bash
  # entry.js:
  #   import * as THREE from 'three';
  #   import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
  #   window.THREE = THREE;
  #   window.THREE.OrbitControls = OrbitControls;
  npx esbuild entry.js --bundle --format=iife --minify --outfile=three.bundle.min.js
  ```

## Usage

Inline the file's contents in a plain `<script>` tag (not `type="module"`), then use
`THREE` and `THREE.OrbitControls` as globals:

```html
<script>/* paste three.bundle.min.js contents here */</script>
<script>
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.1, 100);
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  const controls = new THREE.OrbitControls(camera, renderer.domElement);
  // ...
</script>
```

For a regular (non-sandboxed) Artifact, loading three.js from cdnjs.cloudflare.com
is usually simpler than embedding this file — reach for this vendored bundle
specifically when the target environment has no network egress.

To rebuild with additional addons (loaders, post-processing, etc.), add the needed
imports to `entry.js` above and re-run the esbuild command; keep the output under
version control size limits (currently ~730 KB minified for core + OrbitControls).
