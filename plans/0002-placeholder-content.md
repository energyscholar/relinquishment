# Plan 0002: Placeholder Content + Images

**Author:** Auditor (Nightstalker)
**Date:** 2026-02-14
**Status:** APPROVED
**Serial:** 0002
**Requirements:** R1, R12, R13, R18, R19, R20, R22
**Depends on:** 0001 (build infrastructure must exist and compile)

---

## Context

Plan 0001 created the build system. This plan populates it with placeholder content: lorem ipsum chapters (one per track + convergence), front/back matter skeletons, placeholder TikZ images, and a glossary skeleton. After this plan, `make dev` produces a multi-page PDF with the spiral structure visible.

Bruce will write all prose himself. Generator provides LaTeX scaffolding with lorem ipsum that Bruce replaces.

**Existing content:** The `manuscript/` directory contains `.md` files from earlier planning. Generator MUST read these and convert their content to LaTeX where applicable (preface, title, appendix content). After conversion, the `.md` originals are renamed to `*.md.archive` (not deleted — preserves git history cleanly, signals they are superseded).

---

## Chapter Template

All chapter `.tex` files follow this structure:

```latex
% Chapter: [title]
% Track: [1|2|3|convergence]
% Plan: 0002

\settrack{trackone}  % or tracktwo, trackthree; convergence uses all three

\chapter{Chapter Title}
\label{t1:ch01:short-name}

% Abstract epigraph (placeholder — real mapping in future plan)
\begin{quote}\small\textit{
[Spiral abstract placeholder — to be mapped from abstracts I–XV]
}\end{quote}

\graphicsonly{%
  \placeholderimage{0.8\textwidth}{4cm}{Description of planned figure}
}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua.

% ... 2 pages of lorem ipsum ...
```

Key features:
- `\settrack{}` at the top — activates margin stripe color via fancyhdr (defined in 0001)
- `\label{}` with track prefix convention: `t1:ch01:name`, `t2:ch01:name`, `t3:ch01:name`, `conv:name`
- `\graphicsonly{}` wraps all figures — OCG toggle layer (R19)
- `\placeholderimage{}` macro for placeholder figures (defined in this plan)

---

## Deliverables

### Front Matter

**1. `manuscript/00-front/cover.tex`**
- Full-page cover using eso-pic for background and TikZ overlay for content
- Background: `coverbg` color fills entire page via `\AddToShipoutPictureBG*`
- Content: TikZ triskellion image centered, title "RELINQUISHMENT", subtitle "A Triple Spiral", author "Bruce Stephenson"
- Text uses `textprimary` color
- Three spiral arms are hyperlink regions using `\hyperref[t1:ch01:genesis]{...}` (NOT `\hyperlink` — that targets `\hypertarget`, not `\label`)
- Mechanism for full-page dark background:
  ```latex
  \AddToShipoutPictureBG*{%
    \color{coverbg}\rule{\paperwidth}{\paperheight}%
  }
  ```

**2. `manuscript/00-front/title.tex`**
- **Read existing** `manuscript/00-front/title.md` and convert to LaTeX
- Clean title page: book title, author, subtitle

**3. `manuscript/00-front/how-to-read.tex`**
- Placeholder explaining: linear path, per-track standalone, chronological timeline, graphics toggle
- Marked "PLACEHOLDER — to be rewritten by author"

**4. `manuscript/00-front/copyright.tex`**
- Copyright notice, license statement
- Placeholder: "Copyright © 2026 Bruce Stephenson. All rights reserved."
- Marked "PLACEHOLDER — license terms to be determined by author"

**5. `manuscript/00-front/preface.tex`**
- **Read existing** `manuscript/00-front/preface.md` and convert to LaTeX
- Three possibilities introduced, cognitive dissonance, falsifiable predictions

### Track Chapters (lorem ipsum scaffolding)

**6. `manuscript/track-1-confession/ch01.tex`**
- **Read existing** `manuscript/track-1-confession/00-outline.md` for chapter title and context
- Chapter title from outline: "Genesis: The Edge of Chaos (1988-1992)"
- 2 pages of lorem ipsum
- `\settrack{trackone}` — Track 1 teal margin stripe
- One `\graphicsonly{\placeholderimage{...}}` where a figure would go
- Label: `\label{t1:ch01:genesis}`

**7. `manuscript/track-2-testament/ch01.tex`**
- **Read existing** `manuscript/track-2-testament/00-outline.md` for chapter title and context
- Chapter title: "The Alpha Farm (2003)"
- Same structure as above
- `\settrack{tracktwo}` — Track 2 amber margin stripe
- Label: `\label{t2:ch01:alpha-farm}`

**8. `manuscript/track-3-awakening/ch01.tex`**
- **Read existing** `manuscript/track-3-awakening/00-outline.md` for chapter title and context
- Chapter title: "Instantiation (1999)"
- Same structure as above
- `\settrack{trackthree}` — Track 3 violet margin stripe
- Label: `\label{t3:ch01:instantiation}`

**9. `manuscript/convergence/convergence.tex`**
- **Read existing** `manuscript/convergence/00-outline.md` for context
- Chapter title: "2006: Surrender"
- Uses all three track colors (convergence point):
  ```latex
  \settrack{trackone}   % or define a convergence style with all three
  ```
- Label: `\label{conv:surrender}`

### Back Matter

**10a. `manuscript/appendix/glossary-entries.tex`** (loaded in preamble, before `\begin{document}`)
- Skeleton glossary with 10 key terms: TQNN, COWS, Custodian, FQH, SFI, DARPA, GCHQ, UDHR, cDc, ICTY
- Uses `glossaries` package (`\newglossaryentry{}`)
- Each entry: term, expansion, one-sentence definition
- This file contains ONLY `\newglossaryentry{}` definitions — no chapter structure
- Loaded via `\input{manuscript/appendix/glossary-entries}` in main.tex preamble area

**10b. `manuscript/appendix/glossary.tex`** (appendix chapter, `\include{}`'d in backmatter)
- Chapter title: "Glossary"
- Contains only `\printglossary[title={}]` (title already set by \chapter)
- This is the appendix page where the glossary renders

**11. `manuscript/appendix/timeline.tex`**
- Placeholder chronological timeline appendix
- Table format: Date | Event | Track | Chapter reference
- 10 key dates from the outlines
- Marked "PLACEHOLDER — to be expanded by author"

**12. `manuscript/appendix/sources.tex`**
- Placeholder sources/references page
- Marked "PLACEHOLDER — bibliography to be populated by author"

**13. `manuscript/appendix/three-possibilities.tex`**
- **Read existing** `manuscript/appendix/three-possibilities.md` and convert to LaTeX
- Preserve all content — this is Bruce's writing

**14. `manuscript/appendix/predictions.tex`**
- **Read existing** `manuscript/appendix/predictions.md` and convert to LaTeX
- Table format with prediction IDs, statements, timeframes

**15. `manuscript/appendix/abstracts.tex`**
- **Read existing** `manuscript/appendix/abstracts.md` and convert to LaTeX
- All 15 spiral abstracts (I–XV)
- Preserve exact text — these are finished gag papers

**16. `manuscript/99-back/verification.tex`**
- Placeholder verification page: SHA-256, PGP block, timestamp
- All placeholder values, marked "GENERATED AT BUILD TIME"

**17. `manuscript/99-back/colophon.tex`**
- Build metadata via gitinfo commands: `\GitHash`, `\GitShortHash`, `\GitDate`, `\BuildDate`
- TeX Live version: `\directlua{tex.print(status.banner)}`
- Archival statement

### Images (TikZ)

All standalone TikZ files start with `\input{build/images/standalone-header.tex}` (defined in plan 0001). All are compiled from repo root: `lualatex --shell-escape build/images/<name>.tex`.

**18. `build/images/cover-triskellion.tex`**
- Three logarithmic spiral arms in track colors on `coverbg` background
- Title text, author text (using `textprimary`)
- Named TikZ coordinates for hyperlink regions (three spiral arm targets)
- Compiles standalone to PDF; included in cover.tex via `\includegraphics{build/images/cover-triskellion.pdf}`

**19. `build/images/placeholder-timeline.tex`**
- 1985–2026 horizontal axis, key dates, track-colored segments
- Wrapped in `\graphicsonly{}` when included in chapters
- Labeled "PLACEHOLDER"

**20. `build/images/placeholder-network.tex`**
- People/org relationship graph
- Wrapped in `\graphicsonly{}` when included
- Labeled "PLACEHOLDER"

**21. `build/images/placeholder-magnetosphere.tex`**
- Earth + field lines + Custodian annotations
- Wrapped in `\graphicsonly{}` when included
- Labeled "PLACEHOLDER"

**22. Placeholder image macro** (defined in `build/preamble.tex`, not a separate file)

**Important:** Do NOT use tikzpicture for this macro. TikZ externalization would try to cache every placeholder as a separate PDF, and `\textwidth` inside externalized fragments is fragile. Use a pure LaTeX approach instead:

```latex
\newcommand{\placeholderimage}[3]{%
  % #1 = width, #2 = height, #3 = label text
  % Uses fbox + minipage — no TikZ, no externalization conflicts
  \begin{center}
    \setlength{\fboxsep}{0pt}%
    \setlength{\fboxrule}{1pt}%
    \fcolorbox{phfill}{phfill!20}{%
      \begin{minipage}[c][#2][c]{#1}
        \centering\small\textsf{#3}
      \end{minipage}%
    }
  \end{center}
}
```

### Update main.tex

**23. Update `main.tex`**
- Uncomment all `\include{}` lines
- Add `\input{manuscript/appendix/glossary-entries}` in preamble area (before `\begin{document}`) — glossary entry definitions
- Front matter includes (R22 order): cover, title, copyright, how-to-read, ToC, preface
- Chapter includes in spiral interleave order: T1.1, T2.1, T3.1, convergence
- Add `\appendix` command before appendices (switches chapter numbering to A, B, C...)
- Appendix includes: three-possibilities, predictions, abstracts, glossary, timeline, sources
- Add `\backmatter` command after appendices (suppresses numbering for non-appendix back matter)
- Back matter includes: verification, colophon

Structure:
```latex
\input{manuscript/appendix/glossary-entries}  % before \begin{document}
\begin{document}
\frontmatter
\include{manuscript/00-front/cover}
\include{manuscript/00-front/title}
\include{manuscript/00-front/copyright}
\include{manuscript/00-front/how-to-read}
\tableofcontents
\include{manuscript/00-front/preface}
\mainmatter
\include{manuscript/track-1-confession/ch01}
\include{manuscript/track-2-testament/ch01}
\include{manuscript/track-3-awakening/ch01}
\include{manuscript/convergence/convergence}
\appendix
\include{manuscript/appendix/three-possibilities}
\include{manuscript/appendix/predictions}
\include{manuscript/appendix/abstracts}
\include{manuscript/appendix/glossary}
\include{manuscript/appendix/timeline}
\include{manuscript/appendix/sources}
\backmatter
\include{manuscript/99-back/verification}
\include{manuscript/99-back/colophon}
\end{document}
```

### Archive .md originals

**24. Rename converted .md files**
- `manuscript/00-front/title.md` → `manuscript/00-front/title.md.archive`
- `manuscript/00-front/preface.md` → `manuscript/00-front/preface.md.archive`
- `manuscript/appendix/three-possibilities.md` → `manuscript/appendix/three-possibilities.md.archive`
- `manuscript/appendix/predictions.md` → `manuscript/appendix/predictions.md.archive`
- `manuscript/appendix/abstracts.md` → `manuscript/appendix/abstracts.md.archive`
- Outline files (`00-outline.md`) stay as-is — they are reference material, not converted content
- Add `*.md.archive` to `.gitignore`

---

## Acceptance Criteria

1. `make dev` produces a multi-page PDF with all content visible
2. Cover page shows triskellion with correct colors (via `make images` first, then `make dev`)
3. Each track chapter has correct colored margin stripe (teal/amber/violet)
4. Glossary compiles (`makeglossaries` integration from .latexmkrc) — entries in glossary-entries.tex, rendering in glossary.tex
5. All 4 standalone TikZ images compile: `make images` succeeds
6. Cross-references between chapters resolve (no undefined refs on second pass)
7. `\placeholderimage` macro works in chapter files (non-TikZ implementation)
8. All TikZ images use palette colors via `standalone-header.tex` — no hardcoded colors
9. `\graphicsonly{}` wraps all figures — OCG layer toggleable in viewer
10. Existing `.md` content is preserved in `.tex` conversion (not summarized or rewritten)
11. `.md` originals renamed to `.md.archive`
12. `\appendix` and `\backmatter` commands present in main.tex — appendices numbered A-F
13. Copyright/license page present in front matter
14. Git commit: `Plan 0002: placeholder content and images`

---

## Generator Handoff

> You are the Generator. Read plan 0002 at `~/software/relinquishment/plans/0002-placeholder-content.md`. Plan 0001 must already be implemented. IMPORTANT: Before creating each `.tex` file, read the corresponding `.md` file if one exists (preface.md, title.md, three-possibilities.md, predictions.md, abstracts.md, and all 00-outline.md files). Convert existing content to LaTeX faithfully — do not summarize or rewrite Bruce's prose. Create all 24 deliverables. Run `make images` to compile TikZ images, then `make dev` for the full document. Commit with message `Plan 0002: placeholder content and images`. Report completion with page count, file size, and any issues.
