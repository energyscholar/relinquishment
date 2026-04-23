# Plan 0107: DN Compliance Fixes — Minimum Effective Qualification

**Status:** COMPLETE (verified S63 audit)
**Anneal:** Large → Medium → Small
**Reading level:** p1=8th grade, p2=12th grade, p3=unconstrained
**Principle:** Minimum words, maximum protection. The three-possibilities framework IS the hedge. Fix only what it doesn't cover.

## Context

Full-manuscript DN audit (Session 48) identified six violation patterns. Most are covered by the existing three-possibilities architecture. Two categories are NOT covered:

1. **Present-tense reality claims** — sentences that step outside the story frame and assert something about the world right now. The reader's "might be fiction" flag drops.
2. **Named real people attributed to speculative criminal acts** — the story frame protects narrative claims but does NOT protect attributing unauthorized removal of classified technology to named, living public figures.

Bruce's design decision: the narrative tells the C-version in declarative voice, with three-possibilities qualifiers at key moments. This is intentional and stays. We fix only the gaps.

## Tier 1: Present-Tense Reality Claims (p1/p2)

### Fix 1a: "It is not empty" (summary.tex, White Hot Secret section)

**Current:** "The Flat has been wrapped around this planet, in the magnetosphere, for billions of years. It is not empty."

**Fix:** Rephrase to attribute rather than assert. Options (Generator picks best fit in context):
- "This book argues it is not empty."
- "The implication of this book is that it is not empty."
- "If the story is true, it is not empty."

**Constraint:** Keep the force. This sentence should land. It just can't be an unqualified assertion about present reality.

### Fix 1b: "Two-dimensional worlds harbor life" (summary.tex, White Hot Secret)

**Current:** Standalone declaration after Lane's quote.

**Fix:** This is the content of Lane's secret. Frame it as such. E.g.:
- "The secret: two-dimensional worlds harbor life."
- "What the sequence points to: two-dimensional worlds harbor life."

The sentence is already introduced by "The published science, followed in the right sequence, points there plainly enough." So it reads as conclusion-of-the-sequence, not assertion-about-reality. A light touch may suffice — just ensure the reader connects it to "points there" rather than reading it as a freestanding factual claim.

### Fix 1c: "They are habitats" (summary.tex, White Hot Secret)

**Current:** "The implication is what's not published: these substrates are not just interesting physics. They are habitats."

**Fix:** Already partially protected by "The implication is what's not published" — this labels it as inference. Consider: "The implication is what's not published: these substrates are not just interesting physics. They are — or could be — habitats." OR leave as-is; "The implication is" may be sufficient framing. Generator judgment.

### Fix 1d: "it will be because it was ready to be found" (summary.tex, Why This Matters)

**Current:** "If something is ever found, it will be because it was ready to be found."

**Fix:** Cut or qualify. This is an unfalsifiable claim — if found, it chose to be found; if not found, it chose to hide. Options:
- Cut the sentence entirely. The preceding sentence ("But the clock is running, and the claim is falsifiable") is stronger without it.
- Qualify: "If something is ever found, it may be because it was ready to be found."

**Preference:** Cut. The paragraph is tighter without it.

### Fix 1e: "first real account" (hook.tex)

**Current:** "This may be the first real account of someone who faced that choice and let go."

**Fix:** "This may be the first account of someone who faced that choice and let go."

Remove "real." The word smuggles truthfulness into an otherwise well-qualified sentence. "May be" does the hedging work; "real" undercuts it.

## Tier 2: Named Scientists Protection

### The Logic

No named scientist has been contacted. Contact would provide zero information because the response is overdetermined:
- Under A: "I was never in a classified program" (true — no program existed)
- Under B: "I was never in a classified program" (true enough — story is exaggerated)
- Under C: "I was never in a classified program" (oath-bound — confirmation impossible)

Denial or silence is the predicted response under all three possibilities. This means neither denial nor silence provides evidence for or against any possibility.

### Fix 2a: Blanket Scientist-Protection Passage

**Location:** Early in the book. Two candidates:
- **Option A:** In pos01-three-possibilities.tex, new subsection after "The Author's Position" and before "The Substrate." Title: something like "A Note on Names."
- **Option B:** In the introduction (introduction.tex), as a structural note.
- **Recommendation:** pos01, because that's where the three-possibilities framework is established at p3 level. The protection belongs with the framework.

**Content (~100-150 words). Must include:**

1. Scientists are named because their published work converges on the capability described. The convergence is documented — every citation is public and checkable.
2. Under Possibilities A and B, their inclusion reflects the author's pattern-matching from public information, not evidence of classified involvement. Under A, none of them were in a classified program. The team composition is a product of Bruce's reconstruction, not of underlying truth.
3. No named scientist has confirmed participation in any program described in this book.
4. This is expected. Under A, they would deny because there is nothing to confirm. Under B, they would deny because the story is exaggerated. Under C, they would deny because they are oath-bound. Denial and silence are the predicted response under all three possibilities. Neither constitutes evidence for or against any possibility.
5. The author acknowledges that naming real people in connection with speculative claims carries weight. He does so because the convergence of their published work is the evidence — and evidence requires names.

**Constraint:** This passage must not read like a legal disclaimer. It must read like honest scholarship — which is what it is.

### Fix 2b: Reinforcement at Key Moments (light touch)

At the first mention of each scientist by name in a speculative context (not when citing their published work), add a light marker. NOT "under Possibility C" every time — just occasional reminders. E.g.:

- First mention of the team roster: "According to this account, the team included..."
- Wolfram job offer (pos31): already well-framed with "Evidentiary limitation" notes
- Patrick Ball nexus (pos19): "The proposition holds that..." (already present in places)

**Generator should audit** the first substantive mention of each named scientist and ensure at least one of these markers is present within the same paragraph. Do NOT add markers to every mention — only the first substantive one per chapter.

**Named scientists requiring this check:** Wolfram, Kauffman, Hasslacher, Hillis, Freedman, Joy, Gell-Mann. (Patrick Ball is excluded — the book describes only his public record, not speculative classified involvement.)

## Tier 3: Incremental Improvements (Next Editing Pass — NOT this plan)

These are noted for future plans, not executed here:

- **pos03 rewrite:** Third-person omniscient → Bruce-recounting-what-he-was-told. Already flagged with editorial TODO.
- **Three-then-four options transparency:** Consider adding structural acknowledgment in one of pos06/pos22/pos27.
- **Motive attribution:** Soften "the COWS believed" / "likely informed" in pos25, pos11. Add "I infer" or "according to this account."
- **Circular reasoning (pos10):** Anyon proof via TQNN existence. Consider naming the circularity explicitly.
- **"Precisely matches" (pos20):** → "is consistent with." Temporal proximity ≠ verification.

## Annealing Strategy

### Large pass: Architecture
- Decide exact placement of the blanket scientist-protection passage
- Draft the passage (~150 words), over-writing freely
- Draft all Tier 1 replacement text
- Read each fix in context (surrounding paragraphs) to verify tone match

### Medium pass: Precision
- Tighten blanket passage to ~100-120 words
- Verify each Tier 1 fix is minimum-words
- Verify no fix introduces new DN violations
- Check that the blanket passage works under all three possibilities
- Audit first mention of each named scientist — add light markers only where missing

### Small pass: Polish
- Read p1 start to finish
- Read p2 start to finish
- Read pos01 start to finish
- Verify all `\label{}` tags preserved
- `make html` clean
- Verify word counts haven't grown significantly

## Acceptance Criteria

- [ ] "It is not empty" softened without losing force
- [ ] "Two-dimensional worlds harbor life" clearly attributed to the claim/sequence
- [ ] "it will be because it was ready to be found" cut or qualified
- [ ] "first real account" → "first account"
- [ ] Blanket scientist-protection passage present in pos01
- [ ] Passage includes: convergence logic, A/B/C predictions for denial, no confirmation received
- [ ] Passage does NOT read like a legal disclaimer
- [ ] First substantive mention of each named scientist has framing marker
- [ ] No existing `\label{}` tags broken
- [ ] `make html` clean
- [ ] Total added words across all fixes < 250

## Commit

One commit: `Plan 0107: DN compliance — minimum effective qualification`
