# Plan 0310: Traveller Reference System — Data Completeness

**Status:** READY FOR GENERATOR  
**Priority:** MODERATE — stress test found 13 missing NPCs, 4 active threads with no connections, 3 orgs with no NPC affiliations, and GM query failures on location-based lookups.  
**Prerequisite:** Plan 0309 complete (it is).  
**Source:** S68 stress test #2 — Entity Coverage Audit + GM Query Gauntlet.  
**Estimated effort:** Single Generator session, ~30 min.  
**Branch:** `traveller-ref-phase1` (current)

---

## Why This Plan Exists

The S68 stress test (iteration 2) ran two checks:

1. **Entity Coverage Audit:** Cross-referenced the 92 NPCs in campaign.db against the npc-registry.md in VTT-private (66 named NPCs) and session plans S12-S13. Found 13 NPCs in prose that aren't in the DB, plus affiliation and thread connection gaps.

2. **GM Query Gauntlet:** Tried 15 representative GM queries against the DB. 9 passed, 3 partially worked (text search fallback), 3 failed outright. Key failures: "Who's at Forine?" (current_system all NULL), "Which NPCs connect to SuSAG?" (no affiliations despite org_at_world entries).

The DB needs to match what's in the prose, or it's not serving as the structured query layer the architecture promises.

---

## Phase 1: Add Missing NPCs [13 NPCs]

**Source:** `~/software/traveller-VTT-private/reference/BruceCampaignA/npc-registry.md` and session plans.

**New data script:** `scripts/db-data/023-missing-npcs.sql` (follows 022-campaign-relationships in the 020-series campaign data range)

Add these NPCs with data extracted from their prose sources:

### From npc-registry.md (10):

| Name | entity_type | Role | Notes |
|------|-------------|------|-------|
| Advocate Davi Ren | human | Premium customs advocate (Milagro) | Cr500, fast/expensive. Appears 50+ files. |
| Advocate Pell | human | Budget customs advocate (Milagro) | Elderly, slow, zero errors. Brak brings her tea. |
| Amy Torrelsen | human | Pilot, *Silver Meridian* | Direct and warm. Jack's romantic contact. Confident, flirty. From Glisten. S10. Ship-mobile. |
| Captain Hwaolr | alien | Aslan trader, ship *Iyrlakhte* | S11 transient. Cautious. Family operation, Hierate-border trade. Will vouch for crew. species_id='aslan'. |
| Gina Vasek | human | Captain, *Silver Meridian* (200t free trader) | Dallia-Collace-Tarkine-Binges circuit. Thinks AD is armed merchant. Friendly. S9-S10. |
| Groz | human | Thug leader (Milagro) | Triggers Asao bar fight. 16+ file mentions. |
| "Honest" Jak | human | Bargain advocate (Milagro) | Advocate 0, Cr50, will botch forms. |
| Pel Maddox | human | Comet miner/pilot, SV *Calving Point* (100t mining scout) | Collace-based. Mines ice comets in Forine system. Tight-beamed warning to AD about Lulabai. S6.5 canon. |
| Robbie Azevedo | human | Cargo/Astrogation, *Silver Meridian* | Jack's romantic contact. Belter family near Pagaton = unintentional intel network. S10. |
| Tova Maddox | human | Geologist/survey tech, SV *Calving Point* | Pel's wife. Runs sensors and drill rig. Spotted Lulabai first. S6.5 canon. |

### From S13 session plan (3):

| Name | entity_type | Role | Notes |
|------|-------------|------|-------|
| Ftahea Hrekhyei | alien | Forine factor / Aslan trade liaison | New S13 character (renamed from Ahriy in anneal). |
| Hagen Stross | human | (check S13 plan) | Forine NPC. |
| Senator Koss | human | Collace politician | S13 plan reference. |

**Generator instructions:**
1. Read the npc-registry.md AND the session plans (S10-S13) to extract correct details for each NPC.
2. Use entity_type from species context (Hwaolr is likely Aslan, Ftahea Hrekhyei is Aslan).
3. Set `source = 'play'` for all.
4. Set `current_system` where known (e.g., Milagro NPCs: `1632`, Forine NPCs: `1533`).
5. Use INSERT OR IGNORE to be idempotent.

**Also fix name consistency:**
- If DB has "Councillor Voss-Hallen" but registry says "Councillor Helena Voss-Hallen" — UPDATE to include first name.
- If DB has "Telenn Gha" but registry says "Maker Telenn Gha" — UPDATE to include title.

**Note:** "Supervisor Kai Ren" (Binges, S10) and "Kai Ren KR-7" (robot, aboard AD, S11) may be the same character who relocated. DB already has KR-7. Generator: check prose to confirm, do NOT add duplicate.

**Gate:** `SELECT count(*) FROM npcs;` returns 105+ (92 + 13). New NPCs queryable. Rebuild still clean.

---

## Phase 2: Fill Affiliation Gaps [3 orgs with 0 NPC affiliations]

**Orgs with org_at_world entries but no npc_affiliations:**
- `SuSAG` — Research facility at Forine. **Generator:** Check session plans and npc-registry for who connects to SuSAG. At minimum, Max Planck has investigated them. Anya Korvax may have SuSAG connections (Syndicate operative at Forine where SuSAG operates).
- `McClellan Factors` — Factor at Forine. **Generator:** Check if any NPC is a McClellan factor or contact.
- `Imperial Interstellar Scout Service` — Present at multiple worlds. **Generator:** Check for IISS-affiliated NPCs (scout service contacts, Brynhild crew, etc.).

**New data script:** `scripts/db-data/024-affiliation-gaps.sql`

**Generator instructions:**
1. Read the prose files for each org to identify NPC connections.
2. Only add affiliations that are documented in existing prose — do not invent connections.
3. If no NPC connection exists in prose for an org, leave it. The org_at_world entry is still valid (the org operates there, just no named NPC contact).

**Gate:** `SELECT o.name, count(na.npc_id) FROM organizations o LEFT JOIN npc_affiliations na ON o.id = na.org_id GROUP BY o.name ORDER BY count(na.npc_id), o.name;` — SuSAG and IISS should show ≥1 affiliation if prose supports it.

---

## Phase 3: Fill Thread Connection Gaps [4 active threads with 0 connections]

**Active threads with no thread_connections:**

| Thread | Priority | What's Missing |
|--------|----------|---------------|
| Syndicate Exposure | high | Should connect to: Drakon Syndicate (org), Anya Korvax (npc), Jemara Osei (npc), relevant systems |
| Htasea'a Intelligence Updates | normal | Should connect to: Htasea'a Ora (npc), Asao Ora (npc), JSI (org), Caladbolg/Raschev (systems) |
| Marta Compound Reports | background | Should connect to: Marta Aliyev (npc), compound location (system) |
| Raschev Base Construction | background | Should connect to: Raschev (system), Asao Ora (npc), Htasea'a Ora (npc) |

**New data script:** `scripts/db-data/025-thread-connections.sql`

**Generator instructions:**
1. Read plot_threads.gm_notes and player_summary for each thread to determine connections.
2. Cross-reference with session plans for entity IDs.
3. Use existing entity_id conventions (check thread_connections for existing patterns).
4. Only add connections documented in existing prose.

**Gate:** `SELECT pt.title FROM plot_threads pt LEFT JOIN thread_connections tc ON pt.id = tc.thread_id WHERE pt.status = 'active' AND tc.thread_id IS NULL;` returns 0 rows (all active threads have at least one connection).

---

## Phase 4: Populate Key NPC Locations (ISSUE-003 partial fix)

**This is NOT a full fix for ISSUE-003** — only the NPCs with known fixed locations get `current_system` set. Mobile NPCs stay NULL.

**Data script:** `scripts/db-data/026-npc-locations.sql`

Fixed-location NPCs (from npc-registry.md mobility classes):

| NPC | Location | Hex | Basis |
|-----|----------|-----|-------|
| Telenn Gha (or Maker Telenn Gha) | Binges | 1635 | World-locked, Aslan trade compound |
| Htasea'a Ora | Caladbolg | 1329 | Ticket-traveler, currently at Caladbolg managing JSI affairs (will relocate to Raschev when Asao does). Registry says hex 1815 — use DB hex 1329. |
| Councillor Voss-Hallen | Binges | 1635 | World-locked, politician |
| Hagen Stross | Forine | 1533 | World-locked (if confirmed in S13) |
| Senator Koss | Collace | 1237 | World-locked, politician |
| Chairman Oran Vesik | Forine | 1533 | World-locked, dictator |
| Inspector Tomás Brak | Milagro | 1632 | World-locked, customs chief |
| Delia Cade | Milagro | 1632 | World-locked, food distribution |
| Keeva Ortiz | Milagro | 1632 | World-locked, customs advocate |
| Anya Korvax | Forine | 1533 | Stationed at Forine (surveillance) |
| Dr. Hektor Grish | Forine | 1533 | World-locked, research |
| Gregor Yulkin | Forine | 1533 | World-locked |
| Silena Vos "Silk" | Forine | 1533 | World-locked |
| Cardinal | Forine | 1533 | World-locked |
| Ghost (Petra Valis) | — | — | Ship-mobile (aboard AD), but FROM Forine |
| Pel Maddox | Collace | 1237 | World-locked. Mines in Forine system but based at Collace. (Phase 1 NPC) |
| Tova Maddox | Collace | 1237 | World-locked. Pel's wife. (Phase 1 NPC) |
| Groz | Milagro | 1632 | World-locked thug. (Phase 1 NPC) |
| Advocate Davi Ren | Milagro | 1632 | World-locked advocate. (Phase 1 NPC) |
| Advocate Pell | Milagro | 1632 | World-locked advocate. (Phase 1 NPC) |
| "Honest" Jak | Milagro | 1632 | World-locked advocate. (Phase 1 NPC) |

**Generator instructions:**
1. Use UPDATE statements with WHERE clause on NPC id or name.
2. Set current_system to the hex value (not the name — FK references systems.hex).
3. Verify each location against npc-registry.md mobility class and session plans.
4. Do NOT set current_system for ship-mobile NPCs (crew are aboard AD, not at a world).
5. Do NOT set current_system for NPCs whose location changes per session.

**Also for Phase 1 NPCs:** Set current_system at INSERT time where known (Milagro world-locked NPCs get `1632`, Forine NPCs get `1533`).

**Gate:** `SELECT n.name, s.name as location FROM npcs n JOIN systems s ON n.current_system = s.hex WHERE n.current_system IS NOT NULL ORDER BY s.name, n.name;` returns ≥14 rows with correct locations. Q1 gauntlet re-test: "Who's at Forine?" returns ≥5 NPCs.

---

## Phase 5: Add GM Convenience Views

**Append to:** `scripts/db-setup/010-views.sql` (existing views script — do NOT create a new setup script; 013-meta.sql already exists)

```sql
-- v_npc_full: NPC with species name, location, and affiliation list
CREATE VIEW IF NOT EXISTS v_npc_full AS
SELECT 
    n.id, n.name, n.entity_type, 
    sp.name as species_name,
    n.role, n.status,
    n.current_system,
    s.name as location_name,
    n.description,
    GROUP_CONCAT(DISTINCT o.name) as affiliations
FROM npcs n
LEFT JOIN species sp ON n.species_id = sp.id
LEFT JOIN systems s ON n.current_system = s.hex
LEFT JOIN npc_affiliations na ON n.id = na.npc_id
LEFT JOIN organizations o ON o.id = na.org_id
GROUP BY n.id;

-- v_thread_map: Thread with all connected entity names resolved
CREATE VIEW IF NOT EXISTS v_thread_map AS
SELECT 
    pt.title as thread,
    pt.status,
    pt.priority,
    tc.entity_type,
    CASE tc.entity_type
        WHEN 'npc' THEN (SELECT name FROM npcs WHERE id = tc.entity_id)
        WHEN 'org' THEN (SELECT name FROM organizations WHERE id = tc.entity_id)
        WHEN 'system' THEN (SELECT name FROM systems WHERE hex = tc.entity_id)
        WHEN 'ship' THEN (SELECT name FROM ships WHERE id = tc.entity_id)
    END as entity_name,
    tc.role
FROM thread_connections tc
JOIN plot_threads pt ON pt.id = tc.thread_id;

-- v_world_npcs: NPCs at each world (only those with current_system set)
CREATE VIEW IF NOT EXISTS v_world_npcs AS
SELECT 
    s.name as world,
    s.hex,
    n.name as npc,
    n.role,
    n.entity_type
FROM npcs n
JOIN systems s ON n.current_system = s.hex
WHERE n.current_system IS NOT NULL
ORDER BY s.name, n.name;
```

**Gate:** All 3 views return results. `SELECT * FROM v_world_npcs WHERE world = 'Forine';` returns ≥5 NPCs. `SELECT * FROM v_thread_map WHERE thread = 'Syndicate Exposure';` returns connected entities. `SELECT * FROM v_npc_full WHERE name = 'Max Planck';` returns species, affiliations, everything.

---

## Phase 6: Update MANIFESTs and Hashes

1. Add `023-missing-npcs.sql`, `024-affiliation-gaps.sql`, `025-thread-connections.sql`, `026-npc-locations.sql` to `scripts/db-data/MANIFEST.md` with sha hashes
2. Update `010-views.sql` sha hash in `scripts/db-setup/MANIFEST.md` (views were appended, not a new file)
3. Update `reference-landmarks.md` MANIFEST hashes
4. Run `rebuild-db.sh` — verify clean rebuild with all new data
5. Run `run-tests.sh` — all 12 pass

**Gate:** Manifests match files on disk. Rebuild produces correct counts. Tests pass.

---

## Phase 7: Re-run GM Query Gauntlet

Re-run the 15 queries from the stress test. Target: ≥12/15 PASS (up from 9/15).

Expected improvements:
- Q1 "Who's at Forine?" → PASS (5+ NPCs with current_system)
- Q7 "SuSAG NPCs?" → PASS (if prose supports affiliations)
- Q2 "Forine-associated NPCs" → PASS (structured data, not text search)

Document results in ISSUES.md as updated baselines.

**Gate:** ≥12/15 queries return correct structured data. Update performance/reliability baselines.

---

## Generator Prompt

```
You are the Generator for Plan 0310.
Read: ~/software/relinquishment/plans/0310-traveller-data-completeness.md
Read: ~/software/traveller-VTT-private/reference/BruceCampaignA/npc-registry.md
Execute Phases 1-7 in order.
For Phases 1-3: READ the VTT-private prose files to extract accurate data. Do not invent facts.
For Phase 4: Cross-reference npc-registry.md mobility classes.
Each phase has a Gate — verify before proceeding.
Commit after each phase: "Plan 0310 Phase N: description"
Report: phases completed, NPC count, query gauntlet score.
```

---

## Constraints

- All scripts must be idempotent (INSERT OR IGNORE, CREATE VIEW IF NOT EXISTS)
- All data must come from existing prose — no invention
- Schema unchanged — this plan adds DATA and VIEWS only
- Existing tests must continue passing
- Git tag `pre-0310` before starting
