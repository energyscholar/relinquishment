# Plan 0033: SE Chain H — Restructure Execution

**Type:** Generator chain (Plan 005 Phases 1-3)
**Estimated time:** ~6-10 hours (may need to split into H1/H2 if too large)
**Dependencies:** Chain G complete + Auditor-approved blueprint

---

## PREREQUISITES

Before executing, confirm:
1. Chain G blueprint reviewed and approved by Auditor
2. __dirname approach decided: [ ] per-file fixup / [ ] PROJECT_ROOT constant
3. chat-tui.js placement decided: [ ] move to ui/ / [ ] stay at root
4. `src/data/` naming decided: [ ] keep / [ ] rename to src/world/
5. Batch order finalized (may differ from default if coupling data suggests changes)

**If any prerequisite is missing, STOP and return to Auditor.**

---

## Default Batch Order (adjust per Chain G blueprint)

1. **data/** (or world/) — ~7 files, likely few inbound deps
2. **memory/** — 2 files
3. **ai/** — 3 files
4. **ui/** — 3-4 files (chat-tui.js per decision)
5. **npc/** — 12 files, some cross-deps
6. **game/mechanics/** — 7 files
7. **game/narrative/** — 7 files
8. **game/adventure/** — 8 files
9. **game/systems/** — 4 files

---

## Per-Batch Procedure (repeat for each batch)

```bash
cd ~/software/npc-persona-prototype
```

### Step 1: Create directory
```bash
mkdir -p src/data  # or src/world, per decision
```

### Step 2: Move files
```bash
git mv src/geography-data.js src/data/
git mv src/resource-lookup.js src/data/
# ... all files in this batch
```

### Step 3: Fix require() paths — files that IMPORT the moved files
```bash
# For EACH moved file:
grep -rn "require.*geography-data" src/ tests/ scripts/ | grep -v node_modules
# Update each reference to the new path
```

### Step 4: Fix __dirname data paths — paths INSIDE the moved files (CRITICAL)
```bash
# For EACH moved file, check its __dirname usage:
grep -n "__dirname" src/data/geography-data.js
# Update relative path depth per the fixup table from Chain G
# Moving 1 level deeper: '../data/' → '../../data/'
# Moving 2 levels deeper: '../data/' → '../../../data/'
```

**If using PROJECT_ROOT approach:**
```bash
# Replace __dirname-based paths with PROJECT_ROOT-based paths
# const DATA_DIR = path.join(__dirname, '../data/npcs');
# becomes:
# const PROJECT_ROOT = require('../project-root');
# const DATA_DIR = path.join(PROJECT_ROOT, 'data/npcs');
```

### Step 5: Fix non-require references
```bash
grep -rn "geography-data" package.json tests/run-all.js scripts/ *.md
```

### Step 6: Verify (ALL must pass before commit)
```bash
npm test                                    # Tests pass
node -e "require('./src/index.js')"         # Full require graph loads
npm run lint                                # ESLint clean
npm run format:check                        # Prettier clean
```

### Step 7: Commit (ONLY if Step 6 passes)
```bash
git add -u
git add src/data/   # New directory
git commit -m "refactor(data): move data files to src/data/"
```

---

## Phase 2: Fix Test References

After ALL batches complete:
```bash
grep -rn "require.*\.\./src/" tests/ | grep -v node_modules
```
Update any broken test imports. Run `npm test` after each fix.

---

## Phase 3: Final Verification

```bash
npm test                                # All tests pass
npm run lint                            # ESLint clean
npm run format:check                    # Prettier clean
npm run test:coverage                   # Coverage still works
node -e "require('./src/index.js')"     # Full require graph loads
git log --follow -- src/data/geography-data.js  # Rename tracking works

# Verify ESLint doesn't ignore src/data/:
npx eslint src/data/geography-data.js   # Should lint, not skip
```

---

## Rollback

**All-or-nothing.** If any batch fails and cannot be fixed forward:
1. Revert ALL completed batch commits in reverse order
2. Diagnose the failure
3. Restart from batch 1

**Do NOT partially revert.**

---

## Acceptance Criteria
- [ ] Import graph consulted for batch ordering
- [ ] No files remain in `src/` root except `index.js` (+ `project-root.js` if chosen)
- [ ] All tests pass (`npm test`)
- [ ] Full require graph loads (`node -e "require('./src/index.js')"`)
- [ ] `npm run lint` clean
- [ ] `npm run format:check` clean
- [ ] `npm run test:coverage` works (coverage still measured)
- [ ] Each batch committed separately
- [ ] `git log --follow` tracks renames
- [ ] No __dirname paths resolve to wrong directory
- [ ] ESLint does NOT ignore `src/data/`
- [ ] scripts/ require paths updated where needed
- [ ] Existing subdirectories (knowledge-extraction/, red-team/) unchanged

---

## Report Format

```
Chain H complete.
Batches: [N/9] successful
Approach: [per-file fixup / PROJECT_ROOT]
Files moved: [total count]
__dirname paths fixed: [total count]
require() paths fixed: [total count]
Commits: [list hashes]
Coverage after restructure: Lines=___%, Branches=___%, Functions=___%, Statements=___%
Issues: [any unexpected problems]
```
