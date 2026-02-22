# Plan 0026: SE Chain A — Quick Wins (commit discipline + package-lock)

**Type:** Generator chain (2 tasks, 2 repos)
**Estimated time:** ~75 minutes
**Dependencies:** None — this is the first chain.

---

## Task 1: Plan 006 Phase A — Commit Discipline Setup (npc-persona)

### Goal
Install commitlint + .gitmessage template in npc-persona-prototype. The commitlint hook wiring is deferred to Chain C (when husky is installed).

### Steps

```bash
cd ~/software/npc-persona-prototype
```

**1. Install commitlint:**
```bash
npm install --save-dev @commitlint/cli @commitlint/config-conventional
```

**2. Create commitlint.config.js:**
```js
module.exports = { extends: ['@commitlint/config-conventional'] };
```

**3. Create .gitmessage (interim enforcement until hook is wired):**
```
# type(scope): description
#
# Types: feat, fix, refactor, chore, test, docs, style, perf
# Scope: ai, npc, memory, game, ui, data (optional)
#
# Body: explain WHY, not WHAT
```

**4. Set git template:**
```bash
git config commit.template .gitmessage
```

**5. Set merge strategy:**
```bash
git config merge.ff only
```

**6. Commit:**
```bash
git add commitlint.config.js .gitmessage package.json package-lock.json
git commit -m "chore: add commitlint + .gitmessage template for commit discipline"
```

**7. Verify:**
```bash
# Test commitlint against a bad message:
echo "bad message" | npx commitlint  # Should fail
echo "chore: test message" | npx commitlint  # Should pass
```

### Acceptance Criteria
- [ ] commitlint.config.js exists
- [ ] .gitmessage template exists
- [ ] `git config commit.template` returns `.gitmessage`
- [ ] `git config merge.ff` returns `only`
- [ ] commitlint validates good/bad messages correctly
- [ ] npm test still passes

---

## Task 2: Plan 007 — Track package-lock.json (traveller)

### Goal
Stop gitignoring package-lock.json in traveller-starship-operations-vtt.

### Prerequisites
- Node >=18.0.0
- Native build tools for better-sqlite3: `python3 --version && make --version && gcc --version`

### Steps

```bash
cd ~/software/traveller-starship-operations-vtt
```

**1. Check for .npmrc overrides:**
```bash
cat ~/.npmrc 2>/dev/null | grep package-lock
cat .npmrc 2>/dev/null | grep package-lock
```
If `package-lock=false` is set, remove it.

**2. Edit .gitignore — remove `package-lock.json` line:**
Find and remove the line containing `package-lock.json` from `.gitignore`. Verify `node_modules/` is still present.

**3. Check client/ subdirectory:**
```bash
ls client/package-lock.json 2>/dev/null
```
If it exists or can be generated (`cd client && npm install`), it should also be committed.

**4. Regenerate clean lock file:**
```bash
rm -rf node_modules
npm install
```
Note: Heavy deps (puppeteer, better-sqlite3). This takes a few minutes.

**5. Commit:**
```bash
git add .gitignore package-lock.json
git add client/package-lock.json 2>/dev/null
git commit -m "chore: track package-lock.json for reproducible installs"
```

**6. Verify:**
```bash
# Clone to temp dir and test npm ci
git clone . /tmp/traveller-verify
cd /tmp/traveller-verify
npm ci
npm test
cd ~/software/traveller-starship-operations-vtt
rm -rf /tmp/traveller-verify
```

### Acceptance Criteria
- [ ] No `.npmrc` overrides for package-lock
- [ ] `package-lock.json` removed from `.gitignore`
- [ ] Root `package-lock.json` committed
- [ ] `client/package-lock.json` committed (if exists)
- [ ] `npm ci` succeeds from clean clone
- [ ] `npm test` passes
- [ ] `node_modules/` still gitignored

---

## Report Format

When done, report:
```
Chain A complete.
Task 1 (006A): [PASS/FAIL] — commitlint + .gitmessage in npc-persona
Task 2 (007): [PASS/FAIL] — package-lock tracked in traveller
Commits: [list hashes]
Issues: [any unexpected problems]
```
