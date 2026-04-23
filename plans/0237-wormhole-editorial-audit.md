# Plan 0237 — Track B: Wormhole Editorial Audit

**Status:** COMPLETE (verified S63 audit)
**Author:** Auditor (Argus)
**Date:** 2026-04-22
**Depends on:** Plan 0236 Phase 1 — singular `wormhole:` YAML entry must exist
**Related:** Plan 0236 (Track A infrastructure), Plan 0235 (superseded)

---

## Problem

Even with tooltips on every first-occurrence wormhole (Plan 0236), a few high-exposure instances need editorial strengthening. A deep-link reader sees the word "wormhole" and their sci-fi mental model activates BEFORE they hover. For most instances the tooltip corrects on hover. But for instances in highly shared/linked passages, the bare word carries too much wrong-model weight.

This plan makes 3 surgical edits across 3 files. Total diff: 3-4 words changed.

---

## Fix 1 — three-possibilities.tex:35 AND pos01-three-possibilities.tex:24

These are identical text (spine + bridge mirror). Option A — Confabulation. High deep-link exposure.

**Current (both files):**
```
The wormhole-prone substrate described in it, called the Flat, is real.
```

**Change to (both files):**
```
The \hovertip{wormhole}-prone substrate described in it, called the Flat, is real.
```

**Why `\hovertip{}` instead of adding "topological":** "topological-wormhole-prone" is a triple-hyphenated monstrosity that breaks the rhythm of Bruce's short declarative sentences. The `\hovertip{wormhole}` preserves the prose exactly — reader sees "wormhole-prone" with "wormhole" carrying the hover indicator. Hover fires the rich panel with comparison table + mechanism + SVG. The explicit `\hovertip{}` also prevents auto-detect from wrapping "wormhole" less cleanly in this chapter (it registers in hover_seen).

**Files:**
- `manuscript/spine/three-possibilities.tex` line 35
- `manuscript/bridge/pos01-three-possibilities.tex` line 24

---

## Fix 2 — pos11-the-demo.tex:23

Bridge popup for The Demo chapter. Deep-link target. Context is DARPA moonshot narrative.

**Current:**
```
This ``moonshot project'' would use wormhole technology to implement practical quantum teleportation
```

**Change to:**
```
This ``moonshot project'' would use topological wormhole technology to implement practical quantum teleportation
```

One word added. "Wormhole technology" sounds like Star Trek; "topological wormhole technology" anchors it in real physics. Auto-detect also wraps "wormhole" here (belt and suspenders).

**File:** `manuscript/bridge/pos11-the-demo.tex` line 23

---

## Fix 3 (OPTIONAL — Bruce's call)

`manuscript/record/the-surrender.tex` line 51:
```
the maturity to handle wormhole technology directly
```
Could become "topological wormhole technology." But this is deep in the Record, in a Possibility C discussion. Auto-detect tooltip is probably sufficient. Skip unless Bruce says otherwise.

---

## Verification

Build HTML after edits. Check:
- Three-possibilities chapter: "wormhole" in "wormhole-prone" has hover indicator
- The Demo bridge popup: "topological wormhole technology" renders correctly
- No broken LaTeX (the `\hovertip{wormhole}-prone` pattern compiles cleanly — macro closes before the hyphen)

---

## Commit

Stage only the 3 .tex files (or 2 if Fix 3 is skipped).
Message: `Plan 0237: editorial wormhole disambiguation — 3 high-exposure instances`

Do NOT open a browser. Build and report. Bruce verifies visually.
