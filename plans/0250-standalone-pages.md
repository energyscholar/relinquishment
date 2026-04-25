# Plan 0250 — Standalone Pages: Tooltip Viewer + Author Hub

**Auditor:** Argus (S63)
**Date:** 2026-04-25
**Status:** COMPLETE — executed S63
**Priority:** Medium — unblocks Bruce's tooltip editing workflow
**Annealed:** 4 passes (medium/medium/low/low)

---

## Problem

Bruce reads the book on his phone. When he spots a tooltip that's wrong,
he cannot copy it and cannot see its ID. There is no way to report a
tooltip problem with enough information for Argus to fix it. The
manuscript has 126 hover entries (30 with rich SVG panels). Bruce needs
a single page showing every tooltip with its UID, a functioning hover
demo, and copyable text.

Additionally, the project now has multiple standalone utility pages with
no central index.

---

## Existing Standalone Pages

| Page | Location | Build target |
|------|----------|-------------|
| Puzzle Preview | `docs/downloads/puzzles.html` | `make puzzles` |
| SVG Gallery | `docs/gallery.html` | `make svg-sheet` |

Style convention: self-contained HTML, inline CSS/JS, Georgia serif,
#1a5276 accent, max-width 42-50em, mobile-friendly.

---

## Phase 1: Tooltip Viewer Page

### Card Layout

Every entry from `hover-definitions.yaml`, separated by `<hr>`:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
wormholes                        [rich panel]

  Hover/tap: wormholes  ← functioning tooltip

  Text (copyable):
  ┌──────────────────────────────────────┐
  │ Not the sci-fi kind. Spacetime       │
  │ wormholes (Interstellar) fold        │
  │ spacetime itself — mass and all...   │
  └──────────────────────────────────────┘

  [Rich panel rendered visibly below]

  Target: #wormhole-disambiguation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Spec

- **Source:** `build/hover-definitions.yaml` (canonical, 126 entries)
- **Build script:** `build/build-tooltips.py`
- **Output:** `docs/downloads/tooltips.html`
- **Makefile target:** `make tooltips`

**Per entry:**
- UID in monospace `<code>` (the YAML key or `hover_id` field)
- Badge: `[rich panel]` or `[text]`
- Functioning hover: `<span class="hover-term" data-hover="...">` so
  tap/hover shows the tooltip exactly as in the book
- Copyable text: `<blockquote>` with the plain-text content, selectable
  on mobile Chrome
- If entry has `html`: rich panel rendered visibly below the text
- If entry has `target`: shown as a link
- `<hr>` between entries

**Page structure:**
- Header with entry count ("126 hover definitions, 30 with rich panels")
- Search/filter box — filters on UID and text content
- Alphabetical listing (no category grouping — simpler, search handles it)
- Anchor for each entry (UID as fragment ID) so Bruce can link directly

**Hover JS:**
- Extract only the hover functions (`showPanel`, `positionPanel`,
  `dismissPanel`) from `build/reader.js` — NOT the full reader
  (breadcrumbs, expand/collapse, etc. are irrelevant here)
- Include the hover-data as an inline `<script type="application/json">`
  block, same pattern as the main book HTML
- Must work on mobile (tap to show, tap elsewhere to dismiss)

**YAML handling:**
- `yaml.safe_load()` resolves YAML anchors automatically — entries using
  `<<: *anchor` will appear as resolved dicts. Deduplicate by checking
  if two entries share identical `text` AND `html` AND `target`. Show
  each distinct UID but note shared content.
- Handle both plain-string entries (`term: "definition"`) and dict
  entries (`term: { text: "...", hover_id: "...", html: "..." }`)
- Escape HTML entities in the copyable text block

**Known limitation:** Some rich panels contain nested `<span
class="hover-term">` elements. These nested hovers won't function on the
standalone page (they'll render as plain text). Acceptable — the primary
purpose is viewing and copying, not full interactivity.

**Pattern to follow:** `build/build-puzzles.py` (reads YAML, generates
standalone HTML with inline CSS/JS).

### Acceptance Criteria

- [ ] `make tooltips` produces `docs/downloads/tooltips.html`
- [ ] Every entry in `hover-definitions.yaml` appears (no duplicates
  from alias resolution)
- [ ] Each entry shows its UID in monospace
- [ ] Hover/tap on the term shows the same tooltip as in the book
- [ ] Tooltip text is selectable and copyable on mobile Chrome
- [ ] Rich panels render visibly (not just on hover)
- [ ] Search box narrows visible entries by UID or text content
- [ ] Style matches existing standalone pages (Georgia, #1a5276, 42em)

---

## Phase 2: Author Hub Page

**Location:** `docs/tools.html`

Static HTML, hand-maintained. Links to all standalone pages:

```
RELINQUISHMENT — Author Tools

  Tooltip Viewer    View, search, and copy all 126 hover definitions
  Puzzle Preview    Interactive chapter-end puzzles
  SVG Gallery       All 24 diagrams with metadata
```

- Same style convention (Georgia, #1a5276, mobile-friendly)
- No JS, no build script — add entries by copying a `<div>` block
- New standalone pages get added here as they're built

### Acceptance Criteria

- [ ] Lists all standalone pages with working links
- [ ] Works on mobile
- [ ] Easy to extend

---

## Build Integration

```makefile
# --- Tooltip viewer (standalone, Plan 0250) ---
tooltips:
	python3 build/build-tooltips.py
	@echo "Open docs/downloads/tooltips.html or push to website."
```

Hub page is static — no Makefile target needed.

---

## Phasing

| Phase | Deliverable | Effort |
|-------|-------------|--------|
| 1 | Tooltip viewer | ~2h Generator |
| 2 | Author hub page | ~20min Generator (same session) |

---

*Plan written by Argus (Auditor), S63. Annealed 4 passes.*
