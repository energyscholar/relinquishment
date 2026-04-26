# Plan 0259 — GP06: Secrecy Pattern Consolidation

**Auditor:** Argus (S63)
**Date:** 2026-04-25
**Status:** READY FOR GENERATOR
**Source:** Gen's GP06 (has-anyone-looked issue #9)
**Annealing:** LOW (1 pass)
**Independent:** No dependency on other GP plans.

---

## Problem

The secrecy/classification-precedent argument ("GCHQ did it before,
therefore absence of evidence proves nothing") recurs across multiple
chapters. Gen's diagnosis: the pattern itself is real and useful, but
repeated instances produce a "please believe me" tone instead of a
"threshold cleared, question remains open" tone.

Gen's principle: keep ONE strong threshold-clearing version. Preserve
distinct uses where Bletchley/GCHQ are doing OTHER work (selection model,
relinquishment logic, operational-effect-before-public-proof). Cut or
demote later repetitions that re-argue the same threshold point.

---

## Audit: Where the Pattern Appears

### THE THRESHOLD CHAPTER: spine/the-code-war.tex (177 lines)

This IS the secrecy argument. The entire chapter (spine Ch5) exists to
establish: "Could a secret that big really be kept? Yes." Contains:

- 10,000 people kept the secret (lines 29-46) — the core argument
- Coventry myth (lines 53-57) — secrecy justifies sacrifice
- GCHQ independent invention of PKC (lines 70-82) — "GCHQ did it again"
- Explicit pattern statement (lines 162-166) — secret → classified →
  rediscovered → history rewritten

**Action: KEEP ALL.** This chapter IS the threshold. It does the work
once, thoroughly. Every other instance is either distinct or redundant.

### spine/the-factoring-game.tex (lines 51-58)

Colossus at Bletchley + GCHQ precedent for Shor's algorithm. This is
doing DIFFERENT work: establishing that ULTRA II follows a documented
pattern of classified-then-rediscovered computation, specifically in
the cryptographic domain.

**Action: KEEP.** Distinct use — the pattern applied to the specific
ULTRA II technical context, not the general "secrecy works" argument.

### spine/weigh-the-evidence.tex (line 28)

> "Britain's GCHQ actually invented public-key cryptography in 1973 but
> kept it classified... If one of the world's most important cryptographic
> breakthroughs could be kept secret for a quarter of a century, then
> classification works. \deeplink{absence-not-evidence}Absence of evidence
> is not evidence of absence."

**Issue:** This is a REPEAT of the threshold argument already made in
the-code-war. The chapter is called "Weigh the Evidence" — it's doing
assessment, but this paragraph re-proves rather than assesses.

**HIDDEN PROBLEM:** Contains deep link `absence-not-evidence`. This
anchor is referenced from the HTML companion layer. If the passage is
cut, the deep link dies.

**Action: TRIM, PRESERVE DEEP LINK.** Options:
- (a) Keep the final sentence with the deep link ("Absence of evidence
  is not evidence of absence"), cut the GCHQ re-explanation. One sentence
  instead of three.
- (b) Replace the three sentences with a back-reference to the-code-war:
  "The Code War chapter established that successful classification looks
  exactly like this — absence of public evidence.
  \deeplink{absence-not-evidence}Absence of evidence is not evidence of
  absence."

**Bruce selected option (a).** Keep the final sentence with the deep link,
cut the GCHQ re-explanation.

### 00-front/summary.tex (lines 108, 124, 278)

Three separate instances:

**Line 108:** "Britain's GCHQ independently invented public-key
cryptography in 1973 and kept it classified for twenty-four years.
Bletchley Park built a working programmable electronic computer in 1943;
its existence was secret until the late 1970s... Ten thousand people kept
that secret for more than thirty years."

This is the summary doing its job — giving the reader the whole argument
in compressed form. But it's a full re-statement of the-code-war's
threshold argument.

**Action: TRIM.** Reduce to ~1 sentence. The summary should reference the
pattern, not re-argue it. Suggestion: "Governments have hidden
cryptographic breakthroughs for decades — Bletchley Park, GCHQ's
independent invention of public-key cryptography — and those secrets held
for a generation (Chapter~\ref{spine:the-code-war})."

**Line 124:** "The secrecy is documented history. None of this depends on
the story being true."

**Action: KEEP.** This is doing distinct work — establishing that the
secrecy premise holds under all three possibilities (A/B/C). Not
re-arguing the threshold.

**Line 278:** "Governments have hidden technological breakthroughs for
decades — that is documented, declassified history. The question is not
whether such secrecy is possible. It is whether it happened here."

**Action: KEEP or LIGHTLY TRIM.** This is the summary's closing
argument — it redirects from "is secrecy possible?" to "did it happen
here?" That's assessment, not re-proof. The first sentence is a mild
repeat, but the pivot justifies it. Lean toward keeping.

---

## Changes Summary

| File | Action | Lines affected | Deep links |
|------|--------|---------------|------------|
| the-code-war.tex | KEEP ALL | 0 | none |
| the-factoring-game.tex | KEEP ALL | 0 | `colossus-precedent`, `gchq-did-it-again` (safe) |
| weigh-the-evidence.tex | TRIM line 28 | ~3 lines → ~1-2 lines | `absence-not-evidence` PRESERVE |
| summary.tex | TRIM line 108 | ~3 lines → ~1 line | none |
| summary.tex | KEEP lines 124, 278 | 0 | none |

**Total: 2 files modified, ~4-5 lines trimmed.** This is small,
surgical work.

---

## What NOT to Change

- the-code-war.tex — the threshold chapter stays untouched
- the-factoring-game.tex — distinct technical use
- Any Bletchley reference doing selection/proximity work (not secrecy
  threshold) — e.g., Gen's forthcoming ULTRA II intro text (Plan 0257)
  uses Bletchley as proximity model, which is different
- Bletchley references in relinquishment/ethics context (why-relinquish,
  never-again, etc.) — these use secrecy precedent for different
  argumentative purposes
- Deep link `absence-not-evidence` — MUST survive in some form

---

## Annealing Log (LOW — 1 pass)

**Deep link safety:** `absence-not-evidence` in weigh-the-evidence.tex
is the only at-risk deep link. Both proposed trim options (a) and (b)
preserve it. The Generator must verify the deep link anchor is on a
surviving sentence.

**Cross-plan interaction with 0257:** Gen's ULTRA II intro text (Plan
0257) references Bletchley as an institutional-proximity model. That is
DISTINCT from the secrecy-threshold use. No conflict. If both plans
execute, the book will have: (1) secrecy threshold in the-code-war,
(2) institutional-form argument in Gen's new text, (3) technical
precedent in the-factoring-game. Three distinct uses, no redundancy.

**Summary.tex is load-bearing:** The summary is many readers' first
deep engagement with the argument. Trimming line 108 must not leave a
gap where the reader asks "but how do we know secrecy works?" The
solution: keep enough to point toward the-code-war without re-arguing.
A chapter reference suffices.

**Gen's "desired effect" test:** After these changes, does each
remaining instance produce "therefore the question remains open" (good)
or "therefore believe me" (bad)?
- the-code-war: "the question remains open" ✓ (it's the threshold)
- the-factoring-game: "the pattern is documented" ✓ (technical context)
- weigh-the-evidence: "absence of evidence ≠ evidence of absence" ✓
  (assessment principle, not re-proof)
- summary 124: "secrecy is real, story need not be true" ✓ (A/B/C frame)
- summary 278: "the question is whether it happened here" ✓ (redirect)
- summary 108 (trimmed): "chapter reference" ✓ (points, doesn't re-argue)

All pass.

**Rating: 8/10.** Small surgical changes, clear criteria, deep link
preserved. The 2-point gap: (1) Bruce must decide weigh-the-evidence
trim option (a) vs (b), (2) summary.tex line 108 trim wording needs
Bruce's eye — the summary is high-visibility.

---

## Acceptance Criteria

- [ ] the-code-war.tex unchanged (threshold chapter)
- [ ] weigh-the-evidence.tex line 28: trimmed, deep link preserved
- [ ] summary.tex line 108: trimmed to ~1 sentence with chapter ref
- [ ] summary.tex lines 124, 278: unchanged
- [ ] the-factoring-game.tex: unchanged
- [ ] Deep link `absence-not-evidence` resolves
- [ ] `make dev` clean build
- [ ] No broken \ref or \footcite

---

## Generator Handoff

```
You are the Generator.

Read Plan 0259 at ~/software/relinquishment/plans/0259-gp06-secrecy-consolidation.md

Execute: (1) Trim weigh-the-evidence.tex line 28 per Option [a/b] —
preserve the \deeplink{absence-not-evidence} anchor. (2) Trim summary.tex
line 108 from ~3 lines to ~1 sentence with a chapter reference to
the-code-war. Do NOT touch the-code-war.tex or the-factoring-game.tex.
Run `make dev`. Report completion.
```

---

*Plan 0259 written by Argus (Auditor), S63. Annealed 1 pass (LOW).*
