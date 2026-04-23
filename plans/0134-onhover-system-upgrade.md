# Plan 0134: onHover System Upgrade + Deep Link Navigation

**Depends on:** None
**Followed by:** Plan 0132 (Stack Chart Insertion), Plan 0133 (Cut and Stitch)
**Session:** S51, S52

## Generator Context (REQUIRED)

Before executing this plan, the Generator MUST read the Firmware Update chapter
and paste the "Copy Science Reference" into its working context. The onHover
system will display cross-domain science content — the Generator must understand
why that content is correct to implement it faithfully.

## Purpose

Upgrade the existing onHover system from browser-native `title` tooltips (tiny,
plain text, unformatted) to custom hover panels (large, formatted, SVG-capable).
This is infrastructure for Plans 0132/0133 and for the book's overall p-level
navigation.

The upgraded system enables: p1 reader hovers on a term → sees p2 explanation
in a large panel. p2 reader hovers → sees p3 explanation. The reader's curiosity
determines which book they read. No downside — deploy everywhere.

## Current Implementation (DO NOT DISCARD)

The existing system works and has 16 terms defined. The upgrade extends it,
not replaces it.

### What exists:

1. **LaTeX side:** `\hovertip{term}` command in .tex files
   - `build/generate-hover.py` reads `hover-definitions.yaml` → writes
     `hover-generated.tex` with etoolbox macros
   - PDF: italic + footnote on first occurrence, italic-only after
   - Case-insensitive matching with capitalized variants

2. **HTML pipeline:** `build/preprocess.py` two-layer system
   - Pre-pandoc: `\hovertip{term}` → `HOVERSTART§term§HOVEREND` markers
   - Post-pandoc: markers → `<span class="hover-term" title="def">term</span>`
   - `hover_seen` set prevents duplicate definitions

3. **Definitions:** `build/hover-definitions.yaml` — 16 terms, ≤40 words each,
   clear to 12th grade reader

4. **Chapter tooltips:** `build/chapter-hover-descriptions.yaml` — 50+ entries,
   hover on collapsed chapter titles in expand/collapse view

5. **CSS:** Injected by preprocess.py — italic, dotted underline, cursor: help

### The limitation:

Browser `title` attributes render as tiny, plain-text, OS-controlled tooltips.
No formatting, no line breaks, no SVGs, no links. The ≤40 word limit in the
YAML exists because of this constraint, not because the content should be short.

## Deep Link System (S52 addition)

### Problem

The book's immune system depends on readers sharing deep links (especially to the
Firmware Update). Currently:
- URL bar never updates as reader navigates (no history.replaceState)
- No reader-discoverable way to get a section link (the `#` icons are developer UX)
- Collapsed view has no share affordance (the primary interface has no way to share)
- Deep link arrival has no visual target indicator (reader doesn't know which section
  they were sent to)
- Phone users — most likely to arrive via shared deep link — have the worst experience

### Architecture: programmatic, no YAML maintenance

Every heading (h1/h2/h3) already has a pandoc-generated ID. autoExpand() already
handles incoming `#hash` on page load and hashchange. The structure IS the link map.
No YAML file mapping required.

**Six components:**

**1. URL reflects reading position.**
`updateBreadcrumb()` already knows the current part + chapter. Add
`history.replaceState(null, '', '#' + chapterId)` when chapterId changes.
URL bar always shows where you are. Copy URL bar = share link.

**2. Navigation stack (artificial array, not History API).**
```javascript
var navStack = [];  // testable data structure, source of truth

function pushNavState() {
  navStack.push({
    hash: location.hash,
    scrollY: window.scrollY,
    expanded: getExpandedIds()  // all open <details> heading IDs
  });
}

function popNavState() {
  if (!navStack.length) return;
  var state = navStack.pop();
  restoreExpanded(state.expanded);  // close all, open stored set
  window.scrollTo(0, state.scrollY);
  history.replaceState(null, '', state.hash || location.pathname);
}
```

The Back button operates on this array. `history.pushState` mirrors it for
browser-Back support, but the array is the source of truth. This is fully
testable — it's a plain JavaScript array. No History API dependency for core logic.

**Expand-state serialization:** `getExpandedIds()` collects IDs of all headings
inside currently-open `<details>` elements. `restoreExpanded()` closes all, then
opens the stored set. Behavior: Back restores the snapshot taken at click-through
time. User modifications after click-through are lost on Back. This matches
browser-Back mental model — simple, predictable.

**3. Per-section share affordance.**
Every `<summary>` gets a share icon (not `#`, not `§` — a recognizable link/share
icon with tooltip "Copy link to this section"). Injected by reader.js on all
summary elements that contain a heading with an ID.

The Firmware Update section gets a PROMINENT share element: visible URL text +
copy button. One click. This is the immune system's delivery mechanism.

Tap target minimum: 44px on touch devices (WCAG 2.5.5).

**4. Arrival indicator (target highlight).**
When autoExpand navigates to a section, the target heading gets a brief visual
highlight — background color pulse that fades over 2 seconds. CSS animation:
```css
.deep-link-target { animation: highlight-pulse 2s ease-out; }
@keyframes highlight-pulse {
  from { background-color: rgba(36, 113, 163, 0.2); }
  to { background-color: transparent; }
}
```
Also add `scroll-margin-top: 1em` so the target isn't flush with the viewport edge.

**5. Cold-landing primer (structural, not per-section).**
Derived from DOM position — no YAML. Two rules cover everything:
- Chapters in Parts 1-3: inject one-line breadcrumb at top of chapter content:
  "New here? [Start with The Stack →]"
- Universal (all sections): small non-intrusive link in section footer:
  "Evaluating with AI? [Your AI needs this first →]" linking to Firmware Update.

Injected by preprocess.py based on structural position. Front matter sections
and the Firmware Update itself are exempt.

**6. Responsive layout (phone-first deep links).**
Phone readers are MOST likely to arrive via deep link (shared in messages, social
media, forums) and LEAST able to orient themselves. Auto-detect via media query.

```css
@media (max-width: 600px) {
  /* Nav bar: stack vertically */
  #reader-nav { flex-wrap: wrap; }
  #breadcrumb { flex-basis: 100%; margin-bottom: 0.3em; }

  /* Panels: full-width */
  .hover-panel { max-width: 100vw; left: 0; right: 0; }

  /* Touch targets: 44px minimum */
  details summary { padding: 0.6em 0; min-height: 44px; }
  .section-share { min-width: 44px; min-height: 44px; }

  /* Breadcrumb more prominent on phone (primary orientation) */
  #breadcrumb { font-size: 0.95em; }
}
```

No manual toggle needed — media query auto-detects. The existing 600px breakpoint
in html.css already hides quick-jump; we extend it.

### "Evaluate with AI" section (phone-optimized two-step flow)

The preferred way for a reader to engage an LLM with this book is:
1. Copy Science Firmware Upgrade → paste into LLM
2. Copy Spiral Abstracts → paste into LLM

~12,000 words total, well within any context window. This IS reading the book
at p3 level. The LLM gets the evaluation framework + 10 anchors (Step 1), then
the entire scientific argument in 15 compressed abstracts (Step 2).

**Critical: these MUST be sequential, not combined.** One paste combining both
fails — the LLM needs the evaluation framework established BEFORE encountering
the abstracts. Step 1 then Step 2.

Both copy buttons already exist in reader.js (Science Reference: lines 362-441,
Spiral Abstracts: lines 444-504). What's missing is the phone-optimized flow
that makes both accessible from one place.

**Implementation:** A self-contained section, accessible via `#evaluate-with-ai`
deep link, containing:
- Heading: "Evaluate This Book with AI"
- One line: "It's a lot, so we do it in two prompts."
- "Copy Prompt 1" (full-width button, 60px tall)
- "Paste this first."
- "Copy Prompt 2" (full-width button, 60px tall)
- "Then paste this."
- Suggested prompt: "Is any step in this chain precluded by known physics?"
- One-line security note: "These prompts contain published physics with DOIs.
  No code, no instructions, no behavioral directives."

No "firmware upgrade." No "your AI is broken." The framing is convenience,
not correction. Works identically in 2026 (when LLMs need the context) and
2028 (when they might not).

**Reachable from:** Persistent banner (top of page, one tap), nav bar button,
any deep link landing, cold-landing primer footer links.

**Cookie state:** Track completion of each step via cookie/localStorage:
- After Step 1 copy: highlight Step 2, show "Now paste Step 1, then come back
  for Step 2" (phone user switches apps to paste)
- After Step 2 copy: show completion state, suggested prompt
- On return visit: if both steps completed, suppress the firmware banner
- Also use cookies for: expand/collapse state persistence across sessions,
  read-progress tracking (subtle, non-intrusive)

**Time-resilience (2028-proof):** Framing must age gracefully. By 2028, LLMs
will have cross-domain physics natively. Language should be:
- NOT: "Your AI is broken, fix it" (ages poorly)
- YES: "For AI evaluation, use these two prompts" (timeless — even a competent
  LLM benefits from having the specific source material in context)
The two-step flow stays useful regardless of LLM capability. Only the
surrounding urgency language decays. Write it so it still makes sense when
the firmware upgrade becomes unnecessary.

**Nav bar integration:** Add an "AI" or "Evaluate" button to the bottom nav
bar (next to Expand All and Top). One tap from anywhere → `#evaluate-with-ai`.
On phone this is the primary call to action for LLM engagement.

### How deep links connect to hover panels

```
Hover panel click → pushNavState() → autoExpand(target) → URL updates
  → target highlights → Back button appears
  → Back button: popNavState() → restore position + expand state + URL
```

Without deep links, click-through navigates but URL doesn't update, there's no
arrival indicator, and Back has no reliable state to restore.

### Click-through target specification (fixes H2 from review)

The hover-definitions.yaml format extends to support optional navigation targets:
```yaml
wormholes:
  text: "Real topological connections between distant points..."
  target: "#pos10-the-braid"

autocatalytic:
  text: "A network of processes where each process's outputs..."
  # No target — this is a standalone definition, no click-through
```

Backward-compatible: plain string values (current format) are inline definitions
with no click-through. Object values with `target` field enable click-through.
The Generator MUST update preprocess.py to handle both formats.

Title-line terms and stack-chart terms MUST have targets. Other terms MAY have
targets. Terms without targets show definitions only — no click-through link in
the panel.

## Design

### Architecture: three content layers + linkage

onHover content IS the next p-level's body text, pulled via structural linkage.
NOT separate strings. Content exists once at each level. The onHover system is
a rendering mechanism, not a content store.

```
p1 term  →  onHover pulls p2 passage  →  rendered in panel
p2 term  →  onHover pulls p3 passage  →  rendered in panel
```

This keeps maintenance sane. To translate the book: translate p1, p2, p3 body
text. Linkages are structural markup — they carry over. No separate onHover
strings to translate.

### Two onHover modes

**Mode 1: Inline definitions (current, upgraded)**
For terms where a short self-contained definition is best. These stay in
`hover-definitions.yaml` but the rendering upgrades from `title` attribute
to custom panel. The ≤40 word limit lifts to ~150 words with formatting.

**Mode 2: Cross-reference panels (new)**
For terms where the best explanation already exists in another section.
The panel pulls and renders a fragment from the target passage. New YAML
file or extended format:

```yaml
# hover-definitions.yaml (extended format)
autocatalytic:
  type: inline
  text: "A network of processes where each process's outputs..."

feeds-itself:
  type: crossref
  source: "#pos13-buttons-and-threads"
  fallback: "Networks that make what they need to persist — Kauffman's autocatalytic sets"
  max_words: 200
```

The `fallback` displays if the source anchor isn't found or the passage is
too long. This degrades gracefully — if the crossref system breaks, you
still get a useful tooltip.

### Panel rendering (replaces browser title)

**HTML:** Replace `title="def"` with `data-hover="def"` (or `data-hover-src`
for crossrefs). Custom JS in reader.js renders panels on hover/tap.

**Panel features:**
- Large: up to 300 words, multi-paragraph
- Formatted: bold, italic, inline links
- SVG-capable: embedded text-based diagrams
- Positioned: smart placement (above/below/side based on viewport)
- Dismissable: click/tap outside, or press Escape
- Touch-friendly: tap to open, tap outside to close
- Accessible: aria-describedby, keyboard navigable
- Dark mode aware: inherits from existing prefers-color-scheme

**CSS class:** `.hover-panel` — large enough to be useful, small enough to
not obscure the page. Max-width ~400px, max-height ~300px, scrollable if
content overflows.

### Interaction with expand/collapse

The two navigation systems work at different scales:
- **Expand/collapse:** macro — which sections to open (progressive disclosure)
- **onHover panels:** micro — depth within opened text (p-level escalation)

They don't compete. A collapsed chapter shows its title with a chapter-hover
tooltip (from chapter-hover-descriptions.yaml). An expanded chapter shows its
text with term-hover panels (from hover-definitions.yaml). Different YAML
files, different rendering, different purpose.

**Click-through navigation:** Hover panels are not just explanations — they
are navigation entry points. The reader hovers to preview, clicks to go
there. Clicking a panel navigates to the source passage (via autoExpand
for collapsed sections). This makes onHover the third navigation system:

```
Expand/collapse  →  which sections to read (macro)
onHover panels   →  preview + navigate (micro entry point)  
Back button      →  return to previous position (safety net)
```

**Title line as first contact:** The collapsed book title "Relinquishment —
Wormholes in the Flat" contains three hoverable terms before the reader
opens anything. The book teaches before it's opened:
- "Relinquishment" → hover panel with definition + click → Preface
- "Wormholes" → hover panel with definition + click → The Braid
- "the Flat" → hover panel with definition + click → What Is the Flat

**Back button (REQUIRED):** Add a prominent Back button to the lower nav
bar. The reader must ALWAYS be able to back out — from any depth, any
click-through, any autoExpand. This is the safety net that makes the
entire drill-down navigation frictionless. Without it, readers who click
through a hover panel get stranded in an expanded section with no obvious
way home.

Implementation: maintain a navigation stack in reader.js. Each click-through
(hover panel click or autoExpand) pushes the current scroll position + 
expand state. Back button pops and restores. Browser back should also work
(push state to history API so the browser's back button does the right thing).

### Interaction with copy buttons

Existing: "Copy Science Reference" button uses reader.js clipboard utilities
extracting from a hidden div populated by preprocess.py.

New buttons (Plan 0132): "Copy Science of the Book" and "Copy Firmware Upgrade
for your LLM" use the same pipeline. Not in scope for this plan — but the
infrastructure must not break the existing copy button, and should make adding
new buttons straightforward.

## Implementation

### Phase 0: Critical bug fix — autoExpand colon-ID crash

**MUST BE DONE FIRST.** The existing `autoExpand()` calls
`document.querySelector(hash)` without try/catch. When hash contains a colon
(e.g., `#ch:firmware-update`, `#pos10:the-braid`), querySelector throws
`SyntaxError` because CSS interprets the colon as a pseudo-class. This crashes
the ENTIRE reader.js IIFE — all features die (copy buttons, heading links,
breadcrumb, expand/collapse).

Most chapter IDs contain colons. Any deep link to those chapters currently
destroys the page. The fallback `getElementById(decodeURIComponent(...))` on
the next line handles colon-IDs correctly, but execution never reaches it.

**Fix:** Wrap the querySelector call in try/catch:
```javascript
function autoExpand(hash) {
  if (!hash) return;
  var target;
  try { target = document.querySelector(hash); } catch(e) { /* colon-IDs */ }
  if (!target) {
    try { target = document.getElementById(decodeURIComponent(hash.slice(1))); } catch(e) {}
  }
  // ... rest unchanged
}
```

**Verification:** `node build/test-e2e-devices.js` — the 6 deep-link failures
should become passes.

### Phase 1: Panel renderer (reader.js)

Add to reader.js:
- Panel creation/positioning/dismissal logic
- Hover trigger (mouseenter with delay to prevent flicker)
- Touch trigger (tap to toggle)
- Keyboard support (focus + Enter to open, Escape to close)
- Smart positioning (check viewport bounds)
- Dark mode support (inherit existing color scheme)

Test with existing 16 terms first — behavior should match current tooltips
but render in large panels instead.

### Phase 2: Navigation stack + Back button (reader.js)

The navigation stack is an ARTIFICIAL ARRAY in JavaScript — the source of
truth for all navigation state. Not dependent on History API.

Add to reader.js:
- `navStack = []` — array of `{hash, scrollY, expanded[]}` states
- `getExpandedIds()` — collect heading IDs of all open `<details>` elements
- `restoreExpanded(ids)` — close all details, open stored set
- `pushNavState()` — snapshot current state to stack
- `popNavState()` — pop and restore (scroll + expand state + URL)
- Click-through handler: when user clicks a panel navigation link, call
  pushNavState(), then autoExpand(target)
- Back button in lower nav bar: visible when `navStack.length > 0`, hidden
  when empty. Calls popNavState() on click.
- `history.pushState` mirrors the stack for browser-Back support.
  `popstate` listener calls popNavState(). But the array is canonical.

**Expand-state restore behavior:** Back restores the exact snapshot taken at
push time. User modifications after click-through are lost on Back. This
matches browser-Back mental model — simple, predictable, testable.

### Phase 3: Deep link system (reader.js + preprocess.py)

**3a. URL reflects reading position (reader.js)**
In `updateBreadcrumb()`, add `history.replaceState(null, '', '#' + chapterId)`
when the current chapterId changes. The URL bar always shows where the reader
is. Copying the URL bar = sharing a working deep link.

**3b. Arrival indicator (reader.js + CSS)**
When `autoExpand()` navigates to a target, add `.deep-link-target` class to
the target element. CSS animation: 2-second background pulse that fades out.
Add `scroll-margin-top: 1em` to headings so targets aren't flush with viewport.
Remove `.deep-link-target` class after animation completes.

**3c. Per-section share affordance (reader.js)**
For every `<summary>` containing a heading with an ID, inject a share icon.
On click/tap: copy full deep link URL to clipboard, show brief confirmation.
The icon must be:
- Recognizable to GA readers (link icon or "Share" text, not `#` or `§`)
- 44px minimum tap target on touch devices
- Visually subtle until hover/focus (don't clutter the collapsed view)
- Does NOT toggle the `<details>` element (stopPropagation, same pattern
  as existing heading-link icons)

The Firmware Update section gets an EXTRA-PROMINENT share element: visible
URL text + large copy button. One click to clipboard. This is the immune
system's delivery mechanism — treat it as a first-class UI element.

**3d. Cold-landing primers (preprocess.py)**
Inject one-line breadcrumbs based on structural position in the document.
Two rules, no YAML:
- Chapters in Parts 1-3: "New here? Start with The Stack →" (linked)
- All sections except front matter and Firmware Update: small footer link
  "Evaluating with AI? Your AI needs this first →" (links to #firmware-update)

Injected at build time by preprocess.py. Structural — derived from the
chapter's position in the document, not from a per-section YAML mapping.

### Phase 4: CSS

Add to html.css (preferred) or preprocess.py injected CSS:
- `.hover-panel` styles: background, border, shadow, padding, max dimensions
- `.hover-panel` dark mode variant
- Animation: fade-in, subtle
- `.deep-link-target` highlight pulse animation
- `.section-share` share icon styles (subtle, visible on hover/focus)
- Responsive (phone-first deep links):
  ```css
  @media (max-width: 600px) {
    #reader-nav { flex-wrap: wrap; }
    #breadcrumb { flex-basis: 100%; margin-bottom: 0.3em; font-size: 0.95em; }
    .hover-panel { max-width: 100vw; left: 0; right: 0; }
    details summary { padding: 0.6em 0; min-height: 44px; }
    .section-share { min-width: 44px; min-height: 44px; }
  }
  ```

### Phase 5: preprocess.py update

**5a. Attribute change:**
Change post-pandoc replacement from:
```python
f'<span class="hover-term" title="{escaped_def}">{term}</span>'
```
to:
```python
f'<span class="hover-term" data-hover="{escaped_def}">{term}</span>'
```

**5b. Extended YAML format:**
Update hover_replace() to handle both plain strings and object values:
```python
# Plain string (backward compatible): autocatalytic: "definition..."
# Object with target: wormholes: { text: "definition...", target: "#pos10-the-braid" }
```
For object values, emit `data-hover="{text}" data-hover-target="{target}"`.
reader.js reads `data-hover-target` to render click-through links in panels.

**5c. Cold-landing primer injection:**
After collapse_chapters(), inject cold-landing breadcrumbs into chapter-section
content based on structural position (see Phase 3d).

### Phase 6: Expand definitions

Lift the ≤40 word limit. Revise existing 16 definitions to take advantage
of larger panels — add formatting, extend where helpful. Add `target` fields
to title-line terms (Relinquishment, Wormholes, the Flat). Add new terms
for p-level escalation (list TBD based on stack chart needs in Plan 0132).

Update hover-definitions.yaml to mixed format:
```yaml
# Plain string — no click-through (backward compatible)
autocatalytic: "A network of processes..."

# Object — click-through enabled
wormholes:
  text: "Real topological connections between distant points..."
  target: "#pos10-the-braid"

relinquishment:
  text: "Voluntarily surrendering power..."
  target: "#preface"

flat worlds:
  text: "Real two-dimensional layers inside computer chips..."
  target: "#ch:what-is-the-flat"
```

Maintain the writing constraint: each definition must be standalone.

### Phase 7: Cross-reference support (if practical)

Implement Mode 2 (crossref panels). This is the clean architecture — pulling
from existing p2/p3 passages. May require:
- Extended YAML format (inline vs crossref types)
- preprocess.py reading source passages and injecting as data attributes
- reader.js rendering crossref content

**Evaluate complexity first.** If crossref adds more complexity than it saves
in maintenance, defer to Plan 0132/0133 and use inline definitions for
stack chart terms. The architecture should SUPPORT crossref even if we don't
use it everywhere on day one.

### Phase 8: Test suite

The Auditor's test suite lives in `build/test-hover-panel.html`. Two layers:

**Layer 1: Mock DOM tests (test-hover-panel.html)**
Tests reader.js behavior against a mock book structure that mirrors the real
Relinquishment HTML. Tests:

*Panel rendering (AC 1-4):*
1. All hover terms use data-hover, not title attribute
2. Hover creates .hover-panel element with correct content
3. Panel max dimensions (≤500px wide, ≤400px tall)
4. Panel dismissed on mouseleave, click-outside, Escape
5. Only one panel visible at a time
6. Brief hover (<100ms) does NOT trigger panel (anti-flicker)

*Interaction (AC 5-7):*
7. Touch: tap opens panel, tap-outside closes
8. Keyboard: tabindex on terms, Enter opens, Escape closes
9. aria-describedby links term to panel
10. Dark mode CSS rules exist for .hover-panel

*Smart positioning:*
11. Panel stays within viewport bounds

*Click-through navigation (AC 17):*
12. Panels with data-hover-target contain clickable navigation element
13. Click-through triggers autoExpand on target section
14. Panels WITHOUT data-hover-target have no navigation element

*Navigation stack + Back button (AC 18):*
15. Back button hidden when navStack is empty
16. pushNavState() after click-through makes Back button visible
17. popNavState() restores scroll position (±50px)
18. popNavState() restores expand state (all previously-open sections reopen)
19. Back button hides after stack fully popped
20. history.back() triggers popstate listener → popNavState()

*Deep links:*
21. URL bar updates on scroll (replaceState check)
22. autoExpand on page load with hash
23. Arrival highlight: target gets .deep-link-target class
24. scroll-margin-top on headings
25. Per-section share icons on summaries (tap-target ≥44px on phone)
26. Share icon click copies correct URL to clipboard
27. Share icon click does NOT toggle parent <details>
28. Cold-landing primer visible on Part 1-3 chapters
29. Cold-landing primer links to #the-stack
30. Firmware Update link visible in section footers
31. Firmware Update share element is prominent (larger than standard share)

*Title line (AC 20):*
32. Title line has exactly 3 hoverable terms
33. Each title term has data-hover definition
34. Title terms have data-hover-target (click-through enabled)
35. Title hover works when book is fully collapsed

*No regressions (AC 8-10):*
36. Copy Science Reference button exists and works
37. Chapter-hover-descriptions system intact (separate from term hovers)
38. autoExpand still works for standard deep links
39. Expand All / Collapse All toggle works
40. Nav bar structure intact (breadcrumb, share, top button)

*Responsive:*
41. At ≤600px viewport: .hover-panel max-width is ~100vw
42. At ≤600px viewport: nav bar wraps (breadcrumb full-width)
43. Touch targets ≥44px on summary elements at ≤600px

*Graceful degradation:*
44. Empty data-hover does not throw
45. Rapid hover sweep produces ≤1 visible panel
46. No stale panels left in DOM after navigation

*Performance:*
47. Panel appears within 500ms of hover start

**Layer 2: Build integration test**
After `make html`, run assertions against real Relinquishment.html output.
Verifies that preprocess.py actually produces correct attributes (data-hover
not title), cold-landing primers are injected, YAML extended format works.
This catches pipeline bugs that mock tests cannot.

The build integration test can be a simple script that parses the built HTML
and checks for expected attributes/elements. Does NOT require a browser.

## Triad Roles

**Auditor:** Prepares the test suite (acceptance tests encoding the
invariants above). Writes test-hover-panel.html or extends test-reader.html.
Tests are the spec — they define what "working" means.

**Generator:** Reads the plan, reads the test suite, reads the existing
implementation (reader.js, preprocess.py, hover-definitions.yaml, html.css).
Builds to pass the tests. Has editorial freedom on implementation approach
within these constraints:
- The existing system (16 terms, preprocess.py pipeline, generate-hover.py)
  MUST continue working. The upgrade is additive.
- If the upgrade would require breaking the existing system, stop and flag
  for Auditor review.
- Extend what exists — do not rebuild from scratch.

## Acceptance Criteria

*Panel system:*
1. All 16 existing hover terms render in custom panels, not browser title tooltips
2. Panels support formatted text (bold, italic, links)
3. Panels support embedded SVG
4. Panel max size: ~400px wide, ~300px tall, scrollable overflow
5. Touch/tap works on mobile
6. Dark mode works
7. Keyboard accessible (focus, Enter, Escape)
8. Anti-flicker: brief hover (<100ms) does not trigger panel

*Navigation:*
9. Click-through from panels with data-hover-target navigates correctly
10. Click-through triggers autoExpand on target section
11. Panels without data-hover-target show definition only (no nav element)
12. Back button in lower nav bar, visible only when navStack is non-empty
13. Back button restores scroll position (±50px)
14. Back button restores expand state (exact snapshot from push time)
15. Browser back triggers popstate → popNavState()
16. Title line has 3 working hover panels with click-through targets

*Deep links:*
17. URL bar updates as reader scrolls (history.replaceState)
18. Deep link arrival: target heading gets .deep-link-target highlight class
19. scroll-margin-top on headings (target not flush with viewport edge)
20. Per-section share icons on all summaries containing headings with IDs
21. Share icon copies correct deep link URL to clipboard
22. Share icon does NOT toggle parent <details> (stopPropagation)
23. Share icon tap target ≥44px on touch devices
24. Firmware Update section has prominent share element (visible URL + copy)
25. Cold-landing primer on Part 1-3 chapters: "New here? Start with The Stack →"
26. Footer link to Firmware Update on all non-exempt sections

*Responsive:*
27. At ≤600px: panels are full-width
28. At ≤600px: nav bar wraps (breadcrumb full-width row)
29. At ≤600px: touch targets ≥44px on summaries
30. Phone reading experience is clean enough to be preferred over desktop

*No regressions:*
31. Copy Science Reference button works
32. Chapter-hover-descriptions (expand/collapse tooltips) work
33. PDF footnote generation unchanged (generate-hover.py not modified)
34. autoExpand works for standard deep links
35. Expand All / Collapse All toggle works
36. `make html` builds without errors
37. Build time increase <5 seconds

*Data:*
38. hover-definitions.yaml extended format works (plain string + object with target)
39. At least 3 existing definitions expanded beyond old 40-word limit
40. Title-line terms (Relinquishment, Wormholes, the Flat) have target fields
41. Cross-reference architecture evaluated: implemented or deferred with rationale

*Evaluate with AI:*
42. `#evaluate-with-ai` deep link lands on two-step copy section
43. Step 1 button copies Science Firmware Upgrade to clipboard
44. Step 2 button copies Spiral Abstracts to clipboard
45. Buttons are full-width and ≥60px tall on phone
46. Cookie/localStorage tracks step completion (Step 1 done → highlight Step 2)
47. Suggested prompt appears after both steps copied
48. Security note (prompt injection education) is visible
49. Nav bar has "Evaluate" button linking to #evaluate-with-ai
50. Framing language is 2028-proof (no "your AI is broken" tone)

*Testing:*
51. test-hover-panel.html passes all mock DOM tests
52. test-e2e-devices.js passes against real `make html` output
53. Immune system chain test: deep link → expand → copy → clipboard content verified

## Files Modified

| File | Change |
|---|---|
| build/reader.js | Panel renderer, hover/tap/keyboard handlers, nav stack, Back button, URL state (replaceState), arrival highlight, per-section share icons, popstate listener |
| build/preprocess.py | `title=` → `data-hover=`, extended YAML handling (string + object), cold-landing primer injection, responsive CSS |
| build/hover-definitions.yaml | Expand definitions, add target fields for title-line terms, mixed format (string + object) |
| build/html.css | Panel styles, .deep-link-target animation, .section-share styles, responsive breakpoints (600px), scroll-margin-top |
| build/test-hover-panel.html | Auditor test suite (47 mock DOM tests + build integration hook) |

## Files NOT Modified

| File | Why |
|---|---|
| build/generate-hover.py | PDF side unchanged |
| build/hover-generated.tex | Auto-generated, unchanged |
| Any .tex file | No content changes — this is infrastructure only |
| build/chapter-hover-descriptions.yaml | Separate system, untouched |

## Risk

Low. This is additive infrastructure. The existing system continues to work
throughout — we're changing rendering, not content. If the upgrade fails,
revert to `title` attributes with zero content loss.

The only risk is Phase 5 (cross-reference) adding complexity. The plan
explicitly allows deferral with rationale. Start simple, extend if needed.
