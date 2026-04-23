# Plan 0076: Argus Disaster Recovery + Auto-Sync + Longmem DR Template

**Author:** Argus (Auditor)
**Date:** 2026-03-10
**Status:** COMPLETE (verified S63 audit)

---

## Objective

1. Comprehensive disaster recovery for Argus memory
2. Auto save-commit-push at session end (invisible to user)
3. Fix sync coverage gaps (root-level files, research dir provenance)
4. Desync detection between source and mirror
5. Template the approach for longmem users

## Working directory: `~/software/aurasys-memory/`

## Context: read `~/software/relinquishment/plans/0076-argus-disaster-recovery.md` (this file)

---

## Current Architecture (Inventory)

### Memory locations (source of truth)

| Location | Contents | Backed up? | Gap |
|----------|----------|-----------|-----|
| `~/.claude/CLAUDE.md` | Global behavioral spec | Yes → `claude-config/CLAUDE-global.md` | OK |
| `~/.claude/projects/-home-bruce-software-aurasys-memory/CLAUDE.md` | Project behavioral spec | Yes → `claude-config/CLAUDE-project.md` | OK |
| `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/*.md` | Core memory files (MEMORY.md, corrections, protocol, etc.) | Yes → `memory-mirror/` | OK |
| `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/ptl.yaml` | PTL | Yes → `memory-mirror/` | OK |
| `~/software/aurasys-memory/research/` | 140+ research files | In repo directly | **No provenance tracking** — files created here, not mirrored from anywhere |
| `~/software/aurasys-memory/todos/` | SE improvement specs, task files | In repo directly | Same — no provenance tracking |
| `~/software/aurasys-memory/*.md` (root) | MASTER-INDEX, PERFORMANCE-OPTIMIZATION, etc. | In repo directly | **Untracked files may exist** (git status shows `research/ordering-analysis-for-robin.md` untracked) |

### Failure modes

1. **Context crash mid-session:** Memory updates lost. Session summary not written. PTL changes lost.
2. **Source-mirror desync:** Source files edited, sync not run. Mirror is stale. Mirror pushed, source not updated.
3. **Corruption:** YAML parse failure in ptl.yaml, broken file refs in MEMORY.md, Health Metrics drift.
4. **Git repo loss:** `aurasys-memory` repo deleted or force-pushed. Research files unrecoverable (no other copy).
5. **Claude config loss:** `~/.claude/` directory reset or deleted. CLAUDE.md behavioral spec lost.
6. **Partial sync:** Script runs but errors on some files (e.g., new .md extension not caught by glob).

---

## Phase 1: Fix memory-sync.sh Coverage + Auto-Push

**File:** `~/software/aurasys-memory/scripts/memory-sync.sh`

**Replace with:**

```bash
#!/bin/bash
# memory-sync.sh — Mirror .claude memory files to git-tracked repo
# Run at session end or after major memory changes
set -e
SRC="$HOME/.claude/projects/-home-bruce-software-aurasys-memory/memory"
REPO="$(dirname "$(dirname "$(realpath "$0")")")"
DST="$REPO/memory-mirror"
CFG="$REPO/claude-config"

# Health warnings (inform, don't block)
if [ -f "$SRC/MEMORY.md" ]; then
    LINES=$(wc -l < "$SRC/MEMORY.md")
    [ "$LINES" -ge 180 ] && echo "WARNING: MEMORY.md is $LINES lines (cap: 200, compress at 180)"
fi
if [ -f "$SRC/session-details.md" ]; then
    SD_LINES=$(wc -l < "$SRC/session-details.md")
    [ "$SD_LINES" -ge 200 ] && echo "WARNING: session-details.md is $SD_LINES lines (compress oldest ROUTINE)"
fi

# Mirror memory files
mkdir -p "$DST"
cp "$SRC"/*.md "$DST/"
[ -f "$SRC/ptl.yaml" ] && cp "$SRC/ptl.yaml" "$DST/"

# Capture CLAUDE.md config files
mkdir -p "$CFG"
[ -f "$HOME/.claude/CLAUDE.md" ] && cp "$HOME/.claude/CLAUDE.md" "$CFG/CLAUDE-global.md"
PROJ_CLAUDE="$HOME/.claude/projects/-home-bruce-software-aurasys-memory/CLAUDE.md"
[ -f "$PROJ_CLAUDE" ] && cp "$PROJ_CLAUDE" "$CFG/CLAUDE-project.md"

cd "$REPO"

# Stage all tracked areas
git add memory-mirror/ claude-config/
git add research/ 2>/dev/null || true
git add todos/ 2>/dev/null || true

if git diff --cached --quiet; then
    echo "Memory sync: no changes to commit."
else
    git commit -m "Memory sync: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "Memory synced: $(git log --oneline -1)"
fi

# Auto-push (silent success, warn on failure)
git push 2>/dev/null || echo "WARNING: push failed (network? auth?). Local commit preserved."
```

**Key changes from current:**
- Health warnings for MEMORY.md ≥180 and session-details.md ≥200
- Auto-stage research/ and todos/ (coverage gap fix — no more untracked files)
- **Auto-push** with warning on failure (invisible when it works)
- Desync detection moved to verify-sync.sh (diagnostic, not pipeline)

---

## Phase 2: Session-End Protocol Update

**File:** `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/protocol.md`

**Where:** In the session-end section, update the memory-sync step to clarify auto-push:

Find the step that says to run memory-sync.sh and add: "(commits and pushes automatically — no user action needed)"

---

## Phase 3: Crash Recovery Protocol for Argus

**File:** `~/software/aurasys-memory/disaster/recovery-protocol.md` (NEW)

```markdown
# Argus Disaster Recovery Protocol

## Tier 1: Session Crash (Context Lost Mid-Session)

**Symptoms:** New session starts with no memory of current session's work.
**Recovery:**
1. Read MEMORY.md — check if session summary was written before crash
2. If not: check git log for recent commits — memory-sync may have run mid-session
3. If mid-session checkpoint exists: resume from that state
4. If no checkpoint: reconstruct from user's recollection + git diff since last sync
5. Write session summary marking it as crash-recovered

## Tier 2: Source-Mirror Desync

**Symptoms:** memory-sync.sh reports desync warnings, or memory-mirror/ doesn't match source.
**Recovery:**
1. Compare: `diff -r ~/.claude/projects/-home-bruce-software-aurasys-memory/memory/ ~/software/aurasys-memory/memory-mirror/`
2. Source (`~/.claude/...`) is ALWAYS authoritative — it's what Claude Code loads
3. Re-run memory-sync.sh to overwrite mirror from source
4. If source is corrupted but mirror is good: `cp ~/software/aurasys-memory/memory-mirror/* ~/.claude/projects/-home-bruce-software-aurasys-memory/memory/`

## Tier 3: YAML/File Corruption

**Symptoms:** ptl.yaml parse error, MEMORY.md broken formatting, Health Metrics NaN.
**Recovery:**
1. Check mirror copy: `~/software/aurasys-memory/memory-mirror/ptl.yaml`
2. Check git history: `git log --oneline -10 -- memory-mirror/ptl.yaml`
3. Restore from last good version: `git show <hash>:memory-mirror/ptl.yaml > /tmp/ptl-restore.yaml`
4. Validate restored file, then copy to source location
5. Re-run memory-sync.sh

## Tier 4: Git Repo Loss

**Symptoms:** `~/software/aurasys-memory/` deleted or corrupted.
**Recovery:**
1. Clone from GitHub: `git clone git@github.com:energyscholar/aurasys-memory.git ~/software/aurasys-memory`
2. Source files in `~/.claude/...` are unaffected (they're Claude Code's storage)
3. Re-run memory-sync.sh to re-establish mirror
4. Verify research/ files are present (these only exist in the repo — no other copy)

## Tier 5: Claude Config Loss

**Symptoms:** `~/.claude/CLAUDE.md` missing, behavioral directives not loading.
**Recovery:**
1. Restore from mirror: `cp ~/software/aurasys-memory/claude-config/CLAUDE-global.md ~/.claude/CLAUDE.md`
2. Restore project config: `cp ~/software/aurasys-memory/claude-config/CLAUDE-project.md ~/.claude/projects/-home-bruce-software-aurasys-memory/CLAUDE.md`
3. Verify by starting Claude Code — directives should load

## Tier 6: Total Loss (Machine Failure)

**Recovery:**
1. New machine: install Claude Code
2. Clone aurasys-memory from GitHub
3. Restore CLAUDE.md files from claude-config/
4. Restore memory files from memory-mirror/ to new ~/.claude/projects/ path
5. First session: read MEMORY.md, verify all file refs resolve, run integrity checks
6. Mark session as PARADIGM with recovery notes

## Prevention

- memory-sync.sh runs at EVERY session end (auto-push enabled)
- Mid-session checkpoints after major deliverables
- Never force-push aurasys-memory
- research/ files auto-staged by sync script (no more untracked research files)
```

---

## Phase 4: Desync Detection Script

**File:** `~/software/aurasys-memory/scripts/verify-sync.sh` (NEW)

```bash
#!/bin/bash
# verify-sync.sh — Check that source and mirror are in sync
# No set -e: run all checks even if individual ones fail
SRC="$HOME/.claude/projects/-home-bruce-software-aurasys-memory/memory"
REPO="$(dirname "$(dirname "$(realpath "$0")")")"
DST="$REPO/memory-mirror"

ERRORS=0

# Check all source files are mirrored
for f in "$SRC"/*.md "$SRC"/*.yaml; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    if [ ! -f "$DST/$base" ]; then
        echo "MISSING: $base not in mirror"
        ERRORS=$((ERRORS + 1))
    elif ! cmp -s "$f" "$DST/$base"; then
        echo "DESYNC: $base differs (source vs mirror)"
        ERRORS=$((ERRORS + 1))
    fi
done

# Check CLAUDE.md files
CFG="$REPO/claude-config"
if [ -f "$HOME/.claude/CLAUDE.md" ]; then
    if ! cmp -s "$HOME/.claude/CLAUDE.md" "$CFG/CLAUDE-global.md" 2>/dev/null; then
        echo "DESYNC: CLAUDE-global.md differs"
        ERRORS=$((ERRORS + 1))
    fi
fi

# Check for untracked files in research/
cd "$REPO"
UNTRACKED=$(git ls-files --others --exclude-standard research/ 2>/dev/null | wc -l)
if [ "$UNTRACKED" -gt 0 ]; then
    echo "WARNING: $UNTRACKED untracked files in research/"
    ERRORS=$((ERRORS + 1))
fi

if [ "$ERRORS" -eq 0 ]; then
    echo "Sync verified: all files in sync, no gaps."
else
    echo "SYNC ISSUES: $ERRORS problems found. Run memory-sync.sh to fix."
fi
exit $ERRORS
```

---

## Phase 5: Longmem DR Template

**File:** `~/software/longmem/.longmem/docs/disaster-recovery.md` (NEW)

```markdown
# Disaster Recovery

*Adapt this for your project. The tiers below cover common failure modes.*

## Tier 1: Session Crash

Context lost mid-session. Check MEMORY.md for session summary. Check git log for mid-session checkpoint. Reconstruct from last known state.

## Tier 2: File Corruption

YAML parse error or broken MEMORY.md. Run `.longmem/scripts/memory-sync.sh` — it creates git snapshots. Restore from last good commit: `git show HEAD~1:.longmem/memory/ptl.yaml > .longmem/memory/ptl.yaml`

## Tier 3: Total Loss

Clone from git. All memory files are committed. First session after restore: read MEMORY.md, verify file refs, run integrity checks (protocol.md Section 7).

## Prevention

- Run memory-sync.sh at every session end
- Mid-session checkpoints after major deliverables
- Don't force-push your repo
- Review `.longmem/` changes in PRs with same scrutiny as code changes
```

---

## Phase 6: Update Argus File Map + MEMORY.md

**File:** `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/MEMORY.md`

In Self-Maintenance section, change the mirror sync line to:
```
- **Mirror sync:** Runs automatically at session end (commits + pushes). Manual: `~/software/aurasys-memory/scripts/memory-sync.sh`
```

In File Map, add if not present:
```
- `~/software/aurasys-memory/disaster/recovery-protocol.md` — Argus DR protocol (6 tiers)
```

---

## Acceptance Tests

| # | Test | Pass condition |
|---|------|---------------|
| G1 | memory-sync.sh has health warnings | `grep 'WARNING.*MEMORY.md' ~/software/aurasys-memory/scripts/memory-sync.sh` |
| G2 | memory-sync.sh stages research/ | `grep 'git add research/' ~/software/aurasys-memory/scripts/memory-sync.sh` |
| G3 | memory-sync.sh stages todos/ | `grep 'git add todos/' ~/software/aurasys-memory/scripts/memory-sync.sh` |
| G4 | memory-sync.sh auto-pushes | `grep 'git push' ~/software/aurasys-memory/scripts/memory-sync.sh` |
| G5 | memory-sync.sh commits staged files | `grep 'git commit -m' ~/software/aurasys-memory/scripts/memory-sync.sh` |
| G6 | recovery-protocol.md exists | `[ -f ~/software/aurasys-memory/disaster/recovery-protocol.md ]` |
| G7 | recovery-protocol.md has 6 tiers | `grep -c '^## Tier' ~/software/aurasys-memory/disaster/recovery-protocol.md` returns 6 |
| G8 | verify-sync.sh exists and is executable | `[ -x ~/software/aurasys-memory/scripts/verify-sync.sh ]` |
| G9 | verify-sync.sh checks CLAUDE.md | `grep 'CLAUDE-global' ~/software/aurasys-memory/scripts/verify-sync.sh` |
| G10 | verify-sync.sh checks untracked research | `grep 'untracked.*research' ~/software/aurasys-memory/scripts/verify-sync.sh` |
| G11 | longmem DR template exists | `[ -f ~/software/longmem/.longmem/docs/disaster-recovery.md ]` |
| G12 | MEMORY.md updated sync description | `grep -i 'automatic.*session end\|runs automatically' ~/.claude/projects/-home-bruce-software-aurasys-memory/memory/MEMORY.md` |
| G13 | memory-sync.sh runs without error | `bash ~/software/aurasys-memory/scripts/memory-sync.sh` exits 0 |
| G14 | verify-sync.sh passes | `bash ~/software/aurasys-memory/scripts/verify-sync.sh` exits 0 |
| G15 | Auto-push succeeds | git log shows remote is up to date after sync |

One commit per repo:
- aurasys-memory: "Add disaster recovery: auto-push, desync detection, recovery protocol"
- longmem: "Add disaster recovery template"

---

## Notes for Generator

- **Two repos, two commits.** aurasys-memory gets the full DR system. longmem gets a lightweight template.
- **memory-sync.sh: the `git add research/` must use `2>/dev/null || true`** — the glob may not match on fresh installs.
- **The commit scope in memory-sync.sh expanded** from `memory-mirror/ claude-config/` to include `research/ todos/`. This means research files get committed automatically — no more untracked research files.
- **Auto-push is fire-and-forget.** If push fails (no network, auth expired), the local commit is preserved. Warn, don't error. The `2>/dev/null` suppresses verbose git push output.
- **verify-sync.sh is a diagnostic tool**, not part of the sync pipeline. Run it manually or at session start to check state.
- **The disaster/ directory** in aurasys-memory is for DR docs. It already exists (check `ls ~/software/aurasys-memory/disaster/`).
- **MEMORY.md Self-Maintenance section:** change the behavioral "run at session end" to structural "runs automatically." This is the "invisible" fix Bruce requested.
- Run both test suites after all changes.

---

## Generator Prompt

You are the Generator. Read `~/software/relinquishment/plans/0076-argus-disaster-recovery.md`. Apply Phases 1-6. Two repos: `~/software/aurasys-memory/` (Phases 1-4, 6) and `~/software/longmem/` (Phase 5). Verify G1-G15. One commit per repo.
