# Plan 0231 — SVG Gallery Page

**Status:** COMPLETE (verified S63 audit)
**Author:** Auditor (Argus S59)
**Priority:** Medium-high (Bruce has never seen the images)
**Scope:** New file `docs/gallery.html`, read-only extraction from `build/hover-definitions.yaml` + `build/preprocess.py`

---

## Problem

There are ~19 inline SVGs in `hover-definitions.yaml` and additional SVGs embedded in `preprocess.py`. Bruce has never seen them. They're only visible by hovering on specific terms in a 250-page HTML book. There is no index, no gallery, no way to browse them.

## Solution

Build a single standalone HTML page (`docs/gallery.html`) that:

1. Extracts every SVG from `hover-definitions.yaml` and `preprocess.py`
2. Displays each at readable size with a stable **NAME ID** (e.g., `SVG-001-buttons-and-threads`)
3. Shows the YAML key / function name that sources each SVG
4. Shows which hover term(s) trigger it in the book
5. Groups by category if natural groupings exist

## Requirements

- **Each SVG gets a stable ID:** Format `SVG-NNN-short-name` (e.g., `SVG-001-buttons-and-threads`, `SVG-002-kauffman-filmstrip-scatter`)
- **Viewable in browser:** `open docs/gallery.html` — no build step, no server
- **Self-contained:** All SVGs inline in the HTML, no external dependencies
- **Anchor links:** Each SVG section has an `id=` anchor so Bruce can link to specific images in conversation (e.g., `gallery.html#SVG-005`)
- **Table of contents** at top listing all IDs + short names as anchor links
- **Shows current deployment status:** Where in the book each SVG appears (chapter/term), or "not yet deployed"

## Source Inventory (Generator must verify)

1. `build/hover-definitions.yaml` — ~19 SVGs keyed by hover term name
2. `build/preprocess.py` — Kauffman filmstrip panels (BUTTONS_SVG_1 through BUTTONS_SVG_4), possibly others
3. `build/images/*.svg` — standalone SVG files (cover-triskellion, magnetosphere-test)

## Generator Instructions

1. Read `build/hover-definitions.yaml` — extract every key that contains `<svg`
2. Read `build/preprocess.py` — extract every SVG constant
3. Read `build/images/` — list standalone SVGs
4. Build `docs/gallery.html` with all SVGs displayed, numbered, named, anchored
5. Add a TOC at top
6. Verify by opening in browser: `xdg-open docs/gallery.html`
7. Do NOT modify any existing files — this is read-only extraction into a new gallery page

## Constraints

- Gallery page is a development tool, not part of the book
- No build system changes
- No modifications to hover-definitions.yaml or preprocess.py
- Keep it simple — plain HTML + minimal inline CSS, no JavaScript needed
