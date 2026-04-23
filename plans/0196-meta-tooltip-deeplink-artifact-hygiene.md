# Plan 0196 — Tooltip / Deep-Link / Artifact Hygiene (Meta)

**Auditor:** Argus
**Date:** 2026-04-14
**Type:** Meta-plan. Ships in 5 independent phases. Each phase is a separate commit + separate Generator handoff, reviewable in isolation.
**Governing principle:** **UX invariance.** Nothing in this meta-plan may change reader-visible behavior. The only reader-visible change permitted is *faster load time*. Every phase has a parity test that proves it.

---

## Problem statement

Four interlocking issues, uncovered by Bruce during content review of `build/hover-definitions.yaml`:

1. **Tooltip duplication.** Several concepts have two or three yaml entries with nearly identical rich panels (example: `the-flat-title`, `the Flat`, `flat worlds` all carry the same canonical definition, with hand-edited SVG-ID collisions avoided by renaming gradients `flat-glow` → `flat-glow2`). When Bruce finds an error he has to fix it in every copy. Plan 0195 created the latest one.
2. **Deep-link slug staleness.** Plans 0178/0179/0180/0193 softened superlative/inflammatory prose ("the most powerful technology ever created" → "a technology of this magnitude"). Deep-link slugs were not swept. Slugs are load-bearing: they're URL fragments that travel when the book goes viral. Not yet live — this is the time to get them right.
3. **Tooltip architecture is ad hoc.** There's no schema, no lint, no single-source-of-truth enforcement. Adding a tooltip is copy-and-paste. Errors propagate quietly.
4. **Unknown-state SVG assets.** Bruce: "I think we MADE SVGs and never APPLIED THEM." There may be inline or standalone SVG assets authored in prior plans that never got wired into the book. No manifest currently covers SVG-Image → usage mapping. Plus: tooltips themselves are a form of hidden content (invisible when the hover mechanism fails) — similar "authored but not delivered" content may exist elsewhere.

These compound: the yaml duplication inflates the HTML artifact; the orphaned SVGs inflate the build surface; the slug staleness misaligns URL with content; the absence of lint lets all of this accumulate silently.

---

## Answers governing the plan (Bruce, this session)

- **Easter eggs:** None designated today. Future eggs will carry literal `<easteregg>...</easteregg>` tags. Phase A must enumerate candidate "hidden content" (orphaned SVGs, unused yaml entries, defined-but-unreferenced assets) and present them to Bruce as a list + visual sheet for classification. Until Bruce approves removal of a specific item, it stays.
- **Deep-link renames:** hard rename, no redirect infrastructure needed. Book has not gone live. All \deeplink callsites updated in the same commit as the slug rename.
- **Deep-link audit scope:** mismatch sweep only. Full quality review deferred to a future pass.

---

## The five phases

**Order: A → C → B → D → E.** Lint (C) ships before the refactor (B) so the refactor's collapses land against a protective ratchet; lint's duplicate-detector directly names Phase B's target list.

### Phase A — SVG-and-orphan manifest

**Deliverable:** `build/svg-manifest.json` + `build/svg-sheet.html` (a single HTML page rendering every authored SVG asset side-by-side with its name, size, current usage, and status).

**What it inventories:**
1. Every standalone SVG file in `build/images/`.
2. Every inline SVG in `build/hover-definitions.yaml`.
3. Every inline SVG in `manuscript/**/*.tex` (there's at least one in the magnetosphere chapter per S54 notes).
4. Every SVG referenced in `manifest.json`, `chapter-hover-descriptions.yaml`, `menu-tooltips.yaml`, or the build's generated artifacts.

**For each asset it records:** id / name, source file and line, size (bytes + rough complexity: number of elements), where it's used (list of files/rich-panel keys), **status** (`applied` / `orphaned` / `unreferenced` / `referenced-but-target-missing`).

**The visual sheet** is a single `build/svg-sheet.html` file (lives in `build/`, NOT `docs/` — analysis artifact, never shipped) that Bruce opens locally in a browser, scrolls, and can visually scan. Grouped: Applied / Orphaned / Test-files. This is the surface for "hidden gems."

**Parallel inventory:** same pass catalogs any OTHER hidden assets — yaml entries with no referencing \hovertip/chapter/menu reference, .tex files not in manifest.json, test HTML files in `build/`. Emits `build/orphan-report.md`.

**No deletions in Phase A.** Output is read-only analysis. Bruce reviews, marks up, and responds with a classification list that drives Phase E decisions.

**Tests (before/after is identity — nothing changes):**
- `make dev` clean before Phase A work; clean after.
- `diff` of `Relinquishment.html` before vs after → zero lines changed.
- Manifest self-consistency: every file listed resolves; every "used by" reference resolves both ways.

**Commit:** `Plan 0196 Phase A: SVG + orphan manifest`

---

### Phase C — Lint harness

**Ships before Phase B.** Rationale: lint is a ratchet; once installed, Phase B's collapse is protected as it lands, and Phase C's duplicate-detector produces Phase B's concrete target list for free.

**Deliverable:** `make lint-hover` command (or `build/tests/lint-hover.py`) that runs all checks and exits non-zero on any failure. Hooked into existing `make dev` if one exists.

**Checks implemented:**

1. **Duplicate-content detector.** For any two entries with byte-identical `text:` or `html:` payloads, error: "entries X and Y are byte-identical; one should be `alias_of` the other."
2. **Near-duplicate detector.** For any two entries, normalize whitespace, strip inline `<svg>` blocks, hash the remainder; then compare by common-prefix length in bytes. Flag pairs sharing >500 bytes of matching prefix as warn. Avoids Levenshtein's O(n²) cost on ~10KB rich panels. Tunable threshold.
3. **Dangling `alias_of`.** Every `alias_of: foo` must resolve to an entry that lacks an `alias_of:` key (the canonical entry — convention, no flag needed).
4. **Dangling `hover_id` reference.** Every `hover_id` referenced from preprocess.py's title-panel machinery (`_title_panel_attrs`) must exist.
5. **Broken target anchor.** Every `target: "#some-anchor"` in `hover-definitions.yaml` must resolve to an `id="..."` that exists in the built `Relinquishment.html`. **Error, not warn** — a tooltip "Go to section →" button pointing at a missing anchor silently dead-ends the reader. Pre-Z-restructure anchors (`#pos32:…`, `#pos10:…`, `#pos01:…`, `#pos09:…`, `#ch:what-is-the-flat`) are the known-stale class; the Z-restructure renamed chapters and these targets did not follow. Lint must catch all of them at baseline. (Skip docstring/comment example lines — e.g. the `target: "#anchor"` placeholder at top of yaml.)
6. **Orphan yaml entry.** Any entry not referenced by any `\hovertip`, `\hovertiphtml`, `_title_panel_attrs`, `chapter-hover-descriptions.yaml`, or `menu-tooltips.yaml`. Warn, don't error (may be authored-ahead).
7. **Duplicate SVG `<defs>`.** For any two inline SVGs with identical `<defs>` blocks (gradients, markers), warn — candidate for extraction.
8. **Inconsistent-slug detector** (for Phase D support): list every `\deeplink{slug}` and confirm presence in `deep-links.yaml`. Warn on mismatch.

**Tests:**
- Run lint against current HEAD. Record baseline of errors/warnings (checked into the plan record, not into the repo).
- After Phase B collapse, lint should show zero duplicate-content errors.
- After Phase D, zero mismatched-slug warnings.

**Commit:** `Plan 0196 Phase C: hover + deep-link lint harness`

---

### Phase B — Tooltip alias refactor (single source of truth)

**Deliverable:** `hover-definitions.yaml` with one canonical entry per concept; all other entries are lightweight aliases resolved at build time by `preprocess.py`.

**Schema.** Entries become one of three shapes. Convention: an entry without an `alias_of:` key IS canonical — no separate flag needed.

```yaml
# (1) Canonical — holds the text/html/svg payload
the-flat-title:
  hover_id: "the-flat-title"
  target: "#ch:what-is-the-flat"
  text: "..."
  html: |
    <p>...</p>
    <svg>...</svg>

# (2) Alias — points at a canonical entry. No payload.
"the Flat":
  alias_of: the-flat-title

"flat worlds":
  alias_of: the-flat-title

# (3) Simple string — unchanged, remains valid (preserves existing entries)
entanglement: "Two particles linked so that ..."
```

**Preprocess.py change.** Resolve `alias_of` at load time: replace the alias value with the canonical entry's payload (text/html/svg/target), keeping the alias's surface term as the lookup key. Hovertip macros using the alias emit the canonical content.

**Risk (explicit test coverage required):** preprocess.py tracks first-occurrence across files via `hover_seen`. When aliases share a canonical `hover_id`, first-occurrence logic may fire on whichever surface term appears first, potentially leaving later prose mentions unannotated. `tooltip-parity.py` must include test cases that exercise multi-surface-term concepts (e.g., "the Flat" appearing BEFORE "flat worlds" in reading order, and vice versa) to confirm every currently-hovertipped first-occurrence still renders post-refactor.

**Dedup sweep.** Collapse the following known duplicate triples/pairs (not exhaustive; Phase C lint will catch more):

| Canonical | Aliases collapsed into it |
|---|---|
| `the-flat-title` | `the Flat`, `flat worlds` |
| `wormholes-title` | `wormholes` (IF content matches — audit first; they may be intentionally different) |
| `two-dimensional-electron-gas` | `2DEG`, `two-dimensional electron gas` |
| `nonlocal` | (standalone; verify no duplicate exists) |
| `relinquishment-title` | (add any prose-form aliases that exist) |
| `TQNN` | check for other TQNN mentions |

For each collapse, Generator reads BOTH entries first and reports any semantic divergence before collapsing. If content disagrees, the collapse pauses; Auditor picks which version is canonical.

**SVG de-duplication.** When an alias is collapsed, its inline SVG (with its renamed gradient/marker IDs like `flat-glow2`, `flat-arr2`) is deleted. Only the canonical entry's SVG remains. This directly shrinks the yaml.

**Tests (parity):**
- New script `build/tests/tooltip-parity.py`: for every term currently carrying a hovertip in the manuscript, snapshot the rendered hover content (text + html). **Before-snapshot is taken at the pre-phase commit SHA** (recorded in the phase's handoff) — NOT at whatever moment Generator happens to start. After-snapshot is taken post-refactor at HEAD. Diff must be empty.
- `Relinquishment.html` size before/after — record both. Expected: smaller.
- `hover-definitions.yaml` byte count before/after — record both.
- `grep -c "<svg" hover-definitions.yaml` before/after — expected: decrease by N where N = number of aliased SVG duplicates.
- `make dev` clean.

**Commit:** `Plan 0196 Phase B: tooltip alias refactor`

---

### Phase D — Deep-link mismatch sweep

**Deliverable:** Every \deeplink slug whose framing clashes with the softened book tone is renamed; every \deeplink callsite updated; deep-links.yaml updated.

**Method (two steps, separate commits):**

**Step D1 (Auditor, read-only):** Assemble a per-slug table: `slug | question text | current book voice for referenced passage | verdict (keep/rename) | proposed new slug`. Verdict driven by: does the slug's own wording commit to a superlative, claim, or tone that the book no longer makes? Deliver the table to Bruce for review/approval before any renames land.

**Step D2 (Generator, after Bruce approves the table):** Execute the approved renames — hard rename, no redirect alias; `deep-links.yaml` and all `\deeplink{old}` callsites updated in the same commit.

Known candidates (pre-audit, for scoping; the actual list emerges from Step D1):
   - `all-your-electricity` — meme intentional per prior plans; likely **keep** (joke is load-bearing under C, and the prose around it survived softening). But verify the surrounding prose first; if the meme now reads as a tonal outlier, flag.
   - `udhr-as-cage` — "cage" is loaded; may not match softened custodian framing.
   - `ten-thousand-kept-it` — framed as a skeptic question, probably fine.
   - Others surface from diffing against plans 0178/0179/0180/0193.

**New-slug criteria** (applied in Step D1 when proposing renames): (a) matches current prose, (b) memorable as a URL fragment (hyphenated, lowercase, ~3–5 words), (c) self-documenting for a cold visitor.

**Tests:**
- `grep -rh "\\\\deeplink{" manuscript/ | sort -u` before/after — slugs match exactly the keys in `deep-links.yaml`.
- Lint from Phase C runs clean.
- `make dev` clean.
- Spot-check 3 renamed slugs in the built HTML: anchor resolves, content unchanged.

**Commit:** `Plan 0196 Phase D: deep-link slugs aligned with softened prose`

---

### Phase E — Artifact size reduction + hidden-content decisions

**Deliverable:** Smaller `Relinquishment.html` and `hover-definitions.yaml`, with Bruce's orphan classifications from Phase A applied.

**Method:**
1. Apply Bruce's Phase-A decisions: for each orphaned asset, either delete / link into manuscript / leave as dormant (tagged as such in the new `svg-manifest.json`).
2. Run preprocess.py with alias resolution (Phase B) in size-optimized mode: where practical, extract shared `<defs>` (gradients/markers) so identical definitions are emitted once and referenced across panels. Primary size gain comes from Phase B's alias-collapse; shared-defs extraction is secondary and only applied where it doesn't require invasive rewrites.
3. Compress trailing whitespace + redundant comments in generated artifacts, preserving any `<easteregg>` block verbatim.
4. Measure: report before/after sizes of `Relinquishment.html`, `hover-definitions.yaml`, and the `docs/` tree.

**Tests (UX invariance is absolute here):**
- `tooltip-parity.py` diff empty.
- HTML text-content diff: extract visible text (strip tags, normalize whitespace) from `Relinquishment.html` before and after — must be empty. Inline-SVG diff: structural comparison of SVG payloads (element counts + attribute sets) — equal. (Headless-browser pixel diff is optional and only worth running if the text/structural diffs flag something ambiguous.)
- Performance: record initial-paint time on a cold load for the HTML; should be same-or-faster.

**Commit:** `Plan 0196 Phase E: artifact size reduction, UX-invariant`

---

## Order of operations

Phases A → C → B → D → E, strictly sequential. No phase starts before the previous is merged and Bruce has reviewed. Phase C (lint) lands before Phase B (refactor) so the refactor's collapses drop onto a protective ratchet; Phase C's duplicate-detector output becomes Phase B's concrete target list.

Phase A is **read-only analysis** and can ship before all others are planned in detail. The other phase-plans may be refined after Phase A's findings surface unexpected issues.

---

## Global acceptance criteria

For the whole 0196 meta-plan:
1. Every known tooltip duplication collapsed; yaml has one source of truth per concept.
2. Deep-link slugs align with current book prose.
3. Lint catches regressions; `make lint-hover` exists and passes at HEAD.
4. `Relinquishment.html` byte-size smaller; tooltip parity test passes (content unchanged).
5. SVG manifest exists, is correct, and Bruce has reviewed the visual sheet.
6. No user-facing behavior change other than (possibly) faster initial load.

---

## Non-goals

- No new tooltip content.
- No tonal/prose edits beyond what Phase D rename requires in `deep-links.yaml`.
- No change to chapter structure, front matter order, or track layout.
- No changes to `docs/` infrastructure (CNAME, 404, etc.).
- No refactor of preprocess.py beyond the `alias_of` support and any lint wiring.
- No work on ebook/print outputs — HTML target only (for now; the yaml changes benefit them too, no work needed).

---

## Rollback

Each phase is a single commit. `git revert <sha>` is the rollback. The parity tests and lint make a silent regression unlikely to escape review.

---

## First Generator handoff (Phase A only, read-only)

> You are the Generator. Execute Plan 0196 Phase A only (§ "Phase A — SVG-and-orphan manifest" in `~/software/relinquishment/plans/0196-meta-tooltip-deeplink-artifact-hygiene.md`). Build `build/svg-manifest.json` and `build/svg-sheet.html` per the deliverable spec. No yaml or tex edits, no deletions. Commit: "Plan 0196 Phase A: SVG + orphan manifest". Report back: (a) how many SVG assets found and in which categories, (b) the path to the visual sheet, (c) anything surprising you noticed (especially candidates for "authored but never applied"), (d) build status.

Subsequent handoffs written after Bruce reviews each phase.
