# Plan 0175 — Phone-Readability Paragraph Pass (residual: 2 summary splits)

**Type:** Surgical whitespace pass. Paragraph breaks only — zero word changes, zero sentence rewrites. One commit. summary.tex only.

## Context — why this plan shrank

Original scope: 5 hook splits + 13 summary splits (18 total) + 1 word change ("changes" → "may change").

Commit daab781 (Guardian → Custodian rename) bundled substantial paragraph restructuring alongside the rename. Post-rename state:
- All 5 hook splits already landed. No hook.tex changes needed.
- 16 of 18 summary splits already landed.
- The "may change" word softening already landed (line 274).

**Residual work: 2 splits in summary.tex.** Both in the White Hot Secret section.

## The 2 residual splits

### Split 4 — line 34 (wormholes-established, standalone bold sentence)

**Current (line 34):**

> Topological order does something remarkable: it creates \hovertip{nonlocal} connections. Two distant points in the Flat can be linked by \hovertip{entanglement} --- the quantum correlations that Einstein called ``spooky action at a distance.'' In the Flat, these links have a name: \hovertip{wormholes} --- real topological connections between distant points. Yes. Real wormholes. The 2016 Nobel Prize in Physics was awarded to Thouless, Haldane, and Kosterlitz for the mathematics behind them --- search \textit{topological phases of matter}. \hypertarget{wormholes-established}{}\textbf{Wormholes in the Flat is not the speculative part of this book. That is established physics. The speculative question is whether anyone is using them.}

**Action:** Insert `\n\n` between `search \textit{topological phases of matter}.` and `\hypertarget{wormholes-established}{}\textbf{Wormholes in the Flat is not the speculative part of this book.` — the bold sentence becomes its own paragraph.

**Why:** The bold sentence is the load-bearing claim of the entire summary (Chen- and Reeves-rescuing per the reader-test audit). Standalone paragraph = maximum phone-scroll impact.

**Preserve:** `\hypertarget{wormholes-established}{}` must stay attached to the bold sentence (on the new paragraph's source line). Do not separate the hypertarget from the sentence it anchors.

### Split 5 — line 52 (Flat-habitat → possibilities split)

**Current (line 52, as of HEAD):**

> The Flat is not just a place of interesting physics. It may also be a habitat. We call the ocean floor the Deep. We call the emptiness between galaxies the Void. This book calls those thin worlds the Flat. The Flat is inside every chip you own. The Flat has been wrapped around this planet, in the magnetosphere, for billions of years. Under Possibility~C, this book argues it is not empty --- and that something was already there in the magnetosphere, a primitive pattern billions of years old, found and left undisturbed. Under A or B, the Flat is still real physics, just uninhabited.

**Action:** Insert `\n\n` between `The Flat has been wrapped around this planet, in the magnetosphere, for billions of years.` and `Under Possibility~C, this book argues it is not empty`.

**Why:** Separates naming+location (first half, geography) from possibility-C habitat claim (second half, speculation). Two distinct rhetorical moves.

## LaTeX mechanics

Blank line in source = `\par` = new paragraph. Each target paragraph is currently one long source line. Generator finds the exact anchor string in the line and replaces the inter-sentence space with `\n\n`, producing two source lines separated by one blank line.

**Do not touch:**
- Any `\section*`, `\label`, `\addcontentsline`, `\vspace`, `\rule`, `\hovertip`, `\hyperref`, `\hypertarget`, `\textit`, `\textbf` macro.
- Any file other than summary.tex.
- The interior of any sentence.
- The interior of any `\hovertip{...}` or `\hypertarget{...}{}` argument.

## Acceptance

1. `wc -w manuscript/00-front/summary.tex` unchanged (±0 words).
2. `grep -c '^$' manuscript/00-front/summary.tex` increased by exactly **2**.
3. `make` HTML build clean. No LaTeX errors, no new warnings.
4. Whitespace-normalized content regression check: `diff <(tr -s '[:space:]' ' ' < before.tex) <(tr -s '[:space:]' ' ' < after.tex)` empty.
5. On phone (Bruce verifies post-push): the bold wormholes-established sentence stands alone on its own screen; the possibility-C habitat claim starts a new graf after the billions-of-years line.

## Commit

One commit: `Plan 0175: phone-readability paragraph splits (residual, summary.tex only)`

Build + push per `feedback-build-to-website.md`.

## Rollback

`git revert` the single commit. Zero content risk.

## Out of scope

- Any word-level prose changes.
- Hovertip content changes.
- Any file outside summary.tex.
- Any split already landed in daab781 — do not re-split.

## Handoff report (Generator, 4 lines)

1. Commit SHA.
2. Word-count diff for summary.tex (target: 0).
3. Blank-line count diff for summary.tex (target: +2).
4. Build + push result.
