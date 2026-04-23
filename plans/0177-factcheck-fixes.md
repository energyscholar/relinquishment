# Plan 0177 — Fact-Check Corrections (8 items)

**Type:** Surgical fact-correction pass across multiple files. One commit. Zero structural changes, zero prose rewrites beyond the minimum needed to fix each factual error.

## Context

A thorough fact-check pass (Auditor, 2026-04-13) plus one additional catch by Bruce surfaced 8 factual errors/inconsistencies of consequence. This plan fixes all of them in one commit. One HIGH-severity, three MEDIUM in citation-heavy / load-bearing chapters, rest are one-word date corrections.

## Generator latitude

For each fix, Generator has license to adjust surrounding grammar and punctuation to make the correction read cleanly (e.g., cleaning up a dangling "then" after dropping a clause in Fix 4). Generator does NOT have license to reword surrounding content, add or remove sentences beyond the specified fix, or restructure paragraphs. If a fix cannot be landed cleanly without wider prose changes, halt at that fix and report.

## Pre-flight (Generator does first)

Before any edits, run:

```
cd /home/bruce/software/relinquishment
grep -n "invented in 1978" manuscript/spine/the-factoring-game.tex
grep -n "1,200 km\|1,200\~km\|1200 km" manuscript/spine/the-braid.tex
grep -n "Ultra Secret" manuscript/appendix/timeline.tex
grep -n "Steps Toward" manuscript/appendix/timeline.tex
grep -n "Christle" manuscript/appendix/*.tex manuscript/track-3-awakening/*.tex 2>/dev/null
grep -n "Deutsch-Jozsa\|Deutsch–Jozsa\|Deutsch Jozsa" manuscript/spine/the-factoring-game.tex
grep -rn "thirty-five years" manuscript/
grep -n "Every password would be meaningless" manuscript/00-front/summary.tex
```

If any grep returns ZERO or MULTIPLE unexpected hits (e.g., "thirty-five years" appearing in more than one file), halt and report before editing.

These greps verify each target still exists at the predicted location. If any returns zero hits or unexpected content, halt and report — the file may have moved since the fact-check was performed.

## The 7 fixes

### Fix 1 — HIGH: PKC invention date (the-factoring-game.tex:24)

**Current:** `The mathematics of Public Key Cryptography, invented in 1978, ...`

**Replace with:** `The mathematics of Public Key Cryptography, published publicly between 1976 and 1978, ...`

**Rationale:** "Invented in 1978" contradicts `the-code-war.tex`, which meticulously establishes Ellis 1969 / Cocks 1973 / Diffie-Hellman 1976 / RSA 1977 (published 1978). PKC is the book's load-bearing analogy — any cryptographer reading both chapters will catch a single-year invention claim. "Published publicly between 1976 and 1978" covers Diffie-Hellman's 1976 paper through RSA's 1978 CACM publication, consistent with the-code-war.tex's longer timeline.

**Source:** Diffie & Hellman, "New Directions in Cryptography," IEEE Trans. Info. Theory 22(6), Nov 1976. RSA paper: CACM 21(2), Feb 1978.

### Fix 2 — MEDIUM: Micius teleportation distance (the-braid.tex)

**Current:** `By 2017, the Chinese Micius satellite extended the range to 1,200 km` (approximate wording — Generator confirms via grep above).

**Replace with:** `By 2017, the Chinese Micius satellite extended the range to 1,400 km`

**Rationale:** Ren et al. 2017 (Nature 549, 70-73) reports ground-to-satellite quantum teleportation at up to 1,400 km. 1,203 km is the Yin et al. 2017 (Science) entanglement-distribution figure — different experiment. The book's own `timeline.tex:285` already uses 1,400 km. Converge.

**Source:** Ren et al., Nature 549, 70-73 (2017). https://www.nature.com/articles/nature23675

### Fix 3 — MEDIUM: Winterbotham publication date (timeline.tex:86)

**Current:** `[1975] The Ultra Secret finally revealed publicly, 35 years after its inception...`

**Replace with:** `[1974] The Ultra Secret finally revealed publicly, 34 years after its inception...`

**Rationale:** Winterbotham's *The Ultra Secret* was published 1974, not 1975. The-code-war.tex:40 correctly says 1974. The "35 years" claim depends on the wrong 1975 date; 1940→1974 = 34 years.

**Source:** https://en.wikipedia.org/wiki/F._W._Winterbotham

### Fix 4 — MEDIUM: Minsky entry untangling (timeline.tex:60)

**Current (approximate):** `[1954] Marvin Minsky writes his doctoral thesis, Theory of Neural-Analog Reinforcement Systems..., then publishes Steps Towards Artificial Intelligence.`

**Replace with:** `[1954] Marvin Minsky completes his doctoral thesis, Theory of Neural-Analog Reinforcement Systems and its Application to the Brain-Model Problem.`

**Rationale:** Minsky's "Steps Toward Artificial Intelligence" was published 1961 in Proc. IRE 49(1), 8-30 — not 1954. Title is "Steps Toward" (no 's'). The 1954 thesis and 1961 paper are two different works. Simplest fix: drop the Steps Toward claim from the 1954 entry.

**Optional:** If the author wants the Steps Toward paper in the timeline, add a separate 1961 entry: `[1961] Minsky publishes Steps Toward Artificial Intelligence (Proc. IRE).` Generator: do NOT add the 1961 entry unless Bruce explicitly authorizes — scope creep risk. Drop the Steps Toward fragment from the 1954 entry and stop.

**Source:** Minsky, Proc. IRE 49(1), 8-30 (1961). https://ieeexplore.ieee.org/document/4066245/

### Fix 5 — HIGH (on context, not severity): Firmware Anchor 10 citation (firmware-update.tex Anchor 10)

**Problem:** The Anchor 10 prose claims "room-temperature quantum coherence" and cites Christle et al. 2015. Christle et al. 2015 (Nat. Mater. 14, 160) reports millisecond coherence in SiC at ~20 K — NOT at 300 K. The prose claim (RT coherence exists in NV-diamond and SiC commercial products) is correct; the citation is wrong.

**Action:** Generator reads the current Anchor 10 passage in `manuscript/track-3-awakening/firmware-update.tex` (likely line 44 area per fact-check; confirm via grep in pre-flight). Replace the Christle 2015 citation with the correct RT-coherence sources:

- **For NV-diamond room-temperature coherence:** Balasubramanian et al., *Nature Materials* 8, 383-387 (2009). "Ultralong spin coherence time in isotopically engineered diamond."
- **For SiC room-temperature entanglement:** Klimov, Falk, Christle, Dobrovitski, Awschalom, *Science Advances* 1(10) e1501015 (2015). "Quantum entanglement at ambient conditions in a macroscopic solid-state spin ensemble."

**Replacement citation format:** whatever format the rest of `firmware-update.tex` uses — likely `\footcite{balasubramanian2009, klimov2015}` or equivalent. Generator confirms existing citation style before editing.

**Do NOT rewrite the prose** unless the prose itself makes a 20K-specific claim attributable to Christle; if the prose only says "room-temperature coherence" at the level the fix-target supports, citation swap is sufficient.

**Rationale:** The firmware-update chapter is the book's explicit adversarial-review-proof physics anchor. A citation-claim mismatch in this chapter is the exact failure mode the chapter is designed to prevent.

**Source:** https://pubmed.ncbi.nlm.nih.gov/19349962/ (Balasubramanian); https://www.science.org/doi/10.1126/sciadv.1501015 (Klimov)

### Fix 6 — LOW: Deutsch-Jozsa → Simon's problem (the-factoring-game.tex:32)

**Current (approximate):** `Deutsch-Jozsa hinted that a theoretical quantum algorithm might be able to factor numbers in polynomial time, and thus crack public key cryptography.`

**Replace with:** `Simon's problem (1994) demonstrated an exponential quantum speedup for a structured problem, inspiring Shor to apply the same periodicity-finding insight to integer factoring.`

**Rationale:** Deutsch-Jozsa (1992) is a query-complexity separation with no factoring connection. Shor credits Simon's problem (Simon 1994) as the direct inspiration for his factoring algorithm. Historians of quantum computing will object to the D-J→factoring lineage.

**Source:** Shor retrospective, *Physics Today* 78(4), 2025. Simon, FOCS 1994; SIAM J. Comput. 26, 1474 (1997).

### Fix 8 — MEDIUM: "Every password would be meaningless" overclaim (summary.tex, Lock on Every Door section)

**Current:** `Every password would be meaningless. Every encrypted message --- from your email to military command channels --- could be read by whomever controlled that machine.`

**Replace first sentence with:** `Every encrypted login would be exposed.`

**Rationale:** Shor's algorithm breaks asymmetric cryptography (RSA, ECC, Diffie-Hellman) — the math protecting *channels*, not the hashes protecting passwords-at-rest. Grover's algorithm gives only a √N speedup on hash reversal, effectively halving bit-strength but not rendering hashed passwords "meaningless." The rhetorical thump of the sentence is load-bearing in context; preserve it by shifting the claim from "passwords are broken" to "login channels are exposed" — which is correct under Shor and flows cleanly into the next sentence ("every encrypted message...").

**What NOT to do:** Do not delete the sentence. Do not elaborate into a technical aside about Grover vs Shor. The pop-sci level is right; just the specific claim needs correcting.

**Source:** Shor, FOCS 1994 (factoring/discrete-log, breaks PKI). Grover, STOC 1996 (√N speedup, applies to symmetric/hash brute force). Bernstein & Lange, "Post-quantum cryptography," Nature 549, 188-194 (2017) — standard reference that symmetric and hash-based crypto require only larger key sizes, not wholesale replacement.

### Fix 7 — LOW: Bletchley secrecy duration (summary.tex — ONE occurrence)

**Current:** `Ten thousand people kept that secret for thirty-five years.` (summary.tex, The Secret Lab section)

**Replace with:** `Ten thousand people kept that secret for more than thirty years.`

**Rationale:** 1940→1974 = 34 years. "Thirty-five" depends on the wrong Winterbotham 1975 date. `the-code-war.tex` already uses "more than thirty years" — converge.

**Source:** Internal consistency. Bletchley Park active from late 1939; *The Ultra Secret* published 1974.

## Out of scope (deliberately — pending Bruce's call)

The fact-check surfaced lower-severity items not in this plan:
- Colossus "programmable" vs "configurable" (historians' quibble; defensible at pop-sci level).
- Turing death date discrepancy (died June 7, found June 8 — not actually contradictory, clarity issue only).
- Hopfield "first recurrent neural network" overclaim (LOW).
- Patrick Ball testimony date March 13 vs March 14 (LOW).
- Engel et al. 2007 cited as "Fleming et al." (LOW, citation-style).
- The C-violation flag on the "intelligent life" sentence in summary.tex — separate rewrite pass, not a fact error.

These can be bundled into a follow-up plan if desired. Not in 0177.

## Acceptance

1. `make` HTML build clean. No LaTeX errors, no new warnings.
2. `grep -n "invented in 1978" manuscript/spine/the-factoring-game.tex` returns zero hits.
3. `grep -n "1,200 km\|1200 km\|1,200\~km" manuscript/spine/the-braid.tex` returns zero hits (1,400 is the only Micius teleportation distance).
4. `grep -n "thirty-five years" manuscript/` returns zero hits.
5. `grep -n "Steps Towards" manuscript/appendix/timeline.tex` returns zero hits (also `Towards` → `Toward` spelling).
6. `grep -n "Christle" manuscript/` returns zero hits (replaced by Balasubramanian + Klimov), OR returns only legitimate Christle mentions if the paper appears elsewhere in the book for a correctly-cited claim (e.g., SiC low-temperature coherence would be a legitimate Christle cite).
7. `grep -n "Deutsch-Jozsa\|Deutsch–Jozsa" manuscript/spine/the-factoring-game.tex` returns zero hits in the factoring-inspiration context (may still appear elsewhere for correctly-scoped uses).
8. `grep -n "Every password would be meaningless" manuscript/00-front/summary.tex` returns zero hits (replaced per Fix 8).
9. Whitespace-normalized diff across all touched files shows exactly the 8 fixes and no other content changes.

## Commit

One commit: `Plan 0177: fact-check corrections — PKC date, Micius distance, Winterbotham 1974, Minsky untangle, firmware Anchor 10 citation, Simon's problem, Bletchley duration`

Build + push per `feedback-build-to-website.md`.

## Rollback

`git revert` the single commit. Zero risk.

## Rehearsal step

Generator executes Fix 3 (Winterbotham date) first — smallest, safest, one-line change. Builds, verifies clean. If clean, proceeds with remaining fixes in the same commit. If any fix encounters an ambiguity (e.g., Generator cannot determine which Christle citation style to use), halt at that fix, report, and wait for Auditor guidance — do NOT guess.

## Handoff report (Generator, 6 lines)

1. Commit SHA.
2. Pre-flight grep results — confirm all 7 targets located.
3. Per-fix status: 7 × (applied / halted-for-guidance). If any halted, state why.
4. Acceptance grep results (criteria 2-7).
5. Build + push result.
6. Any surprises (e.g., Christle already cited elsewhere with a different claim, unexpected file moves).
