# Plan 0219: Collapsible Technical Sections

**Purpose:** Give GA readers a way to skip highly technical sections without losing the conclusion. Physicist-facing sections get a HIDE/SHOW toggle in HTML, default collapsed, with a p2-level tooltip on the title. Physicists click to expand. Jane never needs to.

**Motivation:** The book's primary reader (GA, non-technical) is allergic to jargon. But physicists and Dr. Chen will correctly make a fuss if technical objections aren't addressed. These audiences need opposite things from the same section. Collapsible sections let both win: GA reader sees one line with a tooltip summary; physicist opens the full argument.

**Scope:** Pilot with ONE section ("But It's Hot"). Establish the pattern. Expand to other candidates only after Bruce evaluates the pilot.

**Manifest:** `build/tech-collapse.yaml` — already created with 15 GA-AVERSE sections and 7 BORDERLINE. Each entry has `conclusion` (Auditor assessment) and `tooltip` (reader-facing text, to be drafted). Pilot uses only the "But It's Hot" entry.

---

## Red-Team Findings (pre-implementation audit)

### Issue 1: Mobile tap conflict on `<summary>` — HIGH

**Problem:** On desktop, hover shows tooltip and click toggles expand. No conflict. On mobile (Bruce's primary reading device), tap does both. If `data-hover` is on `<summary>`, reader.js's touch handler and the native `<details>` toggle compete. One eats the other's event.

**Fix:** Desktop and mobile get different behavior — simplest reliable approach:

- **Desktop:** `data-hover` on a `<span class="tech-title">` inside `<summary>`. Hover shows tooltip. Click anywhere on summary toggles expand/collapse.
- **Mobile:** Tooltip is a desktop-only enhancement. Tap on summary toggles expand/collapse (native `<details>` behavior, no interference). Mobile users who want the summary read the first sentence after expanding.

```html
<details class="tech-section">
  <summary>
    <span class="tech-title" data-hover="tooltip text">But It's Hot</span>
  </summary>
  ...
</details>
```

reader.js already skips hover panels on touch devices for term-level tooltips — verify it does the same for `tech-title` spans. If not, add a touch-device guard. No custom touch handlers needed; native `<details>` tap behavior is correct and reliable.

### Issue 2: LaTeX comment markers don't survive pandoc — MEDIUM

**Problem:** The original plan used `% TECH-COLLAPSE-END` comment markers in LaTeX. Pandoc strips LaTeX comments during conversion. The post-processing step running on HTML output would never see them.

**Fix:** Use manifest-only boundary detection. The manifest has the section label (which becomes an HTML `id`). The post-processor finds the heading by `id`, then wraps everything from that heading to the next heading of equal or higher level (`<h2>`, `<h3>`, etc.) in a `<details>` wrapper. No LaTeX source changes needed — the manifest is the single source of truth.

**Implementation:** After pandoc generates HTML, a Python post-processing step:
1. Reads `tech-collapse.yaml`
2. For each entry, finds the element with matching `id`
3. Identifies the heading level (h2, h3, etc.)
4. Collects all sibling elements until the next heading of equal or higher level
5. Wraps heading + content in `<details class="tech-section"><summary>...</summary>...</details>`

This is HTML structural parsing (using Python's `html.parser` or BeautifulSoup), not regex. Reliable because pandoc's output structure is consistent.

### Issue 3: Print stylesheet — MEDIUM

**Problem:** Collapsed `<details>` are hidden when printing the HTML version.

**Fix:** Add to `html.css`:
```css
@media print {
  details.tech-section { display: block !important; }
  details.tech-section > summary ~ * { display: block !important; }
  details.tech-section > summary::marker { content: ''; }
}
```

Also verify that reader.js's existing print-mode code (which forces `<details>` open) covers tech sections. The current `querySelectorAll('details')` is generic, so it should — but test.

### Issue 4: Deep links — NOT A PROBLEM (verified)

The existing `autoExpand()` in reader.js (L552-556) already walks ALL ancestor `<details>` generically:
```javascript
var el = target;
while (el) {
  if (el.tagName === 'DETAILS') el.open = true;
  el = el.parentElement;
}
```
No class-specific selectors in the expansion loop. Tech sections would auto-expand on deep link navigation automatically.

### Issue 5: Resilience refactor — OPTIONAL IMPROVEMENT

Bruce's `getThing(id)` pattern: build an index at init time mapping every `id` to its `<details>` ancestor chain. Reveal becomes a lookup, not a DOM walk. More resilient to future structural changes.

```javascript
// Init: build reveal index
var revealIndex = {};
document.querySelectorAll('[id]').forEach(function(el) {
  var chain = [];
  var p = el.parentElement;
  while (p) {
    if (p.tagName === 'DETAILS') chain.push(p);
    p = p.parentElement;
  }
  if (chain.length) revealIndex[el.id] = chain;
});

// Reveal any element by ID — no DOM traversal at call time
function reveal(id) {
  var chain = revealIndex[id];
  if (chain) chain.forEach(function(d) { d.open = true; });
  return document.getElementById(id);
}
```

This is a nice-to-have that makes `autoExpand()` simpler and future-proofs against any new collapsible container types. NOT required for the pilot but recommended as a Phase 1 sub-step if Generator has bandwidth.

### Issue 6: Hovertip terms inside collapsed sections — LOW

Terms with `data-hover` inside collapsed tech sections are hidden on load. When expanded, they must work. reader.js uses event delegation (hover panel appended to body, events handled at document level), so dynamically-shown content should work. Test during pilot.

---

## Design

### Reader Experience

A GA reader scrolling through "The Wrong Substrate" hits this:

```
▸ But It's Hot                                          [hover for summary]
```

One line. Hovering (desktop) or tapping the title (mobile) shows a tooltip:

> "Hot" in a collisionless plasma doesn't mean "thermally noisy." The noise that destroys quantum states is orders of magnitude quieter than the kinetic temperature. The thermal objection doesn't hold.

Clicking the triangle (or tapping outside the title text on mobile) expands the full p3 section. Clicking again collapses it.

**In PDF:** Renders normally. No collapse, no toggle. PDF readers get the full text inline. The collapsible behavior is HTML-only.

### HTML Output

```html
<details class="tech-section">
  <summary>
    <span class="tech-title" data-hover="tooltip text here">But It's Hot</span>
  </summary>
  <!-- content follows directly; no wrapper div needed -->
  ...section content...
</details>
```

Key: `data-hover` on the `<span>`, NOT on `<summary>`. Desktop: hover shows tooltip. Mobile: native tap-to-expand, no tooltip interference. No wrapper `<div>` around content — `<details>` handles visibility natively.

### CSS

```css
details.tech-section {
  border-left: 3px solid #ccc;
  margin: 1.5em 0;
  padding-left: 1em;
}
details.tech-section summary {
  cursor: pointer;
  list-style: none;  /* hide default marker, use custom */
}
details.tech-section summary::before {
  content: '▸ ';
  color: #888;
}
details.tech-section[open] summary::before {
  content: '▾ ';
}
details.tech-section .tech-title {
  font-style: italic;
  color: #555;
  border-bottom: 1px dotted #999;  /* signals "hoverable" — matches existing hovertip convention */
}
/* Dark mode */
@media (prefers-color-scheme: dark) {
  details.tech-section { border-left-color: #555; }
  details.tech-section .tech-title { color: #aaa; border-bottom-color: #666; }
}
/* Print: force all tech sections open */
@media print {
  details.tech-section { display: block !important; }
  details.tech-section > summary ~ * { display: block !important; }
  details.tech-section > summary::before { content: '' !important; }
}
```

**Style notes for Generator:**
- Match border and accent colors to existing `html.css` palette — the values above are starting points, not mandated.
- Dotted underline signals "hoverable" — matches existing hovertip convention.
- Thin left border says "optional depth" — doesn't compete with the chapter accordion.
- Unicode markers ▸ (U+25B8) and ▾ (U+25BE) — test in Safari, Chrome, Firefox.
- Verify the collapsed section doesn't create unexpected whitespace or margin gaps in the chapter flow. The collapsed state should feel like a natural pause, not a missing paragraph.

---

## Phase 1: Infrastructure + Pilot

### Step 1a: Post-processor

Add a tech-collapse post-processing step to the build pipeline. This step runs AFTER pandoc generates HTML, BEFORE the final output is written.

**Input:** HTML output + `build/tech-collapse.yaml`
**Output:** Modified HTML with matched sections wrapped in `<details class="tech-section">`

**Algorithm:**
1. Parse `tech-collapse.yaml`, collect entries with `status: approved` (or `status: live` for already-deployed)
2. Parse HTML with BeautifulSoup or `html.parser`
3. For each manifest entry, try BOTH `spine_label` and `bridge_label` — the combined HTML may contain either or both. Silently skip labels not found (handles build variants that exclude certain tracks).
   a. Find element with matching `id`
   b. Find the parent heading element (the `<h2>` or `<h3>` containing the anchor)
   c. Collect all following siblings until the next heading of equal or higher level
   d. Wrap: heading goes inside `<summary>` (with `<span class="tech-title" data-hover="...">` around title text), content goes after `<summary>`, all inside `<details class="tech-section">`
4. Write modified HTML

**Edge case — pandoc `<section>` divs:** If the build uses `--section-divs`, pandoc wraps each section in a `<section>` tag. In that case, the heading isn't followed by siblings — it's a child of `<section>` along with the content. The post-processor must detect which structure pandoc produces (sibling-walk vs. section-wrapper) and handle both. **Generator: build once with the pilot section, inspect the actual HTML structure, then implement boundary detection to match.**

**Integration:** Add as a function call in the Makefile's HTML build target, after pandoc and before final output. Or integrate into existing `preprocess.py` if that already runs post-pandoc.

### Step 1b: CSS

Add `details.tech-section` styles to `build/html.css` per the CSS section above.

### Step 1c: Deep links

Every tech-collapse section MUST have a corresponding entry in `build/deep-links.yaml` and a `\deeplink{}` macro in the LaTeX source. They go together — the collapsed title is the deep link target; the deep link auto-expands the section on navigation.

**Already have deep links (3 of 15):**
- `dl:topological-error-correction` → Topological Error Correction
- `dl:classical-constraint` → Quantum Teleportation & Classical Constraint
- `dl:buttons-and-threads` → Buttons and Threads

**Need deep links (12):**

| Section | Proposed deep link ID | Question |
|---------|----------------------|----------|
| Hasslacher's Trajectory | `dl:hasslacher-trajectory` | "Who built the mathematical bridge to topological quantum computation?" |
| Hasslacher's Lattice | `dl:hasslacher-lattice` | "How does a quantum chip talk to classical electronics?" |
| The Substrate (the-flat) | `dl:flat-substrate` | "What is the physical substrate where different physics apply?" |
| The Wormhole (the-flat) | `dl:flat-wormhole` | "How does a topological wormhole actually work?" |
| But It's Hot | `dl:but-its-hot` | "If the magnetosphere is millions of degrees, how can quantum states survive?" |
| State of Cryptography in 1990 | `dl:crypto-1990` | "Why would DARPA fund a quantum computer in 1990?" |
| ULTRA II Specifications | `dl:ultra-ii-specs` | "What would a code-breaking quantum computer need to do?" |
| From Chemistry to Computation | `dl:chemistry-to-computation` | "Can self-organization happen in a quantum substrate?" |
| Morphogenesis as Computation | `dl:morphogenesis-as-computation` | "What did Turing discover about how organisms grow?" |
| The Science Underneath | `dl:science-underneath` | "What is the science behind growing a mind instead of programming one?" |
| The Poised Realm | `dl:poised-realm` | "Can quantum effects really work at room temperature?" |
| From Emergence to Function | `dl:emergence-to-function` | "How do you get from 'it exists' to 'it's useful'?" |

**For the pilot:** Add `dl:but-its-hot` to `deep-links.yaml` and add `\deeplink{but-its-hot}` to the "But It's Hot" section in both spine and bridge LaTeX files. Remaining 11 are added when their sections are approved for collapse.

### Step 1d: Pilot manifest entry

In `build/tech-collapse.yaml`, set the "But It's Hot" entry status to `approved` and fill the `tooltip` field:

```yaml
  - title: "But It's Hot"
    spine_label: "spine:ws-but-its-hot"
    bridge_label: "pos32:but-its-hot"
    assessment: GA-AVERSE
    tooltip: >-
      "Hot" in a collisionless plasma doesn't mean "thermally noisy."
      The noise that destroys quantum states is orders of magnitude
      quieter than the kinetic temperature. The thermal objection
      doesn't hold.
    conclusion: "'Hot' in a collisionless plasma..."
    status: approved
```

All other entries remain `status: pending`.

### Step 1e: Optional — reveal index refactor

If Generator has bandwidth, refactor `autoExpand()` in reader.js to use the `revealIndex` pattern described in Issue 5. This replaces the parent-walk loop with a pre-built index lookup. Not required for pilot functionality (current code already works) but improves resilience.

### Step 1f: Commit

```
git add build/tech-collapse.yaml build/deep-links.yaml build/html.css build/preprocess.py
git add manuscript/spine/the-wrong-substrate.tex manuscript/track-3-awakening/pos32-the-magnetosphere.tex
git commit -m "Plan 0219 phase 1: collapsible tech section infrastructure + But It's Hot pilot + deep link"
```

---

## Phase 2: Build, Test, Evaluate

### Step 2a: Build and test

**Functional:**
- Build HTML output
- Verify "But It's Hot" renders collapsed by default
- Verify tooltip appears on hover over the title text (desktop)
- Verify tap toggles expand/collapse on mobile (no tooltip interference)
- Verify deep link to `#spine:ws-but-its-hot` auto-expands the section
- Verify deep link to an anchor INSIDE "But It's Hot" (e.g., a footnote) also auto-expands
- Verify "Expand All" includes tech sections; "Collapse All" re-collapses them
- Verify hovertip terms (`\hovertip{}`) inside the section work after expanding
- Verify state persistence: expand section, reload page — does it stay expanded?

**Visual:**
- Collapsed section doesn't create unexpected whitespace or margin gaps in chapter flow
- Expanded section content matches surrounding typography (font size, line height, margins)
- Left border and italic title are visually distinct but not distracting
- Dark mode renders correctly

**Cross-format:**
- PDF renders normally (no collapse markup, no missing content)
- Print stylesheet forces section open (Ctrl+P from browser)
- Both spine and bridge versions of "But It's Hot" are wrapped (check both labels matched)

### Step 2b: Bruce evaluates

Bruce reviews on phone (primary reading device). Key questions:
- Does the collapsed section feel like "optional depth" or "hidden content"?
- Is the tooltip summary sufficient for a GA reader to skip the section confidently?
- Does the visual treatment (border, italic, dotted underline, muted color) feel right?
- Is the mobile tap behavior intuitive (title = tooltip, chevron = expand)?
- Should the section title include a hint like "(technical detail)" or is the styling enough?

### Step 2c: No commit in Phase 2 — evaluation only.

---

## Phase 3: Tooltip Drafting (post-pilot approval)

After the pilot passes Bruce's evaluation, draft p2-level tooltips for all 15 GA-AVERSE sections in the manifest. Each tooltip must:
- State the conclusion, not the argument
- Use p2 vocabulary (12th-grade reading level)
- Be 1-3 sentences
- Answer the question the section title implies

This phase is a separate Generator task — one batch drafting all 15 tooltips, then Bruce reviews before any are set to `approved`.

---

## Phase 4: Rollout (post-tooltip approval)

After tooltips are approved, set entries to `status: approved` in the manifest. The post-processor automatically picks them up on next build. One commit per batch of approved sections.

---

## What NOT to change

- **Section content** — this plan changes presentation, not substance. No words added or removed.
- **LaTeX source** — no markers, no environments, no macros. All collapsible behavior is manifest-driven and applied in HTML post-processing.
- **Navigation accordion** — existing chapter/part collapse system untouched. Different CSS class, different purpose.
- **Hover-definitions.yaml** — term-level tooltips are a separate system.
- **PDF output** — identical to current. No LaTeX changes means no PDF changes.
- **autoExpand() expansion behavior** — already works generically. Optional refactor in Step 1d improves resilience but doesn't change behavior.

---

## Risk Assessment

**Low-medium risk.** The infrastructure change touches the build pipeline, but:
- Pilot is ONE section — small blast radius
- PDF output completely unaffected (no LaTeX changes at all)
- Failure mode is graceful: if post-processor fails, section renders normally (expanded, no collapse)
- Existing `<details>` infrastructure is proven
- CSS changes are purely additive
- Deep link system already handles nested `<details>` generically

**UX risk:** Collapsed sections might signal "hidden" rather than "optional." The tooltip and dotted-underline convention mitigate this. Bruce's phone evaluation (Phase 2b) is the real test.

**Mobile risk:** Mitigated by simplification — mobile gets native tap-to-expand only, no tooltip. Desktop gets both. This avoids all touch-target conflicts. If Bruce later wants mobile tooltips, that's a separate micro-plan with its own UX testing.

**Section label survival:** The `\label{}` in LaTeX becomes an `id` in HTML. If pandoc mangles the id (e.g., stripping colons from `spine:ws-but-its-hot`), the post-processor won't find it. **Generator: verify actual id attributes in pandoc output against manifest labels before implementing boundary detection.**
