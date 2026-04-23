# Plan 0079: Traveller Sessions 31-40 — Comprehensive Prep

**Status:** COMPLETE (verified S63 audit)
**Project:** Traveller Campaign (BruceGameA)
**Written:** 2026-03-12
**Scope:** 10 sessions (S31-S40), detailed for S31-S33, outlined for S34-S40
**Depends on:** Plan 0078 (Session 7 Pagaton Ambush — beat sheet, combat ref, intel package)

---

## Context

Plan 0078 covers Session 7 (S31 game count) in 3 phases: beat sheet, combat quick reference, post-combat intel. This plan covers the BROADER scope:

- **Phase A:** Stale data fixes (prerequisite for all other work)
- **Phase B:** Discord combat delivery system (scripts + action menus for Pagaton battle)
- **Phase C:** PC-specific world hooks for every upcoming world
- **Phase D:** Pagaton system document (VTT-compatible coordinates)
- **Phase E:** Sessions 34-40 arc outline with world prep and seed schedule
- **Phase F:** Index updates (all new content discoverable)

**Relationship to Plan 0078:** 0078 Phases 1-3 run first (beat sheet, combat ref, intel). 0079 Phases A-F run after or in parallel. Together they cover complete prep for 10 sessions.

---

## Canonical References

| File | Purpose |
|------|---------|
| `PRIVATE/vtt-combat-reference.md` | VTT combat rules + TL upgrade system + pre-calcs (NEW, 2026-03-12) |
| `PRIVATE/astral-dawn-barbette-analysis.md` | RAW-verified barbette calcs: FC/4, HY+LR Ion, HY+IF Particle, hit tables |
| `PRIVATE/session-prep-gap-analysis-s7-s9.md` | Gap analysis for S31-S33 |
| `PRIVATE/npc-registry.md` | Full NPC roster with mobility classes |
| `PRIVATE/pirate-taxonomy-district268.md` | All 6 pirate groups + ecosystem |
| `PRIVATE/factions/blood-profit-pack.md` | Blood Profit fleet, personnel, ops |
| `PRIVATE/factions/jsi-imperial-authority.md` | JSI framework, James's rank, prize options |
| `PRIVATE/recurring-npcs.md` | Ship-mobile NPCs and their corridor schedules |
| `PRIVATE/characters/*.json` | PC stats for combat calculations |
| `PRIVATE/worlds/*.md` | Existing world docs |
| `VTT/data/star-systems/.backup/` | System astrophysics (400+ systems) |
| `VTT/data/star-systems/spinward-marches/subsector-n-district-268.json` | Full D268 system data |
| `VTT/data/sectors/spinward-marches.enriched.json` | AUTHORITATIVE for UWP/star disputes |
| `VTT/data/weapons/weapons.json` | Weapon stats |
| `VTT/data/drills/*.json` | Combat drill scenarios (enemy stats, formations) |

**Path abbreviations:**
- `PRIVATE` = `~/software/traveller-VTT-private/reference/BruceCampaignA/`
- `VTT` = `~/software/traveller-starship-operations-vtt/`

---

## Critical Constraints

1. **VTT is NOT live at the table.** Software not ready. Use VTT *data and rules* as reference, not the running application.
2. **Discord IS the interface.** Roll20 for maps. Discord for: narration, ship's computer messages via private DM channels to each PC, combat action queries, images.
3. **Armor 1** for Astral Dawn. NOT 14. Multiple files still stale.
4. **PC hooks on every world.** Each world the PCs visit must have at least 1-2 things that specifically call to individual PCs based on their backstory, skills, or player type (Robin's Laws mapping in traveller-campaign.md memory).
5. **Ion weapon formula:** 7D x3 (campaign standard per weapons.json + design review).
6. **Seed schedule:** Seeds 3-4 by S31-S33, Seeds 5-6 by S35-S37, Drakon reveal S38+.
7. **Combat pacing:** 30-45 min table time. The drama is in the reveal and boarding, not grinding rounds. AD wins easily — this is the REWARD for preparation.
8. **Discord action queries:** When a PC's role comes up in combat, query them via DM: "Option 1: [specific]. Option 2: [specific]. 3: Tell me what you do." Simple, fast, keeps all PCs engaged.

---

## Phase A: Stale Data Fixes

**Generator deliverable:** Edits to existing files (no new files)
**Model:** Sonnet (mechanical find-and-replace)
**Priority:** PREREQUISITE — do first

### Tasks

1. **`VTT/data/ships/v2/astral_dawn.json`** — Change `armour.rating` from 14 to 1. READ the file first; do NOT change hullPoints unless they're clearly wrong (the ship design may use a different formula than tonnage/2.5).
2. **`PRIVATE/llm-knowledge-export/05-ship-astral-dawn.md`** — Find all instances of "Armor 14" or "Armour 14", replace with "Armor 1". Add note: "Corrected 2026-03-12 per Bruce design review."
3. **`PRIVATE/llm-knowledge-export/13b-combat-cards-1.md`** — Same armor correction. Also fill `[NEED PC SHEET]` placeholders using data from `PRIVATE/characters/*.json` (Von Sydo, Asao, Marina, Jack). Leave James and Max as `[PC SHEET MISSING]`.
4. **`PRIVATE/npc-registry.md`** — Update Marina's homeworld from "?" to "Allgaran IV". Verify Jeri Tallux shows "Glisten" (2036).

### Acceptance Tests

- [ ] astral_dawn.json: `armour.rating` = 1
- [ ] 05-ship-astral-dawn.md: zero instances of "Armor 14" or "Armour 14" (case-insensitive search)
- [ ] 13b-combat-cards: Von Sydo, Asao, Marina, Jack cards filled from JSON data
- [ ] npc-registry.md: Marina homeworld = "Allgaran IV"

---

## Phase B: Discord Combat Delivery System

**Generator deliverable:** `PRIVATE/session-plans/session-7-discord-combat.md`
**Max length:** 4,000 words
**Model:** Opus (voice, dramatic pacing, PC psychology)
**Priority:** HIGH — transforms combat from dice-rolling to immersive experience

### Design

Bruce drops pre-written messages into Discord during combat. Two channels per PC:
- **#spinward-marches** (group channel): Narration, images, ship status
- **PC DM** (private): Ship's computer role-specific messages, action queries

### Contents Required

#### Part 1: Group Channel Narration Beats (~15 messages)

Short, vivid narration drops for key combat moments. 2-4 sentences each. Written in ship's-computer-report style mixed with cinematic description.

Required beats:
1. **Jump emergence** — Pagaton system appears on screens
2. **First contact** — sensors detect the corsair
3. **Corsair hail** — pirate demands (full dialogue)
4. **Stalling** — AD "merchant" response (options for James)
5. **Q-ship reveal** — hidden weapons deploy (THE moment, 6+ lines, visceral)
6. **First volley** — AD opens fire
7. **Ion hit** — corsair power systems stagger
8. **Corsair fires back** — near miss or glancing hit (tension maintenance)
9. **Particle hit** — hull breach on corsair
10. **Corsair desperation** — attempts to flee or signal for help
11. **Fighters launch** (CONDITIONAL — only if Bruce deploys them)
12. **Corsair surrender** — power failing, hull breached, captain yields
13. **Boarding commences** — marines cross
14. **Ship secured** — Asao reports all clear
15. **Aftermath** — floating in Pagaton system, prize alongside, crew processing

#### Part 2: Per-PC Ship's Computer Messages (~10 per role, 60 total)

Delivered to PC DMs at appropriate combat phases. Written in-character as ship AI (Eddie for general, AG-3 Gamma for gunnery). Include data from vtt-combat-reference.md calculations.

**James (Captain) — 10 messages:**
- Pre-combat: threat assessment, recommended battle plan
- Each round: tactical update (range, hull status, enemy actions)
- Decision points: "Recommend weapons free" / "Boarding window opening"
- Post-combat: damage report, crew status, prize assessment

**Marina (Gunnery) — 10 messages:**
- Weapon status reports with actual hit probabilities (from vtt-combat-reference.md pre-calcs)
- Target lock quality at current range
- Ammo status (missiles, sandcasters)
- "Barbette alpha: charged. Ion — 97% hit probability at current range. Fire solution locked."
- Post-volley: damage assessment on target

**Asao (Marines) — 10 messages:**
- Marine section readiness reports
- Enemy crew estimate from sensors
- Breach point analysis
- "Twelve marines at Battle Station 3. Sgt. Reyes confirms ready. Recommend pinnace approach, ventral airlock."
- Boarding progress: "Deck 1 secured. 6 crew surrendered. Proceeding to engineering."

**Max (Engineering) — 10 messages:**
- Power budget (percentage bars using Unicode blocks)
- System status: all green → damage warnings
- "Power plant nominal at 84%. Weapons grid: full. Jump drive: 4hr spin-up if needed."
- Damage control priorities after hits

**Von Sydo (Sensors) — 10 messages:**
- Contact details with range, bearing, signature analysis
- ECM/ECCM recommendations
- Emission analysis: "Transponder falsified. Hull profile: 400t armed trader. Weapons powering up on hardpoints 1, 3."
- Scan depth progression: passive → active → deep

**Jack (Pilot) — 10 messages:**
- Evasion status and thrust budget
- "Current vector suboptimal. Recommend 15° port yaw for broadside."
- Fighter bay status (if deploying)
- Docking approach for boarding

#### Part 3: PC Action Queries (~3 per PC per combat)

Discord DM format. Sent when PC's role activates in phase order.

**Format:**
```
🔴 COMBAT ROUND [N] — [PHASE] — Your action, [Name]:

1. [Specific option with mechanical effect]
2. [Specific option with mechanical effect]
3. Tell me what you do.

⏱️ 30 seconds
```

**James action queries:**
- Round 1: "1. Order weapons free (all turrets + barbettes). 2. Hold fire, attempt intimidation hail. 3. Tell me what you do."
- Round 2: "1. Press attack — close range for kill shot. 2. Demand surrender via comms. 3. Tell me what you do."
- Round 3: "1. Order boarding. 2. Disable and stand off. 3. Tell me what you do."

**Marina action queries:**
- "1. Ion barbette — cripple their power (97% hit, ~88 power drain). 2. Particle barbette — hull damage (97% hit, ~45 hull dmg). 3. Tell me what you do."

**Asao action queries:**
- Pre-boarding: "1. Standard breach — pinnace to ventral lock, 8 marines. 2. Double breach — split team, both airlocks. 3. Tell me what you do."
- During boarding: "1. Secure engineering first (capture data before purge). 2. Bridge assault (capture captain alive). 3. Tell me what you do."

**Max action queries:**
- "1. Full power to weapons grid (+1 FC). 2. Charge jump drive (emergency escape option in 4hrs). 3. Redistribute to [specific system]. 4. Tell me what you do."

**Von Sydo action queries:**
- "1. Active scan — full sensor sweep (reveals everything, also reveals US). 2. Passive monitoring — maintain stealth. 3. Focused scan — deep scan the corsair only. 4. Tell me what you do."

**Jack action queries:**
- "1. Full evasive — 3 Thrust reserved, enemy -3 to hit us. 2. Close to Short range — better hit chance, they hit us easier. 3. Hold course — maintain Medium range. 4. Tell me what you do."

### Acceptance Tests

- [ ] File exists at `PRIVATE/session-plans/session-7-discord-combat.md`
- [ ] Group narration: ≥15 beats covering full combat arc
- [ ] Per-PC messages: ≥8 per role, ≥48 total
- [ ] Action queries: ≥2 per PC, ≥12 total
- [ ] Action queries use format: numbered options + "tell me what you do" + timer
- [ ] Hit probabilities in Marina's messages match vtt-combat-reference.md calculations
- [ ] Eddie/AG-3 Gamma voice consistent (ship AI personality)
- [ ] Q-ship reveal narration: ≥6 lines, visceral, cinematic
- [ ] Pirate captain has dialogue (name from Plan 0078 Phase 1 — **DEPENDENCY: run 0078 Phase 1 first**, or create pirate captain inline)
- [ ] All messages deliverable via Discord copy-paste (no special formatting)
- [ ] Armor 1 for AD (NOT 14)
- [ ] ≤4,000 words total

---

## Phase C: PC-Specific World Hooks

**Generator deliverable:** `PRIVATE/session-plans/pc-world-hooks-s31-s40.md`
**Max length:** 3,000 words
**Model:** Opus (requires understanding PC psychology, backstory, player type)
**Priority:** HIGH — makes every world personally meaningful

### Design Principles

Every world the PCs visit MUST have content that calls to specific PCs. Not generic — tied to their backstory, skills, relationships, or player type (Robin's Laws). Some hooks call to one PC. Some to all. GM deploys based on table energy.

### Required PC Profiles (for Generator context)

| PC | Backstory Hooks | Skills to Feature | Player Type | What Excites Them |
|----|----------------|-------------------|-------------|-------------------|
| James | Secret Admiral, Darrian contacts, Zhanis Tel-Morat, political authority | Tactics, Leadership, Diplomat | Tactician/Storyteller | Strategic decisions, political intrigue, using authority |
| Marina | Blood oath vs Black Lord Kiseth, Duchess Marchant connection, mother's politics, Naval Academy | Gunner 6, Diplomat 2, Deception 1 | Tactician/Method Actor | Gunnery excellence, diplomatic solutions, personal quest progression |
| Asao | Aslan honor, false charges, wife Htasea'a on Caladbolg, genocide secret, Raschev allies | HW(MP) 3, Melee 3, Leadership 2 | Butt-Kicker/Specialist | Tough fights, honor challenges, protecting innocents |
| Max | Bio-anagathics discovery, Otarri contacts, scientific curiosity, published paper | Engineer, Science, Investigation | Specialist/Tactician | Scientific puzzles, tech mysteries, practical problem-solving |
| Von Sydo | Illegal psionics, Vera relationship, Ghersak nemesis (pirate telepath), psi training | Psi (28 powers), Sensors, Tactics 2 | Method Actor/Specialist | Psionic encounters, moral complexity, sensor warfare |
| Jack | Ex-pirate (Red Wake), name on pirate hull, Vargr identity, new to crew | Pilot 3, DEX 15, Melee(Blade) 3, Persuade 3 | Casual (developing) | Piloting challenges, pirate world connections, proving loyalty |

### Worlds to Cover (S31-S40 route)

**Confirmed route:** Forine → Pagaton → [Tarkine or Dallia] → [onwards toward Collace]

| World | Sessions | Hook Requirements |
|-------|----------|-------------------|
| Pagaton (1634) | S31-S33 | Combat hooks + post-combat exploration |
| Tarkine (1434) | S34-S35 | Otarri, Ember Church, wilderness |
| Dallia (1435) | S34-S36 | Darrian intelligence, politics |
| Talos (1436) | S36-S37 (possible) | Poor world, mineral resources |
| Collace (1237) | S38-S40 | Industrial powerhouse, endgame setup |
| Binges (1635) | Pass-through? | OPTIONAL — brief stop possible, minimal canonical data |

### Per-World Hook Format

For each world, provide:
```
## [World Name] (Hex NNNN)

### All-PC hooks (deploy for whole group)
- [Hook description — what it is, why it matters]

### PC-specific hooks
- **James:** [What calls to James specifically]
- **Marina:** [What calls to Marina specifically]
- **Asao:** [What calls to Asao specifically]
- **Max:** [What calls to Max specifically]
- **Von Sydo:** [What calls to Von Sydo specifically]
- **Jack:** [What calls to Jack specifically]

### Deployment notes
[When to deploy, table energy conditions, what hooks combine well]
```

### Minimum Hook Requirements

- **Pagaton:** ≥2 per PC (combat + post-combat). Asao gets a tough fight. Jack faces pirate identity. Marina gets a gunnery triumph. Von Sydo senses Ghersak's absence (relief or suspicion?). Max analyzes captured tech. James makes the prize disposition call.
- **Tarkine:** ≥2 per PC. Max gets Otarri reunion (Keloru). Von Sydo gets Ember Church psionic contact (Sister Maren). Asao gets wilderness challenge. Jack gets Oberlindes merchant connection (Hanne Brekke — ex-pirate to legitimate trader parallel).
- **Dallia:** ≥2 per PC. James gets Darrian intelligence meeting (Zhanis network). Marina gets diplomatic mission opportunity. Von Sydo senses Darrian psionic traditions. Max encounters advanced Darrian science.
- **Collace:** ≥2 per PC. James confronts the CCF/Drakon political structure directly. Marina's Duchess Marchant connection may have reach here. Asao's wife Htasea'a sends intel (email system). Industrial world = Max paradise.

### Acceptance Tests

- [ ] File exists at `PRIVATE/session-plans/pc-world-hooks-s31-s40.md`
- [ ] ≥5 worlds covered
- [ ] Every world has ≥1 hook per PC (≥6 hooks per world, ≥30 total)
- [ ] Hooks reference specific PC backstory details (not generic)
- [ ] Robin's Laws player types inform hook design (noted in deployment notes)
- [ ] Pagaton hooks include: Asao tough fight, Jack pirate identity, Marina gunnery triumph
- [ ] Tarkine hooks include: Keloru + Max, Sister Maren + Von Sydo
- [ ] Dallia hooks include: Darrian intel + James
- [ ] Format follows template above (all-PC + per-PC + deployment notes)
- [ ] ≤3,000 words

---

## Phase D: Pagaton System Document

**Generator deliverable:** `PRIVATE/worlds/pagaton.md`
**Max length:** 2,500 words
**Model:** Sonnet acceptable (data-driven, structural)
**Priority:** MEDIUM — enriches S31-S33 but combat can run without it

### Data Sources

Generator MUST read these before writing:
1. `VTT/data/star-systems/.backup/pagaton.json` — existing system astrophysics (12 celestial objects)
2. `VTT/data/star-systems/spinward-marches/subsector-n-district-268.json` — Pagaton entry
3. `VTT/data/sectors/spinward-marches.enriched.json` — **grep for "1634"** (file is 634KB, don't read whole thing). Canonical UWP + star type.
4. `PRIVATE/session-prep-gap-analysis-s7-s9.md` — Section IV (Pagaton system gaps)

### Stellar Type Resolution

The backup JSON says F0 V. The subsector file says G2 V. **Check the enriched sector file (AUTHORITATIVE).** Use whichever the enriched file says. Note the discrepancy and which was chosen.

### Contents Required

1. **System overview** — star type (resolved), UWP, trade codes, allegiance, population
2. **Celestial object table** — all objects from backup JSON with: name, type, orbitAU, bearing, radiusKm. Compatible with VTT display format.
3. **Mainworld profile** — atmosphere (Standard per UWP 6), hydrosphere (90% per UWP 9), population (10^8), gov (8 = civil service bureaucracy), law (7), TL 4
4. **Gas giant fuel skimming** — which gas giant, distance from mainworld, approach time at various thrust ratings
5. **Asteroid belt** — location, composition, density. THIS IS THE AMBUSH SITE. Detail hiding spots, sensor shadows, approach vectors.
6. **Encounter geometry** — jump emergence zone (extended due to gravitational well overlap per S6 transcript), distance to belt, intercept timeline. How long from emergence to corsair detection to weapons range.
7. **Pirate staging area** — 2-3 specific asteroid clusters (generate names) where a corsair could hide with engines cold. Sensor profiles at various ranges.
8. **Starport** — Class C, what services. Who runs it (TL-4 bureaucracy). Attitude toward outsiders.
9. **Local color** — 100 million people at TL-4 (Industrial Age). What's their daily life? Do they know about the pirates? (Probably not — space is another world to them.) What do they trade? (Rich world — agricultural, phosphates.)
10. **GM quick reference** — first impressions, hazards, cultural notes, arrival procedure

### Acceptance Tests

- [ ] File exists at `PRIVATE/worlds/pagaton.md`
- [ ] Star type resolved against enriched sector file with discrepancy noted
- [ ] All celestial objects from backup JSON included in table
- [ ] Asteroid belt has named hiding spots (≥2)
- [ ] Encounter geometry: emergence → detection → engagement timeline
- [ ] Gas giant fuel skimming distance and time calculated
- [ ] Starport description (Class C, services, attitude)
- [ ] Local population color (TL-4, 10^8, Rich world)
- [ ] ≤2,500 words

---

## Phase E: Sessions 34-40 Arc Outline

**Generator deliverable:** `PRIVATE/session-plans/arc-outline-s34-s40.md`
**Max length:** 3,000 words
**Model:** Opus (arc design, dramatic structure, seed calibration)
**Priority:** MEDIUM — long-range planning

### Contents Required

1. **Route decision tree** — after Pagaton, PCs choose: Tarkine (1434), Dallia (1435), or both. Map the possibilities. Include Binges (1635) and Talos (1436) as waypoints.

2. **Seed progression schedule:**

| Session | Seeds to Advance | Method |
|---------|-----------------|--------|
| S34-S35 | Seed 5 (financial trail deepens) | Tarkine: Sister Maren's network has heard rumors. OR Dallia: Darrian intel confirms CCF pattern |
| S36-S37 | Seed 6 (Forine-based entity identified) | Convergence of evidence. PCs can now say "someone on Forine is running this" |
| S38-S39 | Seed 7 (Drakon named) | Collace contact or captured data names Drakon Syndicate explicitly |
| S40 | Seed 8 (scope of operation) | Full picture: Drakon → JMC → Blood Profit. Next target: Walston base |

3. **Per-session outline** (S34-S40, 200 words each):
   - Key beats (deployable, not fixed)
   - Which PCs get spotlight
   - Recurring NPC appearances (check corridor schedules in npc-registry.md)
   - Dramatic question for the session

4. **Agent Thale tracker** — where is he each session? 2 jumps behind PCs. Starting position: Garoo (0130) or last known per npc-registry.md. Calculate his position based on route. When does he catch up? What happens?

5. **Blood Profit escalation** — after Pagaton, the pack KNOWS about the Q-ship. How do they respond? Increase caution? Set a trap? Consolidate at Walston? Call for help?

6. **Prize ship subplot** — what happens to the captured corsair? Options from jsi-imperial-authority.md (Elixabeth, Mille Falcs, Flammarion, fleet asset). Decision point at which session?

7. **Character arcs** — where is each PC's personal story heading?
   - James: Admiral authority tested, Darrian alliance deepening
   - Marina: Closer to Black Lord Kiseth trail? Diplomatic Corps application?
   - Asao: Wife reunion timing (Htasea'a), genocide audit approaching
   - Max: Bio-anagathics implications, scientific reputation
   - Von Sydo: Psi power growth, Ghersak confrontation approaching
   - Jack: Pirate past confrontation, Red Wake Brotherhood echoes

### Acceptance Tests

- [ ] File exists at `PRIVATE/session-plans/arc-outline-s34-s40.md`
- [ ] Route decision tree with ≥2 branches
- [ ] Seed schedule S34-S40 (Seeds 5-8)
- [ ] Per-session outlines for S34-S40 (7 sessions)
- [ ] Agent Thale position tracker
- [ ] Blood Profit response to Pagaton defeat
- [ ] Prize ship subplot with decision point session
- [ ] Character arc notes for all 6 PCs
- [ ] ≤3,000 words

---

## Phase F: Index Updates

**Generator deliverable:** Edits to existing index files
**Model:** Sonnet (mechanical)
**Priority:** MUST DO LAST (after all other phases complete)

### Tasks

1. **`PRIVATE/CAMPAIGN-INDEX.md`** — Add entries for all new files created in Phases A-E. Add VTT Combat Reference to reference section.

2. **`~/.claude/projects/-home-bruce-software-aurasys-memory/memory/traveller-campaign.md`** — Add to appropriate sections:
   - `vtt-combat-reference.md` under Rules Reference
   - `session-7-discord-combat.md` under Session Plans
   - `pc-world-hooks-s31-s40.md` under Session Plans
   - `worlds/pagaton.md` under World Docs
   - `arc-outline-s34-s40.md` under Session Plans
   - Note Discord combat delivery system under Working Agreements

3. **Verify** all file paths in updated indexes resolve to actual files.

### Acceptance Tests

- [ ] CAMPAIGN-INDEX.md references all new files
- [ ] traveller-campaign.md memory updated with all new entries
- [ ] All file paths in both indexes resolve (no broken references)
- [ ] Discord combat delivery noted in Working Agreements section

---

## Execution Order

```
Phase A (stale fixes)  ←── FIRST, prerequisite
     ↓
Phase B (Discord combat) ←── HIGHEST VALUE, transforms combat experience
Phase C (PC world hooks) ←── Can run parallel with B
Phase D (Pagaton world) ←── Can run parallel with B, C
Phase E (S34-S40 arc)  ←── Can run parallel with B, C, D
     ↓
Phase F (indexes)      ←── LAST, after all content exists
```

**Combined with Plan 0078:**
```
0078 Phase 1 (beat sheet)     }
0078 Phase 2 (combat ref)     } ←── Run first or parallel with 0079 Phase A
0078 Phase 3 (intel package)  }
     ↓
0079 Phases A-E               ←── Run after or parallel
     ↓
0079 Phase F (indexes)        ←── Last
```

---

## Out of Scope

- Running VTT software live (not ready, book priority)
- Generating Pagaton world map SVG/PNG (no source SVG available)
- Pirates of Drinax content (LOST from disk — needs Bruce to re-provide)
- James Delleron / Max Planck character JSONs (waiting on player submissions)
- Walston base detail (S40+ territory)
- Full Drakon org chart (S38+ territory)
- Ship's computer software integration (future — Discord manual delivery for now)

---

## Handoff Prompts

### Phase A Handoff
```
You are the Generator. Read Plan 0079 at ~/software/relinquishment/plans/0079-traveller-sessions-31-40-comprehensive.md. Execute Phase A: fix stale data in 4 files. Use Sonnet. Verify against acceptance tests. Report changes made.
```

### Phase B Handoff
```
You are the Generator. Read Plan 0079 Phase B. Create the Discord combat delivery system. Read PRIVATE/vtt-combat-reference.md for combat calculations, PRIVATE/characters/*.json for PC stats, Plan 0078 for encounter context. Output: PRIVATE/session-plans/session-7-discord-combat.md. Max 4,000 words. Verify against acceptance tests.
```

### Phase C Handoff
```
You are the Generator. Read Plan 0079 Phase C. Create PC-specific world hooks for S31-S40. Read PRIVATE/npc-registry.md (corridor schedules), PRIVATE/characters/*.json (backstories), PRIVATE/worlds/*.md (existing world docs). Also read PRIVATE/recurring-npcs.md for ship-mobile NPC schedules. Output: PRIVATE/session-plans/pc-world-hooks-s31-s40.md. Max 3,000 words. Verify against acceptance tests.
```

### Phase D Handoff
```
You are the Generator. Read Plan 0079 Phase D. Create Pagaton system document. Read the 3 VTT data sources listed + gap analysis Section IV. Resolve stellar type against enriched sector file. Output: PRIVATE/worlds/pagaton.md. Max 2,500 words. Verify against acceptance tests.
```

### Phase E Handoff
```
You are the Generator. Read Plan 0079 Phase E. Create S34-S40 arc outline. Read PRIVATE/pirate-taxonomy-district268.md, PRIVATE/factions/*.md, PRIVATE/npc-registry.md (Agent Thale entry, corridor schedules), PRIVATE/session-prep-gap-analysis-s7-s9.md (seed schedule). Output: PRIVATE/session-plans/arc-outline-s34-s40.md. Max 3,000 words. Verify against acceptance tests.
```

### Phase F Handoff
```
You are the Generator. Read Plan 0079 Phase F. Update CAMPAIGN-INDEX.md and traveller-campaign.md memory with all files created in Phases A-E. Verify all file paths resolve. Report any broken references.
```
