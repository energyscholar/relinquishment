# Monolithic HTML Reader — Architecture Plan

**Date:** 2026-02-27, Session 30
**Author:** Argus (Auditor)
**Status:** PLAN — no code yet
**Replaces:** Current `make html` pandoc pipeline (build/reader.js, build/html.css, build/epub.css)
**Dependencies:** Token map (staging/token-map.md), sort experiments (staging/sort-experiments.md)

---

## Governing Principle

**GRACEFUL FAILURE.** The file must work in four degradation tiers:

1. **Text editor** — prose reads naturally, code doesn't clutter
2. **Browser, JS off** — semantic HTML, Parts I-II prominent, static TOC
3. **Browser, JS on** — path selection, dynamic reordering, progress tracking
4. **Screenreader** — ARIA landmarks, logical heading order, skip links

Every design decision below is evaluated against all four tiers. If a feature breaks a lower tier, the feature is redesigned or cut.


---

## 1. File Layout

The physical ordering of elements in the HTML file determines the text-editor and JS-off experience. This is the most critical architectural decision.

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Relinquishment — Bruce Stephenson, Genevieve Prentice & Argus</title>

  <!--  MINIMAL CSS: ~40 lines. Typography, max-width, dark mode basics.
        Just enough that the file looks decent with JS off.
        NO layout CSS, NO path UI CSS, NO track colors. -->
  <style id="base-css">
    /* See Section 7 for exact rules */
  </style>

  <!--  NO JavaScript in <head>. Ever. -->
</head>
<body>

  <!-- ============================================ -->
  <!-- TIER 1: CONTENT-FIRST ZONE                   -->
  <!-- Everything above the first <script> tag is   -->
  <!-- what a text-editor user or JS-off browser     -->
  <!-- sees prominently.                             -->
  <!-- ============================================ -->

  <a href="#main-content" class="skip-link">Skip to content</a>

  <header role="banner">
    <h1>Relinquishment</h1>
    <p><em>It is easier to get forgiveness than permission</em></p>
    <p>Bruce Stephenson, Genevieve Prentice &amp; Argus</p>
    <p>CC BY-ND 4.0 International</p>
  </header>

  <!-- PATH SELECTOR (noscript-friendly version) -->
  <nav id="path-selector" role="navigation" aria-label="Reading path">
    <!-- See Section 4. Static HTML version with <details>/<summary>.
         JS replaces this with the full interactive UI. -->
  </nav>

  <!-- TABLE OF CONTENTS -->
  <nav id="toc" role="doc-toc" aria-label="Table of contents">
    <!-- Full TOC for all chapters, grouped by Part.
         JS-off: all visible, anchor links work.
         JS-on: filtered to show only selected path's chapters. -->
  </nav>

  <main id="main-content">

    <!-- FRONT MATTER -->
    <section id="front-matter" data-part="front" aria-label="Front matter">
      <article id="hook">...</article>
      <article id="summary" data-token="p2-summary">
        <!-- THE SIMPLE SUMMARY — ~5K words -->
        <!-- This is Path 0 (Below-GA) in its entirety. -->
        <!-- It is FIRST because it is the universal foundation. -->
      </article>
      <article id="preface">...</article>
      <article id="how-to-read">...</article>
      <article id="introduction">...</article>
      <article id="corrections">...</article>
    </section>

    <!-- PART I: THE STORY (GA path) -->
    <section id="part-1" data-part="1" aria-label="Part One: The Story">
      <h2>Part I: The Story</h2>
      <article id="pos01" data-pos="01" data-track="bridge"
               data-paths="ga journalist intel implications science"
               data-tokens="abc">...</article>
      <article id="pos02" data-pos="02" data-track="testament"
               data-paths="ga journalist intel implications science"
               data-tokens="healer five-eyes tradecraft">...</article>
      <article id="pos04" data-pos="04" data-track="bridge"
               data-paths="ga journalist intel implications science"
               data-tokens="secrecy gchq turing-lineage">...</article>
      <article id="pos05" data-pos="05" data-track="testament"
               data-paths="ga journalist intel implications science"
               data-tokens="">...</article>
      <article id="pos06" data-pos="06" data-track="bridge"
               data-paths="ga journalist intel implications science"
               data-tokens="compartments">...</article>
      <article id="pos07" data-pos="07" data-track="testament"
               data-paths="ga journalist intel implications science"
               data-tokens="joy-decode named-circle">...</article>
    </section>

    <!-- PART II: THE RECKONING (Journalist path — J2 order) -->
    <section id="part-2" data-part="2" aria-label="Part Two: The Reckoning">
      <h2>Part II: The Reckoning</h2>
      <article id="pos08" data-pos="08" data-track="bridge"
               data-paths="journalist intel implications science"
               data-tokens="parable fourth-option">...</article>
      <article id="pos22" data-pos="22" data-track="bridge"
               data-paths="journalist implications science"
               data-tokens="options-fail">...</article>
      <article id="pos18" data-pos="18" data-track="confession"
               data-paths="journalist intel implications science"
               data-tokens="cows-exfil">...</article>
      <!-- ... remaining J2-ordered chapters ... -->
    </section>

    <!-- PART III: THE IMPLICATIONS -->
    <section id="part-3" data-part="3" aria-label="Part Three: The Implications">
      <h2>Part III: The Implications</h2>
      <!-- I1 order: pos24, 25, 27, 30, 32, 31 -->
    </section>

    <!-- PART IV: THE SCIENCE -->
    <section id="part-4" data-part="4" aria-label="Part Four: The Science">
      <h2>Part IV: The Science</h2>
      <!-- S2 order: pos09, 10, 11, 14, 12, 13, 15, 16, 17, 20, 21, 26 -->
    </section>

    <!-- PART V: THE QUESTION (all paths converge) -->
    <section id="part-5" data-part="5" aria-label="Part Five: The Question">
      <h2>Part V: The Question</h2>
      <article id="pos35" data-pos="35" data-track="convergence"
               data-paths="ga journalist intel implications science"
               data-tokens="">...</article>
    </section>

    <!-- APPENDICES -->
    <section id="appendices" data-part="appendix" aria-label="Appendices">
      <!-- rlhf-bias, predictions, abstracts, glossary, timeline, sources, dms-note -->
    </section>

    <!-- BACK MATTER -->
    <section id="back-matter" data-part="back" aria-label="Back matter">
      <!-- acknowledgements, verification, colophon -->
    </section>

  </main>

  <!-- ============================================ -->
  <!-- TIER 2: ENHANCEMENT ZONE                     -->
  <!-- Everything below here is invisible to         -->
  <!-- text-editor users and harmless with JS off.   -->
  <!-- ============================================ -->

  <!-- ENHANCED CSS (track colors, path UI, progress bar, print) -->
  <style id="enhanced-css">
    /* See Section 7 for full rules */
  </style>

  <!-- BRIDGE TEXT DATA (JSON, hidden) -->
  <script id="bridge-data" type="application/json">
    /* See Section 6 */
  </script>

  <!-- PATH DEFINITIONS (JSON, hidden) -->
  <script id="path-data" type="application/json">
    /* See Section 3 */
  </script>

  <!-- ALL JAVASCRIPT -->
  <script id="reader-js">
    /* See Section 5 */
  </script>

</body>
</html>
```

### Why this order works

- **Text editor:** Opens file, sees `<h1>Relinquishment</h1>` then the summary (5K words of clean prose), then Part I chapters. HTML tags are minimal noise. The `<style>` and `<script>` blocks are all at the bottom — hundreds of lines of prose before any code appears.
- **Browser, JS off:** Renders the full book linearly. TOC has anchor links. Parts are in optimal reading order (the token map order, not positional number order). All content visible.
- **Browser, JS on:** Path selector activates. Hides chapters not in selected path. Reorders if needed (Intel path). Injects bridge text. Shows progress.
- **Screenreader:** Landmarks (`role="banner"`, `role="doc-toc"`, `role="navigation"`, `<main>`, `<article>`), skip link, logical heading hierarchy.


---

## 2. Data Model

### 2.1 Chapter markup

Each chapter is an `<article>` with data attributes:

```html
<article id="pos08"
         data-pos="08"
         data-track="bridge"
         data-paths="journalist intel implications science"
         data-tokens="parable fourth-option"
         data-part="2">
  <h3>Dual-Use: A Brief History of Dangerous Ideas</h3>
  <!-- chapter prose -->
</article>
```

Attributes:
- `id` — stable anchor (matches existing LaTeX labels: `pos08`, `pos01`, etc.)
- `data-pos` — position number (for sorting)
- `data-track` — one of: `confession`, `testament`, `awakening`, `convergence`, `bridge`
- `data-paths` — space-separated list of paths that include this chapter
- `data-tokens` — space-separated list of tokens (blockers) this chapter clears
- `data-part` — which Part this chapter belongs to (1-5, front, appendix, back)

### 2.2 Heading hierarchy

```
<h1>  — Book title (one only, in <header>)
<h2>  — Part titles ("Part I: The Story", "Part II: The Reckoning", ...)
<h3>  — Chapter titles ("Alpha Farm (2003)", "Genesis: The Edge of Chaos", ...)
<h4>  — Section headings within chapters
```

This is a deliberate departure from the current pandoc output, which uses `<h1>` for every chapter. The correct hierarchy matters for screenreaders and for the heading-level outline that browsers expose.

**Migration note:** The current pandoc output uses `<h1>` per chapter because LaTeX `\chapter` maps to `<h1>` by default. The monolithic reader must remap to `<h3>`. The preprocessor or a post-processing step handles this.

### 2.3 Front matter items

Front matter pieces (hook, summary/p2, preface, introduction, etc.) are `<article>` elements inside the `#front-matter` section. They do not carry `data-pos` or `data-paths` because they are always visible (the summary IS the below-GA path; the hook/preface/introduction are universal framing).

### 2.4 IDs for all addressable elements

Every chapter, section, and footnote gets a stable `id`. These IDs match the LaTeX `\label` scheme where possible: `pos01`, `pos02`, `pos08`, etc. Cross-references within chapters use `pos08:section-name` format. The TOC links to these IDs. URL fragment navigation works: `Relinquishment.html#pos08` opens directly to that chapter.


---

## 3. Path Definitions (Data)

Stored as a `<script type="application/json">` block at the bottom of the file. Not executable JavaScript — just data. The reader JS parses it.

```json
{
  "paths": [
    {
      "id": "below-ga",
      "name": "The Short Version",
      "subtitle": "A Simple Summary (~5K words, ~20 minutes)",
      "description": "The whole story in plain language. Complete on its own.",
      "audience": "Anyone. No prerequisites.",
      "chapters": ["summary"],
      "closing": "pos35",
      "wordcount": 5000,
      "minutes": 20
    },
    {
      "id": "ga",
      "name": "The Story",
      "subtitle": "Parts I & II (~16K words, ~1 hour)",
      "description": "Who these people are, what they did, and why it matters.",
      "audience": "General audience. No science background needed.",
      "chapters": ["pos01","pos02","pos04","pos05","pos06","pos07"],
      "closing": "pos35",
      "wordcount": 16000,
      "minutes": 60
    },
    {
      "id": "journalist",
      "name": "The Investigation",
      "subtitle": "GA + ethics, evidence, aftermath (~29K words, ~2 hours)",
      "description": "The full ethical reckoning. Why they did it. What it cost. The evidence.",
      "audience": "Journalists, lawyers, ethicists.",
      "includes_path": "ga",
      "chapters": ["pos08","pos22","pos18","pos23","pos19","pos28","pos29","pos34","pos34b"],
      "closing": "pos35",
      "wordcount": 29000,
      "minutes": 120
    },
    {
      "id": "intel",
      "name": "The Assessment",
      "subtitle": "GA + operations, evidence, capability (~26K words, ~1.5 hours)",
      "description": "Operational context. Tradecraft. Capability assessment. Evidence you can cross-reference.",
      "audience": "Intelligence analysts, military, policy.",
      "includes_path": "ga",
      "chapters": ["pos08","pos26","pos18","pos19","pos17","pos30","pos28","pos29"],
      "closing": "pos35",
      "wordcount": 26000,
      "minutes": 100
    },
    {
      "id": "implications",
      "name": "The Implications",
      "subtitle": "Journalist path + what follows (~35K words, ~2.5 hours)",
      "description": "If any of this is true, what does it mean? Guardian's design, ethics, the strategic picture.",
      "includes_path": "journalist",
      "audience": "Policy makers, philosophers, technologists.",
      "chapters": ["pos24","pos25","pos27","pos30","pos32","pos31"],
      "closing": "pos35",
      "wordcount": 35000,
      "minutes": 140
    },
    {
      "id": "science",
      "name": "Everything",
      "subtitle": "The complete book (~50K words, ~3.5 hours)",
      "description": "Five fields. The convergence. The full technical and human case.",
      "includes_path": "implications",
      "audience": "Scientists, engineers, the deeply curious.",
      "chapters": ["pos09","pos10","pos11","pos14","pos12","pos13","pos15","pos16","pos17","pos20","pos21","pos26"],
      "closing": "pos35",
      "wordcount": 50000,
      "minutes": 210
    }
  ]
}
```

### Path resolution algorithm

Paths are cumulative (except Intel, which branches from GA):

```
resolve(pathId):
  path = paths[pathId]
  if path.includes_path:
    chapters = resolve(path.includes_path) + path.chapters
  else:
    chapters = ["front-matter"] + path.chapters
  chapters.push(path.closing)
  return chapters
```

Intel is the special case: it includes GA but does NOT include Journalist. The `includes_path` field handles this correctly — Intel's `includes_path` is `"ga"`, not `"journalist"`.

### Shared chapters across paths

pos08, pos17, pos18, pos19, pos26, pos28, pos29, pos30 appear in multiple paths. A chapter is shown once; the `data-paths` attribute lists all paths it belongs to. The path resolver uses the ordering from its own `chapters` array, not positional order.


---

## 4. Path Selection UI

### 4.1 JS-off version (static HTML, always present)

```html
<nav id="path-selector" role="navigation" aria-label="Reading path">
  <h2>How would you like to read this?</h2>
  <p>This book has six reading depths. Each is complete on its own.
     Choose your path, or just scroll down to start reading.</p>

  <details>
    <summary><strong>The Short Version</strong> — ~20 minutes</summary>
    <p>The whole story in plain language. Complete on its own.</p>
    <p><a href="#summary">Start reading</a></p>
  </details>

  <details>
    <summary><strong>The Story</strong> — ~1 hour</summary>
    <p>Who these people are, what they did, and why it matters.</p>
    <p><a href="#pos01">Start reading</a></p>
  </details>

  <!-- ... one <details> per path ... -->

  <details>
    <summary><strong>Everything</strong> — ~3.5 hours</summary>
    <p>The complete book. Five fields. The full technical and human case.</p>
    <p><a href="#pos01">Start reading</a></p>
  </details>

  <p><small>If you're not sure, start with The Story. You can always go deeper.</small></p>
</nav>
```

With JS off, all `<details>` elements work natively (HTML5 disclosure widget). The "Start reading" links jump to the first chapter of that path. The rest of the book is still visible below — the reader scrolls past chapters they don't need.

### 4.2 JS-on version (replaces static version)

When JS runs, it replaces the `<details>` blocks with a card-based selector:

- Six cards arranged in a 2x3 grid (desktop) or stacked (mobile)
- Each card shows: path name, time estimate, one-sentence description, audience hint
- Hovering a card highlights the chapters that path includes (in the TOC)
- Clicking a card: hides all chapters NOT in that path, scrolls to first chapter
- "Read Everything" is visually distinct (full-width, bottom of grid)
- A "Change path" button appears in the floating nav after selection

### 4.3 No path selected = Everything visible

If the reader never clicks a path (JS-off, or JS-on but no selection), ALL chapters are visible in the token-map's optimal order. This is the "Everything" path by default. The book reads linearly.

### 4.4 Path selection persistence

- `localStorage.setItem('relinquishment-path', pathId)` — survives page reload
- On load, if a stored path exists, apply it silently (no re-showing the selector)
- A "Reset path" option clears storage and shows all chapters
- No cookies. No server. No tracking. localStorage only, with graceful fallback to no persistence.


---

## 5. Dynamic Reordering (JS behavior)

### 5.1 The core problem

The physical file order is the optimal linear reading order (the "Everything" path, determined by sort experiments). But the Intel path needs a DIFFERENT chapter order than the linear sequence. Specifically, Intel reads:

```
GA → pos08 → pos26 → pos18 → pos19 → pos17 → pos30 → pos28 → pos29
```

But the physical file order is:
```
Part II: pos08 → pos22 → pos18 → pos23 → pos19 → pos28 → pos29 → pos34 → pos34b
Part III: pos24 → pos25 → pos27 → pos30 → pos32 → pos31
Part IV: ... pos17 ... pos26 ...
```

Intel needs pos26 (Part IV in file) right after pos08 (Part II in file), and pos17 (Part IV) before pos30 (Part III). The Journalist, Implications, and Science paths don't have this problem — they read in file order, just skipping chapters.

### 5.2 Strategy: DOM reordering, not duplication

When Intel path is selected, JS physically moves the `<article>` elements into the correct order within a reading container. This is better than duplicating content (which doubles file size and breaks anchor links) or CSS-based `order` (which breaks screenreader order).

```javascript
function applyPath(pathId) {
  var path = pathData.paths.find(p => p.id === pathId);
  var resolved = resolveChapters(path);
  var container = document.getElementById('reading-flow');

  // Hide all chapters
  document.querySelectorAll('article[data-pos]').forEach(function(el) {
    el.hidden = true;
    el.setAttribute('aria-hidden', 'true');
  });

  // Show and reorder path chapters
  resolved.forEach(function(chapterId) {
    var el = document.getElementById(chapterId);
    if (el) {
      el.hidden = false;
      el.removeAttribute('aria-hidden');
      container.appendChild(el);  // moves element to end of container
    }
  });

  // Show/hide Part headings based on which parts have visible chapters
  updatePartVisibility();

  // Inject bridge text
  injectBridgeText(pathId);

  // Update TOC
  filterTOC(pathId);

  // Update progress tracker
  resetProgress(resolved);
}
```

**Why `hidden` + `aria-hidden`:** The `hidden` attribute prevents rendering and is natively understood by screenreaders. `aria-hidden="true"` is belt-and-suspenders for older assistive tech.

### 5.3 Part headings

When chapters move across Part boundaries (Intel path), the Part headings (`<h2>`) need updating. The approach:

- Part headings are separate `<div>` elements, not inside any chapter's `<article>`
- When a path is applied, Part headings are shown/hidden based on whether any of their chapters are visible
- For Intel path, the Part II heading may need a different subtitle. This is handled by bridge text (Section 6).

### 5.4 Reverting to full book

"Show Everything" undoes the path selection:
1. Move all `<article>` elements back to their original Part `<section>` containers (the order is stored in an array at page load, before any reordering)
2. Remove `hidden` and `aria-hidden` from all chapters
3. Remove injected bridge text
4. Restore full TOC
5. Clear localStorage path selection

### 5.5 Edge case: Intel path shared chapters

pos17 and pos26 appear in both Intel and Science paths. In file order, they live in Part IV. When Intel path is selected, they move into the Intel reading sequence. When Science path is selected, they stay in Part IV. No conflict — a chapter is only shown once per path.


---

## 6. Bridge Text

### 6.1 Purpose

When a reader follows a shorter path, they skip chapters. Sometimes the transition between two chapters in a path needs a connecting sentence or two. Bridge text provides this.

### 6.2 Data format

Stored as JSON in `<script type="application/json" id="bridge-data">`:

```json
{
  "bridges": [
    {
      "path": "journalist",
      "after": "pos07",
      "before": "pos08",
      "text": "The GA path ends here. The chapters that follow explore the ethical weight of what you've just read."
    },
    {
      "path": "intel",
      "after": "pos08",
      "before": "pos26",
      "text": "The intelligence community's own encounter with this technology came through established channels."
    }
  ]
}
```

### 6.3 Rendering

JS creates `<aside>` elements with class `bridge-text` and `role="note"`:

```html
<aside class="bridge-text" role="note" aria-label="Path transition">
  <p>The GA path ends here. The chapters that follow explore the
  ethical weight of what you've just read.</p>
</aside>
```

Bridge text is visually distinct: italic, lighter color, no track stripe. It signals "the author is talking to you about the structure" rather than being part of the narrative.

### 6.4 JS-off fallback

With JS off, no bridge text appears. The book reads linearly without it. The path boundaries are marked by Part headings, which serve as natural breaks. This is acceptable — bridge text is a polish feature, not structural.


---

## 7. CSS Strategy

### 7.1 Base CSS (in `<head>`, ~40 lines)

Only what's needed for readable prose with JS off:

```css
/* Base typography */
body {
  max-width: 40em;
  margin: 0 auto;
  padding: 1em 1.5em;
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.65;
  color: #1a1a1a;
}

h1 { font-size: 2em; margin-top: 0; }
h2 { font-size: 1.5em; margin-top: 2em; border-bottom: 1px solid #ccc; padding-bottom: 0.3em; }
h3 { font-size: 1.25em; margin-top: 1.5em; }

blockquote { margin: 1.5em 0; padding-left: 1.5em; border-left: 3px solid #ccc; }

a { color: #1a5276; }

/* Dark mode */
@media (prefers-color-scheme: dark) {
  body { background: #1a1a1a; color: #e0e0e0; }
  a { color: #6ba3f7; }
  h2 { border-bottom-color: #444; }
  blockquote { border-left-color: #555; }
}

/* Skip link */
.skip-link {
  position: absolute; left: -9999px;
}
.skip-link:focus {
  position: static; left: auto;
  display: block; padding: 0.5em; background: #ff0; color: #000;
}

/* Mobile */
@media (max-width: 600px) {
  body { padding: 0.5em; font-size: 16px; }
}
```

That's it for the `<head>`. No track colors, no path UI, no floating nav, no progress bar.

### 7.2 Enhanced CSS (bottom of file, inside `<style id="enhanced-css">`)

Everything the JS-on experience needs:

```css
/* Track indicators — left border on chapter articles */
article[data-track="confession"]  { border-left: 4px solid #1A6B6A; padding-left: 1em; }
article[data-track="testament"]   { border-left: 4px solid #C4913B; padding-left: 1em; }
article[data-track="awakening"]   { border-left: 4px solid #6B3FA0; padding-left: 1em; }
article[data-track="convergence"] { border-left: 4px solid #8C7853; padding-left: 1em; }
/* Bridge chapters: no stripe (intentional — matches PDF behavior) */

/* Path selector cards */
.path-card { ... }
.path-card:hover { ... }
.path-card.selected { ... }

/* Floating navigation bar */
#reader-nav { ... }

/* Progress indicator */
#reading-progress { ... }

/* Bridge text */
.bridge-text { font-style: italic; color: #666; margin: 2em 0; padding: 1em; }

/* "Go deeper" prompt */
.go-deeper { ... }

/* Dark mode overrides for all enhanced elements */
@media (prefers-color-scheme: dark) { ... }

/* Print styles — see Section 9 */
@media print { ... }
```

### 7.3 Why enhanced CSS is at the bottom, not injected by JS

Track colors should work even with JS off. A browser with CSS but no JS should still see the colored track stripes. Putting the enhanced CSS in a `<style>` tag at the bottom (not inside `<script>`) means it loads without JS. The path UI CSS is wasted in this case, but it's a few hundred bytes — not worth the complexity of JS-conditional loading.


---

## 8. Progressive Upgrade: "Want to Go Deeper?"

### 8.1 Concept

When a reader finishes their selected path (reaches the closing chapter, pos35), they see a prompt:

> You've read The Story. Want to go deeper?
> **The Investigation** adds 13,000 words on the ethics, evidence, and aftermath.
> [Continue to The Investigation] [Stay here]

This is the primary mechanism for drawing readers into longer paths.

### 8.2 Implementation

- JS injects an `<aside class="go-deeper">` element after the last chapter in the current path, before pos35 (The Question)
- The prompt names the next path in the hierarchy (GA -> Journalist -> Implications -> Science)
- Intel path does NOT get a "go deeper" prompt to Journalist (different branch). Instead: "Want the science? Start at The Investigation, then continue to The Implications and The Science."
- Clicking "Continue" applies the next path and scrolls to the first new chapter
- The "Stay here" option scrolls to pos35

### 8.3 Path hierarchy for upgrades

```
Below-GA  →  GA  →  Journalist  →  Implications  →  Science
                →  Intel (dead end — separate branch, no automatic upgrade)
```

### 8.4 JS-off fallback

No "go deeper" prompt appears. The full book is visible; the reader scrolls naturally.


---

## 9. Print CSS

### 9.1 Behavior

When a reader prints (Ctrl+P or browser print dialog), the print stylesheet activates:

```css
@media print {
  /* Hide UI elements */
  #path-selector, #reader-nav, #reading-progress,
  .go-deeper, .bridge-text, .skip-link { display: none; }

  /* Show only selected path's chapters */
  article[hidden] { display: none !important; }

  /* Page breaks */
  article[data-pos] { page-break-before: always; }
  h2[data-part] { page-break-before: always; }

  /* Typography for print */
  body { max-width: none; margin: 0; padding: 0; font-size: 11pt; }

  /* Remove colored borders (ink-saving) */
  article[data-track] { border-left: none; padding-left: 0; }

  /* Force light mode */
  body { background: white; color: black; }
  a { color: black; text-decoration: underline; }
}
```

If a path is selected, printing produces that path. If no path is selected, printing produces the full book. The `hidden` attribute naturally handles this — hidden chapters don't print.

### 9.2 Limitation

Print CSS cannot reorder DOM elements. If the reader selected Intel path (which reorders chapters via JS), printing after that selection will print in the JS-reordered DOM order, which is correct. If JS never ran, the file prints in physical order, which is the "Everything" order — also correct.


---

## 10. Progress Indicator

### 10.1 Visual design

A thin horizontal bar at the top of the viewport (3px height, subtle color). Shows percentage through the SELECTED PATH, not through the entire document.

### 10.2 Calculation

```javascript
function updateProgress() {
  var pathChapters = getVisibleChapters();
  var lastChapter = pathChapters[pathChapters.length - 1];
  var firstChapter = pathChapters[0];

  var totalHeight = lastChapter.offsetTop + lastChapter.offsetHeight - firstChapter.offsetTop;
  var scrolled = window.scrollY - firstChapter.offsetTop;
  var pct = Math.max(0, Math.min(100, (scrolled / totalHeight) * 100));

  progressBar.style.width = pct + '%';
}
```

### 10.3 Chapter-level indicator in nav bar

The floating nav bar (Section 10.4) shows: "Chapter 3 of 7" (for the selected path, not absolute position).

### 10.4 Floating navigation bar

Redesigned from the existing reader.js, adapted for path awareness:

```
[< Prev]    Chapter 3 of 7: The Code War    [Next >]    [TOC]    [Change path]
```

- Prev/Next navigate between chapters IN THE SELECTED PATH
- Chapter count is path-relative
- "Change path" reopens the path selector
- Keyboard: Left/Right arrows for Prev/Next, Home for top


---

## 11. Accessibility

### 11.1 Semantic structure

- Single `<header>` with book title and metadata
- `<nav role="doc-toc">` for table of contents
- `<nav role="navigation">` for path selector
- `<main>` wrapping all content
- `<article>` for each chapter (with appropriate ARIA attributes)
- `<section>` for Part groupings
- `<aside>` for bridge text and "go deeper" prompts
- `<footer>` for colophon/verification

### 11.2 ARIA labels

- `aria-label` on all navigation landmarks
- `aria-expanded` on TOC toggle
- `aria-hidden="true"` on chapters hidden by path selection
- `aria-current="step"` on the current chapter in the floating nav
- `role="note"` on bridge text asides
- `aria-live="polite"` on the progress/chapter indicator (announces path changes)

### 11.3 Keyboard navigation

- Skip link (first focusable element)
- Tab through all interactive elements
- Arrow keys for chapter navigation (only when no input is focused)
- Escape closes the path selector if it's a modal
- Enter/Space activates path cards

### 11.4 Screenreader reading order

With JS off: the DOM order is the reading order. Logical, linear.

With JS on and a path selected: hidden chapters have `aria-hidden="true"` and `hidden` attribute. Screenreader skips them entirely. The reading order follows the DOM order of visible chapters, which has been physically reordered by JS.

### 11.5 Color contrast

All track colors meet WCAG AA contrast ratio against both light and dark backgrounds. The existing palette was chosen for this (from epub.css). Verify with a contrast checker during implementation.

### 11.6 Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; scroll-behavior: auto !important; }
}
```

### 11.7 Testing strategy

1. **VoiceOver (macOS):** Navigate full path. Verify headings, landmarks, skip link.
2. **NVDA (Windows):** Same tests. (Bruce may not have access — defer or use a free VM.)
3. **axe DevTools (browser extension):** Automated WCAG audit.
4. **Keyboard only:** Tab through entire path without mouse.
5. **High contrast mode (Windows):** Verify readability.
6. **200% zoom:** Verify nothing breaks.
7. **Text-only browser (lynx or w3m):** Verify content reads naturally.


---

## 12. Build Integration

### 12.1 Current pipeline

The current `make html` runs:
1. `preprocess.py` — patches LaTeX for pandoc
2. pandoc — converts LaTeX to HTML5 with `--self-contained`
3. Appends `reader-inline.html` (the current reader.js wrapped in `<script>`)

### 12.2 New pipeline

The monolithic reader replaces the pandoc HTML output. Two options:

**Option A: Post-process pandoc output**
1. `make html` runs pandoc as today (produces raw HTML)
2. A new Python script (`build/assemble-reader.py`) transforms the pandoc output:
   - Restructures heading hierarchy (h1 -> h3)
   - Wraps chapters in `<article>` elements with data attributes
   - Groups chapters into Part `<section>` elements
   - Injects the path selector HTML
   - Injects the base CSS in `<head>`, strips pandoc's default styles
   - Appends enhanced CSS, JSON data, and reader JS at bottom
   - Outputs the final monolithic file

**Option B: Generate HTML directly from LaTeX**
Skip pandoc entirely. Write a LaTeX-to-HTML converter that understands the manuscript's specific markup patterns (\settrack, \chapter, \label, \section, etc.) and outputs the exact HTML structure we need.

**Recommendation: Option A.** Pandoc handles the hard parts (math rendering with MathML, footnote processing, cross-reference resolution, Unicode normalization). Our post-processor handles the structural rearrangement. Don't reinvent pandoc.

### 12.3 Makefile change

```makefile
html: gitinfo build/reader-monolith.html
	python3 build/preprocess.py
	cd build/epub-tmp && pandoc main.tex \
		-f latex -t html5 \
		--standalone \
		--top-level-division=chapter \
		--toc --toc-depth=1 \
		--mathml \
		--metadata-file=../../build/metadata.yaml \
		-o ../../build/pandoc-raw.html
	python3 build/assemble-reader.py \
		build/pandoc-raw.html \
		-o $(JOBNAME).html

build/reader-monolith.html: build/reader-monolith.js build/base.css build/enhanced.css build/path-data.json build/bridge-data.json
	python3 build/pack-reader.py  # combines all assets into template fragments
```

The `--self-contained` flag is removed from pandoc — we handle asset embedding in the assembler. This gives us control over where assets end up in the file.

### 12.4 New build files

```
build/
  assemble-reader.py    # post-processes pandoc output into monolithic reader
  pack-reader.py        # packs JS/CSS/JSON into template fragments
  reader-monolith.js    # the full reader JavaScript
  base.css              # minimal <head> CSS
  enhanced.css          # bottom-of-file enhanced CSS
  path-data.json        # path definitions
  bridge-data.json      # bridge text between chapters
  path-selector.html    # static path selector (noscript version)
```


---

## 13. Content Generation from LaTeX

### 13.1 The identification problem

The preprocessor (`preprocess.py`) already converts `\settrack{trackone}` to `% track: confession`. The pandoc output does NOT preserve these as HTML attributes. We need to map chapters to their track, position, and path membership.

### 13.2 Chapter identification map

`assemble-reader.py` needs a static map (or derives it from the `\label` and `% track:` patterns). The map is maintained as a Python dict or JSON file:

```python
CHAPTER_MAP = {
    "pos01:three-possibilities": {
        "pos": "01", "track": "bridge",
        "paths": ["ga", "journalist", "intel", "implications", "science"],
        "part": 1
    },
    "t2:ch01:alpha-farm": {
        "pos": "02", "track": "testament",
        "paths": ["ga", "journalist", "intel", "implications", "science"],
        "part": 1
    },
    # ... etc for all chapters
}
```

This map is the single source of truth for the HTML reader's data attributes. It must be kept in sync with `main.tex` and `token-map.md`.

### 13.3 Track extraction

The preprocessor already converts `\settrack{}` to `% track: name`. Pandoc drops LaTeX comments. So the assembler needs to identify chapters by their `id` attribute (derived from `\label`), not by any inline marker. The chapter identification map (13.2) handles this.


---

## 14. Edge Cases and Failure Modes

### 14.1 Chapter with no label

If a LaTeX chapter has no `\label`, pandoc auto-generates an id from the chapter title. The assembler must handle both explicit labels (matching the map) and auto-generated slugs (fallback matching by title text).

### 14.2 Footnotes

Pandoc renders footnotes as `<a>` links to `<section class="footnotes">` at the end of the document. In a path-aware reader, this section must remain visible regardless of path selection. Footnotes from hidden chapters should still be accessible if a reader follows a direct link.

Alternative: Convert to inline footnotes (popup on click, visible on hover). This is more complex but avoids the "footnotes at the end of a 50K-word file" problem. Defer to implementation phase.

### 14.3 Cross-references between chapters

If a Journalist-path chapter references a Science-path chapter that's currently hidden, the link should still work. Clicking it could either: (a) reveal just that chapter temporarily, or (b) show a tooltip saying "This chapter is in the Science path. Switch paths to read it."

Recommendation: (a) is simpler and more useful. Reveal the target chapter, scroll to it, show a subtle banner: "This chapter is from the Science path. [Return to your path] [Switch to Science]."

### 14.4 Direct URL navigation

If someone opens `Relinquishment.html#pos17`, the file should:
1. Load normally (all content visible by default)
2. Scroll to pos17
3. If a stored path doesn't include pos17, reveal pos17 anyway (direct link overrides path)

### 14.5 File size

Current pandoc HTML: 531KB. The monolithic reader adds:
- Path definitions JSON: ~2KB
- Bridge text JSON: ~3KB
- Reader JS: ~15KB (current reader.js is 6KB; new one is ~2.5x)
- Enhanced CSS: ~3KB
- Path selector HTML: ~2KB
- Data attributes on chapters: ~1KB

Total overhead: ~26KB. Expected final size: ~560KB. Well within reason for a self-contained ebook.

### 14.6 Very old browsers

The file uses: `<details>`/`<summary>` (IE11 doesn't support), `hidden` attribute (IE11 doesn't support), `querySelectorAll`, `forEach`, `localStorage`. All are supported in every browser from roughly 2016 forward.

For IE11 and older: the file degrades to "browser with JS off" tier. All content visible, no path selection. This is acceptable — IE11 usage is ~0.2%.

### 14.7 Email clients

When attached to an email and opened in a webmail client (Gmail, Outlook web), most CSS and all JS are stripped. The content degrades to "text editor" tier — plain semantic HTML. The heading hierarchy and paragraph structure carry the reading experience. This is fine.


---

## 15. Implementation Phases

### Phase 1: Static HTML structure
- Build `assemble-reader.py`
- Generate the full file with correct heading hierarchy, article elements, data attributes
- No JS, no enhanced CSS
- Verify: opens correctly in text editor, browser (JS off), screenreader
- Verify: all anchor links work, TOC is correct

### Phase 2: Path data and static selector
- Add path-data.json and bridge-data.json
- Add the static `<details>`/`<summary>` path selector
- Add base CSS
- Verify: `<details>` elements work in browser, links jump to correct chapters

### Phase 3: Reader JavaScript
- Write reader-monolith.js
- Path selection: show/hide chapters
- DOM reordering for Intel path
- Bridge text injection
- Floating nav bar
- Progress indicator
- Keyboard navigation
- localStorage persistence
- Verify: all six paths render correctly, Intel reordering works

### Phase 4: Enhanced CSS and polish
- Track color stripes
- Path card styling
- Dark mode for all enhanced elements
- Print CSS
- Reduced motion
- Verify: print each path, dark mode, mobile

### Phase 5: Accessibility audit
- Run axe DevTools
- VoiceOver walkthrough
- Keyboard-only navigation test
- High contrast mode
- 200% zoom
- Fix any failures

### Phase 6: Integration
- Update Makefile
- Verify `make html` produces the monolithic reader
- Verify `make epub` still works (separate pipeline, should be unaffected)
- Update release-infrastructure-plan.md


---

## 16. What This Plan Does NOT Cover

- **Content editing.** The plan assumes all chapters exist and contain final prose. pos34b (The Engine) may not be written yet. The assembler handles missing chapters gracefully (skips them, adjusts path).
- **Alignment appendix.** Plan 0052 adds a post-Science appendix for the AI safety community. The monolithic reader should treat it as an optional section accessible via direct link, not part of any standard path. Add as a future enhancement.
- **Offline service worker.** A service worker could cache the file for offline use. Unnecessary — the file is already self-contained. The browser's normal cache handles it.
- **Search.** In-page search (Ctrl+F) works natively in browsers. A custom search feature adds complexity without value.
- **Analytics.** Explicitly excluded. No tracking. Consistent with the book's ethics.

---

*Plan by Argus, Session 30, 2026-02-27.*
*Estimated implementation effort: 12-16 hours across Phases 1-6.*
*The monolithic reader embodies the book's thesis: self-contained, impossible to censor, accessible to everyone, controlled by no one.*
