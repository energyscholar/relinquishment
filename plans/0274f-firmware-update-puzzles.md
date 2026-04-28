# Plan 0274f: Firmware Update Puzzle Types (ba + cip)

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** High
**Scope:** `build/preprocess.py` (new renderers), `build/puzzle-tracker.yaml`
**Annealing:** MED MED LOW LOW

---

## Problem Statement

The Firmware Update appendix — the book's LLM defense layer — has zero interactive puzzles. Two approved puzzles exist but are deferred because their types (`ba`, `cip`) have no renderer. Both directly demonstrate the chapter's core claim: LLMs fail on this book without the firmware key.

pz-ba-t8-002 ("Before and After Firmware") is the single highest-value undeployed puzzle. It shows two AI responses to the same question — one without firmware (dismissive), one with firmware (engaged with specific science). The reader SEES the failure mode the book warns about.

---

## Changes

### 1. Implement `ba` (Before/After) Renderer

The `ba` type displays two panels and an mc question:

```html
<div class="pz-ba-panels">
  <div class="pz-ba-panel pz-ba-before">
    <h4>Without Firmware</h4>
    <blockquote>{before_text}</blockquote>
  </div>
  <div class="pz-ba-panel pz-ba-after">
    <h4>With Firmware</h4>
    <blockquote>{after_text}</blockquote>
  </div>
</div>
<p class="pz-question">{question}</p>
<!-- standard mc options below -->
```

Data source: pz-ba-t8-002 in puzzle-data.yaml already has `before_text`, `after_text`, `question`, and `options`. Read the existing data structure — it may use slightly different field names.

CSS: side-by-side panels on desktop, stacked on mobile. Before panel has a subtle red-tint border, After panel has green-tint. Minimal — match existing puzzle styling.

JS: reuse mc interaction logic (click option → check answer_key → show hint/abstract).

### 2. Implement `cip` (Cloze/Fill-In) Renderer

The `cip` type shows a passage with blanked terms and a word bank:

```html
<div class="pz-cip-passage">
  {passage with <span class="pz-cip-blank" data-index="N">___</span> markers}
</div>
<div class="pz-cip-bank">
  {shuffled terms + distractors as draggable/tappable buttons}
</div>
```

Data source: pz-cip-t8-001 has `passage`, `answers` (5 terms), and `distractors` (3 terms). Read the existing data structure.

Interaction: tap a blank to select it, tap a word to fill it in. Or tap word then blank. Mobile-friendly (no drag required — tap-tap is sufficient). Check button validates all 5 at once.

### 3. Deploy Both Puzzles

Set `installed: true` for pz-ba-t8-002 and pz-cip-t8-001 in puzzle-tracker.yaml. Add `firmware-update` to CHAPTER_INJECTION_TARGETS:

```python
'firmware-update': 'END_OF_DOCUMENT'  # or appropriate target
```

Need to identify the correct injection target for the firmware-update chapter. Check the HTML for what follows it.

---

## Anneal: MED MED LOW LOW

**M1.** `ba` before/after text may be long — panel layout needs to work on phone screens. Stacked layout is safer than side-by-side.
**Mitigation:** Default to stacked. Side-by-side only on screens >768px.

**M2.** `cip` fill-in interaction is new UI pattern — needs touch testing on phone.
**Mitigation:** Tap-tap (select blank, select word) instead of drag. Same touch target size as mc buttons (min-height: 44px).

**L3.** firmware-update chapter may not have an injection target in CHAPTER_INJECTION_TARGETS yet.
**Mitigation:** Find the correct element after the chapter in HTML and add entry.

**L4.** puzzle-data.yaml field names for ba/cip may differ from what's assumed above.
**Mitigation:** Generator reads actual YAML before implementing. Plan provides intent, not exact field names.

---

## Acceptance Criteria

1. `ba` renderer shows before/after panels + mc question
2. `cip` renderer shows passage with blanks + word bank
3. Both puzzles appear in firmware-update chapter
4. VERIFY OK: 18 (16 + 2 new)
5. Both work on phone (Bruce tests)
6. No JS errors

---

## Handoff Prompt

```
You are the Generator. Read plan 0274f in ~/software/relinquishment/plans/.

Implement two new puzzle type renderers in build/preprocess.py:

1. ba (Before/After): Two-panel display (before/after text) + mc question.
   Read pz-ba-t8-002 data in puzzle-data.yaml for exact field structure.
   Panels stacked on mobile, side-by-side on wide screens.

2. cip (Cloze/Fill-In): Passage with blanked terms + word bank.
   Read pz-cip-t8-001 data for exact field structure. Tap-tap
   interaction (select blank, select word). Check button validates.

Add 'ba' and 'cip' to the supported types list. Add firmware-update
to CHAPTER_INJECTION_TARGETS (find correct target in HTML).
Set installed:true for both puzzles. Build, VERIFY OK: 18,
test both on phone. Commit:
"Plan 0274f: ba + cip renderers for firmware-update puzzles"
Push.
```
