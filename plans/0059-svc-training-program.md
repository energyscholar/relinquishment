# Plan 0059: Structure-vs-Control Training Program

*Auditor: Argus (Session 35). Origin: Bruce needs technical proficiency in the structure-vs-control technique before building the AI refactoring product or training others. Three training examples selected, Example 1 fully instantiated.*

---

## Background (Generator: read this section for context)

The structure-vs-control approach (see `~/software/aurasys-memory/training/structure-vs-control/README.md`) replaces defensive control logic (if/else, clamps, guards, NaN checks) with structural invariants that make invalid states unreachable by construction. The canonical example: replacing `Math.min(Math.max(low, value), high)` with a smooth projection `x/(1+|x|)`.

Bruce has done 3 toy exercises and achieved ~90% of optimal. He needs real-world practice to develop the judgment skill: WHERE does this apply, where doesn't it, and what breaks when "more correct" violates implicit contracts?

The training repo is at: `~/software/aurasys-memory/training/structure-vs-control/`
Example 1 is cloned at: `~/software/aurasys-memory/training/structure-vs-control/example-1-color2k/`

The training design document is: `~/software/aurasys-memory/training/structure-vs-control/README.md`

---

## Phase 1: Build the Training Harness for Example 1

**Directory:** `~/software/aurasys-memory/training/structure-vs-control/`

**Action:** Create the following files:

### 1a. `scripts/reset.sh`
Resets Example 1 to baseline state:
```bash
#!/bin/bash
cd "$(dirname "$0")/../example-1-color2k"
git checkout .
echo "Reset complete. Run 'npm test' to verify baseline."
```

### 1b. `scripts/metrics.sh`
Collects before/after metrics for any example:
```bash
#!/bin/bash
EXAMPLE_DIR="${1:-example-1-color2k}"
cd "$(dirname "$0")/../$EXAMPLE_DIR"
echo "=== Metrics for $EXAMPLE_DIR ==="
echo "LOC (src, non-test):"
find src -name '*.ts' -not -name '*.test.*' -not -name '*.d.ts' | xargs wc -l | tail -1
echo "guard() calls:"
grep -rn "guard(" src/ --include="*.ts" --include="*.js" | grep -v test | wc -l
echo "Branches (if/else/ternary in source):"
grep -rn "if \|else \|? " src/ --include="*.ts" --include="*.js" | grep -v test | wc -l
echo "Test results:"
npx jest --silent 2>&1 | grep -E "Tests:|Suites:"
```

### 1c. `scripts/run-phase.sh`
Guides Bruce through each training phase with instructions:
```bash
#!/bin/bash
PHASE="${1:-1}"
case $PHASE in
  1) echo "=== PHASE 1: ANALYSIS ==="
     echo "Task: Read every file in src/. Classify each guard() call as:"
     echo "  D (Defensive) - prevents invalid output, could be structural"
     echo "  E (Essential) - implements spec, cannot change"
     echo "  V (Validation) - detects errors, not correcting values"
     echo ""
     echo "Files with guard() calls:"
     grep -rln "guard(" example-1-color2k/src/ --include="*.ts" | grep -v test
     echo ""
     echo "When done, run: ./scripts/run-phase.sh 2"
     ;;
  2) echo "=== PHASE 2: NAIVE REPLACEMENT ==="
     echo "Task: Replace the guard function body in src/guard.ts with:"
     echo "  const range = high - low;"
     echo "  const mid = (high + low) / 2;"
     echo "  const normalized = (value - mid) / (range / 2);"
     echo "  return mid + (range / 2) * normalized / (1 + Math.abs(normalized));"
     echo ""
     echo "Then run: npm test"
     echo "Expected: ~55 tests fail. Study WHY."
     echo "Key question: What contract does guard(0,255,300)===255 enforce?"
     echo ""
     echo "When done, run: ./scripts/reset.sh then ./scripts/run-phase.sh 3"
     ;;
  3) echo "=== PHASE 3: TARGETED REPLACEMENT ==="
     echo "Task: Reset first, then find WHERE structural replacement works"
     echo "WITHOUT breaking contracts. Candidates:"
     echo "  - Internal computations in mix.ts (weight calculation)"
     echo "  - Saturation/lightness arithmetic (before hsla output)"
     echo "  - Anywhere BETWEEN parse and output formatting"
     echo ""
     echo "Key insight: guard at OUTPUT boundaries (CSS spec) must stay."
     echo "Structure works INSIDE the computation pipeline."
     echo ""
     echo "When done, run: ./scripts/run-phase.sh 4"
     ;;
  4) echo "=== PHASE 4: DESIGN ==="
     echo "Task: Design the hybrid architecture:"
     echo "  - Output functions (rgba, hsla, toHex): KEEP guard (CSS spec)"
     echo "  - Computation functions (darken, mix, etc.): USE projection"
     echo "  - Parse functions (parseToRgba): KEEP guard (validation)"
     echo ""
     echo "Write your design in: training/structure-vs-control/my-design.md"
     echo ""
     echo "When done, run: ./scripts/run-phase.sh 5"
     ;;
  5) echo "=== PHASE 5: IMPLEMENT AND MEASURE ==="
     echo "Task: Implement your Phase 4 design. Requirements:"
     echo "  1. All 96 tests pass"
     echo "  2. guard() calls reduced (some remain — that's correct)"
     echo "  3. New projection function has its own tests"
     echo "  4. Run: ./scripts/metrics.sh > metrics-after.txt"
     echo "  5. Compare with: training/structure-vs-control/metrics-baseline.txt"
     echo ""
     echo "When done: Review metrics-baseline.txt vs metrics-after.txt"
     ;;
  *) echo "Unknown phase. Use 1-5." ;;
esac
```

### 1d. `metrics-baseline.txt`
Capture baseline metrics (from emulated run):
```
=== Metrics for example-1-color2k ===
LOC (src, non-test): 611 total
guard() calls: 15
Branches (if/else/ternary in source): ~45
Test results: 23 suites passed, 96 tests passed, 169 snapshots passed
```

### 1e. `emulation-log.md`
Document the emulated run results:
```markdown
# Emulation Log — Phase 2 (Naive Replacement)

**Date:** 2026-03-08
**Emulated by:** Argus

## What happened

Replaced guard() body with structural projection (C-operator variant).

### Results
- 18 of 23 test suites FAILED
- 55 of 96 tests FAILED
- 41 tests still pass (those that don't exercise boundary behavior)

### Key failure: guard(0, 1, 2) === 0.875 (expected 1)

The structural projection approaches but never reaches boundaries.
Downstream: CSS output produces non-integer RGB values, wrong hex codes,
incorrect luminance calculations, broken color mixing.

### Cascade analysis
guard.ts is called from 5 files. Failure cascades:
- guard → rgba/hsla → darken/lighten/saturate/mix/getScale → getContrast/getLuminance → hasBadContrast/readableColor

One function change, 55 test failures. This demonstrates both:
1. The coupling created by structural primitives (change propagates everywhere)
2. Why boundary-pinning contracts matter (CSS needs exact integers)

### Training value
The failure is the lesson. Phase 2 exists to PRODUCE this failure so the trainee
discovers the constraint themselves rather than being told about it.
```

---

## Phase 2: Make Scripts Executable and Verify

**Action:** `chmod +x scripts/*.sh` and verify each script runs correctly.

---

## Acceptance Criteria

1. `scripts/reset.sh` resets example-1-color2k to baseline (96/96 tests pass after reset)
2. `scripts/metrics.sh` produces correct baseline numbers
3. `scripts/run-phase.sh 1` through `5` print correct instructions
4. `metrics-baseline.txt` matches actual baseline
5. `emulation-log.md` documents the Phase 2 naive replacement results
6. README.md exists with full training program (already written by Auditor)
7. No modifications to the example-1-color2k source (it's a cloned repo, stays clean)
8. Examples 2-3 are outlined in README.md but have no detailed files

---

## Idempotency Statement

A second Generator given only this plan file would produce the same scripts, metrics, and documentation. The content is fully specified. Style of the emulation-log prose may vary.

---

## Handoff Prompt

```
You are the Generator. Read and implement:
~/software/relinquishment/plans/0059-svc-training-program.md

Two phases: (1) Create training harness scripts and documentation
in ~/software/aurasys-memory/training/structure-vs-control/,
(2) Make executable and verify. All file contents specified in plan.
Commit per phase: "Plan 0059 phase N: description"
```
