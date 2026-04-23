# Plan 0054: Recalibrate hook.tex + summary.tex (T12)

**Auditor:** Argus
**Date:** 2026-03-07
**Status:** MOSTLY COMPLETE — minor cleanup only
**PTL:** PTL-014 (T12)

---

## Assessment

T12 was scoped when main.tex still had pos01 as opening chapter, front matter included not-claimed/introduction/corrections, and summary.tex contained Evidence + Predictions sections.

**PTL-062 has already been executed.** The Maugham revision (Sessions 30+) recalibrated both files:

- **hook.tex:** Three Possibilities condensed to one sentence (line 22). Pure narrative pull. No \aidraft markers. No stale chapter references. Matches PTL-062 Phase 1A spec exactly.
- **summary.tex:** Evidence section removed (line 102 comment). Predictions section removed (line 190 comment). Three Possibilities trimmed to ~70 words (lines 92-100). Reading Guide (lines 224-242) matches current 5-part structure in main.tex. No \aidraft markers.

**Both files are functionally recalibrated.** What remains is comment hygiene only.

---

## Remaining Work

### 1. Update SPIRAL-REPEAT comments (comment-only, no functional change)

**hook.tex line 17:** SPIRAL-REPEAT comment references `introduction.tex`, which has been retired from main.tex (commented out at line 50-51 of main.tex). Update the cross-reference list to remove `introduction.tex` and add `three-possibilities-interlude.tex` (where UDHR content now lives).

Current (line 17):
```
% SPIRAL-REPEAT: "Universal Declaration of Human Rights" — thematic through-line, also in introduction.tex, summary.tex, pos05-the-stories.tex, ...
```

Change to:
```
% SPIRAL-REPEAT: "Universal Declaration of Human Rights" — thematic through-line, also in summary.tex, three-possibilities-interlude.tex, pos05-the-stories.tex, ...
```

**summary.tex line 81:** Same fix — replace `introduction.tex` with `three-possibilities-interlude.tex` in the SPIRAL-REPEAT cross-reference.

### 2. Verify SPIRAL-REPEAT comment in summary.tex line 58

Line 58 references `colophon.tex` in the "forgiveness than permission" cross-reference list. Verify this is still accurate (colophon.tex confirmed at `/home/bruce/software/relinquishment/manuscript/99-back/colophon.tex` line 23 — CONFIRMED, still present).

No change needed for line 58.

---

## What Does NOT Need Changing

- Hook narrative content — already pure narrative pull per Maugham revision
- Summary narrative sections (Mentor, Walk-Out, Guardian, Lock on Every Door, etc.) — all consistent with current manuscript and corrections
- Three Possibilities section — already trimmed per PTL-062 Phase 1B
- Reading Guide — 5-part structure + 4 track descriptions + bridge description all match main.tex
- "David Lane (not his real name)" — consistent with Session 7 real-names decision
- "Lane never disclosed anything classified" (line 40) — correct per Correction #12
- Evidence/Predictions removal — already done, comments document where content moved

---

## Dependencies

- **PTL-062:** Already executed. No blocker.
- **PTL-028 (Bruce writing pass):** Independent. Comment hygiene doesn't interact with content.
- **No blockers.** This plan can execute immediately.

---

## Acceptance Criteria

- [ ] hook.tex SPIRAL-REPEAT comment (line 17) no longer references `introduction.tex`
- [ ] summary.tex SPIRAL-REPEAT comment (line 81) no longer references `introduction.tex`
- [ ] Both SPIRAL-REPEAT comments reference `three-possibilities-interlude.tex`
- [ ] No other files modified
- [ ] LaTeX builds without errors (smoke test: `make` in repo root)

---

## Generator Handoff

Read this plan at `~/software/relinquishment/plans/0054-recalibrate-hook-summary.md`. Two comment-only edits in two files. Update SPIRAL-REPEAT cross-reference lists to replace `introduction.tex` (retired) with `three-possibilities-interlude.tex`. No content changes. Verify build succeeds. Report done.
