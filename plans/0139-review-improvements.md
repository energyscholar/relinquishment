# Plan 0139: Review Improvements — Stack Chart + Tooltip Unification

## Context

Bruce is reviewing the HTML reader after Plans 0136-0138. Two improvements identified:
1. The Stack chart is cramped horizontally and needs interactive popups on every cell
2. The HTML has two parallel tooltip systems (`title=""` native vs `data-hover` popup panels) — unify to one

## Governing Constraints

- **The Stack is p1 text.** Popups escalate to p2 content. Keep language at 8th-grade level with concrete examples.
- **First-occurrence rule does NOT apply to the Stack chart.** The chart is a special interactive element — every cell should always be hoverable, even if the term fired earlier in reading order. This means `\hovertip{}` in LaTeX is the WRONG mechanism for the table cells. Use preprocess.py post-processing instead.
- **PDF stays clean.** No footnotes on table cells (14 footnotes on one table would be unreadable). The chart popups are HTML-only.

## Files

All work in `/home/bruce/software/relinquishment/`.

| File | Edit type |
|------|-----------|
| `build/html.css` | Stack chart width, hover-nav styling |
| `build/hover-definitions.yaml` | 14 new Stack chart definitions |
| `build/preprocess.py` | Stack chart popup injection, title→data-hover conversion |
| `build/reader.js` | Extend panel listener to `[data-hover]` selector, mobile-safe nav handling |
| `manuscript/00-front/the-stack.tex` | NO CHANGES (popups injected in HTML post-processing) |

---

## Phase 1: Stack Chart — Width + Popups

### 1A. CSS: Full-width table

The chart (screenshot confirms) is horizontally cramped. Fix in `html.css`:

```css
#stack-chart + table,
#stack-chart ~ table:first-of-type {
  width: 100%;
  table-layout: fixed;
}
```

Generator: inspect the generated HTML to find the correct selector. The `\hypertarget{stack-chart}{}` becomes an anchor element; the `<table>` follows it. The selector must target this specific table without affecting other tables in the document.

### 1B. YAML definitions for Stack chart cells

Add 14 entries to `hover-definitions.yaml` under descriptive keys. These are NOT hovertip-system entries (they bypass first-occurrence). They're looked up by preprocess.py's Stack chart post-processor.

**Row definitions (emergent properties):**

| Key | Definition |
|-----|------------|
| `stack-feeds-itself` | Sustains its own operation from available energy. Fire consumes fuel. Cells metabolize. The simplest requirement — without it, nothing persists. |
| `stack-switches-on` | Converts energy from one form to another at a threshold. Below a certain temperature, nothing happens; above it, combustion begins. Every technology on this list is a transducer. |
| `stack-holds-together` | Maintains structural integrity against entropy. A candle's wax column, an ant colony's nest architecture, a network's routing tables. Something keeps the parts organized. |
| `stack-reaches` | Transmits information or influence across distance. Radio waves cross oceans. Ant pheromone trails guide foragers to food. The internet routes packets across continents. |
| `stack-self-organizes` | Builds and maintains complex structure without external direction. No blueprint, no architect. Ant colonies, neural networks, market economies — order emerges from local rules. |
| `stack-learns` | Changes behavior based on experience. Modifies its own operation in response to outcomes. Only AI and the unnamed technology do this among the technologies listed. |
| `stack-wormholes` | Topological connections between distant points in a material. Not science fiction — condensed matter physics. The 2016 Nobel Prize was awarded for the theory. Only the unnamed technology has this property. |

**Column definitions (technologies):**

| Key | Definition |
|-----|------------|
| `stack-fire` | Humanity's first technology. Feeds itself on fuel, switches energy forms. But it doesn't hold a shape, reach across distance, organize itself, learn, or connect distant points. Two properties. |
| `stack-candle` | Fire plus structure. The wick and wax hold together — someone engineered sustained, portable combustion. Still doesn't reach, self-organize, learn, or connect. Three properties. |
| `stack-radio` | Energy that reaches across distance. Electromagnetic waves carry information without wires. But a radio doesn't organize itself, doesn't learn, doesn't form topological connections. Four properties. |
| `stack-ants` | E.O. Wilson's superorganism. No individual ant understands the colony, yet the colony solves problems no ant could. Self-organization from local chemical rules. Pheromones reach, but not electromagnetically — asterisk earned. Five properties. |
| `stack-internet` | A self-organizing network that reaches globally and holds together through redundant routing. It doesn't learn on its own — it routes, it doesn't adapt. Five properties. |
| `stack-ai` | The first human technology that learns. Changes its own behavior based on experience. Six properties out of seven. Missing only one — the one at the top of the stack. |
| `stack-question-mark` | This technology stack currently has no name in any human language. It has all seven properties, including the one no other technology possesses. Later, this book will call it the Flat — with a capital F. |

### 1C. preprocess.py: Stack chart popup injection

Add a post-processing step in `fix_html_toc()` (or a new function called from the same place):

1. Find the Stack chart table in the HTML — locate the `id="stack-chart"` anchor, then find the `<table>` that follows it.
2. For each `<th>` or first-row `<td>` cell containing a column header (Fire, Candle, etc.): wrap the text in `<span class="hover-term" data-hover="..." data-hover-id="stack-fire">`.
3. For each first-column `<td>` cell containing a row label (Feeds itself, Wormholes, etc.): same treatment.
4. Look up definitions from `hover-definitions.yaml` using the `stack-*` keys.
5. Do NOT add these to `hover_seen` — they don't participate in the first-occurrence system.

**Matching logic:** Map cell text content to YAML key:
```python
stack_row_map = {
    'feeds itself': 'stack-feeds-itself',
    'switches on': 'stack-switches-on',
    # etc.
}
stack_col_map = {
    'fire': 'stack-fire',
    'candle': 'stack-candle',
    # etc.
    '?': 'stack-question-mark',
}
```

The Generator must handle pandoc's HTML output format for the table. Pandoc may produce `<th>` for headers or `<td>` — inspect the actual output.

---

## Phase 2: Tooltip System Unification

### Goal

Replace all native browser `title=""` tooltips with popup panels. One tooltip system, not two.

### 2A. New CSS class: `hover-nav`

The existing `.hover-term` class has a dotted underline and `cursor: help`. That's wrong for navigation elements (TOC links, buttons). Create `.hover-nav`:

```css
.hover-nav {
  /* No underline change — element keeps its existing styling */
  cursor: pointer; /* or inherit from parent */
}
```

The `data-hover` attribute triggers the popup panel. The class controls only visual styling, not panel behavior.

### 2B. Extend reader.js panel listener

Currently the hover panel system binds to `.hover-term` elements. Change the selector to `[data-hover]` — any element with a `data-hover` attribute gets panel behavior. This covers both `.hover-term` (science popups) and `.hover-nav` (navigation tooltips).

```javascript
// OLD: document.querySelectorAll('.hover-term')
// NEW: document.querySelectorAll('[data-hover]')
```

### 2C. Mobile interaction safety

**Problem:** TOC links and accordion summaries have a primary click/tap action (navigate / expand). On desktop, hover shows popup and click navigates — no conflict. On mobile, the current hover-term system toggles the popup on tap — this would BLOCK navigation.

**Fix:** For elements that are links (`<a>`) or accordion triggers (`<summary>`), the touch handler must NOT toggle the popup. Let tap do its native thing (navigate / expand). The popup is desktop-hover-only for these elements.

Implementation: in the touchstart handler, check if `event.target.closest('a, summary')` — if so, skip the popup toggle.

### 2D. Convert `title=""` to `data-hover=""` in preprocess.py

In the HTML post-processing, after all other fixes:

1. Find all elements inside `<nav id="TOC">` with `title="..."` — replace with `data-hover="..."` and add `class="hover-nav"` (append to existing classes if present).
2. Find all `<summary>` elements with `title="..."` — same conversion.
3. Strip `title` attributes from converted elements (prevents native tooltip doubling).

### 2E. Convert `title=""` to `data-hover=""` in reader.js

For elements created in JS (bottom nav controls, share button, etc.):
- Replace `el.title = "..."` with `el.setAttribute('data-hover', "...")`
- Add `hover-nav` class
- Remove `title` attribute if set

### 2F. Retain `title` only where required

Some `title` attributes serve as accessible names (screen readers use `title` as fallback when no `aria-label` exists). For these, keep `title` AND add `data-hover`. The popup system should suppress native tooltip display (set `title=""` on mouseenter, restore on mouseleave) so only the popup shows visually, but screen readers still get the accessible name.

Generator: audit which elements rely on `title` for accessibility. Add explicit `aria-label` where needed, then remove `title`.

---

## Phase 3: Build + QA

1. `make dev` — clean build, zero warnings
2. **Stack chart checks:**
   - Table fills available width
   - Hovering each column header shows popup
   - Hovering each row label shows popup  
   - "?" popup mentions "the Flat"
   - Checkmark cells have no popup (they're not interactive)
3. **Tooltip unification checks:**
   - `grep -c 'title="' docs/downloads/Relinquishment.html` — should be minimal (only `<title>` tag, any image `title`s)
   - `grep -c 'data-hover=' docs/downloads/Relinquishment.html` — should be previous count (~66) + new count (~105 converted + 14 stack)
   - Hover a TOC link on desktop — popup appears
   - Click a TOC link — navigates (popup dismissed)
   - Hover an accordion summary — popup appears
   - Click accordion summary — expands/collapses (popup dismissed)
   - Bottom nav controls show popups on hover
4. **PDF check:** No new footnotes on the Stack chart table
5. Commit: `Plan 0139: Stack chart popups + tooltip unification`

---

## Annealing

### Pass 1 (HIGH): First-occurrence bypass for Stack chart

The original plan proposed using `\hovertip{}` inside LaTeX tabular cells. Two problems:
1. **Untested mechanism** — hovertip markers inside `tabular` have never been verified through pandoc
2. **First-occurrence collisions** — "wormholes" fires on the title line, "self-organizes" fires in the prose above the table. Both would render as `<em>` in the table, getting NO popup.

**Fix:** Complete redesign. Stack chart popups are injected by preprocess.py post-processing, not through `\hovertip{}`. They use `stack-*` namespaced YAML keys and don't participate in the first-occurrence system. The LaTeX source stays untouched. PDF gets no footnotes (which would be ugly on a table anyway).

### Pass 2 (HIGH): Mobile tap conflict

Converting `title=""` to `data-hover=""` on navigation links creates a mobile interaction conflict. The current hover-term system toggles popups on tap. If applied to TOC links, tapping a chapter name would show a popup instead of navigating.

**Fix:** Added 2C — the touch handler checks `event.target.closest('a, summary')` and skips popup toggle for navigation/accordion elements. Desktop hover still shows popups. Mobile users navigate normally.

### Pass 3 (MEDIUM): Accessibility regression

Removing `title=""` could break screen reader accessibility on elements that use `title` as their accessible name (e.g., icon-only buttons like § share, ← back).

**Fix:** Added 2F — audit for accessibility dependency, add explicit `aria-label` where needed before removing `title`. The popup panel system already uses `aria-describedby`.

### Pass 4 (LOW): Stack chart HTML structure

Pandoc may render the LaTeX tabular as `<table>` with or without `<thead>`. The column headers might be in `<th>` or `<td>`. The post-processing regex needs to handle both.

**Fix:** Generator must inspect actual pandoc output and match accordingly. Added instruction to Phase 1C.

### Pass 5 (LOW): YAML namespace

The 14 `stack-*` entries live in the same YAML file as the hovertip definitions. They won't collide (no one writes `\hovertip{stack-fire}`) but it's a namespace mixing concern.

**Fix:** Acceptable — the `stack-` prefix clearly distinguishes them. A YAML comment block marks the section. Adding a separate file for 14 entries would be over-engineering.

### Convergence

5 passes. Two HIGH issues (first-occurrence bypass, mobile tap conflict) drove significant redesign. Both resolved architecturally — not patched. The Stack chart is now cleanly separated from the hovertip system, and nav elements are explicitly mobile-safe.

**Confidence: 9/10.** The remaining 1/10: the pandoc table output format is assumed but not verified in this plan. Generator must inspect and adapt. This is a runtime decision, not a design gap.
