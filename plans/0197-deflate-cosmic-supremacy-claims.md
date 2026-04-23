# Plan 0197 — Deflate cosmic-supremacy claims throughout the manuscript

**Auditor:** Argus
**Date:** 2026-04-14
**Type:** Two-step plan (Auditor proposes table → Bruce approves → Generator executes), single commit at the end.
**Sibling:** Plan 0193 did this for "most powerful" in `summary.tex` only; S55 commits `7d7a436` + `e6006ee` extended softening in `summary.tex` further. Plan 0197 now extends the move to "most important / most consequential / most powerful" across the whole book and — most importantly — renames the summary chapter title + slug.
**Governing line (Bruce):** *"This phrase is an insult & throwdown to religions. We want it fixed anywhere anyone might see it."* And: *"we can safely say 'Relinquishment might be a historically noteworthy incident'"* — i.e. dial back further than `is`→`may be`. Deflate the supremacy claim, keep the content.

---

## 1. Premise

Several sentences in the manuscript carry a cosmic-supremacy register — `the most important X of the century`, `the most consequential decision in human history`, `the most powerful technology ever created`. Each one stakes a "most-of-all-time" claim adjacent to the kind of scope religious traditions reserve for their own foundational events. To a Pastor Mike / Amir / Yusuf reader, these phrases register as throwdown — the book asserting it has displaced the Big Story.

The fix is not to hide the claim. The book is a serious book about a serious possibility. The fix is to drop the **superlative form** ("the most" / "ever") in favor of language that names the same magnitude without competing for the same shelf.

Bruce's example: `the most important event` → `a historically noteworthy incident` is the **far end** of the softening swing. The disposition table below proposes a middle: deflate from "most" / "ever" to "remarkable" / "significant" / "of historical scale" — strong enough to preserve weight, tepid enough to avoid the throwdown register.

---

## 2. Scope

In-scope: cosmic-supremacy phrasing in **prose readers actually see** — manuscript `.tex` files included in the main HTML/PDF build, plus tooltip yaml, plus one cross-cutting rename (Tier A0) that spans `.tex` / `.yaml` / `.py` / `.js` / `.html` files because a superlative LaTeX label has propagated into the JS scroll machinery and URL-fragment surface.

Out-of-scope:
- `manuscript/staging/raw/*.md` — staging area, not in build.
- `manuscript/sources/*.md` — source notes, not in book.
- `manuscript/versions/simple-summary.md` — a parallel plaintext sibling to `summary.tex`, manually swept for "most important truth of our time" and "most important event" earlier this session. **Sibling parity note:** after Generator executes A6b (summary.tex:15), check whether simple-summary.md carries the parallel "most elaborate fantasy ever constructed… or the most important true story never told" triad and sync if so. Treat as a post-execution parity check, not a blocker.
- GCHQ historical claims ("three of the most important cryptographic inventions of the twentieth century", "one of the world's most important cryptographic breakthroughs", "one of the most consequential secrets in the history of warfare") — these are about real, well-documented history, not the COWS story. They don't make the throwdown move. **KEEP.**
- "Most powerful" — already swept by Plan 0193 in summary.tex; remaining instances in other chapters fall in Tier B below.
- Build artifacts (`docs/`, `build/epub-tmp/`, `Relinquishment-plaintext.txt`, `Relinquishment.md`) — refreshed by `make dev`.

---

## 3. Disposition table — Auditor proposes; Bruce must approve before Generator executes

**Tier A0 — the summary chapter title + slug (highest-loudness surface).** The summary chapter is titled **"The Most Important Story Never Told"** and its LaTeX label is `summary:most-important-story`. This title appears in the TOC, every chapter-menu listing, the chapter-hover card, the JS scroll target, and the URL fragment that will travel when a reader shares the passage. It is the single loudest throwdown surface in the book. Renaming is a cross-cutting edit spanning 7 source files (plus `summary.aux`, which regenerates).

| # | File:Line | Current | Proposed |
|---|---|---|---|
| A0.title | `manuscript/00-front/summary.tex:7,9` | `\chapter*{The Most Important Story Never Told}` / `\addcontentsline{toc}{chapter}{The Most Important Story Never Told}` | `\chapter*{The Story Never Told}` / (same replacement in `\addcontentsline`) |
| A0.label | `manuscript/00-front/summary.tex:8` | `\label{summary:most-important-story}` | `\label{summary:story-never-told}` |
| A0.menu | `build/menu-tooltips.yaml:22` | key `"summary:most-important-story"` | `"summary:story-never-told"` |
| A0.hover-card | `build/chapter-hover-descriptions.yaml:17` | key `"summary:most-important-story"` | `"summary:story-never-told"` |
| A0.hover-defs | `build/hover-definitions.yaml:21,28` | `target: "#summary:most-important-story"` (×2) | `target: "#summary:story-never-told"` (×2) |
| A0.preprocess | `build/preprocess.py:1255` | string literal `"summary:most-important-story"` | `"summary:story-never-told"` |
| A0.reader.js | `build/reader.js:137` | `getElementById('summary:most-important-story')` | `getElementById('summary:story-never-told')` |
| A0.reader-inline | `build/reader-inline.html:138` | (same) | (same replacement) |
| A0.aux | `manuscript/00-front/summary.aux` | autogen — regenerated by `make dev`, **no hand edit** | (regenerates) |

Generator note: execute A0 as an atomic rename (all 7 source files in the same edit pass; `summary.aux` regenerates). `make dev` regenerates `summary.aux` and `build/epub-tmp/**` automatically. Verify: the reader.js jump-to-summary still works; the chapter-hover card still renders; the TOC shows the new title.

**Tier A — direct cosmic-supremacy claims (highest priority).** A6a/A6b are a twin-pair (the "three possibilities" triad is quoted identically in hook and summary).

| # | File:Line | Current | Proposed |
|---|---|---|---|
| A1 | `manuscript/00-front/introduction.tex:32` | `The most important technological and ethical event of the twenty-first century has already occurred, in secret` | `A technological and ethical event of historical scale has already occurred, in secret` |
| A2 | `manuscript/00-front/summary.tex:301` | `If Possibility~C is true, then this is the most important event of the twenty-first century.` | `If Possibility~C is true, then this is a remarkable event of the twenty-first century — and one whose implications are still arriving.` |
| A3 | `manuscript/00-front/summary.tex:334` | `or the most important precedent in human history` | `or a precedent of unusual weight` |
| A4 | `manuscript/record/record-intro.tex:5` | `Under Possibility C, it is the most important historical record of the twenty-first century.` | `Under Possibility C, it is a historical record of the twenty-first century worth taking seriously.` |
| A5a | `build/menu-tooltips.yaml:97` | `under C, the most important record of the century` | `under C, a historical record worth taking seriously` |
| A5b | `build/chapter-hover-descriptions.yaml:61` | (same string) | (same replacement) |
| A6a | `manuscript/00-front/hook.tex:42` | `a fantasy, an exaggeration, or the most important true story never told` | `a fantasy, an exaggeration, or a true story that has never been told` |
| A6b | `manuscript/00-front/summary.tex:15` | `the most elaborate fantasy ever constructed, a kernel of truth wrapped in extraordinary claims, or the most important true story never told` | `an elaborate fantasy, a kernel of truth wrapped in extraordinary claims, or a true story that has never been told` |

**Tier B — cosmic-supremacy via "most consequential / most powerful in history".** Z-restructure produced sibling pairs (spine + record / bridge + track) — both copies must be edited per row.

| # | File:Line | Current | Proposed |
|---|---|---|---|
| B1a | `manuscript/spine/three-possibilities.tex:48` | `then the most consequential decision in human history was made by fewer than ten people` | `then a decision of historical scale was made by fewer than ten people` |
| B1b | `manuscript/bridge/pos01-three-possibilities.tex:37` | (same) | (same replacement) |
| B2a | `manuscript/record/never-again.tex:73` | `Under Possibility~C, this is the most consequential act of restraint in human history.` | `Under Possibility~C, this is an act of restraint of unusual scale.` |
| B2b | `manuscript/track-3-awakening/pos25-ethical-framework.tex:72` | (same) | (same replacement) |
| B3a | `manuscript/record/the-walk-out.tex:59` | `If this is the most consequential act of scientific civil disobedience in history` | `If this is a notable act of scientific civil disobedience` |
| B3b | `manuscript/track-1-confession/pos18-the-walk-out.tex:71` | (same) | (same replacement) |
| B4a | `manuscript/record/the-surrender.tex:84` | `voluntarily placed the most powerful technology ever created in trust` | `voluntarily placed a technology of this magnitude in trust` |
| B4b | `manuscript/track-3-awakening/pos30-unipolar-condition.tex:21` | `The most powerful technology ever created has been surrendered to an autonomous entity` | `A technology of this magnitude has been surrendered to an autonomous entity` |
| B4c | `manuscript/track-3-awakening/pos27-extension.tex:83` | (same as B4b) | (same replacement) |
| B5a | `manuscript/record/never-again.tex:39` | `The enforcement mechanism for the most powerful technology on Earth is bound to a specific human rights document.` | `The enforcement mechanism for a technology of this magnitude is bound to a specific human rights document.` |
| B5b | `manuscript/track-3-awakening/pos25-ethical-framework.tex:38` | (same) | (same replacement) |
| B6a | `manuscript/record/never-again.tex:69` | `They had built the most powerful system on Earth. They could feel the corruption beginning.` | `They had built a system of this magnitude. They could feel the corruption beginning.` |
| B6b | `manuscript/track-3-awakening/pos25-ethical-framework.tex:68` | (same) | (same replacement) |

**Tier C — discretionary (Auditor inclined to leave; flag for Bruce judgement).**

| # | File:Line | Current | Auditor note |
|---|---|---|---|
| C1 | `manuscript/spine/the-code-war.tex:46` (and `bridge/pos04-the-code-war.tex:46`) | `one of the most consequential secrets in the history of warfare` | About Ultra, not about COWS. Historical claim, well-supported. The "in history of warfare" superlative is a real historians-have-said-this kind of claim. KEEP unless Bruce flags. |
| C2 | `build/hover-definitions.yaml:157,159` | `The most elite special forces unit shared by Britain and Australia` (SAS / Special Air Service entries) | About SAS, not COWS. Real claim. Throwdown register is to other special forces, not religions. KEEP unless Bruce flags. |
| C3 | `build/hover-definitions.yaml:456` | `The most manufactured device in human history` (MOSFET entry) | Industrial-scale factual claim. Not religious-throwdown register. KEEP unless Bruce flags. |

---

## 4. The principle (so Generator can apply judgement on twin-pairs)

Replace **"the most X of/in Y"** + **"ever created"** + **"in human history"** patterns with one of these moves, picked to fit the surrounding sentence:

- "a [adjective] X" — e.g. *a remarkable event*, *an act of restraint*
- "X of [historical / unusual] scale" — e.g. *a decision of historical scale*
- "X of this magnitude" — e.g. *a technology of this magnitude*
- "X worth taking seriously" — e.g. *a record worth taking seriously*

Avoid: introducing new superlatives ("greatest", "biggest", "unprecedented") in place of the old ones. The point is to leave the throwdown register, not relocate it.

Preserve: the surrounding sentence rhythm, all citations, all `\deeplink{}` and `\hovertip{}` markup, and the meaning of the claim. Only the supremacy phrase changes.

**Em-dash convention:** proposals in §3 are written with Unicode `—` for readability. When applying to `.tex` files, convert to `---` (LaTeX em-dash) to match book convention. When applying to `.yaml` / `.html` / `.md`, leave as `—`.

---

## 5. Acceptance criteria

1. Every Tier A0, Tier A, and Tier B row in §3 applied. Twin-pair rows (a/b/c) get identical treatment.
2. `grep -rnE 'most (important|consequential) (event|truth|story|record|incident|act|decision|precedent|technology|breakthrough|secret)' manuscript/ build/menu-tooltips.yaml build/chapter-hover-descriptions.yaml build/deep-links.yaml` returns **only** the Tier C row(s) Bruce kept and the GCHQ exclusions noted in §2.
3. `grep -rnE 'most powerful (technology|weapon|system)' manuscript/` returns **zero** rows in scope (`manuscript/staging/`, `manuscript/sources/` out-of-scope per §2).
4. `grep -rnE 'most (important|elaborate) (story|fantasy) (never|ever)' manuscript/ build/` returns **zero** rows.
5. A0 rename verification (run **after** `make dev` completes, so `summary.aux` and `build/epub-tmp/**` are regenerated): `grep -rn 'summary:most-important-story' manuscript/ build/` returns **zero** rows. `grep -rn 'summary:story-never-told' manuscript/ build/` returns matches in at least the 7 source files listed in Tier A0 (plus regenerated artifacts).
6. `make dev` clean — no new warnings, no broken hovertips, no broken deep links. Manually verify: (a) clicking the menu entry for the summary chapter scrolls to the new anchor; (b) the chapter-hover card still renders for the summary chapter; (c) the TOC displays the new title "The Story Never Told".
7. Tooltip parity (`build/hover-definitions.yaml` semantics): the tooltip texts in A5a/A5b retain the Three Possibilities structure (A/B/C) and only the C-clause changes.
8. Single commit. Message: `Plan 0197: deflate cosmic-supremacy claims (title rename + superlative sweep)`.

---

## 6. Lint follow-on (handoff to Plan 0196 Phase C)

Add this regex to the lint harness Plan 0196 Phase C is building:

```python
COSMIC_SUPREMACY = re.compile(
    r'\bmost (important|consequential|significant|powerful|profound) '
    r'(event|truth|story|record|incident|act|decision|precedent|'
    r'technology|weapon|breakthrough|secret) (of|in|ever)\b',
    re.IGNORECASE,
)
```

Excludes: GCHQ-context paragraphs (the lint can read the surrounding sentence and skip if "GCHQ", "Ultra", "Bletchley", or "cryptographic" appears in the same paragraph). Warn-level — lets Bruce add intentional uses with an inline `% lint-ok: cosmic` marker on the line.

This is the ratchet that prevents the phrase from being reintroduced after this sweep.

---

## 7. Order of execution

1. **Step 1 (Auditor, this plan):** §3 disposition table written. Bruce reviews and either (a) approves all rows, or (b) edits/strikes specific rows.
2. **Step 2 (Generator, after Bruce sign-off):** Apply approved rows. Run `make dev`. Verify acceptance criteria. Commit.
3. **Step 3 (later, when Plan 0196 Phase C ships):** Add §6 regex to lint harness.

---

## 8. Rollback

Single commit. `git revert <sha>` is the rollback. If the new phrasings read worse on a specific row, that row gets re-edited in a follow-up; the rest stand.

---

## 9. First Generator handoff (held until Bruce approves §3)

> You are the Generator. Execute Plan 0197 (`~/software/relinquishment/plans/0197-deflate-cosmic-supremacy-claims.md`). Apply every approved row in §3 verbatim (Bruce-approved version of the disposition table; if Bruce edited rows, use his edited text). **Tier A0 is a cross-cutting atomic rename** — apply all 7 source-file edits in a single editing pass, do NOT hand-edit `summary.aux` (make dev regenerates it), and verify the three manual checks in §5.6 before committing. Twin-pair rows (a/b/c in Tier A/B) must receive identical treatment in both files. Do not introduce new superlatives. Run `make dev`, verify the §5 grep checks return the expected results, then commit with the message in §5.8. Report back: row count applied, grep results, manual-check results for A0, build status, commit SHA.
