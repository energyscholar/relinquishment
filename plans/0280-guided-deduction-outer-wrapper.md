# Plan 0280: Guided Deduction as Outer Wrapper

## Origin

Bruce's insight (2026-04-29): The last sentence of the `guided deduction` tooltip —

> "It is what truth-telling looks like when the truth is classified and the classification will outlive everyone who knows it."

— is not merely defining a term. It defines **what the book is doing to the reader**. This sentence is the "outer wrapper" — the meta-frame that envelops the entire reading experience.

## The Recursion (Already Documented)

Three nested instances of guided deduction:
1. **Healer → Bruce** (2003-2006): questions, breadcrumbs, public literature in deliberate order
2. **Bruce → Argus** (2025): questions about pedagogy/physics/history, let the LLM follow threads
3. **Book → Reader** (now): presents evidence, maps blockers, builds ladder, lets reader follow

This recursion is explicit in `afterword.tex` / `pos34b-the-engine.tex` (lines 78-82, "The Recursion" section). But it appears LATE — after the reader has finished Part 3. The wrapper needs to be felt from OUTSIDE, not explained inside.

## What "Outer Wrapper" Means Architecturally

The book already IS guided deduction on the reader. Every structural choice embodies it:
- **Three Possibilities** = "I won't tell you which is true; you decide" (no disclosure, only sequence)
- **Progressive JPEG** = each pass adds resolution (the onHover p1→p2→p3 escalator)
- **The Stack chart** = properties accumulate; reader builds the concept bottom-up
- **Puzzles** = the reader DOES the deduction, not just reads about it
- **Silence gap argument** = the evidence is the absence; reader must see what isn't there
- **"The science stands regardless of which possibility is true"** = the legal structure of guided deduction (no classified info changes hands)

**Critical discovery:** The hook (`hook.tex`) already PERFORMS the wrapper without naming it:
- Line 34: "never revealing anything secret, only guiding him through published science in a deliberate sequence" — describes the method
- Line 36: "Guided deduction was how they squared the two." — names it
- Line 42: "why would a man with a [REDACTED] career spend two and a half years teaching a physicist public-domain science in a deliberate order?" — PERFORMS it (ends the hook with a question, which IS guided deduction on the reader)

The book is already doing the wrapper. The reader just doesn't know it's happening to THEM, not only to Bruce.

## Current State

| Location | What Exists | Problem |
|----------|-------------|---------|
| Hook (line 34-36) | Describes AND performs guided deduction | Presents it as Healer→Bruce, not Book→Reader |
| Hook (line 42) | Closing question IS guided deduction on reader | Reader doesn't recognize the method being used ON them |
| Tooltip (`hover-definitions.yaml`) | The wrapper sentence lives here | Only fires on hover — many readers won't see it |
| Summary (line 261) | "Their solution was guided deduction..." + `\hovertip` | Framed as Possibility C only |
| Afterword ("The Recursion") | "Now the book uses guided deduction on you" | Appears too late; payoff without setup |
| Spine (`why-relinquish.tex` line 111) | Full explanation of the method | In Part 3 (unconstrained) — many readers won't reach it |

**The gap:** The book performs guided deduction on the reader from page 1 but only TELLS the reader this is happening in the afterword. There is no early marker that makes the method visible — or at least retrospectively recognizable — for the reading experience itself.

## The Paradox

Guided deduction works BECAUSE the student doesn't know the full shape until they arrive at the conclusion. Explaining it early = breaking it. The wrapper must be:
- **Invisible on first reading** (feels like a natural sentence)
- **Luminous on re-reading** (after The Recursion, reader goes back and sees it)
- **Functional** (actually frames the reading experience, not just decorative)

This is why the phase space has many local minima. Every placement trades off visibility vs. subtlety.

## Option Landscape (Early Marker)

### Option A: End of The Stack — Threshold Sentence

**Location:** After "Might nature have already learned to use that property, as it did the others?" (line 59), before the italic closing instruction (line 62).

**Text:** *What follows is not a disclosure. It is a sequence.*

**Strengths:**
- Stark, minimal, threshold-like — the reader crosses it into the narrative
- Under Possibility C, LITERALLY TRUE: the book is not a disclosure (no classified info), it IS a sequence (deliberate order of published science)
- "Disclosure" is a p1-accessible word. "Sequence" is simple.
- Holds under all three possibilities (even under A, the book is still a sequence of evidence)
- Echoes the tooltip without using the term "guided deduction"

**Weaknesses:**
- Creates a second closing moment in The Stack (currently closes with the reading instruction)
- Reader may read it as a bland disclaimer rather than a structural statement
- "Disclosure" has legal connotation the reader doesn't yet have context for

**Retroactive payoff:** After The Recursion, the reader re-reads this sentence and realizes: "Oh — that wasn't a disclaimer. It was the DESIGN STATEMENT. The book was telling me its method and I didn't notice."

### Option B: End of Hook — After the Closing Question

**Location:** After line 42 ("What could explain that?"), before the italic about "That was the shortest version."

**Text:** *What follows is not a disclosure. It is a sequence.*

**Strengths:**
- Placed right after the hook's closing question, which IS guided deduction being performed
- The reader just read ABOUT the method (line 34-36) and just EXPERIENCED it (line 42's question)
- The wrapper sentence names what's been happening without explaining it
- Maximum early exposure (this is the first page)

**Weaknesses:**
- The hook is already dense — adding a cryptic sentence may lose the reader
- Reader hasn't yet read The Stack, so "sequence" doesn't resonate with the technology-stack concept
- The hook's current flow (explosive narrative → closing question → "That was the shortest version") has strong rhythm; inserting here may break it

### Option C: Woven Into Hook Line 34

**Current:** "never revealing anything secret, only guiding him through published science in a deliberate sequence."

**Revised:** "never revealing anything secret, only guiding him through published science in a deliberate sequence — the same sequence you are about to follow."

**Strengths:**
- Direct. Unmissable. Tells the reader explicitly.
- Creates immediate dramatic irony (reader knows what's being done to them)

**Weaknesses:**
- BREAKS the guided deduction by naming it. The student now knows the shape of the lesson before it begins.
- Feels metafictional / clever in a way that may alienate general readers
- Violates the constraint that guided deduction shouldn't be explained, only experienced

**Verdict:** Probably too explicit. Noted but not recommended.

### Option D: The Tooltip IS the Early Marker (No New Text)

**Argument:** The `\hovertip{guided deduction}` in the summary (line 261) fires the tooltip for hovering readers. The tooltip's last sentence IS the wrapper. The book's own interaction layer (onHover = p-level escalator) delivers the wrapper at the moment the reader is curious enough to hover.

Non-hovering readers don't get the early marker. But: guided deduction doesn't demand that every student notices the method. Some notice. Some don't. That IS the design. The method is visible to those who look.

**Under this option:** Phase 2 (Recursion payoff) is the only change. The wrapper sentence surfaces in body text at the moment of maximum retroactive impact.

**Strengths:**
- Zero new text in the front matter. No risk of breaking existing rhythm.
- The onHover delivery mechanism IS guided deduction in miniature (you have to reach for it)
- Philosophically consistent: the wrapper reveals itself only to engaged readers

**Weaknesses:**
- Print readers get the tooltip as a footnote — less impactful
- Hover-to-discover is unreliable; many online readers won't hover
- Misses the retroactive-recognition effect entirely for passive readers

### Option E: Stack Opening Echo — "You Decide" / "You Follow"

**Current Stack opening (line 9):** "What you just read has three possible explanations. The science that follows is true under all three. You decide."

**Add before Stack closing (line 62):** "You follow the sequence. We follow the science."

**Strengths:** Echo structure (open with "you decide", close with "you follow")

**Weaknesses:** Forced. "We follow the science" has unfortunate pandemic-era connotation. Not recommended.

### Option F: The Hook's Closing Question IS Already the Marker

**Argument:** Line 42 — "why would a man with a [REDACTED] career spend two and a half years teaching a physicist public-domain science in a deliberate order? What could explain that?" — is ALREADY the wrapper sentence in question form. The reader carries this question into the book. When they reach The Recursion, the answer arrives: "It is what truth-telling looks like when the truth is classified."

The Q (hook) → A (afterword) structure IS the wrapper. It's already built. The gap is only that the afterword answer doesn't land with the tooltip's precision.

**Under this option:** Phase 2 only. Add the tooltip sentence to The Recursion as the answer to the hook's question. The wrapper = Q→A spanning the entire book.

**Strengths:**
- The architecture already exists. Minimum intervention.
- The hook question is powerful and memorable
- The Recursion answer ("It is what truth-telling looks like...") completes the arc

**Weaknesses:**
- The Q→A gap is the ENTIRE BOOK. Many readers won't hold the hook question in memory that long.
- No intermediate reinforcement between hook and afterword
- Relies on the reader remembering a specific sentence from page 1 when they reach the last chapter

## Recommendation After Annealing

**Primary: Option A (Stack threshold) + Phase 2 (Recursion sentence)**

Three-touch-point architecture:
1. **Hook line 42:** The question plants guided deduction as EXPERIENCE (already exists)
2. **Stack closing:** "What follows is not a disclosure. It is a sequence." (NEW — 8 words)
3. **Recursion:** "It is what truth-telling looks like when the truth is classified and the classification will outlive everyone who knows it." (NEW — surfaces the tooltip)

The reader gets: a question they carry (hook) → a threshold they cross without understanding (Stack) → a revelation that illuminates both retroactively (Recursion).

**Alternate: Option D + Phase 2 (minimal intervention)**

If Bruce judges that adding text to The Stack risks breaking its rhythm, Option D (tooltip IS the marker) + Phase 2 (Recursion sentence) achieves the wrapper with ONE new sentence total.

**Decision for Bruce:** The choice between A and D is a bet on how much the reader needs to be primed. A = prime them subtly. D = trust the method, let it reveal itself to those who look.

## Phase 2: Late Confirmation (All Options)

Regardless of early-marker choice, add to The Recursion section.

**Location:** `afterword.tex` / `pos34b-the-engine.tex`, after line 82 ("Three levels of the same pedagogy. The method propagates because it works.")

**Add:**

> It is what truth-telling looks like when the truth is classified and the classification will outlive everyone who knows it.

This surfaces the tooltip's wrapper sentence into body text at the exact moment the reader has finished the entire book and been told explicitly that guided deduction was used on them. Maximum retroactive impact.

## Phase 3: Structural Audit

Verify that every major structural choice embodies guided deduction (sequence without disclosure). Specifically check:

- [ ] Does the Stack chart progress bottom-up without STATING what the "?" column IS?
- [ ] Do the Three Possibilities refrain from favoring one? (Check for inadvertent weighting)
- [ ] Does the onHover system escalate WITHOUT the upper layers contradicting lower layers?
- [ ] Do puzzles require the reader to DERIVE rather than recognize?
- [ ] Does any chapter TELL the reader the conclusion before they've built it from evidence?

Any violation of guided-deduction structure = a leak in the wrapper. Fix means: restructure so the reader derives rather than receives.

## Acceptance Criteria

1. A reader who finishes the book and re-reads the early marker experiences retroactive recognition: "It was doing this to me the whole time."
2. The tooltip wrapper sentence appears in body text exactly once — in The Recursion.
3. No front-matter text uses the TERM "guided deduction" (that would be disclosure, not deduction). The early marker (if Option A) describes the EXPERIENCE without naming it.
4. The structural audit finds zero instances where the book tells-before-the-reader-derives within the p1/p2 layer. (p3 may explain directly — that's the unconstrained layer.)

## Constraints

- Must hold under all three possibilities (the wrapper IS possibility-agnostic)
- Must not violate p1/p2 reading levels (8th/12th grade)
- Early marker must be SHORT (one sentence max)
- Must not make the book feel "clever" or self-referential in a way that alienates — it should feel like good teaching, not metafiction
- Must not break existing front-matter rhythm

## Implementation

- **Phase 1 (if Option A):** 1 sentence inserted in `the-stack.tex`
- **Phase 1 (if Option D):** No change
- **Phase 2:** 1 sentence added to `afterword.tex` AND `pos34b-the-engine.tex`
- **Phase 3:** Audit pass, may produce 0-3 small fixes

Estimated scope: Small. One Generator session.

## Decision Required

Bruce chooses early-marker option (A, B, D, or F) before Generator executes.

## Handoff Prompt (after Bruce decides)

> You are the Generator. Read plan `/home/bruce/software/relinquishment/plans/0280-guided-deduction-outer-wrapper.md`. Bruce chose Option [X] for the early marker. Implement Phase 1 (Option [X]) and Phase 2. For Phase 3, perform the structural audit checklist and report findings — fix only if violations are clear and small. Do not restructure chapters.
