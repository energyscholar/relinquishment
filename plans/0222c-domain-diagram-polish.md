# Plan 0222c — Domain Diagram Rebuild

**Status:** COMPLETE (verified S63 audit)
**Author:** Auditor
**Priority:** Medium (Bruce review active)
**EV:** Stable — visual refinement + correctness fix, no structural/content changes
**Scope:** `build/preprocess.py` (`inject_domain_buttons()` SVG constant only)
**Phase:** 3 of 3 (0222a scaffold → 0222b filmstrip polish → 0222c domain rebuild)

## Purpose

The current 11-domain diagram has **wrong domain names** (NN, Neuro don't exist in the canonical list), **wrong cluster color assignments** (NLD grouped with Mat instead of Solitons), and **no legend**. This plan corrects the domain identities, rebuilds the bridge network from published literature, adds a color-coded legend, and reshapes the layout for mobile legibility. The diagram must visually rhyme with the 0222b filmstrip (dashed=missing, dangler=fragile).

## The Canonical Eleven Domains

Source: Silence Gap passage (line 32) + Plan 0149. The manuscript says: *"the five fields become eleven domains in five clusters."*

| Cluster | Domains | Abbrev |
|---------|---------|--------|
| **Topological** (4) | Topology, Topological Field Theory, Condensed Matter, TQC | Topo, TFT, CMP, TQC |
| **Nonlinear** (2) | Solitons, Nonlinear Dynamics | Sol, NLD |
| **Origin** (2) | Autocatalysis, Autopoiesis | ACS, Auto |
| **Computation** (2) | Universality, Parallel Computation | CE, Par |
| **Materials** (1) | Materials Science | Mat |

### What's wrong in the current SVG:
- **"NN" → "Topo"** (Topology — pure mathematics, knot theory, Freedman)
- **"Neuro" → "Sol"** (Solitons — Hasslacher's lattice-gas dynamics)
- **NLD wrong cluster** — currently red with Mat. Should be red with Sol.
- **Mat singleton** — needs its own color (tan), not paired with NLD
- **Green cluster gone** — no such cluster in canonical list

---

## Exact Layout

**SVG dimensions:** `viewBox="0 0 500 510"` rendered `width="460" height="370"`

### Button positions (cx, cy), radius=16:

**Topological cluster — triangle + pendant at center:**

| Button | cx | cy | fill | stroke | Label font |
|--------|----|----|------|--------|------------|
| Topo | 250 | 55 | #2471a3 | #1a5276 | 7px |
| TFT | 190 | 108 | #2980b9 | #2471a3 | 7px |
| CMP | 310 | 108 | #3498db | #2980b9 | 7px |
| TQC | 250 | 220 | #1a5276 | #0d2f4b | 7px |

Topo/TFT/CMP form a **tight triangle** at the top. TQC hangs **far below** on three long solid threads — a pendant from the triangle. The visual: connected but extended, precarious. TQC is the darkest blue because it's the deepest, most consequential domain.

**Nonlinear cluster — stacked pair, far left:**

| Button | cx | cy | fill | stroke | Label font |
|--------|----|----|------|--------|------------|
| Sol | 58 | 82 | #c0392b | #962d22 | 7px |
| NLD | 58 | 140 | #e74c3c | #c0392b | 7px |

**Origin cluster — stacked pair, far right (mirrors Nonlinear):**

| Button | cx | cy | fill | stroke | Label font |
|--------|----|----|------|--------|------------|
| ACS | 442 | 82 | #e67e22 | #bf6516 | 7px |
| Auto | 442 | 140 | #f39c12 | #d4860b | 7px |

**Computation cluster — stacked pair, lower right:**

| Button | cx | cy | fill | stroke | Label font |
|--------|----|----|------|--------|------------|
| CE | 372 | 228 | #8e44ad | #6c3483 | 7px |
| Par | 372 | 278 | #a569bd | #8e44ad | 7px |

**Materials — singleton, lower left:**

| Button | cx | cy | fill | stroke | Label font |
|--------|----|----|------|--------|------------|
| Mat | 110 | 252 | #b8860b | #8b6508 | 7.5px |

### Compositional logic:

```
  Sol ·              Topo               · ACS
  NLD ·         TFT ····· CMP          · Auto
                     |
                     |  (three solid blue threads)
                     |
                    TQC          CE
                                 Par
       Mat

  ═══════════════════ floor ═══════════════════
              [legend below]
```

- **Topological hub at center-top:** densest web, fully connected — it's the keystone
- **Nonlinear and Origin mirror each other** left/right — symmetric pairs, same height
- **TQC pendant:** 112px below the triangle, connected by 3 solid threads reaching up — dramatic, precarious
- **Computation lower-right:** near TQC horizontally but NOT connected — proximity ≠ connection
- **Materials lower-left, solo:** the engineering singleton, far from the theory clusters
- **Negative space between clusters = the silence gap**

---

## Thread Specifications

### SVG draw order (bottom to top):
1. Floor line
2. Dashed bridges (lowest layer — ghostly background)
3. Cross-cluster solid threads (midground)
4. Intra-cluster solid threads (foreground)
5. Buttons (cover thread endpoints)
6. Button labels
7. TQC ▼ arrow
8. Captions
9. Legend

### All 16 threads:

**6 solid blue — intra-Topological (fully connected triangle + pendant):**
`stroke="#2471a3" stroke-width="1.5" opacity="0.65"`

| # | From → To | Visual |
|---|-----------|--------|
| 1 | Topo(250,55) → TFT(190,108) | short diagonal left |
| 2 | Topo(250,55) → CMP(310,108) | short diagonal right |
| 3 | TFT(190,108) → CMP(310,108) | horizontal base of triangle |
| 4 | Topo(250,55) → TQC(250,220) | long vertical pendant thread |
| 5 | TFT(190,108) → TQC(250,220) | long diagonal pendant left |
| 6 | CMP(310,108) → TQC(250,220) | long diagonal pendant right |

Threads 1-3 form the tight triangle. Threads 4-6 are the pendant threads — visibly longer, reaching down to TQC. The contrast (tight triangle vs long pendant) creates the precariousness.

**3 solid — intra-cluster pairs:**

| # | From → To | Color | stroke-width | opacity |
|---|-----------|-------|-------------|---------|
| 7 | Sol(58,82) → NLD(58,140) | #c0392b (red) | 1.5 | 0.65 |
| 8 | ACS(442,82) → Auto(442,140) | #e67e22 (orange) | 1.5 | 0.65 |
| 9 | CE(372,228) → Par(372,278) | #8e44ad (purple) | 1.5 | 0.65 |

Vertical threads within each pair. Short, tight, confident.

**2 solid grey — cross-cluster published bridges:**
`stroke="#777" stroke-width="1.0" opacity="0.4"`

| # | From → To | What it represents |
|---|-----------|-------------------|
| 10 | NLD(58,140) → ACS(442,82) | Edge-of-chaos criticality (Langton 1990, Kauffman 1993) |
| 11 | CMP(310,108) → Mat(110,252) | Semiconductor fabrication literature |

Thread 10 crosses the **full width** of the diagram — it's the longest thread, passing through the Topological hub. This is intentional: the criticality bridge literally runs through the center. Low opacity keeps it from cluttering.

Thread 11 is a long diagonal from upper-right to lower-left.

**5 dashed grey — missing bridges:**
`stroke="#bbb" stroke-width="0.8" opacity="0.3" stroke-dasharray="5,3"`

| # | From → To | What's missing |
|---|-----------|---------------|
| 12 | Sol(58,82) → CMP(310,108) | Solitons ↔ anyons — same math, separate literatures |
| 13 | ACS(442,82) → TQC(250,220) | Kauffman closure ↔ anyon fusion — structural analogy, not peer-reviewed |
| 14 | Par(372,278) → ACS(442,82) | Hillis ↔ Kauffman — network ≈ emergence architecture |
| 15 | CE(372,228) → TQC(250,220) | Wolfram universality ↔ braiding universality — no equivalence proof |
| 16 | Mat(110,252) → ACS(442,82) | Substrates ↔ autocatalysis — unexamined |

These are barely visible — whispers of connections that don't exist yet. The reader's eye sees them if they look, but they don't compete with the solid threads.

---

## Floor, Captions, Arrow

**Floor line:** `y1="335" y2="335"` x1="25" x2="475", stroke="#ccc" dasharray="4,4" width="1"

**TQC arrow:** `▼` at (250, 248), font-size="9", fill="#999" — points down from TQC toward the floor.

**Caption line 1:** (250, 358) `"One thread holds. Cut it, and the argument falls apart."` — Georgia 10px, #555
**Caption line 2:** (250, 373) `"after Kauffman (1993)"` — Georgia 9px, #999

---

## Legend (below floor)

Three rows, two columns. Starts at y=395.

**Row 1 (y=398):**
- Left: circle r=5 at (40,398) fill=#2471a3 + text (55,402) **"Topological"** bold 8px #555 + text (55,414) "Topo · TFT · CMP · TQC" 7px #888
- Right: circle r=5 at (275,398) fill=#e67e22 + text (290,402) **"Origin"** bold 8px #555 + text (290,414) "ACS · Auto" 7px #888

**Row 2 (y=430):**
- Left: circle r=5 at (40,430) fill=#c0392b + text (55,434) **"Nonlinear"** bold 8px #555 + text (55,446) "Sol · NLD" 7px #888
- Right: circle r=5 at (275,430) fill=#8e44ad + text (290,434) **"Computation"** bold 8px #555 + text (290,446) "CE · Par" 7px #888

**Row 3 (y=462):**
- Left: circle r=5 at (40,462) fill=#b8860b + text (55,466) **"Materials"** bold 8px #555 + text (55,478) "Mat" 7px #888
- Right: line solid (275,465) to (300,465) stroke="#777" width="1.2" + text (308,469) "published" 7.5px #888 — then line dashed (275,482) to (300,482) stroke="#bbb" dasharray="5,3" width="0.8" + text (308,486) "missing bridge" 7.5px #888

---

## SVG Title (tooltip)

```
Kauffman's buttons and threads, mapped to eleven scientific domains
in five clusters. Solid threads: published cross-references. Dashed:
bridges no one has built. TQC is connected within its cluster but
isolated from the wider argument.
```

## Figcaption (HTML below SVG)

```
The same metaphor, applied to this book. Eleven domains in five clusters,
connected by published cross-references. The silence gap is visible:
dashed lines mark bridges no one has built.
```

---

## Artistic Direction

**The diagram should feel like a constellation map** — precise points of light connected by threads, surrounded by darkness. The negative space is the story.

- **Opacity layering creates depth:** Intra-cluster threads (0.65) are foreground. Cross-cluster published (0.4) are midground. Missing bridges (0.3) are background whispers. The eye reads the clusters first, then discovers the bridges, then notices the gaps.

- **The TQC pendant is the emotional center.** Three solid blue threads reach up from TQC to the triangle — it's connected, but hanging. The ▼ points down. The reader feels: *this one could fall.*

- **The NLD↔ACS thread crossing the hub is intentional.** The longest thread in the diagram passes straight through the Topological center. That's the criticality bridge — it literally runs through everything. Low opacity keeps it from cluttering but the geometry speaks.

- **Proximity ≠ connection:** CE(372,228) is close to TQC(250,220) — nearly the same height. But the line between them is dashed. Close doesn't mean connected. This echoes the filmstrip's floor-center buttons (4 and 13) sitting in the middle of a lifted web, unattached.

- **Left-right symmetry of pairs:** Nonlinear (left, red) mirrors Origin (right, orange) at the same heights. This visual rhyme says: these are parallel structures in different domains. The symmetry makes the asymmetry of their connections more visible.

- **Materials is alone.** Lower left, single tan dot. The only singleton cluster. The engineering discipline that builds everything but connects to almost nothing in the theoretical literature. Its isolation is data.

---

## Scope Constraints

- **Only** the domain diagram SVG constant in `inject_domain_buttons()`
- No injection logic changes, no new functions, no manuscript changes
- Hover tooltip in `hover-definitions.yaml` stays unchanged
- Injection marker `'five published research streams had independently matured'` unchanged

## Acceptance Tests

1. **11 correct domain buttons:** Topo, TFT, CMP, TQC, Sol, NLD, ACS, Auto, CE, Par, Mat
2. **5 cluster colors:** Blue (4), Red (2), Orange (2), Purple (2), Tan (1)
3. **No green cluster** (NN/Neuro removed)
4. **Thread count:** 11 solid + 5 dashed = 16 total
5. **Intra-Topological fully connected:** 6 solid blue threads
6. **TQC pendant:** TQC y-coordinate ≥ 200 (hangs below triangle)
7. **Legend present:** Color-coded key naming all 5 clusters with abbreviations
8. **Thread legend:** Solid and dashed line samples with labels
9. **Mobile legible:** Button labels ≥7px, legend text ≥7px
10. **Build succeeds:** `make html` exits 0
11. **Filmstrip unaffected:** 6-panel filmstrip still renders
12. **Figcaption updated** per plan

## Handoff Prompt

```
You are the Generator for Plan 0222c (domain diagram rebuild).

Read: ~/software/relinquishment/plans/0222c-domain-diagram-polish.md

The 11-domain Kauffman diagram in `build/preprocess.py` function
`inject_domain_buttons()` (line ~2581) needs a full rebuild. The plan
has exact (cx,cy) coordinates for all 11 buttons, hex codes for every
color, all 16 thread endpoints, draw order, legend pixel positions,
and artistic direction. Follow the plan precisely — it is annealed.

Key changes: NN→Topo, Neuro→Sol. Green cluster eliminated. NLD moves
to Nonlinear (red). Mat becomes singleton (tan). TQC drops to (250,220)
as pendant below tight Topological triangle. 6 solid blue intra-cluster,
3 solid cluster-pair, 2 solid grey cross-cluster, 5 dashed missing.
Legend below floor with cluster key + thread type samples.

SVG viewBox="0 0 500 510", rendered width="460" height="370".
Button r=16, labels 7-7.5px. Respect draw order in plan.

After: `make dev`, commit as "Plan 0222c: domain diagram rebuild —
correct domains, literature-grounded bridges, legend", push.
Report completion ≤5 lines with deviations.
```
