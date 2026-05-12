# Subtask: Inject SVG-054 Kuhn Animation into Built Book

**Output:** Add `inject_sr_animation(html_path)` to `build/preprocess.py`,
embedding the interactive Kuhn framework animation (SVG-054) into the
Scientific Revolutions chapter during build.
**Commit:** `Plan 0321: inject SVG-054 Kuhn animation into build pipeline`
**Read first:** This spec, then:
- `build/images/scientific-revolutions-draft.html` (the animation source, 1944 lines)
- `build/preprocess.py` lines 3551–3620 (`inject_chapter_puzzles` — file-read extraction pattern)
- `build/preprocess.py` lines 4340–4360 (pipeline)

## Context

SVG-054 is a 1944-line standalone HTML file containing the animated Kuhn
framework teaching diagram. Eight historical revolutions play through a
five-phase cycle (Normal Science → Anomaly → Crisis → Revolution → New
Paradigm). It has a scrubber bar, play/pause, fullscreen button, and a
mobile teaser fallback.

The standalone chapter preview (`scientific-revolutions-chapter.html`)
embeds it via `<iframe src="scientific-revolutions-draft.html">`. But the
book builds as a single self-contained HTML file — no iframes. The
animation must be inlined.

The .tex has a `\begin{figure}` with commented-out `\includegraphics`.
Pandoc drops it entirely — the built book has NO figure, NO animation,
NO placeholder between "What follows is an application." and "The Current
Paradigm" heading.

---

## Architecture: File-Read Extraction

Do NOT embed the animation as a Python constant (1944 lines is too large).
Instead, follow the `inject_chapter_puzzles` pattern: read the standalone
HTML at build time, extract CSS/HTML/JS, inject inline.

### Source file
`REPO / 'build' / 'images' / 'scientific-revolutions-draft.html'`

### What to extract

The standalone file has this structure:
```
Lines 7–84:    <style> ... </style>     (CSS)
Lines 86–167:  <body> ... </body>       (HTML: two divs + SVG)
Lines 169–1942: <script>(function(){...})();</script>  (JS: IIFE)
```

Use regex extraction, matching the `inject_chapter_puzzles` helpers:

```python
def extract_sr_css(src):
    m = re.search(r'<style>(.*?)</style>', src, re.DOTALL)
    return m.group(1) if m else ''

def extract_sr_body(src):
    m = re.search(r'<body>(.*?)<script>', src, re.DOTALL)
    return m.group(1).strip() if m else ''

def extract_sr_js(src):
    m = re.search(r'<script>(.*?)</script>', src, re.DOTALL)
    return m.group(1) if m else ''
```

### CSS modification

The standalone CSS contains `body { margin: 0; background: #1a1a2e; ... }`.
This MUST be removed — it would override the book's body styles.

After extraction, strip the `body { ... }` rule:
```python
css = re.sub(r'body\s*\{[^}]*\}', '', css)
```

All other CSS classes are `sr-`prefixed (`.sr-full`, `.sr-fs-btn`,
`.sr-teaser`, etc.) — no conflict with book styles.

Also add width constraint for the text column:
```css
.sr-full { max-width: 800px; margin: 0 auto; }
```

### HTML wrapping

Wrap the extracted body HTML in a figure:
```html
<figure id="fig-kuhn-animation" class="inline-svg sr-animation"
  style="text-align:center;margin:1.5em auto;">
{extracted body HTML}
<figcaption style="font-size:0.85em;color:#666;margin-top:0.3em;">
Eight scientific revolutions mapped to Kuhn's framework. In the
interactive edition, press play to watch each revolution unfold.
</figcaption>
</figure>
```

## Insertion Point

**Marker text:** `Watch the animation first`

**IMPORTANT:** Do NOT use "What follows is an application" — pandoc wraps
long lines and splits that phrase across two lines, breaking `text.find()`.
Use "Watch the animation first" which stays on one line (verified in built HTML).

**Algorithm:**
1. Use `_find_in_chapter(text, 'spine:scientific-revolutions', 'Watch the animation first')` 
2. Find the next `</p>` after the marker
3. Insert the figure + script after that `</p>`, before the next heading

In the current built HTML this produces:
```
...Watch the animation first. What follows is an
application.</p>
>>> INSERT HERE <<<
<h3 class="unnumbered" id="spine:sr-current-paradigm">The Current Paradigm</h3>
```

## Injection Assembly

Insert in this order at the insertion point:
1. `<style>` block with modified CSS
2. Figure with extracted HTML body
3. `<script>` block with extracted JS

The `<style>` could also go in `<head>` — either works. Placing it adjacent
to the figure is simpler and matches how other inline SVGs handle their CSS
(e.g., magnetosphere diagrams include scoped styles near the SVG).

## Idempotency

**Guard:** Before any injection, check:
```python
if 'id="sr-full"' in text:
    print("  SR animation: already present, skipping")
    return
```

The ID `sr-full` is unique to this animation and does not appear elsewhere
in the book.

## Pipeline Position

Add after the other illustration inject functions. Insert at the appropriate
line (after `inject_promoted_illustrations`, near the other `inject_*`
calls):

```python
        inject_sr_animation(sys.argv[2])
```

This must run AFTER chapter-section wrapping (`fix_html_toc`) so that
`_find_in_chapter` can locate the chapter boundaries.

## ID Uniqueness

All IDs in SVG-054 have been verified unique across the book:
`main`, `stage`, `glow`, `glow-strong`, `golden-flash`, `center-stage`,
`loop-labels`, `cycle-path`, `you-are-here`, `title-bar`, `title-line1`,
`title-line2`, `title-line3`, `title-strike`, `year-display`, `scrubber`,
`progress-bar`, `play-btn`, `play-icon`, `scrubber-dots`, `sr-full`,
`sr-fs-btn`, `sr-teaser`, `sr-teaser-btn`.

Zero collisions with existing book HTML (verified via grep on
`docs/Relinquishment.html`).

## JS Safety

The script is wrapped in an IIFE: `(function() { ... })();`
No global variables. All `document.getElementById()` calls reference
SVG-054-specific IDs listed above. No conflicts with book JS or other
SVG scripts.

## Mobile Handling

The animation has built-in mobile support:
- Desktop: inline `.sr-full` div with SVG, fullscreen button
- Mobile (<768px): `.sr-teaser` with static diagram + "Play Fullscreen" button

Both are extracted from the body HTML. The CSS media query handles the
switch. No additional mobile work needed.

## Source File Dependency

The build now depends on `build/images/scientific-revolutions-draft.html`.
If the file is missing, print a warning and return (don't break the build):
```python
sr_path = REPO / 'build' / 'images' / 'scientific-revolutions-draft.html'
if not sr_path.exists():
    print("  WARNING: scientific-revolutions-draft.html not found, skipping SR animation")
    return
```

## Do NOT

- Embed the animation as a Python string constant (too large — 1944 lines)
- Use an `<iframe>` (book is single-file, no external references)
- Modify the animation source file (`scientific-revolutions-draft.html`)
- Modify the chapter .tex file
- Add the `body { ... }` CSS rule (would override book styles)
- Change any existing function in preprocess.py

## Testing

After implementing:
```bash
cd ~/software/relinquishment && make html 2>&1 | grep -i 'sr animation\|warning\|error'
```

Open `docs/Relinquishment.html`, navigate to Scientific Revolutions chapter:
1. Animation container visible after "What follows is an application."
2. Play button works — revolutions animate through the five-phase cycle
3. Scrubber dots are clickable
4. Fullscreen button works
5. On mobile viewport (resize to <768px): teaser shows with "Play Fullscreen"
6. No console errors
7. No style bleeding (book body styles unaffected)

## Report

Confirm: function added, pipeline wired, animation renders, play/pause works,
scrubber works, fullscreen works, no CSS conflicts, idempotent (running
`make html` twice produces identical output).
