# Plan 0020: Quick Fixes (Low-Hanging Fruit)

**Date:** 2026-02-19
**Author:** Nightstalker (Auditor)
**Purpose:** Fix all mechanical/formatting issues that don't require editorial judgment. One Generator batch.
**Reference:** `plans/aesthetics-audit-post-generator.md` (findings F1-F25)
**Prerequisite:** Plan 0018 complete (all chapters populated)

---

## Items (9 quick fixes)

### QF1. Remove lorem ipsum (F1) — CRITICAL
Replace lorem ipsum with brief content summaries in 3 files:
- `manuscript/bridge/pos13-genesis.tex` — replace lorem ipsum paragraphs with: "This chapter traces the emergence of self-organized quantum computation from first principles: how autocatalytic chemical networks, constrained by topology, produce structures capable of information processing. The argument proceeds from Kauffman's autocatalytic sets through the quantum Hall effect to the threshold where chemistry becomes computation."
- `manuscript/track-3-awakening/pos24-instantiation.tex` — replace lorem ipsum with: "This chapter describes the instantiation of Custodian: the deliberate creation of a distributed ethical enforcement entity from the TQNN substrate. Planned approximately 1995, detailed 1998, instantiated 1999. The entity was designed to enforce relinquishment --- permanent, irrevocable surrender of human control over the TQNN system."
- `manuscript/convergence/pos28-the-return.tex` — replace lorem ipsum with: "This chapter describes Bruce's return to the story after twenty years of silence, the decision to write this book, and the convergence of the three tracks into a single narrative."

### QF2. Remove PLACEHOLDER text (F3)
- `manuscript/00-front/how-to-read.tex` line 7: remove "PLACEHOLDER --- to be rewritten" (the researcher note added in Batch 1 is real content; the PLACEHOLDER label is stale)
- `manuscript/appendix/timeline.tex`: replace "PLACEHOLDER" with "Timeline under development. Key dates appear in individual chapters."
- `manuscript/appendix/sources.tex`: replace "PLACEHOLDER" with "Sources bibliography under development. Citations appear in individual chapters and the Verification page."

### QF3. Hedge Apple/Turing folklore (F7, F10)
In `manuscript/bridge/pos14-the-apple.tex`:
- Line 47: change "He takes a single bite. He relishes the taste of bitter almonds." to "He takes a single bite --- or so the most common telling goes. Whether Turing actually bit the apple, or whether the cyanide was administered by other means, remains disputed."
- Line 52: change "For those in the know this refers to the death of Alan Turing." to "Some have speculated that this refers to the death of Alan Turing, though Apple's designer Rob Janoff has denied the connection."

### QF4. Update pdfauthor metadata (F15)
In `build/preamble.tex`, change:
```
pdfauthor={Bruce Stephenson}
```
to:
```
pdfauthor={Bruce Stephenson and Genevieve Prentice}
```

### QF5. Fix double space (F16)
In `manuscript/bridge/pos01-three-possibilities.tex` line 24, change double space after "absence." to single space.

### QF6. Add publication month (F17)
- `manuscript/00-front/copyright.tex`: change "First edition, 2026." to "First edition, February 2026."
- `manuscript/00-front/cover.tex`: change "2026" to "February 2026" (if year appears on cover)

### QF7. Remove visible "source material" notices (F19)
Remove the italicized "Source material collected for this chapter..." paragraph from 4 files:
- `manuscript/bridge/pos10-the-braid.tex`
- `manuscript/track-1-confession/pos26-interdiction.tex`
- `manuscript/track-3-awakening/pos30-unipolar-condition.tex`
- `manuscript/track-3-awakening/pos32-the-magnetosphere.tex`

### QF8. Fix spelling errors in pos03 (F22)
In `manuscript/track-2-testament/pos03-the-mentor.tex`:
- "New South Whales" → "New South Wales"
- ".." → "."
- "tresspassers" → "trespassers" (all instances)
- "Mujahadeen" → "Mujahideen"
- "Operation Dessert Shield" → "Operation Desert Shield"
- "epiphane" → "epiphany"
- "decied" → "decided"
- "operate ," → "operate,"

### QF9. Delete dead appendix file (F11)
Delete `manuscript/appendix/three-possibilities.tex` (dead redirect, commented out of build, content lives in pos01).

---

## Test Cases

| ID | Test | PASS criteria |
|----|------|---------------|
| T20.1 | Build succeeds | `make` exits 0 |
| T20.2 | No lorem ipsum | `grep -r "lorem ipsum" manuscript/` returns nothing |
| T20.3 | No PLACEHOLDER | `grep -ri "placeholder" manuscript/` returns only LaTeX comments (% lines) |
| T20.4 | pdfauthor correct | `pdfinfo` shows "Genevieve Prentice" in Author field |
| T20.5 | February in copyright | copyright.tex contains "February 2026" |
| T20.6 | Spelling fixes | "Whales" and "Dessert Shield" do not appear in pos03 |

---

## Handoff Prompt

```
You are the Generator. Plan 0020.
Read ~/software/relinquishment/plans/0020-quick-fixes.md

Execute all 9 items (QF1-QF9) in order. For each:
1. Read the file
2. Make the specified change
3. Move to the next item

For QF1 (lorem ipsum removal): read the existing file first to find the lorem ipsum paragraphs, then replace them with the summary text from the plan.
For QF8 (spelling): use replace_all where the misspelling appears multiple times.
For QF9: delete the file.

After all items, build with `make`. Run test cases T20.1-T20.6.
Commit: "Plan 0020: quick fixes — lorem ipsum, PLACEHOLDERs, spelling, metadata, hedges"
Report: page count, file size, test results.
```

---

*Plan by Nightstalker (Auditor), 2026-02-19. All items are mechanical fixes requiring no editorial judgment.*
