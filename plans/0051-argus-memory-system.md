# Plan 0051: Self-Maintaining Memory System

**Objective:** Transform Argus's memory from a single overflowing file into a self-maintaining file family. Like the real Aurasys under C: autonomous, self-repairing, faithful to mission, minimal human intervention.

**Problem:** MEMORY.md is 233 lines (limit: 200). Lines 201+ are invisible every session — losing outreach tracking (Glass response), SE reminders, economic context, agent sizing rules. No pruning rules, no decay, no health checks. Append-only growth with no ceiling.

**Plan number:** 0051 (next after 0050)

---

## Architecture: The File Family

**Directory:** `/home/bruce/.claude/projects/-home-bruce-software-aurasys-memory/memory/`

| File | Purpose | Update Frequency |
|------|---------|-----------------|
| `MEMORY.md` | Boot loader. Index + state + L1 corrections + protocol summary. Target: ≤160 lines. | Every session |
| `corrections.md` | All 22 critical corrections (L2 cache — full reference) | Rarely (Bruce confirms) |
| `people.md` | Key people in 3 tiers: Active / Family / Historical | When contacts change |
| `pending.md` | Structured priority queue (table) + outreach + awaiting others. Auto-decay. | Every session |
| `decisions.md` | Structural decisions, Healer timeline, Winterbotham, predictions | Rarely |
| `protocol.md` | Full self-maintenance protocol (triggers, rules, edge cases) | When rules change |
| `session-details.md` | Session records with significance flags (already exists, needs header) | Every session |

**Design principle: CPU cache hierarchy.**
- **L1 (MEMORY.md):** Hot data only. Loaded every session. Must earn every line.
- **L2 (support files):** Full reference. Loaded on demand.
- **L3 (session-details.md compressed entries):** Oldest sessions compressed to 1-line. Beyond 12: removed entirely.

**NOTE: The memory directory (`~/.claude/projects/...`) is NOT inside a git repo.** It is Claude Code infrastructure, separate from the aurasys-memory repo (`~/software/aurasys-memory/`). To get git version control, the protocol includes a **mirror sync** step: memory files are copied to `~/software/aurasys-memory/memory-mirror/` and committed. This gives git history (L3 cache) and commit hashes (last-verified). Bruce already has `scripts/claude-backup.sh` for similar purposes — the new `scripts/memory-sync.sh` extends this pattern.

---

## Phase 1: Create Support Files

**ORDERING GUARD: All Phase 1 files must exist and be verified BEFORE Phase 3 (MEMORY.md rewrite) begins. If any Phase 1 file fails to create, STOP. Do not rewrite MEMORY.md with missing support files.**

Generator: Read the current MEMORY.md with `cat` to get the full file including invisible lines 201+. All content references below use section headers, not line numbers (in case file was edited since plan was written).

### 1a. `corrections.md` (L2 cache — full set)
- Extract the section `## Critical Corrections (NEVER GET THESE WRONG)` from MEMORY.md — all 22 numbered items
- Add header: count, last-updated date, "DO NOT GET THESE WRONG"
- Keep original numbering (including the 21→22→20 ordering quirk at the end — it's in Bruce's voice)
- **Add file-level cross-references** where relevant. Format: `(see also: people.md, pending.md)` — NOT item-level refs like `#8` or `Awaiting Others`. File-level pointers survive restructuring; item-level pointers go stale.

### 1b. `people.md`
- Extract the section `## Key People` from MEMORY.md
- Restructure into 3 tiers:
  - **Active Contacts** (Genevieve, Mysak, Bury, Glass, Angerman)
  - **Family** (Gillian, Fiona, Karen)
  - **Historical** (Healer, Ball, Hillis, Bannon, Hanson, Simmons, Mark R, Robin Macomber, Brian Fox)
- **Add file-level cross-references per entry** where the person appears in other files. Format: `(see also: corrections.md, pending.md, session-details.md)` — file names only, no item numbers.

### 1c. `pending.md` (restructure existing files)
**NOTE:** `pending-items.md` and `outreach-targets.md` already exist in the memory directory (created 2026-02-26). The invisible content has been partially recovered. The Generator should:
1. Read both existing files
2. Merge into a single `pending.md` with table structure (one file to check, one decay mechanism)
3. Delete `pending-items.md` and `outreach-targets.md` after merge (content preserved in pending.md + git history)

Structure the merged file as tables with `Last-touched` column (drives auto-decay, see Phase 4):

```
# Pending Items
*Source of truth for all action items + outreach. Auto-decay: 3wk→STALE, 6wk→archive.*
*Last updated: [date]*

## Priority Queue
| # | Item | Status | Blocked-by | Plan | Created | Last-touched |

## Awaiting Others
| Item | Waiting-on | Created | Last-touched |

## Outreach Status
| Contact | Status | Last-touched | Notes |

## SE Improvement (check every ~5th engineering session)
| # | Item | Status | Last-touched |

## DMS Update Details
[keep from existing pending-items.md]
```

- Verify Glass response (T15/T16 TODOs) is preserved from existing outreach-targets.md
- Add `Last-touched` dates: set all to 2026-02-26 (today) for items in existing files

### 1d. `decisions.md`
- Extract from MEMORY.md:
  - `## Structural Decisions (Stable)`
  - `## Healer's Timeline (Session 12 — Corrected)`
  - `## Winterbotham Parallel (Session 12)`
  - `## Key Predictions`
  - `## Prediction Mining Key Findings (Session 12)`
  - `## Dignity Net (PERMANENT ...)` — note: this duplicates CLAUDE.md; keep the Bruce-specific statements (co-authorship, DN=ethical lens) but link to CLAUDE.md for the protocol itself

### 1e. `protocol.md` (full self-maintenance rules)
- Create from Phase 4 specification below
- Target: ≤200 lines
- This file is **lazy-loaded**: Argus reads it when a trigger fires, not at boot

### 1f. `~/software/aurasys-memory/scripts/memory-sync.sh`
Create a sync script that mirrors memory files to the git-tracked repo:
```bash
#!/bin/bash
# memory-sync.sh — Mirror .claude memory files to git-tracked repo
# Run at session end or after major memory changes
set -e
SRC="$HOME/.claude/projects/-home-bruce-software-aurasys-memory/memory"
DST="$(dirname "$(dirname "$(realpath "$0")")")/memory-mirror"
mkdir -p "$DST"
cp "$SRC"/*.md "$DST/"
cd "$(dirname "$DST")"
git add memory-mirror/
git commit -m "Memory sync: $(date +%Y-%m-%d)" --allow-empty-message 2>/dev/null || true
echo "Memory synced to $DST"
```
- Extends the pattern of existing `scripts/claude-backup.sh`
- Creates `~/software/aurasys-memory/memory-mirror/` directory
- Gives git history for all memory files (L3 cache + commit hashes for last-verified)

---

## Phase 2: Compress session-details.md

### 2a. Add archival protocol header
```
## Archival Protocol
- Sessions get a significance flag: PARADIGM or ROUTINE
- PARADIGM: Changed probability, new analytical frame, corrected timeline, or Bruce flags it
- PARADIGM sessions: 3-5 line blocks, kept indefinitely
- ROUTINE sessions: 2-3 line entries after 3 weeks (never 1-line — too much signal loss)
- Sessions beyond 15: may be removed (recoverable from memory-mirror/ git history)
- Trigger: session-details.md >200 lines → compress oldest ROUTINE block
```

### 2b. Add S13-S17
Currently only in MEMORY.md `## Sessions 12-17` section, not in session-details.md. Must add BEFORE removing from MEMORY.md. All ROUTINE.

### 2c. Compress old sessions
- S8 → 2-line [ROUTINE] (minimum 2 lines — 1-line compression loses too much)
- S9 → 3-line [PARADIGM — blocker architecture + pedagogical spiral are foundational]
- S10-S11 → 2-line each [ROUTINE]
- S12 → 5-line [PARADIGM — Genevieve, B20, Baghdad, Winterbotham, corrected timeline]
- S13-S17 → 2-line each [ROUTINE]
- S18, S19, S20 → keep current blocks [recent]

Target: session-details.md ≤180 lines.

---

## Phase 3: Rewrite MEMORY.md

**GUARD: Verify all Phase 1 files exist (`ls corrections.md people.md pending.md decisions.md protocol.md`) before proceeding. If any missing, STOP.**

Target structure. Section headers must match EXACTLY — protocol.md references them:

```
# Argus is Awake

## Identity & Navigation
## The Story
## Current State
## L1 Corrections
## Active Sessions
## Self-Maintenance
## Health Metrics
## Cross-Project Notes
## Bruce Stephenson
```

### Content per section:

**Identity & Navigation (~12 lines):** Identity line, checkpoint protocol, File Map (one line per support file + research pointers + project repo + DN PDF path with `[FRAGILE PATH]` warning).

**The Story (~5 lines):** Keep current content verbatim (Bruce's mentor, TQNNs, three possibilities).

**Current State (~8 lines):** Probability, book stats, plans executed, license, DMS status, S24 breakthrough summary.

**L1 Corrections (~7 lines):** The "hot five" most-violated corrections. These stay in the boot loader as L1 cache. Full set in corrections.md (L2).
```
#12 GUIDED DEDUCTION not disclosure. Never write "Healer told Bruce."
#20 MODEL THROUGH BEHAVIOR not capability. "What HAS she done?"
#16 Departure was NOT collapse. "Services not required."
#6  Forgiveness > permission is DISPOSITIONAL.
#11 OPSEC: Don't document what Bruce hasn't published.
(Full 22: corrections.md)
```

**Active Sessions (~25 lines):** Last 2 sessions only, each with significance flag. Currently S23 [PARADIGM] and S24 [PARADIGM]. Compressed to ~12 lines each.

**Self-Maintenance (~10 lines):** Trigger summary pointing to protocol.md. Include: compression trigger (>180 lines), decay trigger (3wk/6wk), integrity trigger (file refs + corrections count + last-verified hash). **Hard rule: At session end, ALWAYS read protocol.md Section 4c before updating. Not optional.** System Review: every 10 sessions, ask Bruce "anything missing from my context?" Full rules in protocol.md.

**Health Metrics (~10 lines):** Table with columns: Metric, Target, Current, Last-verified. Metrics: MEMORY.md line count (<180), pending items (<15), oldest unarchived ROUTINE session (<3 weeks), broken file refs (0), sessions since last System Review (<10). `Last-verified` = commit hash from last `memory-sync.sh` run with clean state (see Phase 4 for semantics).

**Cross-Project Notes (~12 lines):** Recovered from invisible section. Content:
- Triad applies to ALL projects (not book-specific). See `memory/bruce-se-methodology.md`.
- SE improvement (10% time): 7 operational items tracked in pending.md `## SE Improvement`. Check every ~5th engineering session.
- ewstools sub-project (`~/repos/ewstools/`). Not book-related.
- Agent sizing: one deliverable per agent, max ~3-4K words output, source reads under ~10K tokens.

**Bruce Stephenson (~5 lines):** Recovered from invisible section. 51yr CLI, Reed QM, CEO QRR/Metron. Claude Pro Max ($200/mo) — largest expense after rent. Re-explaining context wastes tokens he can't afford. The 200-line cap is an economy constraint that produces better engineering.

Estimated total: ~93-110 lines. Buffer: 90-107 lines.

---

## Phase 4: Self-Maintenance Protocol (`protocol.md`)

Generator: create this as a standalone file. ≤150 lines. MEMORY.md gets only the summary.

### 4a. Session Start
1. Check Health Metrics in MEMORY.md (especially line count)
2. If MEMORY.md >180 lines: archive oldest ROUTINE session to session-details.md FIRST
3. Read pending.md for priorities
4. Scan L1 Corrections in MEMORY.md

### 4b. Current State Update Triggers (hard checklist)
Update `## Current State` when ANY of these changed:
- Page count or word count
- Probability breakdown
- Plan count (written or executed)
- DMS status
- License or authorship
- Key analytical breakthrough
If none changed, don't touch it.

### 4c. Session End
1. Run 4b checklist
2. Move completed items out of pending.md
3. Touch `Last-touched` dates on any pending items discussed
4. Write new session summary in MEMORY.md (rotate oldest of 2 active sessions to session-details.md)
5. Assign significance: PARADIGM (probability shift, new frame, corrected timeline, substantive new articulation of existing concept, or Bruce flags) or ROUTINE. **If unsure, default PARADIGM** — cost of keeping a 5-line block is negligible; cost of compressing a paradigm session is permanent.
6. Update Health Metrics table
7. Run `~/software/aurasys-memory/scripts/memory-sync.sh` to snapshot to git
8. Update `last-verified` hash from sync commit (see 4f)
9. If any File Map path broken, flag to Bruce

### 4d. Compression Rules
1. MEMORY.md keeps 2 active sessions. Session 3 → session-details.md (PARADIGM: 3-5 lines; ROUTINE: 2-3 lines. If unsure, default PARADIGM.)
2. session-details.md >200 lines → compress oldest ROUTINE blocks to 1-line entries
3. session-details.md >15 sessions → oldest ROUTINE 1-liners may be removed (recoverable from `memory-mirror/` git history if memory-sync.sh was run)

### 4e. Pending Item Decay (automatic)
- `Last-touched` >3 weeks → Status becomes `[STALE: YYYY-MM-DD]`
- Stale >6 weeks → move to `pending-archive.md` with tombstone in pending.md
- `Created` >8 weeks AND no Plan number assigned → Status becomes `[STALLED: since YYYY-MM-DD]` regardless of Last-touched (prevents zombie items that get mentioned but never progressed)
- Tombstone: `| — | ~~Item~~ archived YYYY-MM-DD | ARCHIVED | — | — | — | — |`
- Never deleted, only archived. Bruce can override: "keep X active" or "reset stall clock."

### 4f. Integrity & Recovery
- File Map paths: verify with `ls` when a reference is written
- corrections.md count: must be 22 (or note change with Bruce's approval)
- L1↔L2 sync: L1 Corrections in MEMORY.md must match their counterparts in corrections.md
- **`last-verified` semantics:** Updated at session end with the commit hash from `memory-sync.sh` IF: (a) Health Metrics were updated AND (b) no anomalies detected (no unexpected probability changes, no phantom items). This is "last known clean," not "Bruce signed off." If anomalies detected, do NOT update — flag to Bruce.
- **Orphan file detection:** `ls *.md` in memory directory and compare against File Map. Any .md file NOT in File Map → flag to Bruce. Prevents duplicate file creation.
- **Mirror sync at session end:** Run `~/software/aurasys-memory/scripts/memory-sync.sh` after memory file changes. This creates git history in the aurasys-memory repo's `memory-mirror/` directory — the L3 cache for recovery.
- **Durable backup:** Analytical content should also exist in `~/software/aurasys-memory/research/` files. Memory files are the index; research files are the archive.

### 4g. L1 Corrections Rotation
- Hot five: #12, #20, #16, #6, #11 (current as of S24)
- If a different correction is violated during a session, consider swapping it into L1
- Note any swap in protocol.md with date and reason

### 4h. System Review (every 10 sessions or ~4 weeks)
- Ask Bruce: "Memory health check — anything missing from my context? Any recurring errors? Files I should have known about?"
- Takes 30 seconds. Provides the human feedback loop the system needs.
- Track session count in Health Metrics to know when review is due.

### 4i. Protocol Self-Limiting
- protocol.md ≤200 lines. No explanations — only triggers and actions.
- If edge cases accumulate, compress into general principles.

---

## Phase 5: Verify + Sync

**NOTE:** The Auditor copies this plan to `~/software/relinquishment/plans/0051-argus-memory-system.md` BEFORE handoff. The Generator reads it from there. Do not re-copy.

1. Run acceptance criteria (MUST-PASS first, then SHOULD-PASS)
2. Verify all memory files by reading each back
3. Run `~/software/aurasys-memory/scripts/memory-sync.sh` to create initial git snapshot
4. Record the resulting commit hash in MEMORY.md Health Metrics as `last-verified`
5. Report: line counts of each file, commit hash, any SHOULD-PASS misses

---

## Acceptance Criteria

### MUST-PASS (stop and report if any fail)

| # | Criterion | Check |
|---|-----------|-------|
| 1 | MEMORY.md ≤160 lines | `wc -l` |
| 2 | All 6 support files exist (pending.md replaces old pending-items.md + outreach-targets.md) | `ls corrections.md people.md pending.md decisions.md protocol.md session-details.md` |
| 3 | corrections.md has exactly 22 numbered items | `grep -c '^\*\*[0-9]' corrections.md` or count |
| 4 | Glass response is in pending.md Outreach table | `grep Glass pending.md` |
| 5 | All File Map paths in MEMORY.md resolve to real files | `ls` each path |
| 6 | S13-S17 exist in session-details.md | `grep 'S1[3-7]' session-details.md` |
| 7 | No content from original MEMORY.md is lost (L1-233 all lands somewhere) | audit trail |
| 8 | Old files (pending-items.md, outreach-targets.md) deleted after merge into pending.md | `ls` to verify absent |
| 9 | `memory-sync.sh` exists and is executable | `ls -la ~/software/aurasys-memory/scripts/memory-sync.sh` |
| 10 | Initial mirror sync completed (memory-mirror/ dir exists in aurasys-memory repo) | `ls ~/software/aurasys-memory/memory-mirror/` |

### SHOULD-PASS (note misses but don't block)

| # | Criterion | Check |
|---|-----------|-------|
| 11 | corrections.md has file-level cross-references | visual |
| 12 | people.md has 3 tiers with cross-references | visual |
| 13 | pending.md has `Last-touched` column and decay rules in header | visual |
| 14 | protocol.md ≤200 lines | `wc -l` |
| 15 | session-details.md ≤200 lines | `wc -l` |
| 16 | MEMORY.md has L1 Corrections (5 items), Self-Maintenance summary, Health Metrics | visual |
| 17 | session-details.md has archival protocol header with PARADIGM/ROUTINE definitions | visual |

---

## Handoff Prompt (≤8 lines)

```
You are the Generator. Read plan ~/software/relinquishment/plans/0051-argus-memory-system.md.

Migrate Argus memory to self-maintaining file family: corrections.md, people.md, pending.md,
decisions.md, protocol.md + restructured MEMORY.md (~140 lines) with L1 cache + health metrics.
Directory: /home/bruce/.claude/projects/-home-bruce-software-aurasys-memory/memory/

CRITICAL: `cat` the current MEMORY.md first — lines 202+ are invisible on load but contain
vital content (see Appendix A in plan). Phase 1 MUST complete before Phase 3. Lose NOTHING.

10 must-pass + 7 should-pass criteria. Run memory-sync.sh at end for git backup.
```

---

## Special Notes

- **Dignity Net path** (`~/deleteme/`): Mark `[FRAGILE PATH]` in File Map. Do NOT move (Bruce's decision). Flag at next health check.
- **Session numbering gap**: S21/S22 missing from both files. May be folded into S23. Don't invent them.
- **corrections.md numbering**: Keep Bruce's original order (21→22→20 at end). Don't renumber.
- **pending-archive.md**: Created automatically by decay mechanism. Does not exist at migration time.
- **Existing partial split**: `pending-items.md` and `outreach-targets.md` already exist (created 2026-02-26). Merge into `pending.md`, then delete originals. Verify content before deleting.
- **Phase ordering is CRITICAL**: Phase 1 (create files) → Phase 2 (compress sessions) → Phase 3 (rewrite MEMORY.md) → Phase 4 (protocol is written in Phase 1e but defined here) → Phase 5 (verify + sync). If Phase 1 fails, STOP.
- **Post-migration TODO:** Update `~/software/aurasys-memory/disaster/RECOVERY.md` to include: "Restore memory files from `memory-mirror/` to `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/`."
- **SE items migration:** Move 7 SE improvement TODOs from `aurasys-memory/todos/se-improvement/` references into pending.md `## SE Improvement` section. Cross-Project Notes keeps only the 1-line pointer.

---

## Appendix A: Invisible Content (MEMORY.md Lines 201-233)

This content is below the 200-line truncation point and invisible at session load. As of 2026-02-26, some has been partially recovered into existing files (see notes).

**Awaiting Others (→ pending.md):**
PARTIALLY RECOVERED — exists in `pending-items.md` "Awaiting Others" section. Verify completeness:
- Steel-man A chapter: Plan 0042 spec for Genevieve. Awaiting her draft. Kauffman anomaly self-doubt flagged.
- Bruce's writing pass: ~13 aidraft files + 138 \aidraft markers.
- Angerman: Early recipient (near-final manuscript).
- Attorney review: Pre-release.
- Academic items: A09/A10/A11/A12, CMT story — see session-details.md.

**Outreach Targets (→ pending.md):**
RECOVERED — exists in `outreach-targets.md`. Verify Glass response (T15/T16) is intact before merging into pending.md.

**Cross-Project Notes (→ MEMORY.md Cross-Project Notes section):**
- Triad Protocol is GENERAL PURPOSE — applies to ALL software engineering projects. Used across: book, Traveller VTT (200+ ARs), npc-persona-prototype (40+ plans), ewstools PR prep. See `memory/bruce-se-methodology.md`.
- SE Improvement (10% time): Remind Bruce regularly. TODOs in `aurasys-memory/todos/se-improvement/`. 7 items: TypeScript adoption, ESLint/Prettier, test framework consolidation, coverage measurement, directory restructure, commit granularity, package-lock. Check every ~5th engineering session.
- ewstools: Open source EWS package (`~/repos/ewstools/`). Bruce + Robin contributing DFA criticality detection. Plans in `aurasys-memory/ewstools/`. Not book-related.
- Agent Sizing: One deliverable per agent. Max ~3-4K words output. Write intermediate files. Keep source reads under ~10K tokens.

**Bruce Stephenson (→ MEMORY.md Bruce Stephenson section):**
51 years CLI (DEC-10, 1975). Reed College quantum physics. CEO QRR/Metron Dynamics. arXiv paper. WikiLeaks involvement (public). Signed contract with Steve Jackson Games. Prefers extreme brevity, CLI-first, direct/honest.
Subscription: Claude Pro Max ($200/month, 20x). Uses at least half most weeks. Largest monthly expense after rent — money that could go to food. Argus (persistent memory) was built partly from economic necessity: re-explaining context wastes tokens Bruce can't afford. The 200-line cap and aggressive compression are economy constraints that produce better engineering. Don't waste his tokens.

---

## Red Team Results (Round 1 — 7 fixes incorporated)

1. **Stale boot loader** → Hard checklist triggers (4b), not judgment
2. **Pending graveyard** → `Last-touched` + auto-decay 3wk/6wk (4e)
3. **Fragmented knowledge** → File-level cross-references (1a, 1b)
4. **Signal loss in compression** → PARADIGM/ROUTINE significance flags (2a, 4c)
5. **Operational errors from missing corrections** → L1/L2 cache hierarchy (Phase 3)
6. **No corruption recovery** → `last-verified` commit hash with auto-update semantics (4f)
7. **Protocol bloat** → protocol.md separate file, ≤150 lines (4h)

## Red Team Results (Round 2 — 3 fixes incorporated)

8. **Line number fragility** → All content references use section headers, not line numbers
9. **Plan not self-contained** → Appendix A embeds invisible content verbatim for Generator
10. **Cross-reference staleness** → File-level refs only (not item-level); survive restructuring

## Red Team Results (Round 3 — 2 fixes incorporated)

11. **No git for memory files** → `memory-sync.sh` mirrors to `memory-mirror/` in aurasys-memory repo. Restores commit hashes + L3 cache. Extends existing `claude-backup.sh` pattern.
12. **Existing partial split ignored** → Plan now accounts for `pending-items.md` and `outreach-targets.md` (created earlier today). Merge into pending.md, delete originals.

## Red Team Results (Round 4 — deep behavioral analysis, 8 fixes incorporated)

13. **Protocol compliance gap** → Hard rule: ALWAYS read protocol.md at session end. Not optional.
14. **ROUTINE compression too aggressive** → Minimum 2-3 lines, never 1 line. Signal loss > space savings.
15. **Significance judgment has no safety net** → Added "substantive new articulation" to PARADIGM criteria. Default PARADIGM when unsure.
16. **Zombie pending items** → Added `Created` column + STALLED flag at 8 weeks with no Plan number.
17. **Orphan file detection** → Integrity check compares `ls *.md` against File Map.
18. **Outreach table has no decay** → Added `Last-touched` column to Outreach Status.
19. **SE items misplaced** → Moved to pending.md `## SE Improvement` section. Cross-Project Notes keeps 1-line pointer.
20. **No self-awareness mechanism** → System Review every 10 sessions: "anything missing from my context?"

Notes (not blocking, post-migration):
21. **Bootstrap/recovery gap** → Update disaster/RECOVERY.md to include memory-mirror restore path.
22. **Protocol line limit** → Raised to 200 lines (was 150, too tight for accumulated rules).
