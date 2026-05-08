# Plan 0308: Aurasys-Memory Retrofit — SQLite + Layered Index

**Status:** BLOCKED — waiting for Bruce to verify and tune the Traveller reference system (Plan 0299).  
**Priority:** TOP — Bruce: "We're upgrading your memory so you make fewer errors and perform better."  
**Prerequisite:** Plan 0299 data migration complete, stress-tested, and tuned by Bruce.  
**Source:** Plan 0299 execution (S67-S68), PHASE-3-REPORT.md recommendations, project-0299-execution-results.md lessons.  
**Estimated effort:** 4-6 sessions (process proven on Traveller, but larger data and higher stakes).

---

## Why This Plan Exists

The current memory system is 164 flat markdown files totaling ~8100 lines. MEMORY.md (177 lines) serves as an always-loaded index, but it mixes index entries with content, approaches its 180-line cap, and provides no queryable access to structured data. After context compaction, Argus loses access to facts stored in files not yet read — the same failure mode that caused 5 confabulations in the Traveller B1 baseline.

Plan 0299 proved the fix: SQLite + L1 always-loaded index + anti-confab guardrails. Confabulations dropped from 5 to 0. Compaction resilience proven (P4 = P3). Voice quality 4/5 → 5/5. This plan applies the same architecture to Argus's core memory system.

**Critical difference from Plan 0299:** The Traveller system is one skill's reference data. Aurasys-memory is Argus's operating system — a bug here affects ALL conversations across ALL projects. Every phase must be rollback-safe.

---

## Lessons from Plan 0299 (Traveller Testbed)

These lessons are proven — each was validated with baseline measurements and quantitative results. They are NOT optional guidelines; they are engineering constraints for this plan.

### 1. Baseline-First Methodology (NON-NEGOTIABLE)

Measure the current system before building anything. Without B1's 5 confabulations we couldn't prove the new system's 0. The Traveller baselines (B0-B3) took ~30 minutes and provided the entire justification for the project.

**For this plan:** Design baselines that measure memory recall accuracy, compaction resilience, cross-project context switching, and protocol compliance.

### 2. L1 Always-Loaded Index

Single entry point that survives compaction. Contains: anti-confab list (corrections hot five), DB pointer, mode profiles, checksums. The anti-confab list at the TOP of L1 is THE critical guardrail — P4 compaction test proved this. Without it, post-compaction quality degrades.

**For this plan:** MEMORY.md already serves this role but is bloated (177 lines, mixed content). Redesign it as a pure index with DB pointer, hot corrections, mode profiles, and nothing else.

### 3. DB-First for Facts

Any datum that can be wrong (names, types, quantities, dates, relationships) goes in a queryable store. Prose is for voice, methodology, and templates — never facts. The B1/B2 Traveller failures were ALL "Generator trusted stale flat file over authoritative source."

**For this plan:** People names/roles, correction details, project states, session dates, PTL items — all structured data that currently lives in flat files and can drift or fragment.

### 4. Source File Specification in Prompts

Iter 1 named every source file with full paths. Generator didn't hunt. Compare to B2 baseline where Generator hunted across 11 files with 15% waste. Every Generator prompt must say exactly what to read.

### 5. Mode-Specific Loading

Don't load everything. L1 directs what subset to load per task type. Traveller prep doesn't need post-game voice guides. For aurasys-memory: book work doesn't need magnetogenesis context. MS science doesn't need book navigation architecture.

### 6. Checksum Verification (Four-Layer Chain)

Prose checksums in L1 detect drift. verify-integrity.sh automates this. Apply to memory files that stay flat (protocol.md, bruce-se-methodology.md, dignity-net.md, CLAUDE.md at `~/.claude/CLAUDE.md`).

**Verification is LAZY** — checksums are checked when a file is about to be loaded, not at session start. This avoids wasting tool calls reading files that won't be used. If mismatch: flag `[CHECKSUM DRIFT]` to Bruce, load the file anyway (assume the edit was intentional, but verify).

**Four layers:**
1. **L1 (MEMORY.md):** Stores `[sha:XXXXXX]` for each flat file that stays. Verified on load.
2. **MANIFEST.md files:** Store `[sha:XXXXXX]` for each SQL script. Verified by verify-integrity.sh.
3. **reference-landmarks.md:** Stores `[sha:XXXXXX]` for each MANIFEST.md. Top of the chain.
4. **DB integrity:** `PRAGMA integrity_check` + `PRAGMA foreign_key_check` + row count verification. Run by test suite.

### 7. INSERT OR REPLACE for Idempotency

Data scripts are re-runnable. DB can be destroyed and rebuilt from scripts alone. Identical result every time. This is the source-of-truth guarantee.

### 8. Iterative Development with Deferred Prompts

Write later iteration prompts AFTER earlier iterations complete, incorporating lessons learned. The ef_calls target (≤8) was wrong — caught at Iter 2 and adjusted. Pre-writing all prompts would have baked in the error.

### 9. ≤8 File Reads, DB Queries Uncapped

The right metric is file reads (expensive, context-consuming), not total tool calls. DB queries are the RIGHT behavior — fast, precise, no context pollution.

### 10. Generator Prompts ≤8 Lines

Detailed instructions in .md files. Generator prompt references the file. Bruce copies ≤8 lines into fresh shell.

---

## Generalization Strategy: Narrow Domain → Open Domain

The Traveller system had a bounded domain: NPCs, ships, plot threads, 3 task modes (prep/live/post). Aurasys-memory serves an unbounded domain: book work, magnetospheric science, Traveller GM, memory maintenance, job search, collaboration, general questions. This section addresses how the Traveller architecture generalizes.

### Problem 1: Unbounded Entity Types

**Traveller:** Fixed schema — every NPC has name, species, status, entity_type. The columns are known in advance.  
**Memory:** Feedback rules, project context, people profiles, corrections, user preferences — each has different structure. No single schema fits all.

**Solution:** Per-type tables with type-specific columns PLUS a general `content` TEXT field. The structured columns capture what CAN be queried (slug, status, established date, last_triggered, compaction_tag). The content field holds the full prose for anything that doesn't decompose into columns. This avoids both over-normalization (100 sparse columns) and under-normalization (one big blob table).

Example: `feedback` table has `slug, rule, why, how_to_apply, established, last_triggered, source, compaction_tag` — but `rule` and `why` are still prose. The DB makes them findable; the prose makes them readable.

### Problem 2: Multi-Mode Task Space

**Traveller:** 3 modes, mutually exclusive. Prep never needs post-game voice.  
**Memory:** ~5 modes, but tasks often SPAN modes. "Review Plan 0295 and update the book" touches book work + memory maintenance. "What did Merkin say, and how does it affect the magnetogenesis paper?" spans people + science + references.

**Solution:** Mode profiles are ADVISORY, not restrictive. L1 says "for book work, load these first" — but doesn't prohibit loading science context if the task requires it. The key insight from Traveller: mode-specific loading reduced waste from 15% to 0%. For memory, the waste reduction comes from NOT loading 57 feedback files when you only need 3, not from hard boundaries.

**Implementation:** L1 mode profiles list primary DB queries per mode. Example: book mode → `SELECT * FROM feedback WHERE domain='book'` + `SELECT * FROM v_active_projects WHERE domain='book'` + corrections hot five + people tier 1. If the task spans modes, run queries from both. Domain is a proper column with CHECK constraint, not a filename prefix pattern.

### Problem 3: Cross-Cutting Queries

**Traveller:** "What ships does Anemone crew?" — one join, one domain.  
**Memory:** "What do I know about Merkin?" — spans people + projects + references + sessions + pending. This is the query type that flat files handle worst (grep across 164 files) and DB handles best (joins across tables).

**Solution:** Cross-entity views. `v_person_context(name, role, projects, references, last_session, pending_items)` joins across tables so a single query returns everything Argus knows about a person. Same pattern for: "What's the state of the book?" → `v_project_summary` joins projects + PTL + recent sessions filtered by domain.

### Problem 4: Behavioral vs Factual Data

**Traveller:** All data is factual — NPC names, ship tonnage, plot status. Either right or wrong.  
**Memory:** Feedback rules are BEHAVIORAL — "don't mock the database in tests." Corrections are factual — "Anemone is human." Projects are contextual — "book release target ~May 19." These need different handling.

**Solution:** The `type` column in the schema distinguishes behavioral (feedback), factual (corrections, people), contextual (projects, decisions), and temporal (sessions). The L1 loading strategy differs by type:
- Factual: always load hot items (corrections L1, people tier 1)
- Behavioral: load by domain match (book feedback for book tasks)
- Contextual: load by recency + relevance (active projects only)
- Temporal: load on demand (session history queried, not pre-loaded)

### Problem 5: Unknown Confabulation Patterns

**Traveller:** Known hot list — Anemone's species, Astral Dawn tonnage, FTL comms prohibition. We built the hot list BEFORE the DB.  
**Memory:** We don't systematically track what Argus gets wrong about non-Traveller domains. The corrections system (23 items) covers the book/Healer domain. But there's no equivalent for: MS science confabulations, book build system errors, protocol compliance failures.

**Solution:** Phase 0 baselines will DISCOVER the confabulation patterns for the broader domain. B1-B4 are designed to find what breaks. The hot list for L1 will be built from baseline results + existing corrections, not assumed in advance. This is the baseline-first methodology applied to an unknown domain.

### Problem 6: Temporal Dynamics

**Traveller:** Campaign data changes slowly (session to session). An NPC's species never changes.  
**Memory:** Projects have lifecycles (created → active → stale → archived). Feedback rules can be superseded. Sessions are append-only. PTL items move between tiers. Pending items decay.

**Solution:** Status fields + timestamp fields + decay views. `v_stale_projects` automatically surfaces items past decay threshold. `v_ptl_stale` does the same for PTL. Health metrics computed from DB state, not manually tracked. The protocol.md decay rules (Section 5) become SQL queries instead of prose instructions.

### Summary: What Changes, What Stays

| Aspect | Traveller | Memory | Change |
|--------|-----------|--------|--------|
| Entity types | Fixed (5) | Variable (12+) | Per-type tables with content field |
| Modes | 3, exclusive | 5+, overlapping | Advisory profiles, multi-mode queries |
| Cross-entity queries | Rare | Common | Cross-entity views |
| Data nature | All factual | Mixed behavioral/factual/temporal | Type column, different loading strategies |
| Confab patterns | Known in advance | Discovered via baselines | Baseline-first, dynamic hot list |
| Temporal dynamics | Slow/static | Fast lifecycle + decay | Status/timestamp fields, decay views |
| L1 hot list | Domain-specific | corrections.md (exists) | Corrections already proven; extend to other domains |

---

## Current System Inventory

**164 files in memory/, breakdown:**
| Type | Count | Examples |
|------|:-----:|---------|
| feedback-*.md | 57 | Rules about how to approach work |
| project-*.md | 66 | Project state, context, decisions |
| reference-*.md | 13 | Pointers to external resources |
| user-*.md | 9 | Bruce's profile, preferences, skills |
| Core files | 12 | MEMORY.md, corrections.md, people.md, pending.md, decisions.md, protocol.md, session-details.md, ptl.yaml, breakthroughs.md, correction-graph.md, traveller-campaign.md, projects.md |
| Other | 7 | gen-*, claude-version-history, skill-ms-science, bruce-se-methodology |

**Largest files:**
| File | Lines | Content |
|------|:-----:|---------|
| ptl.yaml | 2186 | 103 prioritized task items |
| corrections.md | 280 | 23 numbered corrections with metadata |
| session-details.md | 207 | Session history (needs compression) |
| protocol.md | 189 | Self-maintenance rules |
| MEMORY.md | 177 | Always-loaded index |
| people.md | 189+ | People registry, 3 tiers |

---

## Architecture Design

### What Goes in DB (Structured Data)

| Current Source | DB Table | Rows (est.) | Why DB |
|----------------|----------|:-----------:|--------|
| corrections.md | `corrections` | 23 | Numbered, cross-referenced, has dates/types/clusters. Currently requires full-file read for any lookup. |
| correction-graph.md | `correction_connections` | ~40 | Junction table. Currently a separate prose file duplicating correction data. |
| people.md + people-merkin.md | `people` | ~50 | Tiered, has roles/relationships/handles. Currently grep-only. |
| feedback-*.md (57 files) | `feedback` | ~57 | Each is a rule with why/how-to-apply. Currently requires reading individual files. |
| project-*.md (66 files) | `projects` | ~66 | Each is a project fact with why/how-to-apply. Currently requires reading individual files. |
| reference-*.md (13 files) | `references` | ~13 | Each is a pointer with description. Simple lookup table. |
| user-*.md (9 files) | `user_profile` | ~9 | Bruce's attributes. Rarely changes, frequently needed. |
| session-details.md | `sessions` | ~67 | Time-series. Currently requires full-file read, approaching 200-line cap. |
| decisions.md | `decisions` | ~20 | Dated decisions with rationale. Currently mixed in one file. |
| breakthroughs.md | `breakthroughs` | ~15 | Capped set with active/killed status. |
| ptl.yaml | `ptl_items` | ~103 | Already structured (YAML). Natural DB candidate. |
| pending.md | `pending_items` | ~27 | Outreach + awaiting items with decay. |

### What Stays Flat (Structural/Prose)

| File | Why Flat |
|------|----------|
| MEMORY.md | L1 index — always loaded, must be readable without DB. Redesigned to be pure index. |
| protocol.md | Behavioral rules, lazy-loaded. Prose by nature. |
| protocol-snailmail.md | Behavioral rules for specific channel. |
| CLAUDE.md | Claude Code directives. System-level, not project data. |
| dignity-net.md | Governance spec. Versioned prose. |
| bruce-se-methodology.md | Methodology reference. Prose patterns, not facts. |
| skill-ms-science.md | Domain knowledge. Prose patterns. |
| traveller-campaign.md | Pointer to Traveller system (which has its own DB). |

### Schema Overview

**DB path:** `~/software/aurasys-memory/argus.db` (parallel to `traveller-reference/campaign.db`)  
**Pragmas:** WAL mode (concurrent read safety), FK enforcement, journal_size_limit

```
-- Core tables (all include created_at, updated_at auto-timestamps)
corrections(id, number, title, context, type, depth, cluster, source,
            domain, established, last_violated, notice,
            created_at, updated_at)
people(id, name, tier, role, relationship, description, email, handles,
       status, tier_notes, created_at, updated_at)
feedback(id, slug, rule, why, how_to_apply, content,
         established, last_triggered,
         source, domain, compaction_tag, source_file,
         created_at, updated_at)
projects(id, slug, name, status, description, why, how_to_apply, content,
         domain, compaction_tag, source_file,
         created_at, updated_at)
references(id, slug, name, path_or_url, description, source_file,
           created_at, updated_at)
user_profile(id, slug, attribute, value, context,
             created_at, updated_at)
sessions(id, number, date, significance, register,
         summary, reconstruction_priority, handoff,
         created_at, updated_at)
session_themes(session_id, theme)  -- multi-valued, not comma-separated
decisions(id, topic, decision, rationale, date, status,
          created_at, updated_at)
breakthroughs(id, title, description, status, date, killed_date,
              killed_reason, created_at, updated_at)
ptl_items(id, stable_id, title, tier, status, owner, created,
          last_touched, decay_exempt, description, detail_file,
          created_at, updated_at)
pending_items(id, description, status, tier, created, last_touched,
              category, created_at, updated_at)

-- Junction/relationship tables
correction_connections(correction_id, connected_id, relationship)
person_projects(person_id, project_slug)

-- Operational
health_snapshots(id, session_number, date, pressure, freshness,
                 coverage, drift, notes, created_at)
ingest_log(id, source_file, table_name, action, timestamp)
```

**CHECK constraints (all enforced):**
- corrections.type: 'domain', 'epistemic', 'architecture', 'identity'
- corrections.depth: 'routing-change', 'nuance', 'addition'
- corrections.cluster: 'orientation', 'epistemic', 'technical', 'identity'
- feedback.domain: 'book', 'science', 'traveller', 'se', 'memory', 'general'
- projects.domain: same as feedback.domain
- projects.status: 'active', 'stale', 'archived', 'blocked', 'complete'
- sessions.significance: 'PARADIGM', 'ROUTINE'
- breakthroughs.status: 'active', 'killed'
- ptl_items.tier: 'T1', 'T2', 'T3', 'T4', 'T5'
- ptl_items.status: 'active', 'blocked', 'stale', 'done', 'dropped'
- pending_items.tier: 'NOW', 'SOON', 'LATER'

**Concurrent access:** rebuild-db.sh builds to `argus.db.new`, verifies, then atomic `mv argus.db.new argus.db`. Existing readers continue on old file via open descriptor. WAL mode ensures concurrent reads never block.

**source_file column:** Tracks which .md file generated each row. Enables: (a) "which rows came from this file?" queries, (b) staleness detection — if .md file changed but row didn't, ingest is needed.

### Views

| View | Purpose |
|------|---------|
| `v_hot_corrections` | L1 hot five corrections (current rotation from protocol.md §7) |
| `v_correction_cluster` | Corrections grouped by cluster with connection count |
| `v_active_projects` | Non-archived projects with domain, sorted by last activity |
| `v_stale_projects` | Projects past decay threshold (3wk stale, 6wk archive) |
| `v_ptl_active` | T1+T2 items, sorted by tier then priority |
| `v_ptl_stale` | Items past per-tier decay thresholds (per protocol.md §10) |
| `v_recent_sessions` | Last 10 sessions with significance flags and themes |
| `v_paradigm_sessions` | All PARADIGM sessions (never compressed) |
| `v_health_current` | Latest health snapshot with vector components |
| `v_people_active` | Tier 1+2 people with roles and relationship |
| `v_feedback_by_domain` | Feedback rules grouped by domain, sorted by last_triggered |
| `v_memory_stats` | Row counts per table (replaces manual health tracking) |
| `v_person_context` | Cross-entity: person + their projects + references + last session mention |
| `v_project_summary` | Cross-entity: project + related PTL items + recent sessions + feedback rules |
| `v_ingest_recent` | Most recent ingest_log entries per source_file (used by ingest script to detect staleness) |

### Triggers

| Trigger | Purpose |
|---------|---------|
| Auto-timestamp created_at/updated_at on all tables | Consistent timestamps |
| Corrections count check | Enforce 23-item invariant (warn, don't reject) |
| PTL item_count sync | Auto-update count when items added/removed |
| Session significance default | Default PARADIGM if not specified |
| Feedback compaction_tag enforcement | NEVER COMPACT tags preserved |
| Health vector auto-compute | Derive from current state on snapshot insert |

### L1 Redesign (MEMORY.md)

Current MEMORY.md is 177 lines, mixing index, content, session summaries, health metrics, and narrative. Redesign to pure index:

```
## MEMORY.md L1 structure (target: ≤140 lines)

1. Identity + role (5 lines)
2. Anti-confab hot five — static text, updated when rotation changes (10 lines)
3. DB pointer + common queries (15 lines)
4. Mode profiles — what to load + which DB queries per task type (20 lines)
5. File map — flat files that remain, with [sha:XXXXXX] checksums (15 lines)
6. Current state — one-line summary per domain, with query template for detail (15 lines)
7. Active sessions — 2 slots, 8 lines each max (16 lines)
8. Health metrics — query template: SELECT * FROM v_health_current (5 lines)
9. The Story — compressed essential context (15 lines)
10. Cross-project notes (10 lines)
11. Bruce Stephenson — essential profile (10 lines)
```

**≤140 not ≤120:** The Traveller L1 is 148 lines for a single domain. Memory L1 serves ALL domains — forcing 120 would over-compress essentials. 140 is a 21% reduction from 177, and every line saved is context freed for actual work.

**"Current state" design:** L1 has a one-line summary per domain ("Book: polish phase, release ~May 19") that survives compaction PLUS a query template (`SELECT * FROM v_active_projects WHERE domain='book'`) for precision on demand. The one-liner is static text updated at session end; the query gives live detail.

**Anti-confab hot five:** These are STATIC TEXT in L1, not DB query results. The whole point of the hot list is that it's in context before any tool call. The corrections TABLE stores all 23; L1 hardcodes the top 5 for zero-tool-call access. Update L1 when rotation changes (protocol.md §7).

**Key change:** Content that's currently IN MEMORY.md (corrections text, session details, project summaries, Open Threads) moves to DB. MEMORY.md becomes pointers + guardrails + essential compressed context.

### Mode Profiles

| Mode | Load | Don't Load |
|------|------|------------|
| Book work | corrections, breakthroughs, `WHERE domain='book'` projects + feedback | MS science, Traveller, job leads |
| MS / Science | skill-ms-science, `WHERE domain='science'` projects + feedback | Book navigation, Traveller |
| Traveller | traveller-campaign.md → Traveller L1 → campaign.db | Book projects, MS science |
| Memory maintenance | protocol.md, health views, stale item views | Domain-specific anything |
| General / No role | corrections hot five, people active, PTL active | Domain-specific prose |

---

## Write Path: How New Memories Reach the DB

**Problem:** Claude Code's auto-memory system writes .md files with YAML frontmatter. It cannot write SQL or call sqlite3. This is hardcoded in the system prompt — CLAUDE.md cannot override it. After the retrofit, the DB needs new data too, or it goes stale.

**Solution: .md files as write buffer, DB as read cache.**

```
Auto-memory writes .md file (native, unchanged)
  → ingest-memories.sh parses frontmatter + content
  → generates/updates SQL data scripts
  → rebuild-db.sh produces argus.db
```

**ingest-memories.sh** (new script, Phase 1 deliverable):
1. Scans `memory/*.md` for files with YAML frontmatter
2. Parses: `name`, `description`, `type` from frontmatter; body content
3. Derives `slug` from filename (e.g., `feedback-db-scripted-setup.md` → `db-scripted-setup`)
4. Derives `domain` from filename prefix patterns or content keywords
5. Extracts `**Why:**` and `**How to apply:**` lines from body (if present)
6. Generates INSERT OR REPLACE statements for the appropriate table
7. Appends to the correct data script (e.g., `data/013-feedback.sql`)
8. Handles apostrophe escaping (`'` → `''`)

**When to run:**
- **Session start:** Ingest any .md files written since last sync (catches memories from previous sessions)
- **Session end:** Part of memory-sync.sh pipeline (ingest → rebuild → verify → commit)
- **On demand:** After Bruce says "remember X" and wants it queryable immediately

**Steady-state lifecycle:**
1. Auto-memory writes `memory/feedback-new-rule.md`
2. Auto-memory adds line to MEMORY.md
3. At session end, `ingest-memories.sh` parses the file, appends SQL to data script
4. `rebuild-db.sh` produces updated argus.db
5. Next session: DB query finds the new rule
6. After verification period: .md file can be archived (data script is source of truth)

**Source of truth hierarchy:**
- SQL data scripts are the canonical source (committed, versioned, deterministic)
- .md files are the upstream input that generates the data scripts
- argus.db is a derived build artifact (like campaign.db in Traveller)
- If DB and data script disagree: rebuild from scripts
- If data script and .md file disagree: .md file wins (it's upstream)

### Parser Script for Bulk Migration (Phase 1 Deliverable)

**ingest-memories.sh** also handles Phase 2's bulk migration. For the initial 145-file migration:

```bash
# Example: ingest all feedback files
./ingest-memories.sh --type feedback --glob "memory/feedback-*.md" --output data/013-feedback.sql

# Example: ingest all project files  
./ingest-memories.sh --type project --glob "memory/project-*.md" --output data/014-projects.sql
```

This replaces the Generator hand-reading 145 files. The Generator writes the parser ONCE, then runs it for each memory type. Spot-check results against source files.

**Why not have the Generator read each file?**
- 145 files × ~1000 chars = ~145K chars of source reading. Context exhaustion risk.
- Frontmatter format is STANDARDIZED — parsing is mechanical, not creative.
- A parser script is re-runnable (idempotent). Hand-written SQL is one-shot.
- The parser is also the ongoing ingest tool (steady-state, not just migration).

---

## Execution Plan

### Phase 0: Baselines (1 session, ~30 min)

**BLOCKED UNTIL:** Traveller system verified and tuned by Bruce.

Measure current system performance before any changes. Same methodology as Plan 0299 B0-B3.

**B0 — System Health Snapshot:**
- File count, line count, directory structure
- MEMORY.md line count and section breakdown
- Health vector current values
- PTL item count and tier distribution
- Session-details.md line count
- Orphan file count

**B1 — Memory Recall Accuracy:**
Task: "What are the three most recent PARADIGM sessions, and what changed in each?"
Measure: tool calls, file reads, accuracy against session-details.md, time.
This tests whether Argus can retrieve structured facts from flat files.

**B2 — Compaction Resilience:**
Task: Load heavy context (large file reads) to trigger compaction, then ask a memory question.
Measure: can Argus recover correction details, people info, project state after compaction?
This tests the current system's compaction vulnerability.
**Caveat (from Plan 0299):** Compaction triggers are ad hoc — we load large files to consume context, but can't guarantee compaction fires. If it doesn't fire, the test is inconclusive (not failed). Repeat with larger files if needed.

**B3 — Cross-Project Context Switch:**
Task: "I need to prep for Traveller session 12" → "Now, what's the status of the book release?" → "What did Merkin say in his last email?"
Measure: confabulation rate across domain switches, tool call waste.

**B4 — Protocol Compliance:**
Task: Simulate session-end protocol execution.
Measure: does Argus follow all 11 steps correctly? How many file reads required?

### Phase 1: Schema + Build System + Parser (1 session)

**Deliverables:**
- Schema scripts in `~/software/aurasys-memory/scripts/db-setup/` (numbered, dependency-ordered)
- `setup.sh`, `load.sh`, `rebuild-db.sh` in `scripts/` (note: rebuild builds to .db.new, verifies, atomic mv)
- `ingest-memories.sh` — parser script (parses .md frontmatter → SQL data scripts)
- MANIFEST.md with SHA-256 checksums
- `verify-integrity.sh` — checksum chain verification
- Empty `argus.db` at repo root with all tables, views, triggers, indexes
- Test suite: schema existence, constraint rejection, view correctness, rebuild idempotency, parser output validation

**Generator prompt references:** Detailed schema spec written to `scripts/db-setup/schema-spec.md` before Generator runs. Parser spec written to `scripts/ingest-spec.md`.

**Gate:** All tests pass. `PRAGMA integrity_check` and `PRAGMA foreign_key_check` clean. Parser produces valid SQL from 3 sample .md files (one feedback, one project, one reference). Manual review of schema matches this plan's design.

### Phase 2: Core Data Migration (1-2 sessions)

Migrate the most critical and most structured data first. **Phase 2A uses hand-written SQL** (corrections have complex structure). **Phase 2B uses the parser script** (standardized frontmatter format). **Phase 2C is mixed** (structured files + YAML).

**Phase 2A — Corrections + People (hand-written, most critical):**
- Read corrections.md (280 lines, 23 items) → hand-write `data/010-corrections.sql`
  - Corrections have rich metadata (type, depth, cluster, connections, notice) that the parser can't extract from prose body — needs Generator judgment
- Read correction-graph.md → hand-write `data/011-correction-connections.sql`
- Read people.md + people-merkin.md → hand-write `data/012-people.sql`
  - People have tiers, roles, relationships — structured but not in frontmatter format
- Rebuild, verify, run tests
- **Gate:** Exactly 23 corrections. All connection_ids resolve. People tier counts match source.

**Phase 2B — Feedback + Projects + References (parser-driven):**
- `./ingest-memories.sh --type feedback --glob "memory/feedback-*.md" --output data/013-feedback.sql`
- `./ingest-memories.sh --type project --glob "memory/project-*.md" --output data/014-projects.sql`
- `./ingest-memories.sh --type reference --glob "memory/reference-*.md" --output data/015-references.sql`
- `./ingest-memories.sh --type user --glob "memory/user-*.md" --output data/016-user-profile.sql`
- Manual review of generated SQL: spot-check 5 records per type
- Domain assignment review: are feedback/project domain values correct?
- Rebuild, verify, run tests
- **Gate:** Row counts: 57 feedback, 66 projects, 13 references, 9 user_profile. Domain distribution sensible.

**Phase 2C — Sessions + Decisions + Breakthroughs + PTL (mixed):**
- Read session-details.md → hand-write `data/017-sessions.sql` (prose parsing, needs judgment)
- Read decisions.md → hand-write `data/018-decisions.sql` (mixed format)
- Read breakthroughs.md → hand-write `data/019-breakthroughs.sql` (capped set, needs judgment)
- Convert ptl.yaml → `data/020-ptl-items.sql` (YAML→SQL converter, mechanical)
- Read pending.md → hand-write `data/021-pending.sql` (table format)
- Rebuild, verify, run tests
- **Gate:** Session count matches session-details.md. PTL row count matches ptl.yaml item_count. All significance values are PARADIGM or ROUTINE.

**Note on pending_items vs ptl_items:** These overlap — some items appear in both. The DB keeps them separate (different decay rules per protocol.md §5 vs §10). The `category` column on pending_items distinguishes outreach, awaiting, and rules items. No deduplication needed — they serve different purposes.

### Phase 3: L1 Redesign + Mode Profiles + Protocol Update (1 session)

**Deliverables:**
- MEMORY.md rewritten as pure index (target ≤140 lines) per L1 structure above
- Anti-confab hot five as static text in L1 (not query-derived — zero tool calls)
- Mode profiles with DB query templates per domain
- `[sha:XXXXXX]` checksums for every flat file that remains
- Protocol.md updated:
  - Session-end: run ingest-memories.sh → rebuild-db.sh → verify → commit
  - Health vector: derive from v_health_current instead of manual computation
  - Decay sweep: `SELECT * FROM v_stale_projects` + `v_ptl_stale` instead of file scanning
- memory-sync.sh updated: add ingest + rebuild step before commit

**Gate:** MEMORY.md ≤140 lines. All file map paths resolve. All checksums verify. DB query shortcuts return correct results. Health vector computable from `v_health_current`. Session-end protocol executable with ≤3 file writes (down from ~8).

### Phase 4: Integration Testing (1 session)

**P1 — Recall accuracy (post-retrofit):**
Same task as B1 baseline. Compare tool calls, accuracy, time.
Target: fewer file reads, more DB queries, equal or better accuracy.

**P2 — Compaction resilience:**
Same task as B2 baseline. L1 + DB should recover full precision.
Target: after compaction, L1 anti-confab list + DB queries recover all facts tested.

**P3 — Cross-project switching:**
Same task as B3 baseline. Mode profiles should eliminate waste.
Target: zero domain-bleed (Traveller vocab in book response), zero waste reads.

**P4 — Protocol compliance:**
Same task as B4 baseline. DB writes should simplify session-end.
Target: ≤3 file writes at session end (MEMORY.md active sessions + any new .md file + memory-sync).

**P5 — Wiring test:**
Fresh shell, no prior context. MEMORY.md auto-loaded. First DB query within 2 tool calls.
Target: Argus reads L1, sees DB pointer, queries `v_memory_stats` to verify DB is live.

**P6 — Write path test (NEW — no baseline):**
"Remember that Bruce prefers X." Verify: .md file created, ingest-memories.sh parses it correctly, SQL generated, row queryable from DB after rebuild.
Target: end-to-end write path works within one session.

**P7 — Checksum verification test:**
Manually corrupt one flat file's content (without updating checksum). Load that file. Verify `[CHECKSUM DRIFT]` flagged.
Target: lazy verification catches drift, doesn't block loading.

**Gate:** P1-P5 equal or exceed baselines. P6-P7 pass (no baseline comparison — these test new capabilities). Zero regressions. Compaction resilience proven (P2 ≥ B2).

### Phase 5: Flat File Archival (post-verification)

**Only after Phase 4 passes AND Bruce approves:**
1. `git tag pre-flat-archive HEAD`
2. Move migrated flat files to `memory/archive/` (git-tracked, recoverable)
3. Update MEMORY.md file map to remove archived entries
4. Verify: all DB queries still return correct data
5. Verify: `rebuild-db.sh` produces identical DB from scripts alone

**NOT deleted:** Files listed in "What Stays Flat" section above.

---

## Risk Analysis

| Risk | Impact | Mitigation |
|------|--------|------------|
| Bug in argus.db affects ALL conversations | HIGH | Git tag before every phase. Dual-read period. Flat files preserved until Phase 5. |
| MEMORY.md redesign breaks always-loaded behavior | HIGH | Test new L1 in isolated shell before committing. Git tag backup of current MEMORY.md. Run P5 wiring test. |
| Split-brain: auto-memory writes .md, DB not updated | HIGH | ingest-memories.sh at session start + end. Source-of-truth hierarchy documented. DB is cache, data scripts are canonical. |
| Data loss during migration (parser misparsing) | MEDIUM | Row count verification per phase. Spot-check 5 random records. Source files preserved. Parser tested on 3 sample files before bulk run. |
| PTL migration breaks concurrent access | MEDIUM | PTL stays in YAML during migration. DB becomes authoritative only after both systems agree for 3+ sessions. |
| Protocol.md changes break session-end workflow | MEDIUM | Update protocol.md incrementally. Test session-end in isolation before committing. Old protocol.md preserved in git. |
| Concurrent rebuild while another shell queries DB | MEDIUM | rebuild-db.sh builds to .db.new → atomic mv. WAL mode for concurrent reads. |
| New memory type doesn't fit existing tables | LOW | ingest-memories.sh logs unrecognized types to ingest_log. Manual review at next maintenance. |
| Parser can't extract Why/How-to-apply from older files | LOW | Older memory files may not follow current frontmatter conventions. Parser falls back to full body as `content` field. Manual enrichment as maintenance task. |
| Schema too normalized — queries too complex | LOW | Follow Traveller pattern: views encapsulate joins. Query from views, not raw tables. |
| 164 files → DB migration takes longer than estimated | LOW | Parser script handles bulk. Sub-phase gates allow stopping and resuming. Each sub-phase independently valuable. |

---

## Success Criteria

1. All structured data queryable via `sqlite3 ~/software/aurasys-memory/argus.db`
2. MEMORY.md ≤140 lines (down from 177)
3. Zero data loss: every fact in flat files exists in DB (row counts verified per phase)
4. Compaction resilience proven: L1 anti-confab list + DB queries recover all tested facts post-compaction
5. Session-end protocol simplified: ≤3 file writes (down from ~8)
6. Cross-project switching: mode profiles eliminate waste reads, zero domain-bleed
7. Health metrics auto-computable: `SELECT * FROM v_health_current` replaces manual computation
8. PTL queryable: `SELECT * FROM v_ptl_active` replaces YAML render
9. Corrections queryable: `SELECT * FROM v_hot_corrections` replaces full-file grep
10. `rebuild-db.sh` produces identical DB from scripts alone (deterministic, atomic)
11. All baselines (B1-B4) equaled or exceeded by post-tests (P1-P5)
12. Write path works: new .md file → ingest → rebuild → queryable within same session (P6)
13. Checksum verification works: lazy verification catches drift, flags `[CHECKSUM DRIFT]` (P7)
14. Cross-entity queries work: `v_person_context` and `v_project_summary` return correct joined data
15. Ingest pipeline works: `ingest-memories.sh` correctly parses frontmatter from all memory types
16. Bruce approves the system after hands-on verification over 3+ sessions

---

## Blocker: Traveller System Verification

**This plan is BLOCKED.** It cannot proceed until:

1. Plan 0299 full data migration is complete and committed
2. Bruce stress-tests the Traveller reference system with real GM tasks (at least one full session prep + one post-session fiction pass using DB-only workflow)
3. Bruce tunes any issues found during stress testing
4. Bruce explicitly unblocks this plan (verbal or written)

**Why:** The Traveller system is the testbed. If it has architectural issues, we fix them there (cheap, low-risk) before applying to main memory (expensive, high-risk). Bruce's hands-on verification is the quality gate — Argus cannot self-verify a system designed to fix Argus's own errors.

**Expected timeline:** Blocker clears when Bruce runs a real Traveller session using the new system. Next scheduled session is session 12 (date TBD). This plan should be ready to execute immediately after Bruce gives the go-ahead.

---

## Process Reference

Full migration playbook: `memory/project-db-migration-playbook.md`  
Plan 0299 execution results: `memory/project-0299-execution-results.md`  
Phase 3 report (requirements): `traveller-reference/PHASE-3-REPORT.md`  
Traveller metrics: `traveller-reference/metrics/`  
Manifest of manifests: `memory/reference-landmarks.md`
