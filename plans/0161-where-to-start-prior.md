# Plan 0161 — "Where to Start" — Bayesian Prior Instruction

**Auditor:** Argus
**Generator:** TBD
**Date:** 2026-04-12
**Origin:** Dignity Net audit (S54 cont.) flagged Axis 2 "Leave the corners of the field" as HIGH-severity. The A/B/C framing is honest at the meta-level but structurally asymmetric in practice — narrative, pacing, and evidence sequencing funnel readers toward C. This plan inserts an explicit Bayesian prior-setting instruction at the front of `three-possibilities.tex` so readers begin at ~95% Option A and let the book earn any movement. Converts structural persuasion into reader-owned evaluation.

## Purpose

Add a short `\section*{Where to Start}` to `manuscript/spine/three-possibilities.tex`, positioned between the Feynman epigraph and the "After years of research..." intro line. The section instructs the reader to adopt a high-skeptical prior before reading the three options. This directly addresses DN Axes 2, 5, 6, 7 flagged in the audit.

## Target file

`/home/bruce/software/relinquishment/manuscript/spine/three-possibilities.tex`

## Edit specification

**Locate** (lines 15–17, verbatim):

```latex
\vspace{0.5cm}

\deeplink{three-possibilities}After years of research, pressure-testing, and reconstruction we cannot definitively distinguish between these three possibilities. Here is the evidence. You decide.
```

**Replace with:**

```latex
\vspace{0.5cm}

\section*{Where to Start}
\label{spine:where-to-start}

Extraordinary claims deserve extraordinary priors. Before reading further, set yourself near 95\% Option~A --- the story is false. That is the rational starting point for anyone meeting this book for the first time, because the base rate for claims of this magnitude being true is very low. I am not offended by it; I started there myself.

Then let the book earn every point of movement. If by the end it cannot move you, that is a result. If it can, the movement is yours --- earned against a skeptical prior, not handed to you by a narrative that assumed your goodwill.

\vspace{0.5cm}

\deeplink{three-possibilities}After years of research, pressure-testing, and reconstruction we cannot definitively distinguish between these three possibilities. Here is the evidence. You decide.
```

## Acceptance criteria

1. `\section*{Where to Start}` renders in `docs/downloads/Relinquishment.html` before Option A, after the Feynman epigraph.
2. The `\label{spine:where-to-start}` produces a deep-link anchor (`id="spine:where-to-start"` or similar; check postprocessed output).
3. `make html` completes without errors or new warnings.
4. No other text in `three-possibilities.tex` is modified.
5. Existing `\deeplink{three-possibilities}` anchor still functions.
6. Verify via grep: `grep -c "Where to Start" docs/downloads/Relinquishment.html` returns ≥1.
7. No changes to `main.tex`, hover-definitions, or any other build asset.

## Out of scope

- Rewording of the inserted prose — text is final as specified.
- Adding hovertips to the new passage (deliberately plain — the instruction must not be distracted by popups).
- Cross-references in other chapters to the new section — defer to a later plan if wanted.
- Updating `chapter-hover-descriptions.yaml` or `menu-tooltips.yaml` — not needed (this is a subsection, not a chapter).

## Build + ship

1. Apply the edit.
2. Run `make html` from repo root.
3. Verify acceptance criteria 1–7.
4. Commit with message: `Plan 0161: insert Bayesian prior instruction in Three Possibilities`
5. `git push`.

## Reporting

On completion, report:
- Commit hash
- Build status (success/warnings/errors)
- Results of `grep -c "Where to Start" docs/downloads/Relinquishment.html`
- Any unexpected behavior

## Context for audit

This is one of three DN-audit follow-ups identified in S54 cont.:
- (a) A-spine rebalancing — DEFERRED (larger scope)
- (b) Daughters' names redaction — SHIPPED (commit 2cae0fb)
- (c) Bayesian prior instruction — THIS PLAN
