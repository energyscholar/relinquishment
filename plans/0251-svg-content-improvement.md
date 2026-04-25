# Plan 0251 — SVG Content Improvement: Visuals That Teach, Delight, and Deliver

**Auditor:** Argus (S63)
**Date:** 2026-04-25
**Status:** DRAFT — awaiting Bruce approval
**Priority:** Medium — no blockers, steady improvement
**Parent:** eigenvalue-diagnostic.md (p-level analysis)
**Annealed:** 8 passes (HIGH/HIGH/MED/MED/LOW/LOW/MED/MED)

---

## Problem

The book has 24 SVGs, most in hover panels. They're good at what they
do — but they all serve the same purpose: concept diagrams for physics.
The book also tells stories, poses ethical questions, draws surprising
parallels, and has moments of cinematic intensity. None of that has
visuals.

Additionally, the p1 layer delivers only 63% of takeaways and 70% of
failure modes. Several T/F items score p1:1 or p1:2 where a
well-designed visual could lift them.

This plan addresses both: visuals that lift engineering scores AND
visuals that make the reader stop, look, and feel something. A picture
is worth 1000 words — for understanding, for pacing, and for fun.

Also:
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

## The Visuals

Three categories: **understand** (helps the reader GET a concept),
**feel** (narrative energy, emotional weight, wonder), **deliver**
(lifts a specific T/F score at p1). The best visuals do more than one.

### Tier 1 — Build these first

#### Five-Field Silos (T5/F5 + understand)

**Display: BOTH** (hover panel for `five fields` + inline in The Silence
Gap chapter)
**Visual:** Five tall narrow rectangles — silos — labeled condensed
matter, topology, biology, magnetospheric physics, quantum computing.
Each solid, self-contained. Between them: gaps. In the center where
they SHOULD overlap: a dashed outline of the missing intersection,
labeled "No journal. No career. No funding."
**Why silos not circles:** Academic silos is the metaphor. Towers that
don't connect. The absence is visible.
**Why it's here:** Both engineering (T5/F5 lift to 3) AND understanding.
The concept "gap of specialization" is abstract until you see it.

#### Guided Deduction Flow (T8 + understand)

**Display: BOTH** (hover for `guided deduction` + inline in Record)
**Visual:** Left: locked box "Classified." Filter: "No disclosure."
Right: five published papers (Hasslacher, Freedman, Kauffman, Wolfram,
Hillis) flowing in careful sequence. Below: student with lightbulb.
"The student deduces independently. The record enters the world clean."
**Hover version:** Simplified for 380px panel width.
**Why it's here:** T8 is the weakest p1 score (1). But more than that —
guided deduction is the MECHANISM of the entire story. Every reader
who gets this diagram understands WHY the book exists.

#### Relinquishment Decision Tree (T6/F10 + feel)

**Display: BOTH** (hover for `relinquishment` + inline in Why Relinquish)
**Visual:** Three branches from "You hold something too powerful":
- USE IT → "Read everyone's secrets."
- KEEP IT → "Secrets leak. People die."
- GIVE IT UP → "Relinquishment" (highlighted)
**Why it's here:** Engineering (T6/F10 lift). But the real reason is
emotional — the reader SEES there's no good option. The weight of the
decision becomes visual. This is the ethical core of the book.

#### Knot in Flames (F7 + fun)

**Display: BOTH** (hover for `topological protection` + inline where
thermal objection is addressed)
**Visual:** Two panels. Left: knotted rope over flames — knot persists.
Right: beads on a string over flames — beads scatter.
Caption: "Heat the knot, it's still a knot."
**Why it's here:** Engineering (F7 lift). But it's also fun — the
image is vivid, intuitive, and memorable. A reader who forgets
everything else might remember this.

#### Concept Ladder (F4 + understand)

**Display: BOTH** (hover for `convergence` + inline near Three
Possibilities)
**Visual:** Five solid steps + one dashed:
1. The Flat (Nobel ×3)
2. Topological order (Thouless, Haldane, Kosterlitz)
3. Autocatalysis (Kauffman 1993)
4. Universality (Wolfram 2002)
5. Parallel computation (Hillis 1985)
6. → Convergence (dashed — the speculation)
Caption: "Five established results. One convergence."
**Why it's here:** F4 lift, but also the clearest single image of what
the book's scientific argument IS. A reader who sees this staircase
understands the structure of the claim.

### Tier 2 — Understanding and delight

These visuals aren't driven by T/F scores. They're here because they
make the book better — clearer, more alive, more fun.

#### Hydrothermal Vent Parallel (wonder)

**Display: BOTH** (hover for `hydrothermal vent` or `Alvin` + inline
in The White Hot Secret section of summary or relevant chapter)
**Visual:** Side by side. Left: ocean floor, dark, crushing pressure,
tube worms thriving around a vent. Label: "1977 — no one expected
this." Right: the Flat, thin blue layer, braiding patterns, question
marks where life might be. Label: "20?? — ?"
Caption: "We found life where we didn't expect it once before."
**Why it's here:** The Alvin analogy is one of the summary's most
powerful moments. The parallel — lightless, hostile, teeming — is the
kind of thing a visual makes VISCERAL. It's not about a T/F score.
It's about wonder.

#### Anthill Emergence (understand)

**Display: BOTH** (hover for new or enhanced entry + inline in The
Custodian section of summary or relevant chapter)
**Visual:** Cross-section of an anthill. Individual ants running simple
local rules (follow scent, move crumb, pass signal). Arrows showing
local actions. Above ground: the complex structure that emerges —
nurseries, waste sorting, humidity regulation. No single ant knows
the plan.
Caption: "Nothing designs it. It emerges."
**Why it's here:** Emergence is the hardest concept in the book for GA
readers. The anthill analogy is already in the summary text. A visual
makes it click. Once a reader GETS emergence, they get Custodian.

#### HALO Silhouette (feel)

**Display: INLINE only** (section opener for The Mentor, or chapter
header for a Record chapter introducing Healer)
**Visual:** Small silhouette figure — arms out, freefall — against a
gradient sky that goes from blue at the bottom to near-black at the
top (stratosphere). Tiny. Vast sky. No parachute visible yet.
Caption: none needed — the text carries it.
**Why it's here:** Pure narrative energy. The summary describes Healer
falling from the sky; this makes the reader FEEL the character before
meeting him. It's also a style departure — the book's first figurative
image, signaling "this section is about a person, not a concept."
**Note:** This is a stylistic choice — all existing SVGs are concept
diagrams. Bruce decides whether the book includes figurative imagery.

### Tier 3 — Optional / if time allows

#### ChatGPT vs Custodian (F3)

**Display: HOVER only.** Format: HTML table (not SVG — tables aren't
diagrams). The existing text comparison works; this is a polish item.
**Target lift:** F3: 2→3

#### Classical Backchannel (T4)

**Display: HOVER only.** Alice→Bob diagram. The existing text-heavy
rich panel is adequate. Enhancement if time allows.
**Target lift:** T4: 2→3

#### Custodian's Daily Work (T7) — DEMOTED from Tier 1

The text "Mostly IT infrastructure. Boring!" is funnier and more
effective WITHOUT a diagram. A flowchart makes it less boring, which
undermines the point. T7's mundanity is a feature, not a problem to
solve with a visual. **CUT unless Bruce disagrees.**

### Tier 4 — Landing page + planned gallery SVGs

#### Landing Page Title Image

**Options (Bruce to choose):**
1. **The Flat cross-section** (hero version) — glowing blue 2DEG,
   electrons. "Real physics in a surprising place."
2. **Five-field gap** — the silo diagram. "Something is missing."
3. **Convergence web** — simplified domain-buttons.
4. **The question** — typographic: "Would you sell it? Would you hide
   it? Would you use it? Or would you give it up?"

**Spec:** Max ~400px wide, mobile-friendly, inline SVG or optimized
PNG, #1a5276 palette.

#### Build the 4 Planned SVGs (SVG-025 through SVG-028)

Already specified in `build/gallery-manifest.yaml`: autocatalytic-loop,
edge-of-chaos-inline, substrate-parallel, canopy-problem. Build per
existing specs. Inline chapter injections — lift p3, not p1 directly.

---

## Projected p1 Improvement

Tier 1 visuals have T/F targets. Tier 2 visuals improve engagement and
understanding without targeting specific scores (though hydrothermal
vent may nudge T3/F8). Conservative column assumes Tier 3 items aren't
built.

### Takeaways
```
        Current  Tier 1 only  + Tier 3    Source
T1       2        2            2           —
T2       3        3            3           —
T3       2        2            2           — (vent parallel supports, doesn't lift)
T4       2        2            3           Tier 3: backchannel
T5       2        3            3           Five-field silos
T6       2        3            3           Decision tree
T7       1        1            1           DEMOTED — text is funnier
T8       1        2            2           Guided deduction flow
──────────────────────────────────────────────────
TOTAL   15/24   18/24        19/24
         63%     75%          79%
```

### Failure Modes
```
        Current  Tier 1 only  + Tier 3    Source
F1       2        2            2           —
F2       2        2            2           —
F3       2        2            3           Tier 3: ChatGPT table
F4       2        3            3           Concept ladder
F5       2        3            3           Five-field silos
F6       3        3            3           —
F7       2        3            3           Knot in flames
F8       2        2            2           —
F9       2        2            2           —
F10      2        3            3           Decision tree
──────────────────────────────────────────────────
TOTAL   21/30   24/30        26/30
         70%     80%          87%
```

### Combined p1 Floor
```
Current:       36/54 (67%)
Tier 1 only:   42/54 (78%)  — the engineering floor
+ Tier 3:      45/54 (83%)  — if optional items built
```

### What the numbers DON'T capture

Tier 2 visuals (vent parallel, anthill, HALO) don't move T/F scores.
They move something harder to measure: whether a reader stays engaged
long enough for the T/F content to land. The hydrothermal vent makes
them wonder. The anthill makes them understand emergence. The HALO
silhouette makes them want to know who this person is. These improve
the EFFECTIVE delivery rate of everything else.

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

### Gallery-first workflow

All new SVGs are built into `docs/gallery.html` FIRST so Bruce can
review them before they go into the book. The gallery is the staging
area. Book insertion (hover panels + inline) is a later phase, gated
on Bruce's approval of each visual.

### Gallery restructure: p-level sections

Restructure gallery.html into three sections with subtle background
color differences for at-a-glance orientation:

| Section | Background | Contents |
|---------|-----------|----------|
| **p1 — Hover panels** | `#f8fbfe` (faint blue) | SVGs that live in hover-definitions.yaml rich panels. Reader sees on tap/hover. |
| **p2 — Summary-adjacent** | `#f8fef8` (faint green) | Visuals that appear in or support the summary. Currently empty — new plan visuals may land here. |
| **p3 — Chapter inline** | `#fef8f8` (faint rose) | SVGs injected into chapter text by preprocess.py. Filmstrip, domain buttons, flat diagram. |
| **Standalone** | `#fafafa` (neutral) | Files not in the book: cover triskellion, test SVGs, landing page image. |

Each section gets a colored left-border bar + section header with
count. Existing SVGs are reclassified into the appropriate section.
New SVGs from this plan go into the section matching their Display
tag. SVGs tagged BOTH appear in p1 section with a badge noting
"also inline (p3)."

### Build notes

**Style:** #1a5276 primary, #2471a3 secondary, Georgia serif,
#888 captions. Max 380px for hover-panel versions. Full content width
for inline. Alt text / `<title>` on every SVG.

**Gallery numbers:** New SVGs get SVG-029+ in the gallery manifest.

**Hover panels:** When approved, SVGs go into `hover-definitions.yaml`
`html:` blocks, ADDED to existing text content (not replacing it).

**Inline injection:** Requires injection marker in .tex + preprocess.py
logic. Separate phase after gallery review.

---

## Phasing

| Phase | Deliverable | Effort | Dependencies |
|-------|-------------|--------|-------------|
| 1 | **Gallery restructure:** p1/p2/p3 sections with color coding | ~1h Generator | None |
| 2 | **Build all Tier 1 SVGs into gallery:** silos, guided deduction, decision tree, knot, ladder | ~3h Generator | Phase 1 |
| 3 | **Build Tier 2 SVGs into gallery:** vent parallel, anthill, HALO | ~2h Generator | Phase 1 (parallel w/ Phase 2) |
| 4 | **Bruce reviews gallery** | — | Phases 2–3 |
| 5 | **Hover panel insertion:** approved SVGs into hover-definitions.yaml | ~1.5h Generator | Phase 4 approval |
| 6 | **Inline chapter injection:** approved SVGs into chapter HTML | ~2h Generator | Phase 4 approval |
| 7 | **Landing page title image** | ~1h Generator | Bruce chooses option |
| 8 | **Tier 3 optional:** ChatGPT table, backchannel | ~1h Generator | If Bruce wants |
| 9 | **Build 4 planned SVGs** (SVG-025–028) per manifest | ~2h Generator | Existing specs |
| 10 | **Tooltip viewer rebuild + regression test** | ~30min Generator | All prior |

Phases 2 and 3 can run in parallel. Phase 4 is Bruce's review gate —
nothing enters the book until Bruce has seen it in the gallery.
Phases 5 and 6 only process SVGs Bruce approves.

---

## Acceptance Criteria

### Per-SVG (in gallery)
- [ ] Renders correctly in Chrome, Firefox, Safari (desktop + mobile)
- [ ] Alt text / `<title>` describes the visual
- [ ] Palette matches (#1a5276, #2471a3, Georgia, #888)
- [ ] Readable at 320px viewport width
- [ ] Placed in correct p-level section of gallery

### Gallery restructure
- [ ] Three p-level sections with distinct background colors
- [ ] All existing SVGs reclassified correctly
- [ ] Left-border color bars + section headers with counts
- [ ] Mobile-friendly layout preserved

### Book insertion (after approval)
- [ ] Existing rich-panel text preserved (SVG added, not substituted)
- [ ] `make all` builds clean after each insertion
- [ ] Tooltip viewer rebuilt
- [ ] No existing SVGs broken or displaced

### Plan-Level
- [ ] p1 takeaways ≥ 18/24 (75%) — up from 15/24
- [ ] p1 failure modes ≥ 24/30 (80%) — up from 21/30
- [ ] At least 2 visuals serve understanding/delight (not T/F-driven)
- [ ] Landing page has title image
- [ ] All 4 planned SVGs built
- [ ] p2 scores unchanged (≥ 23/24 takeaways, 30/30 failure modes)

---

## Annealing Log

### Passes 1–6 (HIGH HIGH MED MED LOW LOW)

1. **HIGH — Display strategy.** Added dual-display (hover + inline)
   with explicit labels per visual. Existing text preserved in panels.
2. **HIGH — Visual design.** Five-field: circles→silos. ChatGPT:
   SVG→HTML table. Concept ladder: 5 solid + 1 dashed. Decision tree:
   trimmed caption.
3. **MED — Score honesty.** Added Tier 1 vs. +Tier 3 projections.
4. **MED — Pilot phase.** Phase 0 builds one SVG first to validate.
5. **LOW — Gallery numbering.** New items get SVG-029+ in manifest.
6. **LOW — Planned SVGs.** Referenced, not re-specified.

### Pass 7 (MED — Joy audit)

Original plan was pure engineering — every visual justified by T/F
score. Bruce: "maybe we need some images just for fun or for better
understanding."

**Added Tier 2** (understanding/delight): hydrothermal vent parallel
(wonder), anthill emergence (understanding), HALO silhouette (narrative
fun). **Demoted** Custodian's daily work — "Boring!" is funnier
without a diagram. **Restructured tiers** from engineering labels to
purpose labels (build first / understand & delight / optional).

### Pass 8 (MED — Gallery-first workflow)

Bruce: "I want to SEE these images BEFORE we add them to the book."

**Key change:** Gallery is now the staging area. All new SVGs are
built into gallery.html first. Bruce reviews. Only approved SVGs
proceed to hover panels and inline injection. This separates "does the
SVG look right?" from "does it work in the book?" — cheaper to iterate
in the gallery than in hover-definitions.yaml.

**Gallery restructure:** Added p1/p2/p3 sections with subtle background
colors (#f8fbfe / #f8fef8 / #fef8f8) so Bruce can tell at a glance
where each SVG will live. Left-border color bars for quick scanning.

**Phasing revised:** Old Phase 0 (pilot) absorbed into Phase 2 (build
all Tier 1 into gallery). The gallery IS the pilot — Bruce sees every
SVG before anything enters the book. Added explicit Phase 4 review
gate.

**Rating: 8.5/10.** Gallery-first workflow is cleaner and reduces risk.
The review gate means no SVG enters the book unreviewed. The p-level
sections make gallery.html a useful diagnostic tool beyond this plan.
Remaining gap: inline injection (Phase 6) still needs per-chapter
markers, which will be specified when we get there.

---

*Plan written by Argus (Auditor), S63. Annealed 8 passes
(HIGH/HIGH/MED/MED/LOW/LOW/MED/MED).*
