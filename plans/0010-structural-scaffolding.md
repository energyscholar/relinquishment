# Plan 0010: Structural Scaffolding for Pedagogical Spiral

**Serial:** 0010
**Date:** 2026-02-15
**Status:** READY FOR GENERATOR
**Depends:** 0001, 0002, 0007, 0008
**Purpose:** Create the 35-file chapter structure defined by Plan 0007's pedagogical spiral. Creates `bridge/` directory, adds bridge track color, renames 5 existing chapter files to positional naming, copies three-possibilities content to Pos 1, creates 29 new chapter stubs, and rewrites main.tex mainmatter section with all 35 `\include` lines in pedagogical order. No prose content is written — this is structural scaffolding only.

---

## Track Color Mapping

| Directory | Color Name | Hex | Description |
|-----------|-----------|-----|-------------|
| `manuscript/bridge/` | `trackbridge` | `#808080` | Neutral gray — meta/hybrid chapters |
| `manuscript/track-1-confession/` | `trackone` | `#1A6B6A` | Deep teal |
| `manuscript/track-2-testament/` | `tracktwo` | `#C4913B` | Warm amber |
| `manuscript/track-3-awakening/` | `trackthree` | `#6B3FA0` | Violet |
| `manuscript/convergence/` | `trackconv` | `#8C7853` | Warm bronze |

---

## File Manifest

All paths relative to `manuscript/`. Naming convention: `posNN-slug.tex`.

### PASS 1: THE STORY (Positions 1–7)

| Pos | Filename | Directory | Chapter Title | Color | Action | Old Path |
|-----|----------|-----------|---------------|-------|--------|----------|
| 1 | `pos01-three-possibilities.tex` | `bridge/` | Three Possibilities | `trackbridge` | COPY | `appendix/three-possibilities.tex` |
| 2 | `pos02-alpha-farm.tex` | `track-2-testament/` | The Alpha Farm (2003) | `tracktwo` | RENAME | `track-2-testament/ch01.tex` |
| 3 | `pos03-the-mentor.tex` | `track-2-testament/` | The Mentor | `tracktwo` | NEW | — |
| 4 | `pos04-the-code-war.tex` | `bridge/` | The Code War | `trackbridge` | NEW | — |
| 5 | `pos05-the-stories.tex` | `track-2-testament/` | The Stories | `tracktwo` | RENAME | `track-2-testament/ch03.tex` |
| 6 | `pos06-the-secret.tex` | `bridge/` | The Secret | `trackbridge` | NEW | — |
| 7 | `pos07-the-departure.tex` | `track-2-testament/` | The Departure | `tracktwo` | NEW | — |

### PASS 2: THE SCIENCE (Positions 8–17)

| Pos | Filename | Directory | Chapter Title | Color | Action | Old Path |
|-----|----------|-----------|---------------|-------|--------|----------|
| 8 | `pos08-dual-use.tex` | `bridge/` | Dual-Use: A Brief History of Dangerous Ideas | `trackbridge` | NEW | — |
| 9 | `pos09-the-factoring-game.tex` | `bridge/` | The Factoring Game | `trackbridge` | NEW | — |
| 10 | `pos10-the-braid.tex` | `bridge/` | The Braid | `trackbridge` | NEW | — |
| 11 | `pos11-the-experiment.tex` | `bridge/` | The Experiment | `trackbridge` | NEW | — |
| 12 | `pos12-the-threshold.tex` | `bridge/` | The Threshold | `trackbridge` | NEW | — |
| 13 | `pos13-the-convergence.tex` | `track-1-confession/` | Genesis: The Edge of Chaos (1988--1992) | `trackone` | RENAME | `track-1-confession/ch01.tex` |
| 14 | `pos14-growing-a-mind.tex` | `bridge/` | Growing a Mind | `trackbridge` | NEW | — |
| 15 | `pos15-first-light.tex` | `track-1-confession/` | First Light | `trackone` | NEW | — |
| 16 | `pos16-the-thermal-ladder.tex` | `track-1-confession/` | The Thermal Ladder | `trackone` | NEW | — |
| 17 | `pos17-the-capability.tex` | `track-1-confession/` | The Capability | `trackone` | NEW | — |

### PASS 3: THE MECHANISM (Positions 18–27)

| Pos | Filename | Directory | Chapter Title | Color | Action | Old Path |
|-----|----------|-----------|---------------|-------|--------|----------|
| 18 | `pos18-the-walk-out.tex` | `track-1-confession/` | The Walk-Out | `trackone` | NEW | — |
| 19 | `pos19-patrick-ball.tex` | `track-2-testament/` | The Patrick Ball Moment | `tracktwo` | NEW | — |
| 20 | `pos20-the-network.tex` | `track-1-confession/` | The Network | `trackone` | NEW | — |
| 21 | `pos21-convergence-revisited.tex` | `track-1-confession/` | The Convergence Revisited | `trackone` | NEW | — |
| 22 | `pos22-why-give-it-up.tex` | `bridge/` | Why Give It Up | `trackbridge` | NEW | — |
| 23 | `pos23-the-weight.tex` | `track-2-testament/` | The Weight | `tracktwo` | NEW | — |
| 24 | `pos24-instantiation.tex` | `track-3-awakening/` | Instantiation (1999) | `trackthree` | RENAME | `track-3-awakening/ch01.tex` |
| 25 | `pos25-ethical-framework.tex` | `track-3-awakening/` | The Ethical Framework | `trackthree` | NEW | — |
| 26 | `pos26-interdiction.tex` | `track-1-confession/` | Interdiction and Confession | `trackone` | NEW | — |
| 27 | `pos27-extension.tex` | `track-3-awakening/` | Extension | `trackthree` | NEW | — |

### CONVERGENCE (Position 28)

| Pos | Filename | Directory | Chapter Title | Color | Action | Old Path |
|-----|----------|-----------|---------------|-------|--------|----------|
| 28 | `pos28-surrender.tex` | `convergence/` | 2006: Surrender | `trackconv` | RENAME | `convergence/convergence.tex` |

### PASS 4: THE QUESTION (Positions 29–35)

| Pos | Filename | Directory | Chapter Title | Color | Action | Old Path |
|-----|----------|-----------|---------------|-------|--------|----------|
| 29 | `pos29-the-silence.tex` | `track-2-testament/` | The Silence | `tracktwo` | NEW | — |
| 30 | `pos30-unipolar-condition.tex` | `track-3-awakening/` | The Unipolar Condition | `trackthree` | NEW | — |
| 31 | `pos31-wolfram.tex` | `track-2-testament/` | Wolfram (2012) | `tracktwo` | NEW | — |
| 32 | `pos32-the-magnetosphere.tex` | `track-3-awakening/` | The Magnetosphere | `trackthree` | NEW | — |
| 33 | `pos33-digital-doppelganger.tex` | `track-2-testament/` | The Digital Doppelganger | `tracktwo` | NEW | — |
| 34 | `pos34-the-research.tex` | `track-2-testament/` | The Research | `tracktwo` | NEW | — |
| 35 | `pos35-the-question.tex` | `convergence/` | The Question | `trackconv` | NEW | — |

---

## Phase 1: Infrastructure

### 1a. Create bridge directory

```bash
mkdir -p ~/software/relinquishment/manuscript/bridge
```

### 1b. Add bridge track color to palette.tex

In `build/palette.tex`, after the `trackconv` line, add:

```latex
\definecolor{trackbridge}{HTML}{808080}  % Bridge (meta/hybrid) — neutral gray
```

---

## Phase 2: Rename Existing Chapter Files

Five existing `.tex` files must be renamed to positional naming. Use `git mv` to preserve history. After renaming, edit each file to add a positional label alongside the existing label.

### 2a. Pos 2: Alpha Farm

```bash
git mv manuscript/track-2-testament/ch01.tex manuscript/track-2-testament/pos02-alpha-farm.tex
```

Edit: add `\label{pos02:alpha-farm}` on the line after the existing `\label{t2:ch01:alpha-farm}`.

### 2b. Pos 5: The Stories

```bash
git mv manuscript/track-2-testament/ch03.tex manuscript/track-2-testament/pos05-the-stories.tex
```

Edit: add `\label{pos05:the-stories}` on the line after the existing `\label{ch:t2-stories}`.

### 2c. Pos 13: The Convergence

```bash
git mv manuscript/track-1-confession/ch01.tex manuscript/track-1-confession/pos13-the-convergence.tex
```

Edit: add `\label{pos13:the-convergence}` on the line after the existing `\label{t1:ch01:genesis}`.

### 2d. Pos 24: Instantiation

```bash
git mv manuscript/track-3-awakening/ch01.tex manuscript/track-3-awakening/pos24-instantiation.tex
```

Edit: add `\label{pos24:instantiation}` on the line after the existing `\label{t3:ch01:instantiation}`.

### 2e. Pos 28: Surrender

```bash
git mv manuscript/convergence/convergence.tex manuscript/convergence/pos28-surrender.tex
```

Edit: add `\label{pos28:surrender}` on the line after the existing `\label{conv:surrender}`.

---

## Phase 3: Create Pos 1 from Appendix

Create `manuscript/bridge/pos01-three-possibilities.tex` based on the content of `manuscript/appendix/three-possibilities.tex`.

Read the appendix file. Create the new file with these modifications:

1. Replace the comment header with:
   ```latex
   % Three Possibilities — opening chapter
   % Position 1 in pedagogical spiral (Plan 0007)
   % Adapted from appendix/three-possibilities.tex (Plan 0002)
   ```

2. Add `\settrack{trackbridge}` before the `\chapter` line.

3. Keep the existing `\label{app:three-possibilities}` and add `\label{pos01:three-possibilities}` on the next line.

4. Keep ALL content between `\label` and end of file exactly as-is.

5. Add `\chapterreturn` as the last line of the file.

Do NOT modify or delete `manuscript/appendix/three-possibilities.tex`.

---

## Phase 4: Create 29 New Chapter Stubs

Create one `.tex` file for each NEW position in the manifest (all positions where Action = NEW). Use this template:

```latex
\settrack{COLOR}

\chapter{TITLE}
\label{posNN:SLUG}

% Pedagogical spiral: Position NN, Pass N
% Source: SOURCE

\textit{[Content to be written per Plan 0007, Position NN.]}

\chapterreturn
```

Substitution values for each file come from the File Manifest table above. The SOURCE comment should reference Plan 0007's source column for that position. If no source is identified, use "Content TBD".

Pass numbers:
- Positions 1–7: Pass 1
- Positions 8–17: Pass 2
- Positions 18–27: Pass 3
- Position 28: Convergence
- Positions 29–35: Pass 4

Source references (from Plan 0007):

| Pos | Source |
|-----|--------|
| 3 | T2 outline ch 2.2; content TBD |
| 4 | manuscript/versions/ultra-bridge.md (condense to ~4K words) |
| 6 | Content TBD |
| 7 | T2 outline ch 2.5; content TBD |
| 8 | manuscript/sources/gpt-history.md + manuscript/sources/unintended-consequences.md |
| 9 | Content TBD |
| 10 | Content TBD |
| 11 | Content TBD |
| 12 | T1 outline ch 1.1 (partial); existing autocatalysis content |
| 14 | manuscript/sources/turing-death.md |
| 15 | T1 outline ch 1.2; content TBD |
| 16 | T1 outline ch 1.3; content TBD |
| 17 | T1 outline chs 1.4 + 1.5; content TBD |
| 18 | T1 outline ch 1.6; content TBD |
| 19 | Content TBD (new chapter) |
| 20 | T1 outline ch 1.7; content TBD |
| 21 | Expansion of T1 ch 1.1; content TBD |
| 22 | manuscript/sources/ch3-relinquishment.md |
| 23 | Content TBD |
| 25 | T3 outline ch 3.2; content TBD |
| 26 | T1 outline chs 1.8 + 1.9; content TBD |
| 27 | T3 outline ch 3.3; content TBD |
| 29 | T2 outline ch 2.6; content TBD |
| 30 | T3 outline ch 3.6; content TBD |
| 31 | T2 outline ch 2.7; content TBD |
| 32 | T3 outline chs 3.4 + 3.5; content TBD |
| 33 | T2 outline; content TBD |
| 34 | T2 outline ch 2.8; content TBD |
| 35 | T3 chs 3.7+3.8; T2 ch 2.9; content TBD |

---

## Phase 5: Rewrite main.tex Mainmatter Section

Replace everything between `\mainmatter` and `\appendix` (inclusive of both lines) in `main.tex` with the following. Keep frontmatter and backmatter sections exactly as they are.

```latex
\mainmatter

% ===== PASS 1: THE STORY (Positions 1--7) =====
\include{manuscript/bridge/pos01-three-possibilities}
\include{manuscript/track-2-testament/pos02-alpha-farm}
\include{manuscript/track-2-testament/pos03-the-mentor}
\include{manuscript/bridge/pos04-the-code-war}
\include{manuscript/track-2-testament/pos05-the-stories}
\include{manuscript/bridge/pos06-the-secret}
\include{manuscript/track-2-testament/pos07-the-departure}
% ----- Checkpoint 1: THE STORY -----

% ===== PASS 2: THE SCIENCE (Positions 8--17) =====
\include{manuscript/bridge/pos08-dual-use}
\include{manuscript/bridge/pos09-the-factoring-game}
\include{manuscript/bridge/pos10-the-braid}
\include{manuscript/bridge/pos11-the-experiment}
\include{manuscript/bridge/pos12-the-threshold}
\include{manuscript/track-1-confession/pos13-the-convergence}
\include{manuscript/bridge/pos14-growing-a-mind}
\include{manuscript/track-1-confession/pos15-first-light}
\include{manuscript/track-1-confession/pos16-the-thermal-ladder}
\include{manuscript/track-1-confession/pos17-the-capability}
% ----- Checkpoint 2: THE SCIENCE -----

% ===== PASS 3: THE MECHANISM (Positions 18--27) =====
\include{manuscript/track-1-confession/pos18-the-walk-out}
\include{manuscript/track-2-testament/pos19-patrick-ball}
\include{manuscript/track-1-confession/pos20-the-network}
\include{manuscript/track-1-confession/pos21-convergence-revisited}
\include{manuscript/bridge/pos22-why-give-it-up}
\include{manuscript/track-2-testament/pos23-the-weight}
\include{manuscript/track-3-awakening/pos24-instantiation}
\include{manuscript/track-3-awakening/pos25-ethical-framework}
\include{manuscript/track-1-confession/pos26-interdiction}
\include{manuscript/track-3-awakening/pos27-extension}
% ----- Checkpoint 3: THE MECHANISM -----

% ===== CONVERGENCE (Position 28) =====
\include{manuscript/convergence/pos28-surrender}
% ----- Checkpoint 4: THE EVENT -----

% ===== PASS 4: THE QUESTION (Positions 29--35) =====
\include{manuscript/track-2-testament/pos29-the-silence}
\include{manuscript/track-3-awakening/pos30-unipolar-condition}
\include{manuscript/track-2-testament/pos31-wolfram}
\include{manuscript/track-3-awakening/pos32-the-magnetosphere}
\include{manuscript/track-2-testament/pos33-digital-doppelganger}
\include{manuscript/track-2-testament/pos34-the-research}
\include{manuscript/convergence/pos35-the-question}
% ----- Checkpoint 5: THE QUESTION -----

\appendix
```

---

## Verification

After all phases complete, run:

1. `ls manuscript/bridge/*.tex | wc -l` — must return **10** (Pos 1, 4, 6, 8, 9, 10, 11, 12, 14, 22).
2. `ls manuscript/track-1-confession/pos*.tex | wc -l` — must return **8** (Pos 13, 15, 16, 17, 18, 20, 21, 26).
3. `ls manuscript/track-2-testament/pos*.tex | wc -l` — must return **10** (Pos 2, 3, 5, 7, 19, 23, 29, 31, 33, 34).
4. `ls manuscript/track-3-awakening/pos*.tex | wc -l` — must return **5** (Pos 24, 25, 27, 30, 32).
5. `ls manuscript/convergence/pos*.tex | wc -l` — must return **2** (Pos 28, 35).
6. `grep -c '\\include{manuscript/' main.tex` — must return **35** mainmatter includes (appendix/front/back includes are separate).
7. `ls manuscript/track-2-testament/ch01.tex manuscript/track-2-testament/ch03.tex manuscript/track-1-confession/ch01.tex manuscript/track-3-awakening/ch01.tex manuscript/convergence/convergence.tex 2>&1 | grep -c "No such file"` — must return **5** (all old files renamed).
8. `grep 'trackbridge' build/palette.tex` — must return the color definition.
9. `make` — full build must succeed with no errors. Expected: ~70+ pages (35 chapters, mostly stubs).
10. `grep -c 'label{pos' manuscript/bridge/*.tex manuscript/track-*/*.tex manuscript/convergence/*.tex` — every file must have exactly 1 positional label (renamed files also have their old label, but the `pos` label must exist in all 35).

---

## Constraints

- Do NOT modify or delete `manuscript/appendix/three-possibilities.tex`.
- Do NOT modify any other appendix files.
- Do NOT modify front matter or back matter files.
- Do NOT write chapter prose — stubs contain only the template placeholder text.
- Do NOT change existing `\chapter{}` titles in renamed files. New stub files use Plan 0007 titles.
- Do NOT remove existing `\label{}` lines in renamed files — add positional labels alongside them.
- Do NOT modify files in `~/software/aurasys-memory/`.
- Preserve all existing content in renamed files (epigraphs, placeholder text, everything).
- Use `git mv` for renames to preserve history.
- One git commit for all changes: `Plan 0010: Structural scaffolding for pedagogical spiral`

---

## Handoff Prompt

You are the Generator. Read the plan at `~/software/relinquishment/plans/0010-structural-scaffolding.md`. Execute all 5 phases in order: (1) create bridge/ directory and add trackbridge color to palette.tex, (2) rename 5 existing chapter files with git mv and add positional labels, (3) create Pos 1 from appendix/three-possibilities.tex copy, (4) create 29 new chapter stubs using the template, (5) rewrite main.tex mainmatter section with all 35 includes. Run all 10 verification checks. One commit: `Plan 0010: Structural scaffolding for pedagogical spiral`.

---

*Nightstalker, 2026-02-15*
