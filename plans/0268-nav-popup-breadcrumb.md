# Plan 0268: Navigation Popup Breadcrumb

**Status:** DRAFT
**Author:** Auditor (Argus S63)
**Priority:** High
**Scope:** `build/reader.js` (primary), CSS in `build/preprocess.py` or inline
**Related plans:**
- **0276** — Visual Language Deployment (epistemic colors reused in popup)
- **0144** — Epistemic filter buttons (Science/Story, currently commented out — absorbed here)
- **0263/0264** — Cover magnetosphere (nav bar positioning context)

---

## Problem Statement

The bottom navigation bar has 14 items competing for ~375px of phone screen. The breadcrumb — the largest element — has been broken repeatedly because scroll-based detection of the current chapter is fragile, and the text overflows on mobile. Bruce has tried to fix it multiple times. It currently wastes the most valuable real estate on the nav bar.

Meanwhile, quick-jump links (Intro · The Flat · The Record · Appendices) provide limited navigation — four links for a 48-chapter book. Readers who want to jump to a specific chapter have no tool for it; they must scroll or use Expand All, which is disorienting.

## Design: Dual-Mode Breadcrumb

### Passive Mode (default)
The breadcrumb zone shows the reader's current location:

```
The Flat › The Wrong Substrate ▾
```

- Text updates on scroll (existing logic, simplified)
- Small ▾ indicator signals tappability
- Overflow: ellipsis from the LEFT (part name truncates first, chapter name preserved)
- If scroll detection fails: shows "Relinquishment ▾" — still useful because tap opens the popup

### Active Mode (on tap)
A popup overlay rises from the nav bar showing the full book structure:

```
┌─────────────────────────────────┐
│  ✕                              │
│                                 │
│  Introduction                   │
│    What Would You Do?           │
│    The Stack                    │
│    The Story Never Told         │
│    Preface                      │
│                                 │
│  ● The Flat                     │  ← gold dot
│    Three Possibilities          │
│    Wormholes in the Flat        │
│    The Braid                    │
│  ► The Wrong Substrate ◄        │  ← YOU ARE HERE
│    The Silence Gap              │
│    ...                          │
│                                 │
│  ● The Record                   │  ← blue dot
│    Alpha Farm                   │
│    ...                          │
│                                 │
│  ● Appendices                   │
│    Firmware Update              │
│    ...                          │
└─────────────────────────────────┘
```

**Popup behavior:**
- Rises from the nav bar with a slide-up animation (200ms)
- Semi-transparent backdrop dims the page behind
- Max-height: 70vh (scrollable within the popup)
- Auto-scrolls so the current chapter is visible mid-popup
- Current chapter highlighted with accent background
- Tap any chapter → `pushNavState()`, `autoExpand('#' + chapterId)`, scroll to it, popup dismisses
- Tap ✕ or backdrop → popup dismisses
- Escape key → popup dismisses

**Visual elements in the popup:**
- Part names: bold, slightly larger, with epistemic color dot (gold for The Flat, blue for The Record, purple if applicable)
- Chapter names: indented under their part, normal weight
- Current chapter: highlighted row (subtle background accent)
- Chapters with `data-filter-group="G"` (Custodian interludes): italic, purple text — visually distinct as the Custodian's voice
- No icons, no badges, no clutter — text hierarchy does the work

### What Gets Removed from the Nav Bar

| Item | Action | Reason |
|------|--------|--------|
| Quick-jump links (Intro·Flat·Record·Appendices) | **REMOVE** | Subsumed by popup — popup shows ALL chapters, not just 4 |
| § Share button | **KEEP** | Stays next to breadcrumb, still useful |
| PDF link | **MOVE to popup footer** | Secondary action, not primary nav |
| tips:on/off | **MOVE to popup footer** | Niche, clutters bar |
| C (Custodian filter) | **MOVE to popup footer** | Cool but secondary |
| ◐ Magnetosphere toggle | **MOVE to popup footer** | Cosmetic |
| Expand All | **MOVE to popup footer** | Power-user action |
| Science/Story buttons (commented out) | **DELETE code** | Dead feature, replaced by popup + filter group visibility |
| Hidden tools dot | **MOVE to popup footer** | Author tool, keep hidden-ish |

### Final Nav Bar Layout

```
[ ← Back ]  The Flat › The Wrong Substrate ▾  [ § ]  [ AI Eval ]  [ ▲ Top ]
```

Five items. Fits any phone. The breadcrumb zone is the largest element (flex:1) and does double duty.

**Popup footer** (small row at bottom of popup):
```
[ Expand All ]  [ C ]  [ ◐ ]  [ PDF ]  [ tips:on ]
```

These are secondary tools, available one tap from the bar but never cluttering it.

---

## Implementation

### File: `build/reader.js`

All changes are in reader.js. No preprocess.py or manuscript changes needed.

### Phase 1: Build the Popup

**1a. Create popup container (DOM construction)**

After the nav bar is built, create the popup elements:

```javascript
var navPopup = document.createElement('div');
navPopup.id = 'nav-popup';
// Hidden by default, positioned above nav bar
// Contains: close button, scrollable chapter list, footer

var navBackdrop = document.createElement('div');
navBackdrop.id = 'nav-backdrop';
// Full-screen semi-transparent overlay behind popup
```

Append to body (not nav — popup needs to overlay content).

**1b. Populate chapter list from live DOM**

On popup open (not at page load — the DOM may change if filters are active):

```javascript
function buildPopupContents() {
  var list = navPopup.querySelector('.nav-popup-list');
  list.innerHTML = '';
  
  // Walk the book structure: part-section > chapter-section
  document.querySelectorAll('details.part-section').forEach(function(part) {
    // Skip hidden parts (filtered out)
    if (part.style.display === 'none') return;
    
    var summary = part.querySelector(':scope > summary');
    var h1 = summary.querySelector('h1[id]');
    var partName = h1 ? h1.textContent.trim() : summary.textContent.trim();
    var partId = h1 ? h1.id : '';
    
    // Determine epistemic color from first chapter's filter group
    var firstCh = part.querySelector('details.chapter-section');
    var fg = firstCh ? (firstCh.getAttribute('data-filter-group') || 'M') : 'M';
    var dotColor = fg === 'A' ? '#d4a847' : (fg === 'C' ? '#9b7db8' : '#6a9fb5');
    
    // Create part header
    var partEl = document.createElement('div');
    partEl.className = 'nav-popup-part';
    partEl.innerHTML = '<span class="nav-popup-dot" style="color:' + dotColor + '">●</span> ' + esc(partName);
    partEl.addEventListener('click', function() { navigateTo(partId); });
    list.appendChild(partEl);
    
    // Create chapter entries
    part.querySelectorAll(':scope > details.chapter-section').forEach(function(ch) {
      if (ch.style.display === 'none') return;
      var chSummary = ch.querySelector(':scope > summary');
      var h2 = chSummary.querySelector('h2[id], h3[id]');
      var chName = h2 ? h2.textContent.trim() : chSummary.textContent.trim();
      var chId = h2 ? h2.id : '';
      var isInterlude = ch.getAttribute('data-filter-group') === 'G';
      var isCurrent = chId && chId === currentChapterId;
      
      var chEl = document.createElement('div');
      chEl.className = 'nav-popup-chapter' + (isCurrent ? ' nav-popup-current' : '') + (isInterlude ? ' nav-popup-interlude' : '');
      chEl.textContent = chName;
      chEl.setAttribute('data-chapter-id', chId);
      chEl.addEventListener('click', function() { navigateTo(chId); });
      list.appendChild(chEl);
    });
  });
}
```

**1c. Navigation function**

```javascript
function navigateTo(id) {
  closePopup();
  if (!id) return;
  pushNavState();
  autoExpand('#' + id);
}
```

**1d. Open/close functions**

```javascript
var popupOpen = false;

function openPopup() {
  buildPopupContents();
  popupOpen = true;
  navBackdrop.style.display = 'block';
  navPopup.style.display = 'block';
  // Animate in
  requestAnimationFrame(function() {
    navBackdrop.style.opacity = '1';
    navPopup.style.transform = 'translateY(0)';
  });
  // Auto-scroll to current chapter
  var cur = navPopup.querySelector('.nav-popup-current');
  if (cur) cur.scrollIntoView({ block: 'center' });
}

function closePopup() {
  popupOpen = false;
  navBackdrop.style.opacity = '0';
  navPopup.style.transform = 'translateY(100%)';
  setTimeout(function() {
    navBackdrop.style.display = 'none';
    navPopup.style.display = 'none';
  }, 200);
}
```

**1e. Wire breadcrumb tap**

```javascript
breadcrumb.style.cursor = 'pointer';
breadcrumb.addEventListener('click', function(e) {
  e.preventDefault();
  e.stopPropagation();
  if (popupOpen) closePopup();
  else openPopup();
});
```

### Phase 2: Rearrange the Nav Bar

**2a. Remove items from bar, add to popup footer**

```javascript
// These are NO LONGER appended to nav:
// quickJump, pdfBtn, tipsBtn, gBtn, msToggle, expandBtn, toolsLink

// Instead, create a footer row inside the popup:
var popupFooter = document.createElement('div');
popupFooter.className = 'nav-popup-footer';
popupFooter.appendChild(expandBtn);
popupFooter.appendChild(gBtn);
popupFooter.appendChild(msToggle);
popupFooter.appendChild(pdfBtn);
popupFooter.appendChild(tipsBtn);
navPopup.appendChild(popupFooter);
```

**2b. Update nav.appendChild calls**

Final nav assembly:
```javascript
nav.appendChild(backBtn);
nav.appendChild(breadcrumb);
nav.appendChild(shareBtn);
nav.appendChild(evalBtn);
nav.appendChild(topBtn);
```

**2c. Delete dead code**

Remove the commented-out `scienceBtn` / `storyBtn` and their filter functions (`applyFilters`, `updateFilterButtons`, `showScience`, `showStory`). The Custodian-only filter (gBtn) survives in the popup footer.

### Phase 3: CSS

All CSS is injected inline via reader.js (existing pattern). Key styles:

```css
#nav-backdrop {
  display: none;
  position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.4);
  z-index: 99;
  opacity: 0;
  transition: opacity 0.2s;
}

#nav-popup {
  display: none;
  position: fixed;
  bottom: 2.5em; /* above nav bar */
  left: 0.5em; right: 0.5em;
  max-height: 70vh;
  background: #fff;
  border-radius: 8px 8px 0 0;
  box-shadow: 0 -4px 20px rgba(0,0,0,0.15);
  z-index: 100;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  transform: translateY(100%);
  transition: transform 0.2s ease-out;
  font-size: 0.9em;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  #nav-backdrop { background: rgba(0,0,0,0.6); }
  #nav-popup { background: #1e1e1e; box-shadow: 0 -4px 20px rgba(0,0,0,0.4); }
}

.nav-popup-close {
  position: sticky; top: 0;
  text-align: right; padding: 0.5em 0.8em;
  background: inherit;
  cursor: pointer; font-size: 1.2em; color: #888;
}

.nav-popup-list { padding: 0 0.8em 0.5em; }

.nav-popup-part {
  font-weight: bold; font-size: 1em;
  padding: 0.6em 0 0.3em; cursor: pointer;
  border-top: 1px solid #eee;
}
.nav-popup-part:first-child { border-top: none; }

.nav-popup-chapter {
  padding: 0.35em 0 0.35em 1.2em;
  cursor: pointer; color: #333;
  border-radius: 4px;
}
.nav-popup-chapter:hover { background: #f0f6fa; }

.nav-popup-current {
  background: #e8f0f8;
  font-weight: bold;
  color: #1a5276;
}

.nav-popup-interlude {
  font-style: italic;
  color: #9b59b6;
}

.nav-popup-footer {
  display: flex; gap: 0.5em; justify-content: center;
  padding: 0.6em; border-top: 1px solid #eee;
  flex-wrap: wrap;
  position: sticky; bottom: 0;
  background: inherit;
}

/* Dark mode chapter list */
@media (prefers-color-scheme: dark) {
  .nav-popup-part { border-top-color: #333; color: #e0e0e0; }
  .nav-popup-chapter { color: #ccc; }
  .nav-popup-chapter:hover { background: #2a3a4a; }
  .nav-popup-current { background: #1e3248; color: #6ba3f7; }
  .nav-popup-interlude { color: #b77fdf; }
  .nav-popup-footer { border-top-color: #333; }
}
```

### Phase 4: Breadcrumb ▾ Indicator

Add the dropdown indicator to the passive breadcrumb:

```javascript
var dropHint = document.createElement('span');
dropHint.textContent = ' ▾';
dropHint.style.cssText = 'color:#888;font-size:0.85em;';
breadcrumb.appendChild(dropHint);
```

Update `updateBreadcrumb()` to preserve the ▾ at the end:
```javascript
// At end of updateBreadcrumb():
breadcrumb.appendChild(dropHint);
```

### Phase 5: Track Current Chapter ID

The breadcrumb update logic already finds the current chapter. Store the ID in a variable accessible to `buildPopupContents`:

```javascript
var currentChapterId = '';

// Inside updateBreadcrumb(), after finding chapterId:
currentChapterId = chapterId;
```

---

## Anneal: Failure Mode Analysis

### HIGH — Will Break If Not Handled

**H1. Popup covers nav bar on small screens.**
The popup `bottom: 2.5em` assumes nav bar height. If the bar wraps to 2 lines (it shouldn't after cleanup, but safety matters), the popup overlaps.
**Mitigation:** Calculate nav bar actual height: `nav.offsetHeight + 'px'` and set popup bottom dynamically.

**H2. Touch events on mobile: tap on breadcrumb also triggers hover tooltip.**
The breadcrumb currently has `data-hover="Your current location in the book"` and `hover-nav` class. Tapping it on mobile shows a tooltip AND should open the popup.
**Mitigation:** Remove `data-hover` and `hover-nav` from the breadcrumb. The ▾ indicator communicates tappability; the popup IS the tooltip's replacement. If hover info is wanted on desktop, use `title` attribute (native, doesn't conflict).

**H3. `buildPopupContents()` runs on every open — DOM walk could be slow on low-end phones.**
The book has ~48 chapter-section elements and ~6 part-sections. DOM queries are fast for this count. But if someone adds nested details:
**Mitigation:** Use `:scope >` selectors (already in the spec) to avoid deep traversal. Benchmark: if >50ms, cache the list and invalidate on filter change.

### MEDIUM — Visible Bug But Not Fatal

**M4. Current chapter highlight wrong after rapid scrolling then immediate popup open.**
The breadcrumb update is throttled at 150ms. If you scroll fast and instantly tap, `currentChapterId` may lag.
**Mitigation:** Call `updateBreadcrumb()` synchronously at popup open time, before `buildPopupContents()`. The 150ms throttle doesn't apply to direct calls.

**M5. Popup doesn't update when Custodian filter (C button) is toggled inside the popup.**
The gBtn is now in the popup footer. Toggling it changes which chapters are visible, but the popup list was built before the toggle.
**Mitigation:** After gBtn click, call `buildPopupContents()` again to refresh the list. Or: make the popup always show all chapters regardless of filter state, with filtered-out chapters dimmed but still tappable (tapping restores the filter). The popup is a MAP of the whole book — hiding chapters from the map defeats its purpose.
**Decision:** Show all chapters always. Filtered-out chapters get `opacity: 0.4`. Tapping one resets filters and navigates. This is correct: the popup is the reader's complete view of the book.

**M6. Breadcrumb click event may conflict with individual breadcrumb link clicks.**
Currently, `makeBreadcrumbLink` creates clickable links within the breadcrumb. Clicking those navigates to parts/chapters. Now the whole breadcrumb zone triggers the popup.
**Mitigation:** Remove the individual breadcrumb links. The breadcrumb becomes plain text (non-clickable spans) with the popup as the only interaction. The popup replaces the breadcrumb links' function.

### LOW — Edge Case

**L7. Popup opened via keyboard (Enter on focused breadcrumb) needs Escape to close.**
**Mitigation:** Escape key handler already planned. Also add `tabindex="0"` and `role="button"` to breadcrumb for accessibility.

**L8. Print CSS: popup elements should not render.**
**Mitigation:** `@media print { #nav-popup, #nav-backdrop { display: none !important; } }` — same pattern as existing nav print CSS.

**L9. Deep link arrival while popup is open.**
If the user clicks a hash link that triggers `autoExpand`, the popup should close.
**Mitigation:** `hashchange` event listener calls `closePopup()`.

**L10. Back button inside popup footer: if Back is pressed while popup is open, close popup first.**
**Mitigation:** Check `popupOpen` at start of `popNavState()`. If open, `closePopup()` and return without popping.

**L11. Magnetosphere SVG positioning after nav bar height changes.**
The magnetosphere SVG is positioned relative to the nav bar (`bottom: 100%`). After removing items, the bar may be shorter, which shifts the SVG.
**Mitigation:** The bar height is already computed dynamically (`nav.offsetWidth`). The SVG wrapper's `bottom: 100%` is relative to `nav` and auto-adjusts. Test.

**L12. Multiple rapid open/close creates animation stacking.**
**Mitigation:** Check `popupOpen` state before animating. If already transitioning, skip. The `setTimeout(200)` in `closePopup` is the window — guard with a `transitioning` flag.

---

## Automated Testing Plan

The popup is a self-contained JS component inside reader.js. It interacts with the DOM via well-defined queries (`details.part-section`, `details.chapter-section`, element IDs). This makes it testable with a headless browser.

### Test Harness: Playwright

Use Playwright (already available via npm) against the built HTML served from localhost.

**Test file:** `build/tests/test-nav-popup.js`

### Test Cases

```
TC-01: Passive breadcrumb displays current location
  - Load page, scroll to a chapter mid-book
  - Assert breadcrumb text contains the chapter name
  - Assert ▾ indicator is present

TC-02: Tap breadcrumb opens popup
  - Click breadcrumb element
  - Assert #nav-popup is visible (display !== 'none')
  - Assert #nav-backdrop is visible

TC-03: Popup lists all parts and chapters
  - Open popup
  - Count .nav-popup-part elements (expect >= 4: Intro, Flat, Record, Appendices)
  - Count .nav-popup-chapter elements (expect >= 40)

TC-04: Current chapter is highlighted
  - Scroll to known chapter (e.g., #spine:three-possibilities)
  - Wait for breadcrumb update (200ms)
  - Open popup
  - Assert exactly one .nav-popup-current element exists
  - Assert its text contains "Three Possibilities"

TC-05: Tap chapter navigates and closes popup
  - Open popup
  - Click a chapter entry (e.g., one with text "The Braid")
  - Assert popup is hidden
  - Assert page scrolled to that chapter (chapter's <details> is open)

TC-06: Tap backdrop closes popup
  - Open popup
  - Click #nav-backdrop
  - Assert popup is hidden

TC-07: Escape closes popup
  - Open popup
  - Press Escape key
  - Assert popup is hidden

TC-08: Nav bar has exactly 5 elements
  - Count direct children of #reader-nav (excluding hidden tools dot)
  - Expect: backBtn, breadcrumb, shareBtn, evalBtn, topBtn
  - Assert quickJump is NOT in nav bar
  - Assert pdfBtn is NOT in nav bar

TC-09: Secondary tools are in popup footer
  - Open popup
  - Assert .nav-popup-footer contains expandBtn, gBtn, pdfBtn, tipsBtn

TC-10: Mobile viewport (375px) — bar doesn't overflow
  - Set viewport to 375x667
  - Assert #reader-nav does not scroll horizontally
  - Assert all 5 nav items are visible

TC-11: Custodian interludes styled differently
  - Open popup
  - Assert .nav-popup-interlude elements exist
  - Assert they have italic font-style

TC-12: Dark mode rendering
  - Set prefers-color-scheme: dark
  - Open popup
  - Assert popup background is dark (#1e1e1e)
  - Assert chapter text is light colored

TC-13: Filtered chapters still visible in popup (dimmed)
  - Toggle Custodian filter (C button) from popup footer
  - Assert science chapters are still in popup list
  - Assert they have reduced opacity

TC-14: Rapid open/close doesn't break state
  - Click breadcrumb 5 times rapidly
  - Assert popup is in a consistent open or closed state (not stuck mid-animation)

TC-15: Print CSS hides popup elements
  - Emulate print media
  - Assert #nav-popup display is none
  - Assert #nav-backdrop display is none
```

### Running Tests

```bash
# From relinquishment root:
npx playwright test build/tests/test-nav-popup.js --headed   # visual
npx playwright test build/tests/test-nav-popup.js            # headless CI
```

The test file will:
1. Start a local HTTP server on a free port
2. Serve `docs/downloads/Relinquishment.html`
3. Run all 15 test cases
4. Report pass/fail with screenshots on failure

### Regression Guard

After the popup ships, add the test to the build verification step so any future reader.js change that breaks navigation is caught immediately.

---

## Acceptance Criteria

1. Nav bar has exactly 5 visible items: Back, breadcrumb, §, AI Eval, ▲ Top
2. Breadcrumb shows current chapter location with ▾ indicator
3. Tapping breadcrumb opens popup with full book chapter list
4. Current chapter highlighted in popup
5. Tapping a chapter navigates to it and closes popup
6. Backdrop tap, ✕ button, and Escape all close popup
7. Secondary tools (Expand All, C, ◐, PDF, tips) accessible in popup footer
8. Works on 375px phone viewport without overflow
9. Dark mode renders correctly
10. Print CSS hides all popup/backdrop elements
11. All 15 automated tests pass
12. Bruce phone-test: can navigate the whole book from any position in under 3 taps

## Risk Assessment

**Medium risk.** This is the biggest reader.js refactor since the nav bar was built, but it's additive (popup) + subtractive (remove items from bar). No manuscript changes. No build pipeline changes. The existing `autoExpand` and `pushNavState` functions are proven and reused without modification.

The main risk is the mobile touch interaction: breadcrumb tap must reliably open the popup without triggering scroll, tooltip, or other side effects. The anneal mitigations (H2, M6) address this directly.

**Rollback:** If the popup doesn't pass Bruce's phone test, reverting is one `git revert`. The bar reverts to its current (broken but functional) state.

---

## Handoff Prompt

```
You are the Generator. Read plan 0268 in ~/software/relinquishment/plans/.
Implement all 5 phases in build/reader.js. The popup navigation replaces
the current quick-jump links and moves secondary tools into a popup footer.
Test on localhost. All changes are in reader.js — no other files.
```
