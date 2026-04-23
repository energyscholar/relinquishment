# Plan 0080: Player-Facing Ship's Log Summaries

**Status:** COMPLETE (verified S63 audit)
**Project:** Traveller Campaign (BruceGameA)
**Written:** 2026-03-12

---

## Context

Bruce wants player-safe narrative summaries of each session, written as ORACLE ship's log entries. A draft of Session 6.5/7 (Forine transit) exists at `/tmp/session6-ships-log.md` as the voice/style reference. It's good but has gaps — missing NPC names, ship names, and details that exist in source files but weren't pulled into the summary.

**Voice:** ORACLE (ship's computer). Dry, precise, appreciates good tradecraft. Ship's log format. Short sentences where they count, longer where detail earns it. NOT polished LLM prose — slightly imperfect rhythm, varied sentence length, personality showing through.

**Style reference:** `/tmp/session6-ships-log.md` — match this voice exactly.

---

## Canonical References (Generator MUST read these)

| File | Purpose | Priority |
|------|---------|----------|
| `PRIVATE/session-recap-milagro.md` | Session 5 full narrative (GM + player versions) | HIGH |
| `PRIVATE/session-log-2024-12-30.md` | Session 4 (Flammarion → Faldor → Caladbolg) | HIGH |
| `PRIVATE/session-amishi-boarding.md` | Session 4 beat sheet (planned scenes) | MEDIUM |
| `PRIVATE/llm-knowledge-export/03-chunk-01-sessions-1-5.md` | Sessions 1-5 campaign narrative | HIGH |
| `PRIVATE/llm-knowledge-export/03-chunk-02-sessions-6-10.md` | Session 6 confirmed + unconfirmed beats | HIGH |
| `PRIVATE/llm-knowledge-export/session-6-narrative.md` | Session 6 supplemental (Claude Web) | HIGH |
| `PRIVATE/llm-knowledge-export/08-session-state.md` | Current game state snapshot | MEDIUM |
| `PRIVATE/llm-knowledge-export/15-living-timeline.md` | Full timeline with NPC movements | MEDIUM |
| `PRIVATE/session-plans/session-2-forine.md` | Session 2 plan | MEDIUM |
| `PRIVATE/session-plans/session-3-forine-deep.md` | Session 3 plan | MEDIUM |
| `PRIVATE/session-plans/session-4-lifeboat.md` | Session 4 plan | MEDIUM |
| `PRIVATE/session-plans/session-5-blood-profit.md` | Session 5 plan | MEDIUM |
| `PRIVATE/session-plans-s1-s3.md` | Sessions 1-3 combined plan | MEDIUM |
| `PRIVATE/session-20-jan-2026.md` | Session notes (Jan 20) | MEDIUM |
| `PRIVATE/session-20-jan-2026-GM-CHEATSHEET.md` | GM cheatsheet (Jan 20) | MEDIUM |
| `PRIVATE/session-log-20-jan-2026.md` | Session log (Jan 20) | MEDIUM |
| `PRIVATE/session-6-mako-live-plan.md` | Session 6 Mako encounter plan | LOW |
| `PRIVATE/session-6-canon-integration.md` | Session 6 canon decisions | MEDIUM |
| `PRIVATE/npc-registry.md` | Full NPC roster (names, roles, locations) | HIGH |
| `PRIVATE/campaign-notes.md` | Campaign notes | MEDIUM |
| `PRIVATE/pc-dossiers.md` | PC backgrounds and stats | MEDIUM |
| `PRIVATE/CLAUDE.md` | GM philosophy, PC secrets, NPC profiles | HIGH |
| `/tmp/session6-ships-log.md` | **STYLE REFERENCE** — match this voice | CRITICAL |

**Path abbreviations:**
- `PRIVATE` = `~/software/traveller-VTT-private/reference/BruceCampaignA/`

**Generator launch:** `--add-dir ~/software/traveller-VTT-private/reference/BruceCampaignA/`

---

## Critical Constraints

1. **PLAYER-SAFE.** No GM secrets, no plot thread spoilers, no seed calibration, no "planned but unconfirmed" hedging. If it happened at the table, it's in. If it didn't or we're unsure, it's out. When in doubt, leave it out.
2. **ORACLE VOICE.** Not Bruce's voice. Not LLM prose. Ship's computer writing a log. Dry, precise, slightly wry. See style reference.
3. **ALL NAMES.** Every NPC, ship, location mentioned must use their canonical name from the source files. No "a friendly mining scout" — find the actual name. No "a corsair" — find the ship name. If a name truly doesn't exist in any source file, flag it as `[NAME NOT FOUND IN SOURCES]` so Bruce can fill it.
4. **SPECIFIC DETAILS.** Amounts in credits. Distances in diameters. System names with hex codes on first mention. Tonnages for ships. Skills for key checks. The ship's computer would log these.
5. **NO INVENTION.** Do not create events, dialogue, or details not in the source files. This is extraction and rewriting, not creative writing.
6. **CONFIRMED BEATS ONLY for Session 6.** The session-6-narrative.md marks beats as ✓ confirmed or ? unconfirmed. Only use ✓ beats. For chunk-02 "planned beats" — cross-reference against session-6-narrative.md confirmation status.
7. **Session 6.5/7 (Forine transit) ALREADY DONE.** Do not rewrite. The style reference IS the deliverable for that session. Generator produces Sessions 4, 5, and 6 only.

---

## Deliverables

**Output:** `PRIVATE/ships-log-player-summaries.md`
**Max length:** 1,500 words total (~400-500 per session)

### Contents Required

**Header:**
```
# ISS Astral Dawn — Ship's Log Compilations
## Compiled by ORACLE for Crew Review
```

**Entry 1: Session 4 — "Welcome Aboard"**
- Flammarion handover, first walk-through
- Shakedown cruise, JSI asteroid base visit
- Faldor stop (Max's Otarri samples)
- Caladbolg: black market, anagathics, pirate bait seeded
- Departure toward District 268

**Entry 2: Session 5 — "Milagro"**
- Jump space training (battle drills, brig space need identified)
- System arrival, prison planet warnings
- Spam lawyer crisis → Delia Cade's intervention → Barrister Chen
- Customs: crew possesses every prohibited item, relief exemption clears all
- Financial outcome (1,000cr legal, 3,000cr free fuel)
- Landing, refueled, ready

**Entry 3: Session 6 — "The Paper Trail"**
- CONFIRMED BEATS ONLY:
  - Dock shakedown (Jack lured, Asao grabbed, Brak with Form 17-C)
  - Crystal Houses / Sapphire House (fade to black)
  - Kowalski's OPSEC conditioning failures (comedy + pathos)
  - CCF investigation with Mako (IF confirmed ✓)
  - Bar fight with Groz's thugs (IF confirmed ✓)
  - Von Sydo moment at Sapphire House (mention obliquely if confirmed, no details if "debrief pending")
- End state: CCF suspicious, Lt. Kowal identified, next destination Forine

**Entry 4 (ALREADY EXISTS — do not rewrite):**
Reference: `/tmp/session6-ships-log.md` is Session 6.5/7 (Forine transit). Append it as-is to the output file.

---

## Acceptance Tests

- [ ] File exists at `PRIVATE/ships-log-player-summaries.md`
- [ ] Contains Sessions 4, 5, 6 as ORACLE ship's log entries
- [ ] Session 6.5/7 (Forine transit) appended from style reference, unmodified
- [ ] ≤1,500 words for Sessions 4-6 combined (Forine transit is extra)
- [ ] NO GM secrets (Drakon name, seed calibration, Kowal identity as leak, Harlan's tracker, psionic details)
- [ ] All NPCs use canonical names from source files
- [ ] All ships use canonical names from source files
- [ ] Mining ship at comet: name found and used (or flagged `[NAME NOT FOUND]`)
- [ ] NPC couple on mining ship: names found and used (or flagged `[NAME NOT FOUND]`)
- [ ] Kowalski mentioned by name in Session 6 entry
- [ ] No "planned but unconfirmed" beats presented as fact
- [ ] Voice matches style reference (short sentences, varied rhythm, ORACLE personality)
- [ ] No emoji, no LLM filler phrases, no "In conclusion" or "It's worth noting"
- [ ] Credits, distances, tonnages included where source files provide them
- [ ] Player-safe: could be posted in Discord #general without revealing anything

---

## Handoff Prompt

```
You are the Generator. Read Plan 0080 at ~/software/relinquishment/plans/0080-traveller-ships-log-summaries.md. Execute: create player-facing ship's log summaries for Sessions 4, 5, and 6. Read ALL canonical references listed in the plan before writing — especially the style reference at /tmp/session6-ships-log.md. Extract every NPC name, ship name, and specific detail from the source files. Output: PRIVATE/ships-log-player-summaries.md. Max 1,500 words for S4-S6. Append the Forine transit log from /tmp/session6-ships-log.md as Session 6.5. Verify against acceptance tests. Flag any names not found in sources.
```
