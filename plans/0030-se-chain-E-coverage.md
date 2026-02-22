# Plan 0030: SE Chain E — Coverage Setup

**Type:** Generator chain (Plan 004)
**Estimated time:** ~2-3 hours
**Dependencies:** Chain B complete (c8 confirmed working)
**Prerequisite:** Chain B report shows "c8 result: WORKS". If c8 does NOT work, this chain cannot execute — return to Auditor for replanning.

---

## Task: c8 Coverage Reporting (Plan 004 Path A)

### Goal
Configure c8 coverage reporting with ratchet threshold in npc-persona-prototype.

### Steps

```bash
cd ~/software/npc-persona-prototype
```

**1. Create .c8rc.json:**
```json
{
  "include": ["src/**/*.js"],
  "exclude": [
    "tests/**",
    "node_modules/**",
    "data/**"
  ],
  "reporter": ["text", "text-summary", "lcov", "html"],
  "report-dir": "coverage",
  "all": true,
  "temp-directory": ".c8_output"
}
```

**2. Add coverage dirs to .gitignore:**
```
coverage/
.c8_output/
```

**3. Add npm scripts to package.json:**
```json
"test:coverage": "c8 node tests/run-all.js --parallel",
"coverage:report": "c8 report",
"coverage:check": "c8 check-coverage"
```

**4. Run baseline measurement:**
```bash
npm run test:coverage
```

Record ALL of these:
- Test count in run-all.js: ___ (expected ~27)
- Line coverage: ___%
- Branch coverage: ___%
- Function coverage: ___%
- Statement coverage: ___%
- Files with 0% coverage: [list them — expect message-board.js, ship-memory.js, red-team/*.js]
- Files with >80% coverage: [list them]

**5. Set ratchet threshold:**

Take each baseline metric, subtract 1, and write literal integers into .c8rc.json:
```json
{
  "include": ["src/**/*.js"],
  "exclude": [
    "tests/**",
    "node_modules/**",
    "data/**"
  ],
  "reporter": ["text", "text-summary", "lcov", "html"],
  "report-dir": "coverage",
  "all": true,
  "temp-directory": ".c8_output",
  "check-coverage": true,
  "_comment": "Ratchet: update these numbers upward after improving coverage. Never decrease.",
  "lines": 0,
  "branches": 0,
  "functions": 0,
  "statements": 0
}
```
Replace the 0s with (baseline - 1) for each metric.

**6. Verify threshold:**
```bash
npm run coverage:check   # Should exit 0
```

**7. Open HTML report:**
```bash
# Verify it was generated:
ls coverage/index.html
```

**8. Commit:**
```bash
git add .c8rc.json .gitignore package.json package-lock.json
git commit -m "chore: add c8 coverage reporting with ratchet threshold"
```

**9. Final verification:**
```bash
npm test             # Regular tests still pass
npm run test:coverage # Coverage run passes with threshold
npm run coverage:check # Threshold check passes
```

### Acceptance Criteria
- [ ] `npm run test:coverage` produces coverage report
- [ ] Baseline coverage documented (all 4 metrics + distribution)
- [ ] Ratchet threshold set (literal integers in .c8rc.json)
- [ ] `npm run coverage:check` exits 0
- [ ] `coverage/` and `.c8_output/` gitignored
- [ ] HTML report exists at `coverage/index.html`
- [ ] Zero changes to test files or test runner
- [ ] All existing tests still pass

---

## Report Format

When done, report:
```
Chain E complete.
Coverage setup: [PASS/FAIL]
Baseline (against N tests in run-all.js):
  Lines: ___%, Branches: ___%, Functions: ___%, Statements: ___%
  Files at 0%: [list]
Ratchet thresholds set: lines=___, branches=___, functions=___, statements=___
Commit: [hash]
```
