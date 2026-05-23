# Plan 0363: Memory System L3 Diagnostic Repairs

**Origin:** S91 Level 3 Diagnostic (2026-05-21)
**Repo:** ~/software/aurasys-memory
**Prerequisite:** DB rebuilt from scripts (done during diagnostic)

## Context

S91 ran the first Level 3 Diagnostic on the memory system (post-Plan 0308 base + Plan 0360 R1 confidence decay). Found 2 critical, 3 significant, 1 minor issues. Confidence decay math, FTS5, and rebuild pipeline all verified correct. The flat-file-as-source-of-truth architecture was validated when test-schema.sh zeroed the DB and rebuild restored everything.

## Phase 1: Critical Fixes

### 1A. test-schema.sh must not touch production DB

**Problem:** Steps 9-10 (lines 339-378) operate on `${REPO_DIR}/argus.db` instead of `$TEST_DB`. Line 339 deletes argus.db for health-check testing. Line 378 deletes it again as "cleanup." Running the test suite destroys the production DB.

**Fix:** Create a temp directory for steps 9-10. Set `TEST_REPO` to a tmpdir, copy scripts/ into it, then run health-check.sh and rebuild-db.sh against that isolated directory. Remove `rm -f "${REPO_DIR}/argus.db"` from line 378 entirely.

**Acceptance criteria:**
- `test-schema.sh` passes 41/41
- After running test-schema.sh, `argus.db` is unchanged (compare sha256 before/after)
- No reference to `${REPO_DIR}/argus.db` in steps 9-10 (grep verification)

### 1B. Fix v_hot_corrections to match protocol.md

**Problem:** View has `WHERE number IN (12, 20, 23, 6, 11)`. Protocol.md and MEMORY.md both say current hot five is {3, 8, 11, 12, 20}.

**Fix:** In `scripts/db-setup/020-views.sql`, change the WHERE clause:
```sql
CREATE VIEW v_hot_corrections AS
SELECT * FROM corrections WHERE number IN (3, 8, 11, 12, 20)
ORDER BY number;
```

**Acceptance criteria:**
- `SELECT number FROM v_hot_corrections ORDER BY number` returns 3, 8, 11, 12, 20
- Matches MEMORY.md §2 and protocol.md §7 "Current hot five"

### 1C. Rebuild DB after fixes

After 1A and 1B, run `scripts/rebuild-db.sh`. Verify with `scripts/test-schema.sh` (which should now be safe). Confirm argus.db survives the test run.

**Acceptance criteria:**
- `rebuild-db.sh` completes cleanly
- `test-schema.sh` passes AND argus.db sha256 unchanged after test

## Phase 2: Significant Fixes

### 2A. Sync 27 orphan flat files

**Problem:** 27 new .md files in `~/software/aurasys-memory/memory/` (repo dir) are not in the auto-memory path (`~/.claude/projects/-home-bruce-software-aurasys-memory/memory/`) or `memory-mirror/`. They were written to the repo dir by Claude sessions but never synced.

**Fix:**
1. Copy each orphan file from repo `memory/` to the auto-memory path
2. Run `scripts/memory-sync.sh` to propagate to memory-mirror/ and re-ingest
3. Verify new files appear in the DB

**Files to sync** (feedback: 27, project: 14, reference: 8, user: 5):
- All `memory/feedback-*.md` not in memory-mirror/
- All `memory/project-*.md` not in memory-mirror/  
- All `memory/reference-*.md` not in memory-mirror/
- All `memory/user-*.md` not in memory-mirror/
- Also: `memory/concept-stash.md`, `memory/skill-prospect.md`, `memory/people-levin-dossier.md`

**Acceptance criteria:**
- `diff <(ls memory-mirror/feedback-*.md | wc -l) <(echo "increased")`
- `SELECT COUNT(*) FROM feedback` is higher than 83
- FTS5 indexes the new content

### 2B. Add domain tags to feedback flat files

**Problem:** All 83+ feedback entries have `domain='general'` because no flat file includes a `domain:` frontmatter field. Domain-based filtering is dead.

**Fix:** Add `domain:` tag to each feedback .md file in the auto-memory path. Assignment guide:
- `book` — anything about manuscript, reading levels, chapters, pedagogy, rich panels, build pipeline
- `science` — magnetogenesis, IMAGE, SECS, variograms, data analysis, MS methods
- `traveller` — RPG, campaign, NPC, Traveller extraction
- `se` — triad, plans, git workflow, architecture, testing, generator prompts, build systems
- `memory` — protocol, health, ingest, corrections, memory architecture
- `general` — cross-domain, DN, personal, outreach, security, feedback that doesn't fit one domain

Re-ingest and rebuild after tagging.

**Acceptance criteria:**
- `SELECT domain, COUNT(*) FROM feedback GROUP BY domain` shows at least 4 non-empty domains
- No domain has more than 50% of all feedback entries
- `v_feedback_by_domain WHERE domain='book'` returns results

### 2C. Preserve temporal metadata through rebuild

**Problem:** `INSERT OR REPLACE` in generated SQL uses `DEFAULT datetime('now')` for `created_at` and `updated_at`, so every rebuild resets all timestamps. `v_stale_projects` is permanently empty.

**Fix:** Add `established:` field to flat file frontmatter (date of creation). Parse in `ingest-memories.sh` and include as explicit `created_at` in generated SQL. For `updated_at`, use file mtime or git log date.

Changes to ingest-memories.sh:
- Extract `established:` from frontmatter
- Extract mtime via `stat -c %Y` or `git log -1 --format=%ai`
- Include explicit `created_at` and `updated_at` in INSERT statements

**Acceptance criteria:**
- After rebuild, `SELECT slug, created_at FROM projects ORDER BY created_at LIMIT 5` shows dates before today
- `v_stale_projects` returns rows for projects not touched in >21 days
- New files without `established:` still get reasonable defaults

## Git Workflow

- Tag before work: `git tag pre-0363`
- Branch: `feature/0363-l3-repairs`
- Phase 1 commit: `Plan 0363 Phase 1: critical test/view fixes`
- Phase 2 commits: one per sub-phase (2A, 2B, 2C)
- Merge to main after all phases verified

## Risk Notes

- Phase 1 is low-risk: test isolation and a SQL constant change
- Phase 2A (sync) is medium: need to verify no content conflicts between repo memory/ and auto-memory path
- Phase 2B (domain tags) is medium: requires judgment on ~80+ files, could misclassify
- Phase 2C (timestamps) is highest-risk: changes the ingest pipeline. Test with a single file before bulk run
