# Plan 0223 — Make Design Principles Visible

**Status:** READY
**Author:** Auditor
**Priority:** Low
**EV:** Stable — T5 (silence gap) slightly improved: the single-file constraint itself demonstrates the gap (no institution, no publisher, just physics in a file). F-crank slightly reduced: explicit design rationale signals engineering discipline, not amateur sprawl. No F-mode triggers.
**Scope:** `manuscript/99-back/colophon.tex`, `manuscript/track-2-testament/pos34b-the-engine.tex`

## Rationale

The book's format is a deliberate engineering choice, not a limitation. Single self-contained file. Under 1 MB. SVG-only images (embedded, no external dependencies). Phone-readable. Accessible HTML and PDF from the same source. High signal:noise ratio. High signal:bulk ratio. These choices serve the book's mission — maximum reach, minimum friction, no institutional gatekeeping — but they're invisible to the reader. Making them visible turns a constraint into a statement.

## Changes

### 1. `manuscript/99-back/colophon.tex` — Add "Design Principles" section

After the existing "For researchers" subsection and before the Grace Hopper quote, add a new subsection:

```latex
\subsection*{Design Principles}

This book is a single self-contained file. The entire work --- science,
narrative, illustrations, interactive navigation, glossary, citations ---
ships as one HTML document under one megabyte, or as one PDF. No external
dependencies. No images to fail to load. No server to go down. No paywall.
No app.

This is deliberate. The design targets:

\begin{description}
  \item[Signal\,:\,noise.] Every paragraph either advances a takeaway or
    blocks a failure mode. Content that does neither is cut.
  \item[Signal\,:\,bulk.] A 200-page evidence appendix behind a 4,000-word
    summary. Read the summary. Skip the appendix unless you are curious for
    details.
  \item[Portability.] Readable on a phone, a laptop, or printed on paper.
    No special software. No login. The file is the book.
  \item[Survivability.] A single file can be copied, emailed, torrented,
    archived, and cached. It does not depend on any service continuing to
    exist.
  \item[Accessibility.] Semantic HTML. Screen-reader compatible. All
    illustrations are inline SVG with title attributes. No raster images.
\end{description}

These constraints are features, not limitations. If you are reading this on
a device that can display a web page, you have everything you need.
```

### 2. `manuscript/track-2-testament/pos34b-the-engine.tex` — Add brief design philosophy note

Find an appropriate location in the Engine chapter — after the methodology section where Bruce describes building Argus and the book — and add 2-3 sentences connecting the single-file format to the book's purpose. This should feel like Bruce explaining a choice, not a spec sheet. Something in the spirit of:

*The book is a single file. This was not a limitation we worked around — it was a requirement we designed toward. A preparation document that depends on a server, an app, or a publisher's continued goodwill is not a preparation document. It is a hostage.*

The exact prose and insertion point are for the Generator to determine based on reading the chapter's flow. The key constraint: it must feel natural in Bruce's voice, not bolted on. If no clean insertion point exists, skip this change — the colophon alone is sufficient.

### 3. No build system changes

The design principles are prose content. No `preprocess.py` modifications. No new SVG injection. No HTML-only content — this goes in the LaTeX source so it appears in both PDF and HTML.

## What is NOT changed

- Build system — no modifications
- Other chapters — untouched
- HTML-specific features (tooltips, navigation) — unchanged

## Acceptance Tests

1. **Colophon updated:** `grep -c 'Design Principles' manuscript/99-back/colophon.tex` returns ≥1
2. **Signal:noise mentioned:** The colophon contains "Signal" and "noise" in proximity
3. **Signal:bulk mentioned:** The colophon contains "Signal" and "bulk" in proximity
4. **Single file stated:** The colophon contains "single self-contained file" or equivalent
5. **SVG-only stated:** The colophon mentions SVG and no raster images
6. **Build succeeds:** `make` exits 0 (both PDF and HTML)
7. **Engine integration (if attempted):** The added text reads naturally in Bruce's voice — no spec-sheet register, no bullet points
8. **No build system changes:** `git diff build/` shows no modifications
