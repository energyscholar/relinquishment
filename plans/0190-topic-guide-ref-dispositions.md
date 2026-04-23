# Plan 0190 Phase 2b — topic-guide.tex ref audit

**Generated:** 2026-04-13 by Generator
**HEAD:** 970b88b (0190 phase 2a)
**Scope:** `manuscript/appendix/topic-guide.tex`

## Method

1. Extracted 100 unique `\hyperref[...]` targets from topic-guide.tex.
2. Extracted 474 unique `\label{...}` definitions across `manuscript/` and `build/`.
3. Compared via `comm -23 topic-refs all-labels`.

**Raw broken count:** 13 (plan §85 estimated ~50; the actual figure is lower).

## Disposition matrix

| # | Broken ref | Disposition | Retarget to | Notes |
|---|---|---|---|---|
| 1 | `interlude:the-handler` | RETARGET | `record:handler` | Chapter moved to Record; uses single-word label. |
| 2 | `interlude:the-target` | RETARGET | `record:target` | Chapter moved to Record. |
| 3 | `interlude:family-intelligence-lineage` | RETARGET | `record:tgt-family-intelligence-lineage` | Now a subsection inside `the-target.tex`. |
| 4 | `interlude:recruitment-assessment` | RETARGET | `record:tgt-recruitment-assessment` | Subsection inside `the-target.tex`. |
| 5 | `pos06:the-white-hot-secret` | RETARGET | `front:the-white-hot-secret-summary` | Used twice in topic-guide (L42 "2DEG" and L145 "A White Hot Secret"). Only match is the summary front-matter anchor — retarget both occurrences. |
| 6 | `pos28:it-is-done` | RETARGET | `record:sur-it-is-done` | Subsection in `the-surrender.tex`. |
| 7 | `pos35:the-doppelganger` | RETARGET | `record:tq-the-doppelganger` | Subsection in `the-question.tex`. (Alternate `pos33:digital-doppelganger` also exists but is the testament-track variant; Record subsection is the closer narrative match.) |
| 8 | `pos35:the-evidence` | RETARGET | `record:tq-the-evidence` | Subsection in `the-question.tex`. |
| 9 | `pos35:the-proof` | RETARGET | `record:tq-the-proof` | Subsection in `the-question.tex`. |
| 10 | `pos36:leaf-by-niggle-or-the-tree-that-might-be-real` | RETARGET | `spine:so-leaf-by-niggle-or-the-tree-that-might-be-real` | Renamed with `so-` prefix in current spine structure. |
| 11 | `pos36:steelman-a` | RETARGET | `spine:strongest-objection` | No direct `steelman-a` label exists; the whole chapter `The Strongest Objection` IS the steelman for Possibility A. Retarget to chapter anchor. |
| 12 | `pos36:sub-creation` | RETARGET | `spine:so-sub-creation` | Renamed with `so-` prefix. |
| 13 | `pos36:the-boy-in-the-study` | RETARGET | `spine:so-the-boy-in-the-study` | Label preserved in `appendix/niggle-companion.tex` (moved there by 0189 phase 4a). Anchor still resolves. |

## Summary

- **RETARGET:** 13
- **DELETE:** 0
- **FLAG:** 0

All 13 are cleanly retargetable — no orphaned targets require deletion or `% FIXME:` marking. The `pos*` → `record:*` / `spine:so-*` / `front:*` renames reflect the Z-restructure and Plan 0189 Phase 4 moves; topic-guide was not updated alongside those restructurings.

## Notes for Auditor

- Plan §85 expected ~50 broken refs. Actual is 13. Either earlier compaction analysis overcounted, or prior phases have already resolved most refs.
- Target word-count reduction (1423w → ~1000w, −423w) has **not yet been attempted** — per prompt, Phase 2b halts after ref audit and awaits approval before applying changes.
- Application plan when approved: (1) apply the 13 retargets via 13 `Edit` calls (or one `replace_all` per unique string where applicable — `pos06:the-white-hot-secret` appears twice); (2) compress the surrounding prose to land near 1000w; (3) `make dev` clean; (4) commit `Plan 0190 phase 2b: topic-guide refs + compress`.
