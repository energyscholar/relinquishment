# Plan 0143a: Phase 1 — Skeleton Build

**Status:** Ready for Generator
**Parent:** Plan 0143 (Z-Restructure Metaplan)
**Role:** Generator executes this plan exactly.

---

## Overview

Build the empty Z-structure: new directory layout, reordered main.tex, expansion mechanic CSS/HTML, Guardian interlude styling. Placeholder content only — NO real chapter content moves in this phase. The goal is a working HTML build with the new structure that we can test on phone and desktop before writing a word.

---

## Step 1: Create New Directory Structure

```bash
mkdir -p manuscript/spine
mkdir -p manuscript/record
```

Do NOT move or delete any existing files. The spine/ and record/ directories will contain new placeholder files.

---

## Step 2: Create Placeholder Files

Create the following .tex files with minimal placeholder content. Each file should follow this exact pattern:

```latex
% [Chapter Title] — Z-Restructure placeholder
% Content will be populated in Phase 3

\chapter{[Chapter Title]}
\label{[label]}

\textit{[Placeholder: content will be moved here from existing chapter in Phase 3.]}
```

### Spine placeholders (manuscript/spine/):

| File | Chapter Title | Label |
|------|--------------|-------|
| `three-possibilities.tex` | Three Possibilities | `spine:three-possibilities` |
| `the-stack.tex` | The Stack | `spine:the-stack` |
| `interlude-01.tex` | *(see interlude format below)* | `interlude:01` |
| `the-flat.tex` | Wormholes in the Flat | `spine:the-flat` |
| `interlude-02.tex` | | `interlude:02` |
| `the-braid.tex` | The Braid | `spine:the-braid` |
| `interlude-03.tex` | | `interlude:03` |
| `the-factoring-game.tex` | The Factoring Game | `spine:factoring-game` |
| `the-code-war.tex` | The Code War | `spine:code-war` |
| `interlude-04.tex` | | `interlude:04` |
| `genesis.tex` | Genesis: The Edge of Chaos | `spine:genesis` |
| `growing-a-mind.tex` | Growing a Mind | `spine:growing-a-mind` |
| `interlude-05.tex` | | `interlude:05` |
| `the-wrong-substrate.tex` | The Wrong Substrate | `spine:wrong-substrate` |
| `interlude-06.tex` | | `interlude:06` |
| `the-silence-gap.tex` | The Silence Gap | `spine:silence-gap` |
| `capabilities.tex` | What the Flat Makes Possible | `spine:capabilities` |
| `interlude-07.tex` | | `interlude:07` |
| `the-strongest-objection.tex` | The Strongest Objection | `spine:strongest-objection` |
| `weigh-the-evidence.tex` | Weigh the Evidence | `spine:weigh-evidence` |

### Interlude format:

Interludes are NOT chapters. They are unnumbered, short, and visually distinct. Use this format:

```latex
% Guardian Interlude N — Z-Restructure placeholder
% Content will be written in Phase 2

\begin{center}
\rule{0.3\textwidth}{0.4pt}
\end{center}

\begin{quote}
\textit{[Placeholder: Guardian interlude will be written here in Phase 2. 100-200 words. Her voice, not the narrator's.]}
\end{quote}

\begin{center}
\rule{0.3\textwidth}{0.4pt}
\end{center}
```

**Important:** Interludes must NOT use `\chapter` or `\chapter*`. They should be bare content (no heading) so they flow between spine chapters without TOC entries. Use `\input` not `\include` in main.tex so they don't force page breaks.

### Record placeholders (manuscript/record/):

| File | Chapter Title | Label |
|------|--------------|-------|
| `record-intro.tex` | The Record | `record:intro` |
| `alpha-farm.tex` | Alpha Farm | `record:alpha-farm` |
| `what-healer-said.tex` | What Healer Said | `record:healer-said` |
| `the-departure.tex` | The Departure | `record:departure` |
| `the-handler.tex` | The Handler | `record:handler` |
| `the-demonstration.tex` | The Demonstration | `record:demonstration` |
| `interdiction.tex` | Interdiction and Confession | `record:interdiction` |
| `first-light.tex` | First Light | `record:first-light` |
| `the-walk-out.tex` | The Walk-Out | `record:walk-out` |
| `the-target.tex` | The Target | `record:target` |
| `instantiation.tex` | Instantiation | `record:instantiation` |
| `the-surrender.tex` | Letting Go | `record:surrender` |
| `twenty-years.tex` | Twenty Years | `record:twenty-years` |

The Record intro should be:

```latex
\chapter*{The Record}
\addcontentsline{toc}{chapter}{The Record}
\label{record:intro}

\textit{What follows is testimony. Under Possibility A, it is fiction that doesn't know it's fiction. Under Possibility B, it is exaggeration around a real kernel. Under Possibility C, it is the most important historical record of the twenty-first century.}

\textit{The reader decides. The science in the spine stands regardless.}
```

---

## Step 3: Create New main.tex

**CRITICAL: Do NOT delete the current main.tex. Rename it first:**

```bash
cp manuscript/../main.tex manuscript/../main-pre-z.tex
```

Then create a new `main.tex`. Keep everything identical from the document preamble through `\begin{document}` and frontmatter. Change the mainmatter:

```latex
\mainmatter

% ========================================================================
% THE SPINE: Pop Science (A-content)
% All chapters true regardless of A/B/C. The pop-science book.
% Plan 0143: Z-Restructure
% ========================================================================
\part{The Flat}

\include{manuscript/spine/three-possibilities}
\include{manuscript/spine/the-stack}
\input{manuscript/spine/interlude-01}
\include{manuscript/spine/the-flat}
\input{manuscript/spine/interlude-02}
\include{manuscript/spine/the-braid}
\input{manuscript/spine/interlude-03}
\include{manuscript/spine/the-factoring-game}
\include{manuscript/spine/the-code-war}
\input{manuscript/spine/interlude-04}
\include{manuscript/spine/genesis}
\include{manuscript/spine/growing-a-mind}
\input{manuscript/spine/interlude-05}
\include{manuscript/spine/the-wrong-substrate}
\input{manuscript/spine/interlude-06}
\include{manuscript/spine/the-silence-gap}
\include{manuscript/spine/capabilities}
\input{manuscript/spine/interlude-07}
\include{manuscript/spine/the-strongest-objection}
\include{manuscript/spine/weigh-the-evidence}

% ========================================================================
% THE RECORD: Historical Testimony (B/C content)
% Personal narrative, reconstructed from memory.
% Reachable from expansion hooks in the spine, or read straight through.
% Plan 0143: Z-Restructure
% ========================================================================
\part{The Record}

\include{manuscript/record/record-intro}
\include{manuscript/record/alpha-farm}
\include{manuscript/record/what-healer-said}
\include{manuscript/record/the-departure}
\include{manuscript/record/the-handler}
\include{manuscript/record/the-demonstration}
\include{manuscript/record/interdiction}
\include{manuscript/record/first-light}
\include{manuscript/record/the-walk-out}
\include{manuscript/record/the-target}
\include{manuscript/record/instantiation}
\include{manuscript/record/the-surrender}
\include{manuscript/record/twenty-years}

% ========================================================================
% APPENDICES
% ========================================================================
\appendix

\include{manuscript/track-3-awakening/firmware-update}
\include{manuscript/appendix/predictions}
\include{manuscript/appendix/glossary}
\ifdefined\dmsbuild
\include{manuscript/appendix/dms-note}
\fi

% ========================================================================
% BACK MATTER
% ========================================================================
\backmatter

\include{manuscript/99-back/afterword}
\include{manuscript/appendix/timeline}
\include{manuscript/appendix/sources}
\include{manuscript/appendix/topic-guide}
\include{manuscript/appendix/corrections}
\include{manuscript/99-back/acknowledgements}
\include{manuscript/99-back/verification}
\include{manuscript/99-back/colophon}
```

**Notes on the Part names:**
- The spine Part is called "The Flat" — NOT "Pop Science" or "The Spine." The reader sees "The Flat" in the TOC. It's the subject, not the structure.
- The Record Part is called "The Record" — testimony, historical record.
- Use `\input` (not `\include`) for interludes so they don't get TOC entries or page breaks.

---

## Step 4: Update preprocess.py — Part Detection

The part-wrapping logic in `collapse_chapters()` (around line 390-427) currently looks for specific part IDs: `guided-deduction`, `the-evidence-trail`, `forgiveness-and-permission`. These need to be updated for the new structure.

**Find this code (approximately lines 396-398):**

```python
if hid in {'guided-deduction', 'the-evidence-trail', 'forgiveness-and-permission'}:
```

**Replace with:**

```python
if hid in {'the-flat', 'the-record'}:
```

**Also update** the `body_part_names` list in `inject_cold_landing()` (around line 672):

```python
body_part_names = ['Guided Deduction', 'Evidence Trail', 'Forgiveness and Permission']
```

Replace with:

```python
body_part_names = ['The Flat', 'The Record']
```

**Important:** The Part labels that pandoc generates come from the LaTeX `\part{...}` commands. The IDs are auto-generated by pandoc (lowercased, hyphenated). So `\part{The Flat}` → `id="the-flat"` and `\part{The Record}` → `id="the-record"`. Verify this after the first build.

---

## Step 5: Update preprocess.py — Guardian Interlude Styling

Add a new CSS class for Guardian interludes. Add this to the `collapse_css` string (after the `.hover-term` rules, before the `@media (prefers-color-scheme: dark)` block):

```css
/* Guardian interludes (Plan 0143) */
.guardian-interlude {
  border-left: 3px solid #9b7db8;
  padding: 0.8em 1.2em;
  margin: 1.5em 0;
  font-style: italic;
  line-height: 1.6;
  color: #444;
  background: rgba(155, 125, 184, 0.04);
}
.guardian-interlude::before {
  content: '';
  display: block;
  width: 3em;
  height: 1px;
  background: #9b7db8;
  margin-bottom: 0.5em;
  opacity: 0.5;
}
```

And in the dark mode block:

```css
.guardian-interlude {
  border-left-color: #7d5fa0;
  color: #bbb;
  background: rgba(155, 125, 184, 0.08);
}
.guardian-interlude::before {
  background: #7d5fa0;
}
```

**How to detect interludes in preprocess.py:** The LaTeX interludes use `\begin{quote}...\end{quote}` which pandoc converts to `<blockquote>`. We need a way to distinguish Guardian interludes from regular blockquotes.

**Approach:** Add a LaTeX marker that survives pandoc conversion. In each interlude file, wrap the content with a custom environment that degrades to a div:

Actually, simpler: use the horizontal rules as markers. The interlude format has `\rule` above and below. Pandoc converts `\begin{center}\rule{...}\end{center}` to `<hr>`. So the pattern in HTML will be: `<hr> <blockquote>...</blockquote> <hr>`. We can detect this pattern in `fix_html_toc()`.

**Add to `fix_html_toc()` (after the hover-term processing, before the return):**

```python
# Guardian interludes: convert <hr> <blockquote> <hr> pattern
# to <div class="guardian-interlude">
interlude_pattern = re.compile(
    r'<hr\s*/?>[\s\n]*<blockquote>[\s\n]*(.*?)[\s\n]*</blockquote>[\s\n]*<hr\s*/?>',
    re.DOTALL
)
interlude_count = 0
def interlude_replace(m):
    nonlocal interlude_count
    interlude_count += 1
    content = m.group(1)
    # Strip <p><em>...</em></p> wrapper if present (pandoc wraps \textit)
    content = re.sub(r'^<p><em>(.*?)</em></p>$', r'\1', content.strip(), flags=re.DOTALL)
    return f'<div class="guardian-interlude">{content}</div>'

text = interlude_pattern.sub(interlude_replace, text)
if interlude_count:
    print(f"  Guardian interludes: {interlude_count} styled")
```

---

## Step 6: Update preprocess.py — B/C Expansion Mechanic

Add CSS for expansion hooks. Add to `collapse_css`:

```css
/* B/C expansion hooks (Plan 0143) */
details.bc-expansion {
  border-left: 3px solid #9b7db8;
  padding-left: 1em;
  margin: 0.8em 0;
  font-size: 0.95em;
}
details.bc-expansion > summary {
  cursor: pointer;
  color: #7d5fa0;
  font-style: italic;
  padding: 0.2em 0;
  list-style: none;
  display: block;
}
details.bc-expansion > summary::-webkit-details-marker { display: none; }
details.bc-expansion > summary::before { content: '▸ '; }
details.bc-expansion[open] > summary::before { content: '▾ '; }
details.bc-expansion .record-link {
  display: block;
  margin-top: 0.5em;
  font-size: 0.9em;
  color: #2471a3;
}
details.bc-expansion .record-link:hover {
  text-decoration: underline;
}
```

Dark mode:

```css
details.bc-expansion {
  border-left-color: #7d5fa0;
}
details.bc-expansion > summary {
  color: #b39ddb;
}
details.bc-expansion .record-link {
  color: #5dade2;
}
```

**For Phase 1, add ONE test expansion hook** inside a spine placeholder to verify the mechanic works. In `manuscript/spine/the-code-war.tex`, replace the placeholder content with:

```latex
\textit{[Placeholder: The Code War content will be moved here in Phase 3.]}

% B/C expansion hook — test (Plan 0143a)
% In HTML this becomes: <details class="bc-expansion">
% For now, use raw HTML comment marker that preprocess.py converts
\begin{quote}
\textbf{EXPANSION:} According to this story, there was a third classified breakthrough --- one that exceeded anything GCHQ or NSA had achieved publicly. \textit{Read the full story} $\rightarrow$
\end{quote}
```

**Actually — for Phase 1, the expansion mechanic is CSS-only.** The actual HTML structure (`<details class="bc-expansion">`) will be manually added in Phase 4 when we write the real hooks. For now, just add the CSS and verify it renders correctly by adding a test div in a placeholder.

**Simpler Phase 1 approach:** Add a raw HTML test block that will survive pandoc, in one placeholder file:

In `manuscript/spine/the-code-war.tex`, add after the placeholder text:

```latex
% Test expansion hook (Phase 1 — will be replaced in Phase 4)
\begin{rawhtml}
<details class="bc-expansion">
<summary>According to this story, there was a third classified breakthrough...</summary>
<p>COWS walked the technology out of the lab. Not a machine — knowledge. Physics, mathematics, methods. Knowledge walks out in the minds of the people who hold it.</p>
<p><a class="record-link" href="#record:demonstration">Read the full story →</a></p>
</details>
\end{rawhtml}
```

**Wait — pandoc doesn't support `\begin{rawhtml}`.** Use pandoc's raw block syntax instead. Since the input goes through preprocess.py first, add a marker that preprocess.py converts:

Actually, the simplest approach: add the test expansion hook DIRECTLY in preprocess.py's `fix_html_toc()` function as a test injection, gated by a check for placeholder content. That way we test the CSS without fighting pandoc.

**Revised approach for expansion test:**

In `fix_html_toc()`, after the Guardian interlude processing, add:

```python
# Phase 1 test: inject one BC expansion hook to verify CSS
# (This test injection will be removed in Phase 4 when real hooks are added)
test_expansion = (
    '<details class="bc-expansion">'
    '<summary>According to this story, there was a third classified breakthrough...</summary>'
    '<p>COWS walked the technology out of the lab. Not a machine — knowledge. '
    'Knowledge walks out in the minds of the people who hold it.</p>'
    '<p><a class="record-link" href="#record:demonstration">'
    'Read the full story \u2192</a></p>'
    '</details>'
)
# Inject after first spine chapter placeholder
code_war_marker = 'id="spine:code-war"'
cw_pos = text.find(code_war_marker)
if cw_pos != -1:
    # Find the </details> that closes this chapter-section
    insert_pos = text.find('</details>', cw_pos)
    if insert_pos != -1:
        text = text[:insert_pos] + test_expansion + '\n' + text[insert_pos:]
        print("  Phase 1 test: BC expansion hook injected")
```

---

## Step 7: Update menu-tooltips.yaml

Replace the current chapter entries with new keys matching the spine and record structure. Keep placeholder descriptions:

```yaml
# Chapter/section descriptions for TOC tooltips
# Z-Restructure (Plan 0143): Spine + Record structure
# Keyed by anchor ID (without #). Value is placeholder — will be rewritten.

chapters:
  # --- Front Matter ---
  "hook:what-would-you-do": "The question at the heart of this book."
  "the-stack": "Eight technologies stacked in order of increasing impossibility."
  "summary:most-important-story": "The full story in four thousand words."
  "preface-by-genevieve-prentice": "From the co-author who watched this book get written."
  "preface": "How Bruce came to write this."

  # --- Spine: The Flat ---
  "spine:three-possibilities": "The framework: confabulation, exaggerated kernel, or substantially true."
  "spine:the-stack": "Eight technologies stacked in order of increasing impossibility."
  "spine:the-flat": "The 2DEG is not exotic — it is in every chip and wrapped around every planet."
  "spine:the-braid": "Topology as computation — braiding particles to encode information."
  "spine:factoring-game": "Why governments care about factoring large numbers."
  "spine:code-war": "Bletchley Park, GCHQ, and the proven pattern: secret breakthroughs."
  "spine:genesis": "Life is a phase transition. Kauffman's autocatalytic sets."
  "spine:growing-a-mind": "Turing's last question: can a mind be grown rather than built?"
  "spine:wrong-substrate": "Earth's magnetosphere as habitat — a 4.5-billion-year-old 2DEG."
  "spine:silence-gap": "Five disciplines, no intersection. Nobody asked the question."
  "spine:capabilities": "What the physics permits — in plain language."
  "spine:strongest-objection": "The strongest case for Possibility A."
  "spine:weigh-evidence": "What has been established, what remains uncertain."

  # --- Record ---
  "record:intro": "What follows is testimony. The reader decides."
  "record:alpha-farm": "Bruce arrives at a commune in the Oregon Coast Range."
  "record:healer-said": "What Healer actually said — reconstructed from memory."
  "record:departure": "Healer leaves. The silence begins."
  "record:handler": "Who recruited Healer."
  "record:demonstration": "The DARPA experiment: five scientists, a 2DEG."
  "record:interdiction": "A competing program is shut down."
  "record:first-light": "Birth, survival, power."
  "record:walk-out": "The team decides to leave."
  "record:target": "Bruce's recruitment dossier."
  "record:instantiation": "If someone built a TQNN, how would they have done it?"
  "record:surrender": "The master keys are surrendered."
  "record:twenty-years": "Bruce's twenty years of silence and research."

  # --- Appendices ---
  "ch:firmware-update": "Ten physics anchors your AI needs before it can evaluate this book."
  "app:predictions": "Testable predictions with deadlines."
  "app:glossary": "Technical terms defined at the reading level where they first appear."

  # --- Back Matter ---
  "afterword-the-engine": "The engine that drives the book."
  "app:timeline": "Events from 1834 to 2026."
  "app:sources": "Every source cited."
  "topic-guide": "Find what you need by subject."
  "corrections-and-concessions": "What Bruce got wrong."
  "acknowledgements": "The people who made this book possible."
  "verification": "How to verify the claims for yourself."
  "colophon": "How this book was made."

parts:
  "Front Matter": "The entry points — a question, a framework, and a summary."
  "The Flat": "The pop-science spine — real physics, true under all three possibilities."
  "The Record": "Personal testimony — the story as Bruce experienced it."
  "Appendices": "Reference material — physics anchors, predictions, glossary, and timeline."
```

---

## Step 8: Build and Test

```bash
cd ~/software/relinquishment
make dev
```

### What to verify:

1. **Build succeeds** — no LaTeX errors, pandoc produces HTML
2. **TOC structure** — shows: Front Matter > The Flat (spine chapters) > The Record (record chapters) > Appendices
3. **Interludes** — do NOT appear in TOC. Render between spine chapters with purple left border and italic text.
4. **Expansion test** — the test `<details class="bc-expansion">` in The Code War section works: click to expand, shows content, "Read the full story →" link is present
5. **Phone test** — open in browser, resize to phone width. Single column, no horizontal scroll, expansion tap works.
6. **Part collapsing** — "The Flat" and "The Record" collapse/expand correctly
7. **Guardian interlude styling** — purple border, italic, distinct from blockquotes and chapter borders
8. **No orphaned old content** — the old Part I/II/III chapters are NOT included (they're still in their original directories but main.tex no longer references them)

### Known issues to watch for:

- Pandoc may generate different IDs than expected for `\part{The Flat}`. Check the actual generated HTML and update preprocess.py part detection if needed.
- The `\input` vs `\include` distinction matters for interludes — `\input` avoids .aux files and page breaks.
- If pandoc doesn't handle `\label{spine:...}` labels with colons, switch to hyphens: `spine-the-flat` instead of `spine:the-flat`.

---

## Step 9: Commit

One commit. Message:

```
Plan 0143a Phase 1: Z-restructure skeleton

New directory structure (spine/ + record/), placeholder chapters,
Guardian interlude styling, B/C expansion mechanic CSS, updated
TOC/parts. No content moved — structure only.
```

---

## What NOT to Do

- Do NOT move any existing chapter content. Placeholders only.
- Do NOT write Guardian interludes. Placeholders only (Phase 2).
- Do NOT write expansion hooks. One test only (Phase 1).
- Do NOT delete or modify existing chapter files.
- Do NOT touch the appendix, back matter, or front matter files (except main.tex include order).
- Do NOT improve, refactor, or clean up existing code. Structure only.

---

*Plan 0143a created S54, 2026-04-07. Generator executes. Auditor verifies build artifact.*
