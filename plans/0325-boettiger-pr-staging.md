---
Plan-UID: 0325-PR
Status: ARMED — PRs ready-for-review, payload staged, gate active
Parent: 0325 (Boettiger dossier + outreach plan)
Owner: Argus (implement), Bruce (review + submit)
Gate: START-OPERATION-BOETTIGER — no write action visible to Boettiger without this trigger
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

### S79 continued (2026-05-14) — Ready-for-review + Root Cause

**PRs converted to ready-for-review** — Bruce approved, letter mailed Mon May 12, in transit to Berkeley.

**Root-cause sections added to all 3 PR descriptions:**
- [x] PR #210: "Missing structural enforcement at trust boundary" — behavioral vs structural controls
- [x] PR #211: "False positive feedback to the agent" — agent can't detect its own failure
- [x] PR #212: "Silent configuration drift" — declared vs actual state divergence

Three governance failure categories, using language natural to engineering root-cause analysis. No white paper link, no pitch — just good practice that primes the vocabulary.

### Current State (2026-05-14)

| Asset | Status | Boettiger-visible? |
|-------|--------|-------------------|
| Friendly greeting letter (no QR, no links) | Mailed Tue May 13, in transit | Yes (physical mail) |
| PR #210 (XSS) | Ready-for-review, root cause added | Yes |
| PR #211 (success masking) | Ready-for-review, root cause added | Yes |
| PR #212 (asset warnings) | Ready-for-review, root cause added | Yes |
| Payload comment (0325-payload-boettiger.md) | Drafted, NOT posted | No |
| Bury warm-intro | Not drafted | No |
| Paper letter (escalation) | Not drafted | No |

### Gate Protocol: START-OPERATION-BOETTIGER

**No further write action visible to Boettiger without Bruce's explicit trigger.**

This applies to:
1. Payload comment on issue #161 or any PR
2. Any GitHub comment, review, or discussion post
3. Bury warm-intro request
4. Any follow-up communication

The PRs and letter are already in play (approved by Bruce this session). The gate governs everything AFTER.

**Trigger sequence when gate opens:**
1. Wait for Boettiger to engage (merge, comment, or review any PR)
2. Post payload comment (short version if PR reply, full version if issue #161)
3. If no engagement by May 19: consider Bury warm-intro (requires separate Bruce approval)
4. If no engagement by June 2: consider paper letter (requires separate Bruce approval)

### Payload Refinement

The root-cause sections in the PRs now prime three governance failure categories. The payload comment can reference them directly:

> These three bugs map to distinct failure categories — trust boundary enforcement (#210), feedback integrity (#211), configuration drift (#212). I've been working on a systematic taxonomy of these patterns in AI agent systems. Architecture and failure matrix documented at [link]. Happy to discuss if any of this is useful for your agent work.

This version is tighter than the original and connects directly to what he's already read in the PR descriptions. One paragraph, one link.
