# Plan 0216 — p2 T3 pacing: name the thermal objection, earn the conclusion

## Status
Ready for Generator.

## Dependency
Plan 0217 (p3 "But It's Hot" section) — **SHIPPED** at `095a973`. This plan distills from the resolved p3 argument.

## Problem

summary.tex lines 42–48 compress T3 (life in the Flat) into six lines. The reader goes from "The Flat permits self-organization" (L42) through "The magnetosphere has been here for billions of years" (L44) to "Nothing in known physics forbids life in the Flat" (L48) without addressing the physicist's first objection: *but the magnetosphere is millions of degrees.*

The word "temperature" does not appear in the T3 section. "Collisionless" does not appear. "Thermal" does not appear. The single hardest objection a scientifically literate reader will raise goes completely unaddressed at the reading level where most people stop.

Plan 0217 fixed this at p3 by adding a dedicated "But It's Hot" section to `the-wrong-substrate.tex`. This plan distills that argument into p2: one paragraph, ~45 words, naming and answering the objection at 12th-grade level.

## The "could it → does it?" turn

The T3 pacing feedback (memory) says: "FIRST get people going with the Flat. Build up to 'could it support life?' Then 'does it?'"

**Current p2 flow (L42–62):**
1. Kauffman — self-organization can form ✓
2. Magnetosphere — has Flat layers, billions of years ✓
3. ~~thermal objection~~ — **MISSING**
4. "Nothing forbids life" — arrives too fast, feels asserted not earned
5. Three possibilities applied to the Flat
6. "May also be a habitat" — the turn
7. "Under C, not empty" — the claim
8. Hydrothermal vent precedent
9. Dated prediction

**Fixed flow (after this plan):**
1. Kauffman — self-organization can form ✓
2. Magnetosphere — has Flat layers, billions of years ✓
3. **Thermal objection named and answered** — NEW
4. Credibility checkpoint — "Every claim above is published" (now implicitly covers thermal argument too)
5. "Nothing forbids life" — now earned
6. Three possibilities → habitat → Possibility C claim → vent precedent → prediction

The reader earns step 5 by going through step 3.

## Proposed edit

**Insert after L44** (the magnetosphere paragraph ending "...has been here for billions of years.") and **before L46** (the credibility checkpoint starting "Every claim above is published..."):

```latex
A physicist will object: the magnetosphere is millions of degrees. But ``hot'' in a \hovertip{collisionless plasma} --- where particles rarely collide --- does not mean ``thermally noisy.'' The noise that would destroy quantum states is orders of magnitude quieter than the kinetic temperature. The thermal objection assumes conditions that don't hold here.
```

**~45 words.** Names the gap, gives the reframe, moves on. The full argument (nine orders of magnitude, fluctuation spectrum, topology, Fu & Qin) lives in p3's "But It's Hot" section — this is the p2 distillation.

### What this does NOT do

- Does not restructure the rest of L42–62. The remaining flow (credibility checkpoint → "nothing forbids" → three possibilities → habitat → prediction) is well-paced once the thermal objection is cleared.
- Does not add the deep-ocean analogy ("hot the way the deep ocean is dark"). That's p3. The hydrothermal vent at L60 serves a different purpose (precedent for unexpected life) and should not be confused with the thermal-irrelevance analogy.
- Does not address T5 (silence gap). L48 already has a strong T5 statement ("gap of specialization, not conspiracy"). Separate micro-plan if needed.

## Scope

**Edit:** `manuscript/00-front/summary.tex` — insert one paragraph after L44, before L46. No other lines touched.

**No other files touched.**

**Regenerate:** `docs/downloads/Relinquishment.html`

## Phases (3)

### Phase 0 — Pre-flight

```bash
cd ~/software/relinquishment

# Confirm current text at L44
grep -n 'The magnetosphere has been here for billions of years' manuscript/00-front/summary.tex
# expect line 44

# Confirm credibility checkpoint at L46
grep -n 'Every claim above is published' manuscript/00-front/summary.tex
# expect line 46

# Confirm no thermal bridge exists yet
grep -c 'collisionless' manuscript/00-front/summary.tex
# expect 0

# Confirm hovertip for collisionless plasma exists
grep -c 'collisionless plasma' build/hover-definitions.yaml
# expect 1
```

### Phase 1 — Edit

Insert the new paragraph into `manuscript/00-front/summary.tex` after the magnetosphere paragraph (L44, ending "...has been here for billions of years.") and before the credibility checkpoint (L46, starting "Every claim above is published...").

Leave a blank line before and after, matching the file's existing paragraph spacing.

### Phase 2 — Build + verify

```bash
cd ~/software/relinquishment

# New text present
grep -c 'collisionless plasma' manuscript/00-front/summary.tex              # expect 1
grep -c 'thermally noisy' manuscript/00-front/summary.tex                   # expect 1
grep -c 'thermal objection assumes' manuscript/00-front/summary.tex         # expect 1

# Credibility checkpoint still present (now shifted to ~L48)
grep -c 'Every claim above is published' manuscript/00-front/summary.tex    # expect 1

# "Nothing forbids" still present (now shifted to ~L50)
grep -c 'Nothing in known physics forbids' manuscript/00-front/summary.tex  # expect 1

# Build
make html

# Verifier
python3 build/verify-deep-links.py    # expect OK
```

**Smoke test:** Open HTML, navigate to "The Story Never Told" → "The White Hot Secret."

1. Scroll to magnetosphere paragraph ("...has been here for billions of years.")
2. **Next paragraph** names the thermal objection: "millions of degrees."
3. Reframe: "hot does not mean thermally noisy."
4. Credibility checkpoint follows: "Every claim above is published."
5. "Nothing in known physics forbids life" now feels earned, not asserted.
6. Reader continues to habitat → Possibility C → prediction naturally.

### Commit

```bash
git add manuscript/00-front/summary.tex docs/downloads/Relinquishment.html
git commit -m "Plan 0216: p2 thermal bridge — name the objection before 'nothing forbids life'

The hardest physics objection (temperature) was unaddressed at p2.
Inserted one paragraph distilled from p3's 'But It's Hot' section:
collisionless plasma, fluctuation spectrum quieter than kinetic temp.
Reader now earns 'nothing forbids life' instead of being told.

Eigenvalue: T3 PARTIAL→PASS for Jane, Pastor Mike. Rachel MISS→PARTIAL.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

## Eigenvalue assessment

**This is a ~45-word insertion. One paragraph. Distilled from the shipped p3 argument.**

| Persona | T3 Before (post-0217) | T3 After | Δ | Why |
|---|---|---|---|---|
| Chen | PASS (fixed by 0217) | PASS | Neutral | His fix was at p3 level |
| Reeves | PASS (fixed by 0217) | PASS | Neutral | Same |
| Arjun | PARTIAL→PASS (0217) | PASS | Neutral | Same |
| Yusuf | PASS (fixed by 0217) | PASS | Neutral | Same |
| Doctorow | PASS (fixed by 0217) | PASS | +slight | p2 bridge reinforces p3 |
| Jane | PARTIAL | **PASS** | +positive | The thermal paragraph gives her the breathing room. "Nothing forbids" now feels earned. |
| Pastor Mike | PARTIAL | **PARTIAL→PASS** | +slight | Extra paragraph = more time to absorb. His issue isn't temperature per se but the concept needing space. |
| Rachel | MISS | **PARTIAL** | +positive | If she reads p2 (likely), the thermal bridge prevents premature dismissal. Still not full PASS — she needs engagement depth. |
| Amir | MISS | MISS | Neutral | Engagement depth. Not fixable at p2. |

**F-mode check:**
- F4 (Impossible): Improves. The thermal objection was the primary F4 trigger at p2. Now named and answered.
- No regressions.

**C-violation check:** PASS. "Hot in a collisionless plasma does not mean thermally noisy" is published plasma physics. Works under all three possibilities.

## Acceptance

1. Thermal bridge paragraph present between magnetosphere paragraph and credibility checkpoint
2. "collisionless plasma" with `\hovertip{}` present
3. "thermally noisy" reframe present
4. Credibility checkpoint and "Nothing forbids" lines unchanged (just shifted down)
5. No other text in summary.tex modified
6. HTML builds clean, verifier passes

## Risks

- **Very low.** Single paragraph insertion. Published physics distilled to p2 level.
- **Reading level.** "Collisionless plasma," "kinetic temperature," "quantum states" — these are p2-level terms (12th grade science). The hovertip on "collisionless plasma" provides the p1-level explanation for readers who hover.
- **Kauffman hedge.** L42 already hedges Kauffman correctly ("Whether such networks explain the origin of life on Earth is debated. That they can form is not."). The thermal bridge paragraph does not reference Kauffman and does not need to.
- **Complementary to L139.** The Breakthrough section (L139) mentions "near absolute zero" for quantum computers. The new thermal bridge at L44 explains why the magnetosphere doesn't need that. The two passages complement each other — reader absorbs both.
