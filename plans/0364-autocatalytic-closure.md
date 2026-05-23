# Plan 0364: Autocatalytic Closure — Group A

**Origin:** S91 Level 3 Diagnostic evaluation (2026-05-21)
**Repo:** ~/software/aurasys-memory
**Prerequisite:** Plan 0363 Phase 1 merged (tag post-0363-merge)
**Architectural context:** See `memory/project-autocatalytic-memory.md`

## Problem

The memory system has confidence decay (Plan 0360 R1) but no reinforcement — all 323 confidence records have `last_reinforced = NULL`. It has a sync pipeline but no automatic trigger — `memory-sync.sh` only runs when a human remembers. The system can forget autonomously but cannot maintain itself autonomously. This is half a cycle.

## Phase 1A: SessionEnd Hook + Quick-Sync Mode

### Changes

**1. `scripts/memory-sync.sh` — add `--quick` flag:**

When called with `--quick`:
- Skip health check (session is ending, not starting)
- Skip `git push` (network may be slow/unavailable at exit; push happens manually or on next session)
- Everything else runs normally: sync files, ingest (if changed), rebuild (if changed), git add + commit
- Add a diff check before ingest: only run ingest+rebuild if files actually changed (compare auto-memory path vs memory-mirror/)
- Exit silently if nothing changed
- Total timeout budget: 15 seconds

Without `--quick`: current behavior unchanged.

**2. `~/.claude/settings.json` — add SessionEnd hook:**

```json
"SessionEnd": [
  {
    "hooks": [
      {
        "type": "command",
        "command": "/home/bruce/software/aurasys-memory/scripts/memory-sync.sh --quick",
        "timeout": 15
      }
    ]
  }
]
```

### Acceptance Criteria

- `memory-sync.sh --quick` completes in <5s when no files changed (diff check short-circuits)
- `memory-sync.sh --quick` completes in <15s when files changed (ingest + rebuild)
- `memory-sync.sh` (no flag) still works as before (health check + push included)
- settings.json is valid JSON after edit
- Hook runs on session exit (verify by checking git log for auto-commit after ending a test session)

### Pros
- Every session auto-syncs at exit — orphan files never accumulate
- Zero risk: runs an existing pipeline with a speed optimization
- Changes committed to git immediately (available to next session)
- If hook fails, no harm — session was ending anyway; next session's exit catches it

### Cons
- Adds ~2-5s to session exit when files changed
- Git commits accumulate (one per session if memories changed) — cosmetic, not structural
- Push deferred to manual — remote may lag behind local

## Phase 1B: Git-Derived Reinforcement

### Changes

**1. `scripts/rebuild-db.sh` — add post-rebuild reinforcement step (Step 7):**

After FTS5 population (Step 4) and before verification (Step 5), iterate over memory-mirror/ files that map to ingested tables. For each file tracked in git, extract last commit date and UPDATE the corresponding confidence record.

```bash
# Step 5 (new): Populate reinforcement from git history
cd "$REPO_DIR"
for f in memory-mirror/feedback-*.md memory-mirror/project-*.md memory-mirror/reference-*.md memory-mirror/user-*.md; do
    [ -f "$f" ] || continue
    git_date=$(git log -1 --format='%Y-%m-%dT%H:%M:%S' -- "$f" 2>/dev/null)
    [ -z "$git_date" ] && continue
    base=$(basename "$f")
    case "$base" in
        feedback-*)  tbl="feedback"; slug="${base#feedback-}"; slug="${slug%.md}" ;;
        project-*)   tbl="projects"; slug="${base#project-}"; slug="${slug%.md}" ;;
        reference-*) tbl="references"; slug="${base#reference-}"; slug="${slug%.md}" ;;
        user-*)      tbl="user_profile"; slug="${base#user-}"; slug="${slug%.md}" ;;
        *) continue ;;
    esac
    sqlite3 "$DB_NEW" "UPDATE memory_confidence SET last_reinforced = '${git_date}' WHERE source_table = '${tbl}' AND source_id = (SELECT id FROM \"${tbl}\" WHERE slug = '${slug}');"
done
```

Note: this runs against `$DB_NEW` (the in-progress rebuild), not `$DB` (production). It's part of the atomic rebuild — if anything fails, the backup restores.

**2. Verification query after rebuild:**

```sql
SELECT source_table, 
    COUNT(*) as total,
    SUM(CASE WHEN last_reinforced IS NOT NULL THEN 1 ELSE 0 END) as reinforced
FROM memory_confidence 
GROUP BY source_table;
```

Tables `feedback`, `projects`, `references`, `user_profile` should show nonzero reinforced counts. Tables `corrections`, `sessions`, `decisions`, `breakthroughs`, `people` will show 0 (hand-maintained SQL, not individual flat files — acceptable).

### Acceptance Criteria

- After rebuild, `SELECT COUNT(*) FROM memory_confidence WHERE last_reinforced IS NOT NULL` > 0
- Specifically: feedback, projects, references, user_profile all have reinforced records
- `v_memories_decayed` shows `effective_confidence` influenced by reinforcement (recently-modified files have higher confidence than stale ones)
- Rebuild still completes in <5s
- `test-schema.sh` still passes 41/41

### Pros
- Confidence decay becomes bidirectional — recently-maintained memories stay relevant
- Durable across rebuilds (recomputed from git history each time)
- No extra state files — git IS the reinforcement ledger
- Preserves flat-files-as-source-of-truth (reads from git, writes nothing upstream)

### Cons
- Only captures file-level maintenance, not conversation-level usage (a memory referenced but not edited doesn't get reinforced)
- Adds ~1-2s to rebuild (100+ git log calls at ~10ms each)
- Untracked/uncommitted files get NULL reinforcement until committed
- Hand-maintained tables (corrections, sessions, people) don't benefit

## Git Workflow

- Branch: `feature/0364-autocatalysis` (from main, post-0363-merge)
- Commit 1: `Plan 0364 Phase 1A: SessionEnd hook + quick-sync mode`
- Commit 2: `Plan 0364 Phase 1B: git-derived reinforcement in rebuild`
- Tag after merge: `post-0364-groupA`

## What This Enables

After Group A, the system automatically:
1. Syncs flat files to memory-mirror/ on session exit
2. Ingests changed files into SQL
3. Rebuilds the DB (with FTS5, confidence, views)
4. Sets reinforcement dates from git history
5. Commits to git

This converts `memory-sync.sh` from a manual step to an automatic one. Combined with confidence decay (Plan 0360), the system now has a complete forget/remember cycle for ingested tables.

## Future Phases (after Plan 0363 Phase 2)

- **Phase 2A:** Cross-reference validation (`rebuild-verify.sh`) — hot five sync, domain distribution, FTS5 completeness
- **Phase 2B:** MEMORY.md auto-generation for sections 3, 5, 6
