# Plan 0109: Reader Deep Link Discovery + Lower Bar Review

**Status:** COMPLETE (verified S63 audit)
**Scope:** `build/reader.js`, `build/html.css`, new `build/test-reader.html`
**Constraint:** Single-file HTML reader. All JS/CSS must work inline. No external dependencies.

---

## Problem

The reader supports ~476 deep link anchors and auto-expands ancestor `<details>` when a hash URL is followed. But there is no affordance for a reader to *discover* or *copy* a deep link. Someone discussing the book has no way to point another person to a specific chapter or section without manually inspecting the DOM.

## Objective

Make deep links discoverable and copyable through two complementary mechanisms, plus fix three minor bar issues found during review.

---

## Phase 1: Clipboard Utility (DRY refactor)

**What:** Extract the copy-to-clipboard pattern into a shared function. Currently duplicated 3× in reader.js (LLM Primer, Spiral Abstracts).

```javascript
function copyToClipboard(text, onSuccess) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(onSuccess, function() {
      fallbackCopy(text);
      onSuccess();
    });
  } else {
    fallbackCopy(text);
    onSuccess();
  }
}

function fallbackCopy(text) {
  var ta = document.createElement('textarea');
  ta.value = text;
  ta.style.cssText = 'position:fixed;left:-9999px;';
  document.body.appendChild(ta);
  ta.select();
  document.execCommand('copy');
  document.body.removeChild(ta);
}
```

Refactor existing copy buttons to call `copyToClipboard()`. No behavior change.

**Note:** The textarea fallback is essential — `navigator.clipboard` requires HTTPS or localhost. Readers opening the HTML via `file://` will hit the fallback. Keep it.

**Optional:** If the Generator judges this refactor adds noise without value, skip it and just inline the clipboard calls in Phase 2 and 3. The DRY improvement is nice but not required.

## Phase 2: Heading Link Icons (precision linking)

**What:** Each heading with an `id` attribute (`h1[id]`, `h2[id]`, `h3[id]`) gets a `#` link icon that appears on hover.

**Icon:** Use `#` character (plain text, renders everywhere, standard docs convention). Not an emoji.

**Structure:** Insert an `<a>` element as the last child of the heading:
```html
<h2 id="pos01:three-possibilities">
  What Would You Do?
  <a class="heading-link" href="#pos01:three-possibilities">#</a>
</h2>
```

The `<a>` tag serves double duty:
- **With JS:** Click intercepted → copies full URL to clipboard, shows feedback.
- **Without JS:** Right-click → "Copy link address" gives the correct anchor URL. Left-click scrolls to self (harmless).

**Click behavior — critical detail:** Many headings live inside `<summary>` elements (the details/summary collapse structure). Clicking anywhere on a `<summary>` toggles its parent `<details>` open/closed. The link icon click handler must:
1. Call `e.preventDefault()` (prevent navigation).
2. Call `e.stopPropagation()` (prevent summary toggle).

Some headings are NOT inside `<summary>` (regular flow headings). The same handler works fine — `stopPropagation` is harmless when there's no summary to toggle.

**Visibility:**
- Desktop: `opacity: 0` by default, `opacity: 0.5` on heading hover (CSS transition ~0.15s).
- Touch/mobile: `opacity: 0.3` always (no hover available). Detect via `@media (hover: none)`.

**Feedback:** After copying, briefly replace `#` with `✓` for 1.5s, then revert.

**Insertion:** Done via JS in a single pass: `document.querySelectorAll('h1[id], h2[id], h3[id]')`. Progressive enhancement — no icons if JS disabled, headings still work.

**CSS (add to html.css):**
```css
.heading-link {
  text-decoration: none;
  color: #888;
  font-size: 0.7em;
  margin-left: 0.3em;
  opacity: 0;
  transition: opacity 0.15s;
  cursor: pointer;
}
h1:hover .heading-link,
h2:hover .heading-link,
h3:hover .heading-link { opacity: 0.5; }
.heading-link:hover { opacity: 1 !important; }
@media (hover: none) { .heading-link { opacity: 0.3; } }
@media (prefers-color-scheme: dark) { .heading-link { color: #aaa; } }
```

## Phase 3: Breadcrumb Share Button (convenience linking)

**What:** A `§` icon at the trailing edge of the breadcrumb in the lower nav bar. Copies the deep link for the current reading position.

**Structure:** A single `<a>` element created once during nav bar construction, appended after the breadcrumb span. Its `href` is updated on each breadcrumb rebuild (the `updateBreadcrumb()` function already computes `chapterId` and `partId`).

**Behavior:**
- Click: copies `location.origin + location.pathname + '#' + currentId` to clipboard.
- If at the top of the page (no chapter in view): copies the base URL without hash.
- Feedback: `§` → `✓` for 1.5s, then reverts.
- `e.preventDefault()` to suppress navigation.

**Implementation:** At the end of `updateBreadcrumb()`, update the share link's `href` attribute to `'#' + (chapterId || partId || '')`. The click handler reads from `this.href` to build the full URL.

## Phase 4: Lower Bar Fixes

Three issues found during review. None require layout changes.

### 4a. Mobile overflow

The quick-jump section (`Intro · Deduction · Evidence · Agency`) has `white-space:nowrap`. On narrow screens this overflows.

**Fix (CSS):**
```css
@media (max-width: 600px) {
  #nav-quickjump { display: none; }
}
```

Hide quick-jump on mobile. The TOC button already provides part-level navigation. Simpler than abbreviating labels.

### 4b. Dark mode breadcrumb bug

The dark mode block at the bottom of reader.js sets breadcrumb link colors once at load time. But `updateBreadcrumb()` rebuilds links on every scroll — new links don't get dark mode colors.

**Fix:** In `makeBreadcrumbLink()`, check the `isDark` variable (already in scope) and set `color: '#aaa'` instead of `'#777'` when dark. Remove the breadcrumb-specific lines from the dark mode block at the bottom.

### 4c. Dark mode share button

Apply dark mode color to the new `§` share button the same way — set at creation time using `isDark`.

## Phase 5: Test Harness

**File:** `build/test-reader.html`

A minimal self-contained HTML file. No test framework. Opens in any browser.

**Mock structure:**
```html
<details class="book-section" open>
  <summary><h1 id="test-book">Test Book</h1></summary>
  <details class="part-section" open>
    <summary><h1 id="test-part">Test Part</h1></summary>
    <details class="chapter-section">
      <summary><h2 id="test-chapter">Test Chapter</h2></summary>
      <p>Content here.</p>
      <h3 id="test-section">Test Section</h3>
      <p>More content.</p>
    </details>
  </details>
</details>
```

**Load reader.js via:** `<script src="reader.js"></script>` (not inlined — easier to iterate).

**Assertions (run after DOMContentLoaded + 100ms delay for reader.js setup):**

1. **Link icons exist.** Every `h1[id], h2[id], h3[id]` has a child `.heading-link` element.
2. **Link icon href correct.** Each `.heading-link` has `href` matching `#` + parent heading's `id`.
3. **Click does not toggle details.** For a heading inside `<summary>`: record parent `<details>.open`, dispatch click event on `.heading-link`, verify `<details>.open` unchanged.
4. **Clipboard mock.** Override `navigator.clipboard.writeText` with a mock. Click a heading link. Verify mock received `location.origin + location.pathname + '#' + id`.
5. **Nav bar exists.** `document.getElementById('reader-nav')` is truthy.
6. **Share button exists.** A `§` element exists in or adjacent to `#nav-breadcrumb`.
7. **autoExpand works.** Set `location.hash = '#test-chapter'`, call autoExpand, verify all ancestor `<details>` are open.

**Output:** Each assertion prints a green `PASS: description` or red `FAIL: description` line to the page body. Count displayed at top.

**Not tested (manual):** Visual appearance, dark mode colors, touch behavior, cross-browser clipboard.

---

## Acceptance Criteria

1. Every `h1[id]`, `h2[id]`, `h3[id]` in the built HTML shows a `#` link icon on hover.
2. Clicking the icon copies full URL to clipboard and shows `✓` feedback.
3. Clicking the icon does NOT toggle the enclosing `<details>`.
4. Right-clicking the icon → "Copy link address" gives the correct anchor URL.
5. The `§` breadcrumb share button copies the current chapter's deep link.
6. The share button target updates as the user scrolls.
7. All existing copy buttons (LLM Primer, Spiral Abstracts) still work.
8. On mobile (≤600px), the nav bar doesn't overflow.
9. Dark mode breadcrumb links have correct colors after scroll-rebuild.
10. `build/test-reader.html` passes all assertions in Chrome.
11. `make html` produces a working build.

## File Changes

| File | Action |
|------|--------|
| `build/reader.js` | Modify: add clipboard utility, heading link icons, breadcrumb share, dark mode fix, refactor copy buttons |
| `build/html.css` | Modify: add `.heading-link` styles, mobile `@media` for nav, dark mode `.heading-link` |
| `build/test-reader.html` | Create: lightweight test harness |

## Execution Order

1. Phase 1 (clipboard utility + refactor existing copy buttons).
2. Phase 2 (heading link icons + CSS).
3. Phase 3 (breadcrumb share button).
4. Phase 4a-c (mobile overflow, dark mode fixes).
5. Phase 5 (test harness — write and verify).
6. `make html` and manual spot-check in browser.

**Commit:** `Plan 0109 phase 1: reader deep link discovery + lower bar fixes`
(Single commit — all phases are one coherent feature.)
