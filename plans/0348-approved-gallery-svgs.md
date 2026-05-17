# Plan 0348: Build 3 Approved Gallery SVGs (Gallery-First)

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** None
**Files:** `build/images/broken-bridges.svg`, `build/images/guided-deduction-paths.svg`, `build/images/convergence-spotlights.svg`
**Priority:** MEDIUM — approved designs never built; each counters a specific reader-resistance point

---

## Context

Three SVGs are approved in `build/gallery-manifest.yaml` but have no code. Each targets a specific argument weakness. This plan BUILDS the SVG files only. Injection into the book is a separate plan after visual review.

---

## Phase A: SVG-029 — broken-bridges.svg

**Output file:** `build/images/broken-bridges.svg`
**Gallery spec:** "Five tall silos (domains) standing apart. Broken dashed bridges between each pair with × at break. Caption: Bridging these fields — No journal. No career. No funding. No one's job."

**Design (580×380px):**
- 5 vertical rectangles (silos) evenly spaced, labeled: Topology, Autocatalysis, Computation, Plasma Physics, Condensed Matter
- Dashed lines between adjacent pairs, each broken at midpoint with a red ×
- Below silos, centered caption in italic: "No journal. No career. No funding. No one's job."
- Color scheme: silos in muted blue-gray (#5B7B94), × in red (#C44), background transparent
- Style: clean, schematic, no gradients, no animation

---

## Phase B: SVG-030 — guided-deduction-paths.svg

**Output file:** `build/images/guided-deduction-paths.svg`
**Gallery spec:** "Two paths from Classified knowledge. Top (red): Direct disclosure → CRIME → prosecution. Bottom (blue): Guided deduction → five published domains → student deduces → clean record."

**Design (600×280px):**
- Left origin node: "Classified Knowledge" (gray rounded box)
- Two diverging paths:
  - Top path (red #C44): arrow → "Direct Disclosure" → arrow → "CRIME" (bold) → arrow → "Prosecution"
  - Bottom path (blue #2B6CB0): arrow → "Guided Deduction" → arrow → "Published Domains" → arrow → "Student Deduces" → arrow → "Clean Record" (bold)
- Clean horizontal flow, left-to-right, nodes as rounded rectangles
- No animation — this is a static logical diagram

---

## Phase C: SVG-033 — convergence-spotlights.svg

**Output file:** `build/images/convergence-spotlights.svg`
**Gallery spec:** "Five spotlights from five domains converging on central question 'Can this support life?' Four strong beams, one weak (Topological QFT = the hard bridge)."

**Design (520×400px):**
- Central question in a circle: "Can this support life?"
- 5 spotlights radiating inward from edges, labeled:
  - Kauffman (Autocatalysis) — strong beam
  - Wolfram (Universality) — strong beam
  - Freedman (Topology) — strong beam
  - Hasslacher (Lattice Dynamics) — strong beam
  - Topological QFT — weak/dashed beam (the hard bridge)
- Beams as triangular gradients converging on center
- The weak beam is visually distinct: dashed outline, lighter fill, "?" label
- Color: warm gold (#D4A017) for strong beams, pale gray for weak beam

---

## Phase D: Verify files exist and are valid SVG

```bash
ls -la build/images/broken-bridges.svg build/images/guided-deduction-paths.svg build/images/convergence-spotlights.svg
# Open each in browser to verify visual correctness (report dimensions match spec)
python3 -c "
import xml.etree.ElementTree as ET
for f in ['build/images/broken-bridges.svg', 'build/images/guided-deduction-paths.svg', 'build/images/convergence-spotlights.svg']:
    ET.parse(f)
    print(f'{f}: valid XML')
"
```

---

## Do NOT

- Write inject functions in preprocess.py (separate plan, after visual review)
- Modify gallery-manifest.yaml (status updates are separate)
- Add animation
- Exceed specified dimensions
- Touch .tex files or preprocess.py

## Commit

`Plan 0348: build 3 gallery SVGs — broken-bridges, guided-deduction-paths, convergence-spotlights`
