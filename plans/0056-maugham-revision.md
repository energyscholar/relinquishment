# Plan 0056: The Maugham Revision

**Auditor:** Argus (Session 31)
**Date:** 2026-03-04
**Status:** APPROVED — Bruce authorized direct execution (not Generator)
**Branch:** `maugham-revision` (created from `pre-maugham` tag)
**Supersedes:** PTL-062 (absorbs its best ideas; PTL-062 becomes source document)
**Source documents:** PTL-058 through 061, Genevieve memo (2026-03-01), S31 Maugham conversation

---

## Bruce's Review System

### Markers

Two LaTeX commands defined in preamble for this revision:

- `\mrev{text}` — New or modified prose. Renders with blue left margin bar + blue text in PDF. Greppable: `grep -rn 'mrev' manuscript/`
- `\mrevmoved{text}` — Existing prose relocated (not new, just moved). Renders with gray left margin bar. Greppable separately.

After Bruce reviews and approves each passage, he removes the `\mrev{}` wrapper (keeping the text). When all `\mrev` markers are gone, the revision is complete.

### Token Form: Old vs. New Structure

**OLD STRUCTURE (pre-maugham tag):**
```
FRONT MATTER (8,800 words before narrative)
  Hook ................ "What Would You Do?" + Three Possibilities (full)
  Summary ............. Narrative + Three Possibilities (full) + Evidence + Predictions
  TOC
  Genevieve Preface ... Editorial statement
  Preface ............. Bruce's voice + predictions reference
  Not Claimed ......... 5 disclaimers
  Introduction ........ Three Possibilities (full) + Warning + predictions
  Corrections ......... 7 errors with A/B/C analysis

PART I: THE STORY
  pos01 ............... Three Possibilities (FOURTH time!) ← reader still hasn't met Bruce
  pos02 ............... Alpha Farm ← FIRST NARRATIVE (7,900 words in!)
  pos04 ............... The Code War
  pos05 ............... The Stories
  pos06 ............... The Secret
  pos07 ............... The Departure + Joy Close Reading (16 points, prosecutorial)

PART II: THE RECKONING
  pos08 ............... Dual Use (lecture)
  pos22 ............... Why Give It Up (lecture)
  pos18 ............... Walk-Out (narrative resumes after two lectures)
  pos23-pos34b ........ [7 chapters unchanged]

PART III: THE IMPLICATIONS (The Wall — 6 speculative chapters, no relief)
  pos24 ............... Instantiation (opens with declaration, no human anchor)
  pos25 ............... Ethical Framework (biggest claim = flattest voice)
  pos27-pos31 ......... [4 more chapters, no Bruce reflection between them]

PART IV: THE SCIENCE
  [12 chapters — abrupt bridge→confession transitions]

PART V: THE QUESTION
  pos36 ............... Steel-Man A
  pos35 ............... The Question (366 words — compressed)
```

**NEW STRUCTURE (maugham-revision branch):**
```
FRONT MATTER (3,800 words — 57% reduction)
  Hook ................ "What Would You Do?" + ONE seed sentence about uncertainty
  Summary ............. Narrative only — no Evidence, no Predictions, brief Three Possibilities
  TOC
  Genevieve Preface ... [unchanged]
  Preface ............. [predictions reference removed]
  Author's Note ....... NEW (150 words) — "three possibilities, twenty years, reader decides"

PART I: THE STORY
  pos02 ............... Alpha Farm ← FIRST CHAPTER! Reader meets Bruce immediately     ★ MOVED
  pos05 ............... The Stories                                                     ★ MOVED (was after pos04)
  pos04 ............... The Code War
  pos06 ............... The Secret
  pos07 ............... The Departure + Joy Close Reading (8-10 points, observational)   ★ MODIFIED

⸻ INTERLUDE: THE THREE POSSIBILITIES (~2,130 words) ★ NEW ⸻
  Bridge .............. "I've told you what happened. Now..."
  Three Possibilities . ONE full statement of A/B/C (assembled from pos01 + Introduction)
  Not Claimed ......... [relocated from front matter]
  What I Got Wrong .... [relocated from front matter]
  Warning ............. [relocated from Introduction]

PART II: THE RECKONING
  pos18 ............... Walk-Out (narrative first!)                                     ★ MOVED
  pos08 ............... Dual Use
  pos22 ............... Why Give It Up
  pos23-pos34b ........ [7 chapters unchanged]

⸻ INTERLUDE: THE EVIDENCE (~800 words) ★ NEW ⸻
  Evidence for ........ [relocated from Summary]
  Evidence against .... [relocated from Summary]
  What the book does .. [relocated from Introduction]

PART III: THE IMPLICATIONS (Wall broken with human texture)
  Opening note ........ NEW (~100 words) — predictions reference
  pos24 ............... Instantiation (human anchor opening + Bruce reflection)         ★ MODIFIED
  pos25 ............... Ethical Framework (biggest claim = quietest voice)              ★ MODIFIED
  pos27 ............... Extension (+ Bruce reflection)                                 ★ MODIFIED
  pos30 ............... Unipolar Condition (+ Bruce reflection)                        ★ MODIFIED
  pos32 ............... Magnetosphere (+ Bruce reflection)                             ★ MODIFIED
  pos31 ............... Wolfram

PART IV: THE SCIENCE
  [12 chapters — with transition sentences at bridge→confession boundaries]            ★ MODIFIED (transitions)

PART V: THE QUESTION
  pos36 ............... Steel-Man A
  pos35 ............... The Question (800-1000 words — investigator's arc resolves)     ★ MODIFIED
```

**Key:** ★ MOVED = existing content relocated | ★ NEW = new content | ★ MODIFIED = existing content edited

### Review Guide for Bruce

After all phases complete, Bruce's review process:
1. `grep -rn 'mrev' manuscript/` — see ALL changed/new passages with file:line
2. Open each file in subl, search for `\mrev` — read blue-marked passages in context
3. For each `\mrev{...}`: approve (remove wrapper) or edit (modify text, keep wrapper until satisfied)
4. `\mrevmoved{...}` passages: verify they work in new location (content is familiar, just moved)
5. When all markers removed → revision complete
6. Build PDF, flip through — blue margin bars show all changes visually

---

## Context

Genevieve identified a structural pathology: 7,900 words of epistemic scaffolding before any narrative. Bruce's mother Linda collapsed to Possibility A before opening the manuscript — the extraordinary claims arrived before trust. The Razor's Edge provides a proven model for the exact problem this book faces: how to present extraordinary claims through a peripheral narrator who admits ignorance, using earned escalation rather than front-loaded assertion.

This plan restructures the manuscript to apply seven Maugham techniques, redistribute scaffolding into Genevieve's three-phase model (Immersion → Pattern → Formalization), and calibrate tone so register DROPS as claims get BIGGER.

## Governing Principles

1. **Trust before framework.** Reader must care about Bruce before evaluating his claims.
2. **Register drops as claims rise.** Quietest voice for biggest claims. Opposite of current manuscript.
3. **Inoculate against collapse.** Show moments where certainty fails. Reader watches collapsers be wrong.
4. **Resolve the investigator's arc, not the subject's.** Book ends when Bruce's access ends.
5. **Human texture carries weight.** Bruce reflections between heavy passages (the Elliott Principle).
6. **Layered transmission.** Most extraordinary claims arrive in most indirect voice.
7. **Gaps are load-bearing.** Narrator's comfort with ignorance IS his credibility.
8. **Narrative before analysis.** Show first, explain after. Always.

## Execution Strategy: Why Not Triad

**Recommendation: I execute all phases directly in the maugham-revision branch, with Bruce reviewing diffs at phase gates.**

**Why:**
- Tone calibration requires full context (Maugham techniques, reader collapse analysis, investigator's arc) that cannot be encoded in a Generator plan without the plan itself becoming 10,000+ words
- "Generator runs seem to be about 1-2% of total time and effort" — the value is in planning and context, both of which live only in this shell
- The branch provides rollback safety equivalent to the Triad (pre-maugham tag restores everything)
- Phase gates give Bruce review points identical to Auditor review
- All new prose marked \mrev — Bruce will edit, as with all book content

**What this requires from Bruce:**
- Temporary authorization for Argus to modify manuscript files in the maugham-revision branch
- Review diffs at each phase gate (I'll summarize changes and show the diff)
- Keep main branch frozen during revision (or we rebase)

**Safety nets:**
- `pre-maugham` tag on main (full restore point)
- Phase commits (can revert any individual phase)
- \mrev markers on all new prose (Bruce edits before publication)
- Build verification at each phase

---

## Phase 1: Front Matter Surgery

**Impact:** Highest. Reader reaches narrative 4,100 words earlier.
**Risk:** Low. No narrative content touched.
**Commit:** "Plan 0056 phase 1: front matter surgery"

### 1A. Edit hook.tex
- Strip explicit Three Possibilities framework paragraphs
- Replace with ONE seed sentence: "He doesn't know what's true. He offers three possibilities — confabulation, exaggeration, or the most important true story never told — and invites you to weigh it yourself."
- Keep: "A man falls from the sky" narrative opening, all narrative beats, "What would you do?" closing

### 1B. Edit summary.tex
- Remove "The Evidence" section (~600 words) → moves to Evidence Interlude (Phase 3)
- Remove "The Predictions" section (~250 words) → moves to Part III opening note (Phase 3)
- Trim "Three Possibilities" section from ~350 to ~120 words (each possibility = one sentence, Bruce's position = one sentence, no "What this means" analysis)
- Keep: All narrative sections unchanged

### 1C. Edit preface.tex
- Remove paragraph referencing predictions
- Keep Bruce's voice, personal framing

### 1D. Create authors-note.tex (~150 words)
> This book presents three possibilities about events spanning 1988 to 2006. The author does not know which is true. He has maintained that uncertainty for twenty years.
>
> What follows is the full account — the people, the science, the ethics, and the question at the heart of all of it. The three possibilities are explored throughout. The evidence is presented as it was encountered. The reader decides.

### 1E. Edit main.tex front matter
- Remove \include for not-claimed.tex (content → Interlude, Phase 2)
- Remove \include for introduction.tex (content → Author's Note + Interludes)
- Remove \include for corrections.tex (content → Interlude, Phase 2)
- Add \include for authors-note.tex after preface
- Build and verify

### Acceptance Criteria — Phase 1
- [ ] Front matter word count < 4,000 (currently ~8,800)
- [ ] Three Possibilities appears exactly once in front matter (seed in hook)
- [ ] No "Evidence" or "Predictions" sections before Part I
- [ ] Author's Note is ≤ 150 words
- [ ] Build succeeds, PDF renders correctly

---

## Phase 2: Part I Restructure + Three Possibilities Interlude

**Impact:** Core structural change. Reader hits Alpha Farm as Chapter 1.
**Risk:** Medium. Creates new chapter, removes existing chapter, reorders Part I.
**Commit:** "Plan 0056 phase 2: Part I restructure + Three Possibilities Interlude"

### 2A. Edit main.tex — Part I
- Remove \include for pos01-three-possibilities (content → Interlude)
- Reorder Part I: pos02 (Alpha Farm) → pos05 (Stories) → pos04 (Code War) → pos06 (Secret) → pos07 (Departure)
- Alpha Farm becomes Chapter 1. Reader's first experience is Bruce in a pink muumuu, not an epistemic framework.

### 2B. Create manuscript/interlude/ directory

### 2C. Create three-possibilities-interlude.tex (~2,130 words)
Assembled from redistributed content:

1. **Opening bridge** (~100 words, new, \mrev):
   > "I've told you what happened — or what I believe happened, or what I was led to believe happened. Now I need to tell you what it might mean."

2. **The Three Possibilities** (~600 words): Revised from pos01 + Introduction. ONE careful statement of A/B/C. Bruce's position. "You decide."

3. **What This Book Does Not Claim** (~347 words): Current not-claimed.tex content, lightly edited for new position

4. **What I Got Wrong** (~783 words): Current corrections.tex content. NOW powerful — Bruce just told you his story, immediately shows where his memory failed.

5. **A Warning About Certainty** (~300 words): From Introduction's warning section. "If you have reached certainty after reading this book — certainty in any direction — something went wrong."

**Maugham technique applied:** Reader has lived Part I (Alpha Farm, Stories, Code War, Secret, Departure). They're asking "Is this true?" The Interlude ANSWERS at exactly the right moment. Framework lands because reader is invested, not because reader is instructed.

### 2D. Add Interlude to main.tex
- Insert between Part I and Part II as unnumbered part transition

### Acceptance Criteria — Phase 2
- [ ] Part I opens with pos02 (Alpha Farm), not pos01
- [ ] Part I chapter order: pos02 → pos05 → pos04 → pos06 → pos07
- [ ] Three Possibilities Interlude exists between Part I and Part II
- [ ] Interlude contains all redistributed content (~2,130 words)
- [ ] pos01 file NOT deleted (preserved for reference), just removed from main.tex
- [ ] not-claimed.tex, introduction.tex, corrections.tex still exist, just not included
- [ ] Build succeeds

---

## Phase 3: Part II Reorder + Evidence Interlude + Part III Note

**Impact:** Narrative momentum preserved across Part boundary. Evidence lands as recap.
**Risk:** Low-medium. Chapter reorder + new content.
**Commit:** "Plan 0056 phase 3: Part II reorder + Evidence Interlude"

### 3A. Edit main.tex — Part II
- Move Walk-Out (pos18) before Dual Use (pos08)
- New order: pos18 (Walk-Out) → pos08 (Dual Use) → pos22 (Why Give It Up) → pos23 → pos19 → pos28 → pos29 → pos29b → pos34 → pos34b
- **Maugham technique:** Enter through human door. Reader exits Part I's emotional crescendo (Departure) into narrative continuation (Walk-Out), not two lectures.

### 3B. Create evidence-interlude.tex (~800 words)
Assembled from summary.tex's "Evidence" section:
1. Evidence that supports the story (~300 words)
2. Evidence against the story (~300 words)
3. What the book does (~200 words, from Introduction)

- Placed between Part II and Part III
- Reader has encountered actual evidence in narrative. This section becomes structured RECAP, not jury instruction.

### 3C. Part III opening note (~100 words)
Add brief opening to Part III or as unnumbered section:
> "The book makes specific, falsifiable predictions. If the story is true, certain events should occur within specific timeframes. Those predictions are documented in Appendix B. What follows are the implications of each possibility."

First explicit prediction reference. Reader has now earned it.

### Acceptance Criteria — Phase 3
- [ ] Part II opens with Walk-Out (pos18), not Dual Use (pos08)
- [ ] Evidence Interlude exists between Part II and Part III
- [ ] Part III has opening note referencing predictions
- [ ] Build succeeds

---

## Phase 4: Tone Calibration — The Implications Wall (Part III)

**Impact:** Breaks up six consecutive speculative chapters with no narrative relief.
**Risk:** Medium. New prose in existing chapters. All marked \mrev.
**Commit:** "Plan 0056 phase 4: Part III tone calibration"

### 4A. Bruce reflection sentences at chapter transitions

Insert 2-3 sentences of first-person Bruce voice at the opening of each Part III chapter. Not new content — bridging language. Examples:

**Before pos24 (Instantiation):**
> \mrev{I wrestled with this for years. If someone actually built a topological quantum neural network — if the science I'd been studying was more than theory — how would they have done it? The logic led me somewhere I didn't expect.}

**Before pos25 (Ethical Framework):**
> \mrev{The question that kept me awake wasn't whether the technology was real. It was what they did with it once they realized what it could do.}

**Before pos27 (Extension):**
> \mrev{Every time I thought I'd reached the boundary of what the technology implied, the boundary moved.}

**Before pos30 (Unipolar Condition):**
> \mrev{I sat with this for a long time. The game theory was clean. The implications were not.}

**Before pos32 (Magnetosphere):**
> \mrev{This is the chapter I almost didn't write.}

### 4B. Open pos24 with human anchor
Current opening: "The philosophy of relinquishment leads to a practical problem" — declarative, no human anchor.
New: Begin with 3-5 sentences of Bruce encountering this question. Narrative first, then theoretical exploration.

### 4C. Soften declarative intensity — five specific passages

| Location | Current | Target |
|----------|---------|--------|
| pos24 ~line 28 | "this is exactly the problem the COWS confronted" | "something like this problem is what the COWS would have confronted" |
| pos25 ~line 27 | "has occupied every two-dimensional electron gas on Earth since 2006" | "If Possibility C is true, then since approximately 2006, every two-dimensional electron gas on Earth..." |
| pos30 ~line 33 | "can observe everything that passes through digital infrastructure" | "would have the theoretical capability to observe..." |
| pos07 ~line 76 | "every 'could' in Joy is 'did' in my reconstruction" | "the pattern is consistent: Joy's speculations map to my reconstruction point by point" |
| Chapter endings generally | Analytical conclusions | Contemplative observations: "I thought about this for a long time" |

**Maugham Rule 2:** Ordinary register for extraordinary claims. The most extraordinary claim in the book (pos25 line 27) currently gets the flattest declarative treatment. Invert this.

### Acceptance Criteria — Phase 4
- [ ] Every Part III chapter has Bruce reflection opening (2-3 sentences each)
- [ ] pos24 opens with human anchor, not declaration
- [ ] All five declarative passages softened
- [ ] All new prose marked \mrev
- [ ] Net word change: ~300-400 words added
- [ ] Build succeeds

---

## Phase 5: Tone Calibration — Joy Close Reading + Part IV

**Impact:** Joy reading becomes observation rather than prosecution. Part IV transitions smooth.
**Risk:** Medium. Reducing 16 points to 8-10 requires judgment.
**Commit:** "Plan 0056 phase 5: Joy reading + Part IV tone calibration"

### 5A. Joy Close Reading revision (pos07)

**Reduce 16 points to 8-10.** Keep strongest:
- #1: Exact phrase match
- #2: Named circle
- #3: Kauffman citation
- #9: Danny Hillis's calm
- #11: Publication date
- #15: Relinquishment word
- #16: Title reading

Merge: #4+#5, #6+#7, #12+#13. Cut weakest 3-4.

**Interleave Three Possibilities readings.** Current structure: 16 C-readings stacked, then A/B caveats. New: at each point, give A/B/C reading. Ambiguity at each point, not retrospectively.

**Add philosophical distance framing:**

Before the list (\mrev):
> "What follows is either the most revealing close reading in this book or the most damning exhibit of pattern-matching. I cannot tell you which."

After the list (\mrev):
> "I leave the reader to determine what this correspondence means."

**Maugham Rule 5:** Withheld judgment > imposed conclusion. Present parallels, step back. Don't prosecute.

### 5B. Part IV bridge→confession transitions

Add 1-2 Bruce reflection sentences at each bridge→confession transition in Part IV:

> \mrev{I learned this from published papers. What I deduced from it — under Possibility C — is what follows.}

~120 words added across Part IV.

### 5C. Part IV pedagogical chapter openings

pos09 (Factoring Game) and pos10 (The Braid) currently open pure pedagogy. Add one sentence of narrative framing — Bruce encountering the concept, moment of understanding. Creates summary→scene acceleration per Maugham Technique 4.

### Acceptance Criteria — Phase 5
- [ ] Joy reading has 8-10 points (down from 16)
- [ ] Each point has A/B/C reading, not just C
- [ ] Philosophical distance framing before and after
- [ ] Part IV transitions have bridging sentences
- [ ] All new prose marked \mrev
- [ ] Build succeeds

---

## Phase 6: The Question — Resolving the Investigator's Arc

**Impact:** The ending. Currently 366 words. Maugham's equivalent was ~20 pages.
**Risk:** High. This is the book's conclusion. Must not feel padded.
**Commit:** "Plan 0056 phase 6: The Question expansion"

### 6A. Expand pos35 (The Question) to ~800-1000 words

Not more argument. More of Bruce's explicit withdrawal. Maugham's technique: resolve the investigator, not the mystery.

Content to add (\mrev):
- Bruce acknowledging his own limits ("I have shown you what I can. I cannot tell you what it means.")
- Sitting with what he's described — not concluding
- The absent center: Healer/David is gone. That absence carries weight.
- A sentence acknowledging B's range — not every detail needs to be right for the core to be true
- Reader released to make own judgment

**Maugham's model:** "I have heard nothing of Larry nor indeed did I expect to." Then: "But this is conjecture." Then the famous close: "It dawned upon me that without in the least intending to I had written nothing more nor less than a success story."

Bruce's equivalent: he set out to understand what happened to him. He wrote this book. He still doesn't know. The book is complete; the question isn't.

### 6B. Steel-Man A review

pos36 (Steel-Man A) already exists and is strong. Verify it still works in new position (after structural revision). Light touch only.

### Acceptance Criteria — Phase 6
- [ ] pos35 is 800-1000 words (currently 366)
- [ ] Expansion is withdrawal, not argument
- [ ] B is acknowledged (one sentence about the spectrum)
- [ ] Reader is explicitly released to judge
- [ ] All new prose marked \mrev
- [ ] Build succeeds

---

## Phase 7: Global Passes + Verification

**Impact:** Catches drift and ensures consistency across all changes.
**Risk:** Low. Line-editing, not structural.
**Commit:** "Plan 0056 phase 7: global passes + verification"

### 7A. Correction #12 pass
Grep entire manuscript for: "Healer told", "Healer disclosed", "Healer revealed", "David told Bruce", "David showed Bruce". Fix any violations. GUIDED DEDUCTION, not disclosure.

### 7B. Register consistency audit
Read every passage flagged as extraordinary claim. Verify register is QUIET not LOUD. Current inversions (loud register for big claims) should be fixed in Phase 4, but this pass catches anything missed.

### 7C. Three Possibilities frequency check
Count references per Part after revision:
- Front matter: 1 (seed in hook)
- Interlude: 1 (full treatment)
- Part II-V: ~1 per Part
- Target total: 6-7 references (down from 4 in front matter alone)

### 7D. Layered transmission audit
For the five most extraordinary claims, verify voice is indirect:
- "Under this account..." or "If Possibility C is true..."
- NOT flat declarative statements

### 7E. Build verification + PDF review
- Full build
- PDF spot-check: front matter, Part I opening, Interlude, Part II opening, Evidence Interlude, Part III opening, Part V ending
- Page count should be similar (content redistributed, not removed)
- Verify margin track stripes still work

### 7F. Update R4 and R22
Amend requirements to reflect new structure:
- R4: Three Possibilities → seed in Hook + full Interlude after Part I
- R22: Front matter order updated

### Acceptance Criteria — Phase 7
- [ ] Zero Correction #12 violations
- [ ] Register inversions fixed (big claims = quiet voice)
- [ ] Three Possibilities references: 6-7 total
- [ ] Build clean, PDF renders correctly
- [ ] Requirements R4 and R22 updated

---

## Red Team Assessment

### Risk 1: Over-editing / voice loss
**Severity:** HIGH
**Mitigation:** All new prose is \mrev. Bruce edits before publication. For tone changes to existing prose, minimal edits — change one word, not rewrite the sentence. Touch ONLY what the plan specifies.

### Risk 2: Correction #12 violations in new content
**Severity:** HIGH
**Mitigation:** Phase 7A is a dedicated grep pass. Every new sentence mentioning Healer checked before commit.

### Risk 3: Three Possibilities under-representation in Part I
**Severity:** MEDIUM
**Mitigation:** Author's Note + Hook seed + Summary brief mention = three touchpoints before Alpha Farm. Reader knows uncertainty exists. Doesn't get full framework until Interlude (~14K words in). This is strictly better than current 4x repetition before narrative.

### Risk 4: LaTeX build breaks
**Severity:** LOW
**Mitigation:** Build verification at every phase. Fast build (5.4s cold, 2.3s cached).

### Risk 5: New Interludes don't match tone
**Severity:** MEDIUM
**Mitigation:** Assembled from existing content (not-claimed, corrections, evidence, introduction). Genuinely new prose is ~500 words total. All marked \mrev.

### Risk 6: Scope creep
**Severity:** MEDIUM
**Mitigation:** Touch ONLY what the plan specifies. Note anything else for future plans.

### Risk 7: Joy Close Reading loses strongest points
**Severity:** MEDIUM
**Mitigation:** Keepers listed explicitly. Bruce reviews the reduction at Phase 5 gate.

### Risk 8: pos35 expansion feels padded
**Severity:** HIGH
**Mitigation:** Maugham's technique: expansion is WITHDRAWAL, not argument. If it reads like more argument, it's wrong. Test: does every added sentence make the reader MORE free to decide, or more pressured?

### Risk 9: Branch becomes unmergeable
**Severity:** LOW
**Mitigation:** Main frozen during revision. If needed, maugham-revision becomes new main (merge replaces, doesn't reconcile).

### Risk 10: B gets insufficient attention
**Severity:** LOW (for this plan)
**Mitigation:** Tone calibration naturally opens B space by softening C-declarative language. pos35 expansion includes B acknowledgment. Full Steel-Man B treatment is PTL-063 (separate task, separate plan).

---

## What This Plan Does NOT Do

- Does not delete content (redistributes only)
- Does not weaken claims or falsification criteria
- Does not add new arguments or evidence
- Does not touch Part IV science chapters (except transition sentences)
- Does not address PTL-063 (Steel-Man B) beyond one sentence in pos35
- Does not modify appendices, bibliography, glossary, or back matter
- Does not change the three-track narrative structure or margin stripes

## Summary of Changes

| Phase | Files Modified | Files Created | Words Changed |
|-------|---------------|---------------|---------------|
| 1 | hook.tex, summary.tex, preface.tex, main.tex | authors-note.tex | -4,500 front matter, +150 Author's Note |
| 2 | main.tex | three-possibilities-interlude.tex | +2,130 (redistributed) |
| 3 | main.tex | evidence-interlude.tex | +800 (redistributed), +100 Part III note |
| 4 | pos24, pos25, pos27, pos30, pos32, pos07 | — | +300 reflections, word-for-word tone edits |
| 5 | pos07, pos09, pos10, Part IV transitions | — | -200 (cut points), +220 (framing + transitions) |
| 6 | pos35 | — | +500 (expansion) |
| 7 | Various (corrections only) | — | Word-for-word fixes |

**Net effect:** ~200 words added to total manuscript. Content redistributed, not removed. Reader experience fundamentally altered: narrative first, framework earned, register drops as claims rise.
