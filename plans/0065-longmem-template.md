# Plan 0065: Longmem Template Repository

**Status:** COMPLETE (verified S63 audit)
**Owner:** Bruce Stephenson
**PTL:** PTL-064
**Created:** 2026-03-09

---

## Objective

Create `longmem`, an open-source template repository for Claude Code persistent memory. MIT license. Layer 1 only (memory system — no Triad, no Dignity Net, no role separation). The repo IS the product: markdown files + a shell script + documentation.

## Architecture Description

The system uses a three-tier cache model for AI memory persistence:

### L1 — Always In Context (~200 lines)
`MEMORY.md` in the project's `.claude/` directory. Loaded automatically by Claude Code at every conversation start. Contains: project identity, current state summary, hot corrections (top 5), active work summaries, health metrics dashboard. **Hard cap: 200 lines.** Every line costs context tokens.

### L2 — Loaded On Demand
Separate files read when depth is needed:
- `corrections.md` — Things the AI consistently gets wrong. Short imperatives: what not to write, what instead. Hot-five rotate into L1.
- `protocol.md` — Session lifecycle: start checklist, end checklist, compression rules, integrity checks, decay timers. Lazy-loaded (read when triggers fire, not at boot).
- `ptl.yaml` — Prioritized Task List. YAML format. Stable IDs (PTL-NNN), 5 tiers, statuses (READY/ACTIVE/BLOCKED/REVIEW/NEEDS_PLAN/TODO/DONE/DROPPED), decay rules, bandwidth cap.
- `decisions.md` — Structural decisions with rationale. Prevents re-litigating settled questions.
- `session-details.md` — Full session history. Compression target for old ROUTINE sessions.
- `people.md` — Key people in your life, in tiers. Not just collaborators — anyone the AI needs context about: family, colleagues, mentors, friends. Prevents the AI from asking "who's that?" every session.

### L3 — Git Recovery
A session-end shell script commits all memory files to git. Creates versioned snapshots. When context compresses or sessions crash, git history is the backstop.

### Self-Maintenance Protocol
The AI maintains its own memory. At session end:
1. Update current state in MEMORY.md
2. Write session summary (classify PARADIGM or ROUTINE)
3. Compress: if MEMORY.md >180 lines, archive oldest ROUTINE session to session-details.md
4. Integrity checks: broken file refs, correction count matches, L1-L2 sync
5. Health metrics: update dashboard (line count, pending items, oldest unarchived, broken refs)
6. Git sync

### Corrections System (the key innovation)
Each correction is a short imperative preventing a specific recurring error. Example format:
```
## Correction #1: [Short name]
[What the AI gets wrong] → [What to write instead]
Established: [date]. Last violated: [date or "never"].
```
The corrections file functions as a synthetic loss function — locally injected penalties on future generations. Persistent memory + prohibition approximates behavioral fine-tuning without weight changes.

### PTL Schema
```yaml
meta:
  version: 1
  last_modified: "YYYY-MM-DDTHH:MM:SSZ"
  item_count: 0
  tiers:
    1: "Urgent / Close Now"
    2: "Active Projects"
    3: "Queued"
    4: "Infrastructure"
    5: "Someday"
  statuses: [READY, ACTIVE, BLOCKED, REVIEW, NEEDS_PLAN, TODO, DONE, DROPPED]

items: []
```

### CLAUDE.md Directives (generalized)
The CLAUDE.md file contains instructions Claude Code reads at every session:
- Point to memory files and explain their roles
- Define session-start and session-end behaviors
- Set response style preferences
- Define PTL commands ("PTL" = show list, "PTL add: ..." = add item)
- Set the 200-line cap on MEMORY.md
- Instruct the AI to read corrections.md at session start
- Instruct the AI to run memory-sync.sh at session end

### memory-sync.sh
```bash
#!/bin/bash
# memory-sync.sh — Commit memory files to git for L3 recovery
set -e
REPO="$(dirname "$(dirname "$(realpath "$0")")")"
cd "$REPO"
git add memory/ CLAUDE.md
git commit -m "Memory sync: $(date +%Y-%m-%d)" 2>/dev/null || true
echo "Memory synced."
```
Note: The template version is simpler than the original (which mirrors between two directories). Template users keep memory files directly in their project repo.

---

## OPSEC Deny List

Generator MUST NOT include any of the following in template files:
- Any reference to Bruce, Healer, Argus, Genevieve, Robin, or any real person
- Any reference to TQNN, quantum computing, relinquishment, the book, or its content
- Any reference to Dignity Net, Storm Protocol, or governance layers
- Any reference to Triad, Auditor, Generator, or role separation
- Any reference to specific corrections content (use generic examples only)
- Any reference to aurasys-memory, relinquishment, abcre-paper, or other Bruce repos
- No email addresses, GitHub handles, or personal identifiers in template files
- The case study (docs/case-study.md) IS allowed to mention Bruce by name — it's a public document

---

## File Structure

```
longmem/
├── README.md                    # Quickstart, what/why, architecture overview
├── CLAUDE.md                    # Drop-in Claude Code directives (generalized)
├── memory/
│   ├── MEMORY.md                # Template with annotations explaining each section
│   ├── protocol.md              # Session lifecycle rules (generalized)
│   ├── corrections.md           # Empty starter with format spec + 2 generic examples
│   ├── ptl.yaml                 # Empty PTL with schema
│   ├── decisions.md             # Empty with format spec
│   ├── people.md                # Key contacts in tiers (optional but included)
│   └── session-details.md       # Empty with format spec
├── scripts/
│   └── memory-sync.sh           # Git sync for L3 recovery
├── docs/
│   ├── architecture.md          # Three-tier cache model explained in depth
│   └── case-study.md            # "33 Sessions, 22 Corrections, Zero Context Losses"
├── LICENSE                      # MIT
└── .gitignore                   # Minimal: only OS/editor junk. .md files ARE the product.
```

**CRITICAL:** No project planning files, no TODO files, no research files in this repo. The repo contains ONLY the template and its documentation. Keep it clean.

---

## .gitignore Rules

This repo is different from typical repos — markdown IS the product. The .gitignore must be minimal:
```
# OS
.DS_Store
Thumbs.db

# Editors
*.swp
*.swo
*~
.vscode/
.idea/

# Do NOT ignore .md files — they are the product
```

---

## Case Study Content

The case study for docs/case-study.md is provided below. Generator should use this text verbatim (it has been OPSEC-reviewed for public consumption). Only change: update contact email to energyscholar+consulting@gmail.com.

BEGIN CASE STUDY ---

# Persistent Memory for Claude Code: 33 Sessions, 22 Corrections, Zero Context Losses

*Bruce Stephenson — March 2026*

## The Problem

Claude Code is stateless. Every session starts from zero. For a weekend script, that's fine. For a six-week project — 33 sessions, hundreds of decisions, three collaborators, a 224-page manuscript — it's not workable. By session 10, I was spending roughly 30% of each session re-explaining context the AI had known yesterday. Corrections I'd made on Tuesday would need making again on Wednesday. Decisions we'd agreed on would resurface as open questions.

Claude Code ships with auto-memory (a model-managed `MEMORY.md`) and project instructions (`CLAUDE.md`). These get you maybe 20% of the way. There's no structure, no error tracking, no task continuity, no recovery mechanism, and no way to enforce that the AI follows its own previous conclusions.

At $200/month for Claude Pro Max, wasted context is wasted money.

## What I Built

A structured memory system that lives in the filesystem and loads automatically. No plugins, no dependencies, no infrastructure. Just files.

The key insight is a **three-tier cache model**:

- **L1** (`MEMORY.md`): Always in context. Capped at 200 lines. Contains identity, current state, the five most critical corrections, active session summaries, and a health metrics dashboard. This is the context window budget — every line costs tokens.
- **L2** (`corrections.md`, `people.md`, etc.): Loaded on demand. Full reference material the AI reads when it needs depth.
- **L3** (git history): Recovery. A session-end sync script commits everything to git, creating versioned snapshots. When context compresses or sessions crash, L3 is the backstop.

The system maintains itself. At session end, the AI updates current state, writes a session summary, compresses older sessions to stay under the line cap, runs integrity checks, and commits to git.

## The Corrections System

This is the most valuable component and the one I didn't expect.

I maintain a list of 22 corrections — things the AI consistently gets wrong about my project. Each correction is a short imperative: what not to write, what to write instead. The five most-violated rotate into L1, where they're visible at the start of every session.

Before the corrections system, I fixed the same mistakes every session. After: repeat violations dropped to near zero. Not because the model changed — because its environment did.

When I fed the AI's output to ChatGPT for independent analysis, it identified the corrections system without being told about it. Its description: **"The corrections file is a synthetic loss function."** Each entry acts as a locally injected penalty on future generations. Persistent memory plus prohibition approximates fine-tuning — behaviorally, not architecturally.

## What Broke

The system wasn't designed top-down. It evolved from failures.

**The compression catastrophe.** When I migrated from a flat TODO file to the structured system, roughly half of my highest-priority items were dropped. Recovery required reconstructing items from session history.

**MEMORY.md bloat.** Hit 233 lines before I formalized the 200-line cap. The cap forced discipline: what actually needs to be in L1 vs. what can live in L2?

**Orphan files.** Research documents accumulated without being tracked in the file map. Added orphan detection to integrity checks.

**Pending item zombies.** Tasks older than eight weeks with no plan assigned would sit indefinitely. Added the STALLED status and automatic decay rules.

Every protocol rule traces back to a specific failure. That's scar tissue, not theory.

## Results

Over 33 sessions across 6+ weeks:

| Metric | Before | After |
|--------|--------|-------|
| Context re-explanation | ~30% of session | <5% |
| Repeat correction violations | Every session | Near zero |
| Decision tracking | None | All logged with rationale |
| Task continuity | None | 67 items tracked, 53 plans executed |
| Catastrophic context losses | Regular | Zero (after system established) |

## Try It

The system requires no special tools — markdown files, a YAML file, a shell script, and instructions in your `CLAUDE.md`. Clone the **longmem** template repository, customize `MEMORY.md` for your project, and start working. The value is obvious within 2-3 sessions.

For teams adopting AI-assisted development workflows, I consult on structured memory systems and longitudinal AI collaboration: energyscholar+consulting@gmail.com

**Bruce Stephenson** — 51 years CLI experience (DEC-10, 1975). Reed College physics.

--- END CASE STUDY

---

## Generator (Single Prompt)

**Creates ALL files in one pass.** Repo exists at `~/software/longmem/` with prior content that must be replaced.

**FIRST:** Delete stale files from prior attempt:
```bash
cd ~/software/longmem
rm -f docs/dignity-net.md docs/triad-protocol.md docs/memory-system.md
rm -rf docs/examples/
```
Then create all files below.

**Files to create (in this order — hardest first):**

1. **CLAUDE.md** (~80-120 lines) — Generalized Claude Code directives. Reference all memory/ files by path. Define session-start/end behaviors, PTL commands, 200-line cap, corrections loading, memory-sync at session end. Response style preferences. Reference people.md (included as teaching example of tiered contact management).

2. **memory/protocol.md** (~100-150 lines) — Session lifecycle rules: start checklist (read MEMORY.md, check health metrics, read corrections), end checklist (update state, write summary, compress if >180 lines, integrity checks, git sync), compression rules, decay timers (STALE >3wk, archive >6wk, STALLED >8wk with no plan), integrity checks (broken refs, correction count, L1-L2 sync).

3. **README.md** (~200-300 lines) — Title, one-sentence description, "What is this?", quickstart (5 minutes to first session — explain that CLAUDE.md at repo root is auto-loaded by Claude Code, and memory/ files are referenced from it), file structure diagram, "How it works" (brief), "What's included", link to docs/architecture.md, link to docs/case-study.md, "Contributing" (short), MIT license badge, contact: energyscholar+consulting@gmail.com.

4. **docs/architecture.md** (~150-200 lines) — Full explanation of L1/L2/L3 model, corrections system, PTL, self-maintenance protocol, health metrics. Technical audience. No fluff.

5. **memory/MEMORY.md** (~60-80 lines) — Template with `[YOUR PROJECT]` placeholders and inline annotations explaining each section. Sections: Identity, Current State, L1 Corrections (hot five), Active Work, File Map, Health Metrics.

6. **memory/corrections.md** (~30 lines) — Format spec + 2 GENERIC example corrections (e.g., "Don't assume the user wants verbose output → Ask before generating long responses").

7. **memory/ptl.yaml** (~20 lines) — Schema from Architecture Description above, 0 items.

8. **memory/decisions.md** (~20 lines) — Format spec: date, decision, rationale, status. No content.

9. **memory/people.md** (~30 lines) — Format spec with 3 tiers (Active / Peripheral / Historical) + 1-2 GENERIC placeholder entries showing the format (e.g., "[Name] — [Relationship]. [Context note]."). Not just project collaborators — anyone the AI needs to know about: family, mentors, colleagues, friends. Prevents "who's that?" every session.

10. **memory/session-details.md** (~20 lines) — Format spec: session number, date, classification (PARADIGM/ROUTINE), summary. No content.

11. **docs/case-study.md** — Copy the case study text from "BEGIN CASE STUDY" to "END CASE STUDY" in this plan file VERBATIM. Only change: ensure contact email reads energyscholar+consulting@gmail.com.

12. **scripts/memory-sync.sh** — Per the script in Architecture Description. Run `chmod +x` after writing.

13. **LICENSE** — MIT license, copyright "longmem contributors", year 2026.

14. **.gitignore** — Per .gitignore Rules section above. Minimal: OS/editor junk only. Do NOT ignore .md files.

**After all files written:** Single commit with message `Plan 0065: longmem template repository`

---

## Acceptance Criteria

1. `ls longmem/` shows exactly the file structure defined above
2. No file contains any item from the OPSEC Deny List
3. CLAUDE.md references all memory/ files by path
4. memory/MEMORY.md has `[YOUR PROJECT]` placeholders, not real project content
5. memory/corrections.md has generic examples only
6. memory/ptl.yaml parses as valid YAML with 0 items
7. scripts/memory-sync.sh is executable
8. README.md has a quickstart section that gets a user working in <5 minutes
9. docs/case-study.md matches the provided text (with email update)
10. .gitignore does NOT exclude .md files
11. No Triad, Dignity Net, role separation, or governance content anywhere
12. MIT LICENSE file present
