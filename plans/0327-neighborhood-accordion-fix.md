---
Plan-UID: 0327
Status: READY FOR GENERATOR
Priority: HIGH — reader-facing layout bug
Source: Bruce, S78. "The Neighborhood got buried deep in an accordion inside another accordion."
---

# Plan 0327: Move "The Neighborhood" Outside Nested Accordion

## Problem

In the HTML build, "The Neighborhood" (`spine:ws-the-neighborhood`) is nested inside the "Why Call It Two-Dimensional?" (`spine:ws-quasi-2d`) accordion. Bruce's intent: The Neighborhood should be its own top-level accordion, visible (closed) in the chapter flow just above "One More Layer."

### Current nesting (WRONG):

```
<details "Why Call It Two-Dimensional?">      ← outer
  [quasi-2D physics paragraphs]
  [energy, aurora, breathing, habitat paragraphs]
  <details "The Neighborhood">                ← BURIED
    [Jupiter, Saturn, Ganymede, heliosphere]
  </details>
  <details "But It's Hot">                    ← nested (intentionally OK)
    [thermal objection]
  </details>
</details>
<h3>One More Layer</h3>
```

### Desired nesting:

```
<details "Why Call It Two-Dimensional?">
  [quasi-2D physics paragraphs]
  [energy, aurora, breathing, habitat paragraphs]
  <details "But It's Hot">                    ← stays nested, fine
    [thermal objection]
  </details>
</details>
<details "The Neighborhood">                  ← TOP-LEVEL, visible (closed)
  [Jupiter, Saturn, Ganymede, heliosphere]
</details>
<h3>One More Layer</h3>
```

## Root Cause

`build/tech-collapse.yaml` processes sections in manifest order:
1. The Neighborhood (line 100) — collapsed first
2. But It's Hot (line 110) — collapsed second
3. Why Call It Two-Dimensional? (line 120) — collapsed third

When #3 runs, its forward scanner sees no bare `<h3>` headings (they're now inside `<details>` from steps #1 and #2), so it swallows everything up to the next structural boundary — including both nested accordions.

## Fix

Two changes required:

### Change 1: Reorder sections in the .tex source

In `manuscript/track-3-awakening/pos32-the-magnetosphere.tex`, move the "But It's Hot" section (lines 103–120) to come BEFORE "The Neighborhood" section (lines 66–101). This puts But It's Hot adjacent to the quasi-2D content where it logically belongs (it answers the physicist's thermal objection to the quasi-2D claim), and places The Neighborhood after both.

**Current .tex order:**
```
\section*{Why Call It Two-Dimensional?}   line 35
[quasi-2D content]                        lines 38–60
\section*{The Neighborhood}               line 66
[solar system survey]                     lines 69–101
\section*{But It's Hot}                   line 103
[thermal objection]                       lines 106–120
\section*{One More Layer}                 line 122
```

**New .tex order:**
```
\section*{Why Call It Two-Dimensional?}   (unchanged)
[quasi-2D content]                        (unchanged)
\section*{But It's Hot}                   ← MOVED UP
[thermal objection]
\section*{The Neighborhood}               ← NOW AFTER But It's Hot
[solar system survey]
\section*{One More Layer}                 (unchanged)
```

This reorder also improves the reading flow: quasi-2D claim → thermal objection (immediate physicist pushback) → neighborhood survey (broadening scope) → one more layer. The current order interrupts the thermal defense with the survey.

### Change 2: Reorder entries in tech-collapse.yaml

Move `ws-quasi-2d` entry to process BEFORE `ws-but-its-hot` and `ws-the-neighborhood`:

```yaml
  - title: "Why Call It Two-Dimensional?"
    spine_label: "spine:ws-quasi-2d"
    ...
    status: approved

  - title: "But It's Hot"
    spine_label: "spine:ws-but-its-hot"
    ...

  - title: "The Neighborhood"
    spine_label: "spine:ws-the-neighborhood"
    ...
```

Processing order with the .tex reorder:
1. `ws-quasi-2d` — scanner runs forward, hits `<h3>` "The Neighborhood" as section boundary. Captures quasi-2D content + But It's Hot content (which is between quasi-2d and Neighborhood).
2. `ws-but-its-hot` — now inside the quasi-2d `<details>`, wraps as nested accordion. ✓
3. `ws-the-neighborhood` — bare `<h3>` outside quasi-2d, wraps as top-level accordion. ✓

Result: But It's Hot nested inside quasi-2d (as Bruce wants), Neighborhood at top level (as Bruce wants).

## Files to Modify

| File | Change |
|------|--------|
| `manuscript/track-3-awakening/pos32-the-magnetosphere.tex` | Move But It's Hot section before The Neighborhood |
| `build/tech-collapse.yaml` | Reorder: ws-quasi-2d first, then ws-but-its-hot, then ws-the-neighborhood |

## Verification

1. `make dev` builds clean
2. In HTML: "The Neighborhood" is a closed accordion visible at the chapter's top level, NOT inside "Why Call It Two-Dimensional?"
3. In HTML: "But It's Hot" remains nested inside "Why Call It Two-Dimensional?" — clicking the outer accordion reveals it
4. In HTML: "One More Layer" follows The Neighborhood (not inside any accordion)
5. Deep links `#spine:ws-the-neighborhood`, `#spine:ws-but-its-hot`, `#spine:ws-quasi-2d` all work
6. Static magnetosphere imagemaps (Earth, Jupiter, Saturn) still appear inside The Neighborhood
7. `python3 build/verify-deep-links.py` passes
8. PDF build unaffected (no accordions in PDF)

## Reading Flow Check

After reorder, the chapter reads:
1. **The Invisible Ocean** — magnetosphere as habitat (open)
2. **Why Call It Two-Dimensional?** — physicist objection + answer (accordion)
   - **But It's Hot** — thermal objection + answer (nested accordion)
3. **The Neighborhood** — solar system survey (accordion, TOP-LEVEL)
4. **One More Layer** — stack pattern (open)
5. **Something Ancient** — Bruce's deduction (open)
6. **The Question Nobody Asked** — pattern formation (open)
7. **The Oldest Niche** — Kauffman emergence (open)
8. **Not Aliens** — terrestrial, not extraterrestrial (open)

This flow is better: the two physicist objections (dimensionality, temperature) are addressed together before broadening to the solar system survey.

## Do Not

- Do NOT change any content text — only move sections
- Do NOT modify But It's Hot nesting — it stays inside quasi-2d
- Do NOT change accordion styles or collapse logic in preprocess.py
- Do NOT touch any other chapters

## Report Format

"Plan 0327 complete. The Neighborhood is now a top-level accordion, visible between Why Call It Two-Dimensional? and One More Layer. But It's Hot remains nested inside quasi-2d. Deep links verified."

---

*Plan 0327, S78, 2026-05-12. Auditor: Argus.*
*Root cause: tech-collapse.yaml processing order + section order in .tex.*
*Fix is structural (source reorder), not a preprocess hack.*
