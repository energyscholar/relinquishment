# Plan 0032: SE Chain G — Restructure Reconnaissance

**Type:** Generator chain (Plan 005 Phase 0, decision gate)
**Estimated time:** ~2 hours
**Dependencies:** Chains C and E complete (linting + coverage in place)

---

## DECISION GATE

This chain produces the import graph, __dirname audit, and restructure blueprint. Do NOT proceed to Chain H (execution) without Auditor review. Bruce must decide:
1. PROJECT_ROOT constant vs per-file __dirname fixup
2. `src/data/` naming (keep vs rename to `src/world/`)
3. chat-tui.js placement (root vs ui/)

---

## Task 1: Import Graph (Plan 005 Phase 0.1-0.2)

```bash
cd ~/software/npc-persona-prototype
```

**1. Extract all require() dependencies:**
```bash
grep -rn "require.*\./" src/*.js | grep -v node_modules > /tmp/import-graph.txt
```

**2. Try madge for visualization:**
```bash
npx madge --json src/ > /tmp/import-graph.json 2>/dev/null || echo "madge failed — use grep-based graph instead"
npx madge --circular src/ 2>/dev/null || echo "madge failed — check grep output for circular deps manually"
npx madge --image /tmp/import-graph.png src/ 2>/dev/null || echo "graphviz not installed"
```

**Fallback if madge fails to install (network issues, native deps):** Build the graph manually from `/tmp/import-graph.txt` grep output. Count inbound/outbound references per file to identify fan-in/fan-out.

**3. Identify coupling clusters from the graph:**
- Files that import each other (circular deps) — MUST stay in same directory
- Files imported by many others (high fan-in) — moves are expensive
- Files that import many others (high fan-out) — likely to break when deps move

---

## Task 2: chat-tui.js Analysis (Plan 005 Phase 0.3)

**1. Map chat-tui.js connections:**
```bash
# What does chat-tui.js require?
grep -n "require(" src/chat-tui.js | grep -v node_modules

# What requires chat-tui.js?
grep -rn "require.*chat-tui" src/ tests/ scripts/ | grep -v node_modules
```

**2. Decide placement:**
- If chat-tui.js has >10 imports from src/ AND <5 files require it → move to ui/ (update its imports)
- If >5 files require chat-tui.js → keep at root (cheaper to not move it)
- Count both directions and recommend.

---

## Task 3: Test Suite Verification (Plan 005 Phase 0.4)

**1. Temporarily break one require path:**
```js
// In src/memory.js, temporarily change:
// const persona = require('./persona');
// to:
// const persona = require('./BROKEN');
```

**2. Run tests:**
```bash
npm test
```
- If tests FAIL → test suite catches broken imports (good safety net)
- If tests PASS → need `node -e "require('./src/index.js')"` as additional verification

**3. Revert the break immediately.**

---

## Task 4: __dirname Audit (Plan 005 Phase 0.6 — CRITICAL)

**1. Full audit:**
```bash
grep -rn "__dirname" src/ | grep -v node_modules
```

**2. For each hit, build a fixup table:**

| File | Current path | Target directory | Current prefix | New prefix needed |
|------|-------------|-----------------|----------------|-------------------|
| src/persona.js | `../data/npcs` | src/npc/ | `../` | `../../` |
| ... | ... | ... | ... | ... |

**3. Count total path edits needed.** (Expected: ~41 across 28 files.)

**4. Evaluate PROJECT_ROOT alternative:**

A single `src/project-root.js`:
```js
module.exports = require('path').resolve(__dirname, '..');
```

Then every file uses:
```js
const PROJECT_ROOT = require('../project-root');  // or appropriate depth
const DATA_DIR = path.join(PROJECT_ROOT, 'data/npcs');
```

**Trade-offs:**
- Per-file fixup: 41 edits now, future moves need re-editing
- PROJECT_ROOT: 28 files get 1 new require + path rewrite, future moves only update 1 require per file

**Recommend one approach with reasoning.**

---

## Task 5: Non-require References (Plan 005 Phase 0.5)

```bash
grep -n "src/" package.json
grep -rn "src/" tests/run-all.js
grep -rn "require.*\.\./src/" scripts/
grep -rn "path.join.*__dirname.*\.\./src/" tests/
```

---

## Output: Restructure Blueprint (MUST BE WRITTEN TO FILE)

**CRITICAL:** Write the blueprint to `~/software/relinquishment/plans/0032-G-blueprint-output.md`. Chain H's Generator will read this file — it has NO other way to access your findings.

The blueprint file must contain ALL of the following sections:

1. **Import graph summary** — clusters, high-fan-in files, circular deps
2. **chat-tui.js recommendation** — move to ui/ or stay at root, with counts
3. **Test suite verification result** — catches broken imports: yes/no
4. **Complete __dirname fixup table** — every file, every path, every new prefix. This table is used directly by Chain H Step 4. If it's incomplete, Chain H will break files silently.
5. **PROJECT_ROOT recommendation** — yes/no, with reasoning
6. **Non-require references** that need updating (package.json, run-all.js, scripts/, tests/)
7. **Concrete file-to-directory mapping** — for EACH of the 9 batch directories, list EVERY file that goes in it. Chain H executes `git mv` from this list. Example:
   ```
   Batch 1 — src/data/:
     src/geography-data.js → src/data/geography-data.js
     src/resource-lookup.js → src/data/resource-lookup.js
     ...
   ```
8. **Revised batch order** — adjust from default if coupling data suggests different grouping
9. **Naming recommendation** — `src/data/` vs `src/world/` vs `src/gamedata/`

---

## Report Format

```
Chain G complete.
Import graph: [N files, N circular deps, highest fan-in file=___]
chat-tui.js: [move to ui/ / stay at root] — [count] inbound, [count] outbound
Test verification: [catches broken imports / needs additional verification]
__dirname audit: [N files, N total path edits]
PROJECT_ROOT recommendation: [yes/no]
Naming: [src/data/ / src/world/ / src/gamedata/]
Ready for Chain H: [YES / NO — needs decision on ___]
```
