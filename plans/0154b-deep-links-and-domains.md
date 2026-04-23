# Plan 0154b: Deep Link Anchors + Eleven Domains

**Status:** DONE — delivered via Plans 0148+0149 (commits b04aa22, 8c51353, 3df49da, ed686ca, d2d77b3-5df7db8)
**Created:** 2026-04-10
**Plans:** 0148-deep-link-anchors.md + 0149-eleven-domains-cluster-list.md
**Dependency:** 0154a must be done — Demonstration chapter removed, `grown-not-built` anchor moved to first-light.tex.

---

## Scope

Two plans, two commits. 0149 places `\deeplink{eleven-domains}` which requires 0148's macro to exist. So 0148 infrastructure goes first, then 0149, then 0148's marker placement.

## Commit 1: Plan 0148 Phases 1-2 + Plan 0149 — Infrastructure + Eleven Domains

Read `~/software/relinquishment/plans/0148-deep-link-anchors.md` Phases 1, 2, and 2b.
Read `~/software/relinquishment/plans/0149-eleven-domains-cluster-list.md` all phases.

**Step 1 — Deep link macro + preprocess.py (0148 Phase 1):**
- Add `\deeplink` macro to `build/preamble.tex`
- Add hypertarget→share-anchor conversion in preprocess.py
- Add share-anchor CSS to collapse_css

**Step 2 — Toggle + click-to-copy + mobile tooltips (0148 Phases 2 + 2b):**
- 🔗 toggle button in bottom bar
- Click-to-copy handler with toast
- Mobile menu tooltip click-target split
- Mobile dotted underline CSS

**Step 3 — Eleven domains (0149 all phases):**
- Add hover definitions for "five scientific disciplines" / "five scientific fields" / "five fields" to `build/hover-definitions.yaml`
- Insert eleven-domains passage in `manuscript/spine/the-silence-gap.tex` (includes `\deeplink{eleven-domains}`)
- Apply `\hovertip{}` to 4 build-path files per plan spec

**VERIFY:** `make html` clean. Toggle works. Hover on "five scientific disciplines" shows tooltip.

## Commit 2: Plan 0148 Phases 3-4 — Marker Placement + Manifest

Read `~/software/relinquishment/plans/0148-deep-link-anchors.md` Phases 3 and 4.

- Place ~43 `\deeplink{id}` markers per manifest in plan
- Write `build/deep-links.yaml` manifest

**INTERACTION FIX:** Manifest entry `grown-not-built` says `record/the-demonstration.tex`. After 0154a, this is `record/first-light.tex`. Place marker there.

**VERIFY:** `grep -rc '\\deeplink' manuscript/` shows ~44 markers. `make html` clean. `grep -c 'class="share-anchor"' docs/downloads/Relinquishment.html` matches. Spot-check 3 `#dl:*` URLs from address bar.
