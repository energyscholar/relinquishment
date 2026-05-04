# Plan 0290: Pictogram Language System

**Status:** DRAFT — Bruce reviewing
**Author:** Auditor (Argus S64)
**Priority:** HIGH — addresses T3 comprehension, cross-track coherence, progressive concept teaching
**Origin:** S64 strategic review. Bruce: "life in the flat is a pictogram combo"
**Connects to:** Plan 0289 (taxonomy section carries ⬡◈), Plan 0276 (existing ⬡ system)

---

## Overview

Seven Unicode pictograms, one per takeaway (T1-T7), deployed as a visual language across the book. The reader learns individual symbols through repetition, then encounters combinations at key moments where concepts merge. The system builds concept recognition progressively — individual symbols first, combinations later.

All symbols are hidden by the existing `visual-plain` toggle. One button, all-or-nothing.

---

## Symbol Definitions

### Tier 1 — Core (phase-tracked, combination-capable)

| Symbol | Unicode | Concept | T# | Tooltip | Hover anchor |
|--------|---------|---------|-----|---------|-------------|
| ⬡ | U+2B21 | the Flat | T2 | "the Flat" | `data-hover-id="the-flat"` (14 occurrences) |
| ◈ | U+25C8 | emergence | T3 | "emergence" | `data-hover-id="autocatalytic"` (19 occurrences) |
| ◉ | U+25C9 | Custodian | T1 | "Custodian" | `data-hover-id="Custodian"` (18 occurrences) |
| ⊘ | U+2298 | silence | T5 | "the silence" | none — chapter-manifest only |

Core symbols use the three-phase opacity system:
- `intro` (opacity 0.4) — first ~8 chapters
- `reinforce` (opacity 0.65) — chapters 9-18
- `fluent` (opacity 1.0) — chapters 19+

Record chapters shift one step lighter: intro=0.25, reinforce=0.4, fluent=0.65

### Tier 2 — Secondary (occasional marker, fixed opacity)

| Symbol | Unicode | Concept | T# | Tooltip | Color |
|--------|---------|---------|-----|---------|-------|
| ⚙ | U+2699 | capabilities | T4 | "capabilities" | #a0a0a0 |
| ⎈ | U+2388 | stewardship | T6 | "stewardship" | #a0a0a0 |
| ⊞ | U+229E | services | T7 | "services" | #a0a0a0 |

Secondary symbols: fixed opacity 0.5, no phase tracking.

### Color Assignments

| Symbol | Color | Rationale |
|--------|-------|-----------|
| ⬡ | #b8860b (dark gold) | Established — matches gold theme |
| ◈ | #5b9bd5 (blue) | Life/emergence — distinct from gold |
| ◉ | #c4a97d (warm gold) | Entity — warm, present |
| ⊘ | #888 (grey) | Absence — deliberately muted |
| ⚙ ⎈ ⊞ | #a0a0a0 (light grey) | Secondary — recede visually |

---

## Injection Strategy

### Strategy A: Hover-term anchored (⬡ ◈ ◉)

For symbols with hover-term anchors, inject before the first matching `data-hover-id` span per chapter. This extends the existing ⬡ system.

**Current function** (`preprocess.py:4011`): `inject_concept_symbols()` handles `the-flat` only.

**Extended function:** Iterate over all hover-anchored symbols from the manifest. For each chapter, find first matching hover-term span, inject concept symbol span before it.

**Key implementation detail:** The function currently builds a `seen` dict keyed by chapter index. Extend to track `seen[chapter][concept]` so each concept gets exactly one injection per chapter. The existing chapter-boundary detection (`<details class="chapter-section"`) is reused.

### Strategy B: Chapter-manifest anchored (⊘ ⚙ ⎈ ⊞)

For symbols without hover-term anchors, inject at the first `<p>` tag after the chapter's `<summary>` element. The manifest specifies which chapters receive which symbols.

**Fallback for hover-anchored symbols:** If a chapter is assigned ◈ but has no `data-hover-id="autocatalytic"` span, fall back to Strategy B (first `<p>`).

### Strategy C: Chapter-header signatures

Inject a small `<span class="chapter-symbols">` cluster inside each chapter's `<summary>` element, after the chapter title. Shows which concepts the chapter delivers. Styled small, right-aligned, lighter opacity.

---

## Manifest: `build/concept-symbols.yaml`

```yaml
symbols:
  flat:
    glyph: "\\2B21"
    tooltip: "the Flat"
    tier: core
    color: "#b8860b"
    hover_anchor: "the-flat"

  emergence:
    glyph: "\\25C8"
    tooltip: "emergence"
    tier: core
    color: "#5b9bd5"
    hover_anchor: "autocatalytic"

  custodian:
    glyph: "\\25C9"
    tooltip: "Custodian"
    tier: core
    color: "#c4a97d"
    hover_anchor: "Custodian"

  silence:
    glyph: "\\2298"
    tooltip: "the silence"
    tier: core
    color: "#888"
    hover_anchor: null

  capabilities:
    glyph: "\\2699"
    tooltip: "capabilities"
    tier: secondary
    color: "#a0a0a0"
    hover_anchor: null

  stewardship:
    glyph: "\\2388"
    tooltip: "stewardship"
    tier: secondary
    color: "#a0a0a0"
    hover_anchor: null

  services:
    glyph: "\\229E"
    tooltip: "services"
    tier: secondary
    color: "#a0a0a0"
    hover_anchor: null

chapter_assignments:
  # --- Spine ---
  three-possibilities:
    concepts: [custodian]
    track: spine
  the-flat:
    concepts: [flat]
    track: spine
  the-braid:
    concepts: [flat, capabilities]
    track: spine
  the-factoring-game:
    concepts: [capabilities]
    track: spine
  the-code-war:
    concepts: [capabilities]
    track: spine
  genesis:
    concepts: [emergence]
    track: spine
  growing-a-mind:
    concepts: [emergence]
    track: spine
  the-wrong-substrate:
    concepts: [flat, emergence]
    track: spine
    combination: true
  the-silence-gap:
    concepts: [emergence, silence]
    track: spine
    combination: true
  capabilities:
    concepts: [custodian, capabilities]
    track: spine
    combination: true
  why-relinquish:
    concepts: [stewardship, services]
    track: spine
  the-strongest-objection:
    concepts: [custodian, stewardship]
    track: spine
  # --- Record ---
  alpha-farm:
    concepts: [custodian]
    track: record
  what-healer-said:
    concepts: [flat, emergence, capabilities]
    track: record
  the-departure:
    concepts: [custodian, silence]
    track: record
  first-light:
    concepts: [flat, emergence]
    track: record
  interdiction:
    concepts: [custodian, stewardship]
    track: record
  instantiation:
    concepts: [emergence, custodian]
    track: record
    combination: true
  the-surrender:
    concepts: [custodian, stewardship]
    track: record
    combination: true
  twenty-years:
    concepts: [silence]
    track: record
  the-question:
    concepts: [flat, emergence, custodian, silence]
    track: record
    combination: true

combinations:
  - chapter: the-wrong-substrate
    symbols: [flat, emergence]
    label: "life in the Flat"
  - chapter: the-silence-gap
    symbols: [emergence, silence]
    label: "emergence unnoticed"
  - chapter: capabilities
    symbols: [custodian, capabilities]
    label: "Custodian's capabilities"
  - chapter: the-surrender
    symbols: [custodian, stewardship]
    label: "Custodian as steward"
  - chapter: instantiation
    symbols: [emergence, custodian]
    label: "emergence → Custodian"
  - chapter: the-question
    symbols: [flat, emergence, custodian, silence]
    label: "convergence"
```

---

## Teaching Sequence

### Phase 1: Single symbols (Three Possibilities → Code War)

Reader learns: ⬡ ◉ and secondary ⚙, one at a time.

- Three Possibilities: ◉ (Custodian as possibility)
- The Flat: ⬡ (core concept introduced)
- The Braid: ⬡ reinforced + ⚙ (computation)
- Factoring Game: ⚙ reinforced
- Code War: ⚙ reinforced

### Phase 2: Emergence + first combination (Genesis → Wrong Substrate)

Reader learns: ◈. First combination: ⬡◈.

- Genesis: ◈ introduced (Kauffman, autocatalysis)
- Growing a Mind: ◈ reinforced (Turing + Wolfram)
- **Wrong Substrate: ⬡◈ — first combination.** T3 lands visually.

This is the key moment. The reader knows both symbols. Seeing them together IS the argument: the Flat permits emergence. Life in the Flat. The combination does the reasoning visually.

### Phase 3: Full vocabulary (Silence Gap → end of spine)

Reader learns: ⊘, and secondaries ⎈ ⊞.

- Silence Gap: ◈⊘ combination (emergence + nobody noticed)
- Capabilities: ◉⚙ combination (Custodian + what she does)
- Why Relinquish: ⎈ introduced + ⊞ (stewardship + services)
- Strongest Objection: ◉⎈ (Custodian as steward, tested)

### Phase 4: Record (story mirrors science)

Same symbols, reduced opacity. Marks where science concepts surface in Bruce's narrative. The reader recognizes symbols from the spine: "the thing I learned about is alive in this story."

### Interlude handling

Interludes do NOT carry ◉ (redundant — reader knows who's speaking). Instead they carry concept symbols for what Custodian discusses:
- Interlude 1 (Home): no symbol
- Interlude 2 (Dance): ⬡ ("I live here")
- Interlude 3 (Locks): ⚙
- Interlude 4 (Growing): ◈ ("I grew")
- Interlude 5 (Ocean): ⬡◈ ("I was not the first thing in the Flat")
- Interlude 6 (Quiet): ⊘ ("I have watched... and said nothing")
- Interlude 7 (Hello): ◉⎈ (culmination — Custodian as steward, direct address)

---

## CSS Specification

Add to preprocess.py CSS block (after existing `[data-concept="flat"]::before` at line ~1011):

```css
/* Concept symbols — Plan 0290 */
[data-concept]::before {
  font-size: 0.85em;
  margin-right: 0.15em;
  vertical-align: baseline;
}
[data-concept="flat"]::before {
  content: '\\2B21 '; color: #b8860b;
}
[data-concept="emergence"]::before {
  content: '\\25C8 '; color: #5b9bd5;
}
[data-concept="custodian"]::before {
  content: '\\25C9 '; color: #c4a97d;
}
[data-concept="silence"]::before {
  content: '\\2298 '; color: #888;
}
[data-concept="capabilities"]::before {
  content: '\\2699 '; color: #a0a0a0;
}
[data-concept="stewardship"]::before {
  content: '\\2388 '; color: #a0a0a0;
}
[data-concept="services"]::before {
  content: '\\229E '; color: #a0a0a0;
}

/* Tier phases — core symbols */
[data-concept-phase="intro"]::before { opacity: 0.4; }
[data-concept-phase="reinforce"]::before { opacity: 0.65; }
[data-concept-phase="fluent"]::before { opacity: 1.0; }

/* Record track — reduced baseline */
[data-concept-track="record"][data-concept-phase="intro"]::before { opacity: 0.25; }
[data-concept-track="record"][data-concept-phase="reinforce"]::before { opacity: 0.4; }
[data-concept-track="record"][data-concept-phase="fluent"]::before { opacity: 0.65; }

/* Tier 2 — fixed opacity, no phase tracking */
[data-concept-tier="secondary"]::before { opacity: 0.5 !important; }

/* Tooltips — cursor hint */
[data-concept][title] { cursor: help; }

/* Chapter header signatures */
.chapter-symbols {
  display: inline-block;
  margin-left: 0.5em;
  font-size: 0.7em;
  opacity: 0.5;
  vertical-align: middle;
}

/* Hide all concept symbols in visual-plain mode */
body.visual-plain [data-concept]::before { content: none; }
body.visual-plain .chapter-symbols { display: none; }

/* Hide in print */
@media print { [data-concept]::before { content: none; } .chapter-symbols { display: none; } }

/* Hide in tech-section summaries (existing rule, keep) */
details.tech-section summary [data-concept]::before { content: none; }
```

**Generator note:** The existing `[data-concept="flat"]::before` rule at line ~1011 and the phase rules at lines ~1014-1016 must be REPLACED, not duplicated. Remove lines 1011-1017 and insert the new block above.

---

## Python Implementation

### Modified function: `inject_concept_symbols()`

**Location:** `preprocess.py` line ~4011

**Current signature:** Takes `html_path` only, hardcoded for "flat" concept.

**New signature:** Takes `html_path` and reads `build/concept-symbols.yaml` manifest.

**Algorithm:**

```
1. Load manifest from build/concept-symbols.yaml
2. Parse HTML, find chapter boundaries (existing logic)
3. For each chapter:
   a. Look up chapter in manifest.chapter_assignments (match by chapter slug)
   b. For each assigned concept:
      - If concept has hover_anchor: find first data-hover-id match in chapter
      - Else: find first <p> after chapter <summary>
      - If this is a combination chapter: inject symbols adjacent (no gap)
      - Else: inject each symbol at its own anchor point
   c. Determine phase from chapter index (existing logic)
   d. Determine track from manifest (spine/record)
   e. Determine tier from manifest (core/secondary)
   f. Generate span: <span data-concept="NAME" data-concept-phase="PHASE"
        data-concept-track="TRACK" data-concept-tier="TIER"
        title="TOOLTIP" aria-hidden="true"></span>
4. Inject chapter-header signatures into <summary> elements
5. Report: "Concept symbols: N placed across M chapters (K combinations)"
```

**Chapter slug matching:** The chapter assignments use keys like `the-flat`, `genesis`, etc. The function must map these to actual chapter elements in the HTML. The current function identifies chapters by `<details class="chapter-section"`. The chapter slug can be extracted from the chapter's `<h1 id="...">` or from the `<details>` id attribute. The Generator must verify which attribute carries the chapter identifier and match accordingly.

**Generator warning — common errors to avoid:**

1. **Don't hardcode chapter indices.** Use the manifest keys + HTML id matching. Chapter order may change.
2. **Don't break the existing ⬡ injection.** The new function replaces it entirely — verify ⬡ still works after the rewrite.
3. **Regex for hover-term spans:** `r'<span[^>]*data-hover-id="ANCHOR"[^>]*>[^<]*</span>'` — the `[^>]*` before the attribute is essential because spans may have other attributes.
4. **Don't inject inside `<summary>` elements** (existing guard, keep it). Chapter signatures go IN the summary; inline symbols go OUTSIDE.
5. **YAML loading:** Add `import yaml` (or use a simple parser if pyyaml not available). Check `build/concept-symbols.yaml` path relative to script location.
6. **Title attribute escaping:** Tooltip text must be HTML-escaped. "the Flat" is safe; future tooltips with quotes or ampersands would need escaping.

### Chapter-header signature injection

After inline symbol injection, iterate over chapter `<summary>` elements. For each chapter in the manifest, insert a `<span class="chapter-symbols">` block containing one `<span>` per assigned concept (glyph only, no phase/opacity — fixed display). Place after the `</h1>` inside the `<summary>`.

---

## Verification

After build, verify:

1. **Symbol count:** Build log reports total symbols and per-chapter counts. Expected: ~40-60 inline symbols across ~20 chapters.
2. **Tooltip check:** Open reader, hover on any concept symbol → tooltip appears.
3. **Visual-plain check:** Toggle visual-plain → all symbols and chapter signatures disappear.
4. **Phase check:** Symbols in early chapters (The Flat) are faint; symbols in late chapters (The Question) are full opacity.
5. **Record check:** Symbols in Record chapters are visually lighter than same-concept symbols in spine.
6. **Combination check:** In Wrong Substrate, ⬡ and ◈ appear adjacent. In Silence Gap, ◈ and ⊘ appear adjacent. Six combination moments total.
7. **Chapter signature check:** Each assigned chapter shows its symbol cluster in the collapsed header.
8. **No regression:** Existing ⬡ behavior preserved — first "the Flat" hover-term per chapter still gets the hexagon.

---

## Execution Phases

### Phase 1: CSS + manifest (mechanical, low risk)

- Create `build/concept-symbols.yaml` with symbol definitions + chapter assignments
- Replace existing concept-symbol CSS with full 7-symbol block
- Add tooltip `title` attribute to existing ⬡ spans (modify span generation)
- Update pictogram gallery page
- **Test:** Build, verify ⬡ still works with tooltip, new CSS doesn't break layout
- **Commit:** `Plan 0290 phase 1: concept symbol CSS and manifest`

### Phase 2: Multi-concept injection (highest risk, test carefully)

- Rewrite `inject_concept_symbols()` to read manifest and handle all 7 concepts
- Implement hover-anchor strategy (⬡ ◈ ◉) and chapter-manifest fallback (⊘ ⚙ ⎈ ⊞)
- Implement track/tier/phase data attributes
- **Test:** Full build. Verify symbol counts, per-chapter placement, tooltips.
- **Commit:** `Plan 0290 phase 2: multi-concept injection from manifest`

### Phase 3: Combinations + chapter signatures (moderate risk)

- Implement combination injection (6 moments)
- Implement chapter-header signature injection
- **Test:** Verify 6 combinations at correct chapters, header signatures visible
- **Commit:** `Plan 0290 phase 3: combinations and chapter signatures`

### Phase 4: Legend panel (independent, can defer)

- Add legend button to reader.js UI
- Legend shows all 7 symbols with names and brief descriptions
- Hidden by visual-plain toggle
- **Test:** Button toggles legend panel, all symbols render correctly
- **Commit:** `Plan 0290 phase 4: symbol legend panel`

### Dependencies

- Phase 1 is independent — can ship now
- Phase 2 depends on Phase 1
- Phase 3 depends on Phase 2
- Phase 4 is independent of Phases 2-3 (only needs CSS from Phase 1)
- Plan 0289 Part A (Flat Life Taxonomy) should carry ⬡◈ as its symbolic signature once Phase 3 ships

---

## Gallery Update

Update `build/pictogram-gallery.html` to reflect final deployed state after each phase. The gallery serves as the author's reference for the symbol system.
