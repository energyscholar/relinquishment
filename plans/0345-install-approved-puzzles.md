# Plan 0345: Install Approved Puzzles

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** Plan 0343 Phase C (puzzle injection targets for genesis + firmware-update)
**Files:** `build/puzzle-tracker.yaml`
**Priority:** MEDIUM — 7 approved puzzles ready but invisible

---

## Current State

- 38 total chapter puzzles in tracker
- 17 installed (visible in book)
- 21 not installed
- Of those 21: **7 are approved** (content exists in puzzle-data.yaml, ready to display)

---

## The 7 Approved-Not-Installed Puzzles

| ID | Title | Chapter | Type |
|----|-------|---------|------|
| pz-sim-t3-001 | Genesis: The Edge of Chaos | genesis | sim (threads) |
| pz-sim-t4-001 | Can It Be Killed? | capabilities | sim |
| pz-ord-t4-002 | Build the Stack | story-never-told | ordering |
| pz-mc-t5-002 | The Silence Gap | the-silence-gap | mc |
| pz-ord-t1-001 | Guided Deduction | the-braid | ordering |
| pz-cip-t8-001 | The Firmware Key | firmware-update | cipher |
| pz-ba-t8-002 | Before and After Firmware | firmware-update | before/after |

All 7 have complete data in `build/puzzle-data.yaml` (verified).
All target chapters have CHAPTER_INJECTION_TARGETS entries (after Plan 0343 Phase C).

---

## Execution

For each of the 7 entries listed above, change `installed: false` to `installed: true` in `build/puzzle-tracker.yaml`.

---

## Verification

```bash
make html 2>&1 | grep -i "puzzle"
```

Check that puzzle injection reports installing puzzles in the 5 target chapters:
- genesis (1 puzzle)
- capabilities (1 puzzle)
- story-never-told (1 puzzle)
- the-silence-gap (1 puzzle)
- the-braid (1 puzzle)
- firmware-update (2 puzzles)

Then verify in HTML:
```bash
grep -c 'data-puzzle-wrap' docs/Relinquishment.html  # should increase by 7
```

---

## Do NOT

- Modify puzzle-data.yaml (content is complete)
- Change any puzzle that is `approved: false`
- Modify preprocess.py
- Touch .tex files

## Commit

`Plan 0345: install 7 approved puzzles — genesis, capabilities, silence-gap, braid, firmware`
