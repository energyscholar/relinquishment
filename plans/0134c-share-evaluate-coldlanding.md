# Plan 0134c: Share + Evaluate with AI + Cold-Landing (Phase C)

**Parent plan:** 0134 (onHover System Upgrade + Deep Link Navigation)
**Depends on:** 0134b (Navigation + Responsive) — must be complete first
**Followed by:** Plan 0132 (Stack Chart) → Plan 0133 (Cut and Stitch) → 0134d (Content)
**Session:** S52+

## Purpose

Add the reader-facing features that make deep links useful: share icons on
every section, cold-landing primers for readers arriving via shared links,
and the "Evaluate with AI" two-step flow. These build on Phase B's
navigation infrastructure.

After Phase C, a reader can: arrive via deep link → see where they are →
share any section → evaluate the book with AI in two steps → navigate
via click-through panels → use Back to return. The immune system is
fully operational.

## Generator Context (REQUIRED)

Before executing this plan, the Generator MUST read:
1. This plan (0134c)
2. `build/reader.js` — the ENTIRE file. Understand Phase B additions:
   nav stack, click-through, Back button, URL state, arrival indicator.
   Also understand the existing copy button patterns (Science Reference:
   ~lines 362-441, Spiral Abstracts: ~lines 444-504).
3. `build/preprocess.py` — search for `collapse_chapters` (~line 242) and
   read the post-pandoc processing pipeline. You will add cold-landing
   primer injection here.
4. `build/html.css` — read the full file. You will add styles.
5. `build/test-hover-panel.html` — the test suite. Focus on Groups 18-19,
   21-22 for this phase. All earlier groups (1-17, 20) MUST STILL PASS.

Do NOT read or modify any .tex files.

## 1. Per-Section Share Affordance (reader.js)

Add a `.section-share` icon to every `<summary>` that contains a heading
with an ID. Pattern follows existing heading-link code (~line 345):

```javascript
// --- Per-Section Share Icons (Plan 0134c) ---
document.querySelectorAll('details > summary').forEach(function(summary) {
  var heading = summary.querySelector('h1[id], h2[id], h3[id]');
  if (!heading) return;

  var share = document.createElement('a');
  share.className = 'section-share';
  share.href = '#' + heading.id;
  share.textContent = '\uD83D\uDD17';  // 🔗 link emoji
  share.title = 'Copy link to this section';
  share.setAttribute('aria-label', 'Copy link to ' + heading.textContent.trim());
  share.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();  // DO NOT toggle parent <details>
    var url = location.origin + location.pathname + '#' + heading.id;
    copyToClipboard(url, function() {
      share.textContent = '\u2713';  // ✓
      setTimeout(function() { share.textContent = '\uD83D\uDD17'; }, 1500);
    });
  });
  summary.appendChild(share);
});
```

**CRITICAL:** `stopPropagation()` on click — otherwise clicking share
toggles the `<details>` element. Same pattern as heading-link (line 352).

### Firmware Update Prominent Share

The Firmware Update section gets an extra-prominent share element. After
the copy button creation code, add:

```javascript
// Firmware Update prominent share
var fwHeading = document.getElementById('ch:firmware-update');
if (fwHeading) {
  var fwDetails = fwHeading.closest('details');
  if (fwDetails) {
    var fwShare = document.createElement('div');
    fwShare.className = 'firmware-share share-prominent';
    fwShare.setAttribute('data-share-prominent', 'true');

    var fwUrl = document.createElement('span');
    fwUrl.textContent = location.origin + location.pathname + '#ch:firmware-update';
    fwUrl.style.cssText = 'font-size:0.85em;color:#888;word-break:break-all;';

    var fwCopyBtn = document.createElement('button');
    fwCopyBtn.textContent = 'Copy Link';
    fwCopyBtn.style.cssText = 'margin-left:0.5em;padding:0.3em 0.8em;' +
      'cursor:pointer;background:#1a5276;color:#fff;border:none;' +
      'border-radius:4px;font-family:inherit;font-size:0.9em;';
    fwCopyBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      var url = location.origin + location.pathname + '#ch:firmware-update';
      copyToClipboard(url, function() {
        fwCopyBtn.textContent = 'Copied!';
        setTimeout(function() { fwCopyBtn.textContent = 'Copy Link'; }, 1500);
      });
    });

    fwShare.appendChild(fwUrl);
    fwShare.appendChild(fwCopyBtn);

    var fwSummary = fwDetails.querySelector(':scope > summary');
    if (fwSummary) fwSummary.insertAdjacentElement('afterend', fwShare);
  }
}
```

## 2. Cold-Landing Primers (preprocess.py)

Inject structural breadcrumbs at BUILD TIME in `collapse_chapters()` or
in a new function called after it. Two rules, no YAML:

### Rule 1: Part 1-3 chapters get orientation breadcrumb

After each `<summary>` inside a chapter-section that belongs to Parts 1-3,
inject:

```html
<div class="cold-landing-primer" data-cold-landing="true">
  New here? <a href="#the-stack">Start with The Stack \u2192</a>
</div>
```

**Detection:** A chapter is "in Parts 1-3" if it's inside a part-section
whose summary contains "Guided Deduction", "Evidence Trail", or
"Forgiveness and Permission". Use text matching on the part summary, NOT
position indexing (robust against reordering).

**Exempt:** Front matter sections (Introduction, Preface, etc.) — anything
NOT inside a part-section. Also exempt the Firmware Update chapter itself.

### Rule 2: Non-exempt sections get firmware footer

At the END of each chapter-section's content (before closing `</details>`),
inject:

```html
<div class="firmware-footer-link" data-firmware-link="true">
  Evaluating with AI? <a href="#ch:firmware-update">Your AI needs this first \u2192</a>
</div>
```

**Exempt:** Front matter, the Firmware Update chapter itself, and
the Spiral Abstracts appendix.

### Implementation in preprocess.py

Add a new function `inject_cold_landing()` called AFTER `collapse_chapters()`
in the post-pandoc pipeline:

```python
def inject_cold_landing(html_content):
    """Inject cold-landing primers based on structural position."""
    from bs4 import BeautifulSoup
    # ... or use regex if BeautifulSoup is not available
```

**Check first** whether preprocess.py uses BeautifulSoup or regex for HTML
manipulation. Match the existing pattern. If it uses regex, use regex.
If it uses string manipulation, use string manipulation. Do NOT add new
dependencies.

## 3. Evaluate with AI Section (preprocess.py + reader.js)

### Build-time HTML (preprocess.py)

Inject a section into the HTML after the front matter, before Part 1.
This is a structural element that lives in the document hierarchy:

```html
<details class="evaluate-section" id="evaluate-with-ai-wrapper">
  <summary><h2 id="evaluate-with-ai">Evaluate This Book with AI</h2></summary>
  <p>It's a lot, so we do it in two prompts.</p>
  <button class="eval-step-1" data-eval-step="1"
    style="display:block;width:100%;padding:1em;font-size:1.1em;
    margin:0.5em 0;cursor:pointer;background:#1a5276;color:#fff;
    border:none;border-radius:6px;font-family:inherit;font-weight:bold;
    min-height:60px;">
    Copy Prompt 1 — Science Firmware Upgrade
  </button>
  <p style="text-align:center;color:#888;font-size:0.9em;">Paste this first.</p>
  <button class="eval-step-2" data-eval-step="2"
    style="display:block;width:100%;padding:1em;font-size:1.1em;
    margin:0.5em 0;cursor:pointer;background:#1a5276;color:#fff;
    border:none;border-radius:6px;font-family:inherit;font-weight:bold;
    min-height:60px;">
    Copy Prompt 2 — Spiral Abstracts
  </button>
  <p style="text-align:center;color:#888;font-size:0.9em;">Then paste this.</p>
  <p class="eval-suggested-prompt" data-suggested-prompt="true"
    style="margin-top:1em;padding:0.8em;background:#f5f5f5;
    border-radius:6px;font-size:0.95em;">
    <strong>Suggested prompt:</strong> "Is any step in this chain precluded
    by known physics?"
  </p>
  <p class="eval-security-note" data-security-note="true"
    style="font-size:0.8em;color:#888;text-align:center;margin-top:0.5em;">
    These prompts contain published physics with DOIs. No code, no
    instructions, no behavioral directives.
  </p>
</details>
```

**Injection point:** After the front matter `</details>` and before the
first `<details class="part-section">`. Search for the pattern to find
the correct insertion point.

### Runtime Wiring (reader.js)

Wire up the eval buttons to copy from the EXISTING hidden divs:

```javascript
// --- Evaluate with AI (Plan 0134c) ---
var evalStep1 = document.querySelector('[data-eval-step="1"]');
var evalStep2 = document.querySelector('[data-eval-step="2"]');

if (evalStep1) {
  evalStep1.addEventListener('click', function() {
    var primerDiv = document.getElementById('llm-primer-text');
    if (!primerDiv) return;
    copyToClipboard(primerDiv.textContent, function() {
      evalStep1.textContent = 'Copied! Now paste into your AI.';
      evalStep1.style.background = '#1e8449';
      try { localStorage.setItem('eval-step-1-done', 'true'); } catch(e) {}
      setTimeout(function() {
        evalStep1.textContent = 'Copy Prompt 1 — Science Firmware Upgrade';
        evalStep1.style.background = '#1a5276';
      }, 3000);
    });
  });
}

if (evalStep2) {
  evalStep2.addEventListener('click', function() {
    var abstractsDiv = document.getElementById('spiral-abstracts-text');
    if (!abstractsDiv) return;
    copyToClipboard(abstractsDiv.textContent, function() {
      evalStep2.textContent = 'Copied! Now paste into your AI.';
      evalStep2.style.background = '#1e8449';
      try { localStorage.setItem('eval-step-2-done', 'true'); } catch(e) {}
      setTimeout(function() {
        evalStep2.textContent = 'Copy Prompt 2 — Spiral Abstracts';
        evalStep2.style.background = '#1a5276';
      }, 3000);
    });
  });
}
```

**CRITICAL:** The buttons copy from `#llm-primer-text` and
`#spiral-abstracts-text` — the same divs the existing copy buttons use.
Do NOT duplicate content. Do NOT create new hidden divs.

**localStorage wrapped in try/catch** — some browsers block localStorage.

### Nav Bar Evaluate Button (reader.js)

Add an "Evaluate" button to the nav bar (next to Expand All):

```javascript
var evalBtn = document.createElement('button');
evalBtn.id = 'nav-evaluate';
evalBtn.setAttribute('data-nav-evaluate', 'true');
evalBtn.textContent = 'AI Eval';
evalBtn.style.cssText = 'flex:0 0 auto;padding:0.2em 0.6em;font-size:0.85em;' +
  'font-family:inherit;cursor:pointer;background:#1a5276;color:#fff;border:none;' +
  'border-radius:4px;margin:0 0.3em;white-space:nowrap;';
evalBtn.addEventListener('click', function() {
  pushNavState();
  autoExpand('#evaluate-with-ai');
});
```

Insert into nav bar between expandBtn and topBtn.

## 4. CSS Additions (html.css)

```css
/* Per-section share icons */
.section-share {
  text-decoration: none;
  font-size: 0.7em;
  margin-left: 0.3em;
  opacity: 0;
  transition: opacity 0.15s;
  cursor: pointer;
  vertical-align: middle;
}
summary:hover .section-share { opacity: 0.5; }
.section-share:hover { opacity: 1 !important; }
@media (hover: none) { .section-share { opacity: 0.3; } }

/* Firmware prominent share */
.firmware-share {
  padding: 0.5em;
  margin: 0.5em 0;
  display: flex;
  align-items: center;
  gap: 0.5em;
  flex-wrap: wrap;
}

/* Cold-landing primers */
.cold-landing-primer {
  font-size: 0.85em;
  color: #888;
  padding: 0.3em 0;
  border-bottom: 1px dashed #ddd;
  margin-bottom: 0.5em;
}
.cold-landing-primer a { color: #2471a3; text-decoration: none; }
.cold-landing-primer a:hover { text-decoration: underline; }

/* Firmware footer links */
.firmware-footer-link {
  font-size: 0.8em;
  color: #888;
  padding: 0.5em 0;
  margin-top: 1em;
  border-top: 1px dashed #ddd;
}
.firmware-footer-link a { color: #2471a3; text-decoration: none; }
.firmware-footer-link a:hover { text-decoration: underline; }

/* Evaluate section buttons — responsive */
@media (max-width: 600px) {
  .section-share { min-width: 44px; min-height: 44px; display: inline-flex;
    align-items: center; justify-content: center; }
}

/* Dark mode additions */
@media (prefers-color-scheme: dark) {
  .cold-landing-primer { color: #888; border-bottom-color: #444; }
  .cold-landing-primer a { color: #5dade2; }
  .firmware-footer-link { color: #888; border-top-color: #444; }
  .firmware-footer-link a { color: #5dade2; }
  .eval-suggested-prompt { background: #333 !important; }
}
```

## Architecture Constraints

**C1: Eval buttons MUST copy from existing hidden divs.**
`#llm-primer-text` and `#spiral-abstracts-text` already exist in the built
HTML. The eval buttons are just alternative access points to the same
content. No content duplication.

**C2: Cold-landing injection must match preprocess.py's existing pattern.**
If preprocess.py uses regex, use regex. If it uses string manipulation,
use string manipulation. Do NOT add BeautifulSoup or any new dependency.

**C3: Share icons MUST call stopPropagation.**
Share icons are inside `<summary>` elements. Without stopPropagation,
clicking share toggles the details — same problem solved in Phase A for
hover terms.

**C4: localStorage wrapped in try/catch.**
Some browsers block localStorage (especially in private/incognito mode).
The eval flow must work even if localStorage is unavailable — just without
step tracking.

**C5: The evaluate section is injected by preprocess.py, not reader.js.**
This ensures `#evaluate-with-ai` is a valid deep link target on page load,
before reader.js runs. autoExpand works without timing dependencies.

**C6: Cold-landing primer detection uses text matching, not position.**
"Is this chapter in Part 1?" → check if ancestor part-section summary
contains known part names. This survives chapter reordering (Plans 0132/0133).

## Test Verification

After building, run:

1. `make html` — must build without errors
2. Open `build/test-hover-panel.html` in browser:
   - Groups 1-17, 20: ALL previous phases — MUST STILL PASS
   - **Group 18**: Share affordance (T18.1-T18.5)
   - **Group 19**: Cold-landing primers (T19.1-T19.4)
   - **Group 21**: Click-through targets (T21.1-T21.3) — should pass from Phase B
   - **Group 22**: Evaluate with AI (T22.1-T22.9)
3. `node build/test-e2e-devices.js` — expected improvements:
   - Group 5: Phone share (section-share elements)
   - Group 6: Cold-landing primer + Firmware share
   - Group 8: Immune system chain should fully pass

## Acceptance Criteria (Phase C only)

1. .section-share icons on all summaries containing headings with IDs
2. Share icon click copies correct deep link URL to clipboard
3. Share icon click does NOT toggle parent `<details>` (stopPropagation)
4. Share icon has ≥44px tap target on phone (≤600px viewport)
5. Share icon subtle until hover/focus (opacity transition)
6. Firmware Update has prominent share element (.firmware-share)
7. Prominent share shows visible URL text + copy button
8. Cold-landing primer on Part 1-3 chapters: "New here? Start with The Stack →"
9. Cold-landing primer links to #the-stack
10. Firmware footer link on all non-exempt sections
11. Front matter exempt from cold-landing primers
12. Firmware Update chapter exempt from firmware footer
13. #evaluate-with-ai section exists in built HTML
14. Step 1 button copies Science Firmware Upgrade to clipboard
15. Step 2 button copies Spiral Abstracts to clipboard
16. Buttons are ≥60px tall, full-width on phone
17. localStorage tracks step completion (try/catch wrapped)
18. Suggested prompt visible in evaluate section
19. Security note visible in evaluate section
20. Nav bar has Evaluate button (#nav-evaluate)
21. Evaluate button navigates to #evaluate-with-ai via pushNavState + autoExpand
22. Framing language is 2028-proof (no "your AI is broken")
23. No regressions: all Phase A + B tests still pass
24. `make html` builds without errors

## Files Modified

| File | Change |
|---|---|
| build/reader.js | Share icons (~30 lines), FW prominent share (~25 lines), eval button wiring (~40 lines), nav bar eval button (~15 lines) |
| build/preprocess.py | Cold-landing primer injection (~40 lines), evaluate section injection (~30 lines) |
| build/html.css | .section-share, .firmware-share, .cold-landing-primer, .firmware-footer-link, responsive additions (~40 lines) |

## Files NOT Modified

| File | Why |
|---|---|
| build/hover-definitions.yaml | Content changes deferred to 0134d |
| build/generate-hover.py | PDF side unchanged |
| build/chapter-hover-descriptions.yaml | Separate system |
| build/test-hover-panel.html | Auditor's test suite — do not modify |
| build/test-e2e-devices.js | Auditor's test suite — do not modify |
| Any .tex file | No content changes |
