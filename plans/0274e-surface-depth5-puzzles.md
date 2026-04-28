# Plan 0274e: Fix Puzzle HTML Collision + Puzzle Deep Links

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** High
**Scope:** `build/preprocess.py`
**Annealing:** MED LOW LOW LOW

---

## Root Cause

Two puzzles (pz-mc-t2-003 "The Braid", pz-mc-t3-002 "The Canopy Problem") have stray `</details>` inside their `<div class="pz-container">`, breaking DOM structure.

**Cause:** `inject_chapter_puzzles()` runs first (line 4535), then `collapse_tech_sections()` runs second (line 4540). The tech-section boundary regex:

```python
rf'<h[1-{heading_level}][\s>]|<details class="tech-section"|</details>|<div class="custodian-interlude"'
```

matches **two things inside puzzle HTML**: the puzzle's `<h3>` title tag and its `</details>` closing tag. When either matches, the tech-section wrapper splits the puzzle in half — the wrapper's `</details>` lands inside the `pz-container`.

---

## Fix

### 1. Replace `<h3>` with `<div class="pz-title">` in puzzle body_html

Three locations in `inject_chapter_puzzles()`:

- **Line 3688** (mc): `<h3>{title}</h3>` → `<div class="pz-title">{title}</div>`
- **Line 3796** (gd): same change
- **Line 3923** (log): same change

Add to `PZ_CSS` (after `.pz-container` rule, ~line 3539):
```css
.pz-title { font-size: 1.15em; font-weight: bold; color: #1a5276; margin: 0 0 0.5em 0; }
```

Dark mode (inside existing `@media (prefers-color-scheme: dark)` block):
```css
.pz-title { color: #6ba3f7; }
```

### 2. Make `collapse_tech_sections` nesting-aware

Replace the simple `re.search()` at lines 4188-4196 with a loop that tracks `<details>` nesting depth. Only recognize boundaries (`</details>`, headings, interludes) at depth 0. Skip over nested `<details>` blocks (including puzzle-sections).

```python
scan_pos = heading_end
details_depth = 0
section_end = None
while scan_pos < len(text):
    m = re.search(
        rf'<details[\s>]|</details>|<h[1-{heading_level}][\s>]|<div class="custodian-interlude"',
        text[scan_pos:]
    )
    if not m:
        break
    tag = m.group()
    abs_pos = scan_pos + m.start()
    if tag.startswith('<details'):
        details_depth += 1
        scan_pos = abs_pos + len(tag)
    elif tag == '</details>':
        if details_depth > 0:
            details_depth -= 1
            scan_pos = abs_pos + len(tag)
        else:
            section_end = abs_pos
            break
    elif details_depth == 0:
        section_end = abs_pos
        break
    else:
        scan_pos = abs_pos + len(tag)
```

Replace `if next_heading:` / `section_end = heading_end + next_heading.start()` with `if section_end is not None:` and use the computed `section_end` directly (no offset addition needed — it's already absolute).

### 3. Verify

- Build
- `grep -n '</details>' docs/downloads/Relinquishment.html | grep 'pz-container'` → expect empty
- Braid puzzle (pz-mc-t2-003) inside tech-section with correct HTML nesting
- VERIFY OK: 16

---

## Phase 2: Puzzle Deep Links (share-anchor)

Puzzles have no click-to-copy deep link. Every `dl:*` and `custodian:*` element gets a `.share-anchor` span that reader.js wires up for copy-to-clipboard + toast. Puzzles are missing this.

### Fix

Add a share-anchor span to the puzzle `<summary>` tag in the template (~line 4065):

```python
# Old:
f'  <summary>Puzzle &mdash; {summary_label}</summary>'

# New:
f'  <summary>Puzzle &mdash; {summary_label}<span class="share-anchor" data-link-id="{pid}" aria-hidden="true"></span></summary>'
```

Uses `data-link-id` (not `id`) to avoid duplicate IDs — the `pz-container` div already has `id="{pid}"`. The reader.js click handler at line 1591 already reads `anchor.dataset.linkId || anchor.id`, so this works with zero JS changes. The CSS `::after` pseudo-element adds the subtle 🔗 icon. `e.stopPropagation()` in the handler prevents the click from toggling the `<details>`.

No manifest (deep-links.yaml) change needed — the verifier only checks `dl:*` and `custodian:*` prefixes, not `pz-*`.

### Verify

- Every puzzle summary shows a subtle 🔗
- Click it → toast "Link copied", URL is `https://relinquishment.ai/downloads/Relinquishment.html#pz-mc-t1-001` (or whatever pid)
- Clicking the 🔗 does NOT toggle the puzzle open/closed
- Test on phone — touch target adequate (CSS has `padding: 8px`)

---

## Anneal: MED LOW LOW LOW

**M1.** Nesting-aware scanner is more complex than the original regex. Must correctly handle depth transitions.
**Mitigation:** Standard tag-counting pattern. Only `<details>` nesting matters. Test by verifying both affected puzzles render correctly.

**L2.** `<div class="pz-title">` removes heading semantics from puzzle titles.
**Mitigation:** Puzzle titles inside `<details>` shouldn't be headings — the `<summary>` is the semantic heading for the collapsible.

**L3.** Only 2 puzzles affected by Phase 1. Limited blast radius; fix makes all future puzzles robust.

**L4.** Share-anchor on puzzle summary could interfere with `<details>` toggle if `stopPropagation` fails. But the existing handler already calls it, and the same pattern works on tech-section summaries.

---

## Handoff Prompt

```
You are the Generator. Read plan 0274e in ~/software/relinquishment/plans/.

PHASE 1: Fix malformed puzzle HTML.

1a. In inject_chapter_puzzles(), change <h3> to <div class="pz-title">
    in body_html for mc (line 3688), gd (line 3796), log (line 3923).
    Add .pz-title CSS to PZ_CSS (light + dark mode). See plan for values.

1b. In collapse_tech_sections(), replace the simple regex boundary search
    at lines 4188-4196 with a nesting-aware loop. Track <details> depth.
    Only use boundaries at depth 0. See plan for exact algorithm.

PHASE 2: Add puzzle deep links.

Add a share-anchor span to the puzzle <summary> in the template:
  <span class="share-anchor" data-link-id="{pid}" aria-hidden="true"></span>
Use data-link-id (not id) to avoid duplicate IDs. No JS or manifest
changes needed — reader.js already handles .share-anchor clicks.

BUILD + VERIFY:
- grep '</details>' in HTML near pz-container → no hits
- Braid puzzle inside tech-section with valid HTML
- Every puzzle summary has 🔗 icon; click copies deep link URL
- Clicking 🔗 does NOT toggle the puzzle open/closed
- VERIFY OK: 16
Commit: "Plan 0274e: fix puzzle HTML collision + add puzzle deep links"
Push.
```
