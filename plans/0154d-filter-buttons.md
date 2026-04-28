# Plan 0154d: Epistemic Filter Buttons

**Status:** DONE — delivered via Plan 0144 (commit d808bd8)
**Created:** 2026-04-10
**Plans:** 0144-epistemic-filter-buttons.md
**Dependency:** 0154a must be done — chapter set changed. Independent of 0154b and 0154c.

---

## Scope

One plan, one commit. Standalone feature — adds Science/Story toggle buttons.

## Commit: Plan 0144 — Epistemic Filter Buttons

Read `~/software/relinquishment/plans/0144-epistemic-filter-buttons.md` for full spec.

- Propagate `data-filter-group` attributes in preprocess.py (after epistemic-class loop)
- Add Science/Story toggle buttons to bottom bar in reader.js
- Filter logic: Science shows A+M+G, hides B+C. Story shows B+C+G+M, hides A.
- localStorage persistence
- Expand All skips hidden chapters
- Deep links clear active filter if target is hidden
- Fix G comment in `build/menu-tooltips.yaml`

**BOTTOM BAR NOTE:** After all 4 runs complete, the bottom bar will have: [Expand All] [Science] [Story] [AI Eval] [🔗] [§ Share] [PDF]. If too crowded at 375px, use compact icons with tooltip labels. This run only adds [Science] and [Story] — coordinate spacing with whatever's already there.

**VERIFY:** `make html` clean. Science mode hides Record, shows Flat + Custodian. Story mode hides Flat, shows Record + Custodian. Toggle off restores all. Filter persists on reload. Navigate to `#record:alpha-farm` while in Science mode → filter clears.

## Interaction with deep links (0154b)

If 0154b runs first: verify that `#dl:*` anchors inside hidden chapters also trigger filter clear. The `autoExpand()` function finds the parent `<details>` — filter clear should trigger on the parent chapter-section's `display:none`.

If 0154d runs before 0154b: no issue, deep links don't exist yet.
