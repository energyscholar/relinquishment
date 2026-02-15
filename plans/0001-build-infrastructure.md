# Plan 0001: Build Infrastructure

**Author:** Auditor (Nightstalker)
**Date:** 2026-02-14
**Status:** APPROVED
**Serial:** 0001
**Requirements:** R0, R17, R18, R19, R24
**Depends on:** nothing (first plan)

---

## Context

The relinquishment repo has manuscript outlines but no LaTeX build system. This plan creates the build infrastructure: Makefile, LuaLaTeX configuration, preamble with conditional compilation, Docker scaffold (deferred — Docker not available on current host), and validation pipeline. After this plan, `make dev` should compile a minimal document.

**TeX Live constraint:** Host system has TeX Live 2022. Tagged PDF (tagpdf) requires TeX Live 2025+. Dev builds work on host. Final/tagged builds require Docker (not currently installed — deferred to a future plan). The preamble uses `\ifdefined\FINAL` to gate tagging — it is NOT active in dev builds.

**Docker status:** Not installed on current host. Dockerfile is written but untested. Docker-dependent targets (`make final`, `make screen`, `make print`) print a clear error message when Docker is unavailable. This is acceptable — dev builds are the priority now.

---

## Prerequisites

**Generator must verify these before starting. If any fail, install the missing package first.**

```bash
# Required for build orchestration
which latexmk    || sudo apt install -y latexmk

# Required for standalone TikZ compilation (luatex85.sty)
kpsewhich luatex85.sty || sudo apt install -y texlive-luatex

# Should already be present (verify)
which lualatex        # LuaLaTeX engine
which makeglossaries  # Glossary compilation
```

**Current host status (2026-02-14):**
- `latexmk` — NOT installed. Must install.
- `texlive-luatex` — NOT installed. Must install (provides `luatex85.sty` needed by `standalone` class).
- `lualatex` — installed.
- `makeglossaries` — installed.

---

## Decisions

| Decision | Choice |
|----------|--------|
| Source format | LaTeX (.tex) |
| Engine | LuaLaTeX (required for tagpdf, fontspec, Unicode) |
| Build orchestration | Makefile (repo root) + latexmk |
| Screen layout | Letter landscape (11in × 8.5in), single column, generous margins |
| Print layout | Letter portrait, book margins (inner/outer gutter) |
| Reproducibility | Docker + SOURCE_DATE_EPOCH (Docker deferred) |
| Font handling | fontspec (LuaLaTeX native), NOT fontenc/cmap (pdfLaTeX legacy) |

---

## Color Palette (canonical)

Define in `build/palette.tex`. The preamble `\input{}`s this file. Standalone TikZ images also `\input{}` it (all compilation happens from repo root).

| Name | Hex | LaTeX | Usage |
|------|-----|-------|-------|
| Track 1 (Confession) | `#1A6B6A` | `\definecolor{trackone}{HTML}{1A6B6A}` | Deep teal |
| Track 2 (Testament) | `#C4913B` | `\definecolor{tracktwo}{HTML}{C4913B}` | Warm amber |
| Track 3 (Awakening) | `#6B3FA0` | `\definecolor{trackthree}{HTML}{6B3FA0}` | Violet |
| Cover background | `#0D1117` | `\definecolor{coverbg}{HTML}{0D1117}` | Near-black |
| Text on dark | `#E6EDF3` | `\definecolor{textprimary}{HTML}{E6EDF3}` | Cover text |
| Placeholder fill | `#D0D0D0` | `\definecolor{phfill}{HTML}{D0D0D0}` | Gray boxes |
| Body text | `#1A1A1A` | `\definecolor{bodytext}{HTML}{1A1A1A}` | Near-black |
| Link color | `#2563EB` | `\definecolor{linkblue}{HTML}{2563EB}` | Accessible blue |

---

## Deliverables

### 1. `Makefile` (repo root)

The Makefile lives at the repo root (not `build/`). All commands are run from repo root.

Targets:
- `make dev` — fast dev build via latexmk. No tagging. Uses `\includeonly{}` if set. Target: < 30 sec.
- `make final` — full build with tagging (requires Docker). Prints error if Docker unavailable.
- `make screen` — landscape geometry. Implies `final`. Requires Docker.
- `make print` — portrait geometry. Implies `final`. Requires Docker.
- `make images` — compile all standalone TikZ images in `build/images/` to PDF. Run: `lualatex --shell-escape --output-directory=build/images build/images/<name>.tex` for each. Output PDFs land next to source files in `build/images/`.
- `make validate` — runs `build/validate.sh`.
- `make clean` — remove all generated files (aux, log, PDF, tikz-cache, gitinfo).
- `make clean-cache` — remove TikZ cache only.
- `make manifest` — auto-generate `build/manifest.json` from filesystem.
- `make size-report` — per-component file size breakdown.
- `make gitinfo` — generate `build/gitinfo.tex` from git metadata (see deliverable 10).

All targets set `SOURCE_DATE_EPOCH` from `git log -1 --pretty=%ct`.

`make dev` depends on `make gitinfo` (auto-run before compilation).

All targets call latexmk with `-r build/.latexmkrc` to locate the config file.

**Directory creation:** The `dev` target must `mkdir -p build/tikz-cache` before calling latexmk (TikZ externalization fails if the prefix directory doesn't exist).

**Conditional compilation flags** are passed via `build/flags.tex`:
```makefile
dev: gitinfo
	@echo "" > build/flags.tex
	@mkdir -p build/tikz-cache
	latexmk -r build/.latexmkrc main.tex

final:
	@command -v docker >/dev/null 2>&1 || { echo "ERROR: Docker required for final builds"; exit 1; }
	@echo "\\def\\FINAL{1}" > build/flags.tex
	# ... run via Docker ...

screen:
	@echo "\\def\\FINAL{1}" > build/flags.tex
	# ... run via Docker (default geometry is screen) ...

print:
	@echo "\\def\\FINAL{1}\\def\\PRINT{1}" > build/flags.tex
	# ... run via Docker ...

clean:
	# ... remove generated files ...
	@echo "" > build/flags.tex   # recreate empty flags so manual lualatex still works
```

`main.tex` loads this file first: `\input{build/flags.tex}` (before any `\ifdefined` checks). The file is gitignored and always regenerated by the Makefile. `make clean` recreates an empty file so `\input{build/flags.tex}` never fails (issue: if deleted, manual `lualatex main.tex` would error).

### 2. `build/.latexmkrc`

```perl
$pdf_mode = 4;                    # LuaLaTeX
$lualatex = 'lualatex --shell-escape %O %S';
# NO $aux_dir, NO $out_dir.
# LuaLaTeX on TeX Live does NOT support --aux-directory natively.
# latexmk emulates it by copying files, which breaks makeglossaries.
# Aux files land in repo root. Use `make clean` to tidy up.
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
sub makeglossaries {
    system("makeglossaries '$_[0]'");
}
```

**Critical:** Do NOT set `$out_dir` or `$aux_dir`. Setting output directory breaks `\include{manuscript/...}` because LaTeX resolves paths relative to it. Setting aux directory fails because LuaLaTeX on TeX Live does not support `--aux-directory` natively — latexmk's emulation is fragile and breaks glossary compilation. Aux files (`.aux`, `.log`, `.toc`, `.glo`, `.gls`) land in repo root alongside `main.pdf`. Use `make clean` to remove them.

### 3. `build/preamble.tex`

This file is `\input{}`'d from `main.tex` AFTER `\documentclass`. It contains all package loading and macro definitions.

**Document class and metadata ordering** (shown in main.tex, deliverable 7):
```latex
% 0. \input{build/flags.tex}  — build flags (generated by Makefile)
% 1. \DocumentMetadata (FINAL builds only — before \documentclass)
% 2. \documentclass{book}
% 3. \input{build/preamble}  — all packages and macros
```

Packages (in load order):
- `geometry` — page dimensions (loaded conditionally via screen.tex or print.tex)
- `fontspec` — LuaLaTeX font handling (NOT fontenc, NOT cmap — those are pdfLaTeX legacy)
- `xcolor` — with `\input{build/palette.tex}`
- `tikz` — with externalization: `\tikzexternalize[prefix=build/tikz-cache/]`
- `graphicx` — image inclusion
- `hyperref` — links, bookmarks, PDF metadata. Configure via:
  ```latex
  \hypersetup{
    pdftitle={Relinquishment: A Triple Spiral},
    pdfauthor={Bruce Stephenson},
    pdfsubject={Topological quantum neural networks, relinquishment, Guardian},
    pdfkeywords={TQNN, Guardian, relinquishment, SFI, DARPA, predictions},
    colorlinks=true,
    linkcolor=linkblue,
    urlcolor=linkblue,
  }
  ```
- `bookmark` — improved PDF bookmarks (load AFTER hyperref, replaces hyperref's bookmark handling)
- `cleveref` — smart cross-references (load AFTER hyperref)
- `glossaries` — glossary/acronym system. **Must call `\makeglossaries` after loading** (before any `\newglossaryentry` commands)
- `ocgx2` — Optional Content Groups for graphics toggle (R19)
- `fancyhdr` — custom headers/footers with track-colored margin stripes
- `eso-pic` — full-page backgrounds (used for cover page)

Conditional flags:
- `\ifdefined\FINAL` → enables tagpdf, PDF/A compliance, full accessibility. **Not active in dev builds.**
- `\ifdefined\PRINT` → inputs `build/print.tex` for portrait geometry
- Otherwise (including dev builds) → inputs `build/screen.tex` for landscape geometry

**Geometry loading logic:**
```latex
\ifdefined\PRINT
  \input{build/print.tex}
\else
  \input{build/screen.tex}  % default: landscape screen layout
\fi
```

This means dev builds (empty `flags.tex`) automatically get landscape screen geometry. Only `make print` defines `\PRINT` to switch to portrait.

**Track margin stripe mechanism** (fancyhdr):
```latex
% Define a command that chapters set to their track color
\newcommand{\currenttrackcolor}{bodytext}  % default: no stripe
\newcommand{\settrack}[1]{\renewcommand{\currenttrackcolor}{#1}}

% fancyhdr: colored stripe on outer margin
\fancypagestyle{trackpage}{%
  \fancyhf{}
  \fancyhead[RO,LE]{\textcolor{\currenttrackcolor}{\rule{4pt}{\headheight}}}
  \fancyfoot[C]{\thepage}
}
\pagestyle{trackpage}

% CRITICAL: Also redefine 'plain' style — book class forces \thispagestyle{plain}
% on chapter-opening pages. Without this, chapter first pages have no stripe.
\fancypagestyle{plain}{%
  \fancyhf{}
  \fancyhead[RO,LE]{\textcolor{\currenttrackcolor}{\rule{4pt}{\headheight}}}
  \fancyfoot[C]{\thepage}
}
```

Each chapter file calls `\settrack{trackone}` (or `tracktwo`, `trackthree`) to activate its color.

**OCG base setup:**
```latex
\usepackage{ocgx2}
% Define the graphics layer
\newcommand{\graphicsonly}[1]{%
  \begin{ocg}[printocg=always,exportocg=always]{Graphics}{graphics}{1}#1\end{ocg}%
}
```

Figures wrapped in `\graphicsonly{...}` can be toggled off in the PDF viewer's layer panel.

**Cross-reference label convention:** `\label{t1:ch01:section-name}`, `\label{t2:ch03:alpha-farm}`, `\label{conv:surrender}`. Track prefix is `t1:`, `t2:`, `t3:`, or `conv:`.

### 4. `build/palette.tex`

Color definitions per table above. Single source of truth. Uses `\definecolor` (not `\providecolor`) — this file is loaded exactly once per compilation.

### 5. `build/screen.tex` + `build/print.tex`

- Screen: `\geometry{landscape, paperwidth=11in, paperheight=8.5in, left=1.5in, right=1.5in, top=1in, bottom=1in}` — letter landscape, generous margins for comfortable reading at fit-width on a laptop.
- Print: `\geometry{letterpaper, left=1.2in, right=0.8in, top=1in, bottom=1in}` — portrait, inner gutter for binding.

### 6. `build/images/standalone-header.tex`

Shared header for all standalone TikZ images:
```latex
\documentclass[tikz,border=2mm]{standalone}
\usepackage{fontspec}
\usepackage{xcolor}
\input{build/palette.tex}
```

Each standalone TikZ file starts with `\input{build/images/standalone-header.tex}` instead of repeating the preamble. **All standalone TikZ compilation happens from repo root:** `lualatex --shell-escape build/images/cover-triskellion.tex`. This ensures `\input{build/palette.tex}` resolves correctly.

### 7. `main.tex` (repo root)

```latex
% Relinquishment — root document
% Dev: uncomment \includeonly{} with specific chapter for fast builds
% \includeonly{manuscript/track-1-confession/ch01}

% --- ORDERING IS CRITICAL ---
% Step 0: Load build flags (generated by Makefile — defines \FINAL, \SCREEN, \PRINT as needed)
\input{build/flags.tex}

% Step 1: \DocumentMetadata (FINAL builds only — MUST come before \documentclass)
\ifdefined\FINAL
  \DocumentMetadata{
    lang = en-US,
    pdfversion = 2.0,
    testphase = {phase-III},
  }
\fi

% Step 2: Document class
\documentclass[11pt]{book}

% Step 3: Preamble (all packages and macros)
\input{build/preamble}

\begin{document}
\frontmatter
% \include{manuscript/00-front/cover}
% \include{manuscript/00-front/title}
% \include{manuscript/00-front/how-to-read}
% \include{manuscript/00-front/preface}
\tableofcontents

\mainmatter
% Chapters will be \include'd here in spiral interleave order

\backmatter
% Appendices will be \include'd here

\end{document}
```

All `\include{}` lines commented out initially (no content yet). **Plan 0002 rewrites the document body** with the full include structure per R22 ordering. This plan just establishes that main.tex compiles.

**Note:** `\DocumentMetadata` is a LaTeX kernel command (TeX Live 2025+). On TeX Live 2022, `build/flags.tex` is empty (dev builds), so `\FINAL` is never defined and the `\ifdefined` block is skipped entirely. No error.

**Note:** `\input{build/flags.tex}` works before `\documentclass` because it's pure TeX — `\input` is a TeX primitive, not a LaTeX command.

### 8. `build/Dockerfile`

Written but **not tested** (Docker not installed on current host).

- Base: `texlive/texlive:TL2025-historic` (pin to TeX Live 2025)
- Install: full scheme (or specific packages: fontspec, tikz, hyperref, cleveref, glossaries, ocgx2, fancyhdr, eso-pic, tagpdf, geometry, graphicx)
- Install: veraPDF for PDF/A validation
- Working dir: `/src`
- Default command: `make final`
- Environment: `LC_ALL=C`, `TZ=UTC`

### 9. `build/validate.sh`

1. Check LaTeX log for unresolved references (`grep -c "undefined" main.log`)
2. Check LaTeX log for warnings (`grep -c "Warning" main.log`)
3. Size audit: `ls -la main.pdf` + `pdfinfo main.pdf` for page count
4. Manifest check: verify `build/manifest.json` matches filesystem
5. Check that `makeglossaries` is installed: `which makeglossaries || echo "WARNING: makeglossaries not found"`
6. Build timing: report wall-clock time
7. Output: human-readable summary to stdout, JSON to `build/validation.json` (**not** in build/output/)

Note: veraPDF and PDF/A validation only run inside Docker (TeX Live 2025 builds). Skip gracefully on host.

### 10. `build/gitinfo.tex`

Generated by `make gitinfo`, NOT hand-written. The Makefile target:

```makefile
gitinfo:
	@echo "\\newcommand{\\GitHash}{$(shell git log -1 --pretty=%H)}" > build/gitinfo.tex
	@echo "\\newcommand{\\GitShortHash}{$(shell git log -1 --pretty=%h)}" >> build/gitinfo.tex
	@echo "\\newcommand{\\GitDate}{$(shell git log -1 --pretty=%ci)}" >> build/gitinfo.tex
	@echo "\\newcommand{\\BuildDate}{$(shell date -u +%Y-%m-%dT%H:%M:%SZ)}" >> build/gitinfo.tex
```

The preamble loads this file: `\input{build/gitinfo.tex}`.
The colophon (plan 0002) uses `\GitHash`, `\GitShortHash`, `\GitDate`, `\BuildDate`.

### 11. Remove `research/` directory

The `research/` directory exists at repo root but is empty (contains only an empty `notes/` subdir) and is not in R0's allowed subdirectory list. Remove it: `rm -rf research/`. Research lives in aurasys-memory, not here.

### 12. `.gitignore` update

Add:
```
# LaTeX aux files (land in repo root — lualatex doesn't support aux-directory)
*.aux
*.log
*.toc
*.out
*.fls
*.fdb_latexmk
*.synctex.gz
*.glo
*.gls
*.glg
*.ist

# Build artifacts
build/tikz-cache/
build/flags.tex
build/gitinfo.tex
build/validation.json
build/images/*.pdf
main.pdf
*.md.archive
```

**Not gitignored** (committed):
- `build/manifest.json` — versioned filesystem record, used by validation pipeline

---

## Acceptance Criteria

1. `make dev` compiles `main.tex` with no errors on host (TeX Live 2022)
2. Output PDF (`main.pdf`) exists in repo root and is valid (opens in a viewer)
3. Makefile has all targets listed above (dev, final, screen, print, images, validate, clean, clean-cache, manifest, size-report, gitinfo)
4. `build/preamble.tex` loads without errors
5. `build/palette.tex` defines all 8 colors
6. Conditional compilation flags work: `\ifdefined\PRINT` / `\ifdefined\FINAL` (FINAL skipped on TeX Live 2022; screen geometry is default)
7. `build/validate.sh` runs and produces output (including makeglossaries check)
8. `.gitignore` updated
9. `make gitinfo` produces `build/gitinfo.tex` with correct git metadata
10. Docker targets print clear "Docker not available" message (deferred)
11. Git commit: `Plan 0001: build infrastructure`

---

## Generator Handoff

> You are the Generator. Read plan 0001 at `~/software/relinquishment/plans/0001-build-infrastructure.md`. Start by running the Prerequisites checks and installing missing packages. Then create all 12 deliverables. Work in `~/software/relinquishment/`. All compilation and `make` commands run from repo root. Compile `make dev` and verify it works. Docker is NOT installed — write the Dockerfile but skip Docker testing. Commit with message `Plan 0001: build infrastructure`. Report completion with build time and any issues.
