# Plan 0253 — Preface Swap: Gen's Replacement + Remove Bruce's Preface

**Auditor:** Argus (S63)
**Date:** 2026-04-25
**Status:** READY FOR GENERATOR
**Source:** Gen's issue #2 on has-anyone-looked repo + Bruce's approval

---

## Problem

The manuscript has two prefaces:
1. `manuscript/00-front/genevieve-preface.tex` — Gen's February 2026 preface
2. `manuscript/00-front/preface.tex` — Bruce's preface (Plan 0094)

Gen submitted a new standalone preface on has-anyone-looked issue #2.
Bruce approved replacing both prefaces: Gen's new text replaces both.
Bruce's preface content is 100% covered by other front matter
(legal-note.tex, not-claimed.tex, introduction.tex, etc.).

## Changes

### Step 1: Replace genevieve-preface.tex content

Replace the full content of `manuscript/00-front/genevieve-preface.tex`
with Gen's new preface text. Use chapter title `Preface` (not
"Preface by Genevieve Prentice" — Gen's new text is not a personal
statement, it's the book's preface). Keep the label
`\label{front:genevieve-preface}` — no files reference this label
(verified), but keeping it costs nothing and prevents future breakage
if a ref is added.

New content:

```latex
\chapter*{Preface}
\addcontentsline{toc}{chapter}{Preface}
\label{front:genevieve-preface}

This book brings together a set of events that are described as clearly
as possible, but not fully resolved.

They involve real people, real institutions, and technical material that
can be followed in detail. At the same time, the interpretation of what
occurred remains open.

Different readers will find different ways to approach it. Some will read
it as memoir. Some as investigation. Some as a speculative reconstruction
built from incomplete evidence. The book allows for those readings without
requiring a choice between them at the outset.

At the center is a single question that emerges from the material itself:
what would justify giving something up under conditions of uncertainty?

The possibility that something meaningful was not pursued---or not
retained---because its consequences could not be cleanly contained is the
organizing thread.

The account moves across several kinds of material: personal experience,
technical discussion, institutional context, and interpretation. It does
not resolve neatly into a single explanation, and it is not intended to.

The request to the reader is straightforward: to follow the material
closely enough to distinguish what is grounded, what is interpretive, and
what remains unresolved.

If the book succeeds, it will be because it makes the central decision
visible, and allows the reader to encounter it before deciding what to
believe.

\vspace{0.5cm}
\hfill\textit{--- Genevieve Prentice, April 2026}
```

### Step 2: Delete Bruce's preface

1. Remove the `\include{manuscript/00-front/preface}` line from
   `main.tex` (line 47). Delete the line entirely — no commented code.
2. Delete `manuscript/00-front/preface.tex`. Content is in git history
   and fully redundant with legal-note.tex, not-claimed.tex, and
   introduction.tex.
3. Delete `manuscript/00-front/preface.aux` if it exists.

### Step 3: Verify build

Run `make dev` and confirm:
- [ ] Build exits 0
- [ ] No undefined references
- [ ] TOC shows single "Preface" (not two prefaces)
- [ ] Gen's preface text renders correctly
- [ ] Bruce's preface no longer appears

## What NOT to change

- Do not touch legal-note.tex, not-claimed.tex, introduction.tex, or
  any other front matter
- Do not modify Gen's text (use verbatim from issue #2)
- Do not touch copyright.tex or the-stack.tex
- No labels reference `front:preface` — deletion is safe (verified)

## Acceptance Criteria

- [ ] Single preface in output, authored by Genevieve Prentice
- [ ] Bruce's preface removed from reading flow
- [ ] `make dev` clean build
- [ ] No broken \ref or \label
- [ ] TOC correct

---

## Annealing Log (LOW)

### LOW — Deletion safety check

Verified: `front:preface` label is not referenced by any other .tex
file. `front:genevieve-preface` label is not referenced by any other
.tex file. Neither deletion nor replacement creates broken refs.
Bruce's preface content (guided deduction, real names, dialogue
disclaimer, AI disclosure, anti-C-collapse, predictions-as-test) is
covered by legal-note.tex, not-claimed.tex, introduction.tex,
hook.tex, summary.tex, afterword.tex, and evidence-interlude.tex.
Redundancy confirmed across all six points. Gen's text is placeholder
(she plans a further revision) — acceptable per Bruce. The dagger
convention referenced in Bruce's preface is also in legal-note.tex
and copyright.tex, so that disclosure survives deletion.

**Rating: 8/10.** Simple, clean, fully reversible via git. The 2-point
gap: Gen's text is a placeholder she plans to revise again, so this
plan may run twice. Acceptable cost — the mechanical work is trivial
each time.

---

*Plan 0253 written by Argus (Auditor), S63. Annealed 1 pass (LOW).*
