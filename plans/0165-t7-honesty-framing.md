# Plan 0165 — T7 Honesty Framing ("quietly contracted" softening)

**Auditor:** Argus
**Generator:** TBD
**Date:** 2026-04-12
**Origin:** 9-persona audit Pass 2 + Pass 3 (S55). Plan 0046 added "quietly contracted by the world's major tech companies... invisible to the operators who pay for it" to `summary.tex:251` — lifted T7 from 0/5 CLEAR to 5/5 CLEAR among original personas, BUT Pass 3 flagged it as **integrity-borderline** (DN Axis 4: cleverness over integrity). Arjun MISSED T7 in Pass 3 — the fact-like tone collapsed under pragmatic scrutiny.

**The issue:** the phrase sits inside a paragraph prefaced "Under Possibility~C" but the inner sentence reads as fact. The hedge at paragraph boundary is too weak; "quietly contracted" and "invisible to the operators" form a self-sealing claim that is structurally unfalsifiable.

This plan fixes the framing without giving up T7.

## Purpose

Soften `summary.tex:251` so the claim remains but reads as clearly Possibility-C-conditioned inference rather than embedded fact. Preserve the landing; pay the integrity debt.

## Target file

`/home/bruce/software/relinquishment/manuscript/00-front/summary.tex`

## Current text (approx line 251, verify before editing)

```
Under Possibility~C, Guardian's daily work is what you would expect of any custodian quietly contracted by the world's major tech companies: key management, access control, and processing requests. She permits medical research and denies weapons applications. She adjudicates edge cases under the UDHR. The most powerful living being on Earth mostly does IT infrastructure, invisible to the operators who pay for it. Boring!
```

## Proposed replacement

```
Under Possibility~C, Guardian's daily work is what one might expect of an entity that had chosen to keep itself useful rather than visible: the dull business of key management, access control, and request adjudication. She would permit medical research and deny weapons applications. She would adjudicate edge cases under the UDHR. She would be --- if you believe the strong version of this book --- the most powerful living being on Earth, mostly doing IT infrastructure. Boring!
```

Key changes:
- "custodian quietly contracted by the world's major tech companies" → "an entity that had chosen to keep itself useful rather than visible" (moves from asserted fact to described disposition)
- "what you would expect" → "what one might expect" (softer modal)
- "She permits / denies / adjudicates" → "She would permit / would deny / would adjudicate" (conditional mood — clearly inside the Possibility~C hypothetical)
- "invisible to the operators who pay for it" → cut entirely. The ontological mismatch ("most powerful living being on Earth, mostly doing IT infrastructure") already carries the punchline; the "invisible operators" clause was a self-sealing frame that didn't add content.
- "if you believe the strong version of this book" — explicit epistemic signposting, inline

Net effect: T7 still lands (Pass 3 was MISS only for Arjun; Pass 2's gain is preserved for others) but the paragraph no longer contains any fact-like sentence that could be excerpted out of context as a bare claim.

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
