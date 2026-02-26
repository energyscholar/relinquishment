# Plan 0048: Comprehensive PDF Navigation System

## Context

Visual red-team scan + automated test suite (15/18 pass) identified three navigation gaps:
1. No prev/next chapter navigation — reader must return to TOC to hop chapters
2. 34 blank pages (14.5%) from print recto-page formatting
3. Portrait orientation instead of screen-optimized landscape

Current strengths (preserve these):
- 60 bookmarks (53 L1, 7 L2), all valid, all in order
- 38 "Return to TOC" links, all functional
- Footer "TOC" shortcut on 100% of content pages
- Track stripe identification (color + rotated label)
- Clean hyperref setup with semantic PDF metadata

## Deliverables

### 1. Deeper Bookmark Sidebar (preamble.tex)

**Current:** `\bookmarksetup{depth=1, open=false}` — chapters only in sidebar.

**Change to:** `\bookmarksetup{depth=2, open, openlevel=1}`

This gives:
- L1: All chapters (visible, expandable)
- L2: All `\section{}` entries within chapters (visible when chapter expanded)
- Bookmark panel auto-opens when PDF is opened
- L1 entries start expanded (openlevel=1) so reader sees section structure immediately

### 2. Prev/Next Chapter Navigation Footer (preamble.tex)

Add a new macro `\chapternav` that provides prev/next chapter links at chapter boundaries.

**Implementation:** Use LaTeX counters. Define chapter labels in sequence, then create prev/next hyperlinks.

```latex
% --- Chapter navigation (prev/next) ---
\newcounter{chaporder}
\newcommand{\setchapnav}[1]{%
  \stepcounter{chaporder}%
  \label{chapnav:\thechaporder}%
  \edef\@currentchapnum{\thechaporder}%
}

% At chapter end, before \chapterreturn:
\ifdefined\PRINT
  \newcommand{\chapnavlinks}{}%
\else
  \newcommand{\chapnavlinks}{%
    \par\vspace{0.5cm}
    \begin{center}
    \small
    \ifnum\value{chaporder}>1
      \hyperref[chapnav:\the\numexpr\value{chaporder}-1\relax]{%
        \textcolor{linkblue}{$\triangleleft$\enspace Previous Chapter}}%
      \hspace{2em}%
    \fi
    \hyperref[toc]{\textcolor{linkblue}{Contents}}%
    \hspace{2em}%
    \hyperref[chapnav:\the\numexpr\value{chaporder}+1\relax]{%
      \textcolor{linkblue}{Next Chapter\enspace$\triangleright$}}%
    \end{center}
  }%
\fi
```

**ALTERNATIVE (simpler):** Since chapter ordering is fixed in main.tex, define a simpler approach. Replace `\chapterreturn` with a navigation bar:

```latex
\newcommand{\chapterreturn}{%
  \par\vfill
  \begin{center}
    \small
    \hyperref[toc]{\textcolor{linkblue}{$\triangleleft$\enspace Return to Table of Contents\enspace$\triangleright$}}
  \end{center}
}
```

**RECOMMENDED APPROACH:** Keep `\chapterreturn` as-is (it works). Add a separate `\chapternav` macro that goes ABOVE it, providing prev/next. This avoids modifying all 38 chapter files — instead, redefine `\chapterreturn` to include both nav bar and TOC return:

```latex
\renewcommand{\chapterreturn}{%
  \par\vfill
  \begin{center}
    \small
    \hyperref[toc]{\textcolor{linkblue}{$\triangleleft$\enspace Table of Contents\enspace$\triangleright$}}
  \end{center}
}
```

**SIMPLEST APPROACH (recommended):** Don't add prev/next. The bookmark sidebar with depth=2 + footer TOC link + chapter-end TOC return provides sufficient navigation. Prev/next requires maintaining chapter order in macros, which is fragile. The bookmark sidebar IS the prev/next — the reader clicks the next entry.

**Decision for Bruce:** Do you want prev/next links, or is deeper bookmarks + existing nav sufficient?

### 3. Screen Geometry Build (Makefile)

**Current build produces portrait PDF.** Switch to screen build:

```bash
make screen    # Uses \FINAL + screen.tex (landscape 11x8.5in)
```

This eliminates:
- Portrait orientation → landscape
- Print binding gutter → symmetric 1.5in margins
- (Partially) blank recto pages — though `\cleardoublepage` still fires

### 4. Eliminate Blank Pages for Screen (preamble.tex)

**Root cause:** LaTeX's `book` class uses `\cleardoublepage` before each `\chapter`, forcing chapters to start on odd (recto) pages. This creates blank verso pages.

**Fix:** Add to preamble (screen mode only):
```latex
\ifdefined\PRINT\else
  % Screen mode: chapters can start on any page
  \let\cleardoublepage\clearpage
\fi
```

This eliminates ~34 blank pages, reducing the PDF from 235 to ~201 pages.

### 5. TOC Section Entries (preamble.tex)

**Current:** TOC shows only chapters (no `\setcounter{tocdepth}{...}` override).

**Add:**
```latex
\ifdefined\PRINT
  \setcounter{tocdepth}{0}  % Print: chapters only
\else
  \setcounter{tocdepth}{1}  % Screen: chapters + sections
\fi
```

This makes the TOC show section titles within each chapter, giving the reader a richer map.

### 6. Bookmark Panel Default Open

**Change:** `\bookmarksetup{depth=2, open, openlevel=1}` already handles this.

**Additionally for screen builds**, set PDF viewer to open with bookmarks panel:
```latex
\ifdefined\PRINT\else
  \hypersetup{
    pdfpagemode=UseOutlines,  % Open with bookmark panel visible
    pdfstartview=FitH,        % Fit page width to window
  }
\fi
```

## Implementation Order

1. preamble.tex: bookmark depth + open + openlevel (line 57)
2. preamble.tex: pdfpagemode + pdfstartview (add after hypersetup, line 55)
3. preamble.tex: `\let\cleardoublepage\clearpage` for screen (add after geometry, ~line 11)
4. preamble.tex: tocdepth for screen (add after tocloft, ~line 38)
5. Build with `make screen`
6. Run `python3 tests/test_pdf_navigation.py` — expect 18/18 pass

## Files Modified

- `build/preamble.tex` — 4 small edits (bookmark depth, hypersetup, cleardoublepage, tocdepth)
- No chapter files modified
- No main.tex modified

## Verification

1. [ ] `python3 tests/test_pdf_navigation.py` — 18/18 pass
2. [ ] Bookmark sidebar shows sections within chapters
3. [ ] Bookmark panel opens by default
4. [ ] No blank pages between chapters (screen build)
5. [ ] Landscape orientation (screen build)
6. [ ] TOC shows section entries
7. [ ] Track stripes still render correctly
8. [ ] "Return to TOC" still works
9. [ ] Page count reduced by ~34 pages
10. [ ] PDF file size comparable (~750KB)

## Red Team Notes

- **Prev/next deferred:** Bookmark sidebar provides equivalent navigation with zero fragility. If Bruce wants it later, Plan 0049.
- **Print build unaffected:** All changes conditional on `\ifdefined\PRINT`. Print PDF identical to current.
- **Section TOC entries may be long:** Some chapters have 5-8 sections. TOC may grow by 1-2 pages. Net reduction still positive (~30 pages).
- **`\cleardoublepage` override:** This removes ALL blank pages, including intentional ones (e.g., before Part divisions). If any blank pages are intentional, they need explicit `\newpage\mbox{}\newpage`.

## Generator Handoff

You are the Generator. Read plan `plans/0048-comprehensive-pdf-navigation.md`.

Task: Make 4 edits to `build/preamble.tex` as specified. Build with `make screen` (or `make dev` if Docker not available). Run test suite: `python3 tests/test_pdf_navigation.py`. Report results.
