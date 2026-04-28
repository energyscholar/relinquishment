# Plan 0274c: Puzzle Wave Deployment

**Status:** READY FOR GENERATOR (after 0274a and 0274b)
**Author:** Auditor (Argus S63)
**Priority:** High
**Scope:** `build/puzzle-tracker.yaml` (flip `installed: true` per wave)
**Constraint:** Output must remain a single self-contained HTML file. No external dependencies.
**Prerequisites:** Plan 0274a (injection algorithm), Plan 0274b (verification script)
**Annealing:** MED LOW

---

## Problem Statement

23 approved puzzles exist but only 5 are installed in the book HTML. The injection system (`inject_chapter_puzzles()` in preprocess.py) supports only 3 types (mc, gd, log) and has CHAPTER_MARKERS for only 3 chapters, using brittle full-string matching. Distribution is unbalanced: the-flat has 3 puzzles, most chapters have 0.

This plan installs all 17 installable puzzles (mc/gd/log types) across 12 chapters, using a new id-based chapter lookup that's stable across pandoc rebuilds. Deployment is staged in 4 waves with per-puzzle tracking.

### Gating Mechanism (post-274a)

After Plan 0274a executes, the code gates injection on FOUR conditions, ALL required:
1. `approved: true` in puzzle-tracker.yaml
2. `installed: true` in puzzle-tracker.yaml
3. Puzzle type is in the supported set (`mc`, `gd`, `log`)
4. Puzzle's chapter has an entry in CHAPTER_INJECTION_TARGETS

All 10 chapters are already in CHAPTER_INJECTION_TARGETS (installed by 0274a). The `installed` field is the deployment gate — flipping it to `true` is the ONLY action needed to deploy a puzzle.

**Generator instruction:** Each wave is a YAML-only edit: set `installed: true` for the wave's puzzles, build, verify count, test, commit.

---

## Architecture

**Prerequisites:** Plan 0274a installs the id-based injection algorithm, `installed` gate, sort-by-level, and per-puzzle logging. Plan 0274b installs the post-build verification script. After those two plans execute, the system is:

- 10-entry CHAPTER_INJECTION_TARGETS dict (id-based, stable)
- Code gates on `approved: true AND installed: true`
- Verification runs after every build
- 4 puzzles currently installed (mc-t2-001, mc-t2-002, mc-t1-002, log-t6-002)
- All relocations already done in tracker

**This plan (0274c) deploys puzzles in 4 waves by flipping `installed: true` in puzzle-tracker.yaml.** No code changes — only YAML edits + build + verify.

---

## Puzzle Manifest

Every puzzle tracked individually. The puzzle-tracker.yaml is the single source of truth.

### Installable Puzzles (17) — by chapter order

| Wave | ID | Title | Type | Level | Chapter | Status |
|------|----|----|------|-------|---------|--------|
| 1 | pz-gd-t1-001 | The Method | gd | p1 | story-never-told | new |
| 1 | pz-log-t6-002 | Under Which Possibility? | log | p1 | three-possibilities | INSTALLED |
| 1 | pz-mc-t2-001 | Wormholes in the Flat | mc | p1 | the-flat | INSTALLED |
| 1 | pz-mc-t2-002 | The 2DEG in Your Pocket | mc | p1 | the-flat | INSTALLED |
| 2 | pz-mc-t2-003 | The Braid | mc | p2 | the-braid | new |
| 2 | pz-mc-t8-003 | Fish Detecting Water | mc | p1 | the-code-war | new |
| 2 | pz-gd-t2-001 | The Accidental Habitat | gd | p1 | **growing-a-mind** | RELOCATE from the-flat |
| 2 | pz-mc-t3-002 | The Canopy Problem | mc | p1 | growing-a-mind | new |
| 1 | pz-mc-t1-002 | Not a Deity, Not an Alien | mc | p1 | wrong-substrate | INSTALLED |
| 1 | pz-mc-t3-003 | Not Chemistry | mc | p2 | wrong-substrate | new |
| 3 | pz-gd-t5-001 | The Silence | gd | p1 | the-silence-gap | new |
| 3 | pz-mc-t5-002 | The Silence Gap | mc | p2 | the-silence-gap | new |
| 4 | pz-gd-t6-001 | The Ethics | gd | p1 | capabilities | new |
| 4 | pz-mc-t6-001 | Capabilities | mc | p2 | capabilities | new |
| 4 | pz-mc-t6-002 | Why Srebrenica? | mc | p1 | why-relinquish | new |
| 4 | pz-mc-t6-003 | Why Relinquish? | mc | p1 | why-relinquish | new |
| 4 | pz-log-t7-001 | UDHR Service Compatibility | log | p3 | **why-relinquish** | RELOCATE from capabilities |

### Relocations (4 puzzles)

| ID | Title | From | To | Reason |
|----|-------|------|----|--------|
| pz-gd-t2-001 | Accidental Habitat | the-flat | **growing-a-mind** | the-flat overloaded (3→2); habitat = growth environment, better content match than genesis |
| pz-log-t7-001 | UDHR Service Compatibility | capabilities | **why-relinquish** | Reduces capabilities from 3→2; UDHR service analysis directly supports the relinquishment argument |
| pz-ord-t4-002 | Build the Stack | the-flat | **story-never-told** | Stack spans full argument; deferred anyway (tower type) |
| pz-ord-t1-001 | Guided Deduction | three-possibilities | **the-braid** | Ordering fits braiding metaphor; deferred (ord type) |

### Deferred Puzzles (6) — type not yet supported

| ID | Title | Type | Chapter | Reason deferred |
|----|-------|------|---------|----------------|
| pz-sim-t3-001 | Genesis: Edge of Chaos | sim | genesis | sim type not implemented |
| pz-sim-t4-001 | Can It Be Killed? | sim | capabilities | sim type not implemented |
| pz-ord-t4-002 | Build the Stack | tower | story-never-told | tower type not implemented |
| pz-ord-t1-001 | Guided Deduction | ord | the-braid | ord type not implemented |
| pz-cip-t8-001 | The Firmware Key | cip | firmware-update | cip type not implemented |
| pz-ba-t8-002 | Before and After Firmware | ba | firmware-update | ba type not implemented |

### Final Distribution

```
Chapter                      Count  p-levels      Types
──────────────────────────────────────────────────────────
Story Never Told (front)      1     p1            gd          (+1 tower deferred)
Three Possibilities           1     p1            log
The Flat                      2     p1+p1         mc+mc
The Braid                     1     p2            mc          (+1 ord deferred)
The Factoring Game            0     —             —
The Code War                  1     p1            mc
Genesis                       0     —             —           (+1 sim deferred)
Growing a Mind                2     p1+p1         gd+mc
The Wrong Substrate           2     p1+p2         mc+mc
The Silence Gap               2     p1+p2         gd+mc
Capabilities                  2     p1+p2         gd+mc       (+1 sim deferred)
Why Relinquish?               3     p1+p1+p3      mc+mc+log
Strongest Objection           0     —             —
Weigh the Evidence            0     —             —
Firmware Update               0     —             —           (+2 deferred: cip+ba)
──────────────────────────────────────────────────────────
TOTAL INSTALLABLE            17     p1=12 p2=4 p3=1
DEFERRED                      6
```

**Front-weighting:** 8 of 17 (47%) in first 7 chapters (Story Never Told through Growing a Mind).
**Cap:** No chapter exceeds 3 puzzles. The 3 in Why Relinquish? are p1+p1+p3 — the p3 (UDHR Service) is invisible to most readers.
**Level gradient:** p1 dominates front; p2/p3 appear later.

---

## Phase 1: Wave 1 — Baseline + story-never-told + wrong-substrate fix (6 puzzles)

**Scope:** 0274a left 4 puzzles installed. This wave adds 2 more by flipping `installed: true`.

**Expected puzzles after wave (6):**
| ID | Chapter | Type | Level | Notes |
|----|---------|------|-------|-------|
| pz-gd-t1-001 | story-never-told | gd | p1 | **NEW** |
| pz-log-t6-002 | three-possibilities | log | p1 | existing |
| pz-mc-t2-001 | the-flat | mc | p1 | existing |
| pz-mc-t2-002 | the-flat | mc | p1 | existing |
| pz-mc-t1-002 | wrong-substrate | mc | p1 | existing |
| pz-mc-t3-003 | wrong-substrate | mc | p2 | **NEW** (was invisible due to name mismatch, fixed in 1d) |

Note: pz-gd-t2-001 was relocated to growing-a-mind in 0274a — it won't appear until wave 2.

**Tracker changes:** Set `installed: true` for pz-gd-t1-001, pz-mc-t3-003.

**Build, verify VERIFY OK: 6, test The Method and Not Chemistry (new), commit:**
`Plan 0274c wave 1: story-never-told + wrong-substrate puzzles`

---

## Phase 2: Wave 2 — Early A-spine (4 new puzzles)

**Tracker changes:** Set `installed: true` for pz-mc-t2-003, pz-mc-t8-003, pz-gd-t2-001, pz-mc-t3-002.

**New puzzles appearing (4):**
| ID | Chapter | Type | Level | Notes |
|----|---------|------|-------|-------|
| pz-mc-t2-003 | the-braid | mc | p2 | **NEW** |
| pz-mc-t8-003 | the-code-war | mc | p1 | **NEW** |
| pz-gd-t2-001 | growing-a-mind | gd | p1 | **NEW** (relocated from the-flat in 0274a) |
| pz-mc-t3-002 | growing-a-mind | mc | p1 | **NEW** |

**Build, verify VERIFY OK: 10, test each new puzzle in browser, commit:**
`Plan 0274c wave 2: the-braid, the-code-war, growing-a-mind puzzles`

---

## Phase 3: Wave 3 — Mid A-spine (2 new puzzles)

**Tracker changes:** Set `installed: true` for pz-gd-t5-001, pz-mc-t5-002.

**New puzzles appearing (2):**
| ID | Chapter | Type | Level | Notes |
|----|---------|------|-------|-------|
| pz-gd-t5-001 | the-silence-gap | gd | p1 | **NEW** |
| pz-mc-t5-002 | the-silence-gap | mc | p2 | **NEW** |

**Build, verify VERIFY OK: 12, test new puzzles, commit:**
`Plan 0274c wave 3: silence-gap puzzles`

---

## Phase 4: Wave 4 — Late A-spine (5 new puzzles)

**Tracker changes:** Set `installed: true` for pz-gd-t6-001, pz-mc-t6-001, pz-mc-t6-002, pz-mc-t6-003, pz-log-t7-001.

**New puzzles appearing (5):**
| ID | Chapter | Type | Level | Notes |
|----|---------|------|-------|-------|
| pz-gd-t6-001 | capabilities | gd | p1 | **NEW** |
| pz-mc-t6-001 | capabilities | mc | p2 | **NEW** |
| pz-mc-t6-002 | why-relinquish | mc | p1 | **NEW** |
| pz-mc-t6-003 | why-relinquish | mc | p1 | **NEW** |
| pz-log-t7-001 | why-relinquish | log | p3 | **NEW** (relocated from capabilities in 0274a) |

**Build, verify VERIFY OK: 17, test all new puzzles, commit:**
`Plan 0274c wave 4: capabilities and why-relinquish puzzles`

---

## Phase 5: Final Verification + Push

1. Update SUMMARY comment block at bottom of puzzle-tracker.yaml to reflect final state
2. Final build + full browser walkthrough of all 17 puzzles
3. `python3 build/verify-deep-links.py` — passes
4. VERIFY OK: 17
5. No JS console errors
6. Git push to website

**Commit:** `Plan 0274c phase 5: final verification and push`

---

## Anneal: MED LOW

### MEDIUM

**M1. Puzzle data completeness.**
The injection code reads question text, options, abstracts from puzzle-data.yaml. If any of the 17 installable puzzles has incomplete data (missing question, no options, empty abstract), the injection may produce broken HTML.
**Mitigation:** Generator must verify each puzzle's data completeness in puzzle-data.yaml before setting `installed: true`. The verification script (0274b) catches count mismatches but not content errors. Browser testing per wave catches rendering issues.

### LOW

**L2. Two p1 puzzles at growing-a-mind.**
Both are p1 but different types (gd + mc) and topics (habitat vs. canopy).
**Mitigation:** The Flat already has 2x p1 mc and works fine.

**L3. Three puzzles at why-relinquish.**
Two p1 mc + one p3 log. The p3 is invisible to most readers.
**Mitigation:** why-relinquish is the moral climax — it can support weight.

---

## Acceptance Criteria

Per wave:
1. VERIFY OK with expected count (wave targets: 6, 10, 12, 17)
2. Each new puzzle: interaction works, reset works, abstract/reward displays
3. No JavaScript console errors
4. `make html` builds cleanly

Final:
5. 17 total — VERIFY OK: 17
6. `verify-deep-links.py` passes
7. Puzzles appear at END of their respective chapters
8. Within multi-puzzle chapters, p1 before p2 before p3
9. Push succeeds; Bruce phone-verifies

---

## Handoff Prompt (0274c — after 0274a and 0274b are complete)

```
You are the Generator. Read plans 0274a, 0274b, and 0274c (file:
0274-puzzle-placement-and-installation.md) in ~/software/relinquishment/plans/.

Execute in order: 0274a first (algorithm + tracker fixes), then 0274b
(verification script), then 0274c waves (YAML-only deployment).

0274c waves — each is ONLY tracker YAML changes:
Wave 1: installed:true for pz-gd-t1-001, pz-mc-t3-003 → VERIFY OK: 6
Wave 2: installed:true for pz-mc-t2-003, pz-mc-t8-003, pz-gd-t2-001,
  pz-mc-t3-002 → VERIFY OK: 10
Wave 3: installed:true for pz-gd-t5-001, pz-mc-t5-002 → VERIFY OK: 12
Wave 4: installed:true for pz-gd-t6-001, pz-mc-t6-001, pz-mc-t6-002,
  pz-mc-t6-003, pz-log-t7-001 → VERIFY OK: 17

Each wave: edit tracker, build, check VERIFY OK, test new puzzles in
browser, commit. Final: update tracker summary, push.
```
