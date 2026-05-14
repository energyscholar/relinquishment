---
Plan-UID: 0325-PR
Status: STAGED — 3 draft PRs live, awaiting Bruce review
Parent: 0325 (Boettiger dossier + outreach plan)
Owner: Argus (implement), Bruce (review + submit)
---

# Boettiger PR Staging — Work Log

## Session: S78 (2026-05-12)

### Repos forked to energyscholar
- [x] geo-agent: forked
- [x] mcp-data-server: forked
- Both repos pulled to latest main

### Deep-dive findings

**geo-agent current state (as of 9b67585):**
- 18 JS modules in app/, 8 test files in test/
- vitest test framework, 156+ tests
- CDN-loaded ES modules (no bundler) — external libs via `<script>` tags
- Branch protection on main — all changes via PR
- 12+ downstream deployments pinned to version tags/SHAs
- Boettiger is sole contributor (240 commits, 0 other humans)

**Dossier bugs — triage:**
1. **XSS in addMarkdown (chat-ui.js:693)** — STILL PRESENT. Also line 561 (tool reasoning). Boettiger knows about 561 (review-notes.md item 4), considers "low risk for trusted models." But he deploys to 12+ public instances with configurable models. Line 693 is the bigger vector and NOT mentioned in review notes.
2. **setStyle success masking (map-manager.js:745)** — STILL PRESENT. Issue #161 open since Apr 16.
3. **listTools timeout (main.js)** — FIXED by Boettiger in #209.
4. **parseEmbeddedToolCalls (agent.js:341)** — Present, no test coverage, but low-priority.

**mcp-data-server** — all open issues are research/design/features. No easy bug fixes. Sticking with 3 geo-agent PRs.

### Selected PRs (3)

**PR 1: fix(security): sanitize LLM-rendered HTML with DOMPurify**
- Files: app/chat-ui.js (lines 693, 561)
- Fix: wrap marked.parse() output in DOMPurify.sanitize() with graceful degradation
- Pattern: matches existing typeof-check pattern for marked/hljs
- References: chat-ui-review-notes.md item #4 (extends beyond what it covers)
- Impact: 12+ deployed instances serve external users; any untrusted model or MCP server can inject scripts

**PR 2: fix(set_style): propagate property failure to top-level success (#161)**
- Files: app/map-manager.js (line 745)
- Fix: `success` reflects whether any property update succeeded; add error message when all fail
- References: issue #161 with exact log evidence
- Impact: LLM currently can't detect style failures, moves on without retrying

**PR 3: feat(catalog): warn on asset ID mismatches at startup (#177)**
- Files: app/dataset-catalog.js (extractMapLayers, 2 locations), test/dataset-catalog.test.js
- Fix: add console.warn when configured asset ID not found in STAC collection
- References: issue #177 with 4 acceptance criteria
- Impact: catches config drift at boot, saves field debugging time

### Implementation notes

**PR 1 (DOMPurify):**
```javascript
// Line 693 — addMarkdown:
const rawHtml = typeof marked !== 'undefined' ? marked.parse(md) : md;
el.innerHTML = typeof DOMPurify !== 'undefined' ? DOMPurify.sanitize(rawHtml) : rawHtml;

// Line 561 — tool reasoning:
const rawDesc = typeof marked !== 'undefined' ? marked.parse(desc) : this.escapeHtml(desc);
const descHtml = typeof DOMPurify !== 'undefined' ? DOMPurify.sanitize(rawDesc) : rawDesc;
```
No test needed — chat-ui.js is browser-bound (0% coverage, tested visually).
Update review-notes to mark item 4 resolved.

**PR 2 (setStyle):**
```javascript
const anySucceeded = results.some(r => r.success);
const result = { success: anySucceeded, layer: layerId, displayName: state.displayName, updates: results };
if (!anySucceeded && results.length > 0) {
    result.error = 'All property updates failed — see individual update results for details';
}
return result;
```
No test — map-manager.js is browser-bound (0% coverage).

**PR 3 (asset validation):**
Add console.warn in extractMapLayers() at:
- Standard asset: line 322 `if (!asset) continue;`
- Versioned asset: line 251 `if (!vAsset) continue;`
Add test: spy on console.warn, verify warning for missing assets and no warning for matching configs.

### PRs Created (all DRAFT)

| PR | URL | Title | Status | Tests |
|----|-----|-------|--------|-------|
| #210 | https://github.com/boettiger-lab/geo-agent/pull/210 | fix(chat-ui): sanitize marked output with DOMPurify | Draft | 166 pass |
| #211 | https://github.com/boettiger-lab/geo-agent/pull/211 | fix(map-manager): propagate property failure to top-level success (#161) | Draft | 166 pass |
| #212 | https://github.com/boettiger-lab/geo-agent/pull/212 | feat(catalog): warn on asset ID mismatches at startup (#177) | Draft | 169 pass (3 new) |

### S79 Adversarial Review + Polish (2026-05-12)

**Audit completed:** `0325-pr-audit.md` — 10 issues found, all HIGH/MEDIUM resolved.

**Fixes applied:**
- [x] Commit scopes: `fix(security)` → `fix(chat-ui)`, `fix(set_style)` → `fix(map-manager)` (force-pushed)
- [x] Commit message bodies trimmed to 2-3 lines (force-pushed)
- [x] PR 210: title + body updated via API to match Boettiger's `## Summary` / `## Test plan` format
- [x] PR 211: title + body updated via API
- [x] PR 212: body updated — opens with "Fixes #177.", bold module paths, sections aligned
- [x] Existing tests in PR 3 updated to spy on console.warn (eliminates stderr leak)
- [x] Letter updated: "geo-agent repo" (was "geo-agent and mcp-data-server repos")
- [x] Payload drafted: `0325-payload-boettiger.md` — governance pitch for AFTER PR acknowledgment

### Next steps (gated on Bruce)
1. Bruce reviews PR descriptions, code diffs, and payload draft
2. Decide: keep as drafts until Friday, or mark ready-for-review now?
3. Mail letter Tuesday May 13
4. Convert drafts to ready-for-review ~Friday May 15 to coordinate with letter arrival
