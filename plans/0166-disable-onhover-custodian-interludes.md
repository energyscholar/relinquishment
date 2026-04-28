# Plan 0166 — Disable onHover Popups on Custodian Interludes

**Auditor:** Argus
**Generator:** TBD
**Date:** 2026-04-12
**Origin:** Bruce, post-audit review. The popup **mechanism itself** is the problem on the 7 Custodian interludes: the interludes are visually large, and onHover popups occlude the menu / navigation UI when triggered. This is a UI-occlusion issue, not a content or rhetoric issue. Record chapters (also purple) are unaffected — their layout does not trigger the same blocking.

## Purpose

Suppress onHover popup *activation* inside the 7 Custodian interludes. The popups physically block the menu on these pages because of how large the interlude layout is. Disabling popup activation on just these 7 sections restores navigation access.

The `\hovertip{}` markup stays in source — we're not changing content, we're gating the popup *mechanism* from firing inside interlude DOM regions.

## Target files

Any of the following is acceptable — Generator picks the cleanest:

1. **CSS/JS gating** in `docs/assets/reader.js` or the stylesheet that governs popup activation. Gate on a parent class (e.g., `.epistemic-C-interlude` or equivalent). One-location change.

2. **Preprocessor-level strip** in `build/preprocess.py`: when emitting Custodian interlude sections, strip `\hovertip{key}{text}` → `text` before LaTeX compilation.

3. **LaTeX-level**: redefine `\hovertip` inside interlude files to be a no-op passthrough.

Generator to check which mechanism is cleanest and least invasive. Prefer the one-location change.

## Interlude identification

The 7 Custodian interludes were added in Z-restructure Phase 4 (Plan 0143). Locate them via:

- `git log --all --oneline | grep -i interlude`
- Or grep manuscript for interlude markers/filenames
- Or check `build/preprocess.py` for the Custodian-interlude tagging pass

If interludes share a distinct class, tag, or filename pattern from Record chapters, use that. If they don't, Generator may add a marker during preprocessing rather than hunting file-by-file.

## Acceptance criteria

1. In `docs/downloads/Relinquishment.html`, hover events on Custodian-interlude text produce no popup. (Manual visual check on 1-2 interludes.)
2. In Record chapters, onHover still works as before.
3. In spine A-chapters (gold/blue), onHover still works as before.
4. `make html` completes without errors.
5. No visible text changes inside interludes — only the interactive hover behavior is suppressed.
6. Physics primer from Plan 0164 (if merged first) retains its onHovers. Primer is pedagogy, not interlude.

## Out of scope

- Removing hovertip *markup* from interlude `.tex` source files permanently. Keep the markup; just suppress the behavior. Reversible.
- Changing Record chapter popups.
- Changing color stripes.
- Changing popup styling elsewhere.
- Deciding whether to extend this to Record later — separate decision.

## Build + ship

1. Identify the interlude-scoping mechanism (CSS class, file pattern, preprocessor tag).
2. Apply chosen gating approach.
3. `make html`.
4. Verify acceptance criteria manually (open 1 interlude + 1 Record chapter + 1 spine chapter in browser, check hover behavior on each).
5. Commit: `Plan 0166: disable onHover popups on Custodian interludes`
6. `git push`.

## Reporting

- Commit hash
- Build status
- Which mechanism chosen (CSS/preprocessor/LaTeX) and why
- Confirmation that Record + spine onHovers still work
- One interlude name verified as popup-free

## Context

Follows 4-plan audit response (0162-0165). This is a **UI occlusion fix**: popups on interlude-sized layouts physically cover the menu. Scope is narrow (7 interludes) because Record chapters don't exhibit the same blocking behavior.

Reversible: if the underlying popup layout is ever fixed so it no longer occludes menus, this gating can be removed and interludes regain popups.
