# Plan 0078: Traveller Session 7 Prep — Pagaton Ambush

**Status:** COMPLETE (verified S63 audit)
**Project:** Traveller Campaign (BruceGameA)
**Written:** 2026-03-12
**Game date:** Tuesday 2026-03-17 (6 days)

---

## Context

Session 6 (2026-03-10) ended at Forine. Session 7: depart Forine, jump to Pagaton, encounter a single Blood Profit corsair. This is the crew's FIRST real space combat — an easy win designed to reward preparation.

**Pacing philosophy (Bruce, S6 debrief):** Session scope is player-determined. Prepare deployable beats, not fixed sequences. Keep PCs at criticality. Read the room.

---

## Canonical References (Generator MUST read these)

| File | Purpose | Authority |
|------|---------|-----------|
| `PRIVATE/session-prep-gap-analysis-s7-s9.md` | Full gap analysis, open questions, seed schedule | High |
| `PRIVATE/pirate-taxonomy-district268.md` | Blood Profit fleet, personnel, tactics, funding | Canonical |
| `PRIVATE/session-plans/session-5-blood-profit.md` | STRUCTURE/PACING reference only — wrong encounter scale | Medium |
| `PRIVATE/worlds/pagaton.md` | System map, astrophysics, encounter geometry | Canonical |
| `PRIVATE/CLAUDE.md` | PC secrets, NPC profiles, GM philosophy | Canonical |
| `PRIVATE/llm-knowledge-export/13b-combat-cards-1.md` | Combat stat cards — WARNING: Armor 14 is STALE | Reference (stale) |
| `VTT/data/weapons/weapons.json` | Weapon registry | Canonical |
| `VTT/data/ships/v2/astral_dawn.json` | Ship stats — WARNING: Armor 14 is STALE | Reference (stale) |
| `VTT/.claude/MONGOOSE-TRAVELLER-RULES-EXTRACT.md` | Combat rules reference | Canonical |
| `PRIVATE/adventure-hooks/kolvar-brenn-forine.md` | Bren steganographic channel | Canonical |
| `VTT/data/sectors/spinward-marches.enriched.json` | Sector data — AUTHORITATIVE for UWP/star disputes | Canonical |

**Path abbreviations:**
- `PRIVATE` = `~/software/traveller-VTT-private/reference/BruceCampaignA/`
- `VTT` = `~/software/traveller-starship-operations-vtt/`

**Generator launch:** `--add-dir ~/software/traveller-VTT-private/reference/BruceCampaignA/ --add-dir ~/software/traveller-starship-operations-vtt/data/`

---

## Critical Constraints

1. **ARMOR 1** for Astral Dawn. NOT 14. Per Bruce's design review (`VTT/drafts/astral-dawn-review-for-group.txt`). Multiple files still show 14 — ignore them.
2. **SINGLE CORSAIR** encounter. NOT the full Blood Profit Pack. One ship, alone. Easy win.
3. **Pirate taxonomy is canonical** for Blood Profit personnel/ships/tactics. Session 5 is STRUCTURE/PACING reference only — its NPC names (Kfourrz, Ghersak) and fleet composition are from an earlier concept.
4. **Oeg** is the Blood Profit alpha (pirate taxonomy). He is NOT at Pagaton — he runs the pack, not individual ambushes.
5. **Ion weapon formula:** Use 7D×3 per weapons.json and design review (campaign standard). Note the 2D×10 discrepancy exists but don't resolve it.
6. **Established fighter pilots:** Hardpoint (Dex Morain, Lt., commander), Whisper, Brick, Ghost, Preacher, Dice. Use these names.
7. **Tarek Maves** (pirate taxonomy) is Whisper's academy rival and pilots *Whisper Kill*. If Tarek is present, this creates a personal subplot.
8. **Jack Stone** is ex-pirate (Red Wake Brotherhood). His name is painted on the *Red Wake*'s hull. First combat has emotional weight for him.
9. **OPSEC:** All output files are in a PRIVATE repo. No restrictions on content.
10. **Seed schedule:** Session 7 should advance Seeds 3-4 (organized backing, CCF pattern) but NOT reveal Drakon by name. Full reveal deferred to Session 9+.

---

## Defaults (Bruce can override)

- **Encounter ship:** ~400t, not the flagship. *Thornback* (400t converted merchant from taxonomy) or detached element. Generator decides based on fleet logistics (note: *Thornback* is Jump-1 only — explain how it reached Pagaton).
- **Combat pacing:** 30-45 minutes table time.
- **Fighter deployment:** GM's call based on table energy. Prep for both (launch vs. hold).
- **Prize disposition:** Open decision point for PCs.
- **Forine departure:** Included as optional opening beats, deployable if session starts there.

---

## Phase 1: Session 7 Beat Sheet

**Generator deliverable:** `PRIVATE/session-plans/session-7-pagaton.md`
**Max length:** 3,000 words
**Model:** Use Opus for judgment calls (NPC personality, pacing, dramatic beats)

### Contents Required

1. **Optional Forine departure beats** — Bren's first steganographic message (pirate movement intel, Pagaton timing), Jeri's preliminary financial analysis, announced departure. Clearly marked DEPLOYABLE.
2. **Jump to Pagaton** — travel time, crew activity during jump, tension building.
3. **System arrival** — sensor sweep, detection sequence, the corsair closing.
4. **Pirate demands** — the corsair hails, demands cargo/boarding. "Merchant" stalls. Write dialogue for pirate captain (new NPC: name, one-trait, voice sample, Vargr or human per taxonomy).
5. **Q-ship reveal** — scripted dramatic moment. Hidden weapons deploy. Pirate reaction. ≥10 lines of dialogue/narration. Adapt from S5 Scene 1 structure but for single-ship encounter.
6. **Combat** — simplified for beat sheet (detailed mechanics in Phase 2). Key rounds, decision points, energy curve. At least 2 PC decision points.
7. **Boarding sequence** — Asao's marines. Mechanical resolution (opposed rolls or narrative). What they find inside (crew, cargo, computers). Pirate surrender trigger.
8. **Post-combat** — prize assessment, damage, crew reactions, fuel state. Refer to Phase 3 for intel content.
9. **PC spotlight matrix** — all 6 PCs get at least one spotlight moment. Format per S5.
10. **Pacing notes** — energy curve with HIGH/LOW phases. Each major beat is DEPLOYABLE (can be used or skipped). Session can end at multiple natural points.
11. **Fighter pilot reactions** — brief (1-2 lines each) for first-combat moments. Hardpoint, Whisper, Brick, Ghost, Preacher, Dice.
12. **NPC quick reference** — pirate captain + any new NPCs introduced, one-trait format.

### Acceptance Tests

- [ ] File exists at `PRIVATE/session-plans/session-7-pagaton.md`
- [ ] Contains Forine departure beats marked as DEPLOYABLE
- [ ] Q-ship reveal: ≥10 lines of scripted dialogue/narration
- [ ] Pirate captain NPC: name, one-trait, voice sample
- [ ] Boarding sequence with mechanical resolution
- [ ] PC spotlight matrix covers all 6 PCs
- [ ] Uses Armor 1 for Astral Dawn (search for "14" — should not appear as armor value)
- [ ] Single ship encounter (not full Blood Profit fleet)
- [ ] Encounter ship identified with stats summary
- [ ] ≥2 PC decision points (per Robin's Laws)
- [ ] Pacing notes with energy curve
- [ ] Each major beat is deployable (not required in fixed sequence)
- [ ] ≤3,000 words
- [ ] Verify Pagaton star type against enriched sector file; note if discrepancy found

---

## Phase 2: Combat Quick Reference

**Generator deliverable:** `PRIVATE/session-plans/session-7-combat-ref.md`
**Max length:** 2,000 words
**Model:** Sonnet acceptable (mechanical/structural)

### Contents Required

1. **Round structure** — what happens each round, in order. Table format.
2. **Per-role action menu** — what can each PC DO each round. All 6 PCs.
   - James (Captain): Tactics, orders, comm hails
   - Marina (Gunnery): Fire weapons, coordinate fighters, target selection
   - Asao (Marines): Boarding prep, point defense assist, damage control
   - Max (Engineering): Power allocation, damage control, jump drive
   - Von Sydo (Sensors): Detect, lock, ECM/ECCM, sensor warfare
   - Jack (Pilot): Maneuver, evasive action, docking
3. **Pre-calculated hit probabilities** — Astral Dawn weapons vs corsair at short/medium/long range. Include dodge effects (Jack: Pilot 3 + DEX +3 = DM+6 per Thrust reserved).
4. **Corsair stats** — derived from pirate taxonomy ship entry + weapons.json. Hull, armor, weapons, thrust, crew.
5. **Astral Dawn stats** — corrected (Armor 1, FC/4, canonical weapons from design review: 2 visible turrets, 2 hidden turrets, Ion barbette HY+LR, Particle barbette HY+IF). See `PRIVATE/astral-dawn-barbette-analysis.md` for RAW-verified damage calcs and `PRIVATE/vtt-combat-reference.md` for pre-calculated hit tables.
6. **Damage thresholds** — corsair hull total, when systems start failing, surrender trigger (hull below 30%).
7. **Ion weapon effects** — power drain, duration, effect on corsair's power plant. What happens when power drops below maneuver/weapons threshold.
8. **Sandcaster defense** — how it works, effectiveness vs lasers and missiles.
9. **Key rules summary** — dodge, called shots (if any), initiative, range bands.

### Acceptance Tests

- [ ] File exists at `PRIVATE/session-plans/session-7-combat-ref.md`
- [ ] ≤2 pages equivalent (≤2,000 words)
- [ ] Round structure in table format
- [ ] Per-role action menu for all 6 PCs
- [ ] Hit probabilities at 3+ range bands
- [ ] Armor 1 for Astral Dawn (NOT 14)
- [ ] Corsair stats consistent with pirate-taxonomy-district268.md
- [ ] Ion weapon damage/effects included
- [ ] Dodge calculation: Jack Pilot 3 + DEX +3
- [ ] Surrender trigger specified

---

## Phase 3: Post-Combat Intel Package

**Generator deliverable:** `PRIVATE/session-plans/session-7-intel-package.md`
**Max length:** 2,000 words
**Model:** Opus for judgment (seed calibration, dramatic pacing)

### Contents Required

1. **Pirate computer file inventory** — ≥5 distinct file types. Each with: filename, content summary, what PC specialty finds it.
2. **Cargo manifest fragments** — resupply pattern showing regular supply source. Amounts, dates, items. Points toward organized backing WITHOUT naming Drakon.
3. **Financial records** — JMC payments (name appears on records). Amounts without full context. Pattern of regular "geological survey data" purchases. Suspicious but not conclusive.
4. **One encrypted message fragment** — partially decrypted. References "the arrangement" and "the next shipment." Sender unknown. Tantalizing, not complete.
5. **Navigation logs** — frequent returns to a specific set of coordinates (Walston's location, but expressed as nav coordinates, not named). Max or Von Sydo can match to star charts.
6. **Crew personal communications** — humanizing detail. A pirate writing home. Someone complaining about Oeg's decisions. Makes pirates people, not cardboard.
7. **Per-PC discovery matrix** — who finds what based on their specialty:
   - James: command/intel files, strategic assessment
   - Marina: weapons logs, engagement records
   - Asao: ship layout, crew strength, boarding defense plans
   - Max: engineering logs, fuel records, tech analysis
   - Von Sydo: sensor data, communications, encrypted files
   - Jack: navigation logs, flight patterns, pilot notes

### Seed Calibration

| Seed | Status After S7 | What to Reveal |
|------|-----------------|----------------|
| Seed 3 (CCF immunity) | CONFIRMED | Financial records show CCF-connected payments |
| Seed 4 (organized backing) | HINTED | Supply pattern + encrypted message = someone funding this |
| Drakon identity | NOT REVEALED | No name. "Forine-based entity" at most |
| Walston base | HINTED | Nav coordinates cluster, not named |
| Lt. Kowal leak | NOT REVEALED | Too early |

### Acceptance Tests

- [ ] File exists at `PRIVATE/session-plans/session-7-intel-package.md`
- [ ] ≥5 distinct file types from pirate computer
- [ ] Financial records reference JMC or CCF
- [ ] Does NOT name Drakon Syndicate
- [ ] Does NOT name Walston explicitly
- [ ] Contains one encrypted/partial message about "the arrangement"
- [ ] Per-PC discovery matrix for all 6 PCs
- [ ] Seed calibration matches table above
- [ ] ≤2,000 words
- [ ] Crew personal comms included (humanizing detail)

---

## Execution Order

Phases 1-3 are independent — can run in parallel if token budget allows.

**Phase 1** is highest priority (can't run the session without it).
**Phase 2** is second (combat will be awkward without quick reference).
**Phase 3** can be improvised if time runs out, but pre-written is much better.

---

## Out of Scope (deferred)

- Ship's computer combat templates (60-90 messages) — Phase 4 if time permits, not in this plan
- Binges world doc — not needed for S7
- Dallia/Tarkine adventure seeds — Session 9+ territory
- Fleet operations framework — not needed for single-ship encounter
- Updating stale VTT JSON files (astral_dawn.json Armor 14→1) — separate maintenance task
- Updating stale knowledge export files (05-ship-astral-dawn.md, 13b-combat-cards) — separate

---

## Handoff Prompts

### Phase 1 Handoff
```
You are the Generator. Read Plan 0078 at ~/software/relinquishment/plans/0078-traveller-session7-pagaton-ambush.md. Execute Phase 1: create the Session 7 beat sheet. Read all canonical references listed in the plan before writing. Output: PRIVATE/session-plans/session-7-pagaton.md. Max 3,000 words. Verify against acceptance tests.
```

### Phase 2 Handoff
```
You are the Generator. Read Plan 0078 at ~/software/relinquishment/plans/0078-traveller-session7-pagaton-ambush.md. Execute Phase 2: create the Combat Quick Reference. Read pirate taxonomy, weapons.json, rules extract, and design review before writing. Output: PRIVATE/session-plans/session-7-combat-ref.md. Max 2,000 words. Verify against acceptance tests.
```

### Phase 3 Handoff
```
You are the Generator. Read Plan 0078 at ~/software/relinquishment/plans/0078-traveller-session7-pagaton-ambush.md. Execute Phase 3: create the Post-Combat Intel Package. Read pirate taxonomy (especially Drakon funding mechanism, Section 1) and gap analysis Section VII before writing. Output: PRIVATE/session-plans/session-7-intel-package.md. Max 2,000 words. Verify against acceptance tests.
```
