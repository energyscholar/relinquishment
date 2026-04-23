# Plan 0134b: Navigation Stack + Click-Through + Responsive (Phase B)

**Parent plan:** 0134 (onHover System Upgrade + Deep Link Navigation)
**Depends on:** 0134a (panels + bug fix) — COMPLETED
**Followed by:** 0134c (Share + Evaluate with AI + Cold-Landing)
**Session:** S52

## Purpose

Build the navigation infrastructure that makes hover panels useful for
exploration: click a panel → navigate to the target section → use Back to
return. Add responsive CSS so phone readers get the best experience. Add
URL state tracking so deep links always reflect the reader's position.

This is the skeleton. Phase C adds the flesh (share icons, evaluate flow,
cold-landing primers).

## Generator Context (REQUIRED)

Before executing this plan, the Generator MUST read:
1. This plan (0134b)
2. `build/reader.js` — the ENTIRE file (759 lines). Understand the IIFE
   structure, the Phase A hover panel system (lines 524-758), the existing
   `autoExpand()` (lines 308-342), `updateBreadcrumb()` (lines 225-267),
   and the nav bar construction (lines 72-201).
3. `build/preprocess.py` — search for `hover_replace` (~line 851). Read the
   function. You will modify it to handle extended YAML format.
4. `build/hover-definitions.yaml` — current 16 terms (all plain strings).
   You will convert 3 title-line terms to object format.
5. `build/html.css` — read the full file (187 lines). You will add to it.
6. `build/test-hover-panel.html` — the test suite. Focus on Groups 7-8,
   16-17, 20 for this phase. Groups 18-19, 21-22 test Phase C features —
   they WILL fail. Ignore them.

Do NOT read or modify any .tex files.

## 1. Extended YAML Format (preprocess.py)

In `hover_replace()`, the code currently reads all YAML values as plain
strings. Change to handle both formats:

```python
# Plain string (backward compatible):
#   autocatalytic: "definition..."
# Object with target:
#   wormholes:
#     text: "definition..."
#     target: "#pos10-the-braid"
```

In hover_replace(), after loading definitions from YAML, add type checking:

```python
for term, value in definitions.items():
    if isinstance(value, dict):
        escaped_def = html_mod.escape(value.get('text', ''))
        target = value.get('target', '')
        target_attr = f' data-hover-target="{html_mod.escape(target)}"' if target else ''
    else:
        escaped_def = html_mod.escape(str(value))
        target_attr = ''
    # ... use in span:
    f'<span class="hover-term" data-hover="{escaped_def}"{target_attr}>{term}</span>'
```

**CRITICAL:** Change ONLY hover_replace(). Do NOT touch collapse_chapters()
or any other function.

## 2. Title-Line Terms (hover-definitions.yaml)

Convert exactly 3 entries to object format. Keep all other 13 as plain strings.

```yaml
relinquishment:
  text: "Voluntarily surrendering power that cannot be taken by force — a
    decision only the powerful can make. The title asks: what would you do?"
  target: "#preface"

wormholes:
  text: "Real topological connections between distant points in a material.
    Not science fiction — condensed matter physics. The book argues these
    may exist in magnetized plasma."
  target: "#pos10-the-braid"

flat worlds:
  text: "Real two-dimensional layers inside computer chips where quantum
    effects dominate. Flatland is not a metaphor — it is the physics that
    makes your phone work."
  target: "#ch:what-is-the-flat"
```

**Use the existing definition TEXT as a starting point** — expand it to
~30-50 words if the current definition is shorter. Keep p2 reading level.
The targets are the chapter IDs from the manuscript. Do NOT change any
of the other 13 definitions.

## 3. Click-Through Link in Panels (reader.js)

Modify `showPanel()` to check for `data-hover-target`:

```javascript
function showPanel(term) {
  // ... existing panel creation code ...

  // After setting textContent, check for click-through target
  var target = term.getAttribute('data-hover-target');
  if (target) {
    var link = document.createElement('a');
    link.href = target;
    link.textContent = 'Go to section \u2192';
    link.className = 'panel-navigate';
    // Styling via .panel-navigate CSS class (html.css), no inline styles
    if (isDark) link.style.color = '#5dade2';
    link.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      dismissPanel();
      pushNavState();
      autoExpand(target);
      // URL update happens via autoExpand → scroll → updateBreadcrumb
    });
    panel.appendChild(link);
  }

  // ... rest of showPanel ...
}
```

Since showPanel currently uses `textContent` for the definition, but now
we need to append a link element, switch to: set definition via a text
node, then append the link. Do NOT switch to innerHTML for the definition
text — keep it safe.

```javascript
// Replace: panel.textContent = def;
// With:
panel.appendChild(document.createTextNode(def));
```

Then append the link element after.

## 4. Navigation Stack (reader.js)

Add BEFORE the hover panel system section (after updateBreadcrumb, before
the Hover Panel System comment). These must be available to showPanel's
click-through handler.

```javascript
// --- Navigation Stack (Plan 0134b) ---

var navStack = [];

function getExpandedIds() {
  var ids = [];
  document.querySelectorAll('details').forEach(function(d, index) {
    if (d.open) {
      var heading = d.querySelector(':scope > summary h1[id], :scope > summary h2[id], :scope > summary h3[id]');
      if (heading) ids.push(heading.id);
      else ids.push('__idx_' + index);
    }
  });
  return ids;
}

function restoreExpanded(ids) {
  var idSet = {};
  ids.forEach(function(id) { idSet[id] = true; });
  document.querySelectorAll('details').forEach(function(d, index) {
    var heading = d.querySelector(':scope > summary h1[id], :scope > summary h2[id], :scope > summary h3[id]');
    var key = heading ? heading.id : '__idx_' + index;
    d.open = !!idSet[key];
  });
}

function pushNavState() {
  var state = {
    hash: location.hash,
    scrollY: window.scrollY,
    expanded: getExpandedIds()
  };
  navStack.push(state);
  history.pushState({ navIndex: navStack.length }, '', location.hash);
  updateBackButton();
}

function popNavState() {
  if (!navStack.length) return;
  var state = navStack.pop();
  restoreExpanded(state.expanded);
  window.scrollTo(0, state.scrollY);
  if (state.hash) {
    history.replaceState(null, '', state.hash || location.pathname);
  }
  updateBackButton();
}

// Expose on window for testing (Group 17 tests check these)
window.navStack = navStack;
window.pushNavState = pushNavState;
window.popNavState = popNavState;

// Browser back support
window.addEventListener('popstate', function(e) {
  if (navStack.length > 0) {
    popNavState();
  }
});
```

## 5. Back Button (reader.js)

Add Back button to the nav bar, BEFORE the existing `nav.appendChild(breadcrumb)`:

```javascript
// Back button (hidden when nav stack empty)
var backBtn = document.createElement('button');
backBtn.id = 'nav-back';
backBtn.textContent = '\u2190 Back';
backBtn.style.cssText = 'flex:0 0 auto;padding:0.2em 0.6em;font-size:0.85em;' +
  'font-family:inherit;cursor:pointer;background:transparent;color:#1a5276;' +
  'border:1px solid #1a5276;border-radius:4px;margin-right:0.5em;' +
  'white-space:nowrap;display:none;';
backBtn.addEventListener('click', function(e) {
  e.preventDefault();
  e.stopPropagation();
  popNavState();
});

function updateBackButton() {
  backBtn.style.display = navStack.length > 0 ? 'inline-block' : 'none';
}
```

Insert `backBtn` into nav before breadcrumb:
```javascript
nav.appendChild(backBtn);     // NEW — before breadcrumb
nav.appendChild(breadcrumb);  // existing
```

## 6. URL State (reader.js)

Modify `updateBreadcrumb()` to call `history.replaceState` when the
chapter changes. Add at the END of updateBreadcrumb(), after updating
shareBtn.href:

```javascript
// URL reflects reading position
var newHash = chapterId ? '#' + chapterId : (partId ? '#' + partId : '');
if (newHash && newHash !== location.hash) {
  history.replaceState(null, '', newHash);
}
```

**CRITICAL:** Only call replaceState when newHash is non-empty AND different
from current hash. Don't strip existing hash.

## 7. Arrival Indicator (reader.js)

Modify `autoExpand()` to add `.deep-link-target` class on the target:

```javascript
function autoExpand(hash) {
  // ... existing try/catch logic to find target ...
  if (!target) return;

  // ... existing ancestor-opening loop ...

  // Arrival indicator
  target.classList.add('deep-link-target');
  setTimeout(function() {
    target.classList.remove('deep-link-target');
  }, 2500);

  target.scrollIntoView();
}
```

Add the class BEFORE scrollIntoView, remove after 2.5s (animation is 2s
plus 0.5s buffer).

## 8. CSS Additions (html.css)

Add to `build/html.css`:

```css
/* Arrival indicator (deep link target highlight) */
.deep-link-target {
  animation: highlight-pulse 2s ease-out;
}
@keyframes highlight-pulse {
  from { background-color: rgba(36, 113, 163, 0.2); }
  to { background-color: transparent; }
}

/* Scroll margin so target headings aren't hidden behind sticky nav */
h1[id], h2[id], h3[id] {
  scroll-margin-top: 3em;
}

/* Click-through link in hover panels */
.panel-navigate {
  display: block;
  margin-top: 0.5em;
  color: #2471a3;
  text-decoration: none;
  font-weight: bold;
}
.panel-navigate:hover { text-decoration: underline; }

/* Dark mode for panel links and back button */
@media (prefers-color-scheme: dark) {
  .panel-navigate { color: #5dade2; }
  #nav-back { color: #5dade2; border-color: #5dade2; }
}
```

**Extend the EXISTING `@media (max-width: 600px)` block** (line 42-43)
with additional responsive rules:

```css
@media (max-width: 600px) {
  body { padding: 0.5em; font-size: 16px; }
  /* NEW additions: */
  #reader-nav { flex-wrap: wrap; }
  #nav-breadcrumb { flex: 1 1 60%; }
  .hover-panel { max-width: calc(100vw - 16px); left: 8px !important; right: 8px; }
  details summary { padding: 0.6em 0; min-height: 44px; }
}
```

Also extend the OTHER existing 600px block (line 184-186) or consolidate
into one. Prefer consolidation — move `#nav-quickjump { display: none; }`
into the main 600px block.

## Architecture Constraints

**B1: navStack, pushNavState, popNavState MUST be exposed on `window`.**
Test Group 17 (T17.1-T17.3) checks `typeof window.navStack` etc. Without
window exposure, all nav stack unit tests skip.

**B2: restoreExpanded must not cause visible flash.**
Use diff-based restore: set each details.open based on stored set, don't
close-all-then-open. This minimizes DOM churn.

**B3: popstate handler must handle empty navStack gracefully.**
If user browser-Backs past our stack depth, popstate fires with empty
navStack. Do nothing. Don't crash. Don't break browser navigation.

**B4: replaceState in updateBreadcrumb must not fire on empty hash.**
Only call when chapterId or partId is non-empty AND different from current.
Otherwise, repeated replaceState calls with empty string strip the URL.

**B5: The navigation stack code MUST appear BEFORE the hover panel system.**
showPanel's click-through handler calls pushNavState(). If the nav stack
code is defined after the hover panel system, pushNavState is undefined
when click-through fires. Place it after updateBreadcrumb, before the
"--- Hover Panel System ---" comment.

**B6: Back button is OUTLINE style, not filled.**
Expand All is filled blue (#1a5276 background, white text). Back button is
outline (transparent background, #1a5276 border + text). This prevents visual
confusion between two adjacent blue buttons in the nav bar. In dark mode,
use `color:#5dade2; border-color:#5dade2;`.

**B7: `.panel-navigate` styled via CSS class, not inline styles.**
The link element gets `className = 'panel-navigate'` and is styled by the
CSS rule in html.css. No inline `style.cssText` on the link (except dark
mode override via isDark). Keeps styling in one place.

**B8: textContent → createTextNode migration in showPanel.**
Phase A used `panel.textContent = def`. Phase B needs to append both text
and a link element. Replace textContent assignment with
`panel.appendChild(document.createTextNode(def))`. This preserves the
safety guarantee (no innerHTML for user-provided text) while allowing
DOM element children.

## Test Verification

After building, run:

1. `make html` — must build without errors
2. Open `build/test-hover-panel.html` in browser:
   - Groups 1-6: Phase A tests — MUST STILL PASS (no regressions)
   - **Group 7**: Click-through navigation (T7.1-T7.2)
   - **Group 8**: Back button + nav stack (T8.1-T8.5)
   - Groups 9-15: Phase A tests — MUST STILL PASS
   - **Group 16**: Deep link URL state (T16.1-T16.4)
   - **Group 17**: Navigation stack unit tests (T17.1-T17.11)
   - **Group 20**: Responsive layout (T20.1-T20.2)
   - Groups 18-19, 21-22: Phase C features — WILL FAIL. Ignore them.
3. `node build/test-e2e-devices.js` — expected improvements:
   - Group 2: .deep-link-target class should now pass (arrival indicator)
   - Group 2: scroll-margin-top should now pass
   - Group 4: Phone navigation (click-through, back button) should activate
   - Group 6: Responsive layout checks may improve

## Acceptance Criteria (Phase B only)

1. hover-definitions.yaml: 3 title-line terms are objects with text + target
2. hover-definitions.yaml: other 13 terms unchanged (plain strings)
3. preprocess.py handles both string and object YAML values correctly
4. Terms with targets emit both `data-hover` and `data-hover-target`
5. Terms without targets emit only `data-hover` (no data-hover-target)
6. Panels for terms WITH target contain "Go to section →" link
7. Panels for terms WITHOUT target have definition only (no nav link)
8. Click-through link calls pushNavState → autoExpand(target)
9. navStack is a plain array exposed on `window.navStack`
10. pushNavState() exposed on `window.pushNavState`
11. popNavState() exposed on `window.popNavState`
12. pushNavState stores {hash, scrollY, expanded[]}
13. popNavState restores scroll position (±50px)
14. popNavState restores expand state (correct details open/closed)
15. Back button (#nav-back) hidden when navStack is empty
16. Back button visible after click-through
17. Back button calls popNavState on click
18. history.pushState called on pushNavState
19. popstate listener calls popNavState when stack non-empty
20. URL updates via replaceState as reader scrolls past sections
21. autoExpand adds .deep-link-target class to target
22. .deep-link-target class removed after ~2.5 seconds
23. .deep-link-target has CSS animation (background pulse)
24. scroll-margin-top on h1, h2, h3 (≥2em, clears sticky nav)
25. Responsive: .hover-panel full-width at ≤600px
26. Responsive: nav bar wraps at ≤600px
27. Responsive: summary elements ≥44px height at ≤600px
28. showPanel uses createTextNode (not textContent) + appends link element
29. No regressions: Phase A tests (Groups 1-6, 9-15) still pass
30. `make html` builds without errors

## Files Modified

| File | Change |
|---|---|
| build/reader.js | Nav stack (~60 lines), click-through in showPanel (~20 lines), Back button (~20 lines), URL state (~5 lines), arrival indicator (~5 lines), textContent→createTextNode (~2 lines) |
| build/preprocess.py | hover_replace() extended YAML handling (~10 lines) |
| build/hover-definitions.yaml | 3 title-line terms → object format |
| build/html.css | .deep-link-target animation, scroll-margin-top, .panel-navigate, responsive 600px extensions (~30 lines) |

## Files NOT Modified

| File | Why |
|---|---|
| build/generate-hover.py | PDF side unchanged |
| build/chapter-hover-descriptions.yaml | Separate system |
| build/test-hover-panel.html | Auditor's test suite — do not modify |
| build/test-e2e-devices.js | Auditor's test suite — do not modify |
| Any .tex file | No content changes |
