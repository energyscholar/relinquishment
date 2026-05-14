---
Plan-UID: 0320-v6 Patch E (rev 2)
Status: READY FOR GENERATOR
---

# Patch E: Aggressive Accordion Collapse

## Goal

Reduce visible scroll from ~12 pages to ~3 pages on load. Every section collapses to just its h2 heading + one closed accordion bar. All content, diagrams, puzzle/reveal boxes, and existing sub-accordions nest inside. The "Expand all" button (already in TOC) is the escape hatch.

## What to modify

File: `~/software/persistent-ai-collaboration/index.html`

## Structural pattern

Every section gets ONE new accordion immediately after the h2, wrapping EVERYTHING else:

```html
<!-- BEFORE -->
<section id="foo">
  <h2>Heading <a class="anchor-link" href="#foo" aria-hidden="true">#</a></h2>
  [all visible content, paragraphs, diagrams, etc.]
  <details id="existing-1">...</details>
  <details id="existing-2">...</details>
</section>

<!-- AFTER -->
<section id="foo">
  <h2>Heading <a class="anchor-link" href="#foo" aria-hidden="true">#</a></h2>
  <details id="new-id">
    <summary>Label <a class="anchor-link" href="#new-id" aria-hidden="true" onclick="event.stopPropagation()">#</a></summary>
    <div class="accordion-body">
      [everything that was here — paragraphs, diagrams, puzzle, reveal, lists, h3s]
      <details id="existing-1">...</details>
      <details id="existing-2">...</details>
    </div>
  </details>
</section>
```

## Important rules

- Match by CONTENT, not line numbers. Line numbers are approximate.
- Do NOT delete, rewrite, or reorder any text content.
- Do NOT modify content inside existing accordions.
- Preserve ALL existing IDs on SVGs, sections, and accordions.
- Every new `<details>` needs an `id` and an anchor link in `<summary>` with `onclick="event.stopPropagation()"`.

## Do NOT touch

- The hero SVG (stays visible — it's the hook)
- The 5 opening paragraphs (they ARE the abstract)
- The TOC nav box (stays visible — it has Expand All)
- The footer
- The References accordion in the citations section (already collapsed, not inside another section)

---

## Section 1: Shift 1 — Tool → System

Wrap EVERYTHING after the `<h2>` inside one accordion:
- The puzzle box, the paragraph after it, the reveal box
- The paragraph "This is the first shift..."
- The paragraph "A persistent AI system is not a smarter model..."
- The `<ul>` listing the three governance types
- The paragraph "These are not features to add..."
- The SVG `#svg-axes` and its wrapper
- All remaining paragraphs
- Existing accordion `#failure-matrix`
- Existing accordion `#boundary-conditions`

**ID:** `shift-1-content`
**Summary:** `Three boundary conditions — and what fails without each one`

---

## Section 2: Shift 2 — Spending → Investing

Wrap EVERYTHING after the `<h2>` inside one accordion:
- The puzzle box, intermediate paragraph, the reveal box
- The paragraph "This is the shift most people miss..."
- All h3 subsections (Typed persistent memory, Two-layer storage, Health monitoring, Anti-confabulation)
- The SVG `#svg-flow` and its wrapper
- All remaining paragraphs
- Existing accordion `#memory-file-example`
- Existing accordion `#memory-directory`
- Existing accordion `#health-monitoring`

**ID:** `shift-2-content`
**Summary:** `Four components that turn token-spending into compound investment`

---

## Section 3: Shift 3 — Worker → Judge

Wrap EVERYTHING after the `<h2>` inside one accordion:
- The puzzle box, intermediate paragraph, the reveal box
- The paragraph "The two failures demand two different structural responses..."
- h3 "Role separation: the Triad" + all its content
- The SVG `#svg-triad` and its wrapper
- h3 "Behavioral governance: Dignity Net" + all its content
- All remaining paragraphs
- Existing accordion `#dignity-net`
- Existing accordion `#triad-setup`

**ID:** `shift-3-content`
**Summary:** `The Triad, Dignity Net, and why your AI agrees when it shouldn't`

---

## Section 4: The Compartmentalization Problem

Wrap EVERYTHING after the `<h2>` inside one accordion:
- All 4 scenario paragraphs ("You're a freelance designer..." through "Stop. You just leaked...")
- The paragraphs about structural vs behavioral fixes
- The implementation `<ul>`
- The paragraphs about boundary and scaling
- The SVG `#svg-opsec` and its wrapper
- Existing accordion `#compartmentalization`

**ID:** `opsec-content`
**Summary:** `How to make cross-contamination structurally impossible`

---

## Section 5: Portfolio

Wrap EVERYTHING after the `<h2>` inside one accordion:
- The intro paragraph
- h3 "This document" + paragraph
- h3 "The Magnetosphere Tutorial" + all paragraphs + prompt block
- h3 "LLM Inference Tutorial" + all paragraphs + prompt block
- Remaining paragraphs
- Existing accordion `#tutorial-catalog`

**ID:** `portfolio-content`
**Summary:** `Two production tutorials and one document, all from this system`

---

## Section 6: The Competition

Wrap EVERYTHING after the `<h2>` inside one accordion:
- The intro paragraph
- The comparison `<table>`
- The closing paragraphs

**ID:** `competition-content`
**Summary:** `ChatGPT Memory, Mem0, MemoryGPT — and what they don't solve`

---

## Section 7: Honest Costs

Wrap EVERYTHING after the `<h2>` inside one accordion:
- h3 "The obvious question"
- All paragraphs
- h3 "This is probably not for you"
- The pro/con `<table>`
- All remaining paragraphs and lists

**ID:** `costs-content`
**Summary:** `What this costs, who it's for, and who should probably skip it`

---

## Section 8: Build It This Weekend

Wrap EVERYTHING after the `<h2>` inside one accordion:
- The intro paragraph
- All 4 tier `<div>`s with their content
- The paragraph "Start with memory..."
- h3 "Once You're Running" + all paragraphs
- Existing accordion `#directory-structure`
- Existing accordion `#memory-format`

**ID:** `build-content`
**Summary:** `15 minutes to one month — the full replication path`

---

## Update TOC

Replace the entire `<ol>` contents with clean top-level links only. Remove all `<ul>` sub-items — nested accordions are reachable via deep links but don't need TOC clutter:

```html
<ol>
 <li><a href="#shift-1">Shift 1: Tool &rarr; System</a></li>
 <li><a href="#shift-2">Shift 2: Spending &rarr; Investing</a></li>
 <li><a href="#shift-3">Shift 3: Worker &rarr; Judge</a></li>
 <li><a href="#opsec">The Compartmentalization Problem</a></li>
 <li><a href="#portfolio">Portfolio: Three Artifacts</a></li>
 <li><a href="#competition">The Competition</a></li>
 <li><a href="#honest-costs">Honest Costs</a></li>
 <li><a href="#build-it">Build It This Weekend</a></li>
 <li><a href="#references">References &amp; Architecture Notes</a></li>
</ol>
```

---

## Update deep-link JS

The existing `openHashTarget()` function uses `el.closest('details')` which only opens ONE ancestor. With nesting, it needs to open ALL ancestor `<details>` elements.

Find this block in `openHashTarget()`:
```js
var parent = el.closest('details');
if (parent) parent.setAttribute('open', '');
```

Replace with:
```js
var parent = el.closest('details');
while (parent) {
  parent.setAttribute('open', '');
  parent = parent.parentElement ? parent.parentElement.closest('details') : null;
}
```

Also: if `el` itself is a `<details>`, open it AND walk its ancestors:
```js
if (el.tagName === 'DETAILS') el.setAttribute('open', '');
var parent = el.closest('details');
while (parent) {
  parent.setAttribute('open', '');
  parent = parent.parentElement ? parent.parentElement.closest('details') : null;
}
```

Wait — `el.closest('details')` will match `el` itself if it's a `<details>`. So the existing `if (el.tagName === 'DETAILS')` line + the while-loop handles both cases. Keep both: the explicit self-open for clarity, then the while-loop for ancestors. The while-loop's first iteration will re-open `el` if it's a `<details>` — that's harmless.

---

## Verification

1. Count `<details>` elements — should be ~21 total (13 existing + 8 new)
2. On load: only h2 headings and closed accordion bars visible below the TOC. No puzzle boxes, no paragraphs, no diagrams.
3. "Expand all" button in TOC opens everything including nested accordions
4. All existing deep links (#dignity-net, #triad-setup, #failure-matrix, etc.) must still work — clicking opens BOTH parent and child accordion
5. New deep links (#shift-1-content, #shift-2-content, etc.) work
6. Print handler still opens all accordions
7. No content deleted or reordered

## Report format

"Plan-UID: 0320-v6 Patch E complete. [N] new parent accordions added. Visible on load: hero + abstract + TOC + 8 headings with closed accordions. Estimated scroll: ~3 pages."
