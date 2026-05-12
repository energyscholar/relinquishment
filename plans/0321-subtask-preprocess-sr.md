# Subtask: SVG-055/056 + Accordion Injection for Scientific Revolutions

**Output:** Add `inject_sr_illustrations(html_path)` to
`build/preprocess.py`, injecting SVG-055 (spectrum), SVG-056 (fork diagram),
Section 3 accordion, PhD seed accordions, and required CSS.
**Commit:** `Plan 0321: preprocess.py — SVG-055/056 + accordion injection for Scientific Revolutions`
**Read first:** This spec, then:
- `build/images/scientific-revolutions-chapter.html` (SVG source of truth)
- `build/preprocess.py` lines 3551–3620 (`inject_chapter_puzzles` — file-read pattern)
- `build/preprocess.py` lines 4340–4360 (pipeline)
- `build/preprocess.py` lines 2461–2514 (`inject_flat_diagram` — marker pattern)

## Context

The build pipeline runs `preprocess.py --fix-html` AFTER pandoc converts
.tex → HTML. By the time our function runs, tooltip spans and concept symbols
are already injected. Markers must work in post-processed HTML.

SVG-054 (the Kuhn animation) is already injected by `inject_sr_animation()`
added in the previous subtask. This subtask adds the remaining visual
elements: the expert consensus spectrum (SVG-055 with click-to-play JS),
the consequence fork diagram (SVG-056), and accordion wrapping.

---

## Architecture: File-Read Extraction

Follow the `inject_chapter_puzzles` pattern: read the standalone chapter
HTML at build time, extract SVG content by regex, inject inline.

**Source file:** `REPO / 'build' / 'images' / 'scientific-revolutions-chapter.html'`

**Missing-file guard:**
```python
src_path = REPO / 'build' / 'images' / 'scientific-revolutions-chapter.html'
if not src_path.exists():
    print("  WARNING: scientific-revolutions-chapter.html not found, skipping SR illustrations")
    return
```

---

## Extraction from Standalone HTML

### SVG-056 (static fork diagram, ~64 lines)
```python
m = re.search(r'(<!-- SVG-056.*?</svg>)', src, re.DOTALL)
svg056 = m.group(1)
```
Wrap in `<figure>`:
```html
<figure id="fig-consequence-fork" class="inline-svg" style="text-align:center;margin:1.5em auto;">
{svg056}
<figcaption style="font-size:0.85em;color:#908878;margin-top:0.3em;font-style:italic;">
Same evidence. Same silence. Different futures.</figcaption>
</figure>
```

### SVG-055 (animated spectrum + JS, ~212 lines)
The spectrum lives inside `<details open class="svg-panel">` with a
`<script>` block immediately after:
```python
start = src.find('<details open class="svg-panel">')
end_details = src.find('</details>', start) + len('</details>')
script_start = src.find('<script>', end_details)
script_end = src.find('</script>', script_start) + len('</script>')
svg055_block = src[start:script_end]
```
This extracts the complete unit: `<details>` wrapper + SVG + caption +
`</details>` + `<script>` IIFE.

### CSS
Extract the relevant CSS rules from the standalone `<style>` block.
Only need these rules (NOT the full standalone CSS — the standalone has
chapter-level CSS we don't want):

```css
/* SVG-055/056 styles (Plan 0321) */
@keyframes gold-pulse {
  0%, 100% { filter: drop-shadow(0 0 3px rgba(212,160,23,0.3)); }
  50% { filter: drop-shadow(0 0 8px rgba(212,160,23,0.7)); }
}
.gold-marker { animation: gold-pulse 2s ease-in-out infinite; }
.svg-panel { margin: 1rem 0; border-left: 2px solid rgba(212,160,23,0.2); padding-left: 1rem; }
.svg-panel summary { cursor: pointer; color: #c8b898; font-style: italic; font-size: 0.95rem; margin-bottom: 0.5rem; }
.svg-panel .caption { font-size: 0.85em; color: #908878; margin: 0.3rem 0 0.5rem; }
.phd-seed-section { margin: 1rem 0; }
.phd-seed-section summary { cursor: pointer; color: #5c7c9c; font-style: italic; font-size: 0.85rem; }
.phd-seed-section summary:hover { color: #7c9cbc; }
```

Define this CSS as a Python string constant (small, ~12 lines). Inject
before `</head>` in a `<style>` block.

Note: `.tech-section` CSS already exists in preprocess.py (line 901).
Do NOT duplicate it.

---

## Markers and Insertion Points

**CRITICAL:** Pandoc wraps long lines. All markers below have been verified
to survive pandoc wrapping in the current built HTML. Do NOT use longer
phrases without verifying they appear on a single line.

All markers are verified unique within the chapter when found via
`_find_in_chapter(text, 'spine:scientific-revolutions', marker)`.

### SVG-056 insertion
**Marker:** `Neither is a consolation`
**Algorithm:** Find marker → find next `</p>` → insert SVG-056 figure after `</p>`

### SVG-055 insertion
**Insert immediately after SVG-056** (append to the same insertion).

### Section 3 accordion
**Start marker:** `set theory.</strong>`
**End marker:** `let alone studied`
**Algorithm:**
1. Find start marker via `_find_in_chapter`
2. Search backwards from start marker for `<p` (the opening of the first paragraph)
3. Find end marker via `_find_in_chapter`
4. Find next `</p>` after end marker
5. Extract the range (4 paragraphs)
6. Wrap in:
```html
<details class="tech-section">
<summary>The four converging research programs</summary>
{four paragraphs}
</details>
```

### PhD seed accordions
Three blockquotes, each identified by a unique marker:

| # | Marker | Verified unique in chapter |
|---|--------|---------------------------|
| 1 | `feasibility study` | Yes (×1) |
| 2 | `terminological paper` | Yes (×1) |
| 3 | `bibliometric study` | Yes (×1) |

**Algorithm for each:**
1. Find marker via `_find_in_chapter`
2. Search backwards for `<blockquote`
3. Search forward for `</blockquote>`
4. Replace the blockquote with:
```html
<details class="phd-seed-section">
<summary>Research opportunity</summary>
{original blockquote}
</details>
```

**Process in REVERSE document order** (3, 2, 1) so earlier insertions
don't shift positions of later markers.

---

## Idempotency

**All operations MUST be safe to run multiple times.** Guards:

- **CSS:** `if 'gold-pulse' in text:` → skip CSS injection
- **SVG-056:** `if 'id="svg056"' in text:` → skip SVG-056
- **SVG-055:** `if 'id="svg055"' in text:` → skip SVG-055
- **Section 3 accordion:** `if 'four converging research programs' in text:` → skip
- **PhD seeds:** For each, `if 'phd-seed-section' in text[bq_start-50:bq_start]:` → skip that one

Check ALL guards at the top. If everything is already present, return early.

---

## Execution Order

1. **CSS** — into `<head>` (position-independent)
2. **PhD seed wrapping** — reverse order (modifies existing blockquotes in-place)
3. **Section 3 accordion** — modifies existing paragraphs in-place
4. **SVG-056 + SVG-055** — inserts new content after "consolation prize" paragraph

Steps 2-3 wrap existing content (positions shift but markers below them
are unaffected because we process bottom-up). Step 4 inserts after the
markers used in steps 2-3, so no conflict.

---

## Pipeline Position

Add after `inject_sr_animation` (SVG-054), before `inject_chapter_puzzles`:

```python
        inject_sr_illustrations(sys.argv[2])
```

Must run AFTER:
- `fix_html_toc` (chapter-section wrapping for `_find_in_chapter`)
- `inject_sr_animation` (SVG-054 — so we don't collide)
- Tooltip/concept-symbol injection (markers depend on post-processed HTML)

Must run BEFORE:
- `collapse_tech_sections` (defensive — no tech-collapse.yaml entry for
  this chapter, but ordering prevents double-wrap)

**Check pipeline ordering:** `inject_sr_animation` was added in the previous
subtask. Our new function should go immediately after it.

---

## Print Diagnostics

```
  SR illustrations: CSS injected
  SR illustrations: SVG-056 fork diagram injected
  SR illustrations: SVG-055 spectrum + click-to-play injected
  SR illustrations: Section 3 accordion applied
  SR illustrations: PhD seed 1/3 wrapped
  SR illustrations: PhD seed 2/3 wrapped
  SR illustrations: PhD seed 3/3 wrapped
```

---

## Do NOT

- Embed SVGs as Python string constants (use file-read extraction)
- Modify the standalone chapter HTML (it's the source of truth)
- Duplicate `.tech-section` CSS (already exists at preprocess.py line 901)
- Use long marker strings that pandoc might line-wrap
- Modify `inject_sr_animation` or any other existing function
- Add entries to `tech-collapse.yaml`

## Testing

```bash
cd ~/software/relinquishment && make html 2>&1 | grep -i 'sr illustration\|warning\|error'
```

Open `docs/Relinquishment.html`, navigate to Scientific Revolutions:
1. SVG-056 fork diagram renders after "Neither is a consolation prize"
2. SVG-055 spectrum renders with "Click to play" hint
3. Click → animation plays, click → pauses, click → resumes
4. Section 3 has collapsed "The four converging research programs" accordion
5. Three "Research opportunity" collapsed sections visible
6. No console errors
7. Run `make html` again — output identical (idempotency)

## Report

Confirm: function added, pipeline wired, both SVGs render, JS engine works,
accordion opens/closes, PhD seeds open/close, idempotent on double-run.
