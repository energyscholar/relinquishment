# Plan 0252 — SVG-014 Fix: Drop All Four Blue Nodes Below Floor

**Auditor:** Argus (S63)
**Date:** 2026-04-25
**Status:** READY FOR GENERATOR
**Parent:** Plan 0251 Phase 2b (SVG-014 spec was correct, execution was wrong)

---

## Problem

Plan 0251 Phase 2b spec'd that ALL FOUR blue domains (Topo, TFT, CMP,
TQC) should hang below the floor line. The Generator only moved TQC
below — Topo/TFT/CMP remain at y=55/108/108, well above the floor at
y=335. Bruce: "all 4 blue domains are ALL sagging below the others,
as if barely attached."

## File

`/home/bruce/software/relinquishment/docs/gallery.html`

SVG-014 starts at the `<section id="SVG-014-inject-domain-buttons">`
section (around line 961).

## What to change

Replace the entire SVG inside SVG-014's `<div class="svg-container">`.

### Layout (ALL coordinates are exact)

**ViewBox:** `0 0 500 570` (current — keep)

**Floor line:** y=305 (move UP from current y=335 to give more room
below)

**Upper web (7 domains above floor):**

| Domain | Color | Position | Notes |
|--------|-------|----------|-------|
| Sol | #c0392b | (80, 80) | Red pair |
| NLD | #e74c3c | (80, 130) | |
| ACS | #e67e22 | (420, 80) | Orange pair |
| Auto | #f39c12 | (420, 130) | |
| CE | #8e44ad | (250, 180) | Purple pair, moved center-ish |
| Par | #a569bd | (250, 230) | |
| Mat | #b8860b | (160, 230) | Brown, near CE/Par |

**Below floor (4 blue domains — the hanging cluster):**

| Domain | Color | Position | Notes |
|--------|-------|----------|-------|
| Topo | #2471a3 | (250, 345) | Just below floor |
| TFT | #2980b9 | (180, 385) | Lower left |
| CMP | #3498db | (320, 385) | Lower right |
| TQC | #1a5276 | (250, 430) | Bottom of cluster |

### Edges

**Intra-cluster (solid, within pairs):**
- Sol↔NLD: solid red, stroke-width 1.5
- ACS↔Auto: solid orange, stroke-width 1.5
- CE↔Par: solid purple, stroke-width 1.5
- Topo↔TFT, Topo↔CMP, TFT↔CMP, Topo↔TQC, TFT↔TQC, CMP↔TQC:
  solid blue (#2471a3), stroke-width 1.5

**Cross-cluster ABOVE floor (published):**
- NLD↔ACS: solid grey (#777), stroke-width 1.0 (published)

**Cross-cluster ABOVE floor (dashed = not yet built):**
- CE↔NLD: dashed #bbb
- CE↔ACS: dashed #bbb
- Par↔Auto: dashed #bbb
- Mat↔NLD: dashed #bbb

**THREE HANGING BRIDGES (cross the floor — load-bearing):**
- Mat→CMP: **SOLID** (#777, stroke-width 1.5) — published bridge.
  "The one thread that holds." Use `<path>` with quadratic bezier,
  slight downward sag: `M 160,230 Q 240,340 320,385`
- CE→Topo: DASHED (#bbb, stroke-width 0.8, stroke-dasharray="6,4")
  `M 250,180 Q 250,260 250,345` (nearly vertical, small sag)
- ACS→TQC: DASHED (#bbb, stroke-width 0.8, stroke-dasharray="6,4")
  `M 420,80 Q 380,260 250,430` (long diagonal, more sag)

### Visual treatment of hanging cluster

- Blue nodes below floor should have slightly lower opacity (0.85)
  compared to upper nodes (1.0) — they're in shadow
- The floor line should be labeled: small text "published cross-references"
  above line, "silence gap" below line (both in #999, font-size 8)
- Blue intra-cluster edges below floor: full opacity, showing the
  cluster is internally strong

### Tooltips (data-hover)

Keep all existing tooltips EXCEPT:
- TQC: change to "Topological quantum computation — braiding
  non-Abelian anyons for fault-tolerant gates. Freedman-Kitaev-Wang
  2002. The convergence point."

### Caption

Keep: "One thread holds. Cut it, and the argument falls apart."
Keep: "after Kauffman (1993)"
Position below TQC at ~y=460.

### Figcaption / title

Update `<title>` to: "Kauffman's buttons and threads, mapped to eleven
scientific domains. Seven domains form a web of published cross-references
above the floor. The topological convergence cluster — four domains —
hangs below, connected by one solid thread and bridges not yet built."

### Legend

Keep current 5-cluster legend. Move to fit below caption (~y=480+).
Change "missing bridge" to "not yet built."

### What NOT to change

- Do not touch any other SVG
- Do not change the section id, header, or meta div
- Do not change the hover-definitions.yaml version (SVG-007 is separate)

## Acceptance Criteria

- [ ] ALL FOUR blue nodes (Topo, TFT, CMP, TQC) are below the floor line
- [ ] Seven non-blue domains are above the floor line, connected
- [ ] Mat→CMP is a SOLID bridge crossing the floor (the one thread)
- [ ] CE→Topo and ACS→TQC are DASHED bridges crossing the floor
- [ ] Blue cluster is fully connected internally (6 edges among 4 nodes)
- [ ] Floor line has "published" / "silence gap" labels
- [ ] TQC tooltip updated (no "single thread" reference)
- [ ] Legend says "not yet built" instead of "missing bridge"
- [ ] Renders cleanly at 320px mobile viewport
- [ ] No other SVGs affected

---

*Plan 0252 written by Argus (Auditor), S63.*
