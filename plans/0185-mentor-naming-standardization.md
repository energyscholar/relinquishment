# Plan 0185 — Standardize mentor character naming: David (youth) → Healer (post-medic-training)

**Status:** READY — Phases D-G of Plan 0244 (Master Execution Plan)
**Type:** Character-naming standardization pass across manuscript prose. Four phases, four commits. Halt-and-report at ambiguous cases.
**Scope (verified S63):** 215 David/Lane references across 26 files.

## Context

Current prose uses 4+ names for the same person: Healer, David Lane, Lane, David. Bruce's call (2026-04-13): **one canonical name in narrative prose, with one earned-name transition.** Confirmed still needed (Bruce S63).

## The rule

- **David** — pre-combat-medic-training: childhood, ranch life, recruitment, basic training until combat-medic certification.
- **Healer** — post-combat-medic-training: from combat medic certification forward (1984 Northern Ireland onward). All adult/military/DARPA/Bruce-era prose.
- **David Lane** — appears ONCE, in the biographical reveal (summary.tex:245), explicitly as "not his real name." Frames the dual-register: on paper David Lane, in this book Healer.
- **Lane** (without David) — removed from narrative prose entirely. Never appears except as part of the revealed pseudonym "David Lane" at :245.
- **Steven "Legs" Lane** — preserved as-is. External published-account cover identity (McNab/Ryan Bravo Two Zero accounts). Not a name the book chooses; left verbatim where it appears.

**Narrative justification of the transition:** the name "Healer" is earned at combat-medic certification (pos03-the-mentor.tex:90 "He trains as a combat medic"). Pre-training = David the boy; post-training = the man whose calling becomes healing. This maps to the book's epistemic-distance discipline: name the role, not the person.

**Reported-speech rule (IMPORTANT — added S63):** When Healer is TELLING a story about his youth, the narrator still calls him Healer — because the narrator knows him as Healer. Only use "David" when the READER is in a scene where the pre-medic character is directly present (childhood flashback prose, not reported speech). This matters especially in pos05-the-stories.tex (26 hits) where Healer tells Bruce stories spanning many periods. halt-and-report on all ambiguous cases.

## Pre-flight (Generator, once at start of Phase D)

```
cd /home/bruce/software/relinquishment
grep -rn "\bDavid\b\|\bLane\b" manuscript/ --include="*.tex" | grep -v "staging/\|sources/\|raw/\|versions/" | grep -v "^[^:]*:[0-9]*:%" > /tmp/0185-name-audit.txt
wc -l /tmp/0185-name-audit.txt
cut -d: -f1 /tmp/0185-name-audit.txt | sort | uniq -c | sort -rn
```

Expect **215 hits across 26 files.** This is the working list. Generator checks each hit against the rule.

### Full file inventory (verified 2026-04-23):

| Hits | File | Phase |
|------|------|-------|
| 39 | track-2-testament/pos03-the-mentor.tex | E |
| 36 | record/what-healer-said.tex | G |
| 26 | track-2-testament/pos05-the-stories.tex | F |
| 24 | track-2-testament/pos02-alpha-farm.tex | F |
| 24 | record/alpha-farm.tex | G |
| 7 | track-2-testament/pos29-twenty-years.tex | F |
| 7 | record/twenty-years.tex | G |
| 6 | 00-front/summary.tex | D |
| 5 | track-2-testament/pos23-the-weight.tex | F |
| 5 | track-2-testament/pos07-the-departure.tex | F |
| 5 | record/the-question.tex | G |
| 5 | record/the-departure.tex | G |
| 4 | track-2-testament/pos33-digital-doppelganger.tex | F |
| 4 | track-2-testament/pos29-the-silence.tex | F |
| 3 | spine/the-braid.tex | D |
| 3 | bridge/pos10-the-braid.tex | D |
| 3 | appendix/topic-guide.tex | D |
| 1 | track-1-confession/pos18-the-walk-out.tex | D |
| 1 | spine/the-factoring-game.tex | D |
| 1 | record/the-walk-out.tex | G |
| 1 | record/the-handler.tex | G |
| 1 | interlude/evidence-interlude.tex | D |
| 1 | bridge/pos09-the-factoring-game.tex | D |
| 1 | appendix/corrections.tex | D |
| 1 | 99-back/acknowledgements.tex | D |
| 1 | 00-front/corrections.tex | D |

## Phase D — Front matter + ancillary files (commit 1)

**Scope:** ~20 hits across ~12 files. Mostly mechanical (1-3 hits per file). One significant prose change (biographical reveal).

**NOTE:** summary.tex was already edited at :311 by Plan 0165 (Phase A). Different paragraph, no conflict. But line numbers may have shifted. GREP for text, don't trust line numbers.

**Files:**
- `manuscript/00-front/summary.tex` (6 hits)
- `manuscript/00-front/corrections.tex` (1 hit)
- `manuscript/99-back/acknowledgements.tex` (1 hit)
- `manuscript/appendix/corrections.tex` (1 hit)
- `manuscript/appendix/topic-guide.tex` (3 hits)
- `manuscript/interlude/evidence-interlude.tex` (1 hit)
- `manuscript/spine/the-braid.tex` (3 hits)
- `manuscript/spine/the-factoring-game.tex` (1 hit)
- `manuscript/bridge/pos09-the-factoring-game.tex` (1 hit)
- `manuscript/bridge/pos10-the-braid.tex` (3 hits)
- `manuscript/track-1-confession/pos18-the-walk-out.tex` (1 hit)

**Key edits:**

- `summary.tex:26` — "That was Lane, years later" → "That was Healer, years later" — **FIRST-USE FIX. Critical.** Reader currently meets "Lane" 219 lines before learning the name.
- `summary.tex:199` — "drew on Lane's Maori cultural heritage" → "drew on Healer's Maori cultural heritage"
- `summary.tex:245` — **Biographical reveal rewrite.** Current: `His name is David Lane \textit{(not his real name)}.` **Replace with something that frames the dual-register.** Suggested:

  > The name on his passport --- David Lane --- is not his real name either. In this book I call him Healer, the name he earned when he was certified as a combat medic at nineteen. He is half Maori...

  **EDITORIAL NOTE:** The current reveal is punchy and tight. The rewrite MUST be at least as punchy. If the proposed text feels explanatory, write something better. halt-and-report if unsure.

- `summary.tex:247, 253, 259` — "Lane" → "Healer" in remaining instances.
- `pos18-the-walk-out.tex:40` — "a brash and daring warrior-scholar named David" → "named Healer" (adult, DARPA era). Or restructure if "named Healer" sounds odd — Generator judges.
- Spine + bridge files: mechanical Lane→Healer.
- Corrections files: sync convention documentation.

**Acceptance (Phase D):**
1. `grep -n "\bLane\b" manuscript/00-front/*.tex manuscript/99-back/*.tex manuscript/spine/*.tex manuscript/bridge/*.tex manuscript/appendix/*.tex manuscript/interlude/*.tex manuscript/track-1-confession/*.tex` returns hits only in corrections (documenting convention), "David Lane" reveal, and "Steven 'Legs' Lane."
2. `make html` clean.

**Commit:** `Plan 0185 phase D: mentor naming in front matter, spine, bridge, appendix (Lane→Healer)`

## Phase E — pos03-the-mentor.tex (commit 2)

**Scope:** 39 hits in one file. **Hardest single file** — spans childhood → military → present with name transition.

Apply rule **in place**: sentences describing pre-combat-medic-training scenes keep "David"; sentences describing post-training scenes use "Healer." The transition beat at "He trains as a combat medic" is the hinge.

**Specific guidance:**
- **Youth scenes (pre-medic):** KEEP "David." Officer Ken kangaroo incident, ranch life, boyhood.
- **Training itself:** KEEP "David" — the training EARNS the name. Add one short transition sentence after certification: `From that point the men in his unit called him Healer.` (Generator may refine; halt-and-report if unsure.)
- **Adult scenes (post-medic):** USE "Healer." Operation Desert Shield, Bravo Two Zero, SAS service, DARPA era, Bruce era.
- **"Steven 'Legs' Lane":** PRESERVE verbatim. Published-account cover identity.
- **"David Lane" biographical references:** PRESERVE where the full pseudonym is stated.

**Acceptance (Phase E):**
1. `grep -n "\bDavid\b" manuscript/track-2-testament/pos03-the-mentor.tex` returns hits only in youth scenes (pre-combat-medic training) + "David Lane" reference.
2. `grep -n "\bLane\b" manuscript/track-2-testament/pos03-the-mentor.tex` returns hits only in "Steven 'Legs' Lane" + "David Lane."
3. Name transition sentence exists and reads naturally.
4. `make html` clean.

**Commit:** `Plan 0185 phase E: mentor naming in pos03-the-mentor (name transition at combat medic certification)`

## Phase F — Dense Track-2 chapters (commit 3)

**Scope:** ~75 hits across 7 files. Bulk of the Track-2 work.

**Files and hit counts:**
- `pos02-alpha-farm.tex` (24 hits) — Bruce-era adult scene. All David/Lane → Healer.
- `pos05-the-stories.tex` (26 hits) — **NARRATIVE LANDMINE.** Healer telling Bruce stories about various periods. See reported-speech rule above. When Healer is TELLING a story about his youth, narrator calls him Healer. Only use "David" for direct-flashback scenes. halt-and-report on ALL ambiguous cases in this file.
- `pos07-the-departure.tex` (5 hits) — Adult scene.
- `pos23-the-weight.tex` (5 hits) — Bruce-era adult scene.
- `pos29-the-silence.tex` (4 hits) — Bruce-era.
- `pos29-twenty-years.tex` (7 hits) — Bruce-era.
- `pos33-digital-doppelganger.tex` (4 hits) — Bruce-era adult scene.

**Acceptance (Phase F):**
1. `grep -n "\bDavid\b" manuscript/track-2-testament/*.tex` returns hits only in: youth scenes (pos03 from Phase E), "David Lane" reveals, and any genuinely pre-medic scenes in other chapters.
2. `grep -n "\bLane\b" manuscript/track-2-testament/*.tex` returns hits only in "David Lane" + "Steven 'Legs' Lane."
3. `make html` clean.

**Commit:** `Plan 0185 phase F: mentor naming in track-2 chapters (dense files)`

## Phase G — Record chapters + verification sweep (commit 4)

**Scope:** ~79 hits across 7 files. Many mirror Track-2 counterparts — apply same decisions.

**Files and hit counts:**
- `record/what-healer-said.tex` (36 hits) — **DENSE.** Mirrors pos05-the-stories. Same reported-speech rule applies.
- `record/alpha-farm.tex` (24 hits) — Mirrors pos02. Same rule.
- `record/twenty-years.tex` (7 hits) — Mirrors pos29-twenty-years.
- `record/the-departure.tex` (5 hits) — Mirrors pos07.
- `record/the-question.tex` (5 hits) — Review each: adult = Healer.
- `record/the-handler.tex` (1 hit) — Dossier style.
- `record/the-walk-out.tex` (1 hit) — Adult.

**Final verification sweep:**
```
# After all 4 commits:
grep -rn "\bDavid\b\|\bLane\b" manuscript/ --include="*.tex" | grep -v "staging/\|sources/\|raw/\|versions/" | grep -v "^[^:]*:[0-9]*:%" > /tmp/0185-final-audit.txt
# Every remaining hit must be: youth-David, "David Lane" reveal, "Steven 'Legs' Lane", or corrections-documentation.
```

**Acceptance (Phase G):**
1. Final audit grep shows ONLY: youth-David, "David Lane" pseudonym reveal, "Steven 'Legs' Lane" verbatim, corrections documentation.
2. `grep -rn "\bHealer\b" manuscript/ --include="*.tex"` shows expanded footprint.
3. `make html` clean.
4. `make check` passes.

**Commit:** `Plan 0185 phase G: mentor naming in record chapters + verification sweep`

## Build + push

After all four commits land clean, push per `feedback-build-to-website.md`. Tag optional — Bruce's call.

## Rollback

Four separate commits make bisection easy. `git revert` any individual phase without losing others.

## Out of scope (do NOT touch)

- `manuscript/staging/raw/*.md` — raw source documents
- `manuscript/versions/simple-summary.md` — derived/alt version
- `manuscript/bibliography.bib`, any `.aux` files

## Handoff report (Generator, 6 lines per phase)

Per phase:
1. Commit SHA.
2. Pre-flight audit line count (215 total; shrinking across phases).
3. Per-file conversion counts: N David→Healer, N Lane→Healer, N left as David (youth), N left as "David Lane" (reveal), N left as "Steven 'Legs' Lane" (verbatim).
4. Halt-and-report events: count + locations. If zero, say so.
5. Build result.
6. Any surprises (references in files not anticipated above).

## Annealing Log (S63, 4-pass — post-scope-correction)

### HIGH — scope expansion:
- Cover staging/ and raw/? KILLED — source documents, not prose.
- Cover simple-summary.md? KILLED — derived version, Bruce regenerates.
- Standardize OTHER character names? KILLED — scope creep.
- Fold into Custodian rename? NO — different character, already done (aa467a9).

### MEDIUM — test each phase:
- Phase D (front matter + ancillary): summary.tex first-use fix is CRITICAL. Biographical reveal rewrite is ambitious but necessary — must be at least as punchy as original. Light files are mechanical. KEEP.
- Phase E (pos03 alone): 39 hits with name transition. Deserves its own session — too much judgment to batch. halt-and-report essential. KEEP.
- Phase F (dense Track-2): 75 hits. pos05-the-stories.tex is a LANDMINE (reported speech). Reported-speech rule added. halt-and-report on all ambiguous pos05 cases. KEEP.
- Phase G (Record mirrors): 79 hits but many mirror Track-2 decisions made in Phase F. what-healer-said.tex (36 hits) is the densest Record file. KEEP after Phase F.
- Four commits: Good granularity. Phases E and F are riskiest — separate commits allow selective revert. CONFIRMED.

### LOW pass 1 — line number verification:
- summary.tex:26 "That was Lane" — verified 2026-04-23. ✓
- summary.tex:199, 245, 247, 253, 259 — verified. ✓
- Line numbers may shift after Plan 0165 (Phase A). GREP for text. ✓
- pos03 line numbers from original plan: spot-check against current file at execution time.

### LOW pass 2 — interaction check:
- Plan 0165 (Phase A) edits summary.tex:311. DIFFERENT paragraphs. ✓
- Plan 0241 (Phase A) edits pos34b. Uses "Healer" already. ✓
- Plan 0242 (Phases B-C): preprocess.py only. ✓
- Phase D→E→F→G strict order: each builds on prior. ✓

**Rating: 8.5/10.** (Up from 8/10: scope corrected from 100→215 hits, missing files added, reported-speech rule added, biographical reveal OOPS flagged, 4 phases not 3.) Remaining risk: pos03 name transition and pos05 reported-speech ambiguity. Both have halt-and-report safety valves.
