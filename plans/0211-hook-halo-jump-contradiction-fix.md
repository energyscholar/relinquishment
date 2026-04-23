# Plan 0211 — Fix p1 hook contradiction: "He will do it again" vs. "probably my last HALO jump"

## Status
**Status:** COMPLETE (verified S63 audit)
COMPLETE (verified S63 audit). Originally: Ready for Generator.

## Problem

The p1 hook (`hook.tex:13`) says:

> He has done this before. He will do it again.

The Record (`alpha-farm.tex:13`, also `pos02-alpha-farm.tex:14`) says:

> *This will probably be my last military HALO jump.*

Direct contradiction. The hook promises repetition; the Record says farewell. The hook's statement is false under the book's own narrative.

## Proposed edit

**Current (hook.tex:11–13):**
```
A man falls from the stratosphere. The air is thin enough to kill in minutes. He checks his oxygen and parachute. Through cloud, then below cloud, toward a name the world will soon know. His orders are to observe and record. The people below will never know he was there.

He has done this before. He will do it again.
```

**Proposed (hook.tex:11 — line 13 deleted):**
```
A man falls from the stratosphere. The air is thin enough to kill in minutes. He checks his oxygen and parachute. Through cloud, then below cloud, toward a name the world will soon know. His orders are to observe and record. This is not his first HALO jump. The people below will never know he was there.
```

## Why this works

1. **Contradiction eliminated.** "Not his first" is compatible with "probably my last" — they echo each other across reading depths without conflicting.
2. **Experience signal preserved.** "This is not his first HALO jump" says *veteran* as clearly as "He has done this before."
3. **p-level linkage improved.** "HALO jump" currently first appears in p2 (`summary.tex:239`: *"This is called a HALO jump — High Altitude, Low Opening"*) and in p3 (`alpha-farm.tex:13`). Planting the term in p1 creates a proper p1→p2→p3 distillation chain: p1 plants the seed (no explanation), p2 explains it, p3 gives the emotional payoff.
4. **Condensation.** Three sentences across two paragraphs → two sentences in one paragraph. Net: tighter without losing information.
5. **Thematic alignment.** Current ending: "He will do it again" (forward-looking, promising action). Proposed ending: "The people below will never know he was there" (invisibility, silence). The book's throughline is silence, the unseen, the gap — the new closing beat is more on-theme.

## Eigenvalue assessment (Auditor)

**Persona stability check (9 core):**

| Persona | Before | After | Δ |
|---|---|---|---|
| Chen (physicist, skeptic) | Neutral (opening is narrative) | Neutral | None |
| Reeves (phil-of-science) | Neutral | Neutral | None |
| Arjun (CS, Bangalore) | Neutral | Slight positive (military specificity) | +marginal |
| Doctorow (public intellectual) | Neutral | Neutral | None |
| Jane (secular generalist, L1) | PASS — context makes action clear | PASS — "HALO jump" is jargon but "falls from the stratosphere" + "parachute" decode it in context | None |
| Rachel (working parent, L1) | PASS — hooks with action | PASS — still hooks | None |
| Pastor Mike (evangelical) | Neutral | Neutral | None |
| Amir (Shia scholar) | Neutral | Neutral | None |
| Yusuf (Sunni professional) | Neutral | Neutral | None |

**F-mode check:**

| F-mode | Before | After | Δ |
|---|---|---|---|
| F-crank | Not triggered | Not triggered — "HALO jump" adds specificity, slightly reduces crank read | +marginal |
| F-scifi | Not triggered | Not triggered | None |
| F-delusion | Not triggered | Not triggered | None |
| F-AI-slop | Not triggered | Not triggered | None |
| F-conspiracy | Not triggered | Not triggered | None |

**Rhythm/pacing assessment:**

The standalone "He has done this before. He will do it again." paragraph creates a deliberate drumbeat — two short declaratives, a breath before the pivot. Removing it changes the opening's pacing. However: the new version has its own closing rhythm: "...His orders are to observe and record. This is not his first HALO jump. The people below will never know he was there." — three punchy sentences, ending on the invisibility beat. The rhythm is different, not weaker.

**C-violation check:** Neither version makes a Possibility-C-only claim. Both are narrative setup, not epistemic. PASS.

**Verdict: stable eigenvalue.** No persona flips, no F-mode triggers, contradiction eliminated, p-level linkage improved. Net: slightly positive.

## Scope

**Edit:** `manuscript/00-front/hook.tex` — lines 11–13 only.

**No other files touched.** The contradiction is one-directional: the hook said something the Record contradicts. The Record is correct. Only the hook changes.

**Regenerate:** `docs/downloads/Relinquishment.html`

## Phases (3)

### Phase 0 — Pre-flight

```bash
cd ~/software/relinquishment

# Confirm current text
grep -n 'He has done this before' manuscript/00-front/hook.tex
# expect line 13: "He has done this before. He will do it again."

grep -n 'never know he was there' manuscript/00-front/hook.tex
# expect line 11 (end of first paragraph)

# Confirm the contradiction target still exists
grep -n 'probably be my last' manuscript/record/alpha-farm.tex
# expect line 13

# Word count baseline (p1 hook = everything inside \begin{quote}...\end{quote})
sed -n '/\\begin{quote}/,/\\end{quote}/p' manuscript/00-front/hook.tex | wc -w
# Record this number as BASELINE_WC
```

### Phase 1 — Edit

In `manuscript/00-front/hook.tex`, replace lines 11–13:

**OLD (lines 11–13):**
```
A man falls from the stratosphere. The air is thin enough to kill in minutes. He checks his oxygen and parachute. Through cloud, then below cloud, toward a name the world will soon know. His orders are to observe and record. The people below will never know he was there.

He has done this before. He will do it again.
```

**NEW (single paragraph, old line 13 deleted):**
```
A man falls from the stratosphere. The air is thin enough to kill in minutes. He checks his oxygen and parachute. Through cloud, then below cloud, toward a name the world will soon know. His orders are to observe and record. This is not his first HALO jump. The people below will never know he was there.
```

### Phase 2 — Post-edit verification

```bash
cd ~/software/relinquishment

# Contradiction eliminated
grep -c 'He will do it again' manuscript/00-front/hook.tex            # expect 0
grep -c 'He has done this before' manuscript/00-front/hook.tex        # expect 0

# New text present
grep -c 'not his first HALO jump' manuscript/00-front/hook.tex        # expect 1

# HALO seed chain intact
grep -c 'HALO' manuscript/00-front/hook.tex                           # expect 1 (p1 seed)
grep -c 'HALO' manuscript/00-front/summary.tex                       # expect 1 (p2 explanation)
grep -c 'HALO' manuscript/record/alpha-farm.tex                      # expect 1 (p3 payoff)

# Word count delta (should be small — net loss of ~7 words)
sed -n '/\\begin{quote}/,/\\end{quote}/p' manuscript/00-front/hook.tex | wc -w
# Compare against BASELINE_WC. Expect BASELINE_WC minus ~7.

# Closing sentence is now "never know he was there" (invisibility beat)
tail -n +11 manuscript/00-front/hook.tex | head -1 | grep -F 'never know he was there'
# expect match (last sentence of the paragraph)
```

### Phase 3 — Build + smoke

```bash
make html
```

**Smoke test:** Open `docs/downloads/Relinquishment.html`. Read the hook. Confirm:
1. "This is not his first HALO jump." appears after "observe and record."
2. "The people below will never know he was there." closes the paragraph.
3. No standalone "He has done this before" paragraph follows.
4. The next paragraph starts "Years later, he was part of something else."

### Commit

```bash
git add manuscript/00-front/hook.tex docs/downloads/Relinquishment.html
git commit -m "Plan 0211: fix p1 hook contradiction — 'He will do it again' vs. alpha-farm 'probably my last'

'He will do it again' contradicted the Record's 'This will probably be my
last military HALO jump.' Replaced with 'This is not his first HALO jump'
— preserves the experience signal, plants the HALO term for p2/p3 payoff,
eliminates the false statement, and closes on the invisibility beat
('never know he was there') rather than a broken promise.

Eigenvalue: stable across 9 personas, no F-mode triggers.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

## Acceptance

1. `grep -c 'He will do it again' hook.tex` → 0 (contradiction gone)
2. `grep -c 'not his first HALO jump' hook.tex` → 1 (new text present)
3. HALO appears once each in hook.tex, summary.tex, alpha-farm.tex (p1→p2→p3 chain)
4. Word count delta is −7 ± 2 (condensation, not expansion)
5. HTML builds clean; hook reads correctly in browser

## Risks

- **Very low.** Single-paragraph edit in one file. No hovertip changes, no structural changes, no cross-file dependencies. The edit removes text and modifies one sentence.
- **Jane/jargon marginal risk.** "HALO jump" is military jargon. But context ("falls from the stratosphere," "checks his oxygen and parachute") decodes it without explanation. p2 (`summary.tex:239`) explicitly defines the term for any reader who wants it. Risk accepted.
- **Rhythm change.** The standalone two-sentence paragraph is gone. Assessed as neutral-to-positive — the new closing beat is more on-theme. Not reversible in isolation without reintroducing the contradiction.
