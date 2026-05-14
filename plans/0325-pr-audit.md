# Boettiger PR Audit — Adversarial Review

**Reviewer perspective:** Carl Boettiger, solo maintainer of geo-agent. Princeton physics undergrad. High standards. Zero external contributors ever. Gets dozens of cold approaches. First impression matters.

---

## A. Style Mismatches (He Will Notice)

### 1. Commit scope convention — WRONG on PR 1 and PR 2

**His pattern:** scope = module name in kebab-case.
```
fix(mcp): retry listTools...
fix(hex): point coarser-view advice...
feat(tooltip): add set_tooltip...
feat(auto-approve): default to true...
docs(system-prompt): route 'hex'/'h3 grid'...
```

**Our PRs:**
- PR 1: `fix(security):` — "security" is a category, not a module. Should be `fix(chat-ui):`
- PR 2: `fix(set_style):` — underscore, function name. Should be `fix(map-manager):` or just `fix(style):`
- PR 3: `feat(catalog):` — acceptable. `catalog` maps to `dataset-catalog.js`. ✓

**Fix:** Rewrite commit messages and PR titles for PR 1 and PR 2.

### 2. PR description opener — missing "Fixes #NNN" pattern

**His pattern:**
- PR #208: opens with `Closes #196.` on its own line
- PR #209: opens with `Fixes #206.` in the first sentence

**Our PRs:**
- PR 2 references #161 in the title but doesn't use "Fixes" in the body (correct — we don't fully fix #161, only the masking bug)
- PR 3 should open with `Fixes #177.` since we meet all 4 acceptance criteria

**Fix:** PR 3 body should open with "Fixes #177." PR 2 is correct to not use "Fixes" since the issue asks for more than we deliver.

### 3. PR body section structure

**His pattern:**
- `## Summary` — bullet list of changes
- `## Implementation` — (optional) how it works
- `## Test plan` — checkboxes mixing automated + manual
- `## Related` — (optional) links
- Bold module paths: `**app/main.js**`

**Our PRs:**
- PR 1 uses `## Motivation` and `## Downstream integration` — custom sections he doesn't use
- All PRs lack bold module paths in the summary
- PR 1's "Downstream integration" with the script tag is useful but should be folded into the summary

### 4. Commit message body verbosity

**His style:** 1-3 short sentences, sometimes bullet points. Uses em-dashes.
**Ours:** Multi-paragraph. Too much. Should be 2-3 lines.

---

## B. Code Issues (Correctness)

### 5. PR 3: Existing tests leak console.warn to stderr — FIX REQUIRED

The pre-existing tests at lines 365 and 388 now produce warnings they didn't before:

```
stderr | ...skips a versioned config whose asset_ids are all missing
[Catalog] demo: versioned asset "absent" not found in STAC. Available keys: (none)

stderr | ...skips assets whose STAC entry is missing in filtered mode
[Catalog] demo: configured asset "ghost" not found in STAC. Available keys: (none)
```

Boettiger cares about clean test output (he's been expanding coverage). These are noisy.

**Fix:** Update both existing tests to spy on console.warn. Better: assert the warning fires (converts "silent skip" to "documented warning behavior" — stronger tests).

### 6. PR 1: addMarkdown no-marked fallback is raw innerHTML

When `marked` is not loaded, `addMarkdown` falls to `md` → straight to `innerHTML`:
```javascript
const rawHtml = typeof marked !== 'undefined' ? marked.parse(md) : md;
```

Our DOMPurify fix covers the `marked` path but not this fallback. Not a regression (existing behavior), but a reviewer might ask "why not also handle this?"

**Decision:** Note as out-of-scope in PR description. All downstream apps load marked; this path is unreachable in practice. Fixing it changes semantics (escaping vs rendering).

### 7. PR 2: Empty paintProps edge case

`setStyle(layerId, {})` → `results = []` → `anySucceeded = true` (from `results.length === 0`).

This is defensible (nothing failed = success), but Boettiger might question it. The current code also returns `success: true` for this case, so it's not a regression.

---

## C. Strategic Issues

### 8. Payload not yet prepared

The PRs establish credibility. The "pitch" — governance architecture, white paper link — goes in the paper letter, NOT in the PRs. The letter draft in plan 0325 already has this.

But we could also prepare a SEPARATE artifact: a one-paragraph comment for a relevant GitHub Discussion or issue. This would be posted AFTER PRs are acknowledged, not before.

**Draft payload (for later use, NOT for PRs):**

> The success-masking bug in set_style is a specific instance of what I think of as an "execution governance" failure — the agent acts on incorrect feedback about whether its action succeeded. I've been running a system on Claude Code that catches this class of failure through role separation (planning vs execution) with human authorization gates. The architecture is documented at [whitepaper URL]. The failure cross-matrix in Shift 1 maps exactly this pattern: execution governance failing while truth governance holds.
>
> Happy to discuss if any of this is useful for your agent work.

This payload would go in a comment on issue #161 AFTER PR #211 is acknowledged, or as a GitHub Discussion. NOT in the PR itself.

### 9. Letter text needs update

Current: "You may see some PRs from energyscholar on your geo-agent and mcp-data-server repos"
Should be: "You may see some PRs from energyscholar on your geo-agent repo"

### 10. CI coverage report will be posted automatically

The CI workflow posts a vitest coverage report comment. For PR 3, this will show increased coverage (3 new tests in dataset-catalog, which is at 89%). For PR 1 and 2, coverage won't change (browser-bound modules at 0%). This is fine — it looks good that we added tests where tests exist.

---

## D. Fix Priority

| # | Issue | Priority | Status |
|---|-------|----------|--------|
| 1 | Commit scope conventions (PR 1, 2) | HIGH | DONE — force-pushed |
| 5 | Existing tests leak warnings (PR 3) | HIGH | DONE — spy + assert |
| 2 | "Fixes #177" opener (PR 3) | MEDIUM | DONE — body updated |
| 3 | PR body structure (all) | MEDIUM | DONE — all 3 via API |
| 4 | Commit message verbosity | LOW | DONE — force-pushed |
| 6 | Note addMarkdown fallback | LOW | DEFERRED — out of scope, not a regression |
| 8 | Draft payload | MEDIUM | DONE — 0325-payload-boettiger.md |
| 9 | Update letter | LOW | DONE — "geo-agent repo" |
