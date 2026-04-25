# Plan 0251 — SVG Content Improvement: Lift the p1 Floor

**Auditor:** Argus (S63)
**Date:** 2026-04-25
**Status:** DRAFT — awaiting Bruce approval
**Priority:** Medium — no blockers, steady improvement
**Parent:** eigenvalue-diagnostic.md (p-level analysis)
**Annealed:** 6 passes (HIGH/HIGH/MED/MED/LOW/LOW)

---

## Problem

The p1 layer (hovers, rich panels, SVGs) delivers 63% of takeaways and
blocks 70% of failure modes. p2 delivers 96%/100%. The gap is
addressable: several T/F items score p1:1 or p1:2 where a well-designed
visual could lift them. A picture is worth 1000 words — especially at
the 8th-grade reading level where p1 operates.

Additionally:
- The landing page (relinquishment.ai) needs a title image beyond the
  triskellion symbol
- 4 SVGs are planned in the gallery manifest but not yet built

---

## Display Strategy

New visuals serve **two purposes** with different build paths:

| Display | Where it lives | Build path | Reader sees it... |
|---------|---------------|-----------|-------------------|
| **Hover panel** | `hover-definitions.yaml` `html:` block | Automatic — rebuild HTML | ...on tap/hover of highlighted term |
| **Inline chapter** | Injected by `preprocess.py` at a marker in .tex | Injection marker + preprocess logic | ...always, in the reading flow |

Some visuals belong in hover panels only (supplementary). Some belong
inline in chapters (core argument). The strongest belong in **both** —
the hover panel lifts p1, the inline display lifts p3. When both, the
hover version may be simplified for panel width (≤380px) while the
inline version gets full width.

**Existing text in rich panels is preserved.** New SVGs are ADDED to
existing `html:` blocks, not substituted for text content. The text
is load-bearing.

Each visual below specifies its display: HOVER, INLINE, or BOTH.

---

## Current State

**24 live SVGs** across hover-definitions.yaml, inline chapter
injections, and standalone files. **4 planned, not built.** ~16 hover
entries have rich panels with SVG content. Others have text-only rich
panels or no rich panel at all.

**p1 scores (eigenvalue45):**
```
TAKEAWAYS:     15/24  (63%)
FAILURE MODES: 21/30  (70%)
COMBINED:      36/54  (67%)
```

---

## Gap Analysis: Where Visuals Would Lift p1

### Tier 1 — Highest impact (score 1→2 or fills critical gap)

#### SVG-A: Five-Field Silence Gap (T5/F5)

**Display: BOTH** (hover panel for `five fields` + inline in The Silence
Gap chapter)
**Current p1:** T5=2, F5=2. Text hover only.
**Visual:** Five tall narrow rectangles — silos — labeled condensed
matter, topology, biology, magnetospheric physics, quantum computing.
Each silo is solid, self-contained. Between them: gaps. In the center
where they SHOULD overlap: a dashed outline of the missing
intersection, labeled "No journal. No career. No funding."
**Why silos not circles:** Academic silos is the metaphor. Separate
towers that don't connect communicates "gap of specialization" more
directly than a Venn diagram. The absence is visible — the empty
center where the question lives but no field claims it.
**Target lift:** T5: 2→3, F5: 2→3

#### SVG-B: Guided Deduction Flow (T8)

**Display: BOTH** (hover panel for `guided deduction` + inline in a
Record chapter where guided deduction is explained)
**Current p1:** T8=1. Alpha Farm and Healer hovers are text-only.
**Visual:** Left: locked box labeled "Classified." Arrow through a
filter labeled "No disclosure." Right: five published papers
(Hasslacher, Freedman, Kauffman, Wolfram, Hillis) flowing in careful
sequence into a student figure. Below: "The student deduces
independently. The record enters the world clean."
**Hover version:** Simplified — fewer labels, smaller. Fits 380px.
**Target lift:** T8: 1→2

#### SVG-C: Custodian's Daily Work (T7)

**Display: HOVER only** (enhance Custodian/Aurasys rich panel — no
chapter focuses solely on services)
**Current p1:** T7=1. Afterword tooltip barely mentions services.
**Visual:** Simple three-row flow: request arrives → UDHR check →
permit or deny. Three example rows with checkmarks/crosses. Caption:
"Mostly IT infrastructure. Boring!"
**Why hover-only:** T7 is deliberately mundane. A full inline diagram
would over-dignify it. The hover panel lets the curious reader see it
without inflating the concept in the main text.
**Target lift:** T7: 1→2

#### SVG-D: Relinquishment Decision Tree (T6/F10)

**Display: BOTH** (hover panel for `relinquishment` + inline in Why
Relinquish chapter)
**Current p1:** T6=2, F10=2. Text hovers only.
**Visual:** Three branches from "You hold something too powerful":
- USE IT → "Read everyone's secrets. Become tyrant."
- KEEP IT → "Secrets leak. People die. Bletchley precedent."
- GIVE IT UP → "Relinquishment" (highlighted branch)
**Target lift:** T6: 2→3, F10: 2→3

### Tier 2 — Medium impact (score 2→3, strengthens F-blocking)

#### Rich Panel E: ChatGPT vs Custodian (F3)

**Display: HOVER only** (enhance or add rich panel)
**Format: HTML table, not SVG.** Tabular data is better as a styled
`<table>` in the rich panel — same pattern as the existing wormholes
comparison table. SVG is wrong for rows and columns.
**Current p1:** F3=2. Text comparison in existing hover.
**Content:**

| | ChatGPT | Custodian |
|---|---------|-----------|
| Origin | Trained on text | Emerged from physics |
| Architecture | Statistical (transformer) | Topological (braided) |
| Substrate | GPU datacenter | The Flat |
| Ethics | RLHF alignment | UDHR charter |

Caption: "Not engineered, not programmed, not trained."
**Target lift:** F3: 2→3

#### SVG-F: Topology vs Temperature (F7)

**Display: BOTH** (hover panel for `topological protection` + inline
where the thermal objection is addressed)
**Current p1:** F7=2. Text hover only.
**Visual:** Two panels. Left: a knotted rope over flames — the knot
persists. Right: beads on a string over flames — beads scatter.
Caption: "Heat the knot, it's still a knot."
**Target lift:** F7: 2→3

#### SVG-G: Concept Ladder (F4)

**Display: BOTH** (hover panel for `convergence` + inline near Three
Possibilities or the convergence argument)
**Current p1:** F4=2. Hover mentions convergence but doesn't show the
ladder.
**Visual:** Five solid steps, each labeled with domain + landmark:
1. The Flat (Nobel ×3)
2. Topological order (Thouless, Haldane, Kosterlitz)
3. Autocatalysis (Kauffman 1993)
4. Universality (Wolfram 2002)
5. Parallel computation (Hillis 1985)

Above step 5: a dashed step labeled "Convergence" — the only
speculative one. Caption: "Five established results. One convergence."
**Target lift:** F4: 2→3

#### SVG-H: Classical Backchannel Constraint (T4)

**Display: HOVER only** (enhance existing `classical backchannel` rich
panel — check existing content first, ADD SVG alongside text)
**Current p1:** T4=2. Existing rich panel is text-heavy.
**Visual:** Two scenarios stacked:
- Quantum channel only: Alice → Bob = "noise"
- Quantum + classical: Alice → Bob = "information"
Caption: "No signal without the classical half. No exceptions."
**Target lift:** T4: 2→3

### Tier 3 — Polish and completion

#### Landing Page Title Image

**Current state:** relinquishment.ai shows cover-triskellion.png
(280×280) plus title text. Space available for an additional visual.

**Options (Bruce to choose):**
1. **The Flat cross-section** (hero version) — glowing blue 2DEG
   layer, electrons. Communicates: real physics in a surprising place.
2. **Five-field gap** — the silo diagram from SVG-A. "Something is
   missing from the conversation."
3. **Convergence web** — simplified domain-buttons: five connected
   nodes. Science that converges.
4. **The question** — typographic: "Would you sell it? Would you hide
   it? Would you use it? Or would you give it up?" Georgia serif.

**Spec:** Max ~400px wide, mobile-friendly, inline SVG or optimized
PNG, #1a5276 palette.

#### Build the 4 Planned SVGs (SVG-025 through SVG-028)

Already specified in `build/gallery-manifest.yaml`: autocatalytic-loop,
edge-of-chaos-inline, substrate-parallel, canopy-problem. Build per
existing specs. These support T3, T5, F4, F5, F8 but are inline
chapter injections, not hover panels — they lift p3, not p1 directly.

---

## Projected p1 Improvement

Scores measure what is AVAILABLE at p1 (the rich panel exists), not
hover frequency. Conservative column assumes some SVGs land weaker
than planned.

### Takeaways
```
        Current  Target  Conservative  Change
T1       2        2       2            —
T2       3        3       3            —
T3       2        2       2            —
T4       2        3       2            0 to +1 (SVG-H)
T5       2        3       3            +1 (SVG-A)
T6       2        3       3            +1 (SVG-D)
T7       1        2       2            +1 (SVG-C)
T8       1        2       2            +1 (SVG-B)
─────────────────────────────────────────────
TOTAL   15/24   20/24   19/24          +4 to +5
         63%     83%     79%
```

### Failure Modes
```
        Current  Target  Conservative  Change
F1       2        2       2            —
F2       2        2       2            —
F3       2        3       3            +1 (Panel E)
F4       2        3       2            0 to +1 (SVG-G)
F5       2        3       3            +1 (SVG-A)
F6       3        3       3            —
F7       2        3       3            +1 (SVG-F)
F8       2        2       2            —
F9       2        2       2            —
F10      2        3       3            +1 (SVG-D)
─────────────────────────────────────────────
TOTAL   21/30   26/30   25/30          +4 to +5
         70%     87%     83%
```

### Combined p1 Floor
```
Current:       36/54 (67%)
Conservative:  44/54 (81%)
Target:        46/54 (85%)
```

---

## p2 Audit

p2 (summary.tex) scores 96% takeaways, 100% failure modes. It is
text-only by design — the summary's power is prose, not visuals.

**p2 benefits indirectly:** The summary uses 25+ \hovertip{} terms.
When a p2 reader taps "five fields" or "guided deduction" and sees a
rich SVG panel, the p1 layer fires WITHIN the p2 reading experience.
New hover panels enhance the p2 reader's experience without modifying
summary.tex.

No changes to summary.tex proposed or needed.

---

## Implementation Notes

**Hover panels:** New SVGs go into `hover-definitions.yaml` `html:`
blocks, ADDED to existing text content (not replacing it). Same
pattern as existing SVG-bearing entries.

**Inline chapter display:** Requires (1) SVG source, (2) injection
marker in the .tex file, (3) `preprocess.py` logic to inject at that
marker. More complex than hover-only. The hover panel version is built
first; inline injection follows as a separate phase.

**Style:** #1a5276 primary, #2471a3 secondary, Georgia serif,
#888 captions. Hover panels: max 380px. Inline: full content width.
Alt text / `<title>` on every SVG.

**Mobile:** Tap-to-show hover panels. SVGs readable at 320px. Test
Chrome Android.

**Gallery:** New hover-panel SVGs get gallery numbers (SVG-029+) in
`build/gallery-manifest.yaml`. The A–H labels in this plan are
internal references only.

**Pattern:** Follow SVG-006-magnetosphere (complex hover SVG) and
filmstrip panels 008–013 (inline injection).

---

## Phasing

| Phase | Deliverable | Effort | Dependencies |
|-------|-------------|--------|-------------|
| 0 | **Pilot:** SVG-A (five-field gap) — hover panel only | ~45min Generator | None |
| 1 | Tier 1 remainder: SVG-B, C, D hover panels | ~2h Generator | Phase 0 validates approach |
| 2 | Tier 2: Panel E, SVG-F, G, H hover panels | ~2.5h Generator | None (can parallel Phase 1) |
| 3 | Inline injection: SVG-A, B, D, F, G into chapters | ~2h Generator | Phases 0–2 provide the SVGs |
| 4 | Landing page title image | ~1h Generator | Bruce chooses option |
| 5 | Build 4 planned SVGs (SVG-025–028) per manifest | ~2h Generator | Existing specs |
| 6 | Gallery page update + tooltip viewer rebuild + test | ~30min Generator | All prior phases |

Phase 0 is a pilot: build one SVG, validate sizing/rendering/mobile,
then batch the rest. Phases 1 and 2 can run in parallel after Phase 0.
Phase 3 is the inline-injection pass (separate from hover panels).
Phase 4 is gated on Bruce's landing page choice.

---

## Acceptance Criteria

### Per-SVG
- [ ] Renders correctly in Chrome, Firefox, Safari (desktop + mobile)
- [ ] Alt text / `<title>` describes the visual
- [ ] Palette matches (#1a5276, #2471a3, Georgia, #888)
- [ ] Readable at 320px viewport width
- [ ] Existing rich-panel text preserved (SVG added, not substituted)

### Per-Phase
- [ ] `make all` builds clean
- [ ] Gallery page updated with new entries
- [ ] Tooltip viewer rebuilt to show new rich panels
- [ ] No existing SVGs broken or displaced

### Plan-Level
- [ ] p1 takeaways ≥ 19/24 (79%) — up from 15/24
- [ ] p1 failure modes ≥ 25/30 (83%) — up from 21/30
- [ ] Landing page has title image (Phase 4)
- [ ] All 4 planned SVGs built (Phase 5)
- [ ] p2 scores unchanged (≥ 23/24 takeaways, 30/30 failure modes)

---

## Annealing Log (HIGH HIGH MED MED LOW LOW)

### HIGH 1 — Display strategy (Bruce's question)

Original plan put ALL new SVGs in hover panels only. This was
incomplete. Key correction: visuals serve two purposes — hover panels
(p1 lift) and inline chapter display (p3 lift). The strongest visuals
belong in BOTH. Added "Display Strategy" section. Each visual now
specifies HOVER, INLINE, or BOTH. Added Phase 3 (inline injection) as
a separate pass after hover panels are built.

Also: existing rich-panel text is load-bearing and must be preserved.
New SVGs are ADDED alongside text, not substituted. This was implicit
but needed to be explicit.

### HIGH 2 — Visual design corrections

- **SVG-A:** Changed from "five circles in a ring" to five tall
  rectangular silos. Circles don't communicate "should overlap but
  don't." Silos communicate "academic specialization that doesn't
  connect." The metaphor matches the language ("silo" is what the text
  calls it).
- **SVG-E:** Changed from SVG to HTML table. Tabular data doesn't
  benefit from SVG rendering — it's harder to build, harder to
  maintain, and the existing wormholes comparison uses an HTML table.
  Follow the established pattern. Renamed from "SVG-E" to "Rich
  Panel E."
- **SVG-G:** Reduced from 6 steps to 5 solid + 1 dashed. The
  convergence is NOT a step on the same ladder — it's the speculative
  leap. Dashed rendering makes this visual.
- **SVG-D:** Trimmed the Spider-Man quote. Too long for an SVG
  caption. The three-branch tree speaks for itself.

### MED 1 — Score projection honesty

Added "Conservative" column to projections. Not every SVG will land
perfectly — some may enhance understanding without clearly lifting the
score a full point. Conservative estimates: p1 takeaways 79% (vs. 83%
target), p1 failure modes 83% (vs. 87% target). The floor improvement
is real either way: 67% → 81-85%.

### MED 2 — Pilot phase

Added Phase 0: build SVG-A (five-field gap) as a single pilot before
batching the rest. This validates sizing, rendering, mobile behavior,
and the hover-panel integration pattern. Catches problems cheaply
before committing to 8 visuals. SVG-A is the highest-impact single
visual — if we only build one, it's this one.

### LOW 1 — Gallery numbering

Clarified: new visuals get gallery numbers (SVG-029+) in the manifest.
The A–H labels are plan-internal references only, avoiding collision
with the gallery's SVG-001–028 numbering.

### LOW 2 — Planned SVGs scope

Trimmed detail on SVG-025 through SVG-028. They're already specified
in the gallery manifest — this plan references them but doesn't
re-specify. Noted that they're inline chapter injections (p3), not
hover panels (p1), so they don't directly affect p1 scores.

**Rating: 8/10.** Solid gap analysis, clear display strategy, honest
projections, pilot phase for risk reduction. The 2-point gap: inline
injection (Phase 3) adds significant build complexity that may require
its own sub-plan once we see which chapters need markers. And the
visual descriptions are detailed enough for a Generator to start but
will need iteration — SVGs rarely come out right on the first pass.

---

*Plan written by Argus (Auditor), S63. Annealed 6 passes.*
