# Plan 0311: Traveller Reference System — Full Content Inventory

**Status:** READY FOR GENERATOR  
**Priority:** LOW — improves discoverability and completeness tracking but doesn't block other work.  
**Prerequisite:** Plan 0310 complete (data completeness), or can run independently.  
**Source:** S68 stress test #3 — Full Content Inventory.  
**Estimated effort:** Single Generator session, ~40 min.  
**Branch:** `traveller-ref-phase1` (current)

---

## Why This Plan Exists

The Traveller reference system spans two repositories and 263+ files:
- `aurasys-memory/traveller-reference/`: 76 files (30 .md, 24 .sql, 22 .sh)
- `traveller-VTT-private/reference/BruceCampaignA/`: 187+ .md files

The aurasys-memory side has MANIFESTs (db-setup, db-data, tests) covering its scripts. But:
- The VTT-private side has a CAMPAIGN-INDEX.md that is **stale** (last updated 2026-03-12, says "current location: Elixabeth" from S7 era, incorrect NPC roles)
- The VTT-private llm-knowledge-export has a MANIFEST-2026-03-10.md (also stale)
- No cross-repo manifest connects both halves
- Session prep files (S09-S13) have no manifest
- World files (16) have no manifest
- reference-landmarks.md (manifest of manifests) has no entry for VTT-private content

**Goal:** Every Traveller content file appears in at least one manifest. The manifest of manifests (reference-landmarks.md) is complete.

---

## Phase 1: Audit Current Manifest Coverage

**Action:** Generate a completeness report showing every Traveller file and which manifest covers it.

Files to scan:
1. `aurasys-memory/traveller-reference/**/*.md` (30 files)
2. `aurasys-memory/traveller-reference/scripts/**/*.sql` (24 files)
3. `aurasys-memory/traveller-reference/scripts/**/*.sh` (22 files)
4. `traveller-VTT-private/reference/BruceCampaignA/**/*.md` (187 files, excluding discord-exports/ and gigantic_roll20_campaign/)

Manifests to check against:
- `aurasys-memory/traveller-reference/scripts/db-setup/MANIFEST.md`
- `aurasys-memory/traveller-reference/scripts/db-data/MANIFEST.md`
- `aurasys-memory/traveller-reference/scripts/tests/MANIFEST.md`
- `traveller-VTT-private/reference/BruceCampaignA/CAMPAIGN-INDEX.md`
- `traveller-VTT-private/reference/BruceCampaignA/llm-knowledge-export/MANIFEST-2026-03-10.md`

**Output:** List of unmanifested files, grouped by directory. Do NOT generate a fix yet — just the report.

**Gate:** Every file has status: manifested, unmanifested, or excluded (with reason). Coverage percentage calculated.

---

## Phase 2: Update CAMPAIGN-INDEX.md

The current CAMPAIGN-INDEX.md is stale (2026-03-12). Key errors:
- "Current Location: Elixabeth" → should be "Talos/en route to Forine (as of S12)"
- Asao listed as "Gunner/Combat" → is Marine Commander
- Eddie described as "Ship AI" → is Engineering Droid (ED-7)
- Missing Jack Stone (joined S5, replaced Rufus)
- Missing S9-S13 session prep references
- Missing world file references
- Missing many NPC entries (new since March)

**Note:** There are 49 root-level .md files (arc docs, ship analyses, session logs, player comms, VTT references) plus files in 10+ subdirectories. The CAMPAIGN-INDEX rewrite must cover ALL of these.

**Action:** Rewrite CAMPAIGN-INDEX.md as a proper manifest:
- Update all stale data (location, roles, NPC list)
- Add section: Session Prep Files (S09-S13 with paths)
- Add section: World Files (16 worlds with paths)
- Add section: Faction/NPC/Character deep files (with paths)
- Add section: Ship Reference Files (barbette analysis, rules audits, computer design, combat ref)
- Add section: Campaign Arc/Planning Files (arc docs, endgame, thread map, faction reactions)
- Add section: Player Communication Files (email logs, dossiers, discord updates, oracle system)
- Add section: Cross-repo Integration (point to aurasys-memory/traveller-reference/ for DB/scripts)
- Preserve the Data Sources & Tools section (still valid)
- Add "Last Updated" with current date
- Mark deprecated/superseded files (e.g., session-prep-jan5.md, CLAUDE-CODE-SYNC-2026-03-10.md) as ARCHIVED

**Constraint:** CAMPAIGN-INDEX.md lives in VTT-private. Generator may READ this file but modifications go through Bruce (VTT-private is a separate working tree). **Generator: write the updated CAMPAIGN-INDEX content to `aurasys-memory/traveller-reference/CAMPAIGN-INDEX-DRAFT.md` for Bruce to review and copy.**

**Gate:** Draft covers all 187 VTT-private .md files (or explicitly excludes with reason). No stale data in draft.

---

## Phase 3: Add Session Prep Manifest

**New file:** `traveller-VTT-private/reference/BruceCampaignA/session-prep-s09/MANIFEST.md` (and similar for S10-S13)

Actually, a per-directory manifest is overkill for 1-9 files per session. Instead:

**Action:** Add a "Session Prep Files" section to the CAMPAIGN-INDEX-DRAFT (Phase 2) that serves as the manifest for all session prep directories:

```
## Session Prep Files

| Session | Directory | Files | Key Contents |
|---------|-----------|-------|--------------|
| S09 | session-prep-s09/ | 9 | Adventure briefs, Binges library data, Jack Stone type, PC emails, prize ship specs |
| S10 | session-prep-s10/ | 7 | Marina/Anemone riffs, adventure brief, campaign infrastructure, GM cheatsheet |
| S11 | session-prep-s11/ | 5 | Extraction, session plan, Talos arrival, Thale encounter, image prompts |
| S12 | session-prep-s12/ | 1 | Session plan (The Arrangement at Collace) |
| S13 | session-prep-s13/ | 1 | Session plan (The Forine Run) |
```

**Gate:** All session prep directories accounted for with file counts matching actual directory contents.

---

## Phase 4: World Files Manifest

**Action:** Add a "World Files" section to CAMPAIGN-INDEX-DRAFT:

```
## World Files

| World | Hex | File | Approx Lines |
|-------|-----|------|:------------:|
| Binges | 1635 | worlds/binges.md | TBD |
| Caladbolg | 1329 | worlds/caladbolg.md | TBD |
| Collace | 1237 | worlds/collace.md | TBD |
| Dallia | 1435 | worlds/dallia.md | TBD |
| Elixabeth | 1532 | worlds/elixabeth.md | TBD |
| Forine | 1533 | worlds/forine.md | TBD |
| Garoo | 0130 | worlds/garoo.md | TBD |
| HUB | — | worlds/HUB.md | TBD |
| Judice | 1337 | worlds/judice.md | TBD |
| Milagro | 1632 | worlds/milagro.md | TBD |
| Noctocol | 1433 | worlds/noctocol.md | TBD |
| Pagaton | 1634 | worlds/pagaton.md | TBD |
| Raschev | 3230 | worlds/raschev.md | TBD |
| Talos | 1436 | worlds/talos.md | TBD |
| Tarkine | 1434 | worlds/tarkine.md | TBD |
| Walston | 1232 | worlds/walston.md | TBD |
```

**Generator:** Fill in actual line counts. Cross-reference world names against `systems` table in DB — flag any world file that doesn't have a matching system entry (or vice versa: systems in DB with no world file).

**Gate:** 16 world files all listed. Cross-reference with DB shows matches (or documented exceptions for minor systems without dedicated files).

---

## Phase 5: Cross-Repo Integration Manifest

**Action:** Add entry to `reference-landmarks.md` (manifest of manifests) under TRAVELLER section:

```
- `~/software/traveller-VTT-private/reference/BruceCampaignA/CAMPAIGN-INDEX.md` — VTT-private master index (187+ files: session plans, worlds, NPCs, knowledge export, rules)
- `~/software/traveller-VTT-private/reference/BruceCampaignA/llm-knowledge-export/MANIFEST-2026-03-10.md` — LLM knowledge export manifest (54 files)
```

Also add to aurasys-memory traveller-reference a cross-reference file:

**New file:** `aurasys-memory/traveller-reference/CROSS-REPO-POINTER.md`
```markdown
# Traveller Reference — Cross-Repo Pointer

This directory contains the DB, scripts, and prose for the Traveller reference system.
The VTT-private repo contains session plans, world files, NPC deep docs, and rules exports.

- **This repo (aurasys-memory):** DB + scripts + generic prose (canon, GM tools, templates)
- **VTT-private:** Campaign-specific content (session plans, world details, NPC secrets, player stats)
- **CAMPAIGN-INDEX:** ~/software/traveller-VTT-private/reference/BruceCampaignA/CAMPAIGN-INDEX.md

The DB (campaign.db) bridges both repos — it contains structured data extracted from VTT-private prose.
```

**Gate:** reference-landmarks.md has VTT-private entries. CROSS-REPO-POINTER.md exists and paths are correct.

---

## Phase 6: Verify and Report

1. Count manifested vs unmanifested files across both repos
2. Report coverage percentage (target: ≥90% of .md files manifested)
3. List any remaining unmanifested files with reason (transient, deprecated, or needs future manifest)
4. Update reference-landmarks.md MANIFEST hashes

**Gate:** ≥90% coverage. All manifests internally consistent. reference-landmarks.md up to date.

---

## Generator Prompt

```
You are the Generator for Plan 0311.
Read: ~/software/relinquishment/plans/0311-traveller-content-inventory.md
Execute Phases 1-6 in order.
Phase 2 output goes to aurasys-memory/traveller-reference/CAMPAIGN-INDEX-DRAFT.md (NOT VTT-private directly).
Phase 5 modifications to reference-landmarks.md must preserve existing entries.
Each phase has a Gate — verify before proceeding.
Commit after each phase: "Plan 0311 Phase N: description"
Report: phases completed, coverage percentage, unmanifested file count.
```

---

## Constraints

- Do NOT modify VTT-private files directly — write drafts to aurasys-memory for Bruce to review
- Exclude from inventory: discord-exports/*.json, gigantic_roll20_campaign/*, binary files, transcripts/*.txt
- All manifests must be idempotent (re-runnable)
- Existing MANIFEST.md files in aurasys-memory are authoritative — do not restructure
- Git tag `pre-0311` before starting
