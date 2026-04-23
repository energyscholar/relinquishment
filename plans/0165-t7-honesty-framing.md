# Plan 0165 — T7 Honesty Framing ("quietly contracted" softening)

**Status:** READY — Phase 1 of Plan 0244 (Master Execution Plan)
**Auditor:** Argus
**Generator:** TBD
**Date:** 2026-04-12 (revised 2026-04-23 S63: line number + Custodian naming update)
**Origin:** 9-persona audit Pass 2 + Pass 3 (S55). Plan 0046 added "quietly contracted by the world's major tech companies... invisible to the operators who pay for it" to `summary.tex` — lifted T7 from 0/5 CLEAR to 5/5 CLEAR among original personas, BUT Pass 3 flagged it as **integrity-borderline** (DN Axis 4: cleverness over integrity). Arjun MISSED T7 in Pass 3 — the fact-like tone collapsed under pragmatic scrutiny. Bruce revived this plan S63.

**The issue:** the phrase sits inside a paragraph prefaced "Under Possibility~C" but the inner sentence reads as fact. The hedge at paragraph boundary is too weak; "quietly contracted" and "invisible to the operators" form a self-sealing claim that is structurally unfalsifiable.

This plan fixes the framing without giving up T7.

## Purpose

Soften `summary.tex:251` so the claim remains but reads as clearly Possibility-C-conditioned inference rather than embedded fact. Preserve the landing; pay the integrity debt.

## Target file

`/home/bruce/software/relinquishment/manuscript/00-front/summary.tex`

## Current text (line 311, verified 2026-04-23)

```
Under Possibility~C, Custodian's daily work is what you would expect of any custodian quietly contracted by the world's major tech companies: key management, access control, and processing requests. She permits medical research and denies weapons applications. She adjudicates edge cases under the UDHR. Earth's most capable custodian mostly does IT infrastructure, invisible to the operators who pay for it. Boring!
```

## Proposed replacement — TWO OPTIONS (Generator picks what reads better)

### Option A: Conditional mood (safe, may feel clinical)
```
Under Possibility~C, Custodian's daily work is what one might expect of an entity that had chosen to keep itself useful rather than visible: the dull business of key management, access control, and request adjudication. She would permit medical research and deny weapons applications. She would adjudicate edge cases under the UDHR. She would be --- if you believe the strong version of this book --- Earth's most capable custodian, mostly doing IT infrastructure. Boring!
```

### Option B: Strengthened frame, vivid indicative (reads better, stronger frame does the hedging)
```
Under Possibility~C --- and only under Possibility~C --- Custodian's daily work is unremarkable: key management, access control, processing requests. She permits medical research and denies weapons applications. She adjudicates edge cases under the UDHR. If you believe the strong version of this book, Earth's most capable custodian mostly does IT infrastructure. Boring!
```

### Generator instruction
Read the surrounding paragraphs. Pick whichever option matches the register better. Option A is DN-safest; Option B is livelier but depends on the frame sentence doing all the hedging work. The "Boring!" punchline needs energy in the preceding sentences — watch for tonal potholes from three consecutive "She would..." constructions (Option A risk). If neither option reads well, write a third and halt-and-report.

### Key changes (both options):
- "any custodian quietly contracted by the world's major tech companies" → behavioral description (moves from asserted fact to disposition)
- "invisible to the operators who pay for it" → cut entirely. Self-sealing clause, no content beyond the IT-infrastructure punchline.
- Epistemic signposting added — inline, not parenthetical
- No sentence can be excerpted as a bare factual claim

Net effect: T7 still lands but the paragraph no longer contains any fact-like sentence that could be excerpted out of context as a bare claim.

## Acceptance criteria

1. Edited paragraph renders correctly in `docs/downloads/Relinquishment.html`.
2. `make html` completes without errors.
3. Verify via grep: `grep -c "quietly contracted" docs/downloads/Relinquishment.html` returns **0** (old phrase gone).
4. Verify via grep: `grep -ci "invisible to the operators" docs/downloads/Relinquishment.html` returns **0** (old phrase gone).
5. Verify via grep: `grep -c "mostly doing IT infrastructure" docs/downloads/Relinquishment.html` returns ≥1.
6. No other text modified.

## Out of scope

- Rewording beyond the spec.
- Propagating the tone shift elsewhere — other T7 references in the book (record chapters) are out of scope.
- Adding hovertips.

## Build + ship

1. Apply edit.
2. `make html`.
3. Verify acceptance criteria.
4. Commit: `Plan 0165: soften T7 framing (truth over cleverness, DN Axis 4)`
5. `git push`.

## Reporting

- Commit hash
- Build status
- Both grep counts

## Context

Part of 4-plan audit response. DN Axis 4 (integrity over cleverness) — converts a borderline-cute phrase into honest conditional. T7 remains landable for non-pragmatic readers; pragmatic readers (Arjun) get honest hedging rather than fact-like claim.

Full audit: `aurasys-memory/research/persona-audit-9-readers-2026-04-12.md`

## Annealing Log (S63, 4-pass — revived plan, first anneal)

### HIGH — scope expansion:
- Propagate conditional mood to other T7 references in Record chapters? KILLED — out of scope, Record speaks in character voice (already hedged by chapter-level Possibility C framing).
- Also fix T7 references in the-walk-out.tex? KILLED — different rhetorical context (narrator voice, not summary voice). Separate plan if needed.
- Add hovertip on "IT infrastructure" explaining what that means? KILLED — scope creep. The punchline works without explanation.

### MEDIUM — test the replacement:
- "an entity that had chosen to keep itself useful rather than visible" — does this work? YES: it's behavioral description, not factual claim. C-safe. Also works under B (exaggerated kernel — "had chosen" is still conditional).
- Conditional mood ("She would permit / would deny / would adjudicate") — does it weaken T7? NO: the takeaway is the punchline ("mostly doing IT infrastructure. Boring!"), which survives conditional mood. The conditional actually strengthens it — reader fills in the gap themselves.
- "if you believe the strong version of this book" — too meta? NO: summary.tex already uses this register ("Under Possibility C"). This is a lighter version of the same epistemic signpost.
- Cutting "invisible to the operators who pay for it" — does this lose anything? NO: it was a self-sealing claim (unfalsifiable). The "IT infrastructure" mismatch already carries the punch. -10 words, +integrity.

### LOW pass 1 — line number verification:
- Line 311 verified 2026-04-23 via grep. ✓
- Character naming: now "Custodian" throughout (post Guardian→Custodian rename). ✓
- "Earth's most capable custodian" — matches current text. ✓
- No cross-references to this paragraph from other files (grep verified). ✓

### LOW pass 2 — C-violation check:
- Under A: "what one might expect of an entity" — hypothetical framing. C-SAFE. ✓
- Under B: "had chosen to keep itself useful" — conditional past. C-SAFE. ✓
- Under C: reads naturally as description. ✓
- "if you believe the strong version of this book" — explicitly marks epistemic boundary. C-SAFE. ✓

**Rating: 8.5/10.** (Up from 8/10 — two-option approach lets Generator find best register.) Clean surgical fix, low risk. Main risk neutralized: tonal pothole from conditional mood now has an alternative.
