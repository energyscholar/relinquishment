# Plan 0154a: Fold Demonstration + Phonon Reframe

**Status:** DONE — delivered via Plans 0151+0152 (commits 5da0f41, 0257952/554f0cb/e203ac6)
**Created:** 2026-04-10
**Plans:** 0152-fold-demonstration-into-first-light.md → 0151-phonon-reframe-soliton-demotion.md
**Dependency:** None. Run this FIRST — all other runs depend on Demonstration being gone.

---

## Scope

Two plans, two commits. Both modify `manuscript/record/first-light.tex` — 0152 transplants content in, 0151 reframes it. Genuinely coupled.

## Commit 1: Plan 0152 — Fold The Demonstration into First Light

Read `~/software/relinquishment/plans/0152-fold-demonstration-into-first-light.md` for full spec.

Resolved decisions:
- **Gell-Mann/Angerman paragraph** → (b) preserve in `manuscript/appendix/timeline.tex` as a footnote
- **Wolfram PCE paragraph** → (b) add one sentence to First Light Birth section. Name PCE and NKS explicitly. Do NOT mention Stephen Wolfram by name.
- **Ethical pivot** → keep First Light version ("originated"), delete Demonstration version

Files modified:
- `manuscript/record/first-light.tex` — receives transplanted content
- `build/main.tex` — comment out `\include{manuscript/record/the-demonstration}`
- `build/menu-tooltips.yaml` — remove `record:demonstration` entry
- `build/chapter-hover-descriptions.yaml` — remove `ch:the-demo` entry
- `build/hover-definitions.yaml` — change TQNN target → `#record:first-light`
- `build/preprocess.py` — change code-war expansion hook target → `record:first-light`
- `manuscript/appendix/timeline.tex` — Angerman footnote

**VERIFY before proceeding to Commit 2:** `make html` builds clean. `grep -ri demonstration build/ manuscript/` — no dangling refs. Guardian interlude count still 7.

## Commit 2: Plan 0151 — Phonon Reframe / Soliton Demotion

Read `~/software/relinquishment/plans/0151-phonon-reframe-soliton-demotion.md` for full spec.

**CRITICAL:** the-demonstration.tex no longer exists after Commit 1. The plan's Phase 2 has been updated with this note — all changes target first-light.tex.

**SKIP:** `what-healer-said.tex` phonon passage — plan says "Bruce should write this." Do not invent content.

Files modified:
- `manuscript/spine/the-braid.tex` — section rename, soliton→lattice/phonon pivot
- `manuscript/spine/the-silence-gap.tex` — Hasslacher domain label
- `manuscript/spine/genesis.tex` — convergence list
- `manuscript/record/first-light.tex` — reframe transplanted content + new I/O paragraph
- `manuscript/record/twenty-years.tex` — "solitons" → "lattice dynamics"
- `manuscript/record/interdiction.tex` — phonon-photon bridge paragraph
- `manuscript/appendix/glossary-entries.tex` — COWS entry, soliton entry, new phonon entry
- `build/hover-definitions.yaml` — phonon entry, soliton context, Hasslacher label
- `manuscript/appendix/abstracts.tex` — the-braid spiral abstract

**VERIFY:** `grep -ri soliton manuscript/spine/` returns only Russell story + bio context. `grep -ri phonon manuscript/` hits expected files. `make html` clean.

## Interaction notes

- First-light.tex is modified by BOTH commits. Commit 1 adds content, Commit 2 reframes it. No conflict — sequential.
- The `grown-not-built` deep link macro lives in the-demonstration.tex. Commit 1 must move `\deeplink{grown-not-built}` to first-light.tex (Plan 0152 Phase 2d specifies this). Run B (0148) depends on this being done.
