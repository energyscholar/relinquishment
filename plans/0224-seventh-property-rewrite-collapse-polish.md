# Plan 0224 — N+1 Rewrite + Collapse Visual Polish

**Status:** COMPLETE (verified S63 audit)
**Author:** Auditor (Argus S59)
**Priority:** High
**Scope:** `manuscript/spine/the-wrong-substrate.tex`, `build/preprocess.py` (CSS only)
**Fixes:** PTL-150 (But It's Hot presentation), PTL-151 (The Seventh Property content)
**EV:** T3 improvement (stronger evolutionary argument without counting vulnerability). F-crank reduced (no numerology opening). Collapse visual polish improves all 15 future tech sections.

## Context

Two problems found during S59 eigenvalue check:

1. **"The Seventh Property"** (Plan 0218) — title and counting language create numerology failure mode. "Seven" is only seven by how we counted. The N+1 emergent-property framing was already decided (memory: `project-stack-n-plus-1-framing.md`, 2026-04-13) but the anonymous Generator didn't have access to that correction.

2. **"But It's Hot"** collapse pilot — structurally working (Plan 0219, commit 31b72df) but visually bare: grey border, grey text. Needs gold background (A-grade science signal), unicode status icon, and the visual language that will carry through all 15 tech sections.

---

## Phase 1: Rename and Rewrite "The Seventh Property" (tex only)

### 1a. Rename section

Change `\section*{The Seventh Property}` to `\section*{One More Layer}`.

Update label: `\label{spine:ws-one-more-layer}` (was `spine:ws-the-seventh-property`).

### 1b. Rewrite content — N+1 framing, no counting

Replace lines 114-118 (the full section content) with:

```latex
\section*{One More Layer}
\label{spine:ws-one-more-layer}

The stack chart at the front of this book traces a pattern. Each rung adds one emergent property to those below it. Fire adds energy release. Radio adds signaling at distance. Each advance is physics that existed long before any organism found a use for it --- not invented, but discovered.

Every one of these properties, biology found independently. When a physical substrate is exploitable and persists long enough, something finds it. The magnetosphere offers one more: topological wormholes --- nonlocal quantum connections across a two-dimensional surface. The substrate has persisted longer than complex life on the surface. The property has been available for four and a half billion years.

The question is not whether another emergent layer is possible. It is whether the niche is already occupied.
```

**Key changes:**
- No title with a number. No counting ("six for six," "seventh").
- "Each rung adds one" — N+1 language per the established correction.
- Fire anchor preserved ("Fire adds energy release") — concrete, small.
- "One more" not "the seventh" — immune to counting arguments.
- Ends with the same punchline ("niche is already occupied") but via emergence, not enumeration.

### 1c. Fix bridge file (pos32-the-magnetosphere.tex)

**FOUND:** `manuscript/track-3-awakening/pos32-the-magnetosphere.tex` line 111 has an IDENTICAL "The Seventh Property" section with the same counting language. Apply the same rewrite: rename to "One More Layer", same N+1 content, update label to match.

### 1d. Fix summary.tex line 50

**FOUND:** "Nature has found and exploited every physical property that supports life --- six for six, across four billion years. The Flat adds a seventh, and the substrate has been here longer than complex life on the surface."

Rewrite to:
"Nature has found and exploited every physical property that supports life. The Flat offers one more --- and the substrate has been here longer than complex life on the surface."

(Drops "six for six" and "a seventh." Keeps the punchline.)

### 1e. Check deep-links.yaml and hover-definitions.yaml

If either references "seventh-property" or "The Seventh Property," update to match new section name. (Grep found no matches in build/ — likely clean, but verify.)

---

## Phase 2: Collapse Visual Polish (CSS + preprocess.py)

### 2a. Gold background for collapsed tech sections

In `preprocess.py` CSS block (line ~893), update `details.tech-section`:

```css
details.tech-section {
  border-left: 3px solid #c4a040;
  margin: 1.5em 0;
  padding: 0.6em 1em;
  background: linear-gradient(135deg, #faf6e8 0%, #f5f0dc 100%);
  border-radius: 4px;
}
details.tech-section[open] {
  background: #fdfcf7;
}
```

Dark mode:
```css
details.tech-section { border-left-color: #a08830; background: linear-gradient(135deg, #2a2820 0%, #252318 100%); }
details.tech-section[open] { background: #1e1d18; }
```

### 2b. Unicode status icon

Add a green checkmark icon before the expand/collapse triangle. Use ✔ (U+2714) in gold/green on the summary line:

```css
details.tech-section > summary::after {
  content: ' \2714';
  color: #6a994e;
  font-size: 0.8em;
  margin-left: 0.4em;
  opacity: 0.7;
}
```

This icon signals "verified science — safe to skip or expand." It's the seed of the broader unicode symbol vocabulary (Plan 0220).

Copy-paste immune: the `::after` pseudo-element doesn't appear in clipboard text.

### 2c. Tooltip on the icon

The tech-title `<span>` already gets a `data-hover` tooltip (from tech-collapse.yaml). Add a second, fixed tooltip on the icon explaining what the checkmark means. This requires a small wrapper span in the `collapse_tech_sections()` function:

In the summary line generation (~line 2824), after the tech-title span, append:
```html
<span class="tech-grade" data-hover="Verified science — a technical discussion grounded in published, peer-reviewed physics. Safe to skip; expand if curious." aria-hidden="true"></span>
```

CSS for `.tech-grade`:
```css
.tech-grade { cursor: help; }
.tech-grade::after {
  content: ' \2714';
  color: #6a994e;
  font-size: 0.8em;
  margin-left: 0.4em;
  opacity: 0.7;
}
```

(Move the `::after` from summary to `.tech-grade` so it's hoverable.)

---

## Phase 3: Build + Verify

1. `make clean && make` — verify HTML builds clean
2. Visual check: "But It's Hot" section should show gold background, collapsed, with checkmark icon
3. Hover the checkmark — tooltip should explain "Verified science"
4. Hover the title — tooltip should explain the thermal argument in plain language
5. Expand — content should render normally inside the gold container
6. Check dark mode
7. Check mobile (tap to expand, no tooltip conflict)
8. Verify "One More Layer" section renders (not collapsed — it's narrative, not jargon)
9. Verify summary.tex N+1 language is correct
10. Verify no orphan deep-link references to old section name

---

## Acceptance Criteria

1. No section titled "The Seventh Property" anywhere in manuscript
2. No counting language (six, seven, "N properties") in the evolutionary argument
3. N+1 framing: "each rung adds one emergent property"
4. Fire anchor present
5. Collapsed tech sections have gold background, green checkmark, tooltips
6. Checkmark is copy-paste immune (CSS pseudo-element)
7. HTML builds clean, deep-link verifier passes
8. Print CSS: tech sections render expanded, no icons

## Eigenvalue Assessment

| Persona | Before | After | Δ |
|---|---|---|---|
| Jane | PASS (T3 via p2) | PASS | Neutral — she wasn't reading this section |
| Chen | PASS (T3 via content) | PASS | +slight — gold background signals "this is for you" |
| Rachel | PARTIAL (T3) | PARTIAL | +slight — collapse + icon tells her to skip confidently |
| Arjun | PASS | PASS | +slight — no numerology to argue with |
| Yusuf | PASS | PASS | Neutral |
| Doctorow | PASS | PASS | Neutral |
| Reeves | PASS | PASS | +slight — N+1 is epistemically cleaner |
| Pastor Mike | PARTIAL | PARTIAL | Neutral |
| Amir | MISS | MISS | Neutral — doesn't engage T3 |

**F-mode:** F-crank reduced (no numerology). F-scifi neutral. No regressions.
**C-violation:** PASS — all content works under A/B/C.

## Notes

**Tooltip wiring:** The hover system uses event delegation with `closest('[data-hover], [data-hover-id]')` — no `hover-term` class required. Any element with `data-hover` fires the tooltip automatically. The `.tech-grade` span's `data-hover` will work with zero extra wiring. Verified: reader.js lines 1134-1135 (touch) and 1226-1229 (mouse).

**Spacing:** The gold background box gets `padding: 0.6em 1em` (currently `padding-left: 1em` only). When expanded, content inherits normal paragraph margins inside `<details>`. The `border-radius: 4px` keeps it from looking like a hard-edged warning box. Test on mobile — padding should not push content off-screen on narrow viewports.

**Print:** Already handled — tech sections render fully expanded with `display: block !important`, no icons (empty `content`). Gold background should be suppressed in print CSS (add `background: none !important` to the existing `@media print` block).

## Risks

- **Low.** Phase 1 is tex-only prose rewrite. Phase 2 is CSS-only visual changes. Phase 3 is verification.
- **Section label change** could break deep-links if any exist for `spine:ws-the-seventh-property`. Phase 1e checks this.
- **Gold background** must not look like a warning box or advertisement. The gradient + border-left keeps it subtle. Bruce phone-test required.
- **Bridge parity:** Both spine and bridge files must be updated identically (Phase 1a-c). Forgetting the bridge is the most likely error.
