# Plan 0027: SE Chain B — c8 Feasibility Spike

**Type:** Generator chain (1 task, decision gate)
**Estimated time:** ~15 minutes
**Dependencies:** Chain A complete (package.json not in conflict)

---

## DECISION GATE

This chain produces a binary answer: **c8 works with the custom test runner, or it doesn't.** Report the result. Do NOT proceed to Chain E (coverage setup) without Auditor review.

---

## Task: Plan 003 Phase 0 — c8 Feasibility Test

### Goal
Test whether c8 (V8 coverage tool) can see coverage from the custom test runner's child processes.

### Context
npc-persona-prototype has a custom test runner (`tests/run-all.js`) that spawns separate Node processes per test file using `spawnSync` (sequential) or `spawn` (parallel). c8 works by setting `NODE_V8_COVERAGE` env var. Child processes must inherit this env var for coverage to work.

**Pre-verified (round 3 red team):** run-all.js does NOT pass explicit `env` options to spawn calls, so children inherit `process.env` including `NODE_V8_COVERAGE`. c8 SHOULD work. This spike confirms it empirically.

### Steps

```bash
cd ~/software/npc-persona-prototype
```

**1. Document Node version:**
```bash
node --version
```
Record this. c8 requires Node 14+. Expected: v24.12.0.

**2. Verify spawn env inheritance (2-minute code read):**
```bash
# Read tests/run-all.js
# Confirm: spawnSync and spawn calls do NOT pass { env: ... }
# If they do pass env, check that process.env is spread
```

**3. Install c8:**
```bash
npm install --save-dev c8
```

**4. Run c8 with full test suite (sequential for easier debugging):**
```bash
npx c8 node tests/run-all.js
```

**5. Check output:**
- Look at the coverage table. Are src/ files listed with >0% coverage?
- If YES → c8 works. Record the coverage numbers.
- If all src/ files show 0% → c8 can't see child processes.

**6. If Step 5 shows 0%, try NODE_V8_COVERAGE directly:**
```bash
mkdir -p /tmp/v8-coverage
NODE_V8_COVERAGE=/tmp/v8-coverage node tests/run-all.js
npx c8 report --temp-directory=/tmp/v8-coverage
rm -rf /tmp/v8-coverage
```

**7. Commit (c8 stays in devDependencies either way):**
```bash
git add package.json package-lock.json
git commit -m "chore: add c8 for coverage measurement (spike)"
```

### Acceptance Criteria
- [ ] Node version documented
- [ ] Spawn env inheritance verified (code read)
- [ ] c8 tested with run-all.js
- [ ] Binary answer recorded: c8 works / doesn't work
- [ ] If works: baseline coverage numbers recorded (all 4 metrics)
- [ ] npm test still passes

---

## Report Format

When done, report:
```
Chain B complete.
Node version: [version]
c8 result: [WORKS / DOES NOT WORK]
  Method: [direct c8 / NODE_V8_COVERAGE / neither]
Coverage baseline (if works):
  Lines: ___%, Branches: ___%, Functions: ___%, Statements: ___%
  Files at 0%: [list]
Commit: [hash]
```
