# Plan 0260 — GP07: Growing a Mind Placement

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** DRAFT — awaiting Bruce decision (may already be satisfied)
**Source:** Gen's GP07 (has-anyone-looked issue #10)
**Annealing:** LOW (1 pass)
**Independent:** No dependency on other GP plans.

---

## Problem

Gen wants Growing a Mind to arrive "before the later exfiltration /
consequence material" so the reader has absorbed the grown-mind concept
before processing walk-out, bifurcation, spread, consequences,
relinquishment.

## Current Structure

Growing a Mind is **spine Chapter 7** (main.tex line 70):

```
Spine reading order:
  Ch1: Three Possibilities
  Ch2: Wormholes in the Flat
  Ch3: The Braid
  Ch4: The Factoring Game    ← ULTRA II specs
  Ch5: The Code War          ← secrecy threshold
  Ch6: Genesis               ← Kauffman autocatalysis
  Ch7: Growing a Mind        ← HERE (Turing, McCulloch-Pitts, Wolfram)
  Ch8: The Wrong Substrate
  Ch9: The Silence Gap
  Ch10: Capabilities
  Ch11: Why Relinquish?
  Ch12: The Strongest Objection
  Ch13: Weigh the Evidence

ALL spine chapters precede ALL Record chapters.

Record reading order (post Plan 0256):
  The Record (intro)
  Alpha Farm
  The Hobbit in the Mirror
  What Healer Said
  The Departure
  First Light              ← first exfiltration/consequence chapter
  The Walk-Out
  Interdiction
  ...
```

## Assessment

**Gen's concern is already satisfied by the current structure.** Growing
a Mind (spine Ch7) arrives before ALL Record chapters, including First
Light, The Walk-Out, Interdiction, and every other exfiltration/consequence
chapter. The reader encounters the grown-mind concept a full 6+ chapters
before any consequence material.

Gen may not have had the spine/record split clear in her mental model. Her
issue says "please test moving Chapter 7" earlier — but within the spine,
it's already positioned after genesis (which it depends on: Kauffman's
autocatalytic emergence → Turing/Wolfram universality → "what if someone
tried?" is the intellectual sequence).

## Optional Move (Only If Bruce Wants Tighter Science Clustering)

If the goal is to tighten the science sequence within the spine, the only
viable move is to relocate the genesis + growing-a-mind PAIR as a unit:

**Current:** factoring → code-war → genesis → growing-a-mind
**Optional:** factoring → genesis → growing-a-mind → code-war

This creates a tighter science arc: crypto problem → how emergence works →
what computation means → secrecy precedent. The code-war chapter (secrecy
threshold) moves later, serving as transition to the argument/structural
chapters (wrong-substrate, silence-gap, capabilities, etc.).

**Trade-off:** Currently, code-war follows factoring-game naturally
("here's the crypto problem → here's the secrecy tradition they
inherited"). Moving it later separates that pairing. Both orderings are
defensible.

### Dependencies for optional move

- genesis → growing-a-mind order MUST be preserved (growing-a-mind
  depends on autocatalytic emergence concepts from genesis)
- Interlude-04 (between code-war and genesis) and interlude-05 (between
  growing-a-mind and wrong-substrate) would need to move with their
  adjacent chapters
- Cross-references: need to verify \ref{} targets still resolve
  (they will — LaTeX labels are position-independent)

---

## Changes

### If already satisfied (RECOMMENDED):

No changes. Respond to Gen explaining that Growing a Mind already precedes
all consequence material due to the spine/record split.

### If optional move is desired:

Reorder main.tex lines 67-71:
```
From: the-code-war → interlude-04 → genesis → growing-a-mind → interlude-05
To:   genesis → interlude-04(renumber?) → growing-a-mind → interlude-05 → the-code-war
```

Interlude content may need minor adjustment if it references the adjacent
chapter's content. Generator should verify.

---

## Annealing Log (LOW — 1 pass)

**Core finding:** Gen's concern is met by existing structure. The spine/
record split means Growing a Mind arrives ~8 chapters before the first
Record consequence chapter. No action needed unless Bruce wants tighter
spine clustering.

**Deep links in growing-a-mind.tex:** None found. Safe to move if desired.

**Deep links in genesis.tex:** 3 (`life-is-a-phase-transition`,
`buttons-and-threads`, `canopy-problem`). Position-independent — safe to
move.

**Cross-references:** No \ref{} to spine:growing-a-mind from other files
found. No \ref{} to spine:genesis from other files found. Both can move
freely.

**Rating: 9/10 (no action) / 7/10 (optional move).** No-action path is
clean. Optional move has low structural risk but changes the spine's
pedagogical arc, which needs Bruce's judgment.

---

## Acceptance Criteria

### No-action path:
- [ ] Confirm to Gen that Growing a Mind already precedes consequence
      material
- [ ] No files modified

### Optional move path:
- [ ] genesis + growing-a-mind + their interludes relocated in main.tex
- [ ] `make dev` clean build
- [ ] TOC shows new order
- [ ] No broken refs or deep links
- [ ] Interludes still reference correct adjacent chapters

---

## Generator Handoff (only if optional move approved)

```
You are the Generator.

Read Plan 0260 at ~/software/relinquishment/plans/0260-gp07-growing-a-mind-placement.md

Execute optional move: In main.tex, relocate the genesis + growing-a-mind
block (lines 69-71, including interlude-04 and interlude-05) to before
the-code-war (currently line 67). Verify interlude content still references
correct adjacent chapters. Run `make dev`. Report completion.
```

---

*Plan 0260 written by Argus (Auditor), S63. Annealed 1 pass (LOW).*
