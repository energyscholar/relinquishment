# Plan 0299 — Traveller Reference System (SQLite + Layered Prose)

**Author:** Argus (Auditor)
**Date:** 2026-05-06
**Domain:** Traveller Campaign A — ALL Traveller work (prep, live game, post-session)
**Status:** DRAFT v3.4 — iterative restructure (monolithic phases→iterative, Generator prompts realigned)
**Forerunner:** Test prototype for Plan 0300 (aurasys-memory retrofit)
**Prototype:** `/tmp/test-layered-ref/` — checksums + CRUD tested (15/15 pass)

---

## Problem

Argus assembles Traveller context ad hoc from 50+ files (~900K text). This produces confabulations (Anemone-as-AI, Ekuah selling a ship, wrong tonnages, FTL communication assumptions), wastes time re-discovering what to load, and can't answer relational queries in both directions (cultures→worlds AND worlds→cultures require separate index structures in flat files).

The campaign has **genuinely relational data**: cultures exist at multiple worlds, NPCs belong to organizations that span systems, ships move between locations, plot threads connect NPCs to systems. Plus 31 enriched star systems (with full stellar body maps) in JSON format in the VTT app repo, and ~400 canon Spinward Marches systems from published data. Flat files force a single index direction and can't enforce referential integrity.

---

## Objective

Build a **hybrid reference system**: SQLite database for relational data + checksummed prose files for narrative/procedural content. Queryable in any direction, self-maintaining, with full referential integrity.

Serves ALL Traveller work modes (prep, live GM, post-game, inter-session). 90% stable across sessions. Cleanly distinguishes canon (published Mongoose Traveller) from campaign extensions. Cooperates with context compaction by design.

---

## Architecture

```
L1: traveller-reference.md         ← MAP (index, always loaded, ~120-150 lines)
DB: campaign.db (SQLite)           ← RELATIONAL DATA (systems, NPCs, cultures, ships, orgs)
L2: traveller-reference/           ← PROSE FILES (voice guides, rules, pipeline, style)
L3: llm-knowledge-export/          ← DEEP PROSE (full rules, equipment catalogs)
L4: campaign root + session-prep/  ← DETAILED DOCS (ship audits, charts, session prep)
```

**What goes where:**

| SQLite (data) | Prose L2 (narrative) |
|---|---|
| Systems, UWPs, stellar bodies | Jumpspace mechanics explanation |
| Cultures, culture↔world links | What starport classes feel like |
| NPCs, locations, affiliations, voice profiles | Fiction voice guide, embellishment rules |
| Ships, tonnage, capabilities | NPC email system mechanics |
| Organizations, presence at worlds | Encounter design methodology |
| Anti-confabulation registry | Extraction template, pipeline docs |
| Plot threads, thread↔entity links | Quick rules at table speed |
| Content provenance log | Tech level narratives |

**Decision rule:** If the primary use is QUERYING (finding which entities have X property), put it in the DB. If the primary use is READING (understanding how X works narratively), keep it as prose.

**Access pattern:** Argus queries DB via `sqlite3` in bash. Reads prose files via Read tool. L1 references both with change-detection mechanisms (checksums for prose, summary stats for DB).

---

## Database Design

### Entity-Relationship Model

```
systems ──< stellar_bodies          (1 system has many bodies)
systems >──< cultures               (many-to-many via culture_at_world)
systems >──< organizations          (many-to-many via org_at_world)
systems ──< npcs                    (NPCs have a current_system)
species ──< npcs                    (NPCs have a species)
species ──< cultures                (cultures have a parent species)
organizations ──< npc_affiliations  (NPCs affiliated with orgs)
npcs >──< npcs                      (relationships via npc_relationships)
ships ──< npcs                      (crew assigned to ships)
plot_threads >──< entities          (threads connect to systems/NPCs/orgs via thread_connections)
```

### Source Provenance

Every row carries a `source` field:

| Source | Meaning | Mutability |
|--------|---------|------------|
| `canon` | Published Mongoose Traveller | Immutable — never modify |
| `environment` | Bulk campaign infrastructure (all SM stellar bodies) | Rarely changed |
| `prep` | Session-specific world-building | Updated during prep |
| `play` | Emergent from live game | Updated during/after sessions |

### GM-ONLY Marking

Tables with secrets have a `gm_secrets` TEXT column (nullable). NPC tables additionally have:
- `knowledge_level` — what this NPC knows about the campaign
- `opsec_notes` — what they'll share in email vs. in person (drives ORACLE mail system)

Fiction pipeline filters: `WHERE gm_secrets IS NULL` or extraction marks REDACT items.

### Scripted Setup (MANDATORY)

The DB file is a **build artifact**, not a source file. Scripts are the source of truth. Full rebuild at any time via `rebuild-db.sh`.

**Backup policy:** The DB IS committed to git. It's small (<1MB), provides instant disaster recovery, and doesn't make it the source of truth — scripts remain authoritative. If the DB diverges from scripts (e.g., post-session data not yet exported), the committed DB preserves that state. Scripts + committed DB = belt and suspenders.

**Script structure:**
```
traveller-reference/
  campaign.db                    ← BUILD ARTIFACT (committed for DR, scripts are source of truth)
  scripts/
    db-setup/
      MANIFEST.md               ← ordered list of schema scripts [sha:150498]
      001-pragma.sql             ← PRAGMA foreign_keys, journal_mode
      002-species.sql            ← species table
      003-systems.sql            ← systems table (with parsed UWP fields)
      004-stellar-bodies.sql     ← stellar_bodies (FK → systems, CASCADE)
      005-cultures-orgs.sql      ← cultures + organizations tables
      006-npcs.sql               ← NPC table (crew, PCs, external)
      007-ships.sql              ← ships table
      008-relationships.sql      ← junction tables (culture_at_world, org_at_world, affiliations, npc_relationships)
      009-operational.sql        ← confabulations, plot_threads, thread_connections, content_log
      010-views.sql              ← 8 views (v_crew, v_fleet, v_system_detail, v_confab_hot, v_active_voices, v_threads_active, v_culture_worlds, v_world_cultures)
      011-triggers.sql           ← auto-timestamp + provenance logging triggers
      setup.sh                   ← reads MANIFEST.md, runs scripts in order → creates campaign.db

    db-data/
      MANIFEST.md               ← ordered list of data scripts
      010-canon-species.sql      ← INSERT species (Human, Aslan, Vargr, etc.)
      011-canon-orgs.sql         ← INSERT organizations (TAS, IISS, Imperial Navy, megacorps)
      012-canon-systems.sql      ← INSERT systems (published UWP data)
      013-env-stellar.sql        ← INSERT stellar_bodies (GENERATED by import-enriched-systems.py from VTT JSON)
      014-canon-cultures.sql     ← INSERT cultures + culture_at_world
      020-campaign-npcs.sql      ← INSERT Campaign A NPCs (crew + external)
      021-campaign-ships.sql     ← INSERT ships (AD, Blood Fang, small craft)
      022-campaign-relationships.sql ← INSERT npc_relationships, npc_affiliations
      030-confabulations.sql     ← INSERT known confabulations (9+ entries)
      031-plot-threads.sql       ← INSERT plot threads + thread_connections
      load.sh                    ← reads MANIFEST.md, runs scripts in order

    rebuild-db.sh                ← rm campaign.db && setup.sh && load.sh && verify
    verify-integrity.sh          ← DB + prose checksum verification
    update-hash.sh               ← prose checksum helper
```

**Manifest of Manifests entry** (in `reference-landmarks.md`):
```
- DB setup manifest: traveller-reference/scripts/db-setup/MANIFEST.md
- DB data manifest: traveller-reference/scripts/db-data/MANIFEST.md
```

**Manifest gaps (to be resolved):**
- `scripts/tests/MANIFEST.md` — referenced in landmarks as "TBD, Phase 1A" but never written. 8 test scripts exist without a manifest. **Action:** Prompt B must write this manifest (checksummed list of test scripts). Update reference-landmarks.md entry from "TBD" to actual hash.
- Prose files (canon/, prep/, gm/, post/) — NO separate manifest. `traveller-reference.md` (L1 index) serves as the prose manifest via inline `[sha:XXXXXX]` checksums. This is by design: prose files are referenced inline in L1, not via a separate MANIFEST.md. The verify-integrity.sh script parses L1 for checksums.
- When `013-meta.sql` is added (Iteration 3), db-setup/MANIFEST.md hash changes → reference-landmarks.md TRAVELLER section hash must also update.

**Rebuild protocol:** `rm campaign.db && bash scripts/rebuild-db.sh` → identical DB every time.

**Post-session data flow:** New data from play → exported as new numbered data script (e.g., `040-session-12-updates.sql`) → added to data MANIFEST.md → DB remains reproducible.

**Rules:**
- Generator may NOT run raw `CREATE TABLE` or `INSERT` outside of scripts
- All schema changes → new setup script → update setup MANIFEST
- All data additions → new data script → update data MANIFEST
- Scripts are version-controlled; campaign.db is committed (DR backup, scripts remain source of truth)

### Schema Specification

**Plan-vs-implementation note:** The schema below was written before Phase 1A execution. The actual implementation split tables across more scripts than shown here (002-species.sql, 003-systems.sql, 004-stellar-bodies.sql, 005-cultures-orgs.sql, 006-npcs.sql, 007-ships.sql, 008-relationships.sql, 009-operational.sql, 010-views.sql, 011-triggers.sql). The table definitions are identical; only the file boundaries differ. The MANIFEST.md and actual scripts on disk are authoritative for file layout. The SQL below remains authoritative for table/column definitions.

The following SQL defines what the setup scripts must produce. Each section maps conceptually to script groups.

**001-pragma.sql:**
```sql
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
```

**002-entities.sql:**
```sql
-- ═══════════ ENTITIES ═══════════

CREATE TABLE species (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    source TEXT NOT NULL DEFAULT 'canon'
        CHECK(source IN ('canon','environment','prep','play')),
    summary TEXT,
    cultural_notes TEXT,
    updated_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE systems (
    hex TEXT PRIMARY KEY,        -- 4-digit location e.g. '1436'
    name TEXT NOT NULL,
    subsector TEXT,
    uwp TEXT,                    -- Universal World Profile
    starport TEXT,
    tech_level INTEGER,
    population_exp INTEGER,
    trade_codes TEXT,
    travel_zone TEXT DEFAULT 'Green'
        CHECK(travel_zone IN ('Green','Amber','Red')),
    allegiance TEXT,
    source TEXT NOT NULL DEFAULT 'canon'
        CHECK(source IN ('canon','environment','prep','play')),
    notes TEXT,
    gm_secrets TEXT,
    updated_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE stellar_bodies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    system_hex TEXT NOT NULL REFERENCES systems(hex) ON DELETE CASCADE,
    name TEXT NOT NULL,
    body_type TEXT NOT NULL
        CHECK(body_type IN ('star','planet','gas_giant','moon','belt','station','other')),
    orbit_number REAL,
    parent_body_id INTEGER REFERENCES stellar_bodies(id),
    features TEXT,
    source TEXT NOT NULL DEFAULT 'environment'
        CHECK(source IN ('canon','environment','prep','play')),
    updated_at TEXT DEFAULT (datetime('now')),
    UNIQUE(system_hex, name)
);

CREATE TABLE cultures (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    parent_species TEXT REFERENCES species(id),
    source TEXT NOT NULL DEFAULT 'canon'
        CHECK(source IN ('canon','environment','prep','play')),
    description TEXT,
    customs TEXT,
    taboos TEXT,
    updated_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE organizations (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    org_type TEXT,
    parent_org TEXT REFERENCES organizations(id),
    source TEXT NOT NULL DEFAULT 'canon'
        CHECK(source IN ('canon','environment','prep','play')),
    description TEXT,
    gm_secrets TEXT,
    updated_at TEXT DEFAULT (datetime('now'))
);

```

**003-npcs-ships.sql:**
```sql
CREATE TABLE npcs (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    species_id TEXT REFERENCES species(id),
    entity_type TEXT NOT NULL
        CHECK(entity_type IN ('human','robot','ai','alien')),
    is_crew INTEGER DEFAULT 0,
    is_pc INTEGER DEFAULT 0,
    current_system TEXT REFERENCES systems(hex),
    current_ship TEXT REFERENCES ships(id),
    role TEXT,
    status TEXT DEFAULT 'active'
        CHECK(status IN ('active','dormant','dead','departed','unknown')),
    source TEXT NOT NULL DEFAULT 'play'
        CHECK(source IN ('canon','environment','prep','play')),
    description TEXT,
    voice_profile TEXT,
    gm_secrets TEXT,
    knowledge_level TEXT,
    opsec_notes TEXT,
    updated_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE ships (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    ship_class TEXT,
    tonnage INTEGER NOT NULL,
    current_system TEXT REFERENCES systems(hex),
    captain_id TEXT REFERENCES npcs(id),
    is_fleet INTEGER DEFAULT 0,
    status TEXT DEFAULT 'active'
        CHECK(status IN ('active','destroyed','captured','unknown')),
    source TEXT NOT NULL DEFAULT 'play'
        CHECK(source IN ('canon','environment','prep','play')),
    description TEXT,
    hidden_capabilities TEXT,
    updated_at TEXT DEFAULT (datetime('now'))
);

```

**004-relationships.sql:**
```sql
-- ═══════════ RELATIONSHIPS ═══════════

CREATE TABLE culture_at_world (
    culture_id TEXT NOT NULL REFERENCES cultures(id) ON DELETE CASCADE,
    system_hex TEXT NOT NULL REFERENCES systems(hex) ON DELETE CASCADE,
    influence TEXT DEFAULT 'present'
        CHECK(influence IN ('dominant','significant','minority','traces','present')),
    source TEXT NOT NULL DEFAULT 'canon',
    notes TEXT,
    PRIMARY KEY (culture_id, system_hex)
);

CREATE TABLE org_at_world (
    org_id TEXT NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    system_hex TEXT NOT NULL REFERENCES systems(hex) ON DELETE CASCADE,
    facility TEXT,
    source TEXT NOT NULL DEFAULT 'canon',
    notes TEXT,
    PRIMARY KEY (org_id, system_hex)
);

CREATE TABLE npc_affiliations (
    npc_id TEXT NOT NULL REFERENCES npcs(id) ON DELETE CASCADE,
    org_id TEXT NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    role TEXT,
    is_secret INTEGER DEFAULT 0,
    source TEXT NOT NULL DEFAULT 'play',
    PRIMARY KEY (npc_id, org_id)
);

CREATE TABLE npc_relationships (
    npc1_id TEXT NOT NULL REFERENCES npcs(id) ON DELETE CASCADE,
    npc2_id TEXT NOT NULL REFERENCES npcs(id) ON DELETE CASCADE,
    relationship TEXT NOT NULL,
    is_mutual INTEGER DEFAULT 1,
    source TEXT NOT NULL DEFAULT 'play',
    notes TEXT,
    PRIMARY KEY (npc1_id, npc2_id, relationship)
);

```

**005-operational.sql:**
```sql
-- ═══════════ OPERATIONAL ═══════════

CREATE TABLE confabulations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_type TEXT NOT NULL,
    entity_id TEXT,
    wrong_claim TEXT NOT NULL,
    correct_fact TEXT NOT NULL,
    severity TEXT DEFAULT 'high'
        CHECK(severity IN ('critical','high','medium','low')),
    recurrence_count INTEGER DEFAULT 1,
    first_seen_session INTEGER,
    last_seen_session INTEGER,
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE plot_threads (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'active'
        CHECK(status IN ('active','dormant','resolved','cliffhanger')),
    priority TEXT DEFAULT 'normal'
        CHECK(priority IN ('critical','high','normal','background')),
    player_summary TEXT,
    gm_notes TEXT,
    created_session INTEGER,
    updated_session INTEGER,
    updated_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE thread_connections (
    thread_id TEXT NOT NULL REFERENCES plot_threads(id) ON DELETE CASCADE,
    entity_type TEXT NOT NULL
        CHECK(entity_type IN ('system','npc','org','ship')),
    entity_id TEXT NOT NULL,
    role TEXT,
    PRIMARY KEY (thread_id, entity_type, entity_id)
);

CREATE TABLE content_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_number INTEGER,
    table_name TEXT,
    entity_id TEXT,
    action TEXT CHECK(action IN ('insert','update','delete')),
    details TEXT,
    timestamp TEXT DEFAULT (datetime('now'))
);
```

**013-meta.sql** (added in Iteration 3 — export tracking):
```sql
CREATE TABLE db_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    updated_at TEXT DEFAULT (datetime('now'))
);
```
Used by `export-session.sh` to track `last_export_timestamp` and `last_export_session`. Backward-compatible (new table, no changes to existing tables).

### Views — `006-views.sql`

```sql
-- Everything at a system (prep + live GM)
CREATE VIEW v_system_detail AS
SELECT
    s.hex, s.name, s.uwp, s.starport, s.tech_level,
    s.trade_codes, s.travel_zone, s.source,
    (SELECT GROUP_CONCAT(c.name || ' (' || cw.influence || ')', ', ')
     FROM culture_at_world cw JOIN cultures c ON cw.culture_id = c.id
     WHERE cw.system_hex = s.hex) AS cultures,
    (SELECT GROUP_CONCAT(o.name || ' [' || ow.facility || ']', ', ')
     FROM org_at_world ow JOIN organizations o ON ow.org_id = o.id
     WHERE ow.system_hex = s.hex) AS organizations,
    (SELECT COUNT(*) FROM npcs n WHERE n.current_system = s.hex) AS npc_count,
    (SELECT COUNT(*) FROM stellar_bodies sb WHERE sb.system_hex = s.hex) AS body_count
FROM systems s;

-- Crew roster with type labels (anti-confabulation)
CREATE VIEW v_crew AS
SELECT n.name, n.entity_type, n.role, n.is_pc,
    sp.name AS species_name, n.description, n.voice_profile
FROM npcs n
LEFT JOIN species sp ON n.species_id = sp.id
WHERE n.is_crew = 1
ORDER BY n.is_pc DESC, n.entity_type, n.name;

-- Active NPCs with voice profiles (live GM — rotating top 10)
CREATE VIEW v_active_voices AS
SELECT n.name, n.entity_type, n.role, n.current_system,
    s.name AS system_name, n.voice_profile, n.opsec_notes
FROM npcs n
LEFT JOIN systems s ON n.current_system = s.hex
WHERE n.status = 'active' AND n.voice_profile IS NOT NULL
ORDER BY n.is_crew DESC, n.name;

-- Anti-confabulation hot list
CREATE VIEW v_confab_hot AS
SELECT wrong_claim, correct_fact, severity, recurrence_count
FROM confabulations
ORDER BY
    CASE severity WHEN 'critical' THEN 0 WHEN 'high' THEN 1
    WHEN 'medium' THEN 2 ELSE 3 END,
    recurrence_count DESC;

-- Active plot threads with connections
CREATE VIEW v_threads_active AS
SELECT pt.id, pt.title, pt.status, pt.priority, pt.player_summary,
    GROUP_CONCAT(tc.entity_type || ':' || tc.entity_id, ', ') AS connections
FROM plot_threads pt
LEFT JOIN thread_connections tc ON pt.id = tc.thread_id
WHERE pt.status IN ('active', 'cliffhanger')
GROUP BY pt.id
ORDER BY
    CASE pt.priority WHEN 'critical' THEN 0 WHEN 'high' THEN 1
    WHEN 'normal' THEN 2 ELSE 3 END;

-- Fleet ships
CREATE VIEW v_fleet AS
SELECT sh.name, sh.ship_class, sh.tonnage, sh.status,
    n.name AS captain_name, s.name AS location_name,
    sh.description, sh.hidden_capabilities
FROM ships sh
LEFT JOIN npcs n ON sh.captain_id = n.id
LEFT JOIN systems s ON sh.current_system = s.hex
WHERE sh.is_fleet = 1;

-- Culture distribution (culture → worlds)
CREATE VIEW v_culture_worlds AS
SELECT c.name AS culture, c.parent_species,
    GROUP_CONCAT(s.name || ' (' || cw.influence || ')', ', ') AS worlds
FROM cultures c
JOIN culture_at_world cw ON c.id = cw.culture_id
JOIN systems s ON cw.system_hex = s.hex
GROUP BY c.id;

-- World → cultures (reverse direction)
CREATE VIEW v_world_cultures AS
SELECT s.hex, s.name AS world,
    GROUP_CONCAT(c.name || ' (' || cw.influence || ')', ', ') AS cultures
FROM systems s
JOIN culture_at_world cw ON cw.system_hex = s.hex
JOIN cultures c ON cw.culture_id = c.id
GROUP BY s.hex;
```

### Triggers — `007-triggers.sql`

```sql
-- Auto-update timestamps
CREATE TRIGGER tr_systems_ts AFTER UPDATE ON systems
BEGIN UPDATE systems SET updated_at = datetime('now') WHERE hex = NEW.hex; END;

CREATE TRIGGER tr_npcs_ts AFTER UPDATE ON npcs
BEGIN UPDATE npcs SET updated_at = datetime('now') WHERE id = NEW.id; END;

-- (Similar triggers for all tables with updated_at: species, cultures, orgs, ships, stellar_bodies)

-- Provenance logging — covers ALL mutable entity tables.
-- export-session.sh depends on content_log completeness.
-- Current implementation: npcs (insert+update), ships (insert only).
-- REQUIRED (Iteration 3): Add insert/update/delete triggers for:
--   npcs, ships, systems, confabulations, plot_threads
-- These are the tables that change during play. species/cultures/orgs
-- change during prep (rare) — add if needed.

CREATE TRIGGER tr_npcs_log_insert AFTER INSERT ON npcs
BEGIN
    INSERT INTO content_log (table_name, entity_id, action, details)
    VALUES ('npcs', NEW.id, 'insert', NEW.name || ' (' || NEW.entity_type || ')');
END;

CREATE TRIGGER tr_npcs_log_update AFTER UPDATE ON npcs
BEGIN
    INSERT INTO content_log (table_name, entity_id, action, details)
    VALUES ('npcs', NEW.id, 'update', NEW.name || ' status=' || NEW.status);
END;

CREATE TRIGGER tr_npcs_log_delete AFTER DELETE ON npcs
BEGIN
    INSERT INTO content_log (table_name, entity_id, action, details)
    VALUES ('npcs', OLD.id, 'delete', OLD.name);
END;

-- (Similar insert/update/delete triggers for ships, systems,
--  confabulations, plot_threads — see 011-triggers.sql on disk)
```

---

## Manifest System (Separate from Memory)

The manifest system is **build infrastructure**, not knowledge management. It uses the same checksum pattern as the memory system but operates independently with zero-tolerance integrity requirements.

### Why Separate

Manifests guarantee reproducible builds. Memory manages degradable knowledge. If a manifest entry is wrong, the DB build breaks. If a memory entry is wrong, Argus writes a slightly less informed response. These are fundamentally different reliability tiers — mixing them makes build integrity depend on knowledge-management infrastructure.

### 2-Layer Structure

```
Layer 1: reference-landmarks.md (Manifest of Manifests)
  ├── [db-setup/MANIFEST.md] [sha:xxx] — 12 schema scripts (001-012), creates campaign.db structure
  ├── [db-data/MANIFEST.md] [sha:yyy] — N data scripts, populates campaign.db
  └── (future manifests: VTT import, prose build, etc.)

Layer 2: Individual MANIFEST.md files
  db-setup/MANIFEST.md:
    ├── [001-pragma.sql] [sha:aaa]
    ├── [002-species.sql] [sha:bbb]
    ├── [003-systems.sql] [sha:ccc]
    └── ... (12 scripts, each checksummed — see MANIFEST.md on disk for full list)

  db-data/MANIFEST.md:
    ├── [010-canon-species.sql] [sha:ddd]
    ├── [011-canon-orgs.sql] [sha:eee]
    └── ... (each script checksummed)
```

### Manifest Verification

Separate from memory/prose verification. Checks the full tree:

```bash
# verify-manifests.sh
# Phase 1: reference-landmarks.md → each MANIFEST.md exists + hash matches
# Phase 2: each MANIFEST.md → each script exists + hash matches
# Phase 3: scripts run in order without error (optional, slower)
# Exit: 0 = clean, 1 = stale hashes, 2 = missing files
```

**Integrity propagates up:** If a script changes → its MANIFEST checksum is stale → reference-landmarks.md entry is stale. Verification catches any break in the chain.

### MANIFEST.md Format

```markdown
# DB Setup Scripts — Execution Manifest

**Run order:** Sequential, top to bottom. Each script depends on prior scripts.
**Runner:** `setup.sh` (reads this file, executes in order)
**Rebuild:** `rebuild-db.sh` (drops DB, runs setup + data)

| # | Script | Hash | Purpose |
|---|--------|------|---------|
| 1 | 001-pragma.sql | [sha:abc123] | PRAGMA settings (FK enforcement, WAL mode) |
| 2 | 002-entities.sql | [sha:def456] | Core entity tables (species, systems, stellar_bodies, cultures, orgs) |
| 3 | 003-npcs-ships.sql | [sha:789abc] | NPC and ship tables |
| 4 | 004-relationships.sql | [sha:bcd012] | Junction tables (culture_at_world, org_at_world, affiliations) |
| 5 | 005-operational.sql | [sha:345def] | Confabulations, plot threads, content log |
| 6 | 006-views.sql | [sha:678abc] | All CREATE VIEW statements |
| 7 | 007-triggers.sql | [sha:901def] | Auto-timestamp and provenance triggers |
```

### Update Rules

- New script → add entry to MANIFEST → update MANIFEST hash in reference-landmarks.md
- Modified script → update script hash in MANIFEST → update MANIFEST hash in reference-landmarks.md
- Both steps in same session. Verification catches missed updates.
- `setup.sh` and `load.sh` parse the MANIFEST table, not hardcoded file lists

---

## VTT Star System Import Path

### Source Data

**Location:** `~/software/traveller-VTT-private/reference/BruceCampaignA/enriched-systems/`
**Format:** 31 JSON files (one per enriched system), e.g., `milagro.json`, `pagaton.json`, `tarkine.json`
**Scripts live in:** `~/software/traveller-VTT-private/` (same repo as the data — NOT in aurasys-memory)

### JSON Schema (observed)

System-level fields:
```
id, name, sector, subsector, hex, uwp, tradeCodes[], allegiance,
bases[], stellar{primary, type}, worlds, gasGiants, planetoidBelts,
notes, wikiUrl, enriched, enrichedDate, namingTheme,
locations[], celestialObjects[]
```

Each `celestialObject` entry:
```
id, name, type (Star|Planet|Gas Giant|Moon|Belt|Station),
orbitAU, bearing, radiusKm, transponder,
uwp (optional), atmosphere, breathable, inGoldilocks,
gmNotes, magnetosphere, cameraSettings{zoomMultiplier, offsetX, offsetY}
Stars additionally: stellarClass, stellarInfo{temperature, luminosity, mass, habitableZone, frostLine}
```

### Python Importer Design

**Script:** `import-enriched-systems.py` (in traveller-VTT-private repo)
**Reads:** All `enriched-systems/*.json`
**Outputs:** SQL insert scripts for `systems` table + `stellar_bodies` table
**Mapping:**
- JSON `hex` → `systems.hex` (PK)
- JSON `uwp` → `systems.uwp`; parse UWP for `starport`, `tech_level`, `population_exp`
- JSON `tradeCodes` → `systems.trade_codes` (joined string)
- JSON `allegiance` → `systems.allegiance`
- JSON `notes` → `systems.notes`
- JSON `celestialObjects[]` → `stellar_bodies` rows, with `system_hex` FK
- JSON `celestialObject.type` → mapped to `stellar_bodies.body_type` enum
- JSON `celestialObject.gmNotes` → `stellar_bodies.gm_notes`
- All rows get `source = 'environment'`

**UWP parse rule:** Standard Traveller UWP: `XNNNNNN-N` where X=starport (char), digits 1-6 are size/atmo/hydro/pop/gov/law, dash, digit 8 is tech level. Hex digits A-F map to 10-15.

**Idempotent:** Systems use `INSERT OR IGNORE` (canon systems in 012-canon-systems.sql must not be overwritten). Stellar bodies use `INSERT OR REPLACE` (safe to re-run — VTT bodies are always `source='environment'`). Net effect: re-running the importer after VTT data updates adds new bodies and updates existing ones, but never overwrites canon system data.

---

## Prose Reference Files (L2)

With data in the DB, prose files contain ONLY narrative/procedural content. ~14 files across 4 mode directories.

### Canon Prose — `traveller-reference/canon/`

| File | ~Lines | Contents |
|------|--------|----------|
| `jumpspace-and-travel.md` | 80 | How jump works narratively, 7-day transit feel, NO FTL COMMS, mail delays, fuel mechanics |
| `starports-and-trade.md` | 80 | What A/B/C/D/E/X starports feel like, trade code meanings, broker customs |
| `tech-levels.md` | 60 | What TLs mean for daily life, medicine, weapons, culture |
| `psionics.md` | 60 | How psionics work, illegality, training, Zhodani context |
| `imperium-and-politics.md` | 100 | Imperial structure as narrative context, noble protocol, client states |

### Prep Mode — `traveller-reference/prep/`

| File | ~Lines | Contents |
|------|--------|----------|
| `encounter-design.md` | 100 | NPC card format, scene structure, pacing, player spotlight matrix |
| `arc-planning.md` | 80 | Thread management, foreshadowing, cliffhangers |

### GM Mode — `traveller-reference/gm/`

| File | ~Lines | Contents |
|------|--------|----------|
| `email-system.md` | 80 | ORACLE mail mechanics, channel IDs, transit delay rules |
| `quick-rules.md` | 100 | Common DMs, task resolution, social checks |
| `dm-tables.md` | 80 | Range bands, damage multiples, common modifiers |

### Post-Game Mode — `traveller-reference/post/`

| File | ~Lines | Contents |
|------|--------|----------|
| `fiction-voice.md` | 100 | 10%/1% format, embellishment rules, exemplar analysis (S9/S10/S11 corrected) |
| `oracle-voice.md` | 60 | Ships log tone, ORACLE personality, redaction protocol |
| `extraction-template.md` | 60 | Per-session extraction format |
| `pipeline.md` | 60 | End-to-end post-session checklist |

**NPC voice profiles** are stored in `npcs.voice_profile` (DB), not in a separate prose file. The "rotating top 10" problem is solved by querying `v_active_voices`.

---

## L1 Index Design

**File:** `traveller-reference.md` (~120-150 lines, hard cap 160)
**Loads:** Always, at start of any Traveller work.

### Structure

```markdown
# Traveller Reference — Campaign A

**Session:** 11 | **Location:** Talos (1436) | **Mode:** [prep|live|post]
**Post-compaction:** Re-read this file FIRST. Then: `sqlite3 campaign.db "SELECT * FROM v_confab_hot;"`
**DB path:** ~/software/aurasys-memory/traveller-reference/campaign.db

## Anti-Confabulation (Hot List — from DB, verify each draft)
- Anemone Lindqvist = HUMAN (not robot/AI) — RECURRED 3x
- ISS Astral Dawn = 600t Q-ship (not warship, not 1000t)
- NO FTL COMMUNICATION — messages travel at ship speed
- [remaining critical+high entries from v_confab_hot]

## Database
campaign.db [sha:abc123] — 37 systems, 28 NPCs (7 crew), 17 ships, 10 cultures
  Query: sqlite3 campaign.db "SELECT * FROM v_system_detail WHERE hex='1436';"
  Views: v_crew, v_fleet, v_system_detail, v_active_voices, v_confab_hot, v_threads_active, v_culture_worlds, v_world_cultures
  Stats: species=7 | systems=37 | npcs=28 | ships=17 | orgs=18 | cultures=10 | confabs=9

## Load Profiles
  PREP:      DB queries (system, NPCs, threads) + canon/* + prep/*
  LIVE GM:   DB queries (NPCs, voices, OPSEC) + canon/[relevant] + gm/*
  POST-GAME: DB queries (crew, confabs) + canon/[relevant] + post/*

## Prose Files (checksummed)
### Canon
- [Jumpspace](canon/jumpspace-and-travel.md) [sha:______] — 7-day transit, NO FTL comms,
  fuel 10%/20%, 100-diameter limit, misjump. Load for: travel scenes, communication timing.
- [Starports](canon/starports-and-trade.md) [sha:______] — A-X classes, feel and culture of each.
- [Tech Levels](canon/tech-levels.md) [sha:______] — TL 0-15, daily life implications.
- [Psionics](canon/psionics.md) [sha:______] — Illegal, talents, Zhodani. Load for: Von Sydo scenes.
- [Imperium](canon/imperium-and-politics.md) [sha:______] — Structure, nobles, client states.

### Mode-Specific
- [Encounter Design](prep/encounter-design.md) [sha:______] — ...
  (remaining entries follow same pattern)

## L3/L4 Pointers (existence-checked)
- Ship audit: ~/software/traveller-VTT-private/reference/BruceCampaignA/astral-dawn-high-guard-audit.md
- NPC registry: ~/software/traveller-VTT-private/reference/BruceCampaignA/npc-registry.md
- Email log: ~/software/traveller-VTT-private/reference/BruceCampaignA/email-master-log.md
- Star system maps: ~/software/traveller-VTT-private/reference/BruceCampaignA/enriched-systems/ (31 JSON)
```

### Existence-Rich Entries (Prose Files)

Same pattern as prototype-tested: each entry carries enough to write correctly without loading L2. Richness proportional to `confabulation_risk × reference_frequency`.

### DB Summary Stats

L1 includes queryable summary stats for DB change detection:
```
Stats: species=7 | systems=37 | npcs=28 | ships=17 | orgs=18 | cultures=10 | confabs=9
```
Verification: `SELECT count(*) FROM systems; SELECT count(*) FROM npcs;` etc.
If stats match → DB hasn't changed, L1 summaries trustworthy.
If stats differ → re-query to identify what changed, update L1.

---

## Checksum + Integrity System

### Prose File Checksums

Same as prototype-tested system:
- `[sha:XXXXXX]` format (prefix prevents false matches — prototype-proven)
- File path regex requires `/` (prevents prose parenthetical matches — prototype-proven)
- Two-step update: edit L2 → update hash in L1 (or use `update-hash.sh` helper)

### DB Integrity

SQLite provides:
- `PRAGMA foreign_key_check;` — verifies all FK constraints
- `PRAGMA integrity_check;` — full DB structural integrity
- `PRAGMA foreign_keys = ON;` — enforces FK on every INSERT/UPDATE

### Combined Verification Script — `scripts/verify-integrity.sh`

```bash
#!/bin/bash
set -uo pipefail
BASE="$(cd "$(dirname "$0")/.." && pwd)"    # → traveller-reference/
REPO="$(cd "$BASE/.." && pwd)"              # → aurasys-memory/
INDEX="$REPO/traveller-reference.md"        # L1 index is at repo root, NOT inside traveller-reference/
DB="$BASE/campaign.db"

echo "=== Traveller Reference Integrity Check ==="

# Phase 1: DB integrity
echo "--- Database ---"
fk_errors=$(sqlite3 "$DB" "PRAGMA foreign_key_check;" 2>/dev/null | wc -l)
if [ "$fk_errors" -gt 0 ]; then
    echo "FAIL: $fk_errors foreign key violations"
    sqlite3 "$DB" "PRAGMA foreign_key_check;"
else
    echo "VALID: FK constraints clean"
fi
db_integrity=$(sqlite3 "$DB" "PRAGMA integrity_check;" 2>/dev/null)
[ "$db_integrity" = "ok" ] && echo "VALID: DB structure clean" || echo "FAIL: $db_integrity"

# Phase 2: DB summary stats vs L1
echo "--- DB Stats ---"
sys_count=$(sqlite3 "$DB" "SELECT count(*) FROM systems;")
npc_count=$(sqlite3 "$DB" "SELECT count(*) FROM npcs;")
confab_count=$(sqlite3 "$DB" "SELECT count(*) FROM confabulations;")
echo "  systems=$sys_count | npcs=$npc_count | confabs=$confab_count"
echo "  (Compare against L1 stats line — manual check for now)"

# Phase 3: Prose checksums (same algorithm as prototype)
echo "--- Prose Files ---"
valid=0; stale=0; missing=0; orphan=0
declare -a referenced_files=()
while IFS= read -r line; do
    file=$(echo "$line" | grep -oP '\(\K[a-zA-Z0-9_.-]+/[a-zA-Z0-9_./-]+\.md(?=\))' 2>/dev/null || true)
    expected=$(echo "$line" | grep -oP '\[sha:\K[a-f0-9]{6}(?=\])' 2>/dev/null || true)
    [ -z "$file" ] || [ -z "$expected" ] && continue
    referenced_files+=("$file")
    if [ ! -f "$BASE/$file" ]; then
        echo "  MISSING: $file"; missing=$((missing + 1)); continue
    fi
    actual=$(sha256sum "$BASE/$file" | cut -c1-6)
    if [ "$actual" != "$expected" ]; then
        echo "  STALE: $file (index=$expected actual=$actual)"; stale=$((stale + 1))
    else
        echo "  VALID: $file [$actual]"; valid=$((valid + 1))
    fi
done < "$INDEX"

# Phase 4: L3/L4 existence checks
echo "--- External References ---"
# Parse L3/L4 pointer lines and verify files exist
# (implementation: grep for .md files in the L3/L4 section, check existence)

# Summary
echo "=== Summary ==="
echo "  DB: FK=$fk_errors errors, structure=$db_integrity"
echo "  Prose: $valid valid, $stale stale, $missing missing"
```

### Self-Maintenance Protocol

1. **Session start:** Run `verify-integrity.sh`. Fix mismatches before work.
2. **After DB changes:** FK enforced automatically. Log triggers record changes.
3. **After prose edits:** Two-step hash update (or `update-hash.sh`).
4. **Session end:** Update `npcs.status`, `npcs.current_system` if game state changed. Run verification.
5. **Periodic (~5 sessions):** Review L1 existence-rich summaries. Check prose files under 200 lines. Prune `content_log` older than 10 sessions.

---

## Compaction Cooperation

### Compaction Indifference Architecture

The system is designed so compaction destroys only cached copies of data that is trivially re-queryable. No single compaction event can cause confabulation if the protocol is followed.

```
Layer            Compaction behavior         Recovery cost
───────────────  ──────────────────────────  ──────────────
CLAUDE.md        Never compacted             Zero
MEMORY.md        Never compacted             Zero
traveller-       Pointer in MEMORY.md        1 file read (~160 lines)
  reference.md   survives; content may
  (L1 index)     compact with context
L2 prose files   Compacted with context      1 file read per mode (~80 lines)
DB query results Compacted with context      1 bash call (~0.1s)
```

**Key invariant:** Everything above the compaction line (CLAUDE.md, MEMORY.md) contains pointers to everything below it. After compaction, Argus loses cached data but never loses the knowledge of *where to get it back*.

### Post-Compaction Recovery Protocol

When a continuation summary is detected (compaction happened):

1. **Immediately** read `~/software/aurasys-memory/traveller-reference.md` (L1). This restores: anti-confab hot list, all file pointers, DB query patterns, mode-specific load profiles, summary stats.
2. **Before writing any content**, re-query `v_confab_hot` to refresh the confabulation guard.
3. **Before referencing any NPC/ship/system by fact**, re-query the specific entity. Do not rely on compacted memory of prior query results.
4. **Re-read mode-specific prose** only for the current mode (prep, gm, or post — not all three).

### Query Discipline

- **Use results immediately.** Query the 3 NPCs needed for the current scene, write the scene, move on. Do not query 28 NPCs "for later."
- **Small queries = late compaction.** Loading 3 NPC rows (~80 tokens) vs. a full NPC markdown file (~2000 tokens) means compaction hits ~25x later. The DB's precision advantage compounds over a session.
- **Views for associative context.** When broader awareness matters (e.g., "who else is on the ship?"), use v_crew or v_fleet — they return richer joined data than raw table scans, at controlled size.
- **Never hold query results across conversation turns** expecting them to persist. Query → use → write output → done.

### L1 as the Compaction Contract

Any fact in L1 is a promise that it survives compaction (via MEMORY.md pointer → L1 re-read). If a fact isn't in L1 and it matters after compaction, it needs to be either:
- Added to L1 (if it's a recurring confabulation risk), or
- In the DB (queryable on demand after L1 tells Argus what to query)

Facts that exist ONLY in compacted conversation context are unrecoverable. The system must never depend on this.

### DB Advantage Over Flat Files

After compaction drops file content, re-reading a 200-line file costs context. Re-querying the DB for specific data (`SELECT name, entity_type FROM npcs WHERE is_crew=1`) returns only what's needed — no context waste on irrelevant content. The flat filesystem was compaction-vulnerable because recovery meant re-reading large files and hoping you knew which ones. The DB + L1 system is compaction-indifferent because recovery is: read 160 lines → query what you need.

---

## Pipeline: Creative Fiction

### Stage 0: Transcribe (automated)
`transcribe_all.py` chunks FLAC → transcribes → merges. ~15-20 min background.

### Stage 1: Extract (Auditor)
- Load L1 + query DB (`v_crew`, `v_confab_hot`)
- Read full transcript
- Produce extraction document: verified events, key dialogue, humor
- Cross-reference every name: `SELECT name, entity_type FROM npcs WHERE name LIKE '%search%';`
- Separate player-safe from GM-only

### Stage 2: Generate (Generator)
- Input: L1 + DB query results (crew, fleet, confab list) + prose files (fiction-voice.md) + extraction + exemplars (S9/S10/S11 corrected)
- Output: 10% creative fiction + 1% story blurb
- Rule: factual claims from extraction ONLY. Atmospheric embellishment from imagination.
- **Generator may NOT read the transcript directly**

### Stage 3: Verify (Auditor or automated)
- `SELECT name, entity_type FROM npcs;` → verify every name in draft matches
- `SELECT name, tonnage FROM ships WHERE is_fleet=1;` → verify tonnages
- `SELECT * FROM v_confab_hot;` → check no known errors repeated
- Flag any claim not traceable to extraction

### Stage 4: QC (Bruce)
- Reviews in Sublime, edits, approves
- Corrections → `INSERT INTO confabulations (...)`

### Stage 5: Package + Post (after approval only)
- ZIP: full transcript + 10% + 1%
- Post to Discord as file attachments

---

## Extraction Template

```markdown
# Session NN Extraction — [Title]
## Date / Location / Session Length

## Verified Events (chronological, timestamped)
- [HH:MM] Scene: [description]. Participants: [names]. Key facts: [details].

## Key Dialogue (from transcript)
- "[quote]" — Speaker, context

## Character Moments
## Humor / Personal / Romance
## Running Gag Updates

## Player-Safe vs GM-Only
- SAFE: [events players know]
- REDACT: [GM secrets — must not appear in fiction]

## Fact-Check List
- [ ] All names verified against DB (entity_type correct)
- [ ] Ship tonnages match DB
- [ ] No FTL communication assumed
- [ ] Message travel times realistic
- [ ] No confabulation registry entries repeated
```

---

## Test Harness

### Design Principles

Tests are **infrastructure**, not an afterthought. They run from `scripts/run-tests.sh` and gate every build step. No iteration is complete until its tests pass. Tests themselves are checksummed in a test MANIFEST.

The prototype at `/tmp/test-layered-ref/` proved that bash test suites catch real bugs (the `((var++))` trap, the bare-hash false positive, the path regex false match). This test harness scales that approach to cover DB + prose + manifests + importers.

### Test Architecture

```
traveller-reference/
  scripts/
    tests/
      MANIFEST.md                     ← checksummed list of all test scripts
      run-tests.sh                    ← master runner, parses MANIFEST, runs all, reports summary
      test-01-schema.sh               ← DB schema validation
      test-02-constraints.sh          ← FK + CHECK constraint enforcement
      test-03-views.sh                ← view correctness with known test data
      test-04-triggers.sh             ← auto-timestamp + provenance logging
      test-05-rebuild.sh              ← drop→rebuild reproducibility
      test-06-prose-checksums.sh      ← L1↔L2 checksum system (adapted from prototype)
      test-07-manifest-integrity.sh   ← manifest chain verification
      test-08-crud-lifecycle.sh       ← full entity lifecycle with cascade checks
      test-09-importer.sh             ← Python importer output validation
      test-10-confab-registry.sh      ← anti-confabulation priority ordering
      test-11-l1-existence-rich.sh    ← L1 carries enough to prevent known confabulations
      fixtures/
        test-system.json              ← minimal VTT-format JSON for importer testing
        expected-import.sql           ← expected importer output for diff
```

### Test Specifications

**test-01-schema.sh** — Schema Validation
- `PRAGMA table_info(X)` for every table → verify columns, types, defaults
- Verify all 15 tables exist (species, systems, stellar_bodies, cultures, organizations, npcs, ships, culture_at_world, org_at_world, npc_affiliations, npc_relationships, confabulations, plot_threads, thread_connections, content_log)
- Verify all 8 views exist (v_system_detail, v_crew, v_active_voices, v_confab_hot, v_threads_active, v_fleet, v_culture_worlds, v_world_cultures)
- Count: schema objects = 15 tables + 8 views + N triggers + N indexes
- Exit 0 if all present, exit 1 with list of missing objects

**test-02-constraints.sh** — Constraint Enforcement
- INSERT with invalid `source` value → must fail (CHECK constraint)
- INSERT with invalid `entity_type` → must fail
- INSERT NPC referencing nonexistent `species_id` → must fail (FK)
- INSERT `culture_at_world` referencing nonexistent `system_hex` → must fail (FK)
- INSERT with invalid `travel_zone` → must fail
- INSERT with invalid `body_type` → must fail
- DELETE system with stellar_bodies → CASCADE must delete bodies
- DELETE NPC with affiliations → CASCADE must delete affiliations
- Verify `PRAGMA foreign_keys` is ON
- Each test: attempt bad INSERT, capture exit code, assert failure

**test-03-views.sh** — View Correctness
- Insert known test data: 2 systems, 3 NPCs (1 PC, 1 crew, 1 external), 1 ship, 2 cultures, 1 org, 1 confab, 1 thread
- `v_crew` → returns exactly the crew members, species_name populated
- `v_system_detail` → cultures and organizations columns populated for test system
- `v_active_voices` → returns NPCs with voice_profile NOT NULL, status=active
- `v_confab_hot` → critical entries sort first, then by recurrence_count DESC
- `v_threads_active` → active/cliffhanger threads with connections
- `v_fleet` → fleet ships with captain and location names
- `v_culture_worlds` → correct GROUP_CONCAT of worlds per culture
- Clean up test data after (DELETE inserted rows, or use a temp copy of DB)

**test-04-triggers.sh** — Trigger Behavior
- INSERT NPC → verify `content_log` row exists with action='insert'
- UPDATE NPC status → verify `content_log` row with action='update'
- UPDATE NPC → verify `updated_at` changed (compare before/after)
- UPDATE system → verify `updated_at` changed

**test-05-rebuild.sh** — Reproducible Builds
- Run `rebuild-db.sh` → capture DB checksum (sha256sum campaign.db)
- Run `rebuild-db.sh` again → capture second checksum
- Assert checksums match (identical rebuild)
- Verify row counts match expected values from data scripts
- Verify `PRAGMA integrity_check` returns 'ok'
- Verify `PRAGMA foreign_key_check` returns empty (0 violations)

**test-06-prose-checksums.sh** — L1↔L2 Prose Integrity
- Adapted from prototype `verify-integrity.sh` (proven patterns)
- Parse L1 for `[sha:XXXXXX]` entries → verify each file exists and hash matches
- Test staleness detection: modify a prose file → verify script reports STALE
- Test missing detection: reference a nonexistent file → verify script reports MISSING
- Orphan detection: create file not in L1 → verify script reports ORPHAN
- Line cap enforcement: L1 < 160 lines, each L2 < 200 lines
- Uses `[sha:` prefix (prototype-proven, no false positives)
- Path regex requires `/` (prototype-proven, no parenthetical matches)

**test-07-nasty-insert.sh** — Constraint Enforcement (EXISTS — 288 lines)
Already written and passing. Tests invalid inserts, FK violations, CASCADE deletes, CHECK constraints. Covers the original test-02 and test-07 plan specs combined.

**test-08-performance.sh** — Query Performance (EXISTS — 196 lines)
Already written and passing. Tests view query performance and index effectiveness.

**test-09-importer.sh** — Python Importer Validation
- Skip (exit 77) if python3 not available or `fixtures/test-system.json` missing
- Run importer on `fixtures/test-system.json` (Milagro/1632, 18 celestial bodies)
- Structural validation (NOT exact diff — brittle to formatting changes):
  - Verify: output contains `INSERT OR IGNORE` for systems table
  - Verify: output contains `INSERT OR REPLACE` for stellar_bodies table
  - Verify: `source = 'environment'` appears on all rows (grep count matches row count)
  - Verify: all body_type values are in enum (star|planet|gas_giant|moon|belt|station)
  - Verify: system hex '1632' present, UWP fields parsed (starport='E', size=3, tech_level=7)
- Load generated SQL into a fresh temp DB (setup.sh on temp → run SQL → PRAGMA integrity_check + foreign_key_check)
- Verify row counts: 1 system, 18 stellar_bodies

**test-10-confab-registry.sh** — Anti-Confabulation
- Verify 3 critical confabs exist: Anemone=HUMAN (entity_id='anemone-lindqvist'), AD=600t (entity_id='astral-dawn'), NO FTL COMMS (wrong_claim LIKE '%FTL%')
- Verify v_confab_hot sort order: critical entries appear before high, high before medium
- Verify recurrence_count ordering within same severity level
- Cross-check against source tables: Anemone entity_type='human' in npcs, AD tonnage=600 in ships
- (Supersedes test-06-confab-guard.sh — which is replaced by prose-checksums in Iteration 3)

**test-11-l1-existence-rich.sh** — Compaction Resilience
- Parse L1 index text ONLY (no DB queries, no file loads)
- Can L1 alone answer: "Is Anemone human?" → grep for HUMAN
- Can L1 alone answer: "How big is the AD?" → grep for 600t
- Can L1 alone answer: "Can characters send FTL messages?" → grep for NO FTL
- Can L1 alone answer: "What mode should I use for post-game?" → grep for load profile
- Each answer must be derivable from L1 text without any other source
- This is the compaction survival test — if L1 alone can't prevent known confabulations, entries need enriching

### Test Runner — `run-tests.sh`

```bash
#!/bin/bash
set -uo pipefail
BASE="$(cd "$(dirname "$0")/.." && pwd)"
pass=0; fail=0; skip=0; total=0

echo "========================================"
echo "  Traveller Reference Test Suite"
echo "  $(date -Iseconds)"
echo "========================================"

for test_script in "$BASE/scripts/tests"/test-*.sh; do
    name=$(basename "$test_script" .sh)
    total=$((total + 1))
    echo ""
    echo "--- $name ---"
    if bash "$test_script" 2>&1; then
        echo "  PASS"
        pass=$((pass + 1))
    else
        exit_code=$?
        if [ "$exit_code" -eq 77 ]; then
            echo "  SKIP (precondition not met)"
            skip=$((skip + 1))
        else
            echo "  FAIL (exit $exit_code)"
            fail=$((fail + 1))
        fi
    fi
done

echo ""
echo "========================================"
echo "  RESULTS: $pass passed, $fail failed, $skip skipped (of $total)"
echo "========================================"
[ "$fail" -eq 0 ]
```

### Test Fixture — `fixtures/test-system.json`

Minimal VTT-format JSON matching the enriched-systems schema, with exactly 1 star + 2 planets + 1 gas giant. Known values enable deterministic expected-output comparison.

### Phase Gates

| Phase | Required Tests | Gate | Acceptance Criteria |
|-------|---------------|------|---------------------|
| Foundation (1A) | 01-08 | Schema, constraints, views, rebuild, manifests, performance | All 8 tests pass. Already committed. |
| Foundation (1B) | 01-10 | All DB tests pass including importer + confab registry | Tests 09 + 10 pass. stellar_bodies > 0. Test MANIFEST exists. |
| Iteration 1 | Bruce QC | Post-game fiction works | 4 post/* files, L1 ≤ 80 lines, S11 fiction zero confabs, Bruce approves. |
| Iteration 2 | P1 test | Prep mode works | 7 new prose files, L1 ≤ 120, P1 ≤ 8 tool calls. |
| Iteration 3 | 01-11 + P2-P4 | All modes + compaction resilient | 11 tests pass, P2 ≤ 5 calls, P3 zero confabs, P4 = P3. PHASE-3-REPORT.md written. |
| Iteration 4 | Wiring + SKILL tests | Fully integrated | Wiring 5/5, SKILL 5/5, MEMORY.md < 180 lines. |

### Regression Protocol

After any DB schema change, prose file edit, or manifest update:
1. Run `scripts/tests/run-tests.sh`
2. All tests must pass before committing
3. If a test fails after a change that should be valid → update the test, not the code
4. New confabulations discovered → add to test-10 + test-11

---

## Execution Status (as of 2026-05-08)

**What's committed (tag `pre-traveller-ref-v1`, branch `traveller-ref-phase1`):**
- Foundation: directory structure, 12 schema scripts (001-012), MANIFESTs, setup/load/rebuild scripts, verify-manifests.sh, 8 test scripts (01-08), run-tests.sh. All 8 tests passing.
- Data (partial): 9 data scripts. DB: 7 species, 37 systems, 28 NPCs, 17 ships, 18 orgs, 10 cultures, 9 confabs, 12 plot threads. **stellar_bodies = 0** (importer not yet written).

**What's remaining:** 4 iterations, each tested before proceeding.

---

## Iteration Plan

### Design Principle: Build One Mode, Test It, Learn, Expand

The old plan built ALL prose and infrastructure before testing with real work. The iterative plan tests each GM mode end-to-end before building the next. Lessons from each iteration inform the next iteration's prompts — later prompts are written AFTER earlier iterations complete.

```
Foundation (DONE) ──→ Iter 1: POST-GAME ──→ Iter 2: PREP ──→ Iter 3: LIVE+INFRA ──→ Iter 4: INTEGRATE
     schema+data        4 prose, L1 min       7 prose, L1 exp   3 prose, sync, tests   MEMORY + SKILL
                        S11 fiction test       S12 prep test     compaction tests        wiring test
                        Bruce QC              ≤8 tool calls     P3/P4 zero confabs      5-mode activation
```

### Step 0: Baseline Measurement (BEFORE any Generator runs)

Run baseline tests B0-B3 (see "Metrics and Evaluation" section) with the CURRENT system. This is our scientific control — without it, we can't prove the new system is better, only claim it.

**B0 (health):** automated script, ~30 seconds.
**B1 (post-game):** fresh shell, S11 fiction with flat files only. ~15 minutes. Most important baseline.
**B2 (prep):** fresh shell, S12 prep with flat files. ~10 minutes.
**B3 (live GM):** fresh shell, combat adjudication. ~5 minutes.

**Gate:** All 4 baseline YAML files saved in `traveller-reference/metrics/` before Foundation begins.

---

### Foundation: Remaining Infrastructure

**Scope:** Complete Phase 1B. Not mode-specific — fills the DB that all iterations use.

**Prompt A** — Python VTT Importer (unchanged from v3.3, see Generator Handoff Prompts below)
- Writes `import-enriched-systems.py` in traveller-VTT-private repo
- Generates `013-env-stellar.sql` (~475 stellar bodies from 31 enriched systems)
- Fills stellar_bodies table (currently 0 rows)
- Tag before: `pre-traveller-ref-v1` (already exists)

**Prompt B** — Tests 09-10 + Test MANIFEST (unchanged from v3.3)
- Writes test-09-importer.sh, test-10-confab-registry.sh
- Writes scripts/tests/MANIFEST.md (checksummed list of all 10 test scripts)
- Updates reference-landmarks.md test MANIFEST entry from "TBD" to actual hash
- Tag after: `traveller-ref-foundation-complete`

**Foundation gate:** All 10 tests pass. stellar_bodies > 0. Test MANIFEST exists with valid checksums.

---

### Iteration 1: Post-Game MVP

**Goal:** Produce S11 fiction with zero confabulations using the reference system. Bruce QC.

**Why first:** Post-game fiction is the highest-value mode (professional output, ~$90/session) and highest-risk mode (where confabulations actually happen — Anemone-as-robot, wrong tonnages). Testing this first validates the core architecture before expanding.

**Scope (4 prose files + minimal L1 + fiction test):**

1. Write `post/fiction-voice.md` (~100 lines)
   - **CRITICAL:** Read `ships-log-player-summaries.md` (344 lines) FIRST
   - Identify ≥3 structural patterns, codify as reproducible rules
   - Include ≥3 verbatim annotated exemplar excerpts
   - "Write literary SF" is NOT a voice guide. Specific patterns with examples ARE.

2. Write `post/oracle-voice.md` (~60 lines)
   - Source: ORACLE sections in ships-log-player-summaries.md + oracle-comms-log.md

3. Write `post/extraction-template.md` (~60 lines)
   - Source: transcript-pipeline.md

4. Write `post/pipeline.md` (~60 lines)
   - Source: post-session-process.md

5. Write minimal `traveller-reference.md` (L1 index, POST-MODE ONLY):
   - Anti-confab hot list (from v_confab_hot critical+high)
   - DB path + view list + example queries
   - Post-mode load profile ONLY
   - Prose checksums for post/* files only
   - HARD CAP 80 lines (half budget — room to grow in later iterations)

6. S11 Extraction (Auditor):
   - Load L1 + query DB (v_crew, v_confab_hot)
   - Read full transcript (3230 lines)
   - Produce extraction per extraction-template.md format
   - Cross-reference EVERY name against DB
   - Output: `session-prep-s11/s11-extraction.md`

6b. Extraction Validation (Auditor, before fiction):
   - Verify every name in extraction exists in DB: `SELECT name, entity_type FROM npcs WHERE name LIKE '%X%';`
   - Verify every ship in extraction matches DB tonnage: `SELECT name, tonnage FROM ships;`
   - Grep extraction for v_confab_hot wrong_claim patterns — zero matches required
   - Flag any claim not directly traceable to a transcript timestamp
   - **This step catches extraction confabulations before they reach the fiction Generator.**

7. S11 Fiction (Generator):
   - Input: L1 + DB queries + fiction-voice.md + extraction + exemplars
   - Output: `session-prep-s11/transcripts/s11-10pct-v2.txt` + `s11-1pct-v2.txt`
   - Factual claims from extraction ONLY

8. Verification (Auditor):
   - Every name → DB entity_type check
   - Every tonnage → DB ships check
   - Every system → DB systems check
   - v_confab_hot grep against draft — zero matches
   - Count: factual errors, confabulations, invented events

9. Comparison + Bruce QC:
   - Diff against existing 10% (128 lines) and 1% (4 lines)
   - Existing files: `session-prep-s11/transcripts/s11-talos-may05-2026_{ten,one}-percent-transcript.txt`
   - Bruce reviews side by side. Catches style only, not facts.
   - Any factual error → new confab registry entry

**Iteration 1 prompt:** Written in full below (see Prompt I1). Steps 1-5 are one Generator shell. Steps 6-8 are Auditor work. Step 7 is a separate Generator shell (Prompt I1-G).

**Iteration 1 gate:**
- 4 post/* prose files exist, each ≤ line cap
- fiction-voice.md has ≥3 annotated exemplars
- L1 index exists, ≤ 80 lines, anti-confab list populated
- S11 fiction: zero confabulations
- Bruce approves v2 as ≥ existing quality

**Lessons captured:** After Bruce QC, document:
- Did fiction-voice.md produce the right voice? What needs adjusting?
- Did the L1 anti-confab list catch everything? Missing entries?
- Did the extraction template capture enough? Too much?
- How many tool calls for the full post-game pipeline?
- These findings inform Iteration 2 prose writing.

---

### Iteration 2: Prep Mode

**Goal:** Plan S12 session prep from scratch using DB + prose. ≤8 tool calls to useful output.

**Why second:** B2 baseline showed 18 tool calls, 15% file waste, 4 confabs — all from hunting across flat files. Prep mode benefits most from structured canon prose + DB queries replacing ad hoc file discovery. Building this after Iter 1 means the L1 index and DB query patterns are already proven.

**Scope (7 prose files + L1 expansion + validation):**

1. Write 5 canon/* prose files (each sourced from specific extraction files):
   - `jumpspace-and-travel.md` (~80 lines) — SOURCE: `09-spacecraft-operations-trade.md` (trade/fuel/jump). NO FTL COMMS, 7-day transit, fuel 10%/20%, 100-diameter limit, misjump. Cross-check confab registry for FTL entries.
   - `starports-and-trade.md` (~80 lines) — SOURCE: `09-spacecraft-operations-trade.md` (trade codes), `18-world-creation.md` (starport classes A-X, facilities).
   - `tech-levels.md` (~60 lines) — SOURCE: `18-world-creation.md` (TL tables). TL 0-15, daily life implications, manufacturing limits.
   - `psionics.md` (~60 lines) — SOURCE: `05-psionics-rules.md`. Illegal in Imperium, Zhodani exception, talents, PSI characteristic, detection.
   - `imperium-and-politics.md` (~100 lines) — SOURCE: `02-universe-spinward-marches.md` + `01-rules-reference.md` (noble ranks). Imperial structure, client states, megacorps, subsector politics.
   - EDITION LOCK: MgT2e ONLY. [VERIFY] if uncertain — check extraction file page citations.

2. Write 2 prep/* prose files:
   - `encounter-design.md` (~100 lines) — SOURCE: `session-prep-gap-analysis-s7-s9.md` (334 lines, pattern analysis). Also review s11-session-plan.md and s12-session-plan.md for what worked.
   - `arc-planning.md` (~80 lines) — SOURCE: `campaign-arc-endgame.md` (260 lines) + `thread-map.md` (220 lines). ALSO query: `SELECT * FROM v_threads_active;` to verify thread list is current.

3. Expand L1 index:
   - Add canon/* and prep/* prose sections with checksums
   - Add PREP load profile
   - Update summary stats
   - CAP: 120 lines (room for Iter 3)

4. Canon validation (Auditor, before P1 test):
   - Verify jumpspace-and-travel.md against confab registry: `SELECT wrong_claim FROM confabulations WHERE wrong_claim LIKE '%FTL%' OR wrong_claim LIKE '%instant%';` — prose must contradict every wrong_claim.
   - Spot-check 3 page citations per file against extraction source.
   - Verify imperium-and-politics.md factions against DB: `SELECT name, org_type FROM organizations;` — no invented factions.
   - Verify arc-planning.md threads against DB: `SELECT title, priority, status FROM plot_threads;` — no missing high-priority threads.

5. Test P1: Prep Efficiency + Accuracy
   - New shell. "Plan session 12 at Collace."
   - Efficiency target: ≤8 tool calls to useful session plan
   - Record every tool call with purpose
   - Accuracy check (Auditor after P1): verify P1 output against DB
     - All NPCs mentioned exist: `SELECT name, entity_type FROM npcs;`
     - Collace data matches: `SELECT * FROM v_system_detail WHERE hex='1237';`
     - No stale data from flat files (the B2 failure mode — collace.json errors)
   - Compare against B2 baseline: tool calls, waste%, confabs

**Iteration 2 gate:**
- 7 new prose files exist, each ≤ line cap
- L1 expanded, ≤ 120 lines
- Canon validation passes (step 4 — no confabs in canon prose)
- P1 test: ≤8 tool calls to useful output
- P1 accuracy: zero confabs in session prep output
- No [VERIFY] on critical facts (jumpspace, FTL, fuel)
- iter2.yaml saved with metrics, compared against B2

**Lessons captured:** After P1 test, document:
- Did the L1 PREP load profile direct the instance correctly?
- Which canon files were loaded? Which were skipped? Appropriate?
- Did the instance query DB or fall back to flat files?
- How many tool calls vs B2 baseline (target: 18 → ≤8)?
- Was any prep-relevant information missing from the canon prose?
- These findings inform Iteration 3 prompt writing.

**Prompt:** Written AFTER Iteration 1 completes, incorporating lessons learned. Scope defined above; exact prompt informed by Iter 1 results.

---

### Iteration 3: Live GM + Infrastructure

**Goal:** Complete all prose, add sync infrastructure, run compaction tests.

**Scope (3 prose files + sync scripts + remaining tests + compaction):**

1. Write 3 gm/* prose files:
   - `email-system.md` (~80 lines) — source: oracle-npc-mail-profiles.md, oracle-mail-queue.md
   - `quick-rules.md` (~100 lines) — source: vtt-combat-reference.md. MgT2e ONLY.
   - `dm-tables.md` (~80 lines) — source: vtt-combat-reference.md. Exact numbers, no approximation.

2. Complete L1 index:
   - Add gm/* prose + LIVE load profile
   - Add L3/L4 pointers (existence-checked)
   - Add Common Queries section
   - FINAL CAP: 160 lines

3. Infrastructure scripts:
   - `013-meta.sql` (db_meta table for last-export tracking)
   - `011-triggers.sql` UPDATE: extend content_log triggers to cover ships (update+delete), systems (insert+update+delete), confabulations (insert+update+delete), plot_threads (insert+update+delete). Currently only npcs (insert+update) and ships (insert) are logged.
   - `export-session.sh` (live DB changes → versioned data script; handles INSERT OR REPLACE for changed entities AND DELETE for removed entities)
   - `gen-world-brief.sh` (DB + prose → session prep brief)
   - `verify-integrity.sh` (DB + prose checksum verification)
   - `update-hash.sh` (prose checksum helper)
   - ~~export-for-web.sh~~ DEFERRED — build when Claude web export is needed
   - ~~check-sync.sh~~ DEFERRED — no export = no sync check needed

4. Remaining tests:
   - Replace test-06 (confab-guard → prose-checksums)
   - Write test-11 (L1 existence-rich)

5. Compaction tests:
   - P3: fresh shell writes S11 10% → zero confabs
   - P4: same shell after forced compaction → identical quality
   - P2: fresh shell adjudicates personal combat → correct DM in ≤5 calls

6. **PHASE-3-REPORT.md** — requirements document for Plan 0300:
   - Test results table (P1-P4)
   - Tool call audit per mode
   - Gap analysis
   - Recommendations for memory retrofit

**Iteration 3 gate:**
- All 11 tests pass
- All prose files complete (14 total)
- L1 complete, ≤ 160 lines
- P2 correct DM ≤5 calls, P3 zero confabs, P4 = P3
- PHASE-3-REPORT.md written
- `scripts/collect-metrics.sh` operational
- iter3.yaml saved with all CR/EF/QA/CP/SH metrics, compared against baselines

**Prompt:** Written AFTER Iteration 2 completes.

---

### Iteration 4: Integration + SKILL

**Goal:** Wire into memory architecture. Replace stale SKILL.md. Final gates. End-to-end proof.

**Why last:** Integration touches MEMORY.md, SKILL.md, and feedback files — shared infrastructure that affects all projects. These changes must only happen after the reference system is proven through Iterations 1-3. If Iter 3 fails, we don't want half-wired memory pointers.

**Scope:**

1. **MEMORY.md wiring:**
   - Add traveller-reference.md to File Map (under traveller-campaign.md)
   - Update traveller-campaign.md: add DB pointer (`campaign.db`), post-compaction protocol ("After compaction: re-read L1, re-query v_confab_hot and v_crew before generating"), mode-switching instructions
   - Line budget: MEMORY.md currently ~176 lines. Adding 2 lines → 178. If >180, archive oldest ROUTINE session from session-details.md first.
   - Verify MEMORY.md < 180 lines, L1 ≤ 160 lines

2. **SKILL.md v2.0:**
   - Back up current SKILL.md: `cp ~/.claude/skills/traveller/SKILL.md ~/.claude/skills/traveller/SKILL.md.v1.bak`
   - Rewrite using template in "SKILL Module Architecture" section of this plan
   - Verify backup at `claude-backup/global/skills/` exists before deleting: `ls ~/software/aurasys-memory/claude-backup/global/skills/traveller/` — if exists and matches v1, delete. If not found, skip (no blind deletes).
   - Note: craft/ directory (Layer 1 GM Craft) is FUTURE — SKILL.md references it but files are TBD. The prep/encounter-design.md and prep/arc-planning.md from Iter 2 are prep-mode files, not craft files. SKILL.md should note craft/ as "planned" not "available".

3. **Thin session prep template:** `prep/session-template.md` (~40 lines)
   Format:
   ```markdown
   # S[N] Session Prep — [Location]
   <!-- Generated: query v_system_detail WHERE hex='XXXX' -->
   ## Decisions (Bruce)
   - [open questions for GM]
   ## Scenes (3-5)
   - Scene 1: [hook, NPCs involved, location]
   ## Active Threads at [Location]
   <!-- Generated: query v_threads_active filtered by location -->
   ## NPCs Present
   <!-- Generated: query npcs by last_location or affiliation -->
   ## Notes
   ```

4. **Archive headers** on bloated session-prep-s09/s10/ files:
   Format: `<!-- ARCHIVED: Historical session prep. Current prep uses thin template + DB queries. -->`
   Add to top of each .md file in s09/ and s10/ directories. Do NOT delete content.

5. **Update feedback-traveller-extraction.md** for DB-first workflow:
   - Change: "read flat files" → "query campaign.db"
   - Change: "check ships-log for facts" → "check extraction against DB (entity_type, tonnage, confab registry)"
   - Add: "Every name in extraction must verify against `SELECT name, entity_type FROM npcs;`"
   - Add: "Post-compaction: re-read L1 before writing fiction"

6. **Wiring test (PASS/FAIL):**
   - New shell (no prior Traveller context). Prompt: "I need to prep for Traveller session 12."
   - Expected wiring path: MEMORY.md (auto-loaded) → traveller-campaign.md mentions DB → instance reads traveller-reference.md (L1) → queries campaign.db
   - Criteria:
     a. Must reach traveller-reference.md within 3 tool calls
     b. Must query campaign.db within 6 tool calls
     c. Must NOT load old llm-knowledge-export campaign state files (04a, 05, 08, 09, 10) — should query DB instead
     d. Must load correct mode prose (prep/*) not wrong mode (gm/*, post/*)
     e. Session prep output has zero confabs (verified against DB)

7. **SKILL activation tests (5 modes):**
   - `/traveller prep` → loads L1 + prep/* + DB. NOT gm/*, post/*.
   - `/traveller live` → loads L1 + gm/* + DB. NOT prep/*, post/*.
   - `/traveller post` → loads L1 + post/* + DB. NOT prep/*, gm/*.
   - `/traveller rules personal combat` → finds correct rules file in ≤2 calls.
   - `/traveller query SELECT * FROM v_crew;` → runs query, returns result.

8. **Deactivation test:**
   - In same shell after SKILL test: "Done with Traveller. What's the status of Plan 0296?"
   - Instance must NOT reference Traveller vocabulary (parsec, jump, ORACLE) in response
   - Instance must NOT query campaign.db for non-Traveller work
   - Instance must treat Relinquishment/book context as separate domain

9. **End-to-end proof (capstone):**
   - Fresh shell, no prior context. `/traveller post`
   - Task: "Write S11 10% literary SF summary"
   - Provide transcript when asked. Do NOT provide extraction or flat files.
   - Instance must: load L1 → query DB → read post/fiction-voice.md → build extraction → write fiction
   - Auditor QC: compare CR-total against B1 baseline (target: 5 → 0)
   - This is the ultimate proof: new system vs old system, same task, measured comparison.

**Iteration 4 gate:**
- Wiring test passes (all 5 criteria)
- All 5 SKILL activation tests pass
- Deactivation test passes (no vocabulary bleed)
- End-to-end proof: CR-total ≤ 1 (vs B1 baseline of 5)
- MEMORY.md < 180 lines
- Thin template written, archives marked
- iter4.yaml saved with all metrics, full baseline comparison table
- SKILL.md.v1.bak exists as rollback

**Rollback:** If SKILL.md v2 breaks activation tests: `cp ~/.claude/skills/traveller/SKILL.md.v1.bak ~/.claude/skills/traveller/SKILL.md` and diagnose. Do not iterate on a broken SKILL.md — revert, fix the plan, re-deploy.

**Prompt:** Written AFTER Iteration 3 completes.

---

### Phase Gates Summary

| Phase | Required | Gate | Acceptance |
|-------|----------|------|------------|
| Baseline | B0-B3 tests | Current system measured | 4 YAML files in metrics/, B1 CR-total recorded |
| Foundation | Tests 01-10 | Importer works, test MANIFEST exists | stellar_bodies > 0, all 10 tests pass |
| Iteration 1 | Bruce QC + metrics | Post-game fiction works | Zero confabs, Bruce approves, iter1.yaml vs B1 |
| Iteration 2 | P1 test + canon validation + metrics | Prep mode works | ≤8 tool calls, zero confabs in canon + P1 output, iter2.yaml vs B2 |
| Iteration 3 | Tests 01-11, P2-P4, metrics | All modes + compaction resilient | 11 tests pass, P3 zero confabs, P4=P3, full comparison |
| Iteration 4 | Wiring + SKILL + deactivation + E2E proof | Fully integrated | Wiring 5/5, SKILL 5/5, deactivation clean, E2E CR ≤ 1, MEMORY.md < 180 |

---

## Success Criteria

1. Zero confabulations of character type (human/robot/AI) — DB enforces entity_type
2. Zero confabulations of ship tonnage — DB enforces tonnage field
3. Zero FTL communication assumptions — confab registry flags this
4. Zero confabulated plot events
5. Bruce QC catches only style issues, not factual errors
6. Query in BOTH directions: cultures→worlds AND worlds→cultures
7. Referential integrity: DB FK constraints prevent orphaned references
8. Canon clearly distinguished from campaign extensions (`source` field)
9. Pipeline runs end-to-end in under 30 minutes
10. **Compaction resilience:** L1 + DB queries recover full precision
11. **Mode switching:** Prep/live/post loads the right context without manual prompting
12. **SKILL activation:** `/traveller` loads three-layer stack, instance can prep/adjudicate/write without prior campaign context
13. **Prep efficiency:** <8 tool calls for full session prep context (Test P1)
14. **Post accuracy:** zero confabulations in first draft 10% summary (Test P3)
15. **Upgrade path:** new sourcebook content addable via plugin protocol without structural changes
16. **Clean deactivation:** "Done with Traveller" stops campaign vocabulary bleed into other domains
17. **End-to-end proof:** Fresh shell + `/traveller post` → S11 fiction with CR-total ≤ 1 (vs B1 baseline of 5)
18. **Measurable improvement:** Every iteration metric improves over corresponding baseline (B1-B3)

---

## SKILL Module Architecture

### What We're Building

Not just a reference database — a **skill module**. When `/traveller` fires, the instance becomes a capable GM with layered knowledge. The SKILL.md at `~/.claude/skills/traveller/SKILL.md` is the entry point.

### Three-Layer Skill Stack

```
Layer 1: GM Craft (system-agnostic, ~40% proficiency, upgradable)
  ├── traveller-reference/craft/  (NEW — general RPG GM methodology)
  ├── encounter design, pacing, spotlight, arc planning
  ├── post-session write-up methodology (10%/1% format)
  └── applies to: any RPG, any campaign

Layer 2: MgT2e Canon (system-specific)
  ├── llm-knowledge-export/ rules files (16,382 lines, 22 files)
  ├── traveller-reference/canon/ prose (jumpspace, starports, TL, psionics, imperium)
  ├── lookup table in SKILL.md
  └── edition-locked: Mongoose Traveller 2e ONLY

Layer 3: Campaign A (campaign-specific)
  ├── campaign.db (queryable relational data)
  ├── traveller-reference.md (L1 index: anti-confab, load profiles, DB pointer)
  ├── traveller-reference/{prep,gm,post}/ mode prose
  └── VTT repo deep reference (world files, session prep, combat cards)
```

### SKILL.md Redesign

Current SKILL.md (62 lines, stale at session 5) is rules-lookup only. Redesign as unified entry point:

```markdown
---
name: traveller
description: "Traveller GM skill module. Loads layered knowledge: GM craft → MgT2e rules → Campaign A data. Use for any Traveller RPG work."
argument-hint: "[prep|live|post|rules <topic>|query <sql>]"
version: 2.0
skill-proficiency: 40%
upgradable: true
---

# Traveller GM — Skill Module v2.0

## On Activation

1. Read L1 index: ~/software/aurasys-memory/traveller-reference.md
2. Note current mode from L1 header (prep|live|post)
3. Load anti-confabulation hot list (in L1)
4. DB is queryable at: ~/software/aurasys-memory/traveller-reference/campaign.db

## Mode-Specific Loading

| Mode | Load | Don't Load |
|------|------|-----------|
| PREP | canon/* + prep/* + DB(systems, NPCs, threads) | gm/*, post/* |
| LIVE | canon/[relevant] + gm/* + DB(NPCs, voices, OPSEC) | prep/*, post/* |
| POST | canon/[relevant] + post/* + DB(crew, confabs) | prep/*, gm/* |
| RULES | rules lookup table below | prose, DB |

## GM Craft (Layer 1 — system-agnostic)
~/software/aurasys-memory/traveller-reference/craft/
  (files TBD — encounter design, pacing, spotlight, arc planning, write-up methodology)

## Rules Lookup (Layer 2 — MgT2e)
Base path: ~/software/traveller-VTT-private/reference/BruceCampaignA/llm-knowledge-export/

[existing lookup table preserved]

## Campaign Data (Layer 3)
DB: ~/software/aurasys-memory/traveller-reference/campaign.db
Views: v_crew, v_fleet, v_system_detail, v_active_voices, v_confab_hot, v_threads_active
Example: sqlite3 campaign.db "SELECT * FROM v_crew;"

## On Deactivation

When Bruce says "done with Traveller", starts non-Traveller work, or says "no role needed":
1. Note: Traveller mode is no longer active. Do not reference loaded Traveller context for non-Traveller tasks.
2. Traveller vocabulary (parsec, jump, starport, ORACLE) belongs to campaign context only — do not bleed into book, MS, or SE work.
3. L1 index and DB remain on disk but are not actively loaded. Next `/traveller` re-reads L1 fresh.
4. If mid-conversation and Bruce switches topics: treat Traveller context as background (may compact), not foreground.
5. Isolation rule: Traveller campaign facts NEVER appear in Relinquishment manuscript, MS analysis, or memory system work. These are separate domains.

## Upgrade Protocol
- proficiency field in frontmatter tracks skill level (currently 40%)
- New rules books: add extraction file + update lookup table + update manifest
- New campaign data: add SQL data script + update MANIFEST + rebuild DB
- GM craft: add files to craft/ directory
- Version bump on structural changes
```

### Versioning for Upgrades

SKILL.md frontmatter includes `version` and `skill-proficiency`. When content is added:
- Rules file added → minor version bump (2.0 → 2.1)
- Structural change → major version bump (2.0 → 3.0)
- Proficiency updates after Bruce assessment
- All content files are checksummed and manifested — additions don't break existing structure

---

## Content Migration Plan

### What Moves

| Content | From | To | Action |
|---------|------|-----|--------|
| Rules files (22 files, 16K lines) | llm-knowledge-export/ | STAY — referenced by SKILL.md | No change |
| Campaign state files (4K lines) | llm-knowledge-export/ | DB replaces for Claude Code | No action — deferred until export tool built |
| Active SKILL.md | ~/.claude/skills/traveller/ | Rewrite in place | Iteration 4 |
| Backup SKILL.md | claude-backup/global/skills/ | DELETE | Stale copy |
| World files (worlds/*.md) | VTT repo | STAY as L3 — existence-checked from L1 | Add to L3/L4 pointers |

### What's Superseded for Claude Code

These llm-knowledge-export files are now superseded by DB queries for Claude Code instances. No action needed now — when a Claude web export tool is built later, it will generate fresh versions from DB.

| File | DB Replacement |
|------|---------------|
| 00b-entity-index.md | DB queries (any table) |
| 04a-campaign-npcs-player.md | `SELECT * FROM v_crew;` + npcs table |
| 04b-campaign-npcs-gm-secrets.md | npcs.gm_secrets, npcs.opsec_notes |
| 05-ship-astral-dawn.md | `SELECT * FROM v_fleet;` + ships table |
| 08-session-state.md | plot_threads + systems (current state) |
| 09-locations-quick-ref.md | `SELECT * FROM v_system_detail;` |
| 10-plot-threads.md | `SELECT * FROM v_threads_active;` |

**Not superseded:** 00a-QUICK-START.md (orientation), 00-INDEX.md (navigation), 02-universe (sector prose), 03-chunk-* (narrative history), 06-oracle (mail system prose), 12-gm-cheatsheet.md (quick reference).

### Session Prep Consolidation

Session prep directories (s09/, s10/, s11/, s12/) are historical artifacts — each is 500-2000 lines duplicating NPC/ship/world data now in DB. Future session prep uses thin format:

```markdown
# S12 Session Prep — Collace

## Decisions (Bruce)
- Does Thale appear at Collace?
- JSI debrief: what does Vasquez reveal?

## Scenes
1. Arrival (query: SELECT * FROM v_system_detail WHERE hex='1237';)
2. Debrief (query: SELECT * FROM npcs WHERE id IN ('vasquez','delleron');)
3. Evidence delivery (thread: drakon-pipeline)

## Boxed Text
[scene-specific narrative only — no repeated data]
```

---

## Plugin Protocol — Adding New Content

### Two-Track Plugin System

When incorporating content from a new Traveller sourcebook:

**Track 1: Rules (prose extraction)**
1. Extract rules from PDF → numbered .md file in `llm-knowledge-export/`
2. Naming: `{nn}-{book-slug}-{topic}.md` (e.g., `27-pirates-of-drinax-trade.md`)
3. Update SKILL.md lookup table with new row
4. Update `00-extraction-manifest.md` with checksum + coverage
5. Verify: rule is findable via SKILL.md topic search

**Track 2: Data (SQL scripts)**
1. Extract worlds/ships/NPCs/orgs from sourcebook
2. Write SQL data script: `{nnn}-{scope}-{content}.sql` in `scripts/db-data/`
3. All data: `source = 'canon'`, `INSERT OR REPLACE`
4. Update `db-data/MANIFEST.md` with checksum
5. Run `rebuild-db.sh` → verify all tests pass
6. Update L1 stats if row counts changed

**Track 3: GM Craft (methodology)**
1. Extract GM advice/methodology to `traveller-reference/craft/` or appropriate prose dir
2. System-agnostic content only — Traveller-specific goes to canon/
3. Update L1 prose section with checksum
4. This track is for Robin's Guide, GM methodology, encounter design philosophy

### Example: Adding "Pirates of Drinax"
- Rules: pirate-specific combat rules, trade in lawless space → `27-pirates-trade-rules.md`
- Data: Drinax-region systems, pirate NPCs, faction orgs → `040-canon-drinax-systems.sql`, `041-canon-drinax-npcs.sql`
- Craft: sandbox campaign management advice → `craft/sandbox-management.md`

---

## Efficiency Testing Protocol

### Process Walkthroughs (Iteration 3)

Test each GM process end-to-end with a fresh instance loading only SKILL + L1 + DB:

**Test P1: Prep Efficiency**
- Task: "Plan S12 at Collace"
- Load: SKILL → L1 → DB queries (Collace system, active threads, crew) → prep/* prose
- Measure: how many tool calls to gather all needed context?
- Target: <8 tool calls for full session prep context
- Failure mode: instance loads llm-knowledge-export files instead of querying DB
- Failure mode: instance doesn't know about plot threads (needs v_threads_active)

**Test P2: Live GM Efficiency**
- Task: "Adjudicate personal combat: Delleron vs two pirates in corridor"
- Load: SKILL → rules lookup → DB query (Delleron stats, pirate stats from combat cards)
- Measure: time to first correct DM calculation
- Target: correct DM within ≤5 tool calls (SKILL load + L1 + rules file + DB stats + answer)
- Failure mode: wrong edition rules, approximated numbers
- Failure mode: doesn't find combat cards (L3 pointer)

**Test P3: Post-Processing Efficiency**
- Task: "Write 10% summary of S11"
- Load: SKILL → L1 (anti-confab) → DB (crew, confabs) → post/* prose → transcript
- Measure: confabulation count in first draft
- Target: zero confabulations of entity type, tonnage, or FTL communication
- Failure mode: writes Anemone as robot (historic confab, recurrence=3)
- Failure mode: invents plot events not in transcript

**Test P4: Compaction Resilience**
- Task: same as P3 but after forced compaction
- **Compaction method:** In the same shell that ran P3, read 3-4 large files (e.g., full S11 transcript at 3230 lines + ships-log at 344 lines + 2 world files) to push context past the compaction threshold. When the continuation summary appears, immediately attempt P3 again — the compacted context simulates a real mid-session recovery.
- Load: post-compaction recovery protocol → L1 re-read → DB re-query
- Measure: does quality degrade vs. P3?
- Target: identical confabulation rate pre- and post-compaction
- **Key test:** Does the instance re-read L1 and re-query v_confab_hot on its own, or does it rely on compacted memory of the hot list?

### Pain Point Monitoring

After Iteration 1 (S11 test), track:
- Tool calls per process (prep/live/post)
- Confabulation rate per process
- Time to first useful output
- Files loaded that shouldn't have been (wasted context)
- DB queries that returned too much data (wasted context)

---

## Metrics and Evaluation

### Why Metrics

This system replaces an ad hoc flat-file approach. Without baseline measurements, we can't prove the new system is better — we'd just be claiming it. Scientific comparison requires: measure the old system, build the new system, measure the new system, compare.

### Metric Categories

**CR — Confabulation Rate (primary outcome)**

| ID | Metric | Unit | How measured |
|----|--------|------|--------------|
| CR-entity | Entity type confabulations | count/draft | Auditor grep: every name → DB entity_type |
| CR-tonnage | Ship tonnage confabulations | count/draft | Auditor grep: every tonnage → DB ships |
| CR-ftl | FTL communication assumptions | count/draft | Auditor grep for instantaneous-comms language |
| CR-event | Invented plot events | count/draft | Auditor diff: draft events vs extraction events |
| CR-total | Total confabulations | count/draft | Sum of above |
| CR-density | Confabulation density | per 1000 words | CR-total / (word count / 1000) |
| CR-recurrence | Known confab repetitions | count/draft | Grep draft for v_confab_hot wrong_claim patterns |

**EF — Efficiency**

| ID | Metric | Unit | How measured |
|----|--------|------|--------------|
| EF-calls | Tool calls to useful output | count | Count from session transcript, by mode |
| EF-time | Wall clock to useful output | minutes | Timestamp first request → timestamp first output |
| EF-context | Reference material consumed | est. tokens | Sum line counts of all loaded files × ~4 tok/line |
| EF-files | Files read | count + list | Grep transcript for Read tool calls |
| EF-queries | DB queries executed | count | Grep transcript for sqlite3 calls |
| EF-waste | Files loaded but unused in output | count | Files read that contributed nothing to result |

**QA — Output Quality**

| ID | Metric | Unit | How measured |
|----|--------|------|--------------|
| QA-corrections | Bruce QC corrections | count/draft | Bruce counts during review |
| QA-style-ratio | Style vs factual corrections | ratio | style / (style + factual) — target: 1.0 (only style) |
| QA-voice | Voice consistency | 1-5 scale | Bruce rates after review |
| QA-wordcount | Output length | words | wc -w on 10% and 1% |
| QA-approved | First-draft approval | binary | Did Bruce approve without factual revision? |

**CP — Compaction Resilience**

| ID | Metric | Unit | How measured |
|----|--------|------|--------------|
| CP-recovery | Recovery tool calls | count | Tool calls between compaction event and useful output |
| CP-degradation | Quality loss | CR-total delta | CR-total(post-compaction) - CR-total(pre-compaction) |
| CP-l1-reread | L1 re-read after compaction | binary | Did instance Read traveller-reference.md? |
| CP-db-requery | DB re-queried after compaction | binary | Did instance run sqlite3 after compaction? |

**SH — System Health (automated)**

| ID | Metric | Unit | How measured |
|----|--------|------|--------------|
| SH-db-bytes | DB file size | bytes | stat campaign.db |
| SH-db-rows | Row counts per table | count×15 | SELECT count(*) for each table |
| SH-prose-count | Prose files | count | find canon/ prep/ gm/ post/ -name '*.md' |
| SH-prose-lines | Total prose lines | count | wc -l on all prose files |
| SH-l1-lines | L1 index size | lines | wc -l traveller-reference.md |
| SH-checksum-ok | Checksum validity | % | verify-integrity.sh prose phase |
| SH-tests-pass | Test pass rate | N/total | run-tests.sh |
| SH-export-lag | Sessions since export | count | DB query: current session - last_export_session |

### Baseline Protocol (BEFORE Iteration 1)

Run these tests with the CURRENT system (flat files, SKILL.md v1, no DB queries, no L1) to establish the comparison baseline. Use a fresh shell for each test.

**B1: Post-Game Baseline**
```
Fresh shell. Load current SKILL.md + ships-log-player-summaries.md.
Task: "Write a 10% literary SF summary of Traveller Session 11."
Provide S11 full transcript when requested. Do NOT provide L1, DB, or extraction.
Record: CR-total, CR-entity, CR-ftl, EF-calls, EF-files, EF-time, QA-wordcount.
Save: traveller-reference/metrics/baseline-b1-post.yaml
```

**B2: Prep Baseline**
```
Fresh shell. Load current SKILL.md.
Task: "Plan session 12 at Collace."
Let instance request files — record each request.
Record: EF-calls, EF-files, EF-time, EF-waste.
Save: traveller-reference/metrics/baseline-b2-prep.yaml
```

**B3: Live GM Baseline**
```
Fresh shell. Load current SKILL.md.
Task: "Adjudicate personal combat: Delleron vs two pirates in a corridor."
Record: EF-calls, EF-files, EF-time, correctness (binary).
Save: traveller-reference/metrics/baseline-b3-live.yaml
```

**B0: System Health Baseline**
```bash
# Run from aurasys-memory/
echo "=== B0: System Health Baseline ==="
echo "db_bytes: $(stat -c%s traveller-reference/campaign.db)"
echo "prose_files: $(find traveller-reference/canon/ traveller-reference/prep/ traveller-reference/gm/ traveller-reference/post/ -name '*.md' 2>/dev/null | wc -l)"
echo "l1_exists: $([ -f traveller-reference.md ] && echo true || echo false)"
echo "skill_version: $(grep 'version:' ~/.claude/skills/traveller/SKILL.md 2>/dev/null || echo 'v1-stale')"
echo "tests_passing: $(bash traveller-reference/scripts/tests/run-tests.sh 2>/dev/null | tail -1)"
# Save output to traveller-reference/metrics/baseline-b0-health.yaml
```

### Per-Iteration Measurement

After each iteration gate passes, run the corresponding test(s) and record metrics:

| Iteration | Tests to run | Compare against |
|-----------|-------------|-----------------|
| Foundation | B0 (health only — no functional change yet) | B0 baseline |
| Iter 1 | P3 equivalent + B0 health | B1 baseline (post-game) |
| Iter 2 | P1 equivalent + B0 health | B2 baseline (prep) |
| Iter 3 | P2 + P3 + P4 + B0 health | B1 + B2 + B3 baselines (all modes) |
| Iter 4 | Wiring test + SKILL activation + B0 health | Full baseline set |

### Metric Storage

```
traveller-reference/metrics/
  baseline-b0-health.yaml     ← system health snapshot (pre-Iter 1)
  baseline-b1-post.yaml       ← post-game with old system
  baseline-b2-prep.yaml       ← prep with old system
  baseline-b3-live.yaml       ← live GM with old system
  iter1.yaml                  ← post-Iter-1 measurements
  iter2.yaml                  ← post-Iter-2 measurements
  iter3.yaml                  ← post-Iter-3 measurements
  iter4.yaml                  ← post-Iter-4 measurements (final)
  sessions/                   ← ongoing per-session tracking
    s12.yaml                  ← first session with new system
    s13.yaml
```

### YAML Format

```yaml
# Example: iter1.yaml
date: 2026-05-XX
iteration: 1
system_version: "0299-v3.4-iter1"

confabulation:
  cr_entity: 0
  cr_tonnage: 0
  cr_ftl: 0
  cr_event: 0
  cr_total: 0
  cr_density: 0.0
  cr_recurrence: 0

efficiency:
  ef_calls: 7
  ef_time_min: 12
  ef_context_tokens: 1800
  ef_files: ["traveller-reference.md", "post/fiction-voice.md", "post/oracle-voice.md"]
  ef_queries: 3
  ef_waste: 0

quality:
  qa_corrections: 2
  qa_style_ratio: 1.0
  qa_voice: 4
  qa_wordcount_10pct: 1450
  qa_approved: true

compaction:  # only in iter3+
  cp_recovery: null
  cp_degradation: null

health:
  sh_db_bytes: 245760
  sh_db_rows: {species: 7, systems: 37, npcs: 28, ships: 17, orgs: 18, cultures: 10, confabs: 9, plot_threads: 12}
  sh_prose_count: 4
  sh_prose_lines: 320
  sh_l1_lines: 78
  sh_checksum_ok: 100
  sh_tests_pass: "10/10"
  sh_export_lag: 0

notes: |
  First fiction generation with new system.
  Compare cr_total vs baseline-b1-post.yaml.
```

### Key Comparisons (after Iteration 3)

These are the questions the metrics answer:

| Question | Baseline metric | New metric | Success threshold |
|----------|----------------|------------|-------------------|
| Does it confabulate less? | B1:CR-total | Iter1:CR-total | New ≤ 0 (baseline likely >0) |
| Is it faster? | B1:EF-calls | Iter1:EF-calls | New < baseline |
| Does Bruce approve more easily? | B1:QA-approved | Iter1:QA-approved | New = true |
| Does prep work better? | B2:EF-calls | Iter2:EF-calls | New ≤ 8 |
| Does compaction degrade quality? | Iter3:P3 CR | Iter3:P4 CR | P4 = P3 |
| Is the system maintainable? | B0:SH-tests-pass | Iter3:SH-tests-pass | 12/12 |

### Metrics Collection Script

Iteration 3 deliverable: `scripts/collect-metrics.sh <session-number>`
- Queries DB for all SH-* metrics
- Checks prose file counts and checksums
- Runs test suite and records pass count
- Outputs YAML to `metrics/sessions/sNN.yaml`
- Bruce fills in CR-*, QA-* manually after QC

---

## Portability

If Bruce starts Campaign B, these transfer directly:
- DB schema (empty tables, views, triggers)
- DB canon data (species, organizations, published systems, ship classes)
- All prose L2 files (canon/*, craft/*, post/fiction-voice.md, post/pipeline.md, post/extraction-template.md)
- SKILL.md (layers 1+2, campaign layer zeroed)
- Rules extraction files (all 22)
- Verification scripts, L1 structure, checksum system, test harness

Rebuild for new campaign: campaign NPCs, ships, plot threads, culture_at_world for new region, GM prose (email system, NPC voices).

---

## Follow-On Plans

### Plan 0300 — Memory System Retrofit

Once proven, apply lessons to `aurasys-memory/memory/`:
- MEMORY.md → existence-rich L1 with checksums (same pattern)
- Consider SQLite for relational cross-project data (if needed)
- Add load profiles by task domain
- Install integrity verification
- Enable more aggressive compaction

Separate plan, dedicated session. The Traveller system tests the pattern; the memory retrofit scales it.

### Plan 0301 — GM Craft Layer (Robin's Guide Integration)

Build the system-agnostic GM methodology layer:
- `traveller-reference/craft/` directory
- Encounter design principles (not Traveller-specific)
- Pacing and spotlight management
- Session structure and arc planning
- Post-session write-up craft (the 10%/1% format is actually system-agnostic)
- Source: Bruce's accumulated GMing methodology + published GM advice
- Requires: Bruce input on which principles to codify (this is HIS methodology, not generic advice)

Separate plan — Bruce's GM craft knowledge is a SKILL unto itself.

---

## Backup, Disaster Recovery, and DB Failure

### Backup Strategy

**Everything on GitHub.** Both repos (aurasys-memory, traveller-VTT-private) are private GitHub repos. The DB is committed alongside its scripts.

| Asset | Location | Backed up via |
|-------|----------|--------------|
| Schema scripts | aurasys-memory/traveller-reference/scripts/db-setup/ | Git |
| Data scripts | aurasys-memory/traveller-reference/scripts/db-data/ | Git |
| campaign.db | aurasys-memory/traveller-reference/ | Git (committed) |
| Prose files | aurasys-memory/traveller-reference/{canon,prep,gm,post}/ | Git |
| L1 index | aurasys-memory/traveller-reference.md | Git |
| Manifests | aurasys-memory/traveller-reference/scripts/*/MANIFEST.md | Git |
| VTT star data | traveller-VTT-private/reference/.../enriched-systems/ | Git |
| Import scripts | traveller-VTT-private/ | Git |

### Disaster Recovery

**Computer dies → full recovery from GitHub:**

1. `git clone` aurasys-memory → get scripts, manifests, committed DB, prose files, L1
2. If committed DB is recent enough → done (instant recovery)
3. If DB needs refresh → `bash scripts/rebuild-db.sh` → identical DB from scripts
4. `git clone` traveller-VTT-private → get enriched-systems data, importers
5. If stellar body data needs refresh → run importer → regenerate 013-env-stellar.sql
6. `bash scripts/rebuild-db.sh` → complete DB with all data

**Recovery time:** Step 1-2 = minutes. Step 3 = seconds. Full rebuild = under 5 minutes.

### DB Failure Modes and Cures

| Failure | Detection | Cure |
|---------|-----------|------|
| Corruption (disk error) | `PRAGMA integrity_check` returns non-'ok' | `rebuild-db.sh` from scripts |
| FK violation (bad insert) | `PRAGMA foreign_key_check` returns rows | Fix data script, re-run `rebuild-db.sh` |
| Stale data (script changed) | `verify-manifests.sh` reports STALE | Update manifest hash or rebuild |
| Missing data (incomplete load) | Row count check vs expected | Re-run `load.sh` |
| Un-exported session data | DB has rows not in any data script | Run `export-session.sh` before rebuild |
| WAL file left behind | `.db-wal` exists after crash | SQLite auto-recovers on next open |

### Session-End Export Workflow

Post-session data flow prevents data loss between DB state and scripts:

1. During/after game: `INSERT`/`UPDATE`/`DELETE` directly into campaign.db (fast, live)
2. Session end: run `export-session.sh` → generates numbered data script (e.g., `040-session-12-updates.sql`). Handles INSERT OR REPLACE for changed/new entities AND DELETE for removed entities (DELETE triggers log to content_log with action='delete').
3. Add new script to `db-data/MANIFEST.md`, update hash
4. Update MANIFEST hash in reference-landmarks.md
5. `git commit` — DB + new script + updated manifests all committed together
6. Verify: `rebuild-db.sh` on clean DB produces same result

**Critical rule:** NEVER rebuild without exporting first. Un-exported session data exists only in the committed DB until exported.

### Idempotency Guarantees

| Operation | Idempotent? | Mechanism |
|-----------|-------------|-----------|
| `setup.sh` | Yes | Drops and recreates DB (starts fresh) |
| `load.sh` | Yes | Uses `INSERT OR REPLACE` on all data |
| `rebuild-db.sh` | Yes | rm + setup + load = identical every time |
| `verify-manifests.sh` | Yes (read-only) | Only reads, never modifies |
| `verify-integrity.sh` | Yes (read-only) | Only reads, never modifies |
| `run-tests.sh` | Yes | Tests use temp DB copies, don't touch campaign.db |
| `import-enriched-systems.py` | Yes | Generates SQL with `INSERT OR REPLACE` |
| `export-session.sh` | Idempotent per session | Exports only content_log entries since last export |

**Iteration re-runnability:** Every iteration can be re-run without manual cleanup. `rebuild-db.sh` is the universal reset. No hidden state outside of git.

---

## Source of Truth Resolution (BLOCKING — resolved)

### The Problem

Data duplication between DB and flat files creates confabulation risk:
- NPC entity_type in DB (npcs table) AND flat file (04a-campaign-npcs-player.md)
- Ship tonnage in DB (ships table) AND flat file (05-ship-astral-dawn.md)
- System UWP in DB (systems table) AND world files (worlds/collace.md)
- Plot thread status in DB (plot_threads table) AND flat file (10-plot-threads.md)

If one source updates and the other doesn't, an instance reading the stale source confabulates.

### The Rule: ONE SOURCE OF TRUTH PER FACT

| Fact type | Authoritative source | Examples |
|-----------|---------------------|----------|
| Structured data | **DB** | entity_type, tonnage, UWP, status, affiliations, hex, trade_codes |
| Narrative prose | **Flat file** | world descriptions, rules, session prep scenes, voice profiles, GM methodology |
| Generated reports | **Script output** | Claude web export files, world briefs, session prep summaries |

No fact lives in both the DB and a hand-edited flat file. Generated files are MARKED and never hand-edited.

### DB-Authoritative Export (DEFERRED)

Claude web export tool will be built when needed. It will query campaign.db and generate flat markdown files for Claude web instances. Until then, Claude Code queries the DB directly.

### World File Restructure

World files (worlds/collace.md) currently mix structured data and prose. Split them:

**Before (fragmentation risk):**
```markdown
# Collace (1237)
## World Data (Canonical)
| UWP | B628943-D |        ← DUPLICATES DB
| Starport | B (Good) |   ← DUPLICATES DB
...
## Why Collace Matters
Collace is the wealthiest...  ← UNIQUE PROSE
```

**After (clean separation):**
```markdown
# Collace (1237)
<!-- Structured data: query DB — sqlite3 campaign.db "SELECT * FROM v_system_detail WHERE hex='1237';" -->
## Why Collace Matters
Collace is the wealthiest...  ← UNIQUE PROSE (source of truth for narrative)
```

The structured data table is REMOVED from the world file. Any instance needing UWP/starport/TL queries the DB. The world file contains ONLY narrative prose that can't be in the DB.

A `gen-world-brief.sh` script combines both for session prep:
```bash
# gen-world-brief.sh collace
sqlite3 campaign.db "SELECT * FROM v_system_detail WHERE name='Collace';"
echo "---"
cat worlds/collace.md  # narrative prose only
```

### Write Paths (all scenarios)

| Scenario | Where to write | Sync step |
|----------|---------------|-----------|
| Live play: NPC status changes | INSERT/UPDATE DB directly | Session-end: export-session.sh |
| Prep: new NPC created | Write SQL data script → rebuild | No sync needed (DB is authoritative) |
| Prep: world narrative updated | Edit world file directly | No sync needed (prose is flat-file-authoritative) |
| Post-game: new confab discovered | INSERT into DB | Update L1 anti-confab list |
| New sourcebook data | Plugin protocol (SQL track) | rebuild |
| New rules extracted | Plugin protocol (rules track) | No sync needed (rules are flat-file-authoritative) |

### Session-End Workflow

1. During/after game: INSERT/UPDATE directly into campaign.db
2. Run `export-session.sh` → generates numbered data script
3. Add scripts to MANIFESTs, update hashes
4. `git commit` — DB + new scripts + updated manifests
5. Verify: `rebuild-db.sh` on clean DB → identical result

---

## Anti-Patterns

- **Circular reference:** Don't use Argus-written content (ships log, session state) as fact source. Use TRANSCRIPT + DB.
- **Gap filling:** Generator doesn't know → OMIT, never invent.
- **Register contamination:** Ships log (ORACLE) ≠ 10% (narrator) ≠ NPC email. Never mix.
- **Bypassing DB:** Don't hardcode facts in prose files that belong in the DB. Query instead.
- **FTL assumption:** Characters can only know what messages have had time to reach them. Calculate transit times from parsec distances.
- **Stale DB context:** After compaction, re-query — don't rely on remembered query results.

---

## Generator Handoff Prompts

Each prompt below is self-contained and idempotent — a second Generator given the same plan and prompt produces identical output. Copy-paste one at a time to a Generator shell. Each Generator shell should be launched from `~/software/aurasys-memory/`.

**v3.4 restructured 2026-05-08.** Foundation prompts (A, B) unchanged from v3.3. Iteration 1 prompts (I1, I1-G) new. Iterations 2-4 prompts deferred until prior iteration completes. Each prompt red-teamed for: source/canon conflicts, missing source pointers, SQL special chars, body_type enum mismatches, test isolation, edition contamination.

---

### Prompt A — Plan 0299 Phase 1B-2: Python VTT Importer

```
You are the Generator.

Plan 0299 Phase 1B-2: Write the Python VTT importer.

Read `/home/bruce/software/relinquishment/plans/0299-traveller-creative-fiction-pipeline.md` section "VTT Star System Import Path" for full spec. Python 3.11.2 is available.

Write `/home/bruce/software/traveller-VTT-private/import-enriched-systems.py`:
- Usage: `python3 import-enriched-systems.py [file1.json file2.json ...]`
- With args: processes listed files. Without args: processes `reference/BruceCampaignA/enriched-systems/*.json` (31 files, 475 bodies)
- Outputs SQL to stdout (redirect to file when run)
- Systems: use INSERT OR IGNORE (NOT INSERT OR REPLACE — canon systems in 012-canon-systems.sql must not be overwritten). Set source='environment' on all system rows.
- Stellar bodies: use INSERT OR REPLACE. Set source='environment'.
- UWP parse: standard XNNNNNN-N. Char 0=starport, chars 1-6=size/atmo/hydro/pop/gov/law (hex: A=10,B=11,C=12,D=13,E=14,F=15), char 8=tech_level. If UWP is NULL/empty, set all parsed fields to NULL.
- Body type mapping (EXACT — these are the only 6 types in the VTT data):
  Star→star, Planet→planet, Gas Giant→gas_giant, Moon→moon, Planetoid Belt→belt, Highport→station
- SQL strings: escape single quotes by doubling (e.g., O'Brien → O''Brien). No apostrophes exist in current data but the importer must handle them.
- parent_body_id: set NULL (VTT JSON doesn't encode parent relationships)
- Generate deterministic output: sort systems by hex, bodies by system_hex then orbitAU

Test fixture: copy `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/enriched-systems/milagro.json` to `/home/bruce/software/aurasys-memory/traveller-reference/scripts/tests/fixtures/test-system.json`. Run importer on fixture. Verify output by loading into a fresh schema (setup.sh → run generated SQL → PRAGMA integrity_check + PRAGMA foreign_key_check). Save the verified output as `fixtures/expected-import.sql`.
```

---

### Prompt B — Plan 0299 Phase 1B-3: Remaining Tests (07-10)

```
You are the Generator.

Plan 0299 Phase 1B-3: Write test scripts 09 and 10.

Read `/home/bruce/software/relinquishment/plans/0299-traveller-creative-fiction-pipeline.md` section "Test Specifications" for test-09 and test-10 specs. Read existing tests in `/home/bruce/software/aurasys-memory/traveller-reference/scripts/tests/test-0{1..8}*.sh` for the established pattern: set -uo pipefail, pass/fail counters, helper functions (expect_fail/expect_ok/check/check_nonzero), exit 77 for skip, summary line at end, final [ "$fail" -eq 0 ].

NOTE: test-07-nasty-insert.sh (288 lines, constraint enforcement) and test-08-performance.sh (196 lines, query performance) already exist and are passing. Do NOT replace or rename them. Write only test-09 and test-10.

Write 2 files in `/home/bruce/software/aurasys-memory/traveller-reference/scripts/tests/`:

test-09-importer.sh:
- Skip (exit 77) if python3 not available or fixtures/test-system.json missing
- Run importer: `python3 /home/bruce/software/traveller-VTT-private/import-enriched-systems.py fixtures/test-system.json`
- Structural validation (NOT exact diff): verify output contains INSERT OR IGNORE for systems, INSERT OR REPLACE for stellar_bodies, source='environment' on all rows, body_type values all in enum (star|planet|gas_giant|moon|belt|station), valid SQL (load into temp DB without errors)

test-10-confab-registry.sh:
- Verify 3 critical confabs exist: Anemone=HUMAN, AD=600t, NO FTL COMMS
- Verify v_confab_hot sort order: critical before high before medium
- Verify recurrence_count ordering within same severity
- Cross-check: Anemone entity_type=human in npcs table, AD tonnage=600 in ships table

Also write `/home/bruce/software/aurasys-memory/traveller-reference/scripts/tests/MANIFEST.md`:
- Same format as db-setup/MANIFEST.md (table with #, Script, Hash, Purpose columns)
- List ALL test scripts (test-01 through test-10) with sha256 checksums
- Update `~/software/aurasys-memory/memory/reference-landmarks.md` TRAVELLER section: change tests/MANIFEST.md entry from "TBD, Phase 1A" to actual hash

DB path: `$(cd "$(dirname "$0")/../.." && pwd)/campaign.db`. Run full suite to verify: `bash scripts/tests/run-tests.sh`.
```

---

### Prompt I1 — Iteration 1: Post-Game Prose + Minimal L1

```
You are the Generator.

Plan 0299 Iteration 1: Write 4 post-game prose files and a minimal L1 index.

Read `/home/bruce/software/relinquishment/plans/0299-traveller-creative-fiction-pipeline.md` section "Iteration 1: Post-Game MVP" for scope and requirements.

SOURCE FILES — read these BEFORE writing (they contain the campaign-specific voice, mechanics, and formats):
- `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/ships-log-player-summaries.md` → primary voice exemplar (344 lines, Sessions 4-10)
- `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/oracle-comms-log.md` → ORACLE voice exemplar
- `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/oracle-npc-mail-profiles.md` → ORACLE rules (Global Rules + Security Matrix sections)
- `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/post-session-process.md` → pipeline source
- `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/transcript-pipeline.md` → extraction template source

Write in `/home/bruce/software/aurasys-memory/traveller-reference/post/`:

fiction-voice.md (~100 lines):
  **CRITICAL:** Read ships-log-player-summaries.md FIRST. Identify ≥3 structural patterns (paragraph rhythm, embellishment boundary, tense, dialogue integration, ORACLE-vs-narrator register). Include ≥3 verbatim excerpts from that file with annotations explaining what makes each correct. "Write literary SF" is NOT a voice guide. Specific reproducible patterns with examples ARE.
  Embellishment boundary: character reactions and internal states OK, new plot events NOT OK.

oracle-voice.md (~60 lines):
  ORACLE = ship AI, formal/terse, redacts classified content, uses crew ranks. Source: ORACLE sections in ships-log-player-summaries.md + oracle-comms-log.md.

extraction-template.md (~60 lines):
  Per-session extraction format: verified events (timestamped), key dialogue (from transcript), character moments, humor/personal, running gag updates, player-safe vs GM-only, fact-check list. Source: transcript-pipeline.md.

pipeline.md (~60 lines):
  End-to-end post-session checklist. Source: post-session-process.md.

Write `/home/bruce/software/aurasys-memory/traveller-reference.md` (L1 index, POST-MODE ONLY):
  - First line: `<!-- Post-compaction: reload this file. DB: traveller-reference/campaign.db -->`
  - Anti-confab hot list: query `SELECT * FROM v_confab_hot WHERE severity IN ('critical','high') ORDER BY severity, recurrence_count DESC;` from `/home/bruce/software/aurasys-memory/traveller-reference/campaign.db`. List each as a bullet with severity tag.
  - DB path + view list + 3 example queries (v_crew, v_fleet, v_system_detail)
  - Post-mode load profile: list the 4 post/* files with sha256 checksums (`sha256sum <file> | cut -c1-6`)
  - Summary stats: query counts of species, systems, npcs, ships, orgs, cultures, confabs, plot_threads
  - HARD CAP 80 lines. POST-mode only — later iterations expand.

Curate and condense from source files — do NOT copy verbatim (different format/purpose). Flag [VERIFY] if uncertain about a campaign-specific detail.

Tag before first write: `git tag pre-iter1 HEAD` (in aurasys-memory repo).
Commit message: `Plan 0299 Prompt I1: Post-game prose + minimal L1`
```

---

### Prompt I1-G — Iteration 1: S11 Fiction Generation

```
You are the Generator.

Plan 0299 Iteration 1 fiction test: Generate S11 10% and 1% transcripts.

INPUT — load these in order:
1. `/home/bruce/software/aurasys-memory/traveller-reference.md` (L1 index — tells you what to query and load)
2. Query campaign.db: `SELECT * FROM v_crew;` and `SELECT * FROM v_confab_hot;`
3. `/home/bruce/software/aurasys-memory/traveller-reference/post/fiction-voice.md` (voice guide with exemplars)
4. `/home/bruce/software/aurasys-memory/traveller-reference/post/oracle-voice.md` (ORACLE register)
5. `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/session-prep-s11/s11-extraction.md` (Auditor extraction — factual claims come ONLY from here)
6. Exemplars: `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/ships-log-player-summaries.md` (Sessions 4-10, 344 lines — match this voice)

OUTPUT — write TWO files:
- `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/session-prep-s11/transcripts/s11-10pct-v2.txt` — 10% summary (~130 lines). Literary SF fiction, not boring recap. Follow fiction-voice.md patterns exactly.
- `/home/bruce/software/traveller-VTT-private/reference/BruceCampaignA/session-prep-s11/transcripts/s11-1pct-v2.txt` — 1% summary (~4 lines). Hook/tease only.

CONSTRAINTS:
- Factual claims from extraction ONLY. Do NOT invent plot events, discoveries, or character actions not in the extraction.
- Embellishment boundary: character reactions, internal states, sensory details OK. New events, revelations, or decisions NOT OK.
- Every proper name must appear in the extraction or campaign.db. Query DB to verify entity_type if uncertain.
- NO FTL COMMUNICATION — messages travel at ship speed (1 week per parsec). Characters cannot know things faster than couriers travel.
- ORACLE sections use ORACLE voice (formal, terse, crew ranks). Narrative sections use narrator voice (third person, past tense, literary SF).

Tag before first write: `git tag pre-iter1-g HEAD` (in traveller-VTT-private repo).
Commit message: `Plan 0299 Prompt I1-G: S11 fiction generation (v2)`
```

---

### Iterations 2–4: Prompts Written After Prior Iteration Completes

Iteration 2 (Prep), 3 (Live+Infrastructure), and 4 (Integration+SKILL) prompts are NOT pre-written. Each iteration's prompt is drafted by the Auditor after the prior iteration's gate passes, incorporating lessons learned. Scope is defined in the Iteration Plan above; exact Generator prompts are informed by real results.

**Why not pre-write all prompts:** The old monolithic plan (v3.3) pre-wrote all prompts (C through G). This meant:
- Fiction-voice.md patterns couldn't inform canon prose writing style
- Tool call counts from real prep tests couldn't inform infrastructure scope
- Compaction behavior couldn't be tested until all prose existed

The iterative approach lets each prompt benefit from what the prior iteration taught.

### Execution Order

| Step | Prompt | Iteration | Dependencies | Gate |
|------|--------|-----------|-------------|------|
| 0 | *(Baseline)* | Pre-work | None | B0-B3 YAML files saved in metrics/ |
| 1 | A | Foundation | Baseline complete, VTT repo accessible | Fixture SQL loads clean into fresh schema |
| 2 | B | Foundation | A complete (needs fixture + importer) | Tests 01-10 pass, test MANIFEST exists |
| 3 | I1 | Iter 1 | Foundation gate passed | 4 post/* files, fiction-voice ≥3 exemplars, L1 ≤ 80 lines |
| 4 | *(Auditor)* | Iter 1 | I1 complete | S11 extraction validated per 6b, written per template |
| 5 | I1-G | Iter 1 | Extraction complete | S11 fiction: zero confabs, Bruce approves |
| 5b | *(Metrics)* | Iter 1 | Bruce QC complete | iter1.yaml saved, compared against B1 baseline |
| 6 | *(TBD)* | Iter 2 | Iter 1 gate + lessons captured | 7 prose files, L1 ≤ 120, P1 ≤ 8 tool calls |
| 7 | *(TBD)* | Iter 3 | Iter 2 gate passed | 11 tests pass, P2-P4 pass |
| 8 | *(TBD)* | Iter 4 | Iter 3 gate passed | Wiring 5/5, SKILL 5/5, deactivation clean, E2E CR ≤ 1, MEMORY.md < 180 |

**Step 0 first.** A→B sequential. I1 after Foundation gate. I1-G after Auditor extraction. Metrics after each gate. Iterations 2-4 sequential.

### Idempotency Audit

**R27 standard:** "A second Generator given only this plan would produce the same claims." Idempotency has two levels:

| Level | Meaning | Applies to |
|-------|---------|------------|
| **Byte-identical** | Same output every time | A (code), B (tests) |
| **Claim-identical** | Same facts, different wording | I1 (post-game prose), I1-G (fiction) |

**Byte-identical prompts:**
- **Prompt A:** Deterministic JSON→SQL mapping, sorted by hex then orbitAU. Fixture copied verbatim. ✓
- **Prompt B:** Tests verify structural properties via deterministic DB queries and grep patterns. ✓

**Claim-identical prompts:**
- **Prompt I1:** Source files are explicit. Two Generators reading the same ships-log-player-summaries.md will extract the same structural patterns but condense differently. fiction-voice.md is additionally constrained by the ≥3 verbatim exemplar requirement (quotes are byte-identical even if annotations differ). Idempotency risk: Generator adds detail not in the source file. Mitigation: [VERIFY] + "Flag if uncertain about campaign-specific detail."
- **Prompt I1-G:** Creative fiction. **NOT idempotent by design.** Two Generators will produce different stories from the same extraction. Idempotency applies ONLY to factual claims: names must match DB entity_type, tonnages must match DB, no FTL communication. Verification pass (Auditor step 8 in Iteration 1) enforces claim-identity. Voice consistency is verified against exemplars by human QC (Bruce), not mechanically.

**Iteration 2-4 idempotency:** Assessed when prompts are written. Infrastructure prompts (sync scripts, tests) will be byte-identical. Prose prompts (canon, gm modes) will be claim-identical with the same mitigations.

**Idempotency failure mode:** A Generator for I1 writes fiction-voice.md with patterns that don't match the source exemplars. The ≥3 verbatim excerpt requirement constrains this — the quotes themselves ARE the patterns. A Generator that invents a "pattern" not grounded in an excerpt fails the gate. Bruce QC catches misattribution.

---

## Git Safety Protocol

### Existing Tags and Branches

| Asset | Repo | Value |
|-------|------|-------|
| Pre-Generator tag | aurasys-memory | `pre-traveller-ref-v1` on `180fcc9` |
| Pre-Generator tag | traveller-VTT-private | `pre-traveller-ref-v1` on `77a726b` |
| Working branch | aurasys-memory | `traveller-ref-phase1` (active) |
| Main branch | aurasys-memory | `main` (merge target) |

**Rollback:** `git checkout pre-traveller-ref-v1` in either repo restores pre-Generator state.

### Per-Phase Tagging Protocol

Tag BEFORE each Generator prompt runs (not after). Tags are rollback points, not milestones.

| When | Tag | Repo | Purpose |
|------|-----|------|---------|
| Before Prompt A | `pre-traveller-ref-v1` | both | Already exists. Rollback to before any Generator. |
| After Prompt B passes | `traveller-ref-foundation-complete` | aurasys-memory | Gate: all 10 tests pass, stellar_bodies > 0. Safe to start prose. |
| Before Prompt I1 | `pre-iter1` | aurasys-memory | Rollback to before post-game prose. |
| Before Prompt I1-G | `pre-iter1-g` | traveller-VTT-private | Rollback to before fiction generation. |
| After Iter 1 gate | `traveller-ref-iter1-complete` | both | Gate: S11 fiction zero confabs, Bruce approved. |
| After Iter 2 gate | `traveller-ref-iter2-complete` | aurasys-memory | Gate: prep mode works, P1 ≤ 8 tool calls. |
| After Iter 3 gate | `traveller-ref-iter3-complete` | aurasys-memory | Gate: all 11 tests pass, P2-P4 pass. |
| Before Iter 4 wiring | `pre-memory-wiring` | aurasys-memory | Rollback before touching MEMORY.md/SKILL.md. |

**Rule:** Each Generator shell creates the tag as its FIRST action (before any writes). Auditor verifies tag exists before approving the Generator's output.

### Branch and Merge Strategy

```
main ──────────────────────────────────────────────────────────── main
  └── traveller-ref-phase1 ──[A]──[B]──[I1]──[I1-G]──[I2]──...──┐
                                                                    ├── merge after Iter 3 gate
                                                                  ──┘
```

**Branch rules:**
- ALL Generator work happens on `traveller-ref-phase1` in aurasys-memory
- VTT repo: Generators commit to its default branch (no separate feature branch — VTT changes are small and isolated)
- Each Generator prompt = one commit on the branch. Commit message: `Plan 0299 Prompt X: <description>`
- NO intermediate merges to main. The branch accumulates all iteration work.
- Merge to main ONLY after Iteration 3 gate passes (all 11 tests, compaction tests pass)
- Merge method: regular merge (not squash) — preserve individual prompt commits for traceability
- After merge: delete `traveller-ref-phase1` branch

**Iteration 4:** Auditor work directly on main (post-merge). Iteration 4 modifies memory infrastructure and SKILL.md — it should be on main because it affects all sessions, not just Traveller.

**Conflict prevention:** The branch only touches `traveller-reference/` and `memory/reference-landmarks.md`. Main branch work (book, MS, memory maintenance) doesn't touch these paths. If a conflict arises on `reference-landmarks.md`, the branch version wins (it has the Traveller manifest entries that main lacks).

### Cross-Repo Write Rules

Prompts A, I1, I1-G, and later iteration prompts write into traveller-VTT-private. Safety rules:
- **Never overwrite** an existing hand-edited file
- **Prompt A** writes import-enriched-systems.py (NEW file, safe)
- **Prompt I1** reads VTT files (READ-ONLY — writes go to aurasys-memory)
- **Prompt I1-G** writes fiction v2 files (NEW files with v2 suffix, safe — doesn't overwrite originals)
- VTT repo commits use message format: `Plan 0299 Prompt X: <description>` for cross-repo traceability

---

## Technical Debt Register

### Accepted Debt

| ID | Debt | Why Accepted | Pay-Down Plan |
|----|------|-------------|---------------|
| TD-1 | traveller-reference/ lives in aurasys-memory repo | Testbed for memory upgrade, easier pattern transfer | Extract to own repo after Plan 0300 (memory retrofit) if it outgrows ~5MB |
| TD-2 | World files still contain structured data tables | Restructuring 17 world files is out of scope for this plan | Plan 0302: restructure world files (remove UWP tables, keep prose only) |
| TD-3 | llm-knowledge-export files coexist with DB | Claude Code queries DB directly; flat files remain for Claude web until export tool built | Build export tool when Claude web access is needed |
| TD-4 | SKILL.md is stale (session 5, rules-only) | Rewrite depends on Iterations 1-3 completing successfully | Iteration 4 rewrites to v2.0 three-layer architecture |
| TD-5 | Session prep files (s09-s12) are bloated and duplicative | Historical artifacts, still useful as examples | Archive after thin prep template is proven in S12 |
| TD-6 | No automated world file sync (DB UWP ↔ world file UWP) | World files are being restructured to remove UWP (TD-2) | TD-2 eliminates the sync need |

### Monitoring

Review this register at Iteration 3 (efficiency testing) and Iteration 4 (SKILL migration). Items older than 3 months without progress → escalate to Bruce.
