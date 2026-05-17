# Plan 0348: Build 3 Approved Gallery SVGs

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** None
**Files:** `build/preprocess.py`
**Priority:** MEDIUM — approved designs never built; each counters a specific reader-resistance point

---

## Context

Three SVGs are approved in `build/gallery-manifest.yaml` but have no code. Each targets a specific argument weakness identified in Plan 0251. They need inject functions written and called from `__main__`.

---

## Phase A: SVG-029 — broken-bridges (Silence Gap)

**Target:** Chapter `the-silence-gap` (ID: `spine:silence-gap` — note no "the-" prefix in HTML ID)
**Marker text:** `"nobody's job required crossing"` (confirmed in built HTML line 1209)
**Figure ID:** `fig-broken-bridges`
**Gallery spec:** "Five tall silos (domains) standing apart. Broken dashed bridges between each pair with × at break. Caption: Bridging these fields — No journal. No career. No funding. No one's job."

**Design (inline SVG, 580×380px):**
- 5 vertical rectangles (silos) evenly spaced, labeled: Topology, Autocatalysis, Computation, Plasma Physics, Condensed Matter
- Dashed lines between adjacent pairs, each broken at midpoint with a red ×
- Below silos, centered caption in italic: "No journal. No career. No funding. No one's job."
- Color scheme: silos in muted blue-gray (#5B7B94), × in red (#C44), background transparent
- Style: clean, schematic, no gradients

**Implementation (follow pattern of `inject_silence_gap_illustration` at line 4458):**
1. Add `BROKEN_BRIDGES_SVG` constant (after existing SVG constants, before inject functions)
2. Add `inject_broken_bridges(html_path)` function:
   - Read HTML, find `id="spine:silence-gap"`, find marker text within chapter
   - Build `<figure id="fig-broken-bridges" class="inline-svg">` wrapping the SVG
   - Insert after the marker paragraph
3. Add call `inject_broken_bridges(sys.argv[2])` in `__main__` block (after other inject calls, ~line 5458)

---

## Phase B: SVG-030 — guided-deduction-two-paths (Tradecraft)

**Target:** Chapter `the-braid` (ID: `spine:the-braid` — this is where guided deduction is explained)
**Marker text:** `"guided deduction"` hover-term at HTML line ~1633. Specifically target the paragraph containing "find a physicist outside the"
**Figure ID:** `fig-guided-deduction-paths`
**Gallery spec:** "Two paths from Classified knowledge. Top (red): Direct disclosure → CRIME → prosecution. Bottom (blue): Guided deduction → five published domains → student deduces → clean record."

**Design (inline SVG, 600×280px):**
- Left origin node: "Classified Knowledge" (gray box)
- Two diverging paths:
  - Top path (red #C44): arrow → "Direct Disclosure" → arrow → "CRIME" (bold) → arrow → "Prosecution"
  - Bottom path (blue #2B6CB0): arrow → "Guided Deduction" → arrow → "Published Domains" → arrow → "Student Deduces" → arrow → "Clean Record" (bold)
- Clean horizontal flow, left-to-right, nodes as rounded rectangles
- No animation needed — this is a static logical diagram

**Implementation (same pattern as Phase A):**
1. Add `GUIDED_DEDUCTION_PATHS_SVG` constant
2. Add `inject_guided_deduction_paths(html_path)` function targeting `id="spine:the-braid"`
3. Add call `inject_guided_deduction_paths(sys.argv[2])` in `__main__` block

---

## Phase C: SVG-033 — convergence-spotlights (Convergence)

**Target:** Chapter `genesis` (ID: `spine:genesis`)
**Marker text:** `"five published research streams"` or `"five scientific fields"` (verify — note this chapter already has the five-thread-convergence SVG, so place AFTER it)
**Figure ID:** `fig-convergence-spotlights`
**Gallery spec:** "Five spotlights from five domains converging on central question 'Can this support life?' Four strong beams, one weak (Topological QFT = the hard bridge)."

**Design (inline SVG, 520×400px):**
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

**Implementation (same pattern as Phase A):**
1. Add `CONVERGENCE_SPOTLIGHTS_SVG` constant
2. Add `inject_convergence_spotlights(html_path)` function targeting `id="spine:genesis"`
3. Add call `inject_convergence_spotlights(sys.argv[2])` in `__main__` block
4. **IMPORTANT:** The existing five-thread-convergence SVG uses marker "five published research streams had independently matured". Use a LATER marker in the same chapter — try `"Can this support life"` or `"five domains"` (verify in HTML). Place this SVG after the five-thread-convergence one.

---

## Phase D: Verify

```bash
make html 2>&1 | grep -i "broken-bridges\|guided-deduction-paths\|convergence-spotlights\|WARNING"
```

Expected:
- "broken-bridges SVG injected" (or similar)
- "guided-deduction-paths SVG injected"
- "convergence-spotlights SVG injected"
- No new WARNINGs

Then:
```bash
grep -c 'fig-broken-bridges\|fig-guided-deduction-paths\|fig-convergence-spotlights' docs/Relinquishment.html
```
Expected: 3

---

## Do NOT

- Modify existing inject functions or SVGs
- Change gallery-manifest.yaml (status updates are separate)
- Add animation (these are static diagrams)
- Touch .tex files
- Exceed 600px width (mobile reading constraint)

## Commit

`Plan 0348: build 3 approved gallery SVGs — broken-bridges, guided-deduction-paths, convergence-spotlights`
