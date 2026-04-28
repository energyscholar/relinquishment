# Plan 0274g: Ordering Puzzle Types (ord + tower)

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** Medium
**Scope:** `build/preprocess.py` (new renderer), `build/puzzle-tracker.yaml`
**Annealing:** MED MED LOW LOW

---

## Problem Statement

Two approved puzzles use ordering mechanics: pz-ord-t1-001 ("Guided Deduction", type `ord`) and pz-ord-t4-002 ("Build the Stack", type `tower`). Both require the reader to arrange items in correct sequence. No renderer exists for either type.

---

## Changes

### 1. Implement `ord` (Ordering) Renderer

Displays a list of items in shuffled order. Reader taps items in sequence to reorder them:

```html
<div class="pz-ord-items">
  {shuffled items as tappable buttons with sequence numbers}
</div>
<button class="pz-ord-check">Check Order</button>
```

Interaction: tap items in the order you think is correct. Each tap assigns the next sequence number. Tap again to deselect. Check button validates against correct order. Wrong items flash red, correct flash green.

Data: `items` is an ordered list — correct sequence is the list order. Shuffle for display.

### 2. Implement `tower` (Stack) Renderer

Same mechanic as `ord` but with visual stacking — each correctly-placed item builds a layer:

```html
<div class="pz-tower-stack">
  {visual stack grows upward as items are placed}
</div>
<div class="pz-tower-bank">
  {available items as tappable buttons}
</div>
```

Tap an item to place it as the next layer. Wrong choice shakes. Right choice animates into position.

Data: pz-ord-t4-002 has 6 layers (The Flat → Communication).

### 3. Deploy Both Puzzles

Set installed:true for both. pz-ord-t1-001 is in the-braid, pz-ord-t4-002 is in story-never-told. Both chapters already have CHAPTER_INJECTION_TARGETS entries.

---

## Anneal: MED MED LOW LOW

**M1.** Drag-to-reorder is the expected UX for ordering, but drag is unreliable on mobile. Tap-to-sequence is safer.
**M2.** Tower visual stacking needs animation — CSS transitions sufficient, no canvas needed.
**L3.** ord and tower are mechanically identical; could share a renderer with different CSS.
**L4.** Both puzzles are in chapters that already have puzzles — no new injection targets needed.

---

## Handoff Prompt

```
You are the Generator. Read plan 0274g in ~/software/relinquishment/plans/.

Implement two ordering puzzle renderers in build/preprocess.py:

1. ord: Shuffled list, tap items in sequence, check button validates.
   Read pz-ord-t1-001 data for field structure.

2. tower: Same mechanic but visual stack builds upward. Each correct
   tap animates a layer into place. Read pz-ord-t4-002 data.

Both use tap-to-sequence (not drag). Add 'ord' and 'tower' to
supported types. Set installed:true for both. Build, VERIFY OK: 18
(or current count + 2), test on phone. Commit:
"Plan 0274g: ord + tower renderers for ordering puzzles"
Push.
```
