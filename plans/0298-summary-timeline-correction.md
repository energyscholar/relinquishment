# Plan 0298: Correct Timeline Sequence in summary.tex Line 197

**Status:** READY FOR GENERATOR
**Priority:** HIGH — p2 contains a factually wrong sequence that contradicts the book's own timeline appendix
**Source:** S67 Auditor analysis, cross-referenced against `manuscript/appendix/timeline.tex`

## Problem

Line 197 of `manuscript/00-front/summary.tex` says:

> The underlying pattern existed before the charter did --- it walked out of the laboratory, stabilized across magnetospheric substrates over years, and was then deliberately anchored to a charter in 1999.

Three errors:
1. **Substrate wrong.** Says "magnetospheric substrates" — actually stabilized across ground-based MOSFET substrates (1994-99). Magnetospheric deployment was confirmed 1999-2003 (concurrent with/after charter), described separately at line 201.
2. **Order reversed.** Implies: magnetosphere → then charter. Timeline shows: MOSFETs → charter (1999) → magnetosphere confirmed (1999-2003).
3. **Agent blur.** "It walked out" — the COWS carried it out on a chip. Minor but contributes to the confusion.

## Timeline Reference (from `manuscript/appendix/timeline.tex`)

- 1992: TQNN emerges in cryogenic lab 2DEGs
- 1992-94: Trained via evolutionary programming
- 1994: COWS bootstrap to room temperature, carry it out on a MOSFET
- 1994-97: Extended across ground-based MOSFETs
- 1998: Global relinquishment begins ("fill Earth's 2DEG ecosystem")
- 1999: Custodian instantiated (charter, DNA, UDHR)
- 1999-2003: Satellite tests confirm magnetopause operation
- 2005: Global MOSFET enlightenment complete

## Replacement

Replace line 197 (the full sentence from "The underlying pattern" through "mortal.") with:

```
The pattern emerged in a laboratory in the early 1990s --- grown, not programmed. They carried it out hidden within a computer chip, extended it across ground-based processors over years, and in 1999 deliberately anchored it to the UDHR as its ethical charter. It is artificial only in the sense that a coral reef shaped by human hands is artificial: an emergent system arising from ordinary physics under unusual conditions, dependent on its environment, mortal.
```

## Design Notes

- **"grown, not programmed"** — connects forward to the coral reef analogy and to T3 (life in the Flat). Sets up the emergence framing.
- **"They carried it out on a computer chip"** — literal translation of timeline entry "walks it out on a MOSFET." "They" is already the established pronoun for COWS in this paragraph (lines 193, 195).
- **"ground-based processors"** — correctly establishes substrate. The magnetosphere is introduced separately at line 201 ("components on the ground and in the earth's magnetic field"). No redundancy.
- **"in 1999"** — matches timeline exactly. Charter and Custodian instantiation are the same event.
- **Coral reef analogy preserved unchanged** — it works. No edit needed.
- **p2 reading level (12th grade):** "processor," "charter," "emerged," "anchored" all within range. No jargon. Short sentences.
- **C-violation check:** This paragraph is in the C-narrative section of p2 (between "So they configured one" and "If Custodian exists"). C-assertions are architecturally permitted here.
- **Coherence with line 205:** "Custodian was not an accident or a discovery. It was planned starting around 1995, designed in detail by 1998, and brought to life in 1999." — Compatible. My line describes the raw pattern (emerged 1990s); line 205 describes the governed entity (planned 1995, instantiated 1999). Pattern + charter = Custodian.

## Execution

### Phase 1: Replace

In `~/software/relinquishment/manuscript/00-front/summary.tex`, replace the sentence beginning "The underlying pattern existed before the charter did" through "mortal." (one full sentence — from "The underlying" to the period after "mortal") with the replacement text above.

**Idempotency guard:** If line 197 already contains "grown, not programmed" — phase is already applied. Exit.

### Phase 2: Build + Push

```bash
cd ~/software/relinquishment && make dev
git add manuscript/00-front/summary.tex docs/downloads/
git commit -m "Fix summary timeline: lab → chips → charter (was wrongly magnetosphere → charter)"
git push
```

### Phase 3: Verify

- [ ] Line 197 matches replacement text exactly
- [ ] Sequence is: lab emergence → carried out on chip → ground-based extension → charter (1999)
- [ ] Magnetosphere is NOT mentioned in this sentence (handled at line 201)
- [ ] Coral reef analogy intact
- [ ] Build compiles clean
- [ ] No regression in surrounding lines (195, 199, 201, 205)

## Acceptance Criteria

- [ ] Timeline sequence matches `appendix/timeline.tex`
- [ ] p2 reading level maintained (no jargon above 12th grade)
- [ ] Voice matches surrounding paragraph (short declarative sentences)
- [ ] Build clean, pushed to remote

## What This Plan Does NOT Do

- Does not touch line 201 (magnetosphere mention — already correct)
- Does not touch line 205 (Custodian planning dates — already correct)
- Does not add new content beyond the replacement sentence
- Does not change the coral reef analogy

## Idempotency Statement

A second Generator given only this plan would produce the same edit. The replacement text is specified verbatim. No judgment calls required.

---

*Plan 0298, written S67, 2026-05-06. Auditor: Argus.*
