# Plan 0028: SE Chain C — npc-persona Linting + Hooks

**Type:** Generator chain (Plan 002 Phase 1 + Plan 006 Phase B)
**Estimated time:** ~3 hours
**Dependencies:** Chain A complete (commitlint already installed)

---

## Task 1: ESLint + Prettier Setup (Plan 002 Phase 1)

### Goal
Add ESLint 9 (flat config) + Prettier to npc-persona-prototype. Format all files. Set up pre-commit hooks.

### Steps

```bash
cd ~/software/npc-persona-prototype
```

**1. Install dependencies:**
```bash
npm install --save-dev eslint@^9 prettier eslint-config-prettier@^10 @eslint/js@^9 globals
```

**2. Create eslint.config.js:**
```js
const js = require('@eslint/js');
const prettierConfig = require('eslint-config-prettier/flat');
const globals = require('globals');

module.exports = [
  js.configs.recommended,
  prettierConfig,
  {
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'commonjs',
      globals: {
        ...globals.node,
      },
    },
    rules: {
      'no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],
      'no-console': 'off',
    },
  },
  {
    ignores: ['node_modules/', 'data/', 'backups/', 'coverage/'],
  },
];
```

**3. Create .prettierrc:**
```json
{
  "singleQuote": true,
  "semi": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 100
}
```

**4. Create .prettierignore:**
```
node_modules/
data/
backups/
coverage/
```

**5. Commit config files FIRST (separate from formatting):**
```bash
git add eslint.config.js .prettierrc .prettierignore package.json package-lock.json
git commit -m "chore: add ESLint 9 + Prettier configuration"
```

**6. Run bulk format:**
```bash
npx prettier --write "src/**/*.js" "tests/**/*.js" "scripts/**/*.js"
npx eslint --fix "src/**/*.js" "tests/**/*.js" "scripts/**/*.js"
```

**7. Commit formatting (separate commit):**
```bash
# Verify only formatting changes are staged — no config files or other modifications:
git status
git add src/ tests/ scripts/
git commit -m "style: apply Prettier formatting to all JS files"
```

**8. Set up git-blame-ignore-revs:**
```bash
echo "$(git rev-parse HEAD) # style: apply Prettier formatting" >> .git-blame-ignore-revs
git config blame.ignoreRevsFile .git-blame-ignore-revs
git add .git-blame-ignore-revs
git commit -m "chore: add git-blame-ignore-revs for formatting commit"
```

**9. Add npm scripts to package.json:**
```json
"lint": "eslint src/ tests/ scripts/",
"lint:fix": "eslint --fix src/ tests/ scripts/",
"format": "prettier --write \"src/**/*.js\" \"tests/**/*.js\" \"scripts/**/*.js\"",
"format:check": "prettier --check \"src/**/*.js\" \"tests/**/*.js\" \"scripts/**/*.js\""
```

**9b. Commit npm scripts (before moving to Task 2):**
```bash
git add package.json
git commit -m "chore: add lint and format npm scripts"
```

**10. Verify:**
```bash
npm run lint        # Should exit clean (warnings OK, no errors)
npm run format:check # Should exit clean
npm test            # Existing tests still pass
```

---

## Task 2: Pre-commit Hooks + commitlint Hook (Plan 002 Step 1.9 + Plan 006 Phase B)

### Goal
Install husky + lint-staged. Wire commitlint hook (commitlint was installed in Chain A).

### Steps

**1. Install husky + lint-staged:**
```bash
npm install --save-dev husky lint-staged
npx husky init
```

**2. Replace default pre-commit hook (husky init creates "npm test" — wrong):**
```bash
echo "npx lint-staged" > .husky/pre-commit
```

**3. Wire commitlint hook (Plan 006 Phase B):**
```bash
echo 'npx --no -- commitlint --edit "$1"' > .husky/commit-msg
```

**4. Add lint-staged config to package.json:**
```json
"lint-staged": {
  "*.js": ["prettier --write", "eslint --fix"]
}
```

**5. Commit:**
```bash
git add .husky/ package.json package-lock.json
git commit -m "chore: add husky + lint-staged + commitlint hooks"
```

**6. Verify hooks work:**
```bash
# Test lint-staged: modify a file, stage it, commit
echo "// test" >> src/memory.js
git add src/memory.js
git commit -m "test: verify lint-staged hook"
# If it works, prettier+eslint run on the staged file
# Revert:
git reset --soft HEAD~1
git checkout -- src/memory.js

# Test commitlint: try a bad commit message
echo "// test" >> src/memory.js
git add src/memory.js
git commit -m "bad message"  # Should be REJECTED by commitlint
git checkout -- src/memory.js
```

### Acceptance Criteria (both tasks)
- [ ] `npm run lint` exits clean
- [ ] `npm run format:check` exits clean
- [ ] ESLint uses flat config format (`eslint.config.js`)
- [ ] Config commit is separate from formatting commit
- [ ] `.git-blame-ignore-revs` includes formatting commit hash
- [ ] All existing tests still pass (`npm test`)
- [ ] No functional code changes in the formatting commit
- [ ] `.husky/pre-commit` contains `npx lint-staged` (NOT `npm test`)
- [ ] `.husky/commit-msg` contains commitlint command
- [ ] lint-staged runs prettier+eslint on commit
- [ ] commitlint rejects malformed commit messages

---

## Report Format

When done, report:
```
Chain C complete.
Task 1 (002.1): [PASS/FAIL] — ESLint + Prettier in npc-persona
  Lint warnings: [count]
  Files formatted: [count]
Task 2 (002.1.9 + 006B): [PASS/FAIL] — husky + lint-staged + commitlint
Commits: [list hashes]
Issues: [any unexpected problems]
```
