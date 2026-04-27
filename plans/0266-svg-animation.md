# Plan 0266 — Magnetosphere Cover SVG Animation

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR
**Source:** Bruce request (S63)
**Annealing:** N/A — mechanical plan, exact changes specified

---

## Goal

Add subtle SMIL animations to the magnetosphere cover SVGs in
`build/reader.js`. Four animation types: star twinkle, solar wind flow,
bow shock shimmer, field line breathing. Must respect
`prefers-reduced-motion`. Estimated cost: ~2.5 KB added to reader.js.

---

## Accessibility: prefers-reduced-motion

Add this variable near the top of the magnetosphere section (after
`var msWidth = ...` and before `var darkSvg = ...`):

```javascript
var motionOk = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
```

All animation strings are conditional on `motionOk`. When the user
prefers reduced motion, the SVGs render identically to the current
static versions — zero animation markup injected.

---

## Animation Specification

### Convention

Each animated element changes from self-closing (`/>`) to open/close
with a child `<animate>` element. Example:

Before: `'<circle cx="300" cy="38" r="1.0" fill="#fff" opacity="0.7" filter="url(#cv-star-glow)"/>' +`

After: `'<circle cx="300" cy="38" r="1.0" fill="#fff" opacity="0.7" filter="url(#cv-star-glow)">' + (motionOk ? '<animate attributeName="opacity" values="0.7;0.3;0.7" dur="3.2s" repeatCount="indefinite"/>' : '') + '</circle>' +`

### 1. Star Twinkle (dark SVG only — light has no stars)

Animate opacity on 6 of the brighter stars. Different durations and
start offsets create organic randomness. Only the 4 glowing stars
(with `filter="url(#cv-star-glow)"`) plus 2 bright plain stars.

| Star (cx,cy) | Base opacity | Values | Dur | Begin |
|-------------|-------------|--------|-----|-------|
| (300, 38) — glow | 0.7 | 0.7;0.25;0.7 | 3.2s | 0s |
| (520, 60) — glow | 0.6 | 0.6;0.2;0.6 | 4.1s | 1.5s |
| (55, 265) — glow | 0.6 | 0.6;0.2;0.6 | 3.7s | 0.8s |
| (610, 280) — glow | 0.5 | 0.5;0.15;0.5 | 4.5s | 2.2s |
| (45, 22) — plain | 0.6 | 0.6;0.2;0.6 | 5.0s | 0.3s |
| (540, 18) — plain | 0.6 | 0.6;0.2;0.6 | 4.8s | 1.0s |

### 2. Solar Wind Flow (both SVGs)

Add `stroke-dasharray` to each solar wind line and animate
`stroke-dashoffset` to create particles drifting toward the bow shock
(right to left in SVG space = positive dashoffset decreasing).

**Dark SVG — main 5 lines** (in `<g opacity="0.35">`):
Add to each `<line>`: `stroke-dasharray="4,7"`
Add child: `<animate attributeName="stroke-dashoffset" from="11" to="0" dur="1.8s" repeatCount="indefinite"/>`

**Dark SVG — outer 2 lines** (in `<g opacity="0.15">`):
Add to each: `stroke-dasharray="3,6"`
Add child: `<animate attributeName="stroke-dashoffset" from="9" to="0" dur="2.2s" repeatCount="indefinite"/>`

**Light SVG — main 5 lines** (in `<g opacity="0.30">`): Same as dark main.

**Light SVG — outer 2 lines** (in `<g opacity="0.12">`): Same as dark outer.

### 3. Bow Shock Shimmer (both SVGs)

Animate `stroke-width` on the primary bow shock path (the one with
gradient stroke, stroke-width 1.8).

**Dark SVG:**
Change the main bow shock path from `/>` to open/close with child:
`<animate attributeName="stroke-width" values="1.8;2.3;1.8" dur="4s" repeatCount="indefinite"/>`

**Light SVG:**
Same treatment on the corresponding path.

### 4. Field Line Breathing (both SVGs)

Animate opacity on the 3 dayside closed field lines (innermost group).

**Dark SVG** — the 3 paths in the first `<g fill="none" stroke-linecap="round">`:

| Path (opacity) | Values | Dur | Begin |
|---------------|--------|-----|-------|
| 0.55 (inner) | 0.55;0.40;0.55 | 5s | 0s |
| 0.45 (mid) | 0.45;0.30;0.45 | 5.5s | 1s |
| 0.30 (outer) | 0.30;0.18;0.30 | 6s | 2s |

**Light SVG** — same 3 paths:

| Path (opacity) | Values | Dur | Begin |
|---------------|--------|-----|-------|
| 0.40 (inner) | 0.40;0.28;0.40 | 5s | 0s |
| 0.30 (mid) | 0.30;0.18;0.30 | 5.5s | 1s |
| 0.20 (outer) | 0.20;0.12;0.20 | 6s | 2s |

---

## What NOT to Animate

- Earth, continents, atmosphere — static ground truth
- "the Flat" text label — static reference
- Credit text — static
- Magnetotail fill — too large, would look wrong
- Tailward field lines — keep depth; only dayside breathes
- Van Allen belt ellipses — static
- Flat line and copper particles — the Flat is described as steady

---

## Implementation Pattern

Every animation insertion follows this exact pattern:

```javascript
// Self-closing element becomes open/close with conditional animate child
'<element attributes>' +
(motionOk ? '<animate .../>' : '') +
'</element>' +
```

The `motionOk` ternary means: reduced-motion users get exactly the
current static SVG. No runtime cost, no layout shift, no flash.

---

## Byte Budget

| Component | Dark SVG | Light SVG | Total |
|-----------|---------|-----------|-------|
| Stars (6) | ~720 B | 0 | ~720 B |
| Solar wind (7+7) | ~980 B | ~980 B | ~1,960 B (shared pattern) |
| Bow shock (1+1) | ~130 B | ~130 B | ~260 B |
| Field lines (3+3) | ~390 B | ~390 B | ~780 B |
| motionOk variable | — | — | ~100 B |
| **Total** | | | **~2,300 B** |

Within the ~2.5 KB budget Bruce approved.

---

## Acceptance Criteria

- [ ] `var motionOk` declared before SVG strings
- [ ] 6 stars twinkle with staggered timing (dark SVG only)
- [ ] 7 solar wind lines flow toward bow shock (both SVGs)
- [ ] Bow shock shimmers (both SVGs)
- [ ] 3 dayside field lines breathe (both SVGs)
- [ ] `prefers-reduced-motion: reduce` → zero animation elements
- [ ] All animations use `repeatCount="indefinite"`
- [ ] No animation on Earth, the Flat, text labels, or tailward lines
- [ ] Existing toggle, scroll-fade, and light/dark switching unaffected
- [ ] reader.js builds and runs clean
- [ ] `make dev` or equivalent clean build
- [ ] Push to live site

---

## Generator Handoff

```
You are the Generator.

Read Plan 0266 at ~/software/relinquishment/plans/0266-svg-animation.md

Execute: Add SMIL animations to the magnetosphere cover SVGs in
build/reader.js. (1) Add `var motionOk` line after `var msWidth` and
before `var darkSvg`. (2) For each animation target in the plan's
specification tables, change the element from self-closing to open/close
with a conditional animate child: (motionOk ? '<animate .../>' : '').
(3) Add stroke-dasharray attributes to solar wind lines. Follow the
plan's exact parameters (dur, values, begin). Do NOT animate Earth,
the Flat, text, or tailward field lines. Run `make dev`. Push via
`~/software/relinquishment/deploy.sh` or equivalent. Report the 4
animation types and byte delta.
```

---

*Plan 0266 written by Argus (Auditor), S63. Mechanical plan — exact
parameters specified, no editorial judgment needed by Generator.*
