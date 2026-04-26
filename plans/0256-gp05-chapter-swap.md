# Plan 0256 — GP05: Exfiltration Before Consequences (Record Chapter Swap)

**Auditor:** Argus (S63)
**Date:** 2026-04-25
**Status:** DRAFT — awaiting Bruce approval
**Source:** Gen's GP05 (has-anyone-looked issue #8)
**Annealing:** MED (2 passes)

---

## Problem

The Record currently places interdiction (exposure, legal strategy, DARPA
forgiveness, confession logic) BEFORE the exfiltration chapters (first-light,
the-walk-out). The reader is asked to process consequences before the
mechanism of exfiltration is clear.

**Current main.tex order (lines 95-97):**
```
\include{manuscript/record/interdiction}       % line 95
\include{manuscript/record/first-light}        % line 96
\include{manuscript/record/the-walk-out}       % line 97
```

**Proposed order:**
```
\include{manuscript/record/first-light}
\include{manuscript/record/the-walk-out}
\include{manuscript/record/interdiction}
```

Gen's reasoning: the reader needs (1) how the thing escaped containment,
then (2) what that escape meant. Causal order, not current order.

---

## Changes

### Step 1: Swap lines in main.tex

Reorder lines 95-97 so first-light and the-walk-out precede interdiction.
Keep adjacent comments. Keep the commented-out `the-demonstration` line
(line 94) in place — it's above the block and stays as-is.

### Step 2: Verify cross-references

**One known cross-reference:** `manuscript/spine/the-flat.tex` line 41
references `Chapter~\ref{record:interdiction}`. This is a `\ref` — LaTeX
resolves it to the correct chapter number regardless of position. The ref
will still work; only the number changes. No text edit needed.

**No narrative cross-references** between interdiction, first-light, and
the-walk-out that assume a specific order (verified by grep for
`record:int-`, `record:fl-`, `record:wo-` across all .tex files).

### Step 3: Build and verify

- `make dev` clean
- Check TOC order in PDF
- Verify `\ref{record:interdiction}` in the-flat.tex resolves

---

## What NOT to Change

- No content edits to any chapter
- Do not touch the-handler (line 98) or the-target (line 99) — they
  stay in current position after the swapped block
- Do not touch the commented-out `the-demonstration` line (94)
- Do not renumber any labels

---

## Annealing Log (MED — 2 passes)

### Pass 1 — Structural safety

**Cross-references:** Only one: `the-flat.tex:41 → record:interdiction`.
Uses `\ref{}` which resolves by label, not position. Safe.

**Deep links in affected chapters:**
- first-light: `grown-not-built` (line 101) — position-independent. Safe.
- the-walk-out: none found
- interdiction: none found

**Narrative flow:** first-light introduces the TQNN growing paradigm and
ULTRA II's operational context. the-walk-out describes the COWS faction,
bifurcation, MOSFET exfiltration, and the relinquishment plan. interdiction
covers exposure, legal strategy, DARPA forgiveness. The proposed order is
strictly causal: mechanism → exfiltration → consequences. No forward
references from first-light/walk-out to interdiction content. Interdiction
references "what the COWS did" which is in walk-out — so it MUST come after.
Current order has this backwards.

**Chapter numbering:** Record chapters are numbered sequentially by LaTeX.
Swapping changes the chapter numbers for all three chapters. No hardcoded
chapter numbers found in the text (all use `\ref{}`).

### Pass 2 — Edge cases

**the-flat.tex reference wording:** "Chapter~\ref{record:interdiction}
(\S``The Classical Backchannels'')" — the section name stays correct
regardless of chapter position. The reader who follows this reference will
land on the right chapter. Clean.

**Duplicate track files:** pos26-interdiction exists only as staging
material (not in build). first-light and the-walk-out have no pos*
duplicates in the active build. No parallel edits needed.

**Rating: 9/10.** One-file, three-line swap. One cross-reference verified
safe. No content changes. Trivially reversible. The 1-point gap: chapter
renumbering means readers with cached PDFs see different chapter numbers,
but this is routine for any reorder.

---

## Acceptance Criteria

- [ ] main.tex: first-light before the-walk-out before interdiction
- [ ] `make dev` clean build
- [ ] TOC shows correct order
- [ ] `\ref{record:interdiction}` in the-flat.tex resolves
- [ ] No other files modified

---

## Generator Handoff

```
You are the Generator.

Read Plan 0256 at ~/software/relinquishment/plans/0256-gp05-chapter-swap.md

Execute: Swap three \include lines in main.tex (lines 95-97) so the order
becomes first-light, the-walk-out, interdiction. Run `make dev`. Verify
TOC order and that \ref{record:interdiction} resolves in the-flat.tex.
Report completion.
```

---

*Plan 0256 written by Argus (Auditor), S63. Annealed 2 passes (MED).*
