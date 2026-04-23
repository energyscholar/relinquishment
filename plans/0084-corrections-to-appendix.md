# Plan 0084: Move Corrections to Appendix

**Status:** APPROVED
**Auditor:** Argus
**Purpose:** Replace "What I Got Wrong" section in Three Possibilities interlude with one-paragraph summary; move detailed corrections list to new appendix.

---

## Context

The "What I Got Wrong" section in `manuscript/interlude/three-possibilities-interlude.tex` lists 7 corrections with detailed explanations plus a "What these errors tell you" analysis. This is valuable defensive material but interrupts the reader's momentum between Three Possibilities and the dossier interlude. Replace with one summary paragraph pointing to the appendix.

## Branch

**`maugham-revision`** — primary. Also apply to **`main`** if corrections exist there (check `manuscript/00-front/corrections.tex` on the `main` branch).

## Launch

```
cd ~/software/relinquishment && claude
```

## Phase 1: Create Appendix

**Read first:** `manuscript/appendix/predictions.tex` — match its styling for the new appendix.

**Read:** `manuscript/interlude/three-possibilities-interlude.tex` — find the `\section*{What I Got Wrong}` section. It contains:
- Opening paragraphs (2 paragraphs about errors and listing them)
- 7 numbered corrections (`\textbf{1. Bravo Two Zero...}` through `\textbf{7. EO 13026...}`)
- "What these errors tell you" closing paragraphs
- "If I had perfect recall..." final line

**Create:** `manuscript/appendix/corrections.tex`

**Format:**
```latex
\chapter{What I Got Wrong}
\label{appendix:corrections}
```

Move ALL of the above content into this file. Keep content verbatim — no edits to the corrections themselves. The opening paragraphs ("The source material in this book spans twenty years...") become the appendix introduction.

## Phase 2: Replace Section in Interlude

**Edit:** `manuscript/interlude/three-possibilities-interlude.tex`

Find the `\section*{What I Got Wrong}` section. Replace EVERYTHING from that `\section*` through the `\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}` that follows the corrections (but NOT the next section "A Warning About Certainty") with:

```latex
\section*{What I Got Wrong}

This book spans twenty years of memory. I got some things wrong --- patrol compositions, historical myths I repeated without checking, technical details that drifted. A full list of corrections I have identified is in Appendix~\ref{appendix:corrections}. I prefer you find them there rather than discover them yourself and wonder what else I got wrong.

\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}
```

## Phase 3: Add to main.tex

**Read:** `main.tex` — find the `\appendix` section.

**Add** after the `predictions` include and before `abstracts`:
```latex
\include{manuscript/appendix/corrections}
```

Existing appendix order: rlhf-bias → predictions → **corrections (NEW)** → abstracts → glossary → timeline → sources → [dms-note conditional].

**Also check `main` branch:** `git stash && git checkout main` — check if `manuscript/00-front/corrections.tex` exists there. If so, that file is already the full corrections content; just add an `\include` for it in the appendix section of `main`'s `main.tex` and update any references. Then `git checkout maugham-revision && git stash pop` to return.

## Phase 4: Compile and verify

1. `make dev` on `maugham-revision` — zero errors
2. Verify: interlude has one-paragraph corrections summary
3. Verify: `\ref{appendix:corrections}` resolves to correct appendix letter (e.g., "Appendix C")
4. Verify: appendix contains all 7 corrections + closing analysis
5. Verify: TOC shows new appendix entry
6. If `main` branch was modified, compile there too

## Acceptance Criteria

- `make dev` succeeds on both branches
- Interlude is shorter by ~25 lines
- No corrections content lost — all moved to appendix
- Cross-reference resolves correctly
- Appendix renders cleanly

## Build System Notes

- `\label{appendix:corrections}` must be inside the appendix file (after `\chapter`)
- `\ref` in the interlude will render as the appendix letter
- `make dev` runs `latexmk` then builds HTML — both must pass
- Existing macros: `\settrack{}` sets margin color, `\chapterreturn` adds navigation footer, `\srcnote{}` adds source annotations — see existing appendices for usage patterns

## Handoff

```
cd ~/software/relinquishment && claude
```

You are the Generator. First run `pwd` to verify you are in `~/software/relinquishment` — if not, STOP and tell Bruce. Then read plan `plans/0084-corrections-to-appendix.md` and execute all phases. Move the "What I Got Wrong" corrections list from the Three Possibilities interlude to a new appendix. Replace with a one-paragraph summary pointing to the appendix. Work on `maugham-revision` branch first, then check `main`. Compile and verify on both.
