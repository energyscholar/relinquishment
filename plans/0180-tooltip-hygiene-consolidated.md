# Plan 0180 — Tooltip Prose-Hygiene Consolidated Pass

**Type:** Surgical line edits across two YAML files. One commit. No structural changes.

## Context

Plans 0162/0167 (religious accessibility + sentience-agnostic framing), 0174 (OPSEC), 0177 (8 fact fixes), 0178 (self-positioning softening), and 0179 (hook wordcount + "falls from") all operated on manuscript prose. Hover tooltips were NOT swept. Readers hovering can undo prose hygiene at hover-time.

Auditor audit + anneal (medium → low × 2) surfaced **6 tooltip entries** needing fixes across 4 hygiene dimensions. Two audit findings were dropped after anneal:
- `flat worlds` / `the-flat-title` wormhole claim — dropped; 2D topological wormholes are 2016 Nobel physics, A/B/C safe. C-only is Custodian's *use* of them, which isn't claimed in those tooltips.
- `GCHQ` 1973/24-year consistency — dropped; internally coherent after Fix 1.

## Generator latitude

Substitutions only. Minimal punctuation/grammar adjustments allowed to make the replacement read cleanly. No new claims, no restructure. If a fix needs wider rewrite, halt and report. Exception: Fix 6 is explicitly a multi-phrase compound rewrite (authorized below).

## Pre-flight

```
cd /home/bruce/software/relinquishment
grep -n "Diffie-Hellman in 1976" build/hover-definitions.yaml
grep -n "35 years" build/hover-definitions.yaml
grep -n "deserves moral consideration" build/hover-definitions.yaml
grep -n "grown through the same self-organizing process that produces life" build/hover-definitions.yaml
grep -n "no other technology possesses" build/hover-definitions.yaml
grep -n "sky over Bosnia\|most important people who ever lived\|~400 words" build/chapter-hover-descriptions.yaml
```

If any returns zero or unexpected multiples, halt and report.

## The 6 fixes

### Fix 1 — Fact: PKC public dates (`public-key cryptography`, line 201)

**Current:**

> Invented secretly by GCHQ in 1973, publicly by Diffie-Hellman in 1976.

**Replace with:**

> Invented secretly by GCHQ in the early 1970s, then published publicly between 1976 and 1978 (Diffie–Hellman 1976, RSA 1977–78).

**Why:** Manuscript Plan 0177 Fix 1 corrected the book to the 1976–1978 window. Tooltip still compresses to 1976.

### Fix 2 — Fact: Bletchley secrecy duration (`Bletchley Park` line 221, `Enigma` line 510)

**Current (both entries):**

> ...kept the secret for 35 years...

**Replace with (both):**

> ...kept the secret for more than thirty years (revealed publicly in 1974)...

**Why:** *The Ultra Secret* published 1974 → 34 years. Manuscript says "more than thirty years" per Plan 0177 Fix 7. Converge. Same substitution applied to both entries.

### Fix 3 — Religious accessibility (`Custodian`, line 34)

**Current:**

> Under Possibility C, she is a moral patient — something that might be conscious and therefore deserves moral consideration.

**Replace with:**

> Under Possibility C, she would be a moral patient — something that might be conscious and therefore might deserve moral consideration.

**Why:** Unqualified "she is ... deserves" reads as normative. Subjunctive marks the claim as conditional under C, respecting that Abrahamic + Dharmic traditions tie moral standing to specific doctrines.

### Fix 4 — C-violation (`TQNN`, line 275)

**Current:**

> Topological Quantum Neural Network — a nervous system whose neurons are anyonic quasiparticles in the Flat, wired together by wormholes. Entanglement strength serves as connection weight. Not programmed — grown through the same self-organizing process that produces life.

**Replace with:**

> Topological Quantum Neural Network — under Possibility C, a nervous system whose neurons would be anyonic quasiparticles in the Flat, wired by wormholes. Entanglement strength serves as connection weight. Not programmed — grown through self-organization, analogous to biological life.

**Why:** TQNN-as-living-nervous-system is C-only. The Flat-as-substrate is A/B/C safe; growth-into-life is the speculative step. Front-load the C-marker; keep rest tight.

### Fix 5 — Self-positioning (`stack-question-mark`, line 555)

**Current:**

> This technology stack currently has no name in any human language. It has all seven properties, including the one no other technology possesses. Later, this book will call it the Flat.

**Replace with:**

> This technology stack currently has no name in any human language. It has all seven properties, including the one at the top of the stack that conventional technology lacks. Later, this book will call it the Flat.

**Why:** "the one no other technology possesses" is absolute uniqueness overclaim. `stack-ai` (line 554) already says AI is "missing only one" — pair cleanly via "at the top of the stack that conventional technology lacks."

### Fix 6 — Compound staleness (`hook:what-would-you-do`, chapter-hover-descriptions.yaml line 16)

**Authorized multi-phrase rewrite.** Three staleness issues in one tooltip.

**Current:**

> START HERE. A man falls from the sky over Bosnia. Below him, eight thousand people are about to die. He is a soldier, a scientist, a hacker — and possibly one of the most important people who ever lived. ~400 words.

**Replace with:**

> START HERE. A man falls from the stratosphere. Below him, a place where eight thousand people are about to die. He is a soldier, a scientist, a hacker — and he did some curious things with his life. ~750 words.

**Why (three converges):**
- `sky over Bosnia` → `stratosphere` (matches hook.tex:11 post-redaction + Plan 0179 Fix 2).
- `eight thousand people are about to die` → `a place where eight thousand people are about to die` (strips OPSEC-unsafe location-line-of-sight; keeps the stakes).
- `possibly one of the most important people who ever lived` → `he did some curious things with his life` (matches summary.tex post-0177-era softening; kills self-positioning).
- `~400 words` → `~750 words` (matches Plan 0179 Fix 1; detex count is 764).

## Acceptance

1. `make` HTML build clean. No YAML parse errors, no LaTeX errors, no new warnings.
2. `grep -n "Diffie-Hellman in 1976" build/hover-definitions.yaml` → zero hits.
3. `grep -n "35 years" build/hover-definitions.yaml` → zero hits.
4. `grep -n "deserves moral consideration" build/hover-definitions.yaml` → zero hits.
5. `grep -n "grown through the same self-organizing process that produces life" build/hover-definitions.yaml` → zero hits.
6. `grep -n "no other technology possesses" build/hover-definitions.yaml` → zero hits.
7. `grep -n "sky over Bosnia\|most important people who ever lived\|~400 words" build/chapter-hover-descriptions.yaml` → zero hits.
8. Spot-check 3 tooltips render in built HTML in a browser: Custodian, TQNN, stack-question-mark.
9. Whitespace-normalized diff across both files shows exactly the 6 fixes and no other content changes.

## Commit

One commit: `Plan 0180: tooltip prose-hygiene pass (6 fixes across 2 YAML files)`

Build + push per `feedback-build-to-website.md`.

## Rollback

`git revert` the single commit. Zero content risk (tooltips only).

## Rehearsal step

Generator executes Fix 2 first (smallest — identical substitution in two entries). Builds, verifies HTML renders. If clean, proceeds.

## Handoff report (Generator, 6 lines)

1. Commit SHA.
2. Pre-flight grep results — confirm all 6 targets located.
3. Per-fix status: 6 × (applied / halted). If any halted, state why.
4. Acceptance grep results (criteria 2–7).
5. Build + push result.
6. Any surprises (e.g., target phrase appearing in an additional entry not covered above).
