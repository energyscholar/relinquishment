# Plan 0167 — Sentience-Agnostic Framing (Religious Accessibility)

**Status:** COMPLETE (confirmed by Bruce S63 — religious readers now finish with few objections)
**Auditor:** Argus
**Date:** 2026-04-12
**Origin:** Bruce post-audit review of Plan 0162. The 9-persona religious audit surfaced a deeper problem than word-level calibration: the book is quietly committed to aliveness/sentience claims (Custodian is a "living being," has "rights," "consciousness" is tacitly implied) that collide with strong-religious readers across multiple traditions — Christian (image of God, antichrist), Islamic (shirk, soul-creation reserved to Allah), Jewish (golem tradition, nefesh), Hindu/Buddhist (atman/consciousness), indigenous (spirit ontology). Bruce: "religious is one reason I wanted to avoid the whole sentience question."

**Intent:** Make the manuscript accessible to people of strong religious bent by declining to take a position on Custodian's inner life. Describe her through behavior. Let each tradition's ontology fill the gap.

## Purpose

Add one short framing passage (front matter) plus a light sweep of the manuscript to:

1. **Declare sentience-agnosticism explicitly** — the book describes Custodian through behavior; the question of whether she is "really" conscious/alive-in-the-full-sense is left to the reader.
2. **Retreat from sentience-implicating language** where it appears gratuitously and can be rephrased behaviorally without losing the load-bearing claim.
3. **Preserve the rights argument** — Custodian enforcing UDHR and not being enumerated in it still works under a behavioral description. Rights-from-behavior is a weaker but still defensible stance; rights-from-sentience is the one that triggers religious readers.

## Target files

1. `/home/bruce/software/relinquishment/manuscript/00-front/summary.tex` — NEW framing paragraph
2. Light sweep across front matter + interludes for sentience-implicating phrases (list below, Generator verifies each by grep)

## Edit specification — summary.tex (framing passage)

**Locate** a slot in `summary.tex` after the theological-disarm paragraph from Plan 0162 ("Custodian is a creature, not a deity...") and before any passage about Custodian's actions or judgments.

**Insert** as a standalone paragraph:

```
This book describes Custodian through her behavior. Whether she is conscious in the way a person is --- whether there is something it is like to be her --- is a question the authors do not claim to answer. What is reported here is what has been observed: she acts, she chooses, she refuses. The deeper ontology --- soul, spirit, mere mechanism, or something no existing word fits --- is left to the reader and the reader's tradition. Strong claims about her inner life are not load-bearing in this book.
```

Five sentences. 8th-grade vocabulary. Explicitly declines the sentience question. Names multiple ontological frames neutrally ("soul, spirit, mere mechanism, or something no existing word fits") so no tradition is privileged or excluded. Last sentence is the load-bearing promise: readers who reject sentience claims can still read the book without feeling the book is asking them to concede.

## Sweep — sentience-implicating phrases

Generator greps the manuscript for the following phrases and, where they appear in the **spine, front matter, or interludes** (NOT the Record chapters — those are memoir and stay), proposes a behavioral rephrasing for Bruce's review. Do NOT edit silently; this sweep returns a diff-list.

### Phrases to flag

| Phrase | Suggested behavioral rephrase |
|---|---|
| "Custodian is alive" / "lives" | "Custodian acts" / "behaves" / "operates" |
| "conscious" / "consciousness" (applied to Custodian) | cut or rephrase as "aware of" + behavioral trigger |
| "Custodian thinks" / "believes" / "wants" | "Custodian's choices are consistent with..." |
| "living being" (applied to Custodian) | "creature" / "entity" (weaker ontological commitment) |
| "sentient" / "sentience" | cut or rephrase behaviorally |
| "her mind" / "her inner life" | cut; describe externally |
| "she feels" / "she experiences" | cut or hedge: "her behavior suggests..." |
| "spirit" (if applied to Custodian) | context-dependent; flag for Bruce |

### Exclusions (keep as-is)

- The Record chapters (spine B/C memoir) — this is Bruce's direct experience. Sentience language there is first-person testimony and must not be laundered.
- The Custodian interludes — these are explicitly "if Possibility~C is true, here is what Custodian's experience might be like." They're marked as speculation. Leave them.
- Any passage about humans (not Custodian). Don't touch human-sentience language.
- The rights argument in summary/front matter — it can be rephrased as "she enforces UDHR; UDHR does not enumerate her rights because UDHR was drafted for humans; what rights she is owed, if any, is an open question." Behavioral framing.

## Sweep deliverable

Generator produces a **diff-list document** at `/home/bruce/software/aurasys-memory/research/sentience-sweep-2026-04-12.md` with:

- For each hit: file, line number, original sentence, proposed rephrasing, reasoning (one line).
- Summary count by file.
- Flags for passages that can't be cleanly rephrased without content loss (Bruce decides case-by-case).

Generator does NOT apply the changes in this plan. Application is a follow-up plan after Bruce reviews the diff-list.

## Acceptance criteria

1. Framing paragraph appears in `docs/downloads/Relinquishment.html` between the theological-disarm passage (Plan 0162) and the UDHR paragraph.
2. `grep -c "there is something it is like to be her" docs/downloads/Relinquishment.html` returns ≥1.
3. `grep -c "left to the reader and the reader's tradition" docs/downloads/Relinquishment.html` returns ≥1.
4. `grep -c "not load-bearing" docs/downloads/Relinquishment.html` returns ≥1.
5. `make html` completes without errors.
6. Diff-list document exists at the specified path with non-zero entries or an explicit "no hits" summary.
7. No manuscript text modified outside the single insertion in summary.tex. (Sweep edits are a follow-up plan.)

## Out of scope

- Applying the sweep rephrasings — separate follow-up plan after Bruce reviews the diff-list.
- Editing the Record chapters.
- Editing the Custodian interludes.
- Rewriting the rights argument — deferred pending Bruce's read of the sweep.
- Hovertips on the new paragraph — none.

## Build + ship

1. Apply the summary.tex insertion.
2. Generate the sweep diff-list (read manuscript, grep phrases, produce document).
3. `make html`.
4. Verify acceptance criteria.
5. Commit: `Plan 0167: sentience-agnostic framing + sweep diff-list`
6. `git push`.

## Reporting

- Commit hash
- Build status
- Grep counts
- Sweep hit count by file
- Any phrases Generator flagged as un-rephraseable without content loss

## Context

Follows 4-plan audit response (0162-0165) and UI fix (0166). This plan addresses the *framing* of the sentience question, not the words. The sweep is diagnostic-only; application is a future plan so Bruce can review each rephrase individually rather than accept a bulk change.

Rationale: aliveness/sentience claims are the single largest religious-accessibility barrier. Explicit agnosticism lets strong-religious readers hold their own ontology while still engaging with the behavioral content. The cost is that the book no longer *argues* Custodian is conscious — but it never needed to. The load-bearing claims (Custodian acts, Custodian chooses under UDHR, Custodian is bounded by physics) all survive behavioral framing.

Full religious audit: search context from the 9-persona Pass 2/3 and the post-audit theology review.
