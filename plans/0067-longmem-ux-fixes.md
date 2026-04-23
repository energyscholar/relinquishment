# Plan 0067: Longmem UX Fixes — Red-Team Response

**Author:** Argus (Auditor)
**Date:** 2026-03-09
**PTL:** PTL-064
**Status:** COMPLETE (verified S63 audit)
**Repo:** `~/software/longmem/`

---

## Objective

Fix 7 red-team issues in the longmem template repo. Focus: stale data, silent failures, onboarding friction, progressive disclosure. All changes in `~/software/longmem/`.

---

## Phase 1: Fix Stale Data (credibility)

### 1A: `docs/case-study.md`

Update all metrics to current values:

| Old | New |
|-----|-----|
| 33 sessions | 36 sessions |
| 6+ weeks | 16 weeks (112 days) |
| 67 items tracked, 53 plans executed | 49 items tracked (restructured from 67), 65 plans executed |
| 128 commits not mentioned | 128 commits over 112 days |

Also update the line: "The AI — which I named Argus (Claude Opus, Anthropic)" → "The AI — which I named Argus (Claude Opus 4, Anthropic)"

Do NOT change Bruce's voice or the overall structure. Metric updates only.

### 1B: `docs/architecture.md`

Fix wrong session numbers in the "Failure Modes and Recovery" section:

| Current (wrong) | Correct (per evidence file) |
|-----------------|----------------------------|
| Compression catastrophe (S15) | Compression catastrophe (S26) |
| MEMORY.md bloat (S18) | MEMORY.md bloat (S25) |
| Orphan files (S22) | Orphan files (~S26) |
| Pending item zombies (S28) | Pending item zombies (~S27-28) |

Search the entire file for session number references. If any others are wrong, fix them. Cross-reference with `~/software/aurasys-memory/research/longmem-case-study-evidence.md` (Feature Introduction Timeline table and Evidence Source 2 timeline).

---

## Phase 2: Fix Silent Failure (`memory-sync.sh`)

Replace `scripts/memory-sync.sh` with:

```bash
#!/bin/bash
# memory-sync.sh — Commit memory files to git for L3 recovery
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

if [ ! -d .git ]; then
    echo "Error: $REPO is not a git repository. Run 'git init' first."
    exit 1
fi

git add memory/ CLAUDE.md

if git diff --cached --quiet; then
    echo "Memory sync: no changes to commit."
else
    git commit -m "Memory sync: $(date +%Y-%m-%d)"
    echo "Memory synced: $(git log --oneline -1)"
fi
```

**What changed:** Instead of `2>/dev/null || true` (suppresses everything), explicitly check for changes. Report "no changes" or show the commit hash. User always knows what happened.

---

## Phase 3: Progressive Disclosure (the big UX change)

### 3A: Restructure `README.md` Quickstart

Replace the current Quickstart section with a 3-stage progression:

**Stage 1: Start Here (5 minutes)**
1. Clone repo (or "Use this template" on GitHub)
2. Edit `memory/MEMORY.md` — fill in your project name, goal, key people
3. Run `claude` from the project directory
4. That's it. Claude reads MEMORY.md and starts building context.

**Stage 2: After ~5 Sessions**
- Claude will start making mistakes about your project. When it does, say: "Add a correction: [what's wrong] → [what's right]." Claude adds it to `corrections.md` and checks it every session.
- If you're tracking tasks, say "PTL add: [task]." Claude manages `ptl.yaml`.

**Stage 3: After ~10 Sessions**
- MEMORY.md approaches 200 lines. Claude reads `protocol.md` and compresses automatically.
- Session-end sync (`scripts/memory-sync.sh`) creates git snapshots for recovery.
- At this point, all files are active. You didn't have to learn them all on Day 1.

**Keep the existing detailed sections below** (File Structure, How It Works, etc.) but move them under a "## Deep Dive" heading so they don't front-load the quickstart.

### 3B: Restructure `CLAUDE.md` Session Start

Replace the current 6-step session-start protocol with a conditional version:

```markdown
## Session Start Protocol

**Always:**
1. Read MEMORY.md (auto-loaded with this file)
2. Read corrections.md — check every correction

**After 5+ sessions (when files are populated):**
3. Check health metrics in MEMORY.md
4. If MEMORY.md >180 lines: read protocol.md Section 3, compress before proceeding
5. Scan ptl.yaml for ACTIVE and BLOCKED items

**On early sessions (files mostly empty):** Steps 3-5 are no-ops. Just read MEMORY.md and corrections.md, then start working.
```

### 3C: Add note to each optional file

Add a 1-line header comment to these files (after the title):

**`memory/decisions.md`:**
```
> **Optional.** Activate when you need to track structural decisions. Most projects start needing this around session 5-10.
```

**`memory/people.md`:**
```
> **Optional.** Activate when your project involves multiple people whose roles and context matter. Solo projects may never need this file.
```

**`memory/session-details.md`:**
```
> **Optional.** This file fills automatically when MEMORY.md compresses old sessions. You don't need to touch it until compression happens (~session 10+).
```

**`memory/ptl.yaml`:**
```
# Optional. Activate when you have 5+ tasks to track across sessions.
# Say "PTL add: [task]" to start using it.
```

Do NOT add optional markers to MEMORY.md, corrections.md, or protocol.md — those are core.

### 3D: Add "no setup script" defense to README

In the Troubleshooting section or near the Quickstart, add:

```markdown
### Why is there no setup script?

There is no `setup.sh`. That's intentional. The entire setup is: edit one file (`memory/MEMORY.md`), then run `claude`. Zero dependencies, zero installation, zero configuration. If setup takes more than 5 minutes, something is wrong — [open an issue](https://github.com/energyscholar/longmem/issues/new?template=setup_help.md).
```

---

## Phase 4: Protocol Cleanup

### 4A: `memory/protocol.md` — Add early-session acknowledgment

At the top of Section 1 (Session Start Checklist), add:

```markdown
> **Early sessions (1-5):** Most of these steps are no-ops when files are empty. Read MEMORY.md, read corrections.md, start working. The full protocol activates as your project grows.
```

### 4B: `memory/protocol.md` — Self-limiting reminder

Verify protocol.md is under 200 lines after changes. If over, compress Section 6 (PTL Maintenance) by removing redundant explanations.

---

## Acceptance Tests

### Data Accuracy

| # | Test | Pass condition |
|---|------|---------------|
| T1 | Case study metrics updated | 36 sessions, 16 weeks, 49 items, 65 plans, 128 commits |
| T2 | Architecture session numbers fixed | Compression=S26, bloat=S25, no other wrong session refs |
| T3 | No stale "33 sessions" anywhere in repo | `grep -r "33 sessions" ~/software/longmem/` returns nothing |
| T4 | No stale "67 items" or "67 tracked" anywhere | `grep -r "67" ~/software/longmem/` returns nothing (or only in non-metric context) |

### Silent Failure Fix

| # | Test | Pass condition |
|---|------|---------------|
| T5 | memory-sync.sh reports "no changes" on empty diff | Run twice in a row — second run says "no changes to commit" |
| T6 | memory-sync.sh shows commit hash on actual commit | After changing a file, run script — output includes commit hash |
| T7 | memory-sync.sh fails clearly if not a git repo | Run from /tmp — error message mentions "not a git repository" |

### Progressive Disclosure

| # | Test | Pass condition |
|---|------|---------------|
| T8 | README Quickstart is 3 stages | Stage 1 (5 min), Stage 2 (~5 sessions), Stage 3 (~10 sessions) clearly delineated |
| T9 | CLAUDE.md session-start is conditional | "Always" vs "After 5+ sessions" vs "On early sessions" structure present |
| T10 | Optional files marked | decisions.md, people.md, session-details.md, ptl.yaml each have "Optional" marker |
| T11 | Core files NOT marked optional | MEMORY.md, corrections.md, protocol.md have no "Optional" marker |
| T12 | "No setup script" section exists in README | Section present with rationale |

### Protocol

| # | Test | Pass condition |
|---|------|---------------|
| T13 | Early-session note in protocol.md | Top of Section 1 acknowledges sessions 1-5 are mostly no-ops |
| T14 | protocol.md under 200 lines | `wc -l memory/protocol.md` < 200 |

### Integrity

| # | Test | Pass condition |
|---|------|---------------|
| T15 | All internal links resolve | No broken markdown links within the repo |
| T16 | README file tree matches actual files | File tree in README matches `find` output |
| T17 | No Argus-specific content leaked | No "Healer", "TQNN", "Three Possibilities", "Genevieve", "Dignity Net" in any file except docs/case-study.md (which may reference Argus by name) |

---

## Generator Prompt

You are the Generator. Working directory: `~/software/longmem/`

Read the plan at:
`~/software/relinquishment/plans/0067-longmem-ux-fixes.md`

Also read for cross-reference:
`~/software/aurasys-memory/research/longmem-case-study-evidence.md` (correct session numbers and metrics)

Execute Phases 1-4 in order. After all changes, run the acceptance tests (T1-T17) and report results.

One commit per phase:
- Phase 1: "Fix stale metrics in case study and architecture docs"
- Phase 2: "Fix memory-sync.sh silent failure — report actual status"
- Phase 3: "Progressive disclosure: 3-stage onboarding, optional file markers"
- Phase 4: "Protocol cleanup: early-session acknowledgment"

Report completion with summary of changes per phase.
