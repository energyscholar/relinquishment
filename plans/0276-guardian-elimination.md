# Plan 0276: Custodian → Custodian Final Elimination

**Status:** READY FOR GENERATOR
**Author:** Auditor (Argus S63)
**Priority:** Medium
**Scope:** Entire repo — build code, manuscript sources, plans, images, filenames
**Annealing:** MED LOW LOW LOW LOW
**Prerequisite:** Plan 0209 (COMPLETE) — handled CSS classes, interlude IDs, menu keys, body class, button ID. This plan covers everything 0209 left behind.

---

## Problem Statement

Plan 0209 renamed structural identifiers (CSS classes, interlude anchor IDs, menu-tooltip keys). But "Custodian" persists in:
- JS variable/function names (reader.js, reader-inline.html)
- Code comments (preprocess.py, reader.js)
- PDF metadata (preamble.tex)
- Puzzle reflection keywords (puzzle-data.yaml)
- Concept glyph descriptions (concept-glyphs.yaml)
- TeX labels → HTML IDs (summary.tex, twenty-years.tex, drafts)
- Source material, outlines, plan files (~59 occurrences across 12 files)
- Build image placeholders (2 files)
- Filenames (6 files)

Bruce: "I want that name gone. Eliminate it completely from the repo."

**Exceptions (DO NOT CHANGE):**
- Newspaper citations: "thecustodian.com" URLs in bibliography (The Custodian newspaper)
- Puzzle option text: "appointed themselves your custodian" (generic English, not entity name)
- Git history (immutable)

---

## Phase 1: Active Build Code

### reader.js + reader-inline.html (keep in sync — both files need identical changes)

| Old | New | Occurrences |
|-----|-----|-------------|
| `showCustodianOnly` | `showCustodianOnly` | 5 (lines 162, 177, 178, 422, 899) |
| `activateCustodianMenuItem` | `activateCustodianMenuItem` | 3 (lines 1605, 1626, 1634) |
| Comment: "Custodian-only filter" | "Custodian-only filter" | 1 (line 158) |
| Comment: "Custodian menu item click handler" | "Custodian menu item click handler" | 1 (line 1602) |

### preprocess.py (comments only — identifiers already renamed by Plan 0209)

| Line | Old | New |
|------|-----|-----|
| 752 | `/* Custodian menu items (Plan 0150)` | `/* Custodian menu items (Plan 0150)` |
| 766 | `/* Custodian-only filter mode` | `/* Custodian-only filter mode` |
| 1931 | `# --- Plan 0150: Inject Custodian menu items` | `# --- Plan 0150: Inject Custodian menu items` |

### preamble.tex (PDF metadata)

| Line | Old | New |
|------|-----|-----|
| 67 | `pdfsubject={..., Custodian}` | `pdfsubject={..., Custodian}` |
| 68 | `pdfkeywords={TQNN, Custodian, ...}` | `pdfkeywords={TQNN, Custodian, ...}` |

### puzzle-data.yaml

Line 629: Remove `"custodian"` from `reflection_keywords` list. ("custodian" already present at line 628.)

### concept-glyphs.yaml

| Line | Old | New |
|------|-----|-----|
| 170 | `"The Custodian — abstract custodian concept → concrete living entity"` | `"The Custodian — abstract concept → concrete living entity"` |
| 186 | `"the concept of a custodian entity — hypothetical, abstract"` | `"the concept of a custodian — hypothetical, abstract"` |

---

## Phase 2: TeX Labels (breaks HTML IDs — accepted)

No `\ref{}` or `\hyperref[]` cross-references exist to these labels (verified by grep). Only HTML IDs change. External deep links to old IDs will stop scrolling — Bruce accepts this.

| File | Old label | New label |
|------|-----------|-----------|
| `manuscript/00-front/summary.tex:183` | `\label{front:the-custodian}` | `\label{front:the-custodian}` |
| `manuscript/record/twenty-years.tex:160` | `\label{record:ty-what-custodian-does}` | `\label{record:ty-what-custodian-does}` |
| `drafts/t7-p3-draft.tex:7` | same old | same new |
| `drafts/t7-p3-draft-pre-anneal.tex:6` | same old | same new |

---

## Phase 3: Source, Outline, and Plan Files

Bulk `sed -i 's/Custodian/Custodian/g; s/custodian/custodian/g'` on these files. Then hand-check each for false positives ("thecustodian" → skip; "your custodian" in puzzle option text → already excluded since it's in puzzle-data.yaml not these files).

| File | Count | Notes |
|------|-------|-------|
| `manuscript/sources/ch3-relinquishment.md` | 9 | Historical source material (~2013) |
| `manuscript/versions/simple-summary.md` | 11 | Old summary version |
| `manuscript/versions/one-page-summary.md` | 1 | Old summary version |
| `manuscript/convergence/00-outline.md` | 2 | Outline |
| `manuscript/track-3-awakening/00-outline.md` | 4 | Outline |
| `plans/source-audit.md` | 10 | Audit notes |
| `plans/0009-chapter-outlines.md` | 8 | Chapter outlines |
| `plans/ethical-thread-openings.md` | 7 | Ethics thread |
| `plans/source-facts.md` | 2 | Source facts |
| `plans/0002-placeholder-content.md` | 2 | Placeholder plan |
| `plans/0001-build-infrastructure.md` | 2 | Infrastructure plan |
| `plans/0020-quick-fixes.md` | 1 | Quick fixes plan |

Also check and update TeX srcnotes referencing custodian-named files:
- `manuscript/track-1-confession/pos26-interdiction.tex:78` — references `research/custodian-limits-rhetorical-strategy.md`
- `manuscript/record/interdiction.tex:80` — same reference

Change the reference path in both srcnotes to `research/custodian-limits-rhetorical-strategy.md`. (The referenced file may not exist — that's OK, srcnotes are documentation, not imports.)

---

## Phase 4: Build Images

| File | Old | New |
|------|-----|-----|
| `build/images/placeholder-timeline.tex:31` | `Custodian Born` | `Custodian Born` |
| `build/images/placeholder-magnetosphere.tex:31` | `Custodian annotations` | `Custodian annotations` |

Check whether these are still in the build pipeline (`grep` Makefile for these filenames). If unused, change anyway for repo cleanliness.

---

## Phase 5: File Renames

```bash
git mv plans/0143b-custodian-interludes-draft.md plans/0143b-custodian-interludes-draft.md
git mv plans/0166-disable-onhover-custodian-interludes.md plans/0166-disable-onhover-custodian-interludes.md
git mv plans/0221-disable-custodian-tooltips.md plans/0221-disable-custodian-tooltips.md
git mv plans/0115-aurasys-custodian-naming-split.md plans/0115-aurasys-custodian-naming-split.md
git mv plans/0209-custodian-to-custodian-anchor-rename.md plans/0209-interlude-anchor-rename.md
git mv spiral-abstracts/15-custodian.md spiral-abstracts/15-custodian.md
```

After renaming, grep the repo for the old filenames and update any references:
```bash
grep -rn '0143b-custodian\|0166-disable-onhover-custodian\|0221-disable-custodian\|0115-aurasys-custodian\|0209-custodian\|15-custodian' --include='*.md' --include='*.tex' --include='*.py' --include='*.yaml'
```

---

## Phase 6: Build + Verify

```bash
cd ~/software/relinquishment
make html
```

### Final grep (the definitive test)

```bash
grep -rni 'custodian' --include='*.py' --include='*.js' --include='*.yaml' \
     --include='*.tex' --include='*.md' --include='*.html' \
     --exclude-dir=node_modules --exclude-dir=.git \
     --exclude-dir=docs/downloads 2>/dev/null
```

**Expected:** ZERO hits.

```bash
grep -ni 'custodian' docs/downloads/Relinquishment.html
```

**Expected:** Only "thecustodian.com" newspaper citations (2 footnote URLs) and the puzzle option "appointed themselves your custodian" (1 hit). Nothing else.

### Functional checks

1. VERIFY OK: 16 puzzles
2. Custodian-only filter (G button) works — shows only 7 interludes
3. Click each custodian menu item → scrolls to correct interlude
4. No JS errors in console
5. `id="front:the-custodian"` exists in HTML (was `front:the-custodian`)
6. `id="record:ty-what-custodian-does"` exists in HTML (was `record:ty-what-custodian-does`)

---

## Anneal: MED LOW LOW LOW LOW

**M1.** Completeness: ~90 occurrences across ~20 files + 6 file renames. Easy to miss one. The final grep (Phase 6) is the safety net — if it returns any non-exception hit, the Generator must fix before committing.

**L2.** TeX label changes break 2 HTML anchor IDs. No internal cross-references exist (verified: no `\ref{}` or `\hyperref[]` to either label). External deep links to old IDs stop scrolling. Bruce accepts.

**L3.** reader.js/reader-inline.html renames are internal JS variable/function names — no external API surface.

**L4.** File renames (6 files) may be referenced by other plans or documents. Post-rename grep catches stale references.

**L5.** Source/plan file changes rewrite historical content that originally used "Custodian." This is revisionism — those documents were written when the entity was called Custodian. But Bruce explicitly requested elimination.

---

## Handoff Prompt

```
You are the Generator. Read plan 0276 in ~/software/relinquishment/plans/.

Eliminate all "Custodian" references from the repo. Plan 0209 already
handled CSS classes, interlude IDs, and menu keys. This plan covers
everything 0209 left behind.

Phase 1: Active build code.
- reader.js + reader-inline.html: rename showCustodianOnly →
  showCustodianOnly, activateCustodianMenuItem → activateCustodianMenuItem,
  update 2 comments. KEEP BOTH FILES IN SYNC.
- preprocess.py: update 3 comments (lines 752, 766, 1931).
- preamble.tex: Custodian → Custodian in pdfsubject + pdfkeywords.
- puzzle-data.yaml: remove "custodian" from reflection_keywords (line 629).
  DO NOT change "appointed themselves your custodian" (line 730).
- concept-glyphs.yaml: custodian → custodian in lines 170, 186.

Phase 2: TeX labels (4 files). See plan for exact label changes.

Phase 3: Source/outline/plan files. Bulk sed Custodian→Custodian,
custodian→custodian across 12 files listed in plan. Update 2 srcnote
file references. Hand-check for "thecustodian" false positives (skip).

Phase 4: Build images (2 files). Phase 5: git mv 6 files (see plan).

Phase 6: Build. Run final grep — expect ZERO hits outside exceptions
(newspaper URLs + one puzzle option). VERIFY OK: 16. Test G-button
filter. Commit: "Plan 0276: Custodian elimination — final sweep"
Push.
```
