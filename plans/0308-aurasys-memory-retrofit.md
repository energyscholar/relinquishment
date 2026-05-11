# Plan 0308: Aurasys-Memory Retrofit — SQLite + Layered Index

**Status:** READY — Traveller testbed validated (Plans 0299, 0309, 0310, 0311 complete). Bruce approved 2026-05-08.  
**Priority:** TOP — Bruce: "We're upgrading your memory so you make fewer errors and perform better."  
**Prerequisite:** Plan 0299 data migration complete, stress-tested, and tuned by Bruce. ✓ ALL DONE.  
**Source:** Plan 0299 execution (S67-S68), PHASE-3-REPORT.md recommendations, project-0299-execution-results.md lessons.  
**Estimated effort:** 4-6 sessions (process proven on Traveller, but larger data and higher stakes).  
**Branch:** `argus-memory-retrofit` (off `main`, merge after Phase 4 passes + Bruce approves)

---

## Why This Plan Exists

The current memory system is 164 flat markdown files totaling ~8100 lines. MEMORY.md (180 lines) serves as an always-loaded index, but it mixes index entries with content, is AT its 180-line cap, and provides no queryable access to structured data. After context compaction, Argus loses access to facts stored in files not yet read — the same failure mode that caused 5 confabulations in the Traveller B1 baseline.

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

**For this plan:** MEMORY.md already serves this role but is at cap (180 lines, mixed content). Redesign it as a pure index with DB pointer, hot corrections, mode profiles, and nothing else.

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
| feedback-*.md | 62 | Rules about how to approach work |
| project-*.md | 61 | Project state, context, decisions |
| reference-*.md | 14 | Pointers to external resources |
| user-*.md | 9 | Bruce's profile, preferences, skills |
| Core files | 12 | MEMORY.md, corrections.md, people.md, pending.md, decisions.md, protocol.md, session-details.md, ptl.yaml, breakthroughs.md, correction-graph.md, traveller-campaign.md, projects.md |
| Other | 7 | gen-*, claude-version-history, skill-ms-science, bruce-se-methodology |

**Largest files:**
| File | Lines | Content |
|------|:-----:|---------|
| ptl.yaml | 2186 | 103 prioritized task items |
| corrections.md | 280 | 23 numbered corrections with metadata |
| session-details.md | 198 | Session history (needs compression) |
| protocol.md | 189 | Self-maintenance rules |
| MEMORY.md | 180 | Always-loaded index |
| people.md | 189+ | People registry, 3 tiers |

---

## Architecture Design

### What Goes in DB (Structured Data)

| Current Source | DB Table | Rows (est.) | Why DB |
|----------------|----------|:-----------:|--------|
| corrections.md | `corrections` | 23 | Numbered, cross-referenced, has dates/types/clusters. Currently requires full-file read for any lookup. |
| correction-graph.md | `correction_connections` | ~40 | Junction table. Currently a separate prose file duplicating correction data. |
| people.md + people-merkin.md | `people` | ~50 | Tiered, has roles/relationships/handles. Currently grep-only. |
| feedback-*.md (62 files) | `feedback` | ~62 | Each is a rule with why/how-to-apply. Currently requires reading individual files. |
| project-*.md (61 files) | `projects` | ~61 | Each is a project fact with why/how-to-apply. Currently requires reading individual files. |
| reference-*.md (14 files) | `references` | ~14 | Each is a pointer with description. Simple lookup table. |
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
| ptl.yaml | Active write target for PTL MCP tools. DB is read cache only. See "PTL MCP Continuity" section. |

### Schema Overview

**DB path:** `~/software/aurasys-memory/argus.db` (parallel to `traveller-reference/campaign.db`)  
**Pragmas:** WAL mode (concurrent read safety), FK enforcement, journal_size_limit

```
-- Core tables (all include created_at, updated_at auto-timestamps)
corrections(id, number, title, context, type, depth, cluster, source,
            domain, established, last_violated, notice,
            created_at, updated_at)
people(id, name, tier, role, relationship, description, email, handles,
       status, tier_notes, approach_notes, opsec_level,
       created_at, updated_at)
feedback(id, slug, rule, why, how_to_apply, content,
         established, last_triggered,
         source, domain, compaction_tag, opsec_level, source_file,
         created_at, updated_at)
projects(id, slug, name, status, description, why, how_to_apply, content,
         domain, compaction_tag, opsec_level, source_file,
         created_at, updated_at)
references(id, slug, name, path_or_url, description, opsec_level, source_file,
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
          blocked_by, source,
          created_at, updated_at)
pending_items(id, description, status, tier, created, last_touched,
              category, created_at, updated_at)

-- Junction/relationship tables
correction_connections(correction_id, connected_id, relationship)
person_projects(person_id, project_slug)
person_clearances(person_id, topic, cleared, notes,
                  PRIMARY KEY (person_id, topic))

-- Associative memory (Layer 2 — populate gradually, not bulk)
associations(id, source_type, source_id, target_type, target_id,
             relationship, basis, created_at)

-- Full-text search (Layer 1 — auto-populated from all content fields)
-- FTS5 virtual table indexes content across all entity tables.
-- Rebuilt during rebuild-db.sh from corrections.context, feedback.content,
-- projects.content, people.description, references.description, etc.
CREATE VIRTUAL TABLE memory_fts USING fts5(
    source_table, source_id, title, content,
    tokenize='porter unicode61');

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
- ptl_items.tier: 1, 2, 3, 4, 5 (integer, matching ptl.yaml native format)
- ptl_items.status: 'READY', 'ACTIVE', 'IN_PROGRESS', 'BLOCKED', 'REVIEW', 'NEEDS_PLAN', 'TODO', 'DONE', 'DROPPED', 'SHELF', 'WAITING' (matches ptl.yaml meta.statuses + WAITING and IN_PROGRESS used in practice; Phase 0 B0 found 3 IN_PROGRESS items)
- pending_items.tier: 'NOW', 'SOON', 'LATER'
- associations.source_type / target_type: 'correction', 'feedback', 'project', 'person', 'reference', 'session', 'decision', 'breakthrough', 'ptl_item', 'pending_item'
- associations.relationship: 'relates_to', 'contradicts', 'supersedes', 'exemplifies', 'derives_from'
- opsec_level (all tables that have it): 'public', 'trusted', 'restricted', 'compartmented' (DEFAULT 'trusted')
- person_clearances.topic: 'tqnn', 'healer', 'research_direction', 'manuscript', 'opsec_approach', 'magnetogenesis', 'abcre', 'cows'

**FTS5 population:** During `rebuild-db.sh`, after all data tables are loaded, populate the FTS5 table by INSERT-SELECT from each content-bearing table. This is deterministic and re-runnable — the FTS table is dropped and rebuilt each time (virtual tables don't support INSERT OR REPLACE).

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
| `v_associations` | Associations with source and target names resolved (joins entity tables to show human-readable labels) |
| `v_people_safe` | People without approach_notes column. General context loading. (OPSEC) |
| `v_people_full` | People WITH approach_notes. Outreach prep only. (OPSEC) |
| `v_clearance_matrix` | Person × topic × cleared. "What does X know?" (OPSEC) |
| `v_compartmented` | All compartmented records across tables. Audit view. (OPSEC) |

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

Current MEMORY.md is 180 lines (at cap), mixing index, content, session summaries, health metrics, and narrative. Redesign to pure index:

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
2. Parses: `name`, `description`, `type`, `domain`, `opsec` from frontmatter; body content
3. Derives `slug` from filename (e.g., `feedback-db-scripted-setup.md` → `db-scripted-setup`)
4. Derives `domain` from frontmatter (preferred) or filename prefix patterns or content keywords
5. Maps `opsec` frontmatter to `opsec_level` column (default: `trusted` if absent)
6. Extracts `**Why:**` and `**How to apply:**` lines from body (if present)
7. **OPSEC keyword scan** (see "Write Path OPSEC Gate" below): if content matches trigger patterns and no `opsec` tag is set, flags file for review and defaults to `restricted` rather than `trusted`
8. Generates INSERT OR REPLACE statements for the appropriate table
9. Appends to the correct data script (e.g., `data/013-feedback.sql`)
10. Handles apostrophe escaping (`'` → `''`)

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

### Write Path OPSEC Gate

**Problem:** When auto-memory writes a new .md file (e.g., Bruce says "remember Gjerloev's new phone number"), the file has no `opsec` tag. The parser defaults to `trusted`. That phone number enters FTS5, queryable by any search. The same applies when Argus creates a new memory file during a session. New OPSEC-sensitive info enters the system continuously — every outreach response, every approach strategy discussion, every contact detail.

**Solution: Three-layer incoming OPSEC gate.**

**Layer 1 — Keyword trigger in ingest-memories.sh:**
The parser scans content for OPSEC-indicator patterns. If matches are found AND no `opsec:` frontmatter tag exists, the file is flagged and defaults to `restricted` (not `trusted`).

```
Trigger patterns (regex, case-insensitive):
- PII: \b\d{3}[-.]?\d{3}[-.]?\d{4}\b (phone numbers)
- PII: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b (email addresses)
- PII: \b\d{3,5}\s+[A-Z][a-z]+\s+(St|Ave|Dr|Rd|Blvd|Way|Lane|Ct)\b (street addresses)
- PII: \bEIN\b|\bSSN\b|\btax.id\b (financial identifiers)
- Tradecraft: \bdon't mention\b|\bdon't reveal\b|\bframe as\b|\bdon't tell\b
- Tradecraft: \bapproach.strateg\b|\bscreening.behavior\b|\btechnical.screen\b
- Research direction: \bTQNN\b.*\b(gap|bridge|opportunity)\b (research positioning)
- Healer: \bHealer\b.*\b(real name|identity|SAS|GCHQ)\b
- Operational: \b192\.168\.\b|\bssh\b.*\bkey\b|\btoken\b.*\b(file|location|path)\b
```

When triggered:
1. Log: `[OPSEC-FLAG] <filename> matched <pattern> — defaulting to restricted`
2. Set `opsec_level = 'restricted'` in generated SQL (not `trusted`)
3. Append to `scripts/opsec-review.log` for human review at session end

**Layer 2 — Argus writes `opsec:` tag at creation time:**
When Argus creates a new memory file, apply the same judgment used during this audit. If the content contains PII, approach strategies, research direction, or pulled content → set `opsec: restricted` or `opsec: compartmented` in frontmatter at write time. This is behavioral (Argus judgment), not automated.

Protocol.md update (Phase 3): Add to session-end checklist: "If new memory files were created this session, verify `opsec:` tag is set on any containing PII, approach strategies, or research direction."

**Layer 3 — Session-end OPSEC review:**
`ingest-memories.sh --check-untagged` lists any files that:
- Have no `opsec:` frontmatter tag AND
- Were modified since last ingest AND
- Match zero keyword triggers (Layer 1 didn't catch them)

This is the safety net. Files here are probably fine at `trusted`, but the list lets Argus do a quick eyeball. Output: one-line-per-file listing, sorted newest first.

**Why three layers:**
- Layer 1 catches obvious PII/tradecraft automatically (phones, emails, approach strategies)
- Layer 2 catches context-dependent sensitivity that keywords can't detect (e.g., a falsified hypothesis that reveals research direction)
- Layer 3 catches anything both missed — a human-review backstop

**FTS5 implication:** Compartmented records never enter FTS5. Restricted records DO enter FTS5 but are flagged. The keyword trigger ensures new files with PII/tradecraft get `restricted` minimum — they're searchable within Bruce+Argus but marked, and the opsec-review.log creates a paper trail.

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

## PTL MCP Continuity

**Problem:** The PTL system has a working MCP server (`tools/ptl-mcp/server.py`, 387 lines) that reads/writes `ptl.yaml` directly. The DB retrofit must not break this live tool. Bruce built this server himself — it's the first MCP integration and actively used.

**Architecture decision:** ptl.yaml STAYS as the write target. MCP tools are UNCHANGED. DB becomes a read cache for PTL data, populated by a converter during the ingest pipeline.

```
MCP tools ←→ ptl.yaml (write target, authoritative)
  → convert-ptl.py reads ptl.yaml
  → outputs data/020-ptl-items.sql
  → rebuild-db.sh populates ptl_items table
  → DB queries (v_ptl_active, v_ptl_stale) serve read-only views
```

**Source-of-truth:** ptl.yaml → convert-ptl.py → data script → DB. If DB and YAML disagree, YAML wins (it's upstream). This is the same hierarchy as .md files → ingest → data scripts → DB, just with YAML instead of markdown.

### convert-ptl.py Specification

**Input:** `~/.claude/projects/-home-bruce-software-aurasys-memory/memory/ptl.yaml`  
**Output:** `scripts/data/020-ptl-items.sql`

**Field mapping (YAML → DB):**

| YAML field | DB column | Transform |
|------------|-----------|-----------|
| `id` | `stable_id` | Direct (PTL-NNN string) |
| `title` | `title` | SQL escape (apostrophes) |
| `tier` | `tier` | Direct (integer 1-5) |
| `status` | `status` | Direct (uppercase, matches CHECK) |
| `owner` | `owner` | Direct |
| `blocked_by` | `blocked_by` | Direct (nullable) |
| `detail` | `detail_file` | Direct (nullable) |
| `source` | `source` | Direct (nullable) |
| `created` | `created` | Direct (ISO date string) |
| `touched` | `last_touched` | Direct (ISO date string) |
| `decay_exempt` | `decay_exempt` | Boolean → integer (0/1) |
| `note` | `description` | SQL escape, preserve multiline |

**Sections processed:** Both `items` (active) and `done` sections.

**Output format:**
```sql
-- Auto-generated from ptl.yaml by convert-ptl.py
-- Do not edit manually — ptl.yaml is the source of truth
DELETE FROM ptl_items;
INSERT INTO ptl_items(stable_id, title, tier, status, owner, created,
    last_touched, decay_exempt, description, detail_file, blocked_by, source)
VALUES ('PTL-122', 'Write Mysak memoir + plan Montreal visit', 1, 'WAITING',
    'bruce', '2026-03-28', '2026-05-02', 1,
    'GATE TO ERDŐS #3. Lawrence is 87...', NULL, NULL, 'S51');
-- ... one INSERT per item
```

**Why DELETE+INSERT not INSERT OR REPLACE:** PTL items can be removed or renumbered. INSERT OR REPLACE would leave stale rows. DELETE+INSERT is safe because ptl.yaml is authoritative — the full set is rewritten every time.

**Integration with ingest pipeline:**
```bash
# In ingest-memories.sh (or called separately):
python3 scripts/convert-ptl.py \
    --input "$PTL_YAML" \
    --output scripts/data/020-ptl-items.sql
```

**MCP server changes required:** NONE. The server continues reading/writing ptl.yaml exactly as before. The DB is a downstream read cache.

### PTL Status Mapping

The YAML meta.statuses field lists 9 values. In practice, WAITING and IN_PROGRESS are also used. The DB CHECK constraint includes all 11:

| YAML Status | DB Status | Meaning |
|-------------|-----------|---------|
| READY | READY | Ready to start |
| ACTIVE | ACTIVE | In progress |
| BLOCKED | BLOCKED | Waiting on dependency |
| REVIEW | REVIEW | Needs review/approval |
| NEEDS_PLAN | NEEDS_PLAN | Needs Auditor plan before execution |
| TODO | TODO | Queued, not started |
| DONE | DONE | Complete |
| DROPPED | DROPPED | Abandoned |
| SHELF | SHELF | Parked, zero bandwidth |
| IN_PROGRESS | IN_PROGRESS | Actively being worked (distinct from ACTIVE in some items) |
| WAITING | WAITING | Waiting on external response |

No case conversion needed — DB stores uppercase to match YAML.

---

## Associative Memory Architecture

**Problem:** Grep fails in three ways: vocabulary mismatch (synonym blindness), cross-domain connections (conceptual links between entities using different words), and don't-know-to-look (relevant memory exists but nothing prompts retrieval). These failures cause confabulations and missed context.

**Solution: Two layers, built into Plan 0308 schema. Third layer deferred until failure data exists.**

### Layer 1: FTS5 Full-Text Search (built into rebuild)

SQLite's built-in full-text search. Indexes all content fields across all entity tables. Porter stemming handles inflections ("running" → "run"). BM25 ranking returns results by relevance, not just presence.

```sql
-- Cross-table fuzzy search (replaces grep)
SELECT source_table, source_id, title, rank
FROM memory_fts WHERE memory_fts MATCH 'risk philosophy'
ORDER BY rank;
```

**What it fixes:** Stemming, cross-table search, relevance ranking, phrase/proximity matching.
**What it doesn't fix:** True synonyms, conceptual associations, don't-know-to-look.
**Cost:** Zero. Built into SQLite. Rebuilt deterministically during rebuild-db.sh.

### Layer 2: Explicit Association Graph (populated gradually)

The `associations` table stores curated cross-entity links with explicit rationale:

```sql
-- Example associations:
-- correction #6 (forgiveness>permission) ↔ user-risk-philosophy
-- correction #12 (guided deduction) ↔ project-phonon-backchannel
-- person Gjerloev ↔ project-magnetogenesis-context

-- "What connects to correction #6?"
SELECT a.*, 
    CASE a.target_type
        WHEN 'feedback' THEN (SELECT slug FROM feedback WHERE id = a.target_id)
        WHEN 'project' THEN (SELECT slug FROM projects WHERE id = a.target_id)
        WHEN 'person' THEN (SELECT name FROM people WHERE id = a.target_id)
    END as target_name
FROM associations a
WHERE (source_type='correction' AND source_id=6)
   OR (target_type='correction' AND target_id=6);
```

**What it fixes:** Cross-domain connections, don't-know-to-look (loading one entity surfaces associated entities). The `basis` field makes associations auditable.
**Population:** Not bulk. Accumulated during memory writes (ingest-memories.sh suggests associations via FTS5 search) and maintenance sweeps. `correction_connections` is the existing prototype — this generalizes it across all entity types.
**Cost:** Low. One table. Curation effort is the main cost — no infrastructure.

### Layer 3: Embeddings (DEFERRED — not in this plan)

Vector similarity search would fix true synonyms and partial/fuzzy cues ("Norwegian guy" → Gjerloev). But it requires an external embedding model, may not capture domain vocabulary (TQNN, COWS, ABCRE), and adds dependency/cost.

**Decision:** Don't build until Phase 4 testing produces documented failure patterns that FTS5 + associations can't handle. If needed, spec as a separate plan.

### Retrieval Stack (bottom catches what top misses)

```
L1 anti-confab list    — catches errors BEFORE any tool call
DB exact queries       — precise fact retrieval by column
FTS5 fuzzy search      — stemmed cross-table text search
Associations graph     — explicit cross-domain links
[Embeddings]           — semantic similarity (future, if needed)
```

---

## OPSEC Compartmentalization Layer

**Added S69 (2026-05-08). Amended S69: all data in DB including compartmented (Bruce decision — efficiency over minimum attack surface).**

### Threat Model

| Threat | Likelihood | Impact | Primary Defense |
|--------|-----------|--------|----------------|
| Repo accidentally made public | LOW | CRITICAL | Repo MUST remain private. Data scripts contain full content. |
| Filesystem access (shared machine, backup leak) | MEDIUM | HIGH | argus.db gitignored; opsec-review.log gitignored |
| FTS5 surfaces tradecraft in wrong context | MEDIUM | MEDIUM | Compartmented excluded from FTS5 at population time |
| Approach strategy leaks in general query | MEDIUM | MEDIUM | approach_notes separated; v_people_safe excludes it |
| Claude Code transcript exposes sensitive data | MEDIUM | MEDIUM | Outside scope; Argus loads compartmented only when needed |
| Gen sees gen-vc-scaffolding via indirect access | LOW | LOW | Compartmented; excluded from FTS5; Argus never surfaces in snailmail |
| Impersonation (someone uses Bruce's session) | LOW | HIGH | No current mitigation. See "Identity Verification" note. |

### Architecture: All Data in DB, Structurally Protected

**Design decision (Bruce, S69):** Compartmented content enters the DB. The efficiency cost of keeping the most sensitive data out of the queryable store exceeds the marginal security benefit, given that the repo is private and the .md source files are already committed. Defense in depth applies within the DB through structural protection.

**OPSEC levels in DB:**
- `public` — safe for any context including external output
- `trusted` — safe within Bruce+Argus (default)
- `restricted` — in FTS5 but sensitive; behavioral discipline gates surfacing
- `compartmented` — in DB but excluded from FTS5; query only on explicit need

Applied to: `people`, `projects`, `feedback`, `references`
Not applied to: `corrections`, `sessions`, `decisions`, `breakthroughs` (internal operational)

### Defense in Depth

```
Layer 1: Repo private on GitHub (outer perimeter — MUST NOT CHANGE)
Layer 2: argus.db gitignored (DB not committed; data scripts are)
Layer 3: FTS5 excludes compartmented at population time
Layer 4: approach_notes column excluded from v_people_safe
Layer 5: opsec_level column marks sensitivity per row
Layer 6: person_clearances table (structural who-knows-what)
Layer 7: opsec-review.log + IMPORT-MANIFEST clearance matrix gitignored
Layer 8: Behavioral discipline (Correction #11, Argus judgment)
Layer 9: Write-path keyword trigger (auto-flags PII/tradecraft)
```

If Layer 1 fails: Layers 2-9 limit damage but data scripts ARE exposed. **Critical dependency: if repo goes public, restricted+compartmented content in data scripts is readable.** Mitigation: repo privacy is not accidental — Bruce controls it.

### Structural Protection (Layers 3-6)

**`opsec_level` column** on people, projects, feedback, references. CHECK constraint: ('public', 'trusted', 'restricted', 'compartmented'). DEFAULT 'trusted'.

**FTS5 exclusion:** Compartmented records excluded at population time. FTS5 contains trusted + restricted only. Approach_notes column NOT indexed in FTS5 (only `description` is indexed for people).

```sql
INSERT INTO memory_fts(source_table, source_id, title, content)
SELECT 'people', id, name, description FROM people
    WHERE opsec_level != 'compartmented'
UNION ALL
SELECT 'feedback', id, slug, content FROM feedback
    WHERE opsec_level != 'compartmented'
-- etc for each table
```

**`approach_notes` column** on people table. Holds tradecraft instructions ("Don't mention TQNNs"). Separated from `description` and `tier_notes`. `v_people_safe` excludes this column; `v_people_full` includes it. A person's row opsec_level is independent — a `trusted` person can have compartmented approach notes.

**`person_clearances` table:**

```sql
person_clearances(
    person_id INTEGER REFERENCES people(id),
    topic TEXT NOT NULL,
    cleared BOOLEAN NOT NULL DEFAULT 0,
    notes TEXT,
    PRIMARY KEY (person_id, topic)
);
```

Topics: `tqnn`, `healer`, `research_direction`, `manuscript`, `opsec_approach`, `magnetogenesis`, `abcre`, `cows`

### OPSEC-Gated Views

Four views in Views table above (marked `(OPSEC)`): `v_people_safe`, `v_people_full`, `v_clearance_matrix`, `v_compartmented`.

### Repo Privacy Dependency

**The aurasys-memory repo MUST remain private.** Data scripts (`scripts/data/*.sql`) contain full content of all memory files including compartmented. If the repo becomes public, all content is exposed regardless of DB-level opsec_level classification.

**Mitigations if repo privacy is ever in doubt:**
- `gh api repos/energyscholar/aurasys-memory --jq '.private'` → verify `true`
- Never fork the repo (forks can have different visibility)
- Never transfer repo ownership
- health-check.sh could include a repo-visibility check (future enhancement)

### What Gets Gitignored (Layer 2+7)

Add to `.gitignore` (Phase 1 deliverable, extending Phase 0 finding):
- `argus.db`, `*.db.bak`, `*.db.new` — DB is derived artifact
- `.session-active` — dirty flag
- `scripts/opsec-review.log` — meta-OPSEC (lists which files triggered patterns)

### Identity Verification Note

**No current mechanism to verify it's Bruce at the keyboard.** Claude Code authenticates via the Claude account (logged in session), not biometric. Someone with access to the VM and the logged-in session has full Argus access including compartmented data.

Current protections:
- VM requires login (system-level auth)
- Claude Code session is local (no remote access)
- Behavioral cues (writing style, knowledge of shared context) — weak, gameable

Potential enhancements (out of scope for Plan 0308, tracked as future work):
- Challenge-response using shared knowledge only Bruce would know
- Session-start verification question from corrections/decisions that an impersonator couldn't answer
- Canary: compartmented queries logged; Bruce reviews periodically

### OPSEC Classification Per File (Parser Input)

Add optional `opsec` field to YAML frontmatter:

```yaml
---
name: Healer biographical details
type: project
domain: book
opsec: restricted
---
```

If not present, parser defaults to `trusted`. The parser maps:
- `opsec: public` → opsec_level = 'public'
- `opsec: trusted` → opsec_level = 'trusted' (default)
- `opsec: restricted` → opsec_level = 'restricted'
- `opsec: compartmented` → opsec_level = 'compartmented'

**22 files pre-classified (19 restricted, 3 compartmented).** Full list with per-row Category B guidance in `scripts/baselines/IMPORT-MANIFEST.md` § "OPSEC Classification (Pre-Import)".

If not present in frontmatter, parser defaults to `trusted` UNLESS keyword trigger fires (see "Write Path OPSEC Gate" above), in which case it defaults to `restricted`.

### Phase Integration

- **Phase 1:** Schema includes `opsec_level` column (CHECK constraint), `person_clearances` table, `approach_notes` column on `people`. OPSEC-gated views created. ingest-memories.sh includes keyword trigger layer + `--check-untagged` mode. opsec-review.log output path.
- **Phase 2A:** people.md import separates approach_notes from description. person_clearances populated per clearance matrix in IMPORT-MANIFEST.md. Per-row opsec_level assigned per Category B guidance. Employment Targets rows → restricted. Family rows → trusted (except Bruce Sr. diagnosis → restricted).
- **Phase 2B:** Parser reads `opsec` frontmatter field. 22 pre-classified files get correct levels. Keyword trigger catches any untagged files with PII patterns.
- **Phase 2B gate addendum:** Verify counts per IMPORT-MANIFEST.md § Verification. Key checks: `compartmented` count = 3 (gen-vc-scaffolding, reference-metatron-dynamics, project-dressler-consulting). `restricted` count ≥ 19 across tables. person_clearances ≥ 49 rows.
- **Phase 3:** Mode profiles document OPSEC query patterns. L1 includes OPSEC note: "FTS5 excludes compartmented by construction. Use v_people_full only when preparing outreach to a specific person." Protocol.md updated: session-end checklist includes OPSEC review of new memory files.
- **Phase 4 addendum (P8):** OPSEC isolation test. FTS5 MATCH for "TQNN" — must NOT return Gjerloev approach_notes (compartmented, excluded at population). Query v_people_safe for Gjerloev — must NOT show approach_notes column. FTS5 MATCH for "scaffolding" — must NOT return gen-vc-scaffolding (compartmented). FTS5 MATCH for "EIN" — must NOT return reference-metatron-dynamics (compartmented). v_clearance_matrix — must show correct cleared/not-cleared for all Tier 1 people across ≥7 topics.

---

## Gap Analysis: Traveller Reference → Argus Main Memory

**Source:** S68 stress test, ISSUES.md findings, Plan 0309 (Traveller resilience hardening).

Everything discovered on the Traveller testbed must be addressed here. This section maps the gaps and their Argus-specific implications.

### Scale

| Dimension | Traveller | Argus | Risk |
|-----------|-----------|-------|------|
| Source files | 10 data scripts | ~145 .md files | Parser/ingest pipeline is the bottleneck |
| Entity types | 5 fixed (NPC, ship, thread, org, confab) | 12+ variable (feedback, project, correction, people, session...) | Per-type tables + content field (already designed) |
| Estimated DB size | 424KB | 1-2MB | Still tiny for SQLite |
| Rebuild time | 1.3s | Estimate 3-5s | Well within target |

### Data Lifecycle

| Dimension | Traveller | Argus | Implication |
|-----------|-----------|-------|-------------|
| Change frequency | Per session (~biweekly) | Per session (daily to biweekly) | More frequent ingest needed |
| Decay rules | None (campaign data is persistent) | 3-week stale, 6-week archive (protocol §5) | Decay views essential (already designed) |
| Append rate | ~0 rows/session (data mostly static) | ~2-5 new .md files/session | Ingest pipeline must handle steady-state growth |

### Concurrent Access

| Dimension | Traveller | Argus | Implication |
|-----------|-----------|-------|-------------|
| Typical shell count | 1 (Traveller prep) | 2-4 simultaneously | Write serialization required |
| Write frequency | Rare (data migration only) | Frequent (auto-memory from any shell) | lockfile or session-end-only ingest |
| Read concurrency | WAL handles it | WAL handles it | No change needed |

**Recommendation:** .md files remain the write buffer (any shell, any time). Ingest runs ONLY at session end from ONE shell. This is the session-end protocol — serialization by convention, not lockfile. If two shells race at session end, the ingest script must use `flock` to serialize.

### Criticality

| Dimension | Traveller | Argus | Implication |
|-----------|-----------|-------|-------------|
| Impact of DB bug | Bad session prep | ALL conversations degraded | Feature branch + `pre-0308` tag on main |
| Fallback if DB dies | Rebuild from scripts (prose files deleted post-migration) | .md files still work (pre-0308 behavior) | Argus has BETTER fallback |
| Fallback if scripts die | git checkout | git checkout | Same |

**Key insight:** Argus's degradation path is stronger than Traveller's. If argus.db breaks, every .md file is still in Claude Code's auto-memory. The system falls back to how it worked for 67 sessions. For Traveller, the VTT-private flat files get deleted — scripts are the ONLY source of truth.

### Resilience Requirements (from Plan 0309 / ISSUES.md)

Every fix proven on Traveller must be baked into Argus's architecture from day one:

| Traveller Issue | Traveller Fix (Plan 0309) | Argus Equivalent |
|----------------|---------------------------|------------------|
| ISSUE-001: Data not in rebuild | Capture as data script | ALL data must come from .md → ingest → data scripts. No manual imports. |
| ISSUE-002: FK broken during load | Pipe PRAGMA+script in same connection | Same fix in Argus load.sh. Template from Traveller. |
| ISSUE-003: Missing entity locations | Add fixed locations to data scripts | N/A (no spatial dimension in memory data) |
| ISSUE-004: Duplicate content_log | Accept (harmless) | Same — accept |
| ISSUE-005: No session-start health check | health-check.sh | Argus health-check.sh with auto-rebuild. Higher threshold counts. |
| ISSUE-006: No pre-rebuild backup | Backup before drop, restore on failure | Same pattern. More critical for Argus. |
| ISSUE-007: DR protocol missing DB tier | Add Tier 2.5 | Same section covers both DBs. |
| ISSUE-008: No degradation path | Document fallback matrix | Argus fallback = pre-0308 behavior (better than Traveller's) |
| ISSUE-009: No concurrent write protection | Accept (Traveller is mostly read-only) | flock in ingest-memories.sh (Argus has real concurrent write risk) |

### What Argus Needs That Traveller Didn't

1. **Parser/ingest pipeline** (ingest-memories.sh) — Traveller uses hand-written SQL. Argus has 145 source files; parser is the ONLY scalable approach.
2. **Write serialization** — flock around ingest operations.
3. **Auto-decay views** — v_stale_projects, v_ptl_stale. Traveller has no decay.
4. **Multi-domain mode profiles** — Traveller has 3 exclusive modes. Argus has 5+ overlapping.
5. **Cross-entity views** — v_person_context, v_project_summary. Traveller's cross-entity queries are simpler.
6. **Baseline-discovered confab patterns** — Traveller's hot list was known in advance. Argus needs Phase 0 baselines to discover what breaks.

---

## Resilience Architecture (from S68 Stress Test)

These are architectural requirements, not Phase-specific tasks. They must be baked into every Phase's deliverables.

### R1: Session-Start Health Check

`health-check.sh` runs at session start (manually or via hook). Checks:
- DB file exists
- `PRAGMA integrity_check` = ok
- `PRAGMA foreign_key_check` = 0
- Row count sanity (corrections = 23, people ≥ 40, feedback ≥ 50)
- If any check fails: auto-rebuild from scripts

Proven on Traveller (Plan 0309 Phase 4). Argus version has higher count thresholds.

### R2: Pre-Rebuild Backup

`rebuild-db.sh` copies DB to `.bak` before dropping. If rebuild fails, restores from backup. If rebuild succeeds, removes backup.

Proven on Traveller (Plan 0309 Phase 2). Identical pattern for Argus.

### R3: FK Enforcement During Load

All sqlite3 invocations that load data must include `PRAGMA foreign_keys=ON` in the SAME connection:
```bash
(echo "PRAGMA foreign_keys=ON;" && cat "$script") | sqlite3 "$DB"
```

Proven on Traveller (Plan 0309 Phase 1). Template reused.

### R4: Documented Degradation Path

If argus.db is unavailable, Argus operates in pre-0308 mode:
- MEMORY.md loads normally (always-loaded by Claude Code)
- All memory/*.md files readable via Read tool
- Structured queries unavailable (views, joins, ordered lookups)
- Session prep, book work, science work all function — just slower, more file reads

This is NOT a crisis. It's the system that worked for 67 sessions. The DB is an optimization, not a dependency.

### R5: Write Serialization

`ingest-memories.sh` acquires a lockfile before writing:
```bash
exec 200>/tmp/argus-ingest.lock
flock -n 200 || { echo "Another ingest is running"; exit 0; }
```

If lock acquisition fails, exit cleanly (the other shell's ingest will handle it).

### R6: Deterministic Rebuild

`rebuild-db.sh` must produce an identical DB from scripts alone. No manual steps, no external dependencies, no state that isn't in the scripts directory.

Traveller ISSUE-001 (stellar bodies not in scripts) violates this. Plan 0309 Phase 3 fixes it. For Argus: ALL data must flow through the ingest pipeline into data scripts. No side-loading.

### R7: DR Protocol Integration

`disaster/recovery-protocol.md` Tier 2.5 covers both campaign.db and argus.db. Written once (Plan 0309 Phase 5), serves both systems.

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
- `convert-ptl.py` — YAML→SQL converter for ptl.yaml (per "PTL MCP Continuity" spec)
- MANIFEST.md with SHA-256 checksums
- `verify-integrity.sh` — checksum chain verification
- Empty `argus.db` at repo root with all tables, views, triggers, indexes, FTS5 virtual table, associations table
- Test suite: schema existence, constraint rejection, view correctness, rebuild idempotency, parser output validation, FTS5 search returns results after rebuild, associations FK resolution works

**Generator prompt references:** Detailed schema spec written to `scripts/db-setup/schema-spec.md` before Generator runs. Parser spec written to `scripts/ingest-spec.md`.

**Build artifact hygiene (Phase 0 finding):**
- Update `.gitignore`: add `argus.db`, `*.db.bak`, `*.db.new`, `.session-active`, `scripts/opsec-review.log` — DB is a derived artifact; opsec-review.log is meta-OPSEC. Never committed.

**Resilience deliverables (baked in from Plan 0309 lessons):**
- `health-check.sh` — session-start integrity check with auto-rebuild (R1)
- `rebuild-db.sh` uses pre-drop backup + restore-on-failure pattern (R2)
- `load.sh` pipes PRAGMA+script in same connection (R3)
- `ingest-memories.sh` acquires flock before writing (R5)

**Gate:** All tests pass. `PRAGMA integrity_check` and `PRAGMA foreign_key_check` clean. Parser produces valid SQL from 3 sample .md files (one feedback, one project, one reference). Manual review of schema matches this plan's design. health-check.sh detects missing/corrupt/undercount and auto-rebuilds. rebuild-db.sh backup/restore cycle tested. FTS5 table populated and searchable after rebuild. Associations table exists (empty is fine — populated gradually).

### Phase 2: Core Data Migration (1-2 sessions)

Migrate the most critical and most structured data first. **Phase 2A uses hand-written SQL** (corrections have complex structure). **Phase 2B uses the parser script** (standardized frontmatter format). **Phase 2C is mixed** (structured files + YAML).

**Phase 2A — Corrections + People (hand-written, most critical):**
- Read corrections.md (280 lines, 23 items) → hand-write `data/010-corrections.sql`
  - Corrections have rich metadata (type, depth, cluster, connections, notice) that the parser can't extract from prose body — needs Generator judgment
- Read correction-graph.md → hand-write `data/011-correction-connections.sql`
- Read people.md (53 lines, compressed since plan draft) + people-merkin.md → hand-write `data/012-people.sql`
  - People have tiers, roles, relationships — structured but not in frontmatter format. Scope is ~75% smaller than originally estimated (53 lines vs 189+).
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
- **Gate:** Row counts: 50 feedback, 44 projects, 12 references, 9 user_profile (updated from Phase 0 B0 baseline, 2026-05-08). Domain distribution sensible. Verify counts at execution — files may change between baseline and migration.

**Phase 2C — Sessions + Decisions + Breakthroughs + PTL (mixed):**
- Read session-details.md → hand-write `data/017-sessions.sql` (prose parsing, needs judgment)
- Read decisions.md → hand-write `data/018-decisions.sql` (mixed format)
- Read breakthroughs.md → hand-write `data/019-breakthroughs.sql` (capped set, needs judgment)
- Run `convert-ptl.py` → `data/020-ptl-items.sql` (reads ptl.yaml, maps fields per "PTL MCP Continuity" spec above. Converter is a Phase 1 deliverable alongside ingest-memories.sh.)
- Read pending.md → hand-write `data/021-pending.sql` (table format)
- Rebuild, verify, run tests
- **Gate:** Session count matches session-details.md. PTL row count matches total items across both `items` and `done` sections of ptl.yaml (note: meta.item_count only counts `items`; converter processes both). All significance values are PARADIGM or ROUTINE.

**Note on pending_items vs ptl_items:** These overlap — some items appear in both. The DB keeps them separate (different decay rules per protocol.md §5 vs §10). The `category` column on pending_items distinguishes outreach, awaiting, and rules items. No deduplication needed — they serve different purposes.

### Phase 3: L1 Redesign + Mode Profiles + Protocol Update (1 session)

**Deliverables:**
- MEMORY.md rewritten as pure index (target ≤140 lines) per L1 structure above. **Safety: write to MEMORY-NEW.md first, NOT directly to MEMORY.md. See Constraints § Rollback Safety for full protocol.**
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

**P8 — OPSEC isolation test (NEW — no baseline):**
FTS5 MATCH for "TQNN" — must NOT return Gjerloev approach_notes (compartmented, excluded at population). Query v_people_safe for Gjerloev — must NOT show approach_notes column. FTS5 MATCH for "scaffolding" — must NOT return gen-vc-scaffolding (compartmented). FTS5 MATCH for "EIN" — must NOT return reference-metatron-dynamics (compartmented). Query v_clearance_matrix — must show correct cleared/not-cleared for all Tier 1 people across ≥7 topics each. Verify repo privacy: `gh api repos/energyscholar/aurasys-memory --jq '.private'` = true.
Target: zero OPSEC leakage across all test vectors.

**Gate:** P1-P5 equal or exceed baselines. P6-P8 pass (no baseline comparison — these test new capabilities). Zero regressions. Compaction resilience proven (P2 ≥ B2).

**If gate passes:** Proceed to Phase 5 in this same session (no gap — contamination risk).

### Phase 5: Flat File Archival (same session as Phase 4)

**Immediately after Phase 4 gate passes AND Bruce approves:**
1. `git tag pre-flat-archive HEAD`
2. Move migrated flat files to `memory/archive/` (git-tracked, recoverable)
3. Write `memory/archive/README.md`: what these files are, why they're archived, how to recover (`git checkout pre-flat-archive -- memory/<file>` or rebuild from data scripts)
4. Update MEMORY.md file map to remove archived entries
5. Verify: all DB queries still return correct data
6. Verify: `rebuild-db.sh` produces identical DB from scripts alone

**NOT deleted:** Files listed in "What Stays Flat" section above. Specifically, `ptl.yaml` is NEVER archived — it remains the live write target for MCP tools. The DB table `ptl_items` is a read cache only.

**Repo-wide hygiene (separate plan):** Phase 0 B0 identified 30 top-level directories, ~470MB of non-memory content (session exports, old backups, training data). Plan 0312 (repo hygiene) should address this after Plan 0308 merge. Not in scope here — mixing concerns risks the retrofit.

---

## Risk Analysis

| Risk | Impact | Mitigation |
|------|--------|------------|
| Bug in argus.db affects ALL conversations | HIGH | Feature branch with per-phase commits (rollback to any phase). `pre-0308` tag on main. Dual-read period. Flat files preserved until Phase 5. |
| MEMORY.md redesign breaks always-loaded behavior | HIGH | Write to MEMORY-NEW.md first. Test in isolated shell. MEMORY-OLD.md kept for instant revert. Run P5 wiring test. |
| Split-brain: auto-memory writes .md, DB not updated | HIGH | ingest-memories.sh at session start + end. Source-of-truth hierarchy documented. DB is cache, data scripts are canonical. |
| Data loss during migration (parser misparsing) | MEDIUM | Row count verification per phase. Spot-check 5 random records. Source files preserved. Parser tested on 3 sample files before bulk run. |
| PTL migration breaks concurrent access | MEDIUM | PTL stays in YAML during migration. DB becomes authoritative only after both systems agree for 3+ sessions. |
| Protocol.md changes break session-end workflow | MEDIUM | Update protocol.md incrementally. Test session-end in isolation before committing. Old protocol.md preserved in git. |
| Concurrent rebuild while another shell queries DB | MEDIUM | rebuild-db.sh builds to .db.new → atomic mv. WAL mode for concurrent reads. |
| New memory type doesn't fit existing tables | LOW | ingest-memories.sh logs unrecognized types to ingest_log. Manual review at next maintenance. |
| Parser can't extract Why/How-to-apply from older files | LOW | Older memory files may not follow current frontmatter conventions. Parser falls back to full body as `content` field. Manual enrichment as maintenance task. |
| Schema too normalized — queries too complex | LOW | Follow Traveller pattern: views encapsulate joins. Query from views, not raw tables. |
| 164 files → DB migration takes longer than estimated | LOW | Parser script handles bulk. Sub-phase gates allow stopping and resuming. Each sub-phase independently valuable. |
| OPSEC leakage via FTS5 cross-domain query | HIGH | Compartmented records excluded from FTS5 at population time (safe by construction). Restricted records in FTS5 but gated by behavioral discipline (Correction #11). P8 test verifies. |
| Approach-strategy surfaced in general context | HIGH | approach_notes separated from description. v_people_safe excludes it. Only v_people_full exposes approach_notes (outreach prep). |
| Gen sees gen-vc-scaffolding via indirect access | MEDIUM | Classified compartmented. Excluded from FTS5, general queries, domain-mode loading. Snailmail replies must not reference it. |
| DB corruption goes undetected between sessions | MEDIUM | health-check.sh at session start (R1). Auto-rebuild from scripts. |
| Rebuild fails, loses both old and new DB | MEDIUM | Pre-rebuild backup (R2). Restore on failure. git checkout as last resort. |
| FK violations slip through during data load | MEDIUM | FK pragma in same connection as data (R3). Proven on Traveller. |
| Two shells run ingest simultaneously | MEDIUM | flock serialization (R5). Exit cleanly on lock contention. |
| DB becomes a single point of failure | HIGH | DB is a read cache, not source of truth (R4). Degradation = pre-0308 behavior. .md files always present. |

---

## Success Criteria

1. All structured data queryable via `sqlite3 ~/software/aurasys-memory/argus.db`
2. MEMORY.md ≤140 lines (down from 180)
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
17. health-check.sh detects all 3 failure modes (missing, corrupt, data loss) and auto-rebuilds (R1)
18. rebuild-db.sh creates backup before drop, restores on failure (R2)
19. FK enforcement works during load — bad FK rejected at load time, not just test time (R3)
20. Degradation path documented and tested — system functions without DB at pre-0308 capability (R4)
21. Concurrent ingest serialized via flock — no SQLITE_BUSY in multi-shell usage (R5)
22. Rebuild is fully deterministic — no manual steps, no external dependencies (R6)
23. DR protocol Tier 2.5 covers both campaign.db and argus.db (R7)
24. FTS5 full-text search returns relevant results across all entity tables (Layer 1 associative)
25. Associations table exists and accepts cross-entity links with valid CHECK constraints (Layer 2 associative — population is gradual, not gated)
26. OPSEC: compartmented records excluded from FTS5 index at population time (P8 test)
27. OPSEC: v_people_safe excludes approach_notes; approach_notes NOT in FTS5
28. OPSEC: person_clearances populated for all Tier 1 people with ≥7 topics each (≥49 rows)
29. OPSEC: gen-vc-scaffolding, metatron-dynamics, dressler-consulting NOT surfaced by FTS5 search (P8)
30. OPSEC: opsec-review.log and argus.db gitignored (meta-OPSEC and derived artifact not committed)
31. OPSEC: repo privacy verified (`gh api` returns `private: true`)

---

## Blocker: Traveller System Verification — CLEARED

**All blockers resolved (2026-05-08):**

1. Plan 0299 full data migration — complete and committed ✓
2. Plan 0309 (resilience hardening) — 6 phases complete, 6 FIXED, 12/12 tests ✓
3. Plan 0310 (data completeness) — 7 phases complete, 105 NPCs, 14/15 query gauntlet ✓
4. Plan 0311 (content inventory) — 6 phases complete, 93% manifest coverage ✓
5. Bruce stress-tested and explicitly approved ✓

**Sequence completed:** 0299 → 0309 → 0310 → 0311 → Bruce validates → **0308 READY**

**Auditor self-assessment (2026-05-08):** Frontmatter coverage: 121/130 files (93%). Body format consistency: 50/50 feedback files have Why, 48/50 have How-to-apply. Parser-driven migration is viable. One open concern: MCP PTL tools (see below).

---

## Constraints

### Branch & Merge

- **Feature branch:** `argus-memory-retrofit` off current `main`
- **Git tag `pre-0308`** on main before branching (emergency rollback snapshot)
- **Commits:** One per phase, format: `Plan 0308 Phase N: description`
- **Merge to main:** After Phase 4 integration testing passes AND Bruce approves. Merge commit (--no-ff) to preserve full phase history. Merge brings DB alongside unchanged flat files (dual-read on main).
- **Phase 5 immediately follows Phase 4** — archival in the SAME session as integration testing, after Bruce approves. No gap. Delay invites contamination (new .md files, flat/DB divergence). `pre-flat-archive` tag on main before archival.
- **Post-merge tag:** `post-0308` on main after merge (before Phase 5)

### Rollback Safety

- **Phases 0-2:** Rollback = checkout `pre-0308` tag or reset branch. No user-facing impact — DB is new artifact, .md files unchanged, MEMORY.md unchanged.
- **Phase 3 (L1 redesign) — HIGHEST RISK:** MEMORY.md rewrite affects ALL new sessions.
  - Write new L1 to `MEMORY-NEW.md` first (not directly to MEMORY.md)
  - Bruce reviews MEMORY-NEW.md
  - Back up: `cp MEMORY.md MEMORY-OLD.md`
  - Activate: `cp MEMORY-NEW.md MEMORY.md`
  - Test in fresh shell — verify session start, DB pointer, mode profiles, hot corrections
  - If broken: `cp MEMORY-OLD.md MEMORY.md` (instant revert)
  - Keep MEMORY-OLD.md in git until 3+ clean sessions confirm the new L1
- **Phase 5 (archival):** Rollback = `git revert` the archival commit. Archived files restored from git history.

### Idempotency & Determinism

- All scripts must be idempotent (re-runnable, identical result)
- `rebuild-db.sh` must produce identical DB from scripts alone — no manual steps, no external dependencies
- `ingest-memories.sh` must be deterministic (same input → same SQL output)
- `convert-ptl.py` must be deterministic (same ptl.yaml → same SQL output)

### Source Preservation

- No .md files deleted until Phase 5 (and only after Phase 4 passes + Bruce approves)
- During Phases 2-4: dual-read period — both .md files and DB coexist
- If .md file and DB row disagree: .md file wins (upstream source of truth)
- ptl.yaml is NEVER deleted, archived, or modified by migration scripts

### Testing

- All tests pass after every phase
- Phase gates must be verified before proceeding to next phase
- `rebuild-db.sh` must complete clean after each data migration sub-phase (2A, 2B, 2C)

### Working Directory & Generator Read Access

- Generator works in `~/software/aurasys-memory/` (the repo being modified)
- Generator reads plan from `~/software/relinquishment/plans/0308-aurasys-memory-retrofit.md` (full path)
- Generator MAY read `~/software/aurasys-memory/memory/*.md` files — this is an exception to the general Generator/aurasys-memory isolation rule, because Plan 0308 IS the aurasys-memory upgrade
- Generator must NOT modify `~/.claude/CLAUDE.md` — CLAUDE.md updates (if any) are a post-merge Auditor task
- Generator must NOT modify `tools/ptl-mcp/server.py` or `.mcp.json` — MCP server is unchanged

### Schema Stability

- Schema (table definitions, CHECK constraints) frozen after Phase 1 commit
- Data scripts, views, and FTS5 population may change in Phases 2-4
- Schema changes after Phase 1 require a plan amendment with Auditor approval

---

## Process Reference

Full migration playbook: `memory/project-db-migration-playbook.md`  
Plan 0299 execution results: `memory/project-0299-execution-results.md`  
Phase 3 report (requirements): `traveller-reference/PHASE-3-REPORT.md`  
**Traveller issue tracker: `traveller-reference/ISSUES.md`** ← stress test findings, resilience baselines  
**Plan 0309 (Traveller resilience): `plans/0309-traveller-resilience-hardening.md`** ← prerequisite  
**Gap analysis: in this file, "Gap Analysis" section above**  
Traveller metrics: `traveller-reference/metrics/`  
Manifest of manifests: `memory/reference-landmarks.md`
