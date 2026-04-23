# Plan 0054: Session Journal System

**Auditor:** Argus (Session 31)
**Date:** 2026-03-04
**Status:** COMPLETE (verified S63 audit)

## Purpose

Add a per-session journal layer to Argus memory. Currently new instances lose the middle layer between 5-line MEMORY.md summaries and full conversation context. Journals capture decision reasoning, key exchanges, working state, and handoff notes in ~500-1000 word files that fade automatically.

## Design: Three-Window Fading

| Window | Sessions | Size | On disk? |
|--------|----------|------|----------|
| ACTIVE | Last 3 | 500-1000 words | Yes, `memory/sessions/s{NNN}.md` |
| WARM | 4-10 back | 200-300 words | Yes, same location |
| COLD | 11+ back | 2-3 lines | No — session-details.md only, file deleted (git-recoverable) |

**PARADIGM journals stay WARM indefinitely** (exempt from COLD deletion).

Zero boot cost. Journals are lazy-loaded, never read automatically at session start.

## Phase 1: Create directory

Create `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/sessions/` (empty, will be populated at session ends).

## Phase 2: Update protocol.md

**All edits are in:** `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/protocol.md`

### 2a. Section 3 (Session End) — insert after line 33 (step 5), before step 6

Add steps 5a and 5b:

```
5a. Write session journal to `memory/sessions/s{NNN}.md` using template below.
    Target: 500-1000 words. Sections: Decisions, Key Exchanges, Working State, Artifacts, Handoff.
5b. Slide journal windows:
    - If >3 ACTIVE journals: compress oldest ACTIVE → WARM (remove Key Exchanges,
      compress Decisions to single lines, truncate Handoff to 1 sentence, update Window: header)
    - If >10 journal files on disk: delete oldest non-PARADIGM WARM file
      (verify session-details.md has 2-3 line entry first)
```

### 2b. Section 4 (Compression) — insert after line 51 (end of current Section 4), before Section 5

Add subsection:

```
### 4a. Journal Window Compression

Journal files: `memory/sessions/s{NNN}.md`
- ACTIVE (last 3): 500-1000 words. Written at session end (step 5a).
- WARM (4-10 back): 200-300 words. Compressed when pushed out of active window.
  Remove: Key Exchanges. Compress: Decisions to single lines. Truncate: Handoff to 1 sentence.
  Update Window: header from ACTIVE to WARM.
- COLD (11+ back): File deleted from disk. session-details.md 2-3 liner is only record.
  Full journal recoverable from memory-mirror/ git history.
- PARADIGM journals exempt from COLD deletion (stay WARM indefinitely).
  If WARM window exceeds 10 files, compress oldest PARADIGM WARM to ~150 words.

Template:
  # Session {N} — {Title}
  **Date:** YYYY-MM-DD | **Significance:** PARADIGM|ROUTINE | **Window:** ACTIVE|WARM
  ## Decisions
  ## Key Exchanges
  ## Working State (In progress / Blocked / Next likely)
  ## Artifacts
  ## Handoff (2-4 sentences for cold-start pickup)
```

### 2c. Section 6 (Integrity) — append after line 71 (before Section 7)

Add:

```
- **Journal count:** `ls memory/sessions/s*.md` should yield ≤10 files (3 ACTIVE + ≤7 WARM). If >10, compress or delete oldest.
- **Journal alignment:** Every ACTIVE session in MEMORY.md must have a corresponding journal file. Flag if missing.
```

## Phase 3: Update MEMORY.md

**File:** `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/MEMORY.md`

### 3a. File Map section — add entry:

```
- `memory/sessions/` — per-session journals (lazy-loaded, three-window fading)
```

### 3b. Active Sessions — add cross-reference line after each session entry:

```
**Journal:** `sessions/s030.md`
```

(For S30 only — no retroactive journals for earlier sessions.)

### 3c. Self-Maintenance section — add bullet:

```
- **Journals:** 3 ACTIVE, ≤7 WARM on disk, rest COLD (deleted, git-recoverable). Compression at session end per protocol.md 4a.
```

### 3d. Health Metrics table — add row:

```
| Active journals | 3 | 0 (new system) | pending |
```

## Phase 4: Update memory-sync.sh

**File:** `~/software/aurasys-memory/scripts/memory-sync.sh`

Add after the existing `cp` lines (after the line that copies ptl.yaml):

```bash
[ -d "$SRC/sessions" ] && mkdir -p "$DST/sessions" && cp "$SRC/sessions/"*.md "$DST/sessions/" 2>/dev/null || true
```

## Acceptance Criteria

1. `memory/sessions/` directory exists
2. protocol.md has steps 5a/5b in Section 3, subsection 4a in Section 4, journal checks in Section 6
3. protocol.md line count ≤200
4. MEMORY.md has File Map entry, journal cross-ref on S30, Self-Maintenance bullet, Health Metrics row
5. MEMORY.md line count <180
6. memory-sync.sh copies sessions/ directory
7. Single commit: "Plan 0054: session journal system"

## What NOT to Do

- Do NOT write any actual journal files (that happens at session end, not in this plan)
- Do NOT modify session-details.md
- Do NOT modify corrections.md, decisions.md, people.md, or pending.md
- Do NOT change MEMORY.md Active Sessions content (only add `**Journal:**` cross-refs)
- Do NOT read files outside `~/software/aurasys-memory/` and `~/.claude/projects/-home-bruce-software-aurasys-memory/`
