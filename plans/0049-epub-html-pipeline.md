# Plan 0049: EPUB/HTML Primary Distribution Pipeline

## Context

Bruce's decision: EPUB as primary format, PDF as afterthought. Priority: widest access, easiest use, fully open, accessible to all. Most readers will be on phones.

The book is 38 chapter files + 8 appendices + 8 front/back matter files. 216 custom macro instances across 38 files. 33 inline math expressions. 4 TikZ-generated images.

## Red Team Findings (incorporated)

Testing pandoc directly on `main.tex` with all 60 `\input`/`\include` files produced a working 252KB EPUB (55 chapter files) and 8,203-line HTML. Pandoc's native LaTeX reader handles:
- `\include`/`\input` file following
- `\newcommand` expansion (including `\DMSRedacted`, `\srcnote`)
- Tables (including `p{6cm}` column specs), lists, quotes
- `\textit`, `\textbf`, `\href`, `\hyperref`, `\label`, `\footnote`
- TeX quotes → Unicode, em dashes → Unicode
- Inline math → MathML (EPUB) / `<span class="math inline">` (HTML)

**What pandoc CANNOT handle (preprocessor scope):**

| Issue | Why | Fix |
|-------|-----|-----|
| `\dag` silently dropped | Pandoc produces empty `<sup></sup>` — kills all 142 AI-draft markers | Replace `\dag` with Unicode † (U+2020) before pandoc |
| `\graphicsonly{}` OCG wrapper | OCG parameters leak as visible text | Strip wrapper, keep inner content |
| `\settrack{name}` | pgfkeys silently ignored — track identity completely lost | Convert to pandoc raw HTML div |
| Cover image is PDF | PDF embeds don't render in EPUB readers | Convert to SVG/PNG before pandoc |
| `\hfill` in quote attributions | Silently dropped — attributions lose right-alignment | Wrap in CSS class |

That's 5 targeted fixes, not a 200-line general-purpose preprocessor.

## Architecture (Revised)

```
LaTeX source (canonical)
    │
    ├──► preprocess.py (5 targeted fixes, ~60 lines)
    │       │
    │       └──► pandoc main.tex ──► EPUB 3 / HTML / Markdown
    │
    └──► latexmk ──► PDF (print/legacy)
```

Pandoc reads `main.tex` directly and follows all `\include`/`\input` chains. The preprocessor only patches the 5 known issues — it does NOT concatenate files, expand includes, or strip standard LaTeX commands. Pandoc does all of that.

## Preprocessor: What It Does (build/preprocess.py)

The preprocessor creates a temporary copy of the manuscript with 5 targeted substitutions, then invokes pandoc on the patched copy. Intermediate files written to `build/epub-tmp/` for inspection.

### Fix 1: Dagger symbol (142 instances)
In `build/preamble.tex` (temp copy), redefine:
```latex
\newcommand{\aidraftmark}{†\,}
```
This replaces `{\textsuperscript{\dag}}` with the Unicode literal. Pandoc will pass it through.

### Fix 2: OCG wrapper (1 instance, cover.tex)
Strip `\graphicsonly{...}` → keep inner content. Simple regex safe here (single usage, no nesting).

### Fix 3: Track identity (37 instances)
Convert `\settrack{trackone}` to pandoc raw block:
```latex
\begin{rawhtml}<div class="track track-trackone">\end{rawhtml}
```
Close previous track div when a new `\settrack` appears, and at document end.

Actually simpler: redefine `\settrack` in the patched preamble to emit a section-break comment that a post-processor can use. Or: since track identity is purely visual (colored borders), and EPUB readers may strip the CSS anyway, consider adding a plain-text track label before each chapter instead:
```
CONFESSION
```
This degrades to readable on any device.

**Decision for Generator:** Implement the CSS border approach. If it doesn't render, Phase 2 adds text labels as fallback.

### Fix 4: Cover image
Convert `build/images/cover-triskellion.pdf` → `.svg` (via pdf2svg) or `.png` (via pdftoppm). Reference SVG in `--epub-cover-image`.

### Fix 5: Quote attributions
Redefine `\hfill` to emit nothing (already pandoc's behavior). Add CSS class for `blockquote footer` to right-align. This is CSS-only — no preprocessing needed.

**Revised: preprocessor handles fixes 1-4 only. Fix 5 is CSS.**

## Preprocessor Design

```python
#!/usr/bin/env python3
"""Patch manuscript for pandoc EPUB/HTML conversion."""

import shutil, re, subprocess, sys, tempfile
from pathlib import Path

REPO = Path(__file__).parent.parent
TMP = REPO / "build" / "epub-tmp"

def patch():
    # Create temp copy of manuscript tree
    if TMP.exists():
        shutil.rmtree(TMP)
    # Copy only .tex files and images (not .pdf output)
    for src in REPO.glob("**/*.tex"):
        if "epub-tmp" in str(src):
            continue
        dst = TMP / src.relative_to(REPO)
        dst.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text()

        # Fix 1: Replace \dag with Unicode †
        text = text.replace(r"{\textsuperscript{\dag}}", "†\\,")
        text = text.replace(r"\textsuperscript{\dag}", "†")

        # Fix 2: Strip \graphicsonly wrapper
        text = re.sub(
            r"\\graphicsonly\{%?\s*\n?(.*?)\n?\}",
            r"\1", text, flags=re.DOTALL
        )

        # Fix 3: Convert \settrack to raw HTML div
        # (pandoc passes raw HTML through with appropriate extension)
        track_map = {
            "trackone": "confession",
            "tracktwo": "testament",
            "trackthree": "awakening",
            "trackconv": "convergence",
            "trackbridge": "bridge",
        }
        for latex_name, html_name in track_map.items():
            text = text.replace(
                f"\\settrack{{{latex_name}}}",
                f"% track: {html_name}"
            )

        # Fix 4: Convert cover PDF reference to SVG
        text = text.replace(
            "build/images/cover-triskellion.pdf",
            "build/images/cover-triskellion.svg"
        )

        dst.write_text(text)

    # Copy images
    img_src = REPO / "build" / "images"
    img_dst = TMP / "build" / "images"
    img_dst.mkdir(parents=True, exist_ok=True)
    for f in img_src.iterdir():
        shutil.copy2(f, img_dst / f.name)

    return TMP / "main.tex"
```

~60 lines. No brace-counting parser needed — pandoc handles all the nested macro expansion.

## EPUB Metadata (build/metadata.yaml)

```yaml
---
title: "Relinquishment: It is easier to get forgiveness than permission"
author:
  - name: Bruce Stephenson
  - name: Genevieve Prentice
  - name: Argus
language: en
rights: "CC BY-ND 4.0 International"
date: 2026-02
publisher: Self-published
description: >
  Three narrative threads. Real science. Real people. Real institutions.
  Three possible explanations for all of it. You decide.
---
```

## CSS Design (build/epub.css)

```css
/* Track indicators — subtle left border */
.track-confession { border-left: 4px solid #1A6B6A; padding-left: 1em; }
.track-testament { border-left: 4px solid #C4913B; padding-left: 1em; }
.track-awakening { border-left: 4px solid #6B3FA0; padding-left: 1em; }
.track-convergence { border-left: 4px solid #8C7853; padding-left: 1em; }
.track-bridge { border-left: 4px solid #808080; padding-left: 1em; }

/* Scene breaks */
hr { width: 50%; margin: 2em auto; border: none; border-top: 1px solid #666; }

/* Redacted content */
blockquote.redacted { font-style: italic; border-left: 3px solid #999; padding-left: 1em; }

/* Block quote attributions */
blockquote p:last-child { text-align: right; font-size: 0.9em; }

/* Responsive body */
body {
  max-width: 40em; margin: 0 auto; padding: 1em;
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.6; color: #1a1a1a;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  body { background: #1a1a1a; color: #e0e0e0; }
  a { color: #6ba3f7; }
  .track-confession { border-left-color: #2a9b9a; }
  .track-testament { border-left-color: #d4a14b; }
  .track-awakening { border-left-color: #8b5fc0; }
  .track-convergence { border-left-color: #ac9873; }
  .track-bridge { border-left-color: #a0a0a0; }
}
```

## HTML-Specific CSS (build/html.css)

```css
/* Responsive phone layout */
@media (max-width: 600px) {
  body { padding: 0.5em; font-size: 16px; }
}

/* Sticky TOC nav */
nav#TOC {
  position: sticky; top: 0; background: white;
  padding: 0.5em; border-bottom: 1px solid #ccc;
  max-height: 50vh; overflow-y: auto;
}
@media (prefers-color-scheme: dark) {
  nav#TOC { background: #1a1a1a; border-bottom-color: #444; }
}
```

## Inline Math

Let pandoc handle it. Do NOT pre-convert to Unicode.
- EPUB: pandoc emits MathML (EPUB 3 standard)
- HTML: use `--mathjax` flag for complex expressions
- 33 expressions total, most simple (`$\nu=5/2$`, `$10^{-6}$`)

## TikZ Image Conversion

```bash
# If pdf2svg available:
pdf2svg build/images/cover-triskellion.pdf build/images/cover-triskellion.svg
# Fallback (Inkscape):
inkscape build/images/cover-triskellion.pdf --export-type=svg
# Fallback (pdftoppm for PNG):
pdftoppm -png -r 300 build/images/cover-triskellion.pdf build/images/cover-triskellion
```

Only cover-triskellion matters for EPUB. The 3 placeholder images are TODO content.

## Build Targets (Makefile additions)

```makefile
# --- EPUB (primary distribution) ---
epub: gitinfo
	python3 build/preprocess.py
	pandoc build/epub-tmp/main.tex \
		-f latex -t epub3 \
		--top-level-division=chapter \
		--toc --toc-depth=1 \
		--epub-cover-image=build/images/cover-triskellion.svg \
		--css=build/epub.css \
		--metadata-file=build/metadata.yaml \
		-o $(JOBNAME).epub

# --- Single HTML (universal fallback) ---
html: gitinfo
	python3 build/preprocess.py
	pandoc build/epub-tmp/main.tex \
		-f latex -t html5 \
		--standalone --embed-resources \
		--top-level-division=chapter \
		--toc --toc-depth=2 \
		--mathjax \
		--css=build/epub.css --css=build/html.css \
		--metadata-file=build/metadata.yaml \
		-o $(JOBNAME).html

# --- Markdown (archival) ---
markdown: gitinfo
	python3 build/preprocess.py
	pandoc build/epub-tmp/main.tex \
		-f latex -t gfm \
		--top-level-division=chapter \
		--toc --toc-depth=2 \
		-o $(JOBNAME).md
```

Note: preprocessor writes to `build/epub-tmp/`, pandoc reads from there. Intermediate result inspectable.

## Implementation Order

### Phase 1 (this plan)
1. Install pandoc (`sudo apt install pandoc`) and pdf2svg
2. Convert cover-triskellion.pdf → .svg
3. Write `build/preprocess.py` (~60 lines, 4 fixes)
4. Write `build/metadata.yaml`
5. Write `build/epub.css` and `build/html.css`
6. Add Makefile targets
7. Run `make epub` → verify EPUB structure
8. Run `make html` → verify responsive layout
9. Run `epubcheck` if available (or install: `sudo apt install epubcheck`)

### Phase 2 (separate plan)
- Proper EPUB cover (title text baked into image)
- Track label text fallback for CSS-stripping readers
- `epubcheck` validation in CI
- Test across: Apple Books, Google Play Books, Kindle, Kobo, Firefox Reader View
- Accessibility: ARIA landmarks, alt text, reading order metadata
- GitHub Pages hosting for HTML version
- Phone PDF target (narrow geometry, larger font)

## Files Created/Modified

**New files:**
- `build/preprocess.py` — targeted patcher (~60 lines)
- `build/metadata.yaml` — EPUB/HTML metadata
- `build/epub.css` — shared responsive styles
- `build/html.css` — HTML-specific styles
- `build/images/cover-triskellion.svg` — converted cover

**Modified files:**
- `Makefile` — add epub, html, markdown targets
- `.gitignore` — add build/epub-tmp/

**No manuscript files modified.** LaTeX remains canonical.

## Verification

1. [ ] `make epub` produces EPUB file
2. [ ] EPUB opens in reader app (or `epubcheck` passes)
3. [ ] All 55+ chapters present in EPUB TOC
4. [ ] Dagger marks (†) visible on AI-drafted sections
5. [ ] Tables render (dual-use tech, predictions)
6. [ ] Inline math readable
7. [ ] Block quotes render with attributions
8. [ ] Redacted sections render as styled blockquotes
9. [ ] Footnotes present (3 total, in pos22)
10. [ ] External URLs clickable (16 total)
11. [ ] Cover image renders
12. [ ] Metadata correct (title, 3 authors, CC BY-ND, language)
13. [ ] `make html` produces self-contained file
14. [ ] HTML responsive at 375px (phone) — no horizontal scroll
15. [ ] HTML dark mode works
16. [ ] No LaTeX artifacts in output (no backslashes, no `\textit`, no `\begin`)
17. [ ] `make markdown` produces clean GFM
18. [ ] `build/epub-tmp/` is inspectable intermediate output

## Generator Handoff

You are the Generator. Read plan `plans/0049-epub-html-pipeline.md`.

Phase 1 only. Implementation order:
1. Install pandoc and pdf2svg (sudo apt install)
2. Convert cover-triskellion.pdf to SVG
3. Write build/preprocess.py (the 4-fix patcher, ~60 lines)
4. Write build/metadata.yaml
5. Write build/epub.css and build/html.css
6. Add epub/html/markdown targets to Makefile
7. Add build/epub-tmp/ to .gitignore
8. Run `make epub` and `make html`
9. Report: file sizes, chapter count in EPUB, any conversion warnings, spot-check dagger marks and tables
