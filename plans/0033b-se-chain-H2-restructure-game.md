# Plan 0033b: SE Chain H2 — Restructure Execution (game/ batches)

**Type:** Generator chain (Plan 005 Phases 1-3, continued)
**Estimated time:** ~3-5 hours
**Dependencies:** Chain H1 complete (batches 1-5 done, tests passing)

---

## PREREQUISITES

Before executing, confirm:
1. Chain H1 completed successfully (batches 1-5: data, memory, ai, ui, npc)
2. `npm test` passes in current state
3. Blueprint file exists: `~/software/relinquishment/plans/0032-G-blueprint-output.md`

**If H1 is not complete or tests are failing, STOP.**

**CRITICAL:** Read `~/software/relinquishment/plans/0032-G-blueprint-output.md` for:
- File-to-directory mapping for batches 6-9
- __dirname fixup table
- Non-require references

---

## Batches to Execute

6. **game/mechanics/** — 7 files
7. **game/narrative/** — 7 files
8. **game/adventure/** — 8 files
9. **game/systems/** — 4 files

---

## Per-Batch Procedure (same as H1 — repeat for each batch)

```bash
cd ~/software/npc-persona-prototype
```

### Step 1: Create directory
```bash
mkdir -p src/game/mechanics
```

### Step 2: Move files
```bash
# Use the file list from the blueprint for this batch
git mv src/skill-check.js src/game/mechanics/
# ... all files in this batch per blueprint
```

### Step 3: Fix require() paths — files that IMPORT the moved files
```bash
grep -rn "require.*skill-check" src/ tests/ scripts/ | grep -v node_modules
# Update each reference to the new path
```

### Step 4: Fix __dirname data paths (CRITICAL)
Consult `~/software/relinquishment/plans/0032-G-blueprint-output.md` fixup table.
```bash
grep -n "__dirname" src/game/mechanics/skill-check.js
# Apply the exact prefix change from the fixup table
```

### Step 5: Fix test imports for this batch (DO NOT DEFER)
```bash
grep -rn "require.*skill-check" tests/ | grep -v node_modules
# Update each test's require path
```

### Step 6: Fix non-require references
```bash
grep -rn "skill-check" package.json tests/run-all.js scripts/ *.md
```

### Step 7: Verify (ALL must pass before commit)
```bash
npm test                                    # Tests pass
node -e "require('./src/index.js')"         # Full require graph loads
npm run lint                                # ESLint clean
npm run format:check                        # Prettier clean
```

### Step 8: Verify __dirname paths resolve at runtime
```bash
node -e "const f = require('./src/game/mechanics/skill-check.js'); console.log('loaded OK')"
```

### Step 9: Commit (ONLY if Steps 7 AND 8 pass)
```bash
git add -u
git add src/game/mechanics/
git commit -m "refactor(game/mechanics): move mechanics files to src/game/mechanics/"
```

---

## After ALL Batches: Final Verification

```bash
npm test                                # All tests pass
npm run lint                            # ESLint clean
npm run format:check                    # Prettier clean
npm run test:coverage                   # Coverage still works
node -e "require('./src/index.js')"     # Full require graph loads
git log --follow -- src/game/mechanics/skill-check.js  # Rename tracking works

# Verify no files left in src/ root (except index.js + project-root.js if chosen):
ls src/*.js

# Verify ESLint doesn't ignore new dirs:
npx eslint src/game/mechanics/skill-check.js

# Sweep for straggler test imports:
grep -rn "require.*\.\./src/[a-z]" tests/ | grep -v node_modules | grep -v "src/index"
```

---

## Rollback

If any H2 batch fails and cannot be fixed forward:
1. Revert H2's completed batch commits in reverse order
2. Report failure to Auditor — Auditor has H1's commit hashes and will decide whether H1 also needs rollback
3. Do NOT attempt to revert H1 commits yourself (you do not have H1's hashes)

**Do NOT partially revert H2.**

---

## Acceptance Criteria
- [ ] All 4 game/* batches completed and committed
- [ ] No files remain in `src/` root except `index.js` (+ `project-root.js` if chosen)
- [ ] All tests pass (`npm test`)
- [ ] Full require graph loads (`node -e "require('./src/index.js')"`)
- [ ] `npm run lint` clean
- [ ] `npm run format:check` clean
- [ ] `npm run test:coverage` works
- [ ] `git log --follow` tracks renames
- [ ] No __dirname paths resolve to wrong directory
- [ ] Existing subdirectories (knowledge-extraction/, red-team/) unchanged

---

## Report Format

```
Chain H2 complete.
Batches: [N/4] successful (6-9)
Files moved: [total count]
__dirname paths fixed: [total count]
require() paths fixed: [total count]
Commits: [list hashes]
Coverage after restructure: Lines=___%, Branches=___%, Functions=___%, Statements=___%
Combined with H1: [total files moved across all 9 batches]
Issues: [any unexpected problems]
```
