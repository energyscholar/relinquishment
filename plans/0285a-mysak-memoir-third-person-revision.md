# Plan 0285a — Mysak Joint Memoir: Third-Person Revision + Lawrence Feedback

**Status:** ANNEALED — ready for Generator
**Author:** Auditor (Argus S67)
**Parent:** Plan 0285 (phase 1 COMPLETE — v2 draft exists at `memoir/drafts/bruce-half-v2.md`)
**PTL:** PTL-122
**Urgency:** TONIGHT — Bruce committed to sending Lawrence a revised version by end of day 2026-05-04. Lawrence returns additions by Wednesday 2026-05-07.

---

## What Changed: Phone Call 2026-05-04 15:10 PDT

Transcript: `~/deleteme/mysak/Mysak_memoir_2026_05_04_17_03_35_transcript.md`

### Lawrence's Feedback

1. **Third person.** Lawrence wants the memoir rewritten in third person — not first person. This is the structural change. The v2 draft is entirely first-person ("I asked Lawrence," "my mother Linda"). Must become third-person throughout ("Bruce asked Lawrence," "his mother Linda").

2. **Lawrence's self-introduction.** Lawrence drafted his own opening line: "...and a flute-playing professor emeritus from McGill, with many published papers to his credit... he is the other author of this story." He's writing himself INTO the piece — not just filling hooks but actively shaping the narrative frame.

3. **Confirmed details (use in revision):**
   - Singing on the bus: confirmed, multiple times, Lawrence and Janet led it
   - Impromptu flute concert: confirmed ("food concert" — may be Lawrence's term)
   - The dining area: "great big dining area, almost alone, our group at a great long table"
   - Topic of dinner conversation: "Ocean Dynamics and Mathematics until the food came"
   - Berlin Wall 1972: Lawrence saw the wall, steel pipes, barbed wire

4. **References to add:**
   - Bruce's arXiv preprint (2601.22389) — Lawrence noted "your preprint is submitted"
   - The memoir chapter Bruce read (Moscow/Berlin conference) — Lawrence remembers Bruce reading it
   - Lawrence's three AMOC papers — Lawrence looking up exact titles, will send

5. **Lawrence's working style:** He's typing notes during the call, adding material in his own time (afternoons), returning by Wednesday. He's engaged as a co-writer, not a reviewer.

---

## Pre-flight

1. Verify source: `cat ~/software/relinquishment/memoir/drafts/bruce-half-v2.md | wc -w` (should be ~850-900 words)
2. Verify transcript: `ls ~/deleteme/mysak/Mysak_memoir_2026_05_04_17_03_35_transcript.md`
3. Verify pandoc: `pandoc --version` (needed for .docx output — if missing, install or skip .docx and note)
4. Read Plan 0285 section "Constraints" for must-include/must-exclude lists

---

## Scope of This Sub-Plan

**Single task:** Convert `bruce-half-v2.md` from first person to third person, incorporating Lawrence's confirmed details and self-introduction framing. Preserve all existing structure, hooks, and insertion markers.

This is NOT a rewrite. The five beats, comedic structure, hooks, and emotional spine from Plan 0285 are all correct. The change is mechanical (POV) plus detail enrichment from the call.

**Confirmed by Lawrence (2026-05-04):** He likes the current draft, plans to fill in his sections and return additions by Wednesday. This cleanup gives him a better base to work from.

---

## Conversion Rules

### POV Shift
- "I" → "Bruce" or "he" (vary for readability)
- "my mother Linda" → "his mother Linda" or "Linda"
- "I asked Lawrence" → "Bruce asked Lawrence"
- "I read them" → "Bruce read them" / "he read them"
- Direct quotes from Bruce stay in first person within quotation marks: Bruce told him: "Had you not encouraged me..."
- Handoff sentences to Lawrence stay in first person — these are Bruce speaking directly to Lawrence: "I leave it to you..." These are authorial asides, not narration.
- Insertion markers `[Lawrence — ...]` unchanged

### Detail Updates
- Beat 1: Incorporate "Ocean Dynamics and Mathematics until the food came" (already in v2 — verify wording matches Lawrence's confirmed version)
- Beat 1: Strengthen bus singing — Lawrence confirmed "several times," "it was great"
- Beat 1: Lawrence's self-framing: "a flute-playing professor emeritus from McGill with many published papers to his credit... the other author of this story" — INTEGRATE this into the existing opening (which already has similar language: "a flute-playing professor emeritus from McGill with a hundred and eighty published papers"). Use Lawrence's version as the base and weave in the paper count. Do NOT duplicate — one introduction, blending both voices.
- Beat 4: Add reference note for arXiv preprint (2601.22389)
- Memoir chapter reference: leave as "the story of Bob Dietz and a conference behind the Iron Curtain" — Bruce will verify the specific chapter from Lawrence's memoir collection in hand edits
- Beat 1 or context: Lawrence saw Berlin Wall 1972 — available detail but may not fit memoir's Costa Rica arc. Use only if natural.

### Prefatory Note
Plan 0285 specified a prefatory note ("Lawrence — You'll find marked places...") but v2 didn't include one and Lawrence understood the hooks without it. Do NOT add a standalone prefatory note to v3. The hooks are self-explanatory. Bruce may add a cover note in the email.

### What NOT to Change
- Five-beat structure
- Hook placement and insertion markers
- Comedic expectation→subversion pivots
- Must-include / must-exclude lists from Plan 0285
- Target length (600-900 words)
- Tone: warmth, Lawrence as senior figure, humor from situation not jokes

---

## Deliverables

1. `memoir/drafts/bruce-half-v3.md` — third-person revision (Bruce's working copy)
2. `memoir/drafts/bruce-half-v3.docx` — pandoc conversion (what Lawrence receives)
3. `memoir/drafts/bruce-half-v3.txt` — plain text fallback

All three must have insertion markers. Editorial scaffold in .md only.

---

## Verification Checklist

- [ ] NO first-person narration remains (except direct quotes and handoff asides to Lawrence)
- [ ] Word count 600-900
- [ ] Five beats present and ordered
- [ ] All Lawrence hooks and insertion markers preserved
- [ ] Lawrence's confirmed details incorporated (singing, dining area, Ocean Dynamics)
- [ ] arXiv preprint reference present
- [ ] Memoir chapter reference present (Moscow/Berlin — the one Bruce and Linda edited)
- [ ] No TQNN, Flat, Diamond Node, Healer detail
- [ ] No email quotes
- [ ] Lawrence as senior figure throughout
- [ ] Three output files (.md, .docx, .txt)
- [ ] .docx is PRIMARY delivery format

---

## Timeline

- **Tonight (2026-05-04):** Bruce reviews v3, hand-edits, sends to Lawrence
- **By Wednesday (2026-05-07):** Lawrence returns his additions
- **Then:** Plan 0285 phase 2 — merge Lawrence's additions, next revision cycle

---

## Generator Prompt

```
You are the Generator for Plan 0285a.

Read: ~/software/relinquishment/plans/0285a-mysak-memoir-third-person-revision.md

Then read source material:
1. ~/software/relinquishment/memoir/drafts/bruce-half-v2.md (current draft — convert this)
2. ~/deleteme/mysak/Mysak_memoir_2026_05_04_17_03_35_transcript.md (today's call — confirmed details)

Convert the v2 draft from first person to third person. Preserve all structure,
hooks, insertion markers, and emotional spine. Incorporate Lawrence's confirmed
details from today's call. Do NOT rewrite — convert and enrich.

Save to memoir/drafts/ as bruce-half-v3.md, .docx, .txt.
Run verification checklist. Do NOT send to Lawrence.
Commit: "Plan 0285a: Mysak memoir v3 — third-person conversion per Lawrence feedback"
```
