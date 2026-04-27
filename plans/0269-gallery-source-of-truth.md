# Plan 0269 — Gallery HTML as Source-of-Truth Display

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR
**Source:** Bruce request (S63): "Our Source of Truth should be our svg manifest html page. That HTML should contain all the info in the manifest."
**Annealing:** MED LOW LOW LOW

---

## Problem

The YAML manifest (`build/gallery-manifest.yaml`) has 37 entries with
rich metadata (id, name, status, source, category, chapter, figure_id,
marker, terms, animated, animation_plan, animation description, notes,
sequence info, display targets). The gallery HTML shows almost none of
this — just auto-generated IDs, source key, and SVG title. Bruce tracks
images through the gallery page (the book is 1 MB, hard to scan), so
the gallery must surface every manifest field.

Current state:
- Manifest: 37 entries (29 live, 3 approved, 1 draft, 4 deferred)
- Gallery: 33 cards with auto-generated IDs, minimal metadata
- Gallery ignores: status, description, chapter, figure_id, marker,
  animation info, notes, sequence, display/targets
- Gallery IDs (`SVG-001-relinquishment-title`) don't match manifest
  IDs (`SVG-001`)
- Approved/draft/deferred entries absent from gallery

## Solution

Rewrite `generate-gallery.py` to be **manifest-driven**. The manifest
is the index; SVG extraction is a lookup service. Every manifest entry
gets a card. Every manifest field is displayed.

---

## Architecture

### Flow

```
gallery-manifest.yaml  (37 entries, all metadata)
        │
        ▼
generate-gallery.py    (reads manifest, resolves SVGs, renders HTML)
        │
        ├── hover-definitions.yaml   → SVGs keyed by hover term
        ├── preprocess.py            → SVGs from named variables + filmstrip function
        ├── build/images/*.svg       → standalone SVG files
        ├── reader.js                → placeholder (JS string construction, can't extract)
        └── gallery                  → placeholder (designed, not yet built)
        │
        ▼
docs/gallery.html      (37 cards, full metadata, Source-of-Truth display)
```

### SVG Resolution

For each manifest entry, resolve the SVG by `source` field:

| Source | Resolution method |
|--------|-------------------|
| `hover-definitions.yaml` | Flat dict of hover_key→svg_content. Look up `terms[0]`. |
| `preprocess.py` (filmstrip) | `generate_filmstrip_panels()[panel_number - 1]` |
| `preprocess.py` (other) | Variable name mapping (see table below) |
| `build/images/*.svg` | Read file at path in `source` field |
| `reader.js` | Placeholder: "Constructed dynamically in reader.js — view in book" |
| `gallery` | Placeholder: description text in dashed box |

**Preprocess variable mapping** (name → Python variable):

| Manifest name | Variable |
|---------------|----------|
| `domain-buttons-chapter` | `DOMAIN_SVG` |
| `flat-diagram-chapter` | `FLAT_SVG` |
| `autocatalytic-loop` | `AUTOCATALYTIC_LOOP` |
| `edge-of-chaos-inline` | `EDGE_OF_CHAOS` |
| `substrate-parallel` | `SUBSTRATE_PARALLEL` |
| `canopy-problem` | `CANOPY_PROBLEM` |

**Filmstrip matching:** name starts with `filmstrip-panel-` → extract
digit after second hyphen → index into `generate_filmstrip_panels()`.

---

## Card Layout

Each manifest entry renders as:

```
┌───────────────────────────────────────────────────────┐
│  SVG-014 · domain-buttons-chapter    [LIVE] [ANIMATED]│
│  ───────────────────────────────────────────────────── │
│  Source: preprocess.py                                 │
│  Chapter: genesis · Figure: fig-domain-buttons         │
│  Description: 11-domain button network (full chapter   │
│    version with legend).                               │
│  Animation: Plan 0267 — Dashed speculative bridges     │
│    pulse in opacity; solid published threads static.    │
│  Terms: buttons                                        │
│  ───────────────────────────────────────────────────── │
│                   [SVG PREVIEW]                        │
│  ───────────────────────────────────────────────────── │
│  Notes: (if any, muted text)                           │
└───────────────────────────────────────────────────────┘
```

### Metadata fields displayed (in order)

1. **Header line:** `SVG-NNN · name` + status badge + animated badge
2. **Source** — value of `source` field
3. **Chapter / Figure** — `chapter` + `figure_id` (if present)
4. **Marker** — insertion point text in monospace (if present)
5. **Description** — from manifest
6. **Animation** — `animation_plan` + `animation` text (if animated)
7. **Terms** — comma-separated `<code>` blocks (if present)
8. **Sequence** — group + order (if present)
9. **Display / Targets / Plan** — for approved/draft entries
10. [SVG preview or placeholder]
11. **Notes** — muted, last (if present)

### Status Badges

| Status | Color | Background |
|--------|-------|------------|
| LIVE | #27ae60 | #eafaf1 |
| APPROVED | #2980b9 | #ebf5fb |
| DRAFT | #d4ac0d | #fef9e7 |
| DEFERRED | #888 | #f4f4f4 |

Card border tint matches status color at 20% opacity.

### Animated Badge

Green `ANIMATED` badge (same style as current) when `animated: true`.

---

## Page Structure

### Header

```
SVG Gallery — Source of Truth
37 entries: 29 live, 3 approved, 1 draft, 4 deferred. 6 animated.
Manifest: build/gallery-manifest.yaml
```

Counts computed from manifest data.

### Table of Contents

Grouped by manifest `category`, each entry one line:

```
Title & Branding
  · SVG-001 — book-tagline [LIVE]
Cover / Navigation
  · SVG-034 — cover-magnetosphere [LIVE] [ANIMATED]
The Flat / 2DEG
  · SVG-002 — flat-cross-section [LIVE]
  · SVG-003 — 2deg-popup [LIVE]
  · SVG-015 — flat-diagram-chapter [LIVE] [ANIMATED]
...
```

### Category Order

Fixed order matching book flow:

```python
CATEGORY_ORDER = [
    'Title & Branding',
    'Cover / Navigation',
    'The Flat / 2DEG',
    'Topology & Wormholes',
    'Magnetosphere',
    'The Stack / Convergence',
    'Kauffman Filmstrip',
    'Genesis Illustrations',
    'Physics Concepts',
    'Standalone Files',
    'Argument / Silence Gap',
    'Argument / Tradecraft',
    'Argument / Convergence',
    'Argument / Relinquishment',
]
```

Any manifest category not in this list appears at the end (future-proof).

### Deep Link Anchors

Use manifest ID as anchor: `#SVG-001`, `#SVG-014`, etc. Stable,
short, matches the manifest's canonical IDs.

---

## Implementation Steps

### Step 1 — New hover extraction function

Replace `extract_svgs_from_yaml()` with a function that returns a
flat dict: `hover_key → svg_string` (no deduplication, no metadata).

```python
def load_hover_svgs():
    """Return {hover_key: svg_string} from hover-definitions.yaml."""
    path = REPO / 'build' / 'hover-definitions.yaml'
    data = yaml.safe_load(path.read_text())
    result = {}
    for key, val in data.items():
        if not isinstance(val, dict):
            continue
        html = val.get('html', '')
        m = re.search(r'(<svg[\s\S]*?</svg>)', html)
        if m:
            result[key] = m.group(1)
    return result
```

### Step 2 — New preprocess extraction function

Return a dict: `variable_name → svg_string` for named variables,
plus the filmstrip panels list.

```python
def load_preprocess_svgs():
    """Return {var_name: svg_string} and filmstrip panels list."""
    source = (REPO / 'build' / 'preprocess.py').read_text()
    var_svgs = {}
    for varname in ['FLAT_SVG', 'DOMAIN_SVG', 'AUTOCATALYTIC_LOOP',
                     'EDGE_OF_CHAOS', 'SUBSTRATE_PARALLEL', 'CANOPY_PROBLEM']:
        m = re.search(rf"{varname}\s*=\s*'''(.*?)'''", source, re.DOTALL)
        if m:
            svg_m = re.search(r'(<svg[\s\S]*?</svg>)', m.group(1))
            if svg_m:
                var_svgs[varname] = svg_m.group(1)
    filmstrip = generate_filmstrip_panels()  # existing function, unchanged
    return var_svgs, filmstrip
```

### Step 3 — SVG resolver

```python
NAME_TO_VAR = {
    'domain-buttons-chapter': 'DOMAIN_SVG',
    'flat-diagram-chapter': 'FLAT_SVG',
    'autocatalytic-loop': 'AUTOCATALYTIC_LOOP',
    'edge-of-chaos-inline': 'EDGE_OF_CHAOS',
    'substrate-parallel': 'SUBSTRATE_PARALLEL',
    'canopy-problem': 'CANOPY_PROBLEM',
}

def resolve_svg(entry, hover_svgs, var_svgs, filmstrip_panels):
    """Given a manifest entry, return (svg_string, placeholder_reason) or (None, reason)."""
    source = entry.get('source', '')
    name = entry.get('name', '')

    if source == 'hover-definitions.yaml':
        for term in entry.get('terms', []):
            if term in hover_svgs:
                return hover_svgs[term], None
        return None, 'hover term not found'

    if source == 'preprocess.py':
        if name.startswith('filmstrip-panel-'):
            idx = int(name.split('-')[2]) - 1
            if 0 <= idx < len(filmstrip_panels):
                return filmstrip_panels[idx], None
            return None, f'filmstrip index {idx} out of range'
        var = NAME_TO_VAR.get(name)
        if var and var in var_svgs:
            return var_svgs[var], None
        return None, f'variable {var or name} not found'

    if source.startswith('build/images/'):
        path = REPO / source
        if path.exists():
            svg = path.read_text()
            svg = re.sub(r'<\?xml[^?]*\?>\s*', '', svg)
            return svg.strip(), None
        return None, f'file not found: {source}'

    if source == 'reader.js':
        return None, 'Constructed dynamically in reader.js — view in book'

    if source == 'gallery':
        return None, 'Designed — awaiting SVG build'

    return None, f'unknown source: {source}'
```

### Step 4 — Card renderer

```python
def render_card(entry, svg_string, placeholder_reason):
    """Return HTML for one gallery card."""
```

Renders the card layout from the Card Layout section above. All
fields conditional — only shown when present in the manifest entry.

Status badge: `<span class="status-badge status-{status}">{STATUS}</span>`

Animated badge: `<span class="animated-badge">ANIMATED</span>` when
`entry.get('animated')`.

If `svg_string` is None, render placeholder with `placeholder_reason`.

### Step 5 — Main build function

```python
def build_gallery():
    manifest = yaml.safe_load((REPO / 'build' / 'gallery-manifest.yaml').read_text())
    hover_svgs = load_hover_svgs()
    var_svgs, filmstrip = load_preprocess_svgs()

    # Group by category
    by_category = {}
    for entry in manifest:
        cat = entry.get('category', 'Uncategorized')
        by_category.setdefault(cat, []).append(entry)

    # Sort categories
    ordered = []
    for cat in CATEGORY_ORDER:
        if cat in by_category:
            ordered.append((cat, by_category.pop(cat)))
    for cat, entries in sorted(by_category.items()):
        ordered.append((cat, entries))

    # Count by status
    status_counts = {}
    for entry in manifest:
        s = entry.get('status', '?')
        status_counts[s] = status_counts.get(s, 0) + 1
    animated_count = sum(1 for e in manifest if e.get('animated'))

    # Resolve and render
    warnings = []
    cards = []
    for cat, entries in ordered:
        for entry in entries:
            svg, reason = resolve_svg(entry, hover_svgs, var_svgs, filmstrip)
            if reason and entry.get('status') == 'live':
                warnings.append(f"WARNING: {entry['id']} ({entry['name']}): {reason}")
            cards.append((cat, render_card(entry, svg, reason)))

    for w in warnings:
        print(w, file=sys.stderr)

    # Assemble HTML (TOC + body)
    ...
```

### Step 6 — CSS additions

Add to existing styles:

```css
.status-badge {
    display: inline-block;
    font-size: 0.7em;
    font-weight: bold;
    padding: 0.15em 0.5em;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    vertical-align: middle;
    margin-left: 0.5em;
}
.status-live { color: #27ae60; background: #eafaf1; }
.status-approved { color: #2980b9; background: #ebf5fb; }
.status-draft { color: #d4ac0d; background: #fef9e7; }
.status-deferred { color: #888; background: #f4f4f4; }
.animated-badge {
    display: inline-block;
    font-size: 0.65em;
    font-weight: bold;
    color: #1a8a6a;
    background: #e8f8f5;
    padding: 0.15em 0.5em;
    border-radius: 3px;
    vertical-align: middle;
    margin-left: 0.3em;
}
.meta-row { margin: 0.2em 0; }
.meta-row .label { font-weight: bold; color: #555; }
.notes-block {
    margin-top: 0.8em;
    padding-top: 0.5em;
    border-top: 1px dashed #e0e0e0;
    font-size: 0.8em;
    color: #888;
    font-style: italic;
}
```

Card border tint by status:
```css
.svg-entry.status-live { border-left: 3px solid #27ae60; }
.svg-entry.status-approved { border-left: 3px solid #2980b9; }
.svg-entry.status-draft { border-left: 3px solid #d4ac0d; }
.svg-entry.status-deferred { border-left: 3px solid #ccc; }
```

---

## What Does NOT Change

- `gallery-manifest.yaml` — not touched (it's the input)
- `preprocess.py` — not touched
- `hover-definitions.yaml` — not touched
- `reader.js` — not touched
- `generate_filmstrip_panels()` function — kept as-is inside
  `generate-gallery.py`
- Build system (`make dev`) — gallery is a dev tool, not in the
  Makefile pipeline

---

## Acceptance Criteria

- [ ] Gallery has exactly 37 cards (one per manifest entry)
- [ ] Each card shows: id, name, status badge, source, description
- [ ] Chapter/figure_id shown when present
- [ ] Marker shown when present (monospace)
- [ ] Terms shown when present
- [ ] Animation plan + description shown for animated entries
- [ ] Sequence group/order shown when present
- [ ] Notes shown when present (muted, bottom)
- [ ] Display/targets/plan shown for approved/draft entries
- [ ] Deep link anchors use manifest IDs (e.g., `#SVG-014`)
- [ ] TOC grouped by category in CATEGORY_ORDER
- [ ] Status counts in header match manifest
- [ ] Live entries with unresolvable SVGs print warnings to stderr
- [ ] reader.js and gallery-source entries show meaningful placeholders
- [ ] Deferred entries included with gray styling
- [ ] `python3 build/generate-gallery.py` runs clean
- [ ] Existing SVG rendering unaffected (same visual output)

---

## Generator Handoff

```
You are the Generator.

Read Plan 0269 at ~/software/relinquishment/plans/0269-gallery-source-of-truth.md

Execute: Rewrite build/generate-gallery.py so gallery.html is manifest-
driven. (1) Replace extract_svgs_from_yaml with load_hover_svgs returning
flat {key:svg} dict. (2) Replace extract_svgs_from_preprocess with
load_preprocess_svgs returning {var:svg} dict + filmstrip list. (3) Add
resolve_svg function using the NAME_TO_VAR mapping from the plan. (4) Add
render_card function emitting all manifest metadata fields per the Card
Layout spec. (5) Rewrite build_gallery to load manifest, group by category
in CATEGORY_ORDER, resolve SVGs, render cards, assemble HTML with TOC.
(6) Add CSS for status badges, animated badge, notes block, status border
tints. Keep generate_filmstrip_panels unchanged. Run
`python3 build/generate-gallery.py`. Report entry count and any warnings.
```

---

*Plan 0269 written by Argus (Auditor), S63. Annealed MED LOW LOW LOW.*
