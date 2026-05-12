# Subtask: Sync scientific-revolutions.tex to Current HTML

**Output:** Update `manuscript/spine/scientific-revolutions.tex` (139 lines) to
match the current chapter HTML after all session changes.
**Commit:** `Plan 0321: sync scientific-revolutions.tex — symbols, Nobel-level, figure refs`
**Read first:** The current .tex file, this spec. Do NOT read the standalone
HTML — all changes are specified here.

## Context

The .tex was created by an earlier Generator and wired into `main.tex` at
line 78. The build pipeline (pandoc → preprocess.py --fix-html) converts it
to the final chapter HTML. The .tex is now stale — it predates the ⬡¬◈/⬡◈
symbol rename, the "Nobel-level" fix, and SVG-055/SVG-056 figure placeholders.

This subtask is TEXT ONLY. SVG injection and accordion wrapping are handled
by preprocess.py and are separate subtasks.

---

## 1. Symbol Rename: A1/A2 → ⬡¬◈/⬡◈

The .tex uses lualatex (confirmed in Makefile). Unicode characters ⬡ (U+2B21),
◈ (U+25C8), ¬ (U+00AC) render natively — no special packages needed.

### First use (Adams-style introduction with gloss)

Line 87, change:
```
\textbf{A1:} Autocatalytic dynamics do not produce...
```
to:
```
\textbf{⬡¬◈ (A1):} Autocatalytic dynamics do not produce...
```

Line 89, change:
```
\textbf{A2:} The physics permits it...
```
to:
```
\textbf{⬡◈ (A2):} The physics permits it...
```

### Subsequent uses (bare symbols)

Every remaining instance of `A1` and `A2` in the prose becomes `⬡¬◈` and `⬡◈`.
There are 11 total instances across the file. The two first-use instances above
get the `(A1)`/`(A2)` gloss; the other 9 use bare symbols.

**Complete replacement list (lines are approximate — verify by surrounding text):**

| Line | Old text | New text |
|------|----------|----------|
| 87 | `\textbf{A1:}` | `\textbf{⬡¬◈ (A1):}` |
| 87 | `Under A1, Possibility~A` | `Under ⬡¬◈, Possibility~A` |
| 89 | `\textbf{A2:}` | `\textbf{⬡◈ (A2):}` |
| 89 | `Under A2, the situation` | `Under ⬡◈, the situation` |
| 91 | `A1 still advances` | `⬡¬◈ still advances` |
| 91 | `A2 opens a sixth` | `⬡◈ opens a sixth` |
| 102 | `the A1/A2 question resolves toward A2` | `the ⬡¬◈/⬡◈ question resolves toward ⬡◈` |
| 102 | `Under A1, none of these` | `Under ⬡¬◈, none of these` |
| 109 | `applies under A2` | `applies under ⬡◈` |
| 111 | `Under A2, the current situation` | `Under ⬡◈, the current situation` |
| 111 | `reverting to A1` | `reverting to ⬡¬◈` |
| 113 | `Under A1, the distributed` | `Under ⬡¬◈, the distributed` |
| 113 | `A1 means this is one` | `⬡¬◈ means this is one` |
| 115 | `A1 produces incremental` | `⬡¬◈ produces incremental` |
| 115 | `A2 produces a crisis` | `⬡◈ produces a crisis` |
| 130 | `Under A2, biology's definition` (4× in paragraph) | `Under ⬡◈,` (4×) |
| 132 | `Under A1, these implications` | `Under ⬡¬◈, these implications` |
| 137 | `if A2, if the physics` | `if ⬡◈, if the physics` |

After replacement: zero instances of bare `A1` or `A2` in the .tex (verify
with grep). The `(A1)` and `(A2)` glosses on lines 87 and 89 are the only
surviving references to the old names.

## 2. Nobel Fix

Line 83, change:
```
Nobel-caliber experimental confirmation
```
to:
```
Nobel-level experimental confirmation
```

## 3. SVG-055 Figure Placeholder

Insert after line 91 (after "Neither is a consolation prize.") and before the
existing SVG-056 fork diagram position. The SVG-055 spectrum is a `<details open>`
block in the HTML — it always shows. In the .tex, add a figure placeholder:

```latex
% SVG-055: Expert Consensus Spectrum (animated, click-to-play)
% HTML build: inline SVG injected by preprocess.py
% PDF build: static keyframe image
\begin{figure}[ht]
\centering
% \includegraphics[width=\textwidth]{build/images/svg055-spectrum-static.pdf}
\caption{Expert consensus spectrum: historical revolutions migrating from
``impossible'' to ``established,'' failed hypotheses fading out, and one
open question in progress.}
\label{fig:expert-spectrum}
\end{figure}
```

## 4. SVG-056 Figure Placeholder

The fork diagram sits between "Neither is a consolation prize." (after the
SVG-055 placeholder) and the first PhD seed blockquote. Insert:

```latex
% SVG-056: Consequence Fork Diagram (static)
% HTML build: inline SVG injected by preprocess.py
% PDF build: static image
\begin{figure}[ht]
\centering
% \includegraphics[width=0.85\textwidth]{build/images/svg056-fork-static.pdf}
\caption{Same evidence, same silence, different futures.}
\label{fig:consequence-fork}
\end{figure}
```

## 5. Deep Link References

The .tex already uses `Chapter~\ref{spine:...}` format for cross-references.
Verify these resolve:
- `\ref{spine:three-possibilities}` — line 19
- `\ref{spine:capabilities}` — line 46
- `\ref{spine:the-flat}` — line 46
- `\ref{spine:option-a}` — line 87
- `\ref{spine:option-c}` — line 89
- `\ref{spine:silence-gap}` — line 61
- `\ref{spine:sg-five-fields-no-bridge}` — line 61
- `\ref{spine:sg-the-gap}` — line 61
- `\ref{spine:strongest-objection}` — line 109, 137
- `\ref{spine:cap-think}` — line 130
- `\ref{spine:why-relinquish}` — line 102, 130

If any `\ref{}` target doesn't exist in the current manuscript, flag it in
the report — do NOT invent labels.

## Ordering

The section order in the .tex already matches the HTML:
1. The Pattern (+ SVG-054 figure)
2. The Current Paradigm
3. Anomaly Accumulation (+ PhD seed #1)
4. Life in the Flat (+ SVG-055, SVG-056, PhD seed #2)
5. Beyond the Laboratory
6. How It Plays Out (+ PhD seed #3)
7. The Social Process
8. The Reader's Position

Verify this order is preserved after edits.

## Do NOT

- Add accordion/`<details>` markup (preprocess.py handles this)
- Add concept symbol markup (preprocess.py handles this)
- Add tooltip annotations (preprocess.py handles this)
- Change any prose beyond the specific replacements listed
- Add LaTeX packages or preamble changes
- Modify main.tex or any other .tex file
- Create static PDF versions of the SVGs
- Run `make` — just edit the .tex

## Report

Confirm:
1. Zero instances of bare `A1` or `A2` in prose (grep)
2. Two instances of `(A1)` and `(A2)` as glosses only
3. "Nobel-level" not "Nobel-caliber" (grep)
4. SVG-055 and SVG-056 figure placeholders present with labels
5. All `\ref{}` targets listed, noting any that may not resolve
6. Section order preserved
7. Total line count (should be ~155–160, up from 139)
