# Plan 0034: SE Chain I — TypeScript Setup

**Type:** Generator chain (Plan 001 Phase 1)
**Estimated time:** ~2-4 hours
**Dependencies:** Chain H complete (directory structure stable)

---

## Task: Enable TypeScript Type Checking in npc-persona

### Goal
Add tsconfig.json with allowJs + checkJs + noEmit. Establish error baseline. Add npm script. NO file renames — JSDoc-only approach.

### Steps

```bash
cd ~/software/npc-persona-prototype
```

**1. Check Node version:**
```bash
node --version  # Document for reference
```

**2. Install TypeScript + type declarations:**
```bash
npm install --save-dev typescript @types/node
```

**3. Audit third-party deps for types:**
- `@anthropic-ai/sdk` — ships own types (.d.ts). No @types needed.
- `dotenv` — ships own types. No @types needed.
- For npc-persona, `@types/node` is sufficient.

**4. Create tsconfig.json:**
```json
{
  "compilerOptions": {
    "target": "ES2021",
    "module": "commonjs",
    "allowJs": true,
    "checkJs": true,
    "noEmit": true,
    "strict": false,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "baseUrl": "."
  },
  "include": ["src/**/*", "scripts/**/*"],
  "exclude": ["node_modules", "data"]
}
```

Notes:
- `module: "commonjs"` — confirmed CJS codebase.
- `strict: false` — start permissive, tighten later.
- `noEmit: true` — check-only, no compilation, no build step.
- `scripts/**/*` included — scripts import from src/.
- Tests initially excluded (included in Step 8).

**5. Run initial check and triage:**
```bash
npx tsc --noEmit 2>&1 | head -100                        # Preview
npx tsc --noEmit 2>&1 | wc -l                             # Count
npx tsc --noEmit 2>&1 | grep "error TS" | \
  sed 's/.*error //' | sort | uniq -c | sort -rn          # Categorize
```

**CommonJS-specific gotchas to expect:**
- `module.exports = function() {}` then `module.exports.helper = ...` — TS loses export shape
- `exports.foo = ...` — partial type inference
- Dynamic `require('./' + name)` — gives `any`

**6. Suppress errors to establish baseline:**

For each file with errors, use targeted suppression:
```js
// @ts-ignore — [reason]   (above specific lines — preferred)
// @ts-nocheck              (top of file — last resort)
```

Goal: `npx tsc --noEmit` exits 0.

**7. Add npm script:**
```json
"typecheck": "tsc --noEmit"
```

**8. Include tests in tsconfig:**
Add `"tests/**/*"` to `include` in tsconfig.json.
Run `npx tsc --noEmit` again.
Suppress test file errors with `// @ts-nocheck` at top of each test file.

**9. Document baseline:**
Record in this chain's report:
- Date started
- Initial src/ error count (before suppression)
- Initial tests/ error count (before suppression)
- Error categories (top 5 by frequency)
- Files with @ts-nocheck count
- Files with @ts-ignore count

**10. Commit:**
```bash
git add tsconfig.json package.json package-lock.json src/ tests/ scripts/
git commit -m "chore: add TypeScript type checking (allowJs + checkJs, JSDoc-only)"
```

**11. Verify:**
```bash
npm run typecheck    # Exits 0
npm test             # Tests still pass
npm run lint         # ESLint still clean
npm run test:coverage # Coverage still works
```

---

## Acceptance Criteria
- [ ] tsconfig.json exists with allowJs, checkJs, noEmit
- [ ] typescript and @types/node in devDependencies
- [ ] `npm run typecheck` exits 0 (with documented suppressions)
- [ ] Tests included in tsconfig (with @ts-nocheck suppression)
- [ ] Error baseline documented (counts + categories)
- [ ] No runtime behavior changes
- [ ] All existing tests still pass
- [ ] No files renamed (JSDoc-only approach)
- [ ] ESLint still clean
- [ ] Coverage still works

---

## Report Format

```
Chain I complete.
TypeScript setup: [PASS/FAIL]
Node version: [version]
Baseline:
  src/ errors (before suppression): [count]
  tests/ errors (before suppression): [count]
  Top error categories: [list top 5]
  Files with @ts-nocheck: [count]
  Files with @ts-ignore: [count]
Commit: [hash]
```
