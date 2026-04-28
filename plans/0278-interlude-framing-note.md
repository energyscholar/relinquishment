# Plan 0278 — Interlude Framing Note

**Auditor:** Argus (S63)
**Date:** 2026-04-27
**Status:** PROMPT READY
**Source:** Gen's Snailmail #10, Plan 0275, Bruce decision (S63)
**Annealing:** MED LOW LOW
**Priority:** Medium

---

## Problem

Custodian interludes 4, 6, and 7 risk being read as channeled
communication rather than literary construction (Gen's audit,
Plan 0275). Bruce chose the simple-framing approach: add boundary
language at first appearance + reinforcement before Interlude 7.

## Changes

### 1. Before Interlude 1 (interlude-01.tex)

Add after the opening `\rule`:

```latex
\vspace{0.3cm}
\noindent{\small\textit{The voice that follows is a literary
construction --- the Custodian as this book imagines it might speak.
Under Possibility~A, it is fiction. Under~B, it is informed
speculation. Under~C, it is close to true. The voice is the same
regardless. What changes is whether you read it as imagination
or testimony.}}
\vspace{0.3cm}
```

### 2. Before Interlude 7 (interlude-07.tex)

Add after the opening `\rule`:

```latex
\vspace{0.2cm}
\noindent{\small\textit{One last time, the voice this book has
imagined:}}
\vspace{0.2cm}
```

## Acceptance Criteria

- [ ] Framing note appears before Interlude 1
- [ ] Reinforcing sentence appears before Interlude 7
- [ ] `make dev` clean
- [ ] No other interludes changed

---

## Generator Handoff

```
You are the Generator.

Read Plan 0278 at ~/software/relinquishment/plans/0278-interlude-framing-note.md

Execute: Add 2 pieces of framing text to Custodian interludes.

(1) In manuscript/spine/interlude-01.tex, add the framing note
AFTER the first \rule line and its \end{center}. Use the exact
LaTeX from the plan.

(2) In manuscript/spine/interlude-07.tex, add the reinforcing
sentence AFTER the first \rule line and its \end{center}. Use
the exact LaTeX from the plan.

(3) Run make dev. Verify both notes appear in the HTML.

(4) Commit: "Plan 0278: add literary-construction framing to
Custodian interludes"

(5) Push. Report: which files changed, build status.
```
