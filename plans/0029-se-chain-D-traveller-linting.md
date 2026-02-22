# Plan 0029: SE Chain D — Traveller Linting

**Type:** Generator chain (Plan 002 Phase 2)
**Estimated time:** ~2-3 hours
**Dependencies:** Chain C complete (approach proven in npc-persona)

---

## Task: ESLint + Prettier for traveller-starship-operations-vtt

### Goal
Add ESLint 9 (flat config) + Prettier to traveller backend. The client already has its own ESLint 9 config — do NOT touch client/.

### Critical Context
- Traveller backend code is in `lib/` (NOT `src/` — there is no src/ directory)
- `public/` contains 126 browser JavaScript files — needs DIFFERENT ESLint config (browser globals, not Node)
- `client/` has its own `eslint.config.js` (ESM format, React+TS) — exclude from root config
- ~795 JS files total outside client/: 237 lib, 389 tests, 126 public, 23 scripts, 20 other

### Steps

```bash
cd ~/software/traveller-starship-operations-vtt
```

**1. Install dependencies:**
```bash
npm install --save-dev eslint@^9 prettier eslint-config-prettier@^10 @eslint/js@^9 globals
```

**2. Create eslint.config.js (TWO config blocks — Node + browser):**
```js
const js = require('@eslint/js');
const prettierConfig = require('eslint-config-prettier');
const globals = require('globals');

module.exports = [
  js.configs.recommended,
  prettierConfig,
  // Node.js CommonJS files (backend, tests, scripts, tools, config)
  {
    files: ['lib/**/*.js', 'config/**/*.js', 'scripts/**/*.js', 'tools/**/*.js',
            'tests/**/*.js', 'test/**/*.js', '*.js'],
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
  // Browser JS files (public/)
  {
    files: ['public/**/*.js'],
    languageOptions: {
      ecmaVersion: 'latest',
      sourceType: 'script',
      globals: {
        ...globals.browser,
      },
    },
    rules: {
      'no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],
      'no-console': 'off',
    },
  },
  {
    ignores: [
      'node_modules/',
      'client/',
      'data/',
      'coverage/',
      'dist/',
      'reference/',
      'sessions/',
      'player-data/',
    ],
  },
];
```

**3. Create .prettierrc (same as npc-persona):**
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
client/
coverage/
dist/
data/
reference/
sessions/
player-data/
*.db
*.sqlite
```

**5. Add npm scripts to package.json:**
```json
"lint": "eslint .",
"lint:fix": "eslint --fix .",
"format": "prettier --write .",
"format:check": "prettier --check ."
```

**6. Commit config FIRST:**
```bash
git add eslint.config.js .prettierrc .prettierignore package.json package-lock.json
git commit -m "chore: add ESLint 9 + Prettier configuration (backend + public)"
```

**7. Run bulk format:**
```bash
npx prettier --write .
npx eslint --fix .
```

**8. Commit formatting:**
```bash
git add -u  # Only modified files
git commit -m "style: apply Prettier formatting to all JS files"
```

**9. Set up git-blame-ignore-revs:**
```bash
echo "$(git rev-parse HEAD) # style: apply Prettier formatting" >> .git-blame-ignore-revs
git config blame.ignoreRevsFile .git-blame-ignore-revs
git add .git-blame-ignore-revs
git commit -m "chore: add git-blame-ignore-revs for formatting commit"
```

**10. Verify:**
```bash
npm run lint         # Should exit clean (warnings OK)
npm run format:check # Should exit clean
npm test             # Existing tests still pass

# Verify browser files lint correctly (no false positives on document/window):
npx eslint public/login.js 2>&1 | head -20  # Representative browser file
# Should show no 'no-undef' errors for document, window, etc.

# Verify client is untouched:
cd client && npx eslint . && cd ..  # Client's own config still works
```

### Acceptance Criteria
- [ ] `npm run lint` exits clean
- [ ] `npm run format:check` exits clean
- [ ] ESLint flat config with TWO blocks (Node.js + browser)
- [ ] `client/` excluded — client's own ESLint config untouched
- [ ] `public/` files linted with browser globals (no false positives on `document`, `window`)
- [ ] Config commit separate from formatting commit
- [ ] `.git-blame-ignore-revs` includes formatting hash
- [ ] All existing tests pass
- [ ] Same `.prettierrc` as npc-persona

---

## Report Format

When done, report:
```
Chain D complete.
Traveller linting: [PASS/FAIL]
  Backend lint warnings: [count]
  Public lint warnings: [count]
  Files formatted: [count]
Commits: [list hashes]
Issues: [any unexpected problems]
```
