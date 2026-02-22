# Plan 0033: SE Chain H1 — Restructure Execution (Batches 1-5)

**Type:** Generator chain (Plan 005 Phases 1-3, first half)
**Estimated time:** ~6-10 hours total, split into TWO Generator runs:
- **H1 (this plan):** Batches 1-5 (data, memory, ai, ui, npc) — ~3-5 hours
- **H2 (Plan 0033b):** Batches 6-9 (game/*) — ~3-5 hours

**Agent sizing:** Each Generator run must stay under ~3-4K words output. 9 batches × 7 steps exceeds this limit. Split at batch 5/6 boundary (npc/ has many cross-deps into game/, so completing npc/ first stabilizes the import graph for game/* batches).
**Dependencies:** Chain G complete + Auditor-approved blueprint

---

## PREREQUISITES

Before executing, confirm:
1. Chain G blueprint file exists: `~/software/relinquishment/plans/0032-G-blueprint-output.md`
2. Blueprint reviewed and approved by Auditor
3. __dirname approach decided: [ ] per-file fixup / [ ] PROJECT_ROOT constant
4. chat-tui.js placement decided: [ ] move to ui/ / [ ] stay at root
5. `src/data/` naming decided: [ ] keep / [ ] rename to src/world/
6. Batch order finalized (may differ from default if coupling data suggests changes)

**If any prerequisite is missing, STOP and return to Auditor.**

**CRITICAL:** Read `~/software/relinquishment/plans/0032-G-blueprint-output.md` FIRST. It contains:
- The concrete file-to-directory mapping (which files go in which batch)
- The __dirname fixup table (exact path edits per file)
- Non-require references that need updating
Use the blueprint as your source of truth. The defaults below are FALLBACKS only.

---

## Batches for This Run (H1: 1-5 only)

Adjust per Chain G blueprint. Batches 6-9 are in Plan 0033b (Chain H2).

1. **data/** (or world/) — ~7 files, likely few inbound deps
2. **memory/** — 2 files
3. **ai/** — 3 files
4. **ui/** — 3-4 files (chat-tui.js per decision)
5. **npc/** — 12 files, some cross-deps

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

**Source:** The complete fixup table is in `~/software/relinquishment/plans/0032-G-blueprint-output.md`, section "Complete __dirname fixup table". Consult it for every file in this batch.

```bash
# For EACH moved file, check its __dirname usage:
grep -n "__dirname" src/data/geography-data.js
# Look up the file in the blueprint fixup table for the exact new prefix
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

### Step 5: Fix test imports for this batch (DO NOT DEFER)
```bash
# For EACH moved file in this batch, fix test imports immediately:
grep -rn "require.*geography-data" tests/ | grep -v node_modules
# Update each test's require path to the new location
```

### Step 6: Fix non-require references
```bash
grep -rn "geography-data" package.json tests/run-all.js scripts/ *.md
```

### Step 7: Verify (ALL must pass before commit)
```bash
npm test                                    # Tests pass
node -e "require('./src/index.js')"         # Full require graph loads
npm run lint                                # ESLint clean
npm run format:check                        # Prettier clean
```

### Step 8: Verify __dirname paths resolve at runtime (CRITICAL)
```bash
# Pick one moved file from this batch that uses __dirname for data access.
# Run it in isolation to confirm the path resolves:
node -e "const f = require('./src/data/geography-data.js'); console.log('loaded OK')"
# If it throws ENOENT or similar, the __dirname fixup is wrong. Fix before committing.
```

### Step 9: Commit (ONLY if Steps 7 AND 8 pass)
```bash
git add -u
git add src/data/   # New directory
git commit -m "refactor(data): move data files to src/data/"
```

---

## After ALL Batches: Sweep for Stragglers

```bash
# Any test imports still referencing old paths?
grep -rn "require.*\.\./src/[a-z]" tests/ | grep -v node_modules | grep -v "src/index"
# Should return nothing — all were fixed per-batch in Step 5
```

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
Chain H1 complete.
Batches: [N/5] successful (1-5)
Approach: [per-file fixup / PROJECT_ROOT]
Files moved: [total count]
__dirname paths fixed: [total count]
require() paths fixed: [total count]
Commits: [list hashes]
Tests passing: [YES/NO]
Ready for H2: [YES/NO]
Issues: [any unexpected problems]
```
