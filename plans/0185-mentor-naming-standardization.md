# Plan 0185 — Standardize mentor character naming: David (youth) → Healer (post-medic-training)

**Type:** Character-naming standardization pass across manuscript prose. Three phases, three commits under one plan. Halt-and-report at ambiguous cases.

## Context

Current prose uses 4+ names for the same person: Healer, David Lane, Lane, David. Bruce's call (2026-04-13): **one canonical name in narrative prose, with one earned-name transition.**

## The rule

- **David** — pre-combat-medic-training: childhood, ranch life, recruitment, basic training until combat-medic certification.
- **Healer** — post-combat-medic-training: from combat medic certification forward (1984 Northern Ireland onward). All adult/military/DARPA/Bruce-era prose.
- **David Lane** — appears ONCE, in the biographical reveal (summary.tex:237), explicitly as "not his real name." Frames the dual-register: on paper David Lane, in this book Healer.
- **Lane** (without David) — removed from narrative prose entirely. Never appears except as part of the revealed pseudonym "David Lane" at :237.
- **Steven "Legs" Lane** — preserved as-is. External published-account cover identity (McNab/Ryan Bravo Two Zero accounts). Not a name the book chooses; left verbatim where it appears.

**Narrative justification of the transition:** the name "Healer" is earned at combat-medic certification (pos03-the-mentor.tex:90 "He trains as a combat medic"). Pre-training = David the boy; post-training = the man whose calling becomes healing. This maps to the book's epistemic-distance discipline: name the role, not the person.

## Pre-flight (Generator, once at start)

```
cd /home/bruce/software/relinquishment
grep -rn "\bDavid\b\|\bLane\b\|\bHealer\b" manuscript/*.tex manuscript/**/*.tex 2>/dev/null > /tmp/0185-name-audit.txt
wc -l /tmp/0185-name-audit.txt
```

Expect ~100+ hits. This is the working list. Generator checks each hit against the rule and converts or leaves per phase.

## Phase 1 — Front matter (commit 1)

**Files:** `manuscript/00-front/*.tex` (summary, introduction, preface, legal-note, corrections, the-stack, hook).

**Expected converts:**

- `summary.tex:26` — "That was Lane, years later, talking to Bruce Stephenson" → "That was Healer, years later, talking to Bruce Stephenson" — **FIRST-USE FIX. Critical.** Lane was appearing 211 lines before the reveal.
- `summary.tex:191` — "drew on Lane's Maori cultural heritage" → "drew on Healer's Maori cultural heritage"
- `summary.tex:237` — biographical reveal. **Update to frame the dual-register explicitly.** Current: `His name is David Lane \textit{(not his real name)}. He is half Maori...` **Replace with:**

  > The name on his passport --- David Lane --- is not his real name either. In this book I call him Healer, the name he earned when he was certified as a combat medic at nineteen. He is half Maori --- an indigenous people of New Zealand --- on his mother's side. He grew up on a ranch in New South Wales, Australia, raised partly by Aboriginal elders. As a youth --- before the military --- he was David. He was selected for the SAS\@. He climbed K2, one of the deadliest mountains on earth.

- `summary.tex:239, 245, 251` — "Lane" → "Healer" in remaining instances.
- `corrections.tex:18` — leave content mostly intact (it already explains the Lane-is-pseudonym convention); tighten to reference the David→Healer rule if cleanly possible, else leave.
- `introduction.tex` — already uses "Healer" throughout; verify no "Lane" or "David" instances.
- `preface.tex`, `legal-note.tex` — already use "Healer"; verify.

**Halt-and-report if:** any conversion in summary.tex produces an awkward sentence that can't be resolved by straight substitution. Report current phrasing + proposed phrasing; wait for Auditor.

**Acceptance (Phase 1):**

1. `grep -n "\bLane\b" manuscript/00-front/*.tex` returns hits only in `corrections.tex` (documenting the convention) + `summary.tex:237` (in the "David Lane" biographical reveal).
2. `grep -n "\bDavid\b" manuscript/00-front/*.tex` returns hits only in `corrections.tex` + `summary.tex:237` (reveal) and any youth-scene reference if present. Front matter is narrator-to-reader voice; no in-scene youth prose expected here.
3. `make` HTML build clean.

**Commit 1:** `Plan 0185 phase 1: standardize mentor naming in front matter (Healer throughout, David in biographical reveal)`

## Phase 2 — Track-2 testament narrative (commit 2)

**Files:** `manuscript/track-2-testament/pos02-alpha-farm.tex`, `pos03-the-mentor.tex`, `pos23-the-weight.tex`, `pos33-digital-doppelganger.tex`.

**Special attention — pos03-the-mentor.tex:**

This chapter spans childhood → military → present. Apply rule **in place**: sentences describing pre-combat-medic-training scenes keep "David"; sentences describing post-training scenes use "Healer." The transition beat at line 90 ("He trains as a combat medic") is the hinge.

**Specific guidance for pos03:74** (Officer Ken kangaroo incident): youth, keep **David**.

**Specific guidance for pos03:90** (combat medic training): keep **David** during the training itself ("He trains as a combat medic") — the training EARNS the name, but the name transition happens at certification, which the prose should mark. Generator: at the end of the training sentence, add one short sentence marking the name transition. Suggested: `From that point the men in his unit called him Healer.` (Generator may refine phrasing; halt-and-report if unsure).

**Specific guidance for pos03:100** (Operation Desert Shield, Bravo Two Zero): adult, **Healer** — except the Steven "Legs" Lane published-account reference stays verbatim. "David was ordered to the Middle East" → "Healer was ordered to the Middle East." "David participated in the compromised Bravo Two Zero operation" → "Healer participated in...". "In these accounts David is known as Steven 'Legs' Lane" → "In these accounts Healer is known as Steven 'Legs' Lane."

**pos02-alpha-farm.tex:** Bruce-era adult scene. "David" → "Healer" throughout. Line 89's "David is a trained combat medic" → "Healer is a trained combat medic" (preserves the etymology-of-name reveal in the scene).

**pos23-the-weight.tex, pos33-digital-doppelganger.tex:** Bruce-era adult scenes. All "David" → "Healer."

**Halt-and-report if:** any David→Healer conversion produces a sentence where the name change introduces logical ambiguity (e.g., a sentence that only parses if both names refer to different people).

**Acceptance (Phase 2):**

1. `grep -n "\bDavid\b" manuscript/track-2-testament/*.tex` returns hits only in youth scenes (pre-combat-medic-training prose) + "David Lane" / "Steven 'Legs' Lane" / any already-qualified reference.
2. `grep -n "\bLane\b" manuscript/track-2-testament/*.tex` returns hits only in "David Lane" biographical refs + "Steven 'Legs' Lane" published-account refs.
3. `make` HTML build clean.

**Commit 2:** `Plan 0185 phase 2: mentor naming in track-2 narrative (David→Healer post-medic-training)`

## Phase 3 — Track-1, record, and spine parallels (commit 3)

**Files:** `manuscript/track-1-confession/pos18-the-walk-out.tex`, `manuscript/record/alpha-farm.tex`, `manuscript/record/the-handler.tex`, `manuscript/record/the-demonstration.tex`, `manuscript/spine/*.tex` if any mentor naming appears there, `manuscript/appendix/corrections.tex`.

**pos18-the-walk-out.tex:40** "The youngest project scientist --- described as a brash and daring warrior-scholar named David --- took the critical step." This is DARPA era (1994-95), adult, post-training. → "named Healer" (or restructure to drop the aside if awkward — Generator judges).

**record/alpha-farm.tex:88, 97** parallel to pos02. Same rule.

**record/the-handler.tex** dossier style — review each appearance of David/Lane; apply rule.

**appendix/corrections.tex:22** parallel to front-matter corrections; sync.

**Out of scope (do NOT touch):**
- `manuscript/staging/raw/*.md` — raw source documents; leave for separate pass.
- `manuscript/versions/simple-summary.md` — derived/alt version; Bruce can regenerate or update separately.
- `manuscript/bibliography.bib`, any `.aux` files — not prose.

**Acceptance (Phase 3):**

1. `grep -rn "\bDavid\b\|\bLane\b" manuscript/ --include="*.tex" | grep -v "staging/"` shows only: youth scenes, "David Lane" reveal, "Steven 'Legs' Lane" verbatim refs, and any corrections-documentation references.
2. `grep -rn "\bHealer\b" manuscript/ --include="*.tex"` shows expanded footprint — all former adult-David / adult-Lane converted.
3. `make` HTML build clean.

**Commit 3:** `Plan 0185 phase 3: mentor naming in track-1, record, appendix`

## Build + push

After all three commits land clean, push per `feedback-build-to-website.md`. Tag is optional — Bruce's call.

## Rollback

Three separate commits make bisection easy. `git revert` any individual phase, or all three.

## Handoff report (Generator, 6 lines per phase)

Per phase:
1. Commit SHA.
2. Pre-flight audit line count (total David/Lane/Healer references before Phase 1; shrinking across phases).
3. Per-file conversion counts: N David→Healer, N Lane→Healer, N left as David (youth), N left as "David Lane" (reveal), N left as "Steven 'Legs' Lane" (verbatim).
4. Halt-and-report events: count + locations. If zero, say so.
5. Build result per phase.
6. Any surprises (e.g., a mentor reference in a file not anticipated above).
