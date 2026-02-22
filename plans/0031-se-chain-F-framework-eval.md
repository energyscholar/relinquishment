# Plan 0031: SE Chain F — Testing Framework Evaluation

**Type:** Generator chain (Plan 003 Phases 1-4, decision gate)
**Estimated time:** ~4-8 hours
**Dependencies:** Chains B and E complete (c8 working, baseline measured)

---

## DECISION GATE

This chain produces an evaluation document with a recommendation. Do NOT execute the recommendation without Auditor review.

---

## Task 1: Benchmark Current Runner (Plan 003 Phase 1)

```bash
cd ~/software/npc-persona-prototype
```

**1. Count and categorize tests:**
```bash
find tests/ -name '*.test.js' | wc -l
find tests/ -name '*.test.js' -exec wc -l {} +
```

**2. Triage orphaned tests:**
```bash
# List tests in run-all.js:
grep -oP "'[^']+\.test\.js'" tests/run-all.js | tr -d "'" | sort > /tmp/runner-tests.txt

# List tests on disk:
find tests/ -name '*.test.js' -printf '%P\n' | sort > /tmp/disk-tests.txt

# Find orphans:
comm -13 /tmp/runner-tests.txt /tmp/disk-tests.txt
```

For each orphaned test, determine:
- Can it run standalone? (`node tests/orphan.test.js`)
- Does it crash? (Jest-dependent or broken imports?)
- Should it be added to run-all.js?

**IMPORTANT:** Do NOT modify run-all.js in this chain. Triage is READ-ONLY — report which tests SHOULD be added and why, but leave the actual modification for the Auditor to decide. Modifying run-all.js would invalidate Chain E's coverage baseline and ratchet thresholds.

**Known Jest-dependent dead code (3 files):** `autonomous-player.test.js`, `campaign-filtering.test.js`, `tuesday-npc-contexts.test.js` — these use `describe`/`test`/`expect` as globals without defining them. Jest is not installed.

**Known broken import:** `narrator-improvisation.test.js` references nonexistent `src/emergent-npc.js`.

**3. Benchmark current runner (5 runs each):**
```bash
for i in $(seq 5); do time npm test 2>&1; done
# If test:seq exists:
for i in $(seq 5); do time npm run test:seq 2>&1; done
```
Record median wall-clock time for parallel and sequential.

**4. Benchmark alternatives (5 representative test files only):**

Pick 5 tests that are in run-all.js and represent different areas.

**(a) Jest (if feasible):**
```bash
npm install --save-dev jest
time npx jest tests/memory.test.js tests/persona.test.js tests/prompts.test.js tests/skill-check.test.js tests/disposition.test.js 2>&1
npm uninstall jest  # Remove after benchmark
# Restore package files to committed state (cleaner than trusting npm uninstall):
git checkout -- package.json package-lock.json
npm install  # Restore node_modules from committed lockfile
# Verify:
git status  # Working tree should be clean
```

**(b) Node built-in test runner:**
```bash
time node --test tests/memory.test.js tests/persona.test.js tests/prompts.test.js tests/skill-check.test.js tests/disposition.test.js 2>&1
```

**WARNING:** The existing tests use `assert` + custom patterns, NOT `node:test` `describe`/`it`. `node --test` will attempt to run them as test files but may not recognize the assertion pattern. Record BOTH the timing AND whether tests actually executed (check output for "pass"/"fail" counts vs silent skip). **If `node --test` reports 0 tests, enter "N/A (0 tests detected)" in the Speed cell of the gap matrix. Do NOT enter a timing number — it would skew the comparison against runners that actually executed tests.**

---

## Task 2: Gap Analysis (Plan 003 Phase 2)

Score each candidate on this matrix:

| Criterion | Weight | Current Runner | Jest | node --test |
|-----------|--------|---------------|------|-------------|
| 1. Speed (median time) | HIGH | ? | ? | ? |
| 2. Coverage integration | HIGH | c8 (confirmed) | Built-in | --experimental-test-coverage |
| 3. Assertion completeness | MED | assert only | expect() | assert + describe/it |
| 4. Process isolation | MED | Yes (spawn) | Partial | Yes |
| 5. Watch mode | LOW | No | Yes | Yes (--watch) |
| 6. Mocking/stubbing | LOW | No | Yes | Partial |
| 7. Failure diagnostics | MED | Basic | Rich diffs | Moderate |
| 8. Zero dependencies | LOW | Yes | No (50MB) | Yes |

---

## Task 3: Decision Document (Plan 003 Phase 4)

**Write the decision document to `~/software/relinquishment/plans/0031-F-framework-eval-output.md`.** The Auditor reviews this file to decide the next chain. Terminal output alone is insufficient — persist to file.

Write a recommendation choosing one of:

**Option A: Keep custom runner + c8** (least disruption)
- Condition: c8 works (confirmed), no critical gaps
- Cost: already done (Plan 004)
- Risk: LOW

**Option B: Migrate to Node built-in test runner**
- Condition: Node 18+ confirmed, patterns compatible
- Cost: 8-16 hours
- Risk: MEDIUM

**Option C: Migrate to Jest/Vitest**
- Condition: Both A and B insufficient
- Cost: 16-24 hours
- Risk: HIGH

---

## Task 4: Traveller Investigation (Plan 003 Phase 3, informational)

Quick catalog only — does NOT gate npc-persona decision:
- Which traveller test files use Jest vs Mocha vs custom runner?
- How many of each?
- Is consolidation worthwhile?

```bash
cd ~/software/traveller-starship-operations-vtt
grep -rl "describe\|it(" tests/ | head -20    # Jest/Mocha patterns
grep -rl "assert\." tests/ | head -20          # assert patterns
```

---

## Acceptance Criteria
- [ ] All orphaned tests triaged (runnable / dead code / broken)
- [ ] Benchmark data for current runner (parallel + sequential, 5 runs)
- [ ] Gap matrix completed
- [ ] Decision document written with recommendation
- [ ] Traveller test inventory (informational)

---

## Report Format

```
Chain F complete.
Decision document: ~/software/relinquishment/plans/0031-F-framework-eval-output.md
Orphan triage: [N runnable, N dead code, N broken]
  Recommend adding to run-all.js: [list]
  NOTE: If tests added, coverage baseline from Chain E is stale — re-measurement needed
Benchmark: current=___ms, jest=___ms, node --test=___ms (N/A if 0 tests detected)
Recommendation: [A/B/C] — [one-sentence reason]
Traveller: [N Jest, N Mocha, N custom]
```
