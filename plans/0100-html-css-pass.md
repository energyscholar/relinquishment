# Plan 0100: HTML CSS & Appearance Pass

## Origin

S46 20% audit. Agent explored full CSS coverage, pandoc output structure, reader.js
nav. Findings: ~30% of pandoc-generated elements have custom styling. Major gaps:
headings, code, footnotes, tables, blockquotes, `.center` divs. Code renders in
*serif* (broken). Footnotes have zero visual separation. Tables have no borders.

## Scope

Stylesheet-only changes in `build/html.css`. No LaTeX, no preprocess.py, no
reader.js rewrite. Goal: every visible element in the HTML output looks intentional.
Best practices reference: Butterick's Practical Typography, Tufte CSS.

## Phases

### Phase 1: Fix What's Broken (~30 min)

1. **`.center` class** — `text-align: center` (missing entirely; 14 instances broken)
2. **Inline code** — monospace font, subtle background, slight padding
3. **Code blocks** — monospace, background, padding, overflow-x scroll, border-radius
4. **Dark mode** for code (background + text colors)

### Phase 2: Heading Hierarchy (~20 min)

1. **h1** (chapter titles) — size, weight, margin-top/bottom, letter-spacing
2. **h2** (sections within chapters) — smaller than h1, adequate spacing
3. **h3** (subsections) — smaller still, distinct from body
4. **h4** (rare) — bold body-size
5. Dark mode heading colors (slightly lighter than body text)

### Phase 3: Blockquotes & Footnotes (~30 min)

1. **Blockquotes** — left border (3px #ccc), padding-left, slight background tint,
   reduced font-size (0.95em), italic option. Attribution line right-aligned (already
   partial). Dark mode variants.
2. **Footnotes section** — top border separator, smaller font (0.85em), tighter
   line-height, backlink styling, item spacing. Dark mode.

### Phase 4: Tables & Lists (~20 min)

1. **Tables** — cell padding, thead bottom-border, tbody row borders (light),
   optional alternating row background, responsive overflow wrapper
2. **Lists** — consistent margin/padding, nested list indentation
3. Dark mode for both

### Phase 5: Reader Nav Polish (~20 min)

1. **Focus/hover states** on nav buttons (background highlight, outline)
2. **TOC toggle** — smoother visual state (open vs closed)
3. **Mobile** — reduce nav bar height on small screens, ensure no viewport overflow
4. **Progress bar** — ensure readable in both modes

### Phase 6: Responsive & Polish (~15 min)

1. **Tablet breakpoint** (768px) — slightly smaller body text, adjusted margins
2. **Table overflow** — horizontal scroll on mobile for wide tables
3. **Code block overflow** — horizontal scroll on mobile
4. **`prefers-reduced-motion`** — disable smooth scroll

## Constraints

- All changes in `html.css` only (plus dark mode variants for each rule)
- No changes to LaTeX source, preprocess.py, or reader.js logic
- Must not break EPUB (epub.css is separate; html.css is HTML-only)
- Test: `make html` then visual check in browser (light + dark mode)
- Preserve existing track-colored borders, TOC styling, title block

## Acceptance Criteria

1. `make html` builds clean
2. Every pandoc-generated element type has explicit CSS (no browser defaults visible)
3. Dark mode parity for all new rules
4. Code renders in monospace with visible background
5. Footnotes visually separated from body text
6. Tables have borders and padding
7. Heading hierarchy visually distinct (h1 > h2 > h3 > h4)
8. `.center` class works
9. No horizontal overflow on mobile (320px viewport)

## Estimated Total: ~2.5 hours
