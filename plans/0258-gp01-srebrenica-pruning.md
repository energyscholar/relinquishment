# Plan 0258 — GP01: Srebrenica Pruning (Post-Witness-Reframe)

**Auditor:** Argus (S63)
**Date:** 2026-04-25
**Status:** READY FOR GENERATOR
**Source:** Gen's GP01 (has-anyone-looked issue #5)
**Annealing:** LOW (1 pass)
**Independent:** No dependency on other GP plans.

---

## Problem

Now that Plan 0254 (witness-not-recruit reframe) is implemented, the
Srebrenica material carries excess burden. Gen's diagnosis: the section
does not need to prove the atrocity happened — it needs to serve the
post-atrocity/UDHR frame, Healer's claimed presence, and corroborating
public artifacts with source order clear.

Gen (issue #5): "Please cut or demote material whose only job is to prove
that the atrocity itself happened."

Gen (issue #6): The keep/cut distinction turns on source order — was this
David-first-then-corroborated, or Bruce-found-later? "That distinction
matters a lot for how the section should function."

---

## Affected Files

**Primary:** `manuscript/record/what-healer-said.tex` (193 lines, 14
Srebrenica mentions)

**Duplicate:** `manuscript/track-2-testament/pos05-the-stories.tex` (180
lines, 13 mentions) — testament track copy. All pruning changes must be
applied to BOTH files identically.

**Residual:** `manuscript/track-2-testament/pos19-patrick-ball.tex` (57
lines) — merged into what-healer-said per Plan 0091. Verify whether this
file is still \included in the build. If not, ignore it.

---

## What to KEEP (Gen's criteria)

1. **Post-atrocity / UDHR frame** — Healer's nightmares, motivation for
   ethical framework. Lines ~168: "he carried Srebrenica in his nightmares."

2. **Healer's claimed presence** — The fact that he said he was there.
   Core testimony. The HALO jump opening sentence, the observation claim,
   the extraction. Keep enough to establish the claim without excess
   tactical detail.

3. **Corroborating public artifacts (source order clear):**
   - SAS at Srebrenica section (lines ~159-161): NIOD documentation, JCO
     presence, MoD lawsuit, classified honours. ALL independently sourced.
   - Patrick Ball ICTY nexus (lines ~153-157): Ball → Milosevic trial →
     cDc connection. Independently documented bridge.

4. **Deep link `srebrenica-witness`** (line 133) — preserve the anchor.
   If surrounding text is trimmed, keep the deep link on whatever sentence
   survives.

---

## What to CUT or DEMOTE

The extended tactical narration (lines ~113-137) currently runs ~25 lines
of first-person operational detail: terminal velocity HALO jump, parachute
mechanics, landing technique, bush concealment, scent discipline, five
days of observation, telescopic scope, night vision gear, rifle sights on
officers, waterproof paper, camera lenses.

Gen's principle: this reads as fiction-craft, not testimony. The reader
doesn't need the operational detail to believe or weigh the claim. What
matters is: (a) he says he was there, (b) he says he witnessed atrocities,
(c) independent sources confirm SAS presence.

**Proposed approach:** Compress lines ~113-137 from ~25 lines to ~8-10
lines. Keep: the claim of presence, the witnessing, the emotional weight,
the deep link anchor, the extraction. Cut: HALO jump mechanics, parachute
details, bush dimensions, scent discipline, night vision inventory, rifle-
sight moral dilemma (already covered by "closest I ever come to disobeying
direct orders"), camera lens details.

**Bruce decides:** How much tactical detail stays. Gen says cut; Bruce may
want to preserve specific details for authenticity. The Generator should
present Bruce with a compressed draft for approval before finalizing.

---

## Changes

### Step 1: Compress Srebrenica narration in what-healer-said.tex

Reduce lines ~113-137 from ~25 lines to ~8-10 lines. Preserve:
- Opening claim of presence (1-2 sentences)
- Witnessing claim + emotional weight (2-3 sentences)
- `\deeplink{srebrenica-witness}` anchor on a surviving sentence
- Extraction mention (1 sentence)

### Step 2: Apply identical changes to pos05-the-stories.tex

Mirror all cuts. The testament track must match.

### Step 3: Verify pos19-patrick-ball.tex status

If pos19 is still `\include`d in main.tex, it may have duplicate
Srebrenica content that also needs pruning. If it's not in the build
(merged per Plan 0091), ignore it.

### Step 4: Build and verify

- `make dev` clean
- Deep link `srebrenica-witness` still resolves
- Deep link `katharine-gun-connection` (line 188) unaffected
- No broken footnotes (Srebrenica passages cite ballicty2002,
  ictydecision, foreignpolicy2012, niod2002)

---

## Source Order (RESOLVED)

Bruce's answer: He already knew the surrounding history (Serbian war crimes
trials, Patrick Ball) before meeting Healer. When Healer referenced these
items, Bruce recognized them. He then researched the history in detail.

**Pattern:** Bruce-knew-context → Healer-referenced → Bruce-verified.

This is a three-step corroboration: independent prior knowledge, then
Healer's reference landed because Bruce recognized it, then systematic
verification. The section should make this source order explicit. The
Generator should add 1-2 sentences clarifying that Bruce's knowledge of
the war crimes trials preceded the mentorship, and Healer's references
connected to what Bruce already knew.

---

## What NOT to Change

- Patrick Ball ICTY nexus section (it's doing its own evidentiary work)
- SAS at Srebrenica corroboration section (independently documented)
- Katharine Gun connection (line 188, unrelated deep link)
- Iraq war discussion (line 168, "he carried Srebrenica in his nightmares")
- Any footnote citations — keep all \footcite references

---

## Annealing Log (LOW — 1 pass)

**Duplicate sync risk:** Both files must change identically. The Generator
must edit what-healer-said.tex FIRST, verify, then apply the same cuts to
pos05-the-stories.tex. Line numbers differ slightly between files — use
content matching, not line numbers.

**Deep link preservation:** `srebrenica-witness` is in the heart of the
passage being pruned. The Generator MUST keep this anchor on whatever
sentence survives the compression. Suggested anchor point: the witnessing
sentence itself ("I witness and take careful notes" or equivalent).

**Footnote preservation:** Four \footcite references in the broader
Srebrenica/Ball sections. If any cited passage is cut, the Generator must
ensure the citation survives on remaining text or is cleanly removed (no
orphaned citations).

**pos19 status:** Checked main.tex — pos19-patrick-ball.tex is NOT
\included (no line for it). It's in the testament track only
(track-2-testament). Let me check...

Actually, pos05-the-stories.tex already contains the merged pos19 content
(per Plan 0091 srcnote). So pos19 may be redundant. The Generator should
check whether pos19 is in any \include and flag if so.

**Rating: 8/10.** The pruning itself is contained and reversible. The
2-point gap: (1) Bruce must answer the source-order question before Gen's
editorial intent is fully served, (2) the right amount of compression is
subjective — the Generator should present a draft to Bruce rather than
finalizing unilaterally.

---

## Acceptance Criteria

- [ ] Srebrenica tactical narration compressed from ~25 to ~8-10 lines
- [ ] Deep link `srebrenica-witness` preserved on surviving sentence
- [ ] what-healer-said.tex and pos05-the-stories.tex match
- [ ] SAS corroboration section intact
- [ ] Patrick Ball ICTY nexus section intact
- [ ] All \footcite references either kept or cleanly removed
- [ ] `make dev` clean build
- [ ] Source order made explicit (Bruce-knew → Healer-referenced → Bruce-verified)

---

## Generator Handoff

```
You are the Generator.

Read Plan 0258 at ~/software/relinquishment/plans/0258-gp01-srebrenica-pruning.md

Execute: Compress the Srebrenica tactical narration in
manuscript/record/what-healer-said.tex (lines ~113-137) from ~25 lines
to ~8-10 lines per the plan's keep/cut criteria. Preserve the
\deeplink{srebrenica-witness} anchor. Apply identical changes to
manuscript/track-2-testament/pos05-the-stories.tex. Do NOT touch the
Patrick Ball or SAS corroboration sections. Run `make dev`. Report
completion with a summary of what was cut.
```

---

*Plan 0258 written by Argus (Auditor), S63. Annealed 1 pass (LOW).*
