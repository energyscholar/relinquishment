# Plan 0270 — Magnetosphere Teaching Imagemaps

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR (Phase 1)
**Source:** Bruce request (S63): MS imagemaps with hover tooltips for
"The Wrong Substrate" chapter. Earth, Jupiter, Saturn.
**Annealing:** MED LOW LOW

---

## Goal

Three interactive magnetosphere diagrams with `data-hover` tooltips
teaching structural names and behaviors. Each is an SVG in
preprocess.py, injected into "The Wrong Substrate" chapter, floated
right so text wraps alongside. Hover works via the existing reader.js
tooltip system (same as domain-buttons SVG-014).

## Decision: New SVGs, Not Cover Reuse

Build purpose-built teaching SVGs. Same visual language as the cover
magnetosphere (warm palette, soft gradients, SMIL animation) but
optimized for:
- Non-overlapping hover zones (each `<g data-hover>` clearly delineated)
- Structures the cover omits (magnetosheath, magnetopause, Io torus, etc.)
- Consistent sizing across all three planets
- The chapter's nature-documentary voice in tooltip text

## Phases

| Phase | Planet | Hover Zones | Chapter Marker | SVG ID |
|-------|--------|-------------|----------------|--------|
| 1 | Earth | 9 | "Sixty thousand kilometers above your head" | SVG-039 |
| 2 | Jupiter | 8 | "Five hundred million kilometers away" | SVG-040 |
| 3 | Saturn | 7 | "Saturn's magnetosphere is smaller" | SVG-041 |

Each phase is independently deployable. Phase 1 is specified below in
full. Phases 2 and 3 follow the identical pattern.

---

## Common Specification (All Three Phases)

### SVG Dimensions

- Viewport: `viewBox="0 0 420 280"`
- Display: `width="100%"` (responsive within container)
- Container: see Float Layout below

### Float Layout

```html
<figure id="fig-ms-{planet}" class="inline-svg ms-teaching"
  style="float:right;margin:0 0 1em 1.5em;max-width:420px;width:45%;
         text-align:center;">
  <svg ...>...</svg>
  <figcaption style="font-size:0.75em;color:#888;margin-top:0.3em;
    font-style:italic;">Hover to explore</figcaption>
</figure>
```

### Mobile Collapse

Add to preprocess.py's CSS injection (or the SVG's inline style):

```css
@media (max-width: 700px) {
  .ms-teaching {
    float: none !important;
    width: 100% !important;
    max-width: 100% !important;
    margin: 1em auto !important;
  }
}
```

### Injection Mechanism

New function `inject_ms_diagrams(html)` in preprocess.py. For each
planet:
1. Find the marker text in the HTML
2. Find the opening `<p` tag of the paragraph containing that marker
3. Insert the figure HTML **before** that `<p>` tag

This is different from inject_genesis_illustrations (which inserts
after the closing `</p>`). The before-insertion is required for
float:right to work — the figure must precede the text it floats
beside.

### Hover Integration

Each structural region wrapped in:
```xml
<g data-hover="Tooltip text here" style="cursor:pointer">
  ...svg elements...
</g>
```

Reader.js already picks up `data-hover` attributes and shows tooltips
on mouseover. No additional JS needed.

### Color Palette

Shared across all three planets for visual consistency:

| Element | Color | Notes |
|---------|-------|-------|
| Background | transparent | Adapts to page light/dark |
| Planet body | #4a90d9 | Atmosphere glow |
| Bow shock | #ff6b35 → transparent | Gradient stroke |
| Solar wind | #ffaa44 | Arrows/lines |
| Dayside field | #5ba3cf | Closed loops |
| Tailward field | #3a5f7a | Stretched lines |
| Magnetotail fill | #1a2d4a, opacity 0.15 | Tail region |
| Plasma sheet | #cd7f32 | Copper/gold — "the Flat" |
| Van Allen / rad belt | #7b68ee, dashed | Trapped particle zones |
| Labels | #555 | Georgia, 9-10px |
| Magnetopause | #6a9fba, dash 3,3 | Boundary line |
| Magnetosheath | #d4a574, opacity 0.08 | Turbulent region fill |

Jupiter-specific additions: Io torus = #e8a832 (volcanic orange).
Saturn-specific additions: ring system = #c9b896 (pale gold).

### Animation

Subtle SMIL, same principles as Plan 0266/0267:
- Solar wind lines: `stroke-dasharray` + `stroke-dashoffset` animation
  (shows flow direction, ~2s cycle)
- No other mandatory animations (teaching clarity > atmosphere)
- Reduced-motion: `<style>@media(prefers-reduced-motion:reduce){animate{display:none}}</style>`

### Title Element

Each SVG must include a `<title>` element for accessibility describing
the full diagram.

---

## Phase 1: Earth Magnetosphere

### Layout (schematic — Generator determines exact coordinates)

```
Sun →  ←wind←  ((( bow  sheath   /--- dayside
       ←wind←  ((( shock        |    field lines
       ←wind←  (((    mpause   EARTH ←Van Allen
       ←wind←  (((              |
       ←wind←  (((               \---
                                    ══════════ plasma sheet
                                   magnetotail
                                    ══════════
```

Cross-section view: Sun implied at far left, Earth center-left,
magnetotail stretching right. Standard textbook orientation.

### Hover Zones (9)

**Zone 1: Solar Wind** (far-left arrows/lines)
```
<strong>Solar Wind</strong><br>A continuous stream of charged particles
from the Sun — about 400 km/s, roughly five particles per cubic
centimeter at Earth. It has blown without interruption for four and a
half billion years.
```

**Zone 2: Bow Shock** (outermost curved boundary, left)
```
<strong>Bow Shock</strong><br>Where the supersonic solar wind brakes
against Earth's magnetic field. A standing shock wave, roughly
90,000 km out — about 14 Earth radii.
```

**Zone 3: Magnetosheath** (region between bow shock and magnetopause)
```
<strong>Magnetosheath</strong><br>Turbulent heated plasma between the
bow shock and magnetopause. Solar wind that has slowed but has not yet
been fully deflected.
```

**Zone 4: Magnetopause** (inner boundary curve, dashed)
```
<strong>Magnetopause</strong><br>The outer boundary of Earth's magnetic
domain. Compressed on the dayside by solar wind, it expands and
contracts as pressure changes — the magnetosphere breathes.
```

**Zone 5: Dayside Field Lines** (compressed loops left of Earth)
```
<strong>Dayside Field Lines</strong><br>Closed magnetic loops compressed
by solar wind pressure. Particles trapped along these loops form the
radiation belts. Strongest near the equator.
```

**Zone 6: Earth** (planet body, center-left)
```
<strong>Earth</strong><br>Magnetic dipole tilted 11.5° from the
rotation axis. This tilt rocks the entire magnetosphere as Earth
turns — a twelve-hour breathing rhythm that has run since the field
first formed.
```

**Zone 7: Van Allen Belts** (two dashed ellipses around Earth)
```
<strong>Van Allen Belts</strong><br>Radiation belts of trapped
high-energy particles. Inner belt: protons. Outer belt: electrons.
Discovered by Explorer 1 in 1958.
```

**Zone 8: Magnetotail** (stretched tail region, right)
```
<strong>Magnetotail</strong><br>Earth's magnetic field stretched by the
solar wind into a tail millions of kilometers long — two lobes of
opposite polarity, like the wake behind a ship.
```

**Zone 9: Plasma Sheet — the Flat** (thin copper line in tail center)
```
<strong>Plasma Sheet — the Flat</strong><br>A thin, hot layer of plasma
where the two magnetotail lobes meet. About two Earth-radii thick,
stretching thousands of kilometers. A natural two-dimensional surface
of confined charged particles.
```

### Injection

- **Marker:** `Sixty thousand kilometers above your head`
- **Position:** Before the `<p>` containing the marker
- **Chapter:** the-wrong-substrate (spine)
- **Figure ID:** `fig-ms-earth`

### Manifest Entry

```yaml
- id: SVG-039
  name: ms-earth-teaching
  status: live
  source: preprocess.py
  category: Magnetosphere Teaching
  chapter: the-wrong-substrate
  figure_id: fig-ms-earth
  marker: "Sixty thousand kilometers above your head"
  animated: true
  animation_plan: "0270"
  animation: "Solar wind flow — dashed lines drift toward bow shock."
  description: "Earth's magnetosphere cross-section with 9 hover zones teaching structural names and behaviors."
```

---

## Phase 2: Jupiter Magnetosphere

### Key Differences from Earth

- **Much larger scale** — magnetopause at 42–75 Jupiter-radii
- **Self-powered** — rotation, not solar wind, drives the system
- **Io plasma torus** — dense volcanic ring along Io's orbit (the
  distinctive visual feature)
- **Ganymede** — nested sub-magnetosphere (small circle with own
  field lines)
- **Immense magnetotail** — extends nearly to Saturn's orbit

### Layout (schematic)

```
  ←wind←  ((( bow         /---
  ←wind←  (((    mpause  |  Io torus (ring)
  ←wind←  (((          JUPITER
  ←wind←  (((            | Ganymede (tiny MS)
  ←wind←  (((             \---
                             ════════════════ long tail
```

### Hover Zones (8)

1. **Jupiter** — 14x surface field, 18,000x moment, rotation-powered
2. **Io** — most volcanic body, 1 ton/s material ejected
3. **Io Plasma Torus** — ionized volcanic material swept into dense ring
4. **Magnetopause** — 42–75 Jupiter-radii, variable from plasma loading
5. **Aurora** — ~100 TW/hemisphere, 10,000–100,000x Earth's, rotation-driven
6. **Magnetotail** — extends nearly a billion km, almost to Saturn's orbit
7. **Inner Radiation Belt** — most intense in the solar system
8. **Ganymede Mini-Magnetosphere** — only moon with intrinsic field, nested MS

### Injection

- **Marker:** `Five hundred million kilometers away`
- **Position:** Before `<p>` containing marker
- **Figure ID:** `fig-ms-jupiter`

### Manifest Entry

```yaml
- id: SVG-040
  name: ms-jupiter-teaching
  status: planned
  source: preprocess.py
  category: Magnetosphere Teaching
  chapter: the-wrong-substrate
  figure_id: fig-ms-jupiter
  marker: "Five hundred million kilometers away"
  animated: true
  animation_plan: "0270"
  animation: "Solar wind flow + Io torus particle drift."
  description: "Jupiter's magnetosphere cross-section with 8 hover zones. Io torus, Ganymede sub-MS, rotation-powered."
```

---

## Phase 3: Saturn Magnetosphere

### Key Differences from Earth

- **Enceladus plumes** — water vapor, primary plasma source (the
  distinctive visual feature)
- **Disc-shaped field** — heavy plasma centrifugally confined to equator
- **Ring system** — absorbs charged particles, creates gaps in
  radiation belts
- **Titan** — thick atmosphere interacts with magnetosphere

### Layout (schematic)

```
  ←wind←  (((          /---
  ←wind←  (((    ===RINGS===
  ←wind←  (((       SATURN    Enceladus (plume)
  ←wind←  (((    ===RINGS===   ...Titan orbit
  ←wind←  (((          \---
                          ══════ disc-shaped tail
```

### Hover Zones (7)

1. **Saturn** — rapid rotation, centrifugal confinement, disc-shaped field
2. **Enceladus** — up to 1,000 kg/s water vapor through polar ice cracks
3. **Water-Group Plasma** — Enceladus material ionized, confined to equator
4. **Ring System** — absorbs particles, creates radiation belt gaps
5. **Current Sheets** — structured, 8–15 Saturn-radii
6. **Titan Orbit** — thick atmosphere interacts with magnetosphere
7. **Bow Shock** — "bowl-shaped" magnetosphere from axial geometry

### Injection

- **Marker:** `Saturn's magnetosphere is smaller`
- **Position:** Before `<p>` containing marker
- **Figure ID:** `fig-ms-saturn`

### Manifest Entry

```yaml
- id: SVG-041
  name: ms-saturn-teaching
  status: planned
  source: preprocess.py
  category: Magnetosphere Teaching
  chapter: the-wrong-substrate
  figure_id: fig-ms-saturn
  marker: "Saturn's magnetosphere is smaller"
  animated: true
  animation_plan: "0270"
  animation: "Solar wind flow + Enceladus plume drift."
  description: "Saturn's magnetosphere cross-section with 7 hover zones. Enceladus plumes, disc-shaped field, ring interaction."
```

---

## Implementation Steps (Phase 1)

### Step 1: CSS

Add `.ms-teaching` float styles and mobile collapse media query to
preprocess.py's CSS injection block (where `.inline-svg` styles live).

### Step 2: Earth SVG

Build `EARTH_MS_SVG` as a triple-quoted Python variable in preprocess.py.
Requirements:
- 9 `<g data-hover="..." style="cursor:pointer">` groups
- Each group contains the SVG elements for that structural region
- Tooltip text exactly as specified in Phase 1 Hover Zones above
- `<defs>` with reduced-motion style + any gradients/filters
- `<title>` accessibility element
- Solar wind `stroke-dasharray` + `stroke-dashoffset` animation
- Copper-colored plasma sheet prominently labeled "the Flat"

### Step 3: Injection Function

Add `inject_ms_diagrams(html)` to preprocess.py's pipeline. For
Phase 1, it handles Earth only (Jupiter/Saturn added in later phases).
Uses the "before `<p>`" insertion pattern described in Common
Specification.

### Step 4: Build + Test

- `make dev` — clean build
- Verify hover tooltips work on the Earth MS diagram
- Verify float:right layout — text wraps on left
- Verify mobile layout (narrow browser → centered)
- Verify reduced-motion → no animation

### Step 5: Manifest + Gallery

- Add SVG-039 entry to `gallery-manifest.yaml`
- Regenerate gallery: `python3 build/generate-gallery.py`

### Step 6: Deploy

- Commit, push, build

---

## What Does NOT Change

- reader.js (cover magnetosphere stays as-is)
- hover-definitions.yaml (magnetosphere hover popup stays as-is)
- Existing SVGs — no modifications
- Chapter text — no prose changes

---

## Acceptance Criteria

### Phase 1
- [ ] Earth MS diagram visible in "The Wrong Substrate" chapter
- [ ] Floated right, text wraps on left (desktop)
- [ ] Centered on mobile (< 700px)
- [ ] 9 hover zones produce tooltips on mouseover
- [ ] Tooltip text matches plan specification
- [ ] Plasma sheet labeled "the Flat" in copper
- [ ] Solar wind arrows animate (flow direction)
- [ ] `prefers-reduced-motion` → static
- [ ] `<title>` element present for accessibility
- [ ] `make dev` clean build
- [ ] SVG-039 in manifest + gallery updated
- [ ] Commit and push

### Phase 2 (added when Phase 1 accepted)
- [ ] Jupiter MS diagram with 8 hover zones
- [ ] Io plasma torus visually prominent
- [ ] Ganymede sub-MS visible

### Phase 3 (added when Phase 2 accepted)
- [ ] Saturn MS diagram with 7 hover zones
- [ ] Enceladus plumes visible
- [ ] Ring system interaction shown

---

## Generator Handoff (Phase 1)

```
You are the Generator.

Read Plan 0270 at ~/software/relinquishment/plans/0270-ms-teaching-imagemaps.md

Execute Phase 1 (Earth Magnetosphere Teaching Imagemap):

(1) Add .ms-teaching CSS (float:right + mobile collapse media query)
to preprocess.py's style injection block.

(2) Build EARTH_MS_SVG variable in preprocess.py: cross-section view,
viewBox 420×280, 9 hover zones each wrapped in <g data-hover="tooltip"
style="cursor:pointer">. Tooltip text is in the plan's Phase 1 Hover
Zones section — use it EXACTLY. Color palette in Common Specification.
Solar wind animated with stroke-dasharray + dashoffset. Include
<title> and reduced-motion <style> in <defs>.

(3) Add inject_ms_diagrams(html) function. Find marker text "Sixty
thousand kilometers above your head" — inject the float:right figure
BEFORE the <p> containing that marker. Wire into preprocess pipeline.

(4) Add SVG-039 to gallery-manifest.yaml.

(5) Run make dev. Run python3 build/generate-gallery.py.

(6) Commit and push. Report: hover zone count, byte delta, any issues.
```

---

*Plan 0270 written by Argus (Auditor), S63. Annealed MED LOW LOW.
Three-phase project: Earth (Phase 1, ready), Jupiter (Phase 2),
Saturn (Phase 3). Each phase independently deployable.*
