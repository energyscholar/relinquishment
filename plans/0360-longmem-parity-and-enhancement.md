---
Plan-UID: 0360-LONGMEM
Status: APPROVED — Bruce confirmed 3-step roadmap 2026-05-21
Owner: Auditor (plans), Generator (executes)
Repos:
  longmem: ~/software/longmem/ (public, MIT)
  argus: ~/software/aurasys-memory/ (private)
  plans: ~/software/relinquishment/plans/ (this file)
Contingency: Git tag before each phase, DB backup before schema changes
---

# Plan 0360: Longmem Parity Update + Memory Architecture Enhancement

## Context

Longmem (`~/software/longmem/`) is the public MIT-licensed template for persistent
Claude Code memory. Last commit: 2026-04-03 (9f1bb6c). Argus (the live installation
at `~/software/aurasys-memory/`) has evolved significantly since:

- DB-backed storage (SQLite + WAL + FTS5, 20 tables, 25 views)
- 77 registered sessions (S1–S80, 3 gaps), 24 corrections, 143 PTL items
- Ingest pipeline (frontmatter .md → SQL data scripts)
- Mode profiles, health auto-compute, campaign state machines, snailmail protocol
- Associations table (typed entity relationships)

### Landscape Survey (2026-05-21)

15 CC memory repos analyzed. Key findings informing Phase 3:

| Repo | Stars | Key Feature Worth Adopting |
|------|-------|--------------------------|
| claude-memory-compiler | 1,072 | Anti-RAG: structured index > vector at personal scale |
| Ogham | 105 | Progressive compression (full→summary→one-liner), novelty detection |
| KoretyAutomate | 0 | Ebbinghaus decay (23-day half-life), pinned memories |
| codenamev | 20 | Truth maintenance + provenance tracking |
| Cog | 364 | Zero-code conventions, /reflect + /foresight as memory operations |
| total-recall | 79 | Write-gate: 5-question pre-write check |

Our approach validated: structured index + file-first + corrections = unique combination.
No surveyed repo has persistent error tracking with rotation.

### Plan Goals

1. Fix bugs in the current Argus memory system (Phase 1)
2. Update longmem to match current Argus architecture (Phase 2)
3. Enhance Argus with survey-sourced features, validate there first (Phase 3)
4. Propagate validated Phase 3 features to longmem template (Phase 4)
5. End-to-end validation (Phase 5)

### Principle: Template Follows Production

No feature enters the public longmem template until validated in Argus.
Survey-sourced features go to Argus first (Phase 3), then longmem (Phase 4).
Phase 2 includes ONLY features Argus already has.

---

## Phase 0: Baseline (before any changes)

**Purpose:** Establish known-good state. All rollback references point here.

### 0a. Tag longmem current state

```bash
cd ~/software/longmem
git tag v1.0.0 -m "Pre-0360 baseline: file-only template, 36-session case study"
```

### 0b. Backup Argus DB

```bash
cp ~/software/aurasys-memory/argus.db ~/software/aurasys-memory/argus.db.pre-0360
```

### 0c. Record current test status

```bash
cd ~/software/longmem && tests/run-all.sh
cd ~/software/aurasys-memory && ./scripts/test-schema.sh
```

Note: Argus test-schema.sh is EXPECTED to fail (stale counts — that's Phase 1's job).
Record pass/fail status as baseline. Longmem tests should pass.

### 0d. Record verified stats (single source of truth for all later phases)

```bash
cd ~/software/aurasys-memory && sqlite3 argus.db "
  SELECT 'sessions' as metric, COUNT(*) as value FROM sessions
  UNION ALL SELECT 'corrections', COUNT(*) FROM corrections
  UNION ALL SELECT 'ptl_items', COUNT(*) FROM ptl_items
  UNION ALL SELECT 'feedback', COUNT(*) FROM feedback
  UNION ALL SELECT 'projects', COUNT(*) FROM projects
  UNION ALL SELECT 'tables', COUNT(*) FROM sqlite_master WHERE type='table'
    AND name NOT LIKE 'memory_fts%'
  UNION ALL SELECT 'views', COUNT(*) FROM sqlite_master WHERE type='view'
  UNION ALL SELECT 'max_session', MAX(number) FROM sessions
"
```

Use these numbers in case study and README. Do not hardcode from memory.

**Acceptance criteria:**
- v1.0.0 tag exists on longmem
- argus.db.pre-0360 backup exists
- Test status recorded (longmem should pass; Argus expected to fail on counts)
- Stats recorded and saved to `~/software/aurasys-memory/phase0-stats.txt`

**No commit needed — tagging only.**

---

## Phase 1: Argus Bug Fixes (local, no longmem changes)

**Branch:** `fix/argus-memory-bugs` on `~/software/aurasys-memory/`

### 1a. Fix CRLF line endings

Verify actual CRLF files first (list may have drifted since plan was written):
```bash
file memory/*.md | grep CRLF
```
Run `dos2unix` on ALL files that show CRLF. Verify ingest still works after.

**IMPORTANT:** This changes every line in affected files. Commit separately with a
clear message so the diff doesn't obscure real changes in later commits.

**Commit 1:** `Fix: convert CRLF files to LF line endings`

### 1b. Update test-schema.sh expected counts

File: `scripts/test-schema.sh`
- Query ACTUAL counts dynamically: `SELECT COUNT(*) FROM sqlite_master WHERE type='table'
  AND name NOT LIKE 'memory_fts%'` and `WHERE type='view'`
- Update expected values to match. Current: 20 tables, 25 views.
- VERIFY these numbers at execution time, don't trust plan numbers.

### 1c. Recalculate checksums in MEMORY.md section 5

All 6 documented checksums have drifted. Recompute with `sha256sum FILE | cut -c1-8`.
Update MEMORY.md.

**Note:** Phase 3 will change some of these files again. That's fine — Phase 3
should update checksums as part of its work.

### 1d. Fix missing file references in MEMORY.md

Before removing any reference, check `git log --all -- memory/FILENAME` to verify
the file wasn't lost rather than never existing.

- `user-ms-physics-skill.md` — check git history, verify exists or remove entry
- `traveller-reference.md` — clarify path (may be in repo root, not memory/)
- `dignity-net.md` — verify path, add if missing
- `disaster/recovery-protocol.md` — verify path, add if missing

### 1e. Fix correction count mismatch

Protocol.md says 23 corrections; DB says 24. Verify which is correct.
Update protocol.md to match actual count.

### 1f. Fix dead wiki-link

`project-gen-html-communication.md` references `[[project-gen-structural-authority]]`
which doesn't exist. Remove the dead link text. Do NOT create a new memory
file — scope creep for a bug-fix phase.

### 1g. Update session count comment

`scripts/data/017-sessions.sql` line 3 comment: update to actual count.
Query: `SELECT COUNT(*) FROM sessions` at execution time.

**Acceptance criteria:**
- `./scripts/rebuild-db.sh` succeeds
- `./scripts/test-schema.sh` passes
- `./scripts/ingest-memories.sh` processes all files without errors
- `file memory/*.md | grep CRLF` returns empty
- All MEMORY.md File Map paths resolve

**Commit 2:** `Fix: resolve memory system inconsistencies (checksums, counts, refs)`

---

## Phase 2: Longmem Parity (match current Argus architecture)

**Branch:** `feature/parity-update` on `~/software/longmem/`

### Scope Rule

Phase 2 templates ONLY what Argus has today. Survey-sourced features
(write-gate, progressive compression, novelty detection, Ebbinghaus decay)
go in Phase 3 (validate in Argus) then Phase 4 (propagate to longmem).

### What's changed since April 2026 that longmem doesn't reflect:

| Feature | Argus has | Longmem has | Phase 2 action |
|---------|----------|-------------|----------------|
| DB-backed storage | SQLite + WAL + FTS5 | File-only | Document as optional upgrade |
| Memory frontmatter | name/description/type metadata | No standard | Document standard |
| Mode profiles | Per-domain loading config | No concept | Add template section |
| Associations table | Typed entity relationships | None | Document [[wiki-link]] conventions |
| Dirty flag | `.session-active` for crash detection | None | Add to protocol |
| Lazy-regenerative | Metadata heals on contact | None | Add to protocol |
| PTL concurrency | .bak + last_modified check | None | Add to protocol |
| Ingest pipeline | frontmatter → SQL → DB | Nothing | Document for DB-backed mode |

Features that are Argus-specific and DO NOT go in template:
campaigns, snailmail, OPSEC views, person_clearances, correction_connections,
book-specific update triggers, Triad, Dignity Net.

### Hard Constraint: protocol.md Line Cap

Both Argus and longmem protocol.md are at 197 lines (cap: 200).
Adding dirty flag (~4 lines), lazy-regenerative (~3 lines), PTL concurrency
(~4 lines) requires ~11 lines. Must compress existing sections to fit.

**Compression targets:**
- Section 12 (Tutorials): 12 → 4 lines (reference patterns.md for details)
- Section 13 (Open Threads): 11 → 5 lines (compress to essentials)
- Saves ~14 lines. Enough for the 3 additions.

### Argus Reference Map (Generator: read these for each concept)

The Generator shell has NO conversation context. Read these Argus files to
understand the concepts being templated:

| Concept to template | Read this Argus file | Section/line |
|---------------------|---------------------|--------------|
| Dirty flag | `~/software/aurasys-memory/memory/protocol.md` | Section 1 (Session Start), line 10 |
| Lazy-regenerative | `~/software/aurasys-memory/memory/protocol.md` | Section 6 (Integrity), line 74 |
| PTL concurrency | `~/software/aurasys-memory/memory/protocol.md` | Section 10, lines 142-143 |
| Mode profiles | `~/software/aurasys-memory/memory/MEMORY.md` | Section 4 (Mode Profiles table) |
| Health vector | `~/software/aurasys-memory/memory/protocol.md` | Section 13 (Health Vector) |
| Corrections with domains | `~/software/aurasys-memory/memory/corrections.md` | Any entry (see `domain` field in frontmatter) |
| Memory frontmatter | Any file in `~/software/aurasys-memory/memory/feedback-*.md` | YAML frontmatter block |
| DB schema overview | `~/software/aurasys-memory/scripts/db-setup/010-tables.sql` | Full file |
| Ingest pipeline | `~/software/aurasys-memory/scripts/ingest-memories.sh` | Lines 1-30 (header/usage) |

**Do NOT copy Argus-specific content** (corrections data, people data, session
data, campaigns, snailmail, OPSEC). Template the STRUCTURE, not the content.

### 2a. Update architecture.md

**Critical:** architecture.md currently says databases are BAD extensions
("Database backends (breaks portability)" in "Bad extensions" list at ~line 305).
This is a reversal. The Generator MUST use the pre-written framing below,
adapting for fit but preserving the tone and argument structure.

#### Pre-written framing (Generator: use these, adapt for context)

**Replace "Why not a database?" (line ~223) with:**

> **Why file-first?**
>
> Markdown and YAML are the default storage for good reasons:
> - Human-readable (easy to review, easy to fix)
> - Git-friendly (diffs are meaningful)
> - Tool-agnostic (works with any editor, any AI)
> - Zero dependencies (no schema migrations, no version conflicts)
> - Recoverable (worst case: text editor and git log)
>
> File-only mode works indefinitely. Most projects never need more. Start here.

**Add new section after "Why file-first?":**

> **When to add a database (optional, for mature installations)**
>
> After 30+ sessions, some projects outgrow file-only mode. Symptoms:
> - You grep memory files often and want ranked full-text search
> - Health metrics are tedious to compute manually
> - You want decay queries ("what haven't I verified in 90 days?")
> - Cross-referencing between memories matters (associations, provenance)
>
> The upgrade path: add SQLite (WAL mode, FTS5) alongside your existing
> files. Files remain the source of truth. An ingest pipeline reads
> frontmatter from .md files and populates the DB. The DB is a read
> cache — if it breaks, delete it and rebuild from the files.
>
> This is how the founding project evolved. For the first 36 sessions,
> file-only was sufficient. By session 50, computed views and full-text
> search justified the modest added complexity. File-only users lose
> nothing. DB-backed users gain query power without sacrificing
> portability — the files are still there, still human-readable,
> still git-friendly.

**Replace "Bad extensions" list (line ~304) with:**

> **Extensions to approach with caution:**
> - Database backends *without a file layer* (breaks portability — files
>   must remain source of truth; see "When to add a database" for the
>   right approach)
> - Web dashboards (adds complexity for marginal benefit)
> - Automated agents (removes human judgment)
> - Clever abstractions (harder to debug, harder to recover)

#### Other architecture.md additions (Generator writes these, no pre-written framing needed):

- **"Memory Frontmatter Standard"** section: Document the YAML frontmatter
  format used by .md memory files: `name` (kebab-case slug), `description`
  (one-line summary), `type` (user|feedback|project|reference). This is what
  the ingest pipeline parses. See Argus Reference Map for examples.

- **"Mode Profiles"** section: Document how to configure per-domain loading
  behavior. Different work modes load different L2 files. Template a table
  format (see Argus MEMORY.md Section 4 for the pattern).

- **"Associations & Relationships"** section: Document [[wiki-links]] as
  typed semantic relationships between memories: `relates_to`, `contradicts`,
  `supersedes`, `depends_on`. For file-only users: convention only. For DB
  users: associations table with typed edges.

- **"Landscape Context"** subsection (brief, under "Design Rationale"):
  Position longmem vs alternatives. Use survey data from plan header.
  Key differentiators: corrections system (unique), file-first portability,
  zero dependencies. Keep to ~8 lines — this is context, not marketing.

### 2b. Update protocol.md (within 200-line cap)

**Current state:** 197 lines (cap: 200). MUST compress before adding.

**Step 1 — Compress (do this FIRST, verify line count before proceeding):**
- Section 12 (Tutorials, lines ~165-178, 14 lines): reduce to 4-line pointer:
  "Tutorials appear as PTL items at session thresholds. See patterns.md for
  content. Max ONE per session. Skip if user said 'no tutorials.'"
- Section 13 (Open Threads, lines ~181-193, 13 lines): reduce to 5-line essentials:
  "At session end, extract unresolved topics from session. Topics in ≥3 of last 5
  sessions → add to Open Threads in MEMORY.md (max 5, one line each). Stale after
  3 sessions without mention. 'PTL add' to promote."
- **Expected savings: ~18 lines → protocol.md at ~179 lines**
- Run `wc -l` to verify ≤ 185 before proceeding to Step 2.

**Step 2 — Add (after compression verified):**
- **Dirty flag** (add to Section 1, Session Start, after line 1): 4 lines.
  If `.session-active` exists at start → last session ended uncleanly → run crash
  recovery (Section 10) first. Create `.session-active` at start. Remove at session end.
- **Lazy-regenerative** (add to Section 7, Integrity): 3 lines.
  "Metadata heals on contact. When you load a tracked resource and find stale
  metadata, fix it immediately — don't log it as debt."
- **PTL concurrency** (add to Section 6, PTL Maintenance): 4 lines.
  Before writing ptl.yaml: (1) backup to .bak, (2) validate YAML, (3) check
  last_modified hasn't changed since read, (4) update last_modified + item_count,
  (5) write.
- **Expected additions: ~11 lines → protocol.md at ~190 lines**

**Step 3 — Verify:** `wc -l .longmem/memory/protocol.md` must be ≤ 197.

### 2c. Update MEMORY.md template

- Add "Mode Profiles" section (4-5 lines): template showing per-domain config
  ```
  | Mode | Load | Notes |
  |------|------|-------|
  | Default | MEMORY.md + corrections.md | Always |
  | [Domain 1] | + [domain-specific L2 files] | Customize |
  ```
- Add "Database" one-liner in File Map pointing to architecture.md for details
- Health metrics: already present and adequate. No changes needed.
- L1 Corrections: already has hot-five concept. Add note about frequency-based
  rotation being the selection criterion.

### 2d. Update corrections.md template

- Add domain-tagging example in format block:
  ```
  **Domain:** [book|science|general|...]
  ```
- Add note about frequency-based L1 rotation:
  "The five most-violated corrections rotate into L1 in MEMORY.md."
- Keep existing format otherwise.

### 2e. Update directives.md

directives.md is the quick reference (133 lines). Must reflect protocol changes:
- Add dirty flag mention in Session Start Protocol
- Add lazy-regenerative concept in self-maintenance section
- Add PTL concurrency note
- Keep under 140 lines

### 2f. Update memory-sync.sh

Current script: 35 lines, does health warnings + git add/commit.
Add:
- CRLF detection: `file .longmem/memory/*.md | grep -l CRLF` → warning
- Checksum verification: compare `.file-hashes` before/after to detect drift
- `--verify-only` flag for dry-run integrity check
- Keep total under 60 lines

### 2g. Update template files (breakthroughs, people, decisions)

- `breakthroughs.md` — add format template with cap note (15 active + 5 killed)
- `people.md` — add three-tier template (Active / Peripheral / Historical)
  with example format. No clearance concept (Argus-specific).
- `decisions.md` — add rationale + status example format

### 2h. Review unchanged files for accuracy

These files exist but aren't being changed. Verify they're still accurate:
- `patterns.md` — 7 patterns, still valid? References still correct?
- `disaster-recovery.md` — 3 tiers, still sufficient?
- `ptl.yaml` — template seed item, still appropriate?
- `session-details.md` — empty template, no changes needed

If any are stale, fix. If all accurate, note "reviewed, no changes" in commit.

### 2i. Update case-study.md

Use verified stats from `~/software/aurasys-memory/phase0-stats.txt` (written
by Phase 0d). Do NOT confabulate numbers. If file doesn't exist, query the DB:
`cd ~/software/aurasys-memory && sqlite3 argus.db "SELECT 'sessions', COUNT(*)
FROM sessions UNION ALL SELECT 'corrections', COUNT(*) FROM corrections
UNION ALL SELECT 'ptl_items', COUNT(*) FROM ptl_items"`
- Add narrative: "The system has since evolved a DB-backed layer (SQLite + FTS5)
  as an optional acceleration. File-only mode remains the default."
- Note landscape positioning: "Surveyed 15 alternative CC memory systems (May 2026).
  longmem's corrections system remains unique — no competitor has persistent error
  tracking with rotation."
- Verify consulting email still correct

### 2j. Update README.md

- Update results table with verified stats
- Add brief mention of optional DB-backed mode (link to architecture.md)
- Update "What's Included" if new concepts were added
- Do NOT add "How It Compares" section — keep README focused on the user,
  not on competitors. Landscape context goes in architecture.md.
- Verify requirements section still accurate

### 2k. Update install.md and uninstall.md

Review both for accuracy against updated template structure.
- install.md: If new files were added to .longmem/memory/, install prompt
  should still work (it copies the entire .longmem/ directory).
- uninstall.md: Should still be accurate (removes .longmem/, cleans CLAUDE.md).
- If structure changes break either, fix them.

### 2l. Create CHANGELOG.md

```markdown
# Changelog

## [2.0.0] — 2026-05-XX

### Added
- Optional DB-backed mode documented in architecture.md
- Memory frontmatter standard (name/description/type)
- Mode profiles for per-domain loading
- Dirty flag for crash detection (protocol.md)
- Lazy-regenerative metadata healing (protocol.md)
- PTL concurrency guard (protocol.md)
- CRLF detection in memory-sync.sh
- Checksum drift detection in memory-sync.sh

### Changed
- Case study updated to 80+ sessions (from 36)
- Architecture "Why not a database?" → "Why file-first?"
- protocol.md: compressed tutorials and open threads sections
- corrections.md: domain-tagging and rotation note
- people.md: three-tier template

### Fixed
- memory-sync.sh: checksum verification on sync

## [1.0.0] — 2026-04-03
- Initial public release
```

### 2m. Run and fix tests

- Regenerate `.longmem/.file-hashes` for all changed files
- Update `tests/test-hashes.sh` baselines to match new hashes
- Run `tests/run-all.sh` — all must pass
- Run `tests/test-integrity.sh` separately to verify cross-references

### 2n. Tag release

```bash
git tag v2.0.0 -m "Parity update: match Argus S80 architecture"
```

**Acceptance criteria:**
- Fresh clone + edit MEMORY.md + `bash .longmem/scripts/memory-sync.sh` → works
- All template files have clear "fill this in" markers
- No Argus-specific content (campaigns, snailmail, OPSEC, people data, corrections data)
- README quickstart still accurate
- All tests pass (`tests/run-all.sh` exit 0)
- CHANGELOG.md exists and is accurate
- protocol.md ≤ 200 lines
- directives.md ≤ 140 lines
- v2.0.0 tag ready to push

**Commits:**
1. `Compress protocol.md: tutorials + open threads sections`
2. `Add parity features: dirty flag, lazy-regenerative, PTL concurrency`
3. `Update architecture.md: DB-backed mode, frontmatter, mode profiles`
4. `Update templates: corrections, people, breakthroughs, decisions`
5. `Update docs: case study, README, CHANGELOG, install/uninstall review`
6. `Update tests: regenerate hashes, verify all pass`

Or if cleaner: combine into 2-3 logical commits. Generator's judgment.

---

## Phase 3: Survey-Informed Enhancement (into Argus, validate first)

**Branch:** `feature/survey-enhancements` on `~/software/aurasys-memory/`

**IMPORTANT SCHEMA NOTE:** Argus has NO unified `memories` table. Content lives
in type-specific tables (corrections, feedback, projects, references, user_profile,
sessions, decisions, breakthroughs). The FTS5 `memory_fts` table provides unified
search via `source_table` + `source_id` columns. Argus already has an `associations`
table for typed entity relationships.

Phase 3 schema changes must work WITH this architecture, not against it.

### 3a. Confidence decay model

**Source:** KoretyAutomate (Ebbinghaus curve, 23-day half-life), adapted.

**Problem:** The non-existent `memories` table means confidence can't go on one table.

**Options (Generator chooses, Auditor reviews):**
1. **Metadata overlay:** New `memory_confidence` table keyed by (source_table, source_id).
   Pro: clean separation, no ALTER TABLE on 8 tables. Con: joins on every query.
2. **Per-table columns:** Add `confidence`, `last_verified`, `decay_half_life_days`
   to each content table. Pro: no joins. Con: 8 ALTERs, schema repetition.
3. **FTS5 extension:** Add confidence to `memory_fts`. Pro: search + decay in one query.
   Con: FTS5 content tables have constraints.

**Recommendation:** Option 1 (metadata overlay). Aligns with existing `associations`
pattern — metadata about content, not in content.

```sql
CREATE TABLE memory_confidence (
  id INTEGER PRIMARY KEY,
  source_table TEXT NOT NULL,
  source_id INTEGER NOT NULL,
  confidence REAL DEFAULT 1.0,
  last_verified TEXT,
  decay_half_life_days INTEGER DEFAULT 90,
  access_count INTEGER DEFAULT 0,
  last_accessed TEXT,
  UNIQUE(source_table, source_id)
);

CREATE VIEW v_memories_decayed AS
SELECT mc.*,
  mc.confidence * exp(-0.693 * (julianday('now') - julianday(mc.last_verified))
    / mc.decay_half_life_days) AS effective_confidence
FROM memory_confidence mc
WHERE mc.last_verified IS NOT NULL;
```

**Pinning:** Items with `decay_half_life_days = NULL` are pinned (no decay).
Use for corrections and safety-critical knowledge.

**Risk: access_count changes read path.** Every query becomes read+write.
Mitigate: update access_count asynchronously (batch at session end, not per query).

### 3b. Enhanced FTS5 ranking

**Source:** Instar (multi-signal ranking), adapted for our architecture.

**What:** Join `memory_fts` with `memory_confidence` to rank results:
0.4 × text_match + 0.3 × effective_confidence + 0.2 × recency + 0.1 × access_count.

**Where:** New view `v_memory_search` that combines FTS5 rank with confidence data.
Existing raw FTS5 queries remain available for unranked search.

### 3c. Associations table enhancement (NOT a new edges table)

**CRITICAL:** Argus already has `associations` with typed relationships
(`relates_to`, `contradicts`, `supersedes`, `exemplifies`, `derives_from`).
4 rows exist. The original plan proposed a duplicate `memory_edges` table.

**Fix:** Extend the existing `associations` table:
- Add `weight REAL DEFAULT 1.0` column (for ranking relationship strength)
- Add `verified_by` and `depends_on` to the relationship CHECK constraint
- Add views for inverse queries: "what depends on X?", "what contradicts X?"

```sql
-- Extend CHECK constraint (requires table rebuild in SQLite)
-- Add new relationship types to existing constraint:
--   'relates_to','contradicts','supersedes','exemplifies','derives_from',
--   'depends_on','verified_by','part_of'
```

**Note:** SQLite can't ALTER CHECK constraints. This requires a table rebuild
(CREATE new → INSERT from old → DROP old → RENAME new). Safe because
`associations` has only 4 rows.

### 3d. Evidence/provenance tracking

**Source:** Instar (evidence table) + codenamev (truth maintenance).

**What:** Append-only evidence rows linked to any memory via (source_table, source_id).

```sql
CREATE TABLE memory_evidence (
  id INTEGER PRIMARY KEY,
  source_table TEXT NOT NULL,
  source_id INTEGER NOT NULL,
  kind TEXT CHECK(kind IN ('message','commit','session','observation','correction')),
  evidence_text TEXT,
  confidence REAL DEFAULT 1.0,
  session_number INTEGER,
  created_at TEXT DEFAULT (datetime('now'))
);
```

**Population:** Corrections already have `established` and `last_violated` dates.
Initial population: INSERT one evidence row per correction from existing dates.
Ongoing: session registration creates evidence rows for discussed items.

### 3e. Write-gate protocol

**Source:** total-recall (5-question gate).

**What:** Before writing any new .md memory file, apply 5-question gate:
1. Does it change future behavior? → WRITE
2. Is it a commitment with consequences? → WRITE
3. Is it a decision with rationale? → WRITE
4. Is it a stable fact that will matter again? → WRITE
5. Did the user explicitly say "remember this"? → ALWAYS WRITE

**Where:** Argus protocol.md. BUT — protocol.md is at 197 lines.
Must be added as a compressed 3-line principle, not a 10-line section.
Or: add to directives (CLAUDE.md) rather than protocol.md.

### 3f. Progressive compression

**Source:** Ogham (3-tier staleness).

**What:** Stale memories compress in stages rather than binary keep/delete:
- Full text (active)
- Summary (3–5 lines, key decisions + rationale)
- One-liner (title + one sentence + date)
- Archive (git history only)

**Where:** Extend Compression Rules (protocol.md Section 4) from 2-state
(keep/archive) to 4-state. This REPLACES existing compression logic,
not addition — no net line increase.

### 3g. Novelty detection / dedup gate

**Source:** Ogham (similarity check), Instar (dedup).

**What:** Before creating a new .md memory file:
1. Exact slug match → skip (existing file covers this)
2. FTS5 search on proposed content → if top hit > threshold similarity,
   flag: "Existing memory [name] covers similar ground. Update or create new?"

**Where:** Protocol instruction for the AI. NOT in ingest-memories.sh
(ingest is batch, too late — gate must fire before file creation).

**Risk:** FTS5 doesn't return similarity scores natively. Approximate via
`rank` column from `memory_fts MATCH`. Set threshold empirically.

### Phase 3 Round 3: Progressive Compression

**Generator UID:** GEN-0360-R3
**Branch:** `feature/progressive-compression` on `~/software/aurasys-memory/`
**Depends on:** Round 1 (confidence decay must be live for stage classification)

**Design:** Replace binary compression (keep/archive) with 4-stage model.
Dual trigger: confidence-threshold OR age-threshold, least-compressed-wins
(i.e., an item stays at FULL if EITHER condition says FULL).

**Compression stages (from Resolved UQs):**

| Stage | Confidence gate | Age gate | What remains |
|-------|----------------|----------|-------------|
| FULL | >0.5 | <30d since last reinforced | Full text, no changes |
| SUMMARY | >0.2 | <90d | 3-5 lines: key decisions + rationale |
| ONE-LINER | >0.05 | <180d | Title + one sentence + date |
| ARCHIVE | ≤0.05 | ≥180d | Removed from .md; recoverable from git |

Pinned items (corrections) are always FULL — decay_rate = 0, confidence = 1.0.

**Scope:** Two changes:

1. **protocol.md Section 4** — replace lines 52-59 (8 lines) with 4-stage model.
   Session compression rules (MEMORY.md keeps 2 sessions, PARADIGM vs ROUTINE)
   are ORTHOGONAL to confidence-based compression and must be PRESERVED.
   Session rules govern session blocks in MEMORY.md/session-details.md.
   Confidence stages govern memory .md files (feedback, project, reference, etc.).

   Replacement (8 lines, no net increase):
   ```
   ## 4. Compression Rules

   **Sessions:** MEMORY.md keeps 2 active sessions. Session 3 → session-details.md
   (PARADIGM 3-5 lines indefinitely; ROUTINE 2-3 lines; default PARADIGM if unsure).
   session-details.md >200 lines → oldest ROUTINE blocks to 2-line entries.

   **Memory files:** 4-stage progressive compression, dual-trigger (least-compressed wins):
   FULL (conf>0.5 OR <30d) → SUMMARY 3-5 lines (>0.2 OR <90d) → ONE-LINER (>0.05 OR <180d) → ARCHIVE (git only).
   Query: `SELECT * FROM v_compression_candidates`. Pinned items exempt. Act during maintenance (§14).
   ```

2. **scripts/db-setup/020-views.sql** — add `v_compression_candidates` view at end.
   Returns non-pinned items whose effective_confidence has crossed a stage boundary
   below their current storage state. Since we don't track current storage state in
   the DB, this view simply lists all non-pinned items with their recommended stage:

   ```sql
   CREATE VIEW v_compression_candidates AS
   SELECT vmd.source_table, vmd.source_id, vmd.effective_confidence,
       vmd.half_life_days, vmd.last_reinforced, vmd.created_at,
       CASE
           WHEN vmd.effective_confidence > 0.5 THEN 'FULL'
           WHEN vmd.effective_confidence > 0.2 THEN 'SUMMARY'
           WHEN vmd.effective_confidence > 0.05 THEN 'ONE-LINER'
           ELSE 'ARCHIVE'
       END AS recommended_stage,
       ROUND(julianday('now') - julianday(
           COALESCE(vmd.last_reinforced, vmd.created_at)), 0) AS days_since_reinforced
   FROM v_memories_decayed vmd
   WHERE vmd.pinned = 0
   AND vmd.effective_confidence <= 0.5
   ORDER BY vmd.effective_confidence ASC;
   ```

   Note: Only shows items below FULL threshold (conf ≤ 0.5). Items at FULL don't
   need compression action. The age gate (least-compressed-wins) is applied by the
   operator reading the view — if `days_since_reinforced < 30`, the item stays FULL
   regardless of confidence. This keeps the view simple and the judgment with the AI.

### Round 3 Acceptance Criteria

- `./scripts/rebuild-db.sh` succeeds
- `./scripts/test-schema.sh` passes
- protocol.md ≤ 201 lines (current cap; 200 preferred but 201 pre-existing)
- protocol.md Section 4 has 4-stage model with session rules preserved
- `v_compression_candidates` returns rows with recommended_stage column
- Pinned items (corrections) do NOT appear in v_compression_candidates
- Items with effective_confidence > 0.5 do NOT appear
- Old sessions/projects with low confidence DO appear with correct stage

### Round 3 Git Workflow

1. Tag before: `git tag v0.3.2-pre-compression`
2. Branch: `git checkout -b feature/progressive-compression`
3. Commit: `Plan 0360 R3: progressive compression (4-stage, dual-trigger)`
4. Tag after: `git tag v0.3.3-progressive-compression`
5. Merge: `git checkout main && git merge feature/progressive-compression --no-ff`
6. Clean up: `git branch -d feature/progressive-compression`

### Round 3 Generator Reference Map

| Concept | Read this file | What to look for |
|---------|---------------|-----------------|
| Current compression rules | `memory/protocol.md` lines 52-59 | Section 4 (replace target) |
| Current protocol line count | `wc -l memory/protocol.md` | Must stay ≤ 201 |
| Confidence view | `scripts/db-setup/011-confidence-tables.sql` | v_memories_decayed columns |
| Current views | `scripts/db-setup/020-views.sql` | End of file (add new view) |
| Maintenance section | `memory/protocol.md` lines 164-179 | §14 where compression is actioned |

### Phase 3 Round 4: Evidence/Provenance

**Generator UID:** GEN-0360-R4
**Branch:** `feature/evidence-provenance` on `~/software/aurasys-memory/`
**Depends on:** Round 1 (confidence overlay must exist for evidence→reinforcement link)

**Design:** Append-only evidence table linked to any memory via (source_table, source_id).
Evidence records WHY we believe something — provenance for confidence scores.

**Scope:** Three changes:

1. **New schema file:** `scripts/db-setup/012-evidence-tables.sql`
   Loads between 011-confidence and 020-views (same pattern as 011).

   ```sql
   CREATE TABLE memory_evidence (
       id INTEGER PRIMARY KEY,
       source_table TEXT NOT NULL,
       source_id INTEGER NOT NULL,
       kind TEXT NOT NULL CHECK(kind IN
           ('established','violated','referenced','observed','corrected')),
       evidence_text TEXT,
       session_number INTEGER,
       created_at TEXT NOT NULL DEFAULT (datetime('now'))
   );

   CREATE INDEX idx_evidence_source
       ON memory_evidence(source_table, source_id);
   ```

   **Kind values:** `established` (initial creation evidence), `violated` (correction
   was triggered), `referenced` (accessed in a session), `observed` (user confirmed
   still true), `corrected` (content was updated). These are evidence events, not
   judgments.

2. **New data file:** `scripts/data/027-evidence.sql`
   Seed from existing correction dates (the only table with provenance data today):

   ```sql
   INSERT INTO memory_evidence(source_table, source_id, kind, evidence_text, created_at)
   SELECT 'corrections', id, 'established',
       'Correction established (seeded from corrections.established)',
       established
   FROM corrections WHERE established IS NOT NULL;

   INSERT INTO memory_evidence(source_table, source_id, kind, evidence_text, created_at)
   SELECT 'corrections', id, 'violated',
       'Correction violated (seeded from corrections.last_violated)',
       last_violated
   FROM corrections WHERE last_violated IS NOT NULL;
   ```

3. **Update `scripts/setup.sh`** — add line after 011-confidence-tables.sql:
   ```bash
   sqlite3 "$DB" < "${SCRIPT_DIR}/db-setup/012-evidence-tables.sql"
   ```

4. **Update `scripts/rebuild-db.sh`** — bump table count check from `-lt 18` to
   appropriate value (check actual count after rebuild, use that).

5. **Update `scripts/test-schema.sh`** — add `memory_evidence` to table existence checks.

**No protocol.md changes.** Evidence is infrastructure — the protocol already says
to verify stale memories. Evidence provides the audit trail.

**No views in this round.** A `v_evidence_timeline` could be useful but is not
required for the core feature. Add if needed in a future maintenance session.

### Round 4 Acceptance Criteria

- `./scripts/rebuild-db.sh` succeeds
- `./scripts/test-schema.sh` passes
- `memory_evidence` table exists with correct schema
- Seeded evidence rows: at least 24 `established` rows (one per correction)
- `INSERT INTO memory_evidence(source_table, source_id, kind, evidence_text) VALUES ('feedback', 1, 'referenced', 'test')` succeeds
- Invalid kind rejected: `INSERT ... kind='invalid' ...` fails CHECK constraint
- Index exists on (source_table, source_id)

### Round 4 Git Workflow

1. Tag before: `git tag v0.3.3-pre-evidence`
2. Branch: `git checkout -b feature/evidence-provenance`
3. Commit: `Plan 0360 R4: evidence/provenance table + seed from corrections`
4. Tag after: `git tag v0.3.4-evidence`
5. Merge: `git checkout main && git merge feature/evidence-provenance --no-ff`
6. Clean up: `git branch -d feature/evidence-provenance`

### Round 4 Generator Reference Map

| Concept | Read this file | What to look for |
|---------|---------------|-----------------|
| Confidence overlay pattern | `scripts/db-setup/011-confidence-tables.sql` | Same (source_table, source_id) pattern |
| Corrections data | `scripts/data/010-corrections.sql` | `established` and `last_violated` columns |
| Setup pipeline | `scripts/setup.sh` | Insert new file between 011 and 020 |
| Rebuild checks | `scripts/rebuild-db.sh` | Table count assertion |
| Test structure | `scripts/test-schema.sh` | Table existence check pattern |

---

### Phase 3 Round 5: Novelty Detection

**Generator UID:** GEN-0360-R5
**Branch:** `feature/novelty-detection` on `~/software/aurasys-memory/`
**Depends on:** Round 2 (FTS5 ranking must be live for similarity check)

**Design:** Before creating a new .md memory file, check for duplicates.
Two-step gate: exact slug match, then FTS5 similarity check.

**Scope:** One change — protocol.md only. This is a behavioral instruction,
not schema or code.

**Add to protocol.md** — insert as Section 16 (after §15 Write Gate), 5 lines:

```
## 16. Novelty Gate (before creating .md memory files)

1. Exact match: `ls memory/*-SLUG-*.md` — if exists, UPDATE don't create.
2. FTS5 check: `SELECT title, ROUND(-rank,1) FROM memory_fts WHERE memory_fts MATCH 'KEY TERMS' ORDER BY rank LIMIT 3`
   If top hit rank > 10.0 (tight match), flag: "Existing [title] covers similar ground. Update or create?"
3. If both clear, create. Record reasoning in commit message.
```

**Threshold rationale:** Tested against live corpus. Tight/specific queries
(3+ related terms) return ranks 10-14 for genuine matches, 2-3 for loose
associations. Threshold of 10.0 catches true duplicates without false
positives on broad terms. Documented as tunable.

**Protocol line budget:** Currently 201. Adding 5 lines → 206. Must compress
elsewhere to stay near cap. Target: §14 Opportunistic Maintenance (lines
164-179, 16 lines) — compress action list from current form to save 5+ lines.
Generator must measure before and after.

### Round 5 Acceptance Criteria

- protocol.md ≤ 201 lines (no net increase from current)
- Section 16 exists with novelty gate
- §14 compressed to offset the addition
- No other sections altered in meaning

### Round 5 Git Workflow

1. Tag before: `git tag v0.3.4-pre-novelty`
2. Branch: `git checkout -b feature/novelty-detection`
3. Commit: `Plan 0360 R5: novelty detection gate (§16) + §14 compression`
4. Tag after: `git tag v0.3.5-novelty`
5. Merge: `git checkout main && git merge feature/novelty-detection --no-ff`
6. Clean up: `git branch -d feature/novelty-detection`

### Round 5 Generator Reference Map

| Concept | Read this file | What to look for |
|---------|---------------|-----------------|
| Write gate pattern | `memory/protocol.md` §15 | Same structure — behavioral gate |
| Maintenance section | `memory/protocol.md` §14 | Compression target |
| Protocol line count | `wc -l memory/protocol.md` | Must stay ≤ 201 |
| FTS5 rank behavior | `scripts/db-setup/040-fts5.sql` | Column names for MATCH query |

---

### Components NOT adopting (from survey):

| Component | Source | Why not |
|-----------|--------|---------|
| Vector search (sqlite-vec) | agentmemory, claude-brain | Overkill at ~100-500 items |
| Biomimetic working/archive | claude-mem | 60-90s latency per tool call |
| Cloud memory sync | supermemory | Privacy: all local |
| Self-reflection pipeline | Cog | Interesting but premature — revisit after Phase 5 |
| Knowledge article compilation | claude-memory-compiler | Claude Code manages its own session context |
| Graph database | ViralV00d00 | Neo4j infrastructure too heavy |
| Privacy scoping (3-tier) | Instar | Single-user system |

**Acceptance criteria:**
- `rebuild-db.sh` succeeds with new schema
- Existing data migrates without loss (verify counts match Phase 0d)
- `memory_confidence` table populated for all FTS5-indexed items
- `v_memories_decayed` returns results with effective_confidence < base for old items
- `v_memory_search` returns ranked FTS5 results
- `associations` table accepts new relationship types
- `memory_evidence` table populated from existing correction dates
- Write-gate documented in protocol or directives
- Progressive compression replaces binary compression in protocol.md (no net line increase)
- Novelty detection documented

**Commits (revised per Round structure below):**
Per-round commits. Each round is a separate Generator session with settle-in period.

### Phase 3 Round Structure (approved 2026-05-21)

**Note:** Round implementation sections below supersede the design exploration
in sections 3a-3g above. Generators read the Round sections, not 3a-3g.

Features grouped into 5 rounds with dependency ordering. Each round gets 2-4
sessions of settle-in before the next round begins.

| Round | Features | Deps |
|-------|----------|------|
| 1 | Write-gate (protocol) + Confidence decay (schema) | None |
| 2 | Enhanced FTS5 ranking (multi-signal) | Round 1 |
| 3 | Progressive compression (dual-trigger) | Round 1 |
| 4 | Evidence/provenance (new table + seed) | None (but informs Round 2 ranking) |
| 5 | Novelty detection (dedup gate) | None |

### Resolved UQs (2026-05-21)

| Decision | Resolution |
|----------|-----------|
| Half-life per type | corrections=∞(pinned), feedback=90d, projects=60d, sessions=30d, references=180d, people=365d, breakthroughs=180d, decisions=90d |
| Compression trigger | Both: confidence-threshold OR age-threshold, least-compressed-wins |
| Evidence population | Both automated (session registration) + manual annotation |
| Access tracking | `last_accessed` timestamp only (no access_count); frequency derived from evidence table (Round 4) |
| Write-gate scope | Substantive writes only; skip mechanical updates (timestamps, checksums, status, session rotation) |
| Math functions | SQLite 3.40.1 confirmed: `pow()` available — use real-time decay in views |
| FTS5 ranking weights | text_match × 0.4 + confidence × 0.35 + recency × 0.2 + session_refs × 0.05 |
| Compression stages | FULL (conf>0.5 OR age<30d) → SUMMARY (>0.2 OR <90d) → ONE-LINER (>0.05 OR <180d) → ARCHIVE |

### Round 1A: Write-gate protocol

**Generator UID:** GEN-0360-R1A
**Branch:** `feature/confidence-decay` on `~/software/aurasys-memory/`
**File:** `~/software/aurasys-memory/memory/protocol.md` (196 lines, cap 200)

**Step 1 — Compress (measure before proceeding):**
Primary target: Section 8 (System Review, lines 96-101, 6 lines → 3 lines):
```
## 8. System Review (every 10 sessions or ~4 weeks)
Ask Bruce: "Memory health check — anything missing, recurring errors, unknown files?"
Track session count in Health Metrics. Due when d≥1.0 in health vector.
```
Run `wc -l`. If headroom < 7 lines, also compress Section 14 (Opportunistic
Maintenance, lines 164-179): consolidate action list from 6 items to 4,
remove rules 3-4 (already implied by rule 1-2). Target: save 3-4 more lines.

**Step 2 — Add (only after Step 1 verified):**
Section 15 — Write Gate. Fold scope rule into header to save 1 line:
```
## 15. Write Gate (substantive writes only — skip mechanical updates)

Before creating or substantially changing a memory file, all 5 must pass:
1. Will this matter in 30+ days?
2. Does existing memory already cover this?
3. Derivable from code, git, or existing files?
4. Contains context I can't reconstruct?
5. Would a future instance behave differently without this?
```

**Step 3 — Verify:** `wc -l` must show ≤200. If over, compress more before committing.
**Note on section numbering:** Existing sections are out of order (§12, §14, §13).
Do NOT renumber — references exist in other files. §15 goes at the end.
**Commit:** `Plan 0360 R1A: add write-gate protocol (§15)`

### Round 1B: Confidence schema + seed data

**Generator UID:** GEN-0360-R1B
**Branch:** `feature/confidence-decay` on `~/software/aurasys-memory/` (same branch as R1A)
**Depends on:** R1A complete (sequential execution — same branch)

**CRITICAL ORDERING:** Tables and `v_memories_decayed` must load BEFORE `020-views.sql`.
File name `011-confidence-tables.sql` ensures correct sort order.

**Design pattern: Structure-not-Control** (see
github.com/Relational-Relativity-Corporation/structure-vs-control).
Division-by-zero is eliminated structurally, not by runtime guards:
- `half_life_days` (human-readable period) is stored with CHECK > 0
- `decay_rate` (computed: `ln(2)/half_life_days`) is a GENERATED STORED column
- Pinned items: `half_life_days = NULL` → `decay_rate = 0.0` → `exp(0) = 1.0`
- Query formula: `base * exp(-decay_rate * elapsed)` — no division, no CASE, no branching
- Invalid states (zero half-life, division by zero) are impossible to represent

**Create:** `scripts/db-setup/011-confidence-tables.sql`
```sql
-- Confidence decay overlay (metadata pattern: keyed by source_table + source_id)
-- Loads before 020-views.sql so views can reference v_memories_decayed.
-- Uses structure-not-control: decay_rate generated column eliminates
-- division-by-zero structurally. Pinned items have decay_rate = 0,
-- so exp(-0 * t) = 1.0 — no branching needed.
CREATE TABLE memory_confidence (
    id INTEGER PRIMARY KEY,
    source_table TEXT NOT NULL,
    source_id INTEGER NOT NULL,
    base_confidence REAL NOT NULL DEFAULT 1.0,
    half_life_days INTEGER CHECK(half_life_days IS NULL OR half_life_days > 0),
    pinned INTEGER NOT NULL DEFAULT 0,
    decay_rate REAL GENERATED ALWAYS AS (
        CASE WHEN half_life_days IS NULL THEN 0.0
             ELSE ln(2) / half_life_days
        END
    ) STORED,
    last_accessed TEXT,
    last_reinforced TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE(source_table, source_id)
);

CREATE TABLE confidence_config (
    source_table TEXT PRIMARY KEY,
    default_half_life_days INTEGER CHECK(default_half_life_days IS NULL OR default_half_life_days > 0),
    default_pinned INTEGER NOT NULL DEFAULT 0,
    description TEXT
);

-- Branchless decay: exp(-rate * elapsed). No CASE, no division at query time.
-- decay_rate = 0 (pinned) → exp(0) = 1.0. decay_rate > 0 → exponential decay.
-- MAX(0, elapsed) guards against future-dated last_reinforced (clock skew).
CREATE VIEW v_memories_decayed AS
SELECT mc.source_table, mc.source_id, mc.base_confidence, mc.half_life_days,
    mc.pinned, mc.decay_rate, mc.last_accessed, mc.last_reinforced, mc.created_at,
    mc.base_confidence * exp(
        -mc.decay_rate * MAX(0,
            julianday('now') - julianday(COALESCE(mc.last_reinforced, mc.created_at)))
    ) AS effective_confidence
FROM memory_confidence mc;
```

**How structure-not-control handles the three risks found in audit:**
1. Division by zero → eliminated: `decay_rate` is pre-computed, query has no division
2. `half_life_days = 0` → impossible: CHECK constraint prevents at INSERT
3. Future timestamp → bounded: single `MAX(0, elapsed)` guard (minimal, at boundary)

**Create:** `scripts/data/026-confidence.sql`

**Verified:** All 8 source tables have `created_at`. Five also have semantic
date columns (corrections: `established`, feedback: `established`, sessions:
`date`, decisions: `date`, breakthroughs: `date`). Seed SQL below uses
COALESCE with semantic dates to survive rebuild-time `created_at` reset.

```sql
INSERT INTO confidence_config(source_table, default_half_life_days, default_pinned, description) VALUES
('corrections', NULL, 1, 'Safety-critical, never decay'),
('feedback', 90, 0, 'Behavioral guidance'),
('projects', 60, 0, 'State changes frequently'),
('sessions', 30, 0, 'Ephemeral by nature'),
('references', 180, 0, 'External pointers change slowly'),
('people', 365, 0, 'Relationships are durable'),
('breakthroughs', 180, 0, 'Analytical advances persist'),
('decisions', 90, 0, 'Decision context');

-- Seed from existing data.
-- IMPORTANT: Use semantic date columns where available, NOT created_at.
-- created_at resets to NOW on every rebuild (full DROP+INSERT cycle).
-- Tables with semantic dates: corrections(established), feedback(established),
--   sessions(date), decisions(date), breakthroughs(date).
-- Tables without: projects, references, people — use created_at (accept
--   rebuild-reset; their long half-lives make this tolerable).
INSERT INTO memory_confidence(source_table, source_id, base_confidence, half_life_days, pinned, created_at)
SELECT 'corrections', id, 1.0, NULL, 1, COALESCE(established, created_at) FROM corrections
UNION ALL SELECT 'feedback', id, 1.0, 90, 0, COALESCE(established, created_at) FROM feedback
UNION ALL SELECT 'projects', id, 1.0, 60, 0, created_at FROM projects
UNION ALL SELECT 'sessions', id, 1.0, 30, 0, COALESCE(date, created_at) FROM sessions
UNION ALL SELECT 'references', id, 1.0, 180, 0, created_at FROM "references"
UNION ALL SELECT 'people', id, 1.0, 365, 0, created_at FROM people
UNION ALL SELECT 'breakthroughs', id, 1.0, 180, 0, COALESCE(date, created_at) FROM breakthroughs
UNION ALL SELECT 'decisions', id, 1.0, 90, 0, COALESCE(date, created_at) FROM decisions;
```

**Update:** `scripts/setup.sh` — add BETWEEN 010-tables and 020-views:
```bash
sqlite3 "$DB" < "${SCRIPT_DIR}/db-setup/011-confidence-tables.sql"
```
Insert after `010-tables.sql` line, before `020-views.sql` line. This is the
critical ordering fix — `v_memories_decayed` must exist before views in 020 reference it.

**Update:** `scripts/rebuild-db.sh` — change table count check from `-lt 16` to `-lt 18`
(+2 tables: memory_confidence, confidence_config).

**Note on `last_reinforced`:** In Round 1, set `last_reinforced = last_accessed`
at session end. The distinction activates in Round 4 when evidence-based
reinforcement differs from simple access.

**Note on rebuild:** Full rebuild resets `last_accessed`/`last_reinforced` to NULL.
Acceptable for Round 1 — decay uses `COALESCE(..., mc.created_at)` as fallback.
Evidence table (Round 4) provides durable access tracking.

**Commit:** `Plan 0360 R1B: add memory_confidence overlay + confidence_config + seed data`

### Round 1C: Confidence-aware views

**Generator UID:** GEN-0360-R1C
**Depends on:** R1B complete (schema and `v_memories_decayed` must exist)

**Modify:** `scripts/db-setup/020-views.sql`

For each view below, ADD `effective_confidence` as a NEW column at the end.
NEVER remove or reorder existing columns. Use this JOIN pattern:
```sql
LEFT JOIN v_memories_decayed vmd
    ON vmd.source_table = '<table_name>' AND vmd.source_id = <table>.id
```
Column: `COALESCE(vmd.effective_confidence, 1.0) AS effective_confidence`

**CRITICAL: Change `SELECT *` to `SELECT <alias>.*` in any view getting a LEFT JOIN.**
Bare `SELECT *` with a JOIN includes ALL columns from BOTH tables — leaking
`source_table`, `source_id`, `decay_rate`, etc. into the view output. Verified
by test: bare `*` returns 9 columns; `p.*` returns 5. The three views using
`SELECT *` (v_active_projects, v_stale_projects, v_feedback_by_domain) must
become `SELECT p.*` / `SELECT f.*` when the JOIN is added.

The COALESCE handles records created between rebuilds that don't yet have
confidence rows (new items default to 1.0 = full confidence).

**Views to modify (column-additive ONLY, use table alias for SELECT):**
1. `v_active_projects` — `SELECT p.*` + join on source_table='projects'
2. `v_feedback_by_domain` — `SELECT f.*` + join on source_table='feedback'
3. `v_stale_projects` — `SELECT p.*` + add effective_confidence column for information ONLY.
   Do NOT change the WHERE clause or staleness logic. Time-based staleness
   and confidence decay are distinct concepts. (Staleness = "not touched."
   Low confidence = "not verified." An item can be stale but confident or
   fresh but unverified.)
4. `v_memory_stats` — add rows for memory_confidence and confidence_config counts

**Add new view (at END of 020-views.sql):**
```sql
CREATE VIEW v_confidence_overview AS
SELECT source_table,
    COUNT(*) AS total,
    SUM(CASE WHEN pinned = 1 THEN 1 ELSE 0 END) AS pinned_count,
    ROUND(AVG(effective_confidence), 3) AS avg_confidence,
    SUM(CASE WHEN effective_confidence < 0.2 THEN 1 ELSE 0 END) AS below_threshold
FROM v_memories_decayed
GROUP BY source_table;
```

**Update:** `scripts/test-schema.sh` — expected table and view counts (+2 tables,
+2 views: v_memories_decayed in 011, v_confidence_overview in 020).

**Commit:** `Plan 0360 R1C: add confidence to views + v_confidence_overview`

### Round 1 Acceptance Criteria (all three prompts combined)

- `./scripts/rebuild-db.sh` succeeds
- `./scripts/test-schema.sh` passes
- `SELECT * FROM v_memories_decayed LIMIT 5` returns rows with effective_confidence < 1.0 for old items
- `SELECT * FROM v_confidence_overview` shows per-table summary with 8 rows
- `SELECT * FROM confidence_config` shows 8 rows with correct half-lives
- `SELECT * FROM v_active_projects` has effective_confidence column
- `v_stale_projects` columns unchanged except appended effective_confidence
- protocol.md ≤ 200 lines AND contains write-gate section (§15)
- All existing views return same columns in same order (plus appended new ones)
- Phase 0d row counts unchanged (no data loss)
- Old items SHOULD show low effective_confidence — this is correct decay behavior, not a data error

### Round 1 Generator Reference Map

| Concept | Read this file | What to look for |
|---------|---------------|-----------------|
| Current protocol | `memory/protocol.md` | §8 (compress target), §14 (backup target), line count |
| Current schema | `scripts/db-setup/010-tables.sql` | Table patterns, FK conventions, **timestamp column names per table** |
| Current views | `scripts/db-setup/020-views.sql` | View column orders (PRESERVE), existing v_stale_projects WHERE clause |
| Campaign pattern | `scripts/db-setup/060-campaigns.sql` | Precedent: tables+views in single numbered file |
| Pipeline | `scripts/setup.sh`, `scripts/load.sh`, `scripts/rebuild-db.sh` | File ordering, verification checks |
| FTS5 population | `scripts/rebuild-db.sh` lines 41-60 | Which 8 tables feed FTS5 (same 8 for confidence) |

### Phase 3 Round 2: Enhanced FTS5 Ranking

**Generator UID:** GEN-0360-R2
**Branch:** `feature/fts5-ranking` on `~/software/aurasys-memory/`
**Depends on:** Round 1 complete + 2-4 sessions settle-in

**Auditor finding (tested 2026-05-21):** FTS5 MATCH cannot go through a SQLite view.
`CREATE VIEW ... FROM memory_fts` succeeds, but `WHERE view_name MATCH ?` fails with
"no such column." This is a SQLite limitation — MATCH must reference the FTS5 table
directly. Consequence: ranked search is a **query template**, not a view.

**Design:** A helper view `v_fts_confidence` pre-joins FTS5 content metadata with
confidence data. The ranked search query uses this view plus a direct FTS5 MATCH.

**Ranking formula (3-signal, Round 2):**
```
score = (-rank) × 0.4                           -- text relevance (FTS5 BM25, flipped)
      + effective_confidence × 0.35              -- confidence (0-1, from decay)
      + 1/(1 + days_since_access) × 0.2          -- recency (hyperbolic, 0-1)
```
Weights sum to 0.95. The remaining 0.05 (session_refs) adds in Round 4 when the
evidence table exists. Re-weighting to 1.0 is unnecessary — relative ordering
is unchanged.

Note: `-rank` from FTS5 BM25 ranges ~0.01-20 for our corpus. At 0.4 weight,
text relevance contributes 0.004-8.0. Confidence contributes 0-0.35. Recency
contributes 0-0.2. Text relevance dominates by design — search term match is
the primary signal, confidence and recency are tiebreakers.

**Recency source:** `COALESCE(mc.last_accessed, mc.created_at)`. In Round 2,
`last_accessed` is NULL for most records (not yet populated). Falls back to
`created_at` — which for sessions/decisions/breakthroughs uses the semantic
date from seed data (Round 1B fix). For projects/references/people, falls back
to rebuild-time timestamp. Acceptable; improves when access tracking activates.

### Round 2 Implementation

**Create helper view** in `scripts/db-setup/020-views.sql` (at end):
```sql
-- Pre-join FTS5 metadata with confidence for ranked search.
-- Cannot be queried with MATCH directly (SQLite limitation).
-- Used by the ranked search query template in MEMORY.md.
CREATE VIEW v_fts_confidence AS
SELECT mf.source_table, mf.source_id, mf.title, mf.content,
    COALESCE(vmd.effective_confidence, 1.0) AS effective_confidence,
    COALESCE(vmd.last_accessed, vmd.created_at) AS last_active,
    vmd.pinned, vmd.half_life_days
FROM memory_fts mf
LEFT JOIN v_memories_decayed vmd
    ON vmd.source_table = mf.source_table AND vmd.source_id = mf.source_id;
```

**Ranked search query template** (add to MEMORY.md Database section):
```sql
SELECT mf.source_table, mf.source_id, mf.title,
    snippet(memory_fts, 3, '>', '<', '...', 20) as snippet,
    ROUND(-mf.rank * 0.4
        + COALESCE(vmd.effective_confidence, 1.0) * 0.35
        + (1.0 / (1.0 + MAX(0, julianday('now')
            - julianday(COALESCE(vmd.last_accessed, vmd.created_at))))) * 0.2
    , 3) AS score
FROM memory_fts mf
LEFT JOIN v_memories_decayed vmd
    ON vmd.source_table = mf.source_table AND vmd.source_id = mf.source_id
WHERE memory_fts MATCH ?
ORDER BY score DESC
LIMIT 10;
```

**Update:** `scripts/test-schema.sh` — view count +1 (v_fts_confidence).

**Update:** `~/software/aurasys-memory/memory/MEMORY.md` — add ranked query to
Section 3 (Database) query table:
```
| `SELECT ... FROM memory_fts mf LEFT JOIN v_memories_decayed ... WHERE memory_fts MATCH ?` | Ranked search (text × 0.4 + confidence × 0.35 + recency × 0.2) |
```
Replace or augment the existing FTS5 query line. Keep the raw FTS5 query available
for unranked search.

### Round 2 Acceptance Criteria

- `./scripts/rebuild-db.sh` succeeds
- `./scripts/test-schema.sh` passes (view count updated)
- `v_fts_confidence` returns rows with confidence and last_active columns
- Ranked query returns results ordered by composite score
- Pinned items (corrections) show effective_confidence = 1.0 in results
- Old sessions show lower scores than recent ones for same search term
- Raw FTS5 query still works (not broken by view addition)
- MEMORY.md updated with ranked query reference

### Round 2 Git Workflow

1. Tag before: `git tag v0.3.1-pre-fts5-ranking`
2. Branch: `git checkout -b feature/fts5-ranking`
3. Work + commit: `Plan 0360 R2: add ranked FTS5 search with confidence weighting`
4. Tag after: `git tag v0.3.2-fts5-ranking`
5. Merge: `git checkout main && git merge feature/fts5-ranking --no-ff`
6. Clean up: `git branch -d feature/fts5-ranking`

### Round 2 Generator Reference Map

| Concept | Read this file | What to look for |
|---------|---------------|-----------------|
| Current views | `scripts/db-setup/020-views.sql` | End of file (add new view) |
| FTS5 structure | `scripts/db-setup/040-fts5.sql` | FTS5 table definition + column names |
| FTS5 population | `scripts/rebuild-db.sh` lines 41-60 | source_table column values |
| Confidence view | `scripts/db-setup/011-confidence-tables.sql` | v_memories_decayed columns |
| Current MEMORY.md | `memory/MEMORY.md` | Section 3 (Database) query table |
| Existing FTS5 query | `memory/MEMORY.md` | Line with `memory_fts MATCH` |

---

## Phase 4: Propagate Phase 3 to Longmem

**Generator UID:** GEN-0360-P4
**Branch:** `feature/enhanced-memory` on `~/software/longmem/`

### Constraints

- **SQLite ≥ 3.35.0** required for DB-backed mode (GENERATED STORED + math functions).
  File-only mode has no SQLite dependency. Document in architecture.md.
- **protocol.md cap:** 200 lines. Currently 184. Headroom: 16 lines.
  Progressive compression REPLACES §3 (no net increase).
  Write-gate: +4 lines. Novelty detection: +3 lines. Total: ~7 net addition → ~191.
- **directives.md cap:** 140 lines. Currently 139. Headroom: 1 line.
  References only — no additions to directives.md body. Just verify
  compression/write references still accurate after protocol changes.
- **No Argus-specific content.** Template the STRUCTURE, not Bruce's data.

### 4a. protocol.md — three additions

**Current state:** 184 lines, cap 200.

**Step 1 — Replace §3 Compression Rules (lines 42-50, 9 lines → 9 lines, net 0):**

Replace current binary compression with 4-stage model. Session compression
rules (MEMORY.md cap, ROUTINE vs PARADIGM) are PRESERVED alongside the new
memory-file compression stages.

```
## 3. Compression Rules

**Sessions:** MEMORY.md keeps 2 active sessions. Session 3 → session-details.md
(PARADIGM 3-5 lines indefinitely; ROUTINE 2-3 lines; default PARADIGM if unsure).
session-details.md >200 lines → oldest ROUTINE blocks to 2-line entries.
**Never compress:** Identity, Current State, L1 Corrections, Health Metrics, File Map.

**Memory files:** 4-stage progressive compression, dual-trigger (least-compressed wins):
FULL (conf>0.5 OR <30d) → SUMMARY 3-5 lines (>0.2 OR <90d) → ONE-LINER (>0.05 OR <180d) → ARCHIVE (git only).
Pinned items (corrections) exempt. For DB-backed: `SELECT * FROM v_compression_candidates`. Act during maintenance.
```

Preserve the "Overflow" line from current §3 (line 50) if it fits within 200.

**Step 2 — Add §15 Write Gate (after §14, +4 lines):**

```
## 15. Write Gate (substantive writes only — skip mechanical updates)

Before creating or substantially changing a memory file, all must pass:
1. Will this matter in 30+ days? 2. Does existing memory cover this? 3. Derivable from code/git?
4. Contains context I can't reconstruct? 5. Would a future instance behave differently without this?
```

**Step 3 — Add §16 Novelty Gate (after §15, +3 lines):**

```
## 16. Novelty Gate (before creating .md memory files)

1. Exact match: `ls .longmem/memory/*-SLUG-*.md` — if exists, UPDATE don't create.
2. FTS5 check (DB-backed): `SELECT title, ROUND(-rank,1) FROM memory_fts WHERE memory_fts MATCH 'KEY TERMS' LIMIT 3` — if rank>10.0, flag overlap. File-only: grep for key terms across memory/*.md.
```

**Step 4 — Verify:** `wc -l` must show ≤ 200. If over, compress §12 or §13 further.

### 4b. architecture.md — three new sections

Add after "Associations & Relationships" (line ~381), before "Landscape Context":

**Section: "Confidence Decay (DB-backed mode)"** (~20 lines)
- Ebbinghaus-inspired exponential decay model
- Per-type half-lives: corrections=pinned, feedback=90d, projects=60d,
  sessions=30d, references=180d, people=365d, breakthroughs=180d, decisions=90d
- Schema: `memory_confidence` table (metadata overlay pattern)
- View: `v_memories_decayed` with `effective_confidence` column
- Structure-not-control: `decay_rate` is GENERATED STORED, branchless formula
- SQLite ≥ 3.35.0 requirement
- File-only users: track staleness manually or via git timestamps

**Section: "Evidence & Provenance (DB-backed mode)"** (~10 lines)
- Append-only `memory_evidence` table
- Five kinds: established, violated, referenced, observed, corrected
- Seeds from existing data (correction dates)
- Provides audit trail for confidence scores

**Section: "Ranked Search (DB-backed mode)"** (~10 lines)
- FTS5 MATCH limitation (can't go through views)
- Multi-signal formula: text × 0.4 + confidence × 0.35 + recency × 0.2
- Query template (not view) — copy from Argus MEMORY.md
- `v_fts_confidence` helper view for pre-joining

**Read Argus files for reference (Generator reads these to understand the concepts):**

| Concept | Read this Argus file |
|---------|---------------------|
| Confidence schema | `~/software/aurasys-memory/scripts/db-setup/011-confidence-tables.sql` |
| Evidence schema | `~/software/aurasys-memory/scripts/db-setup/012-evidence-tables.sql` |
| FTS5 ranking view | `~/software/aurasys-memory/scripts/db-setup/020-views.sql` (end — v_fts_confidence, v_compression_candidates) |
| Ranked query | `~/software/aurasys-memory/memory/MEMORY.md` line 38 |
| Compression stages | `~/software/aurasys-memory/memory/protocol.md` §4 |
| Write gate | `~/software/aurasys-memory/memory/protocol.md` §15 |
| Novelty gate | `~/software/aurasys-memory/memory/protocol.md` §16 |

### 4c. CHANGELOG.md

Add v2.1.0 entry above v2.0.0:

```markdown
## [2.1.0] — 2026-05-21

### Added
- Progressive compression: 4-stage model (FULL/SUMMARY/ONE-LINER/ARCHIVE) with confidence-based decay
- Write gate: 5-question pre-write check (protocol.md §15)
- Novelty gate: duplicate detection before memory creation (protocol.md §16)
- Confidence decay documentation for DB-backed mode (architecture.md)
- Evidence/provenance documentation for DB-backed mode (architecture.md)
- Ranked FTS5 search documentation for DB-backed mode (architecture.md)

### Changed
- Compression rules: binary keep/archive → 4-stage progressive (protocol.md §3)
```

### 4d. README.md

- Add "Confidence Decay", "Write Gate", "Novelty Detection" to the features
  list or "What's Included" section. One line each, not paragraphs.
- Do NOT restructure or rewrite the README — minimal additions only.

### 4e. directives.md

- Verify compression references (line ~27, ~42, ~95) still work with new §3.
  Current references say "read protocol.md Section 3" — section number unchanged.
- If wording needs adjustment (e.g., "compress" → "check compression stage"),
  make minimal edits. Stay ≤ 140 lines.

### 4f. Tests

- Regenerate `.longmem/.file-hashes` for all changed files
- Run `tests/run-all.sh` — all 3 tests must pass
- If test-hashes baselines need updating, update them

### 4g. Tag and commit

```bash
git tag v2.1.0 -m "Add Phase 3 features: confidence decay, progressive compression, write-gate, novelty detection"
```

**Commits (Generator's judgment on split, suggested):**
1. `Update protocol.md: progressive compression, write-gate, novelty detection`
2. `Update architecture.md: confidence decay, evidence, ranked search`
3. `Update docs: CHANGELOG, README, directives review`
4. `Update tests: regenerate hashes`

Or combine into 2 logical commits if cleaner.

### Phase 4 Acceptance Criteria

- protocol.md ≤ 200 lines
- protocol.md has §3 (4-stage), §15 (write-gate), §16 (novelty gate)
- architecture.md has confidence decay, evidence, ranked search sections
- CHANGELOG has v2.1.0 entry
- README mentions new features
- directives.md ≤ 140 lines, compression references still valid
- `tests/run-all.sh` passes (3/3)
- No Argus-specific content (no Bruce, no corrections data, no people, no campaigns)
- v2.1.0 tag ready
- `grep -ri "bruce\|argus\|relinquishment\|healer\|genevieve\|custodian\|snailmail\|energyscholar\|hacktivismo\|dignity.net" .longmem/ README.md` → only author attribution

### Phase 4 Git Workflow

1. Tag before: `git tag v2.0.1-pre-phase4`
2. Branch: `git checkout -b feature/enhanced-memory`
3. Work + commits
4. Tag after: `git tag v2.1.0`
5. Merge: `git checkout main && git merge feature/enhanced-memory --no-ff`
6. Clean up: `git branch -d feature/enhanced-memory`

---

## Phase 5: End-to-End Validation

**Purpose:** Verify the template actually works for a new user.

### 5a. Fresh-clone test

```bash
cd /tmp
git clone ~/software/longmem test-longmem-project
cd test-longmem-project
# Edit MEMORY.md with test project info
# Run memory-sync.sh
# Verify bootstrap
```

### 5b. Day-1-through-Day-5 scenario walkthrough

Manually verify the progressive disclosure works:
- Session 1: MEMORY.md + corrections.md loads, basics work
- Session 3: First tutorial PTL item appears (Pattern 1: planning)
- Session 5: Corrections accumulate, health vector computes correctly

### 5c. DB-backed mode upgrade test

Starting from a file-only installation after ~5 sessions:
- Follow migration guide in architecture.md
- Verify DB builds from existing .md files
- Verify FTS5 search works
- Verify health auto-compute works

### 5d. Verify no Argus leak

```bash
grep -ri "bruce\|argus\|relinquishment\|healer\|genevieve\|custodian\
  \|snailmail\|energyscholar\|hacktivismo\|dignity.net" \
  ~/software/longmem/.longmem/ ~/software/longmem/README.md \
  ~/software/longmem/CONTRIBUTING.md
```

Only legitimate hits: energyscholar in README contact info and CONTRIBUTING.

**Acceptance criteria:**
- Fresh clone bootstraps correctly
- Progressive disclosure triggers at correct session counts
- DB upgrade path works from file-only state
- No Argus-specific content in template (except author attribution)

**No commit — validation only.**

### Phase 5 Results (S96)

- **5a Fresh clone:** PASS. Clone → memory-sync.sh → tests/run-all.sh 3/3.
- **5b Scenario walkthrough:** PARTIAL. Verified template structure, §3/§15/§16
  present, architecture sections present. Full day-1-through-5 requires multi-session
  usage — not automatable in one pass.
- **5c DB-backed upgrade:** NOT TESTED. Requires manual SQLite setup + ingest
  pipeline configuration. Architecture.md documents the path. Deferred to first
  external user report.
- **5d OPSEC leak check:** PASS with known exceptions. "Bruce Stephenson" and "Argus"
  appear in case-study.md only (author attribution — legitimate, pre-existing from v2.0.0).
  No other Argus-specific content leaked.
- **Finding:** 4 template files have CRLF line endings (corrections.md, decisions.md,
  people.md, session-details.md). Pre-existing from v2.0.0. Non-blocking.

---

## Risk Register

| # | Risk | Phase | Severity | Mitigation |
|---|------|-------|----------|------------|
| R1 | Protocol.md line cap exceeded | 2, 4 | HIGH | Compress tutorials/threads first. Measure before adding. Split file if needed. |
| R2 | Survey features in Phase 2 (template ahead of production) | 2 | HIGH | Scope rule: Phase 2 = Argus parity only. Survey features → Phase 3/4. |
| R3 | CRLF diff noise obscures real changes | 1 | MEDIUM | Separate commit for CRLF fix, before other changes. |
| R4 | Confabulated stats in case study | 2 | MEDIUM | Phase 0d records verified stats. Generator uses those, not memory. |
| R5 | "Why not a database?" reversal breaks trust | 2 | MEDIUM | Frame as evolution, not reversal. File-only is still the default. |
| R6 | `associations` table rebuild loses data | 3 | MEDIUM | Only 4 rows. Backup before rebuild. Verify count after. |
| R7 | ~~access_count on read path~~ | 3 | RESOLVED | Eliminated: use `last_accessed` timestamp only, derive frequency from evidence table (Round 4). |
| R8 | Existing longmem users can't upgrade cleanly | 2 | LOW | CHANGELOG + architecture.md migration section. No breaking changes to file format. |
| R9 | Non-existent `memories` table referenced in schema changes | 3 | HIGH | Fixed: use metadata overlay table, not ALTER on non-existent table. |
| R10 | Phase 1 checksums invalidated by Phase 3 | 1→3 | LOW | Acceptable: Phase 3 updates checksums as part of its work. |
| R11 | FTS5 similarity threshold for novelty detection is arbitrary | 3 | LOW | Set empirically. Document as tunable. |
| R12 | Schema load ordering: views reference tables not yet created | 3 | RESOLVED | Fixed: `011-confidence-tables.sql` loads between 010 and 020. |
| R13 | Division by zero in decay formula | 3 | RESOLVED | Structure-not-control: `decay_rate` generated column, branchless `exp()` formula. |
| R14 | `v_stale_projects` semantic change | 3 | RESOLVED | Add confidence column informational only. Don't change WHERE clause. |
| R15 | ~~Column name mismatch in seed SQL~~ | 3 | RESOLVED | Verified: all 8 tables have `created_at`. Real issue was semantic dates (see R16). |
| R16 | Seed uses `created_at` which resets on rebuild | 3 | MEDIUM | Fixed: use COALESCE with semantic dates (established, date) where available. Accept reset for projects/references/people (long half-lives). |
| R17 | `SELECT *` with LEFT JOIN leaks mc columns into views | 3 | RESOLVED | Fixed: plan specifies `SELECT <alias>.*` not bare `*`. Verified by test. |
| R18 | SQLite version too old for GENERATED columns / math functions | 4 | LOW | Phase 4 docs note ≥ 3.35.0 requirement. Not a Round 1 issue (Argus = 3.40.1). |

---

## Contingency Plan

### Before ANY schema change (Phases 1, 3):
```bash
cp ~/software/aurasys-memory/argus.db ~/software/aurasys-memory/argus.db.pre-PHASE
```

### If DB migration fails:
1. Restore backup: `cp argus.db.pre-PHASE argus.db`
2. Schema is deterministic: `./scripts/rebuild-db.sh` rebuilds from SQL scripts
3. All data lives in `scripts/data/*.sql` — nothing is DB-only

### If longmem template breaks (Phases 2, 4):
1. `git revert` on longmem repo
2. Fresh clone test: `git clone ... && cd ... && bash .longmem/scripts/memory-sync.sh`
3. If tag exists, `git checkout v1.0.0` for known-good state

### If ingest pipeline breaks:
1. .md files are upstream (source of truth)
2. `./scripts/rebuild-db.sh` is idempotent
3. `./scripts/ingest-memories.sh` can re-run safely

### Rollback order:
Phase 5 (validation, no changes) → Phase 4 (longmem v2.1.0) →
Phase 3 (Argus enhancements) → Phase 2 (longmem v2.0.0) →
Phase 1 (Argus bug fixes) → Phase 0 (tags, no changes)

Each phase is independently revertible via `git revert` on its branch.
Tags at Phase 0 (v1.0.0) and Phase 2 (v2.0.0) provide stable rollback points.

---

## Generator Execution Order

| Phase | UID | Sessions | Rating | Risk | Status |
|-------|-----|----------|--------|------|--------|
| 0 | GEN-0360-P0 | 1 (short) | 98% | NONE | ✓ DONE |
| 1 | GEN-0360-P0P1 | 1 | 95% | LOW | ✓ DONE (2 commits) |
| 2A | GEN-0360-P2A | 1 | 90% | MEDIUM | ✓ DONE (2 commits) |
| 2B | GEN-0360-P2B | 1 | 90% | MEDIUM | ✓ DONE (4 commits, v2.0.0 tagged+pushed) |
| 3-R1A | GEN-0360-R1A | 1 (short) | 94% | LOW — text edit | ✓ DONE (S91, commit b0e90b1) |
| 3-R1B | GEN-0360-R1B | 1 | 93% | MEDIUM — schema | ✓ DONE (S91, commit 73c469f) |
| 3-R1C | GEN-0360-R1C | 1 | 92% | MEDIUM — views | ✓ DONE (S91, commit 0f4d729, merged 5b65cd4) |
| 3-R2 | GEN-0360-R2 | 1 | 95% | LOW — 1 view + query | ✓ DONE (S96, commit 14949bc, merged 6cb6b3f) |
| 3-R3 | GEN-0360-R3 | 1 | 96% | LOW — protocol edit + 1 view | ✓ DONE (S96, commit e93392e, merged cc47c11) |
| 3-R4 | GEN-0360-R4 | 1 | 94% | MEDIUM — new table + seed | ✓ DONE (S96, commit cb02eff, merged 209a420) |
| 3-R5 | GEN-0360-R5 | 1 | 96% | LOW — protocol edit only | ✓ DONE (S96, commit 10b9dee, merged 2f34485) |
| 4 | GEN-0360-P4 | 1 | 91% | MEDIUM — 5 files, template work | ✓ DONE (S96, 4 commits, merged 06438a2, v2.1.0 tagged) |
| 5 | (Auditor) | 1 | 95% | NONE | ✓ DONE (S96, validation passed, see notes below) |

**Phase 3 Round 1:** COMPLETE. Merged to main (5b65cd4). Tag: v0.3.0-confidence-r1.
Settle-in: S91 → S94, S95, S96 (3 sessions). No issues found.

**Total estimated:** 12–15 Generator sessions across all phases.
Phases 0 and 5 can be done in Auditor shell (no implementation).

---

## Successor Plan

After Plan 0360 completes (longmem at parity, Argus enhanced, validated):

**Plan 0362: Three-Axis Governance Integration Evaluation**

Evaluate building a single repo that integrates all three governance axes
(memory + ethical + structural) into one system. This is a PRODUCT DECISION,
not a propagation task. See `plans/0362-three-axis-governance-evaluation.md`.

Plan 0360 deliverables feed into 0362:
- Phase 2 (longmem v2.0.0) = the memory axis, proven and public
- Phase 3 (Argus enhancements) = best-of-survey memory, validated
- DN spec = the ethical axis, proven in Argus
- Triad + operators = the structural axis, proven in Argus
- 0362 evaluates whether and how to merge them into one repo
