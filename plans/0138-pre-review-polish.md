# Plan 0138: Pre-Review Polish (0136 Completion)

## Context

Plans 0136 (onHover expansion) and 0137 (D-K remediation) are mostly complete. This plan closes the remaining phases of 0136 — menu tooltips (Phase 0), orphaned definition cleanup, and full QA — so Bruce can do a clean manual review of the HTML reader with everything working.

Bruce will manually improve and add SVGs after this plan completes. This plan does NOT create new SVG illustrations. It ensures everything already built is wired up and working.

**Predecessor plans:** 0136 (Phases 0, 1A, 1B, 2 complete; Phases 0, 3-partial, 4 incomplete), 0137 (complete)

## Governing Constraint

**Build must pass before this plan is considered complete.** `make dev` must produce a clean PDF and HTML. Any hovertip warnings printed during build must be resolved.

## Files

All work in `/home/bruce/software/relinquishment/`.

| File | Edit type |
|------|-----------|
| `build/hover-definitions.yaml` | Add menu-tooltip entries, clean orphans |
| `build/reader.js` | Inject `title` attributes on TOC links |
| `build/preprocess.py` | Inject `title` attributes on `<details><summary>` from YAML (if not already present) |
| `build/html.css` | Minor: TOC link title styling if needed |

## Phase 1: Menu + TOC Tooltips

**Goal:** Every clickable navigation element has a descriptive tooltip.

### Current State

The HTML has two navigation surfaces:

1. **TOC panel** (top, toggled by "Contents" button): Pandoc-generated `<nav id="TOC">` with `<ul>/<li>/<a>` links. 26 chapter links + 10 appendix links + 4 part group labels. **No tooltips on any of these.**

2. **Bottom nav bar**: Breadcrumb, § share button, Intro/Deduction/Evidence/Forgiveness quick-jump links, Top button, ←/→ expand/collapse, Back button, AI Eval button. **Most already have `title` attributes.** Check: expand/collapse and Back may be missing them.

3. **Accordion summaries**: `<details class="part-section"><summary>` elements. Some have `title` attributes (e.g., "Authors, taglines, and copyright."), some don't.

### Steps

#### 1A. Write chapter descriptions

Add a `menu-tooltips` section to `hover-definitions.yaml`. One entry per TOC link, keyed by the `href` anchor (e.g., `hook:what-would-you-do`). Value is a 1-sentence description (~60-100 chars) that tells the reader what they'll find.

**Voice:** Informational, not promotional. "Bruce discovers the mathematics behind quantum computation" not "A thrilling chapter about quantum math!" Match the book's register — literate but direct.

**Scope:** All ~36 non-appendix chapters + the 4 part group labels. Appendices get shorter functional descriptions ("Complete timeline of events, 1988–2006").

**Separate file:** `build/menu-tooltips.yaml` (NOT inside `hover-definitions.yaml` — that file is iterated by the hovertip system and a nested section would pollute `hover_lower`).

**Format:**
```yaml
# Chapter/section descriptions for TOC tooltips
# Keyed by anchor ID (without #). Value is 1 sentence.
chapters:
  "hook:what-would-you-do": "The question at the heart of this book — what would you do with a dangerous discovery?"
  "the-stack": "Eight technologies that changed the world, stacked in order of increasing impossibility."
  # ... etc

parts:
  "Front Matter": "The entry points — a question, a technology stack, and a summary."
  "Guided Deduction": "The story as Bruce experienced it, told in the order the pieces arrived."
  # ... etc
```

#### 1B. Inject tooltips on TOC links

In `reader.js`, after the TOC is found (`var toc = document.getElementById('TOC')`), iterate through all `<a>` elements inside it. For each link, extract the `href` (e.g., `#hook:what-would-you-do`), strip the `#`, and look up the description from a data object. Set it as the `title` attribute.

**Data injection approach:** `preprocess.py` injects a `<script>` block with the menu-tooltip data as a JSON object, read from the YAML `menu-tooltips` section. `reader.js` reads `window.__menuTooltips` (or similar) and applies them.

This keeps the data in YAML (single source of truth) and the logic in JS (where the DOM manipulation happens).

#### 1C. Verify bottom nav completeness

Check every element in the bottom nav bar for a `title` attribute. Add any missing ones. The expand/collapse button toggles text ("Expand All ▸" / "Close ◂") — its `title` should also toggle ("Open all chapters" / "Close all chapters"). Back button needs "Return to previous reading position" or similar.

#### 1D. Part-label tooltips

The `<span class="toc-part-label">` elements in the TOC ("Front Matter", "Guided Deduction", "The Evidence Trail", etc.) don't have tooltips. Add them — either via the same `window.__menuTooltips` mechanism or as `title` attributes on the `<span>` elements.

### Gate 1: Every navigation element (TOC links, part labels, bottom nav controls) has a `title` attribute. Hovering over any menu item shows a description.

---

## Phase 2: Orphaned Definition Cleanup

**Goal:** Every YAML entry is either used by a `\hovertip{}` call or explicitly marked as reserved.

### Current orphans (9 entries with no `\hovertip{}` call):

| YAML key | Has SVG? | Verdict |
|----------|----------|---------|
| `anyon` | YES | **ADD** `\hovertiphtml{anyon}` — appears in The Braid, Growing a Mind |
| `edge of chaos` | YES | **ADD** `\hovertiphtml{edge of chaos}` — appears in Genesis, Extension |
| `non-abelian anyon` | no | **ADD** `\hovertiphtml{non-abelian anyon}` — appears in The Braid |
| `graphene` | no | **ADD** `\hovertip{graphene}` — appears in Wormholes in the Flat or The Stack |
| `topological insulator` | no | **ADD** `\hovertiphtml{topological insulator}` — appears in The Braid or Wormholes in the Flat |
| `guided deduction` | no | **SKIP** — structural/navigational term (Part I heading), not a science concept. No `\hovertip{}` call exists. Keep in YAML for potential Bruce use. |
| `no-cloning theorem` | no | **ADD** `\hovertiphtml{no-cloning theorem}` — appears in The Factoring Game or The Braid |
| `Special Air Service` | no | **SKIP** — story content (Rule 1: no story popups). Keep definition in YAML for potential Bruce manual use. |
| `two dimensions` | no | **SKIP** — too generic as a hovertip trigger phrase. Keep in YAML. |

### Steps

1. **For each ADD verdict:** Find the first occurrence of the term in reading order (check main.tex include order). Add `\hovertip{}` or `\hovertiphtml{}` depending on whether it's in p1/p2 (hovertip) or p3 (hovertiphtml). Verify it doesn't collide with an existing hovertip (Rule 3).

2. **For each SKIP verdict:** Add a YAML comment explaining why it's intentionally unused:
   ```yaml
   # Reserved: story content (Rule 1) — may be added manually by Bruce
   Special Air Service: "..."
   ```

3. **Deduplicate `braiding` vs `anyon` SVGs.** The agent reported nearly identical SVG diagrams. If true, differentiate them: `anyon` should show the particle nature (quasiparticle labels), `braiding` should show the operation (exchange arrows, group notation). Or consolidate to one SVG and have the other be text-only. Generator decides — the criterion is: do they teach different things?

### Gate 2: Zero orphaned definitions without a comment explaining why. All ADD items have exactly one `\hovertip{}` call at first occurrence.

---

## Phase 3: Build + Full QA

**Goal:** Clean build, no warnings, all hovertips resolve, visual verification.

### Steps

#### 3A. Build

```bash
make dev
```

This runs: `generate-hover.py` → `latexmk` (PDF) → `preprocess.py` + `pandoc` (HTML).

**Expected:** Clean build. Zero `WARNING: hovertip term not in YAML` messages. Zero LaTeX errors.

If build fails: fix and re-run. Do not proceed to 3B with a broken build.

#### 3B. Automated QA checks

Run these grep/script checks on the generated HTML (`docs/downloads/Relinquishment.html`):

1. **All hovertips resolved:** `grep -c 'HOVERSTART' Relinquishment.html` → must be 0 (no unresolved markers)
2. **No duplicate hover-term spans for same term:** Extract all `data-hover-id` values, check for duplicates
3. **All menu tooltips applied:** Count `<a` tags in `<nav id="TOC">` that have `title=` attributes vs. total `<a>` tags
4. **No empty tooltips:** `grep 'data-hover=""' Relinquishment.html` → must be 0
5. **SVG integrity:** `grep -c '<svg' Relinquishment.html` → count should match expected (currently 9 inline SVGs)
6. **hover-id present on all hover-terms:** `grep -c 'class="hover-term"' Relinquishment.html` should equal `grep -c 'data-hover-id=' Relinquishment.html`

#### 3C. Visual spot-check (Generator)

Open the HTML in a browser (or read key sections) and verify:
1. Title-line panels render (Relinquishment, Wormholes, the Flat)
2. At least 3 p1/p2 hovertips show popups with correct content
3. At least 3 p3 hovertips show popups
4. A menu item shows its tooltip on hover
5. Bottom nav controls show tooltips
6. SVG diagrams render inside hover panels (magnetosphere, phase transition, anyon)
7. "Go to section →" links navigate correctly
8. Hover ID footer visible in dev build (e.g., `[magnetosphere]`)
9. First-occurrence rule works: second instance of a term renders as `<em>`, not hover-term

#### 3D. PDF spot-check

Open the PDF and verify:
1. `\hovertip{}` terms produce footnotes on first occurrence
2. `\hovertiphtml{}` terms render as italic only (no footnote)
3. No broken references or missing citations

### Gate 3: Build clean. All automated checks pass. Visual spot-check confirms system works end-to-end.

---

## Phase 4: Final Cleanup

1. **Update stale YAML comment** — the header says "95 terms planned, 47 defined." Update to actual count.
2. **Update Plan 0136** — mark all phases complete with dates
3. **Commit** — single commit: `Plan 0138: pre-review polish (menu tooltips, orphan cleanup, QA)`

### Gate 4: Committed, pushed, Bruce can `make dev` and review.

---

## Verification

1. `make dev` produces clean PDF + HTML (zero errors, zero hovertip warnings)
2. `grep -c 'HOVERSTART' docs/downloads/Relinquishment.html` → 0
3. All TOC links have `title` attributes
4. All bottom nav elements have `title` attributes
5. Zero orphaned YAML definitions without explanatory comments
6. Hover ID footers visible in dev build
7. First-occurrence rule: no duplicate `data-hover-id` values in HTML

## Scope

4 phases. ~40 menu descriptions to write. ~5 `\hovertip{}` calls to add. JS/preprocess changes for tooltip injection. Build verification. No new SVGs. No manuscript restructuring. No new chapters.

Estimated time: 2-3 hours.

## Annealing

### Pass 1 (MEDIUM): Menu description voice

The 36 chapter descriptions are the biggest creative output. Risk: they could sound like a movie trailer ("A SHOCKING revelation...") or like an academic abstract ("This chapter examines..."). Neither matches the book.

**Fix:** Generator must read 3-4 chapter openings to calibrate voice before writing descriptions. Descriptions should be informational and slightly understated — like a knowledgeable friend telling you what's in each chapter. Added voice guidance to Step 1A.

### Pass 2 (MEDIUM): Data injection architecture

The menu tooltip data needs to get from YAML → JS. Two approaches considered:
- (a) `preprocess.py` injects `title` attributes directly on `<a>` tags in the TOC during HTML post-processing
- (b) `preprocess.py` injects a `<script>` block with JSON data, `reader.js` applies them at runtime

Approach (a) is simpler and doesn't require JS changes. But the TOC is pandoc-generated — modifying it in post-processing means regex-matching `<a href="#...">` tags inside `<nav id="TOC">`. This is fragile if pandoc changes its output format.

Approach (b) is more robust but adds a coupling between preprocess.py and reader.js.

**Fix:** Use approach (a) — direct `title` injection in preprocess.py. The TOC structure is stable (pandoc has generated this format for years), and it avoids JS complexity. If pandoc ever changes, the fix is one regex update in preprocess.py. Simpler is better for a one-time setup. Data source: `build/menu-tooltips.yaml` (separate file, not inside hover-definitions.yaml — see Pass 5).

### Pass 3 (LOW): Orphan verdict accuracy

The orphan verdicts assume terms like "anyon" and "edge of chaos" actually appear in the manuscript text. If they don't appear as standalone phrases, the `\hovertip{}` call has nowhere to go. Generator must verify each term appears in the target file before adding the call.

**Fix:** Added "Generator: verify" instruction to verdicts. If a term doesn't appear in manuscript text, keep the YAML entry but don't force a hovertip — Bruce may add the term during his review.

### Pass 4 (LOW): Build time

`make dev` runs LaTeX + pandoc. On this machine, full build takes ~2-5 minutes. The plan calls for at least 2 builds (after Phase 2 edits + after Phase 3 fixes). Budget 10-15 minutes of build time.

**Fix:** No action needed — just awareness. Generator can run automated checks while PDF builds.

### Pass 5 (MEDIUM): YAML schema separation

Original plan put `menu-tooltips` as a nested section inside `hover-definitions.yaml`. But `preprocess.py` iterates all keys in that file to build `hover_lower`. A nested dict would land in the lookup table — harmless today, but a latent bug if anyone ever writes `\hovertip{menu-tooltips}` or if future code assumes all values are strings/dicts-with-text.

**Fix:** Separate file: `build/menu-tooltips.yaml`. Updated Phase 1A and annealing Pass 2 accordingly.

### Pass 6 (LOW): Orphan `guided deduction` verdict

Original verdict said "verify" — vague. Verified: no `\hovertip{}` call exists. Term is the Part I heading ("Guided Deduction"), making it structural/navigational, not a science concept. Popup on a Part heading would be confusing — that's what the menu tooltips are for.

**Fix:** Changed verdict to SKIP with clear rationale.

### Convergence

6 passes. Voice calibration (Pass 1) and architecture choice (Pass 2) are the substantive decisions. Both resolved. Orphan verification (Pass 3) is a runtime check, not a design issue. Build time (Pass 4) is logistics.

**Confidence: 9/10.** All remaining work is well-defined: write descriptions, wire them up, verify. The only creative judgment is the 36 chapter descriptions, and the voice guidance constrains that adequately. No structural risks — the hovertip system is proven and the build pipeline is stable.
