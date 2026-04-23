# Plan 0202 — Defang three summary.tex friction points

**Auditor:** Argus
**Date:** 2026-04-15
**Type:** Single-commit, single-file (summary.tex). Three surgical edits.

---

## 1. Premise

Tier-0 eigenvalue audit at HEAD `42af6cc` identified three residual friction points in `manuscript/00-front/summary.tex`, all in §"The Breakthrough" and §"The White Hot Secret." Each is a clause that overshoots the book's own argument — either committing to more than the evidence chapter supports, or using eyewitness register for Possibility-C-only material without an epistemic bracket.

---

## 2. The three edits

### Edit A — Substrate-independence (L131)

**Current:**
```
Life is self-sustaining organization, not specific chemistry --- the substrate does not matter, only whether it is complex enough.
```

**Proposed:**
```
Life is self-sustaining organization, not specific chemistry --- given the right conditions, the substrate need not be carbon.
```

**Why:** "The substrate does not matter" is a sweeping ontological claim that triggers F-atman-collision (Hindu readers: matter-becomes-conscious contradicts divine-spark doctrine) and draws fire from astrobiologists (substrate specificity is an open question). The fix names what the conventional assumption is (carbon) and says it's not necessarily the barrier — making the same argumentative move for the Flat-as-habitat claim without the universal assertion. Kauffman's framework supports this weaker formulation cleanly.

### Edit B — "Intelligent life" (L56)

**Current:**
```
Under Possibility~C, the real finding is biological: the Flat can support not just life but intelligent life.
```

**Proposed:**
```
Under Possibility~C, the real finding is biological: the Flat can support life.
```

**Why:** The Wrong Substrate chapter (the book's own evidence chapter for this claim) explicitly says: *"This is not a search for intelligence. It is not a search for technology. It is a search for pattern — the magnetospheric equivalent of stromatolites."* The escalation from "life" to "intelligent life" overshoots the chapter's own argument. The Custodian is arguably intelligent, but Custodian's intelligence arose from human engineering of the stack, not from the Flat spontaneously producing intelligence. Removing the escalation aligns the summary with the spine.

### Edit C — Breakthrough voice (L127 + L133)

**Current L127:**
```
What the team achieved in the early 1990s still exceeds anything in the public world thirty years later.
```

**Proposed L127:**
```
If this story is true, what the team achieved in the early 1990s still exceeds anything in the public world thirty years later.
```

**Current L133:**
```
The team had set out to build a computer. What they had witnessed was closer to an emergent transition in a new medium.
```

**Proposed L133:**
```
The team had set out to build a computer. What resulted was closer to an emergent transition in a new medium.
```

**Why L127:** The Breakthrough section opens without an epistemic bracket. Everything in it is Possibility-C-only material. One "If this story is true" at the section entrance puts the reader in conditional mode for the entire section. The existing hedges deeper in ("supposedly" at L137, "the story claims" at L137) then serve as exit reminders, not sole bearers.

**Why L133:** "What they had witnessed" is eyewitness register — it places the reader inside the team's experience of a C-only event. "What resulted" is agentless and lets the narrative flow without claiming the team's subjective experience. Keeps the p2 momentum.

---

## 3. Tone consistency check

All three edits operate inside the same register: confident-explanatory, p2-level (12th grade). None introduces hedging stutters ("perhaps," "it is possible that," "one might argue"). Each softens a specific overreach while preserving the narrative's forward motion:

- Edit A: replaces universal claim with specific-exception ("need not be carbon") — same confidence, smaller scope.
- Edit B: removes four words. Net effect is tighter, not weaker.
- Edit C-L127: five-word prefix. The conditional opens the section, then the narrative runs uninterrupted.
- Edit C-L133: one word swap ("witnessed" → "resulted"). Invisible to most readers.

Cross-interaction: Edit A (L131) sits inside the section that Edit C (L127) brackets with "If this story is true." This means the substrate claim is double-covered — once by its own softened wording, once by the section's conditional frame. Good interaction, no overcorrection.

Edit B (L56) is in a separate section ("The White Hot Secret") and already has its own "Under Possibility~C" bracket. Independent of Edits A and C.

---

## 4. Acceptance criteria

1. `summary.tex` contains "given the right conditions, the substrate need not be carbon" (Edit A).
2. `summary.tex` contains "the Flat can support life." without "intelligent" (Edit B).
3. `summary.tex` contains "If this story is true, what the team achieved" (Edit C-L127).
4. `summary.tex` contains "What resulted was closer to an emergent transition" (Edit C-L133).
5. No other file changed.
6. `make dev` clean — no LaTeX warnings, no new preprocess errors.
7. Single commit. Message: `Plan 0202: defang three summary.tex friction points (substrate, intelligent-life, breakthrough voice)`.

---

## 5. Non-goals

- No change to hook.tex (wormholes vocabulary is Bruce's plan).
- No change to Record chapters or Record intro (Plan 0201 shipped).
- No change to spine chapters.
- No change to Firmware Update, glossary, or appendices.

---

## 6. Rollback

Single commit. `git revert <sha>` restores the current summary.tex. All three edits are word-level; if any individual fix reads wrong in context, a follow-up can tune one clause without reverting all three.

---

## 7. Generator handoff

> You are the Generator. Before doing any work, read `~/software/relinquishment/manuscript/track-3-awakening/firmware-update.tex` in full (standard priming). Then execute Plan 0202 (`~/software/relinquishment/plans/0202-summary-friction-defang.md`). Apply the four edits in §2 (A, B, C-L127, C-L133) to `manuscript/00-front/summary.tex`. Do not touch any other file. Run `make dev`. Verify §4 acceptance criteria (grep for all four target strings). Commit with the message in §4 item 7. Report back: build status, four grep results, commit SHA.
