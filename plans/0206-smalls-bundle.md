# Plan 0206 — Smalls bundle: P0204 P4 + summary L58 + commit pending edits

## Status
**Status:** COMPLETE (verified S63 audit)
COMPLETE (verified S63 audit). Originally: Ready for Generator. Three mechanical micro-edits + one build + one commit covering four already-authorized changes (two of which are already on disk from Auditor-direct execution).

## Why bundle

Four small changes individually too trivial to justify their own plan. Two are already on disk from the prior session (auditor-authorized direct edits): the lowercase→Flat fix in `hover-definitions.yaml` and the Doe/Epstein pub digression cut from `what-healer-said.tex`. Two remain to execute: P0204 P4 (the-question.tex L145 trim that didn't land at 6e92bae) and summary.tex L58 ("of the first application" trim, audit-positive).

One `make html`, one commit, one push. Done.

## Files modified

- `manuscript/record/the-question.tex` (Phase 1 — P0204 P4 trim)
- `manuscript/00-front/summary.tex` (Phase 2 — L58 trim)
- (Already on disk, will be staged in Phase 4 commit:)
  - `build/hover-definitions.yaml` (stack-question-mark lowercase→Flat fix at L604)
  - `build/hover-generated.tex` (downstream of YAML edit)
  - `docs/downloads/Relinquishment.html` (downstream rebuild)
  - `manuscript/record/what-healer-said.tex` (Doe/Epstein digression cut, ~640w out)
  - `manuscript/00-front/summary.tex` L30 (Nobel count two→three, +", 2016") — auditor-direct edit per Bruce's authorization; consistency fix matching 5 other sites in the book

---

## Pre-flight: verify OLD strings unique

Run these greps before any edits. Each must return exactly one match in the named file.

```
cd ~/software/relinquishment
grep -c "He planted a witness at the beginning" manuscript/record/the-question.tex   # expect 1
grep -c "is a side effect of the first application" manuscript/00-front/summary.tex  # expect 1
```

If either returns 0 or >1, stop and report — the plan was authored against a different file state.

---

## Phase 1 — the-question.tex L145 trim "at the beginning"

**File:** `manuscript/record/the-question.tex` line 145

**Edit (Edit tool):**

OLD:
```
He planted a witness at the beginning so that the story might eventually be told. This is that telling.
```

NEW:
```
He planted a witness so that the story might eventually be told. This is that telling.
```

Strip "at the beginning " (3 words + trailing space). Closing two-sentence beat preserved. This is the unlanded P4 from Plan 0204.

---

## Phase 2 — summary.tex L58 trim "of the first application"

**File:** `manuscript/00-front/summary.tex` line 58

**Edit (Edit tool):**

OLD:
```
A working quantum computer is one application of that primitive; \hovertip{quantum teleportation} of information across a nonlocal channel is another. The code-breaking capability that makes governments nervous is a side effect of the first application. Under Possibility~C, the real finding is biological: the Flat can support life.
```

NEW:
```
A working quantum computer is one application of that primitive; \hovertip{quantum teleportation} of information across a nonlocal channel is another. The code-breaking capability that makes governments nervous is a side effect. Under Possibility~C, the real finding is biological: the Flat can support life.
```

Strip " of the first application" (5 words + leading space). Audit-positive: cleaner punch line; technical readers infer the attribution.

---

## Phase 3 — Build

```
cd ~/software/relinquishment
make html
```

`make html` auto-runs `build/generate-hover.py` and the pandoc/HTML pipeline. No `make pdf` needed — Bruce reads HTML on phone (per `feedback-build-to-website.md`).

### Pass criteria
1. **Build succeeds** (no LaTeX, pandoc, or YAML errors).
2. **Post-edit greps return zero matches** for the stripped strings:
   ```
   grep -c "He planted a witness at the beginning" manuscript/record/the-question.tex   # expect 0
   grep -c "is a side effect of the first application" manuscript/00-front/summary.tex  # expect 0
   ```
3. **HTML reflects all four logical changes** when reloaded on phone (only spot-check needed since Bruce already audited each).

---

## Phase 4 — Commit + push

Stage all six files (two from this plan + four already-on-disk):

```
cd ~/software/relinquishment
git add manuscript/record/the-question.tex \
        manuscript/00-front/summary.tex \
        manuscript/record/what-healer-said.tex \
        build/hover-definitions.yaml \
        build/hover-generated.tex \
        docs/downloads/Relinquishment.html
git commit -m "Plan 0206: smalls bundle (P0204 P4, summary L30+L58, Doe cut, stack-? Flat)"
git push
```

If `make html` regenerated additional files (e.g. other doc-export artifacts), include them in the `git add` line. If the working tree contains files NOT in the list above and unrelated to this plan, leave them unstaged and report what was skipped.

---

## Risk

- **Phase 1, Phase 2:** zero (mechanical strips, OLD strings unique by pre-flight grep).
- **Phase 3 build:** low (no new YAML keys, no new macros, no new file dependencies — only prose strips).
- **Phase 4 commit:** low (six-file commit; pre-existing on-disk changes were already audited and authorized in prior turns).

## Out of scope

- L23 "Same goes for biological brains" revert — already at desired state (current L23 reads "Artificial intelligence does all of that, and learns." with no addition). Verified by grep.
- P0204 P1, P2a-e, P3 — all landed at 6e92bae per Bruce.
- Plan 0205 (tooltip externalization) — separate plan, pending Option A vs B decision.
- Plan 0207 (Strongest Objection Argus Part 2 cut) — separate plan, queued.
- Record fat-pass beyond Doe cut — separate plan candidate.

---

## Annealing log

- **Pass 1 (low amplitude):** Bundle reduced from 4→3 items (L23 revert is no-op). Added pre-flight grep for OLD-string uniqueness. Specified `make html` only, no PDF (Bruce reads on phone). Expanded commit list to include the 4 already-on-disk changes from prior auditor-direct execution.
- **Pass 2 (low amplitude):** Added post-edit grep verification (OLD strings gone). Tightened commit message from 76→70 chars to fit conventional title length. Push step retained per `feedback-build-to-website.md`.
- **Pass 3:** Plan converged. No structural changes warranted.
