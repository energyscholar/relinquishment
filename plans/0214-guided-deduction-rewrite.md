# Plan 0214 — Rewrite "Getting the Record Out" to match letter-quality prose

## Status
Ready for Generator.

## Problem

The "Getting the Record Out" section (`manuscript/spine/why-relinquish.tex:104-126`) describes Operation Guided Deduction in a way that is significantly weaker than the same description in Bruce's personal letters to Genevieve (2026-04-16) and Linda (undated). The letters were written in Bruce's direct voice for people he trusts. The book version reads like a committee wrote it.

**Book (current):**
> "Find someone with the right scientific background — physics, computation, pattern recognition. Someone with the memory to hold five fields simultaneously. Someone naturally inclined to publish what they learned without being asked."

**Linda letter:**
> "You select a civilian with the right cognitive profile and no institutional ties. Over years you ask him questions that guide him to read the public literature in an order that eventually lets him see the convergence for himself. You give him no documents, no written reading list, and then you leave. He derives the result from openly published science and publishes it as his own work. A teacher who asks questions commits no crime. A student who reasons from public sources has received nothing classified. The trail is clean. The science gets out."

### Why the letters are better

1. **Method before person.** The book jumps to a shopping list of traits. The letters explain the *method* first — Socratic teaching, the legal logic — and the person falls out naturally.
2. **The legal logic is explicit and load-bearing.** "A teacher who asks questions commits no crime" — this is the sentence the reader needs. The book buries a weaker version ("A teacher who asks the right questions commits no crime. A student who derives conclusions from public science has received nothing classified.") at the end of a paragraph that's already lost the reader in a trait list.
3. **"The trail is clean. The science gets out."** — Two sentences that land like a punch. The book has "The trail is clean." but not the payoff.
4. **No shopping list.** The book lists cognitive traits like a job posting. The letters describe a method, and the traits are implied by the method's requirements.
5. **The Socratic anchor.** The letters name the method's lineage: "a close relative of Socratic teaching, and of how advisers have always taught graduate students by asking the next right question." This grounds the method in something every educated reader recognizes.

## Proposed edit

Replace `why-relinquish.tex` lines 107-117 (the "Getting the Record Out" section body, keeping the `\section*` and `\label`).

**OLD (lines 107-117):**
```latex
Under Possibility~C, the COWS had a second problem. Custodianship was solved. The record was not.

What they had discovered needed to reach the outside world --- not the technology itself, but the knowledge that it existed and had been relinquished. Every team member had signed NDAs. Direct publication was a crime. The intent was permanent classification. The COWS already knew what it would take an outsider twenty years to learn: the scientific community was not going to connect the domains on its own. The disciplines would sit in their silos forever --- condensed matter physics, complexity biology, topology, quantum computing, and neuroscience, each with its own journals and no one assigned to the intersection. The \hovertip{bridges} were never coming.

They needed someone outside the classification regime. Someone who had never signed anything.

The solution was guided deduction. Find someone with the right scientific background --- physics, computation, pattern recognition. Someone with the memory to hold five fields simultaneously. Someone naturally inclined to publish what they learned without being asked. Teach them only published science, in a deliberate sequence, and let them arrive at the conclusions independently. A teacher who asks the right questions commits no crime. A student who derives conclusions from public science has received nothing classified. The trail is clean.

The guided deduction was one phase of a larger effort. The Relinquishment itself spanned nearly a decade --- from the initial plan around 1997 to the handover in 2006 --- and required a top-tier operator and several overlapping teams. The Guided Deduction teaching phase began in 2003. It took three years. The student then spent twenty years confirming what the operator had already known: the bridges were not going to build themselves, the NDA holders were not going to speak, and the record was not going to emerge through official channels. Ever.

This book is one result. A mathematics paper is another. More papers are coming.
```

**NEW:**
```latex
Under Possibility~C, the COWS had a second problem. Custodianship was solved. The record was not.

What they had discovered needed to reach the outside world --- not the technology itself, but the knowledge that it existed and had been relinquished. Every team member had signed NDAs. Direct publication was a crime. The intent was permanent classification. And the COWS already knew what it would take an outsider twenty years to learn: the scientific community was not going to connect these domains on its own. The disciplines would sit in their silos forever --- condensed matter physics, complexity biology, topology, quantum computing, and neuroscience, each with its own journals and no one assigned to the intersection. The \hovertip{bridges} were never coming.

The solution was \hovertip{guided deduction} --- a method as old as Socratic teaching, and a close relative of how advisers have always taught graduate students: by asking the next right question. You select a civilian with the right cognitive profile and no institutional ties. Over years, you ask him questions that guide him to read the public literature in an order that eventually lets him see the convergence for himself. You give him no documents, no written reading list, and then you leave. He derives the result from openly published science and publishes it as his own work. A teacher who asks questions commits no crime. A student who reasons from public sources has received nothing classified. The trail is clean. The science gets out.

The Relinquishment itself spanned nearly a decade --- from the initial plan around 1997 to the handover in 2006 --- and required a top-tier operator and several overlapping teams. The \hovertip{guided deduction} teaching phase began in 2003. It took three years. The student then spent twenty years confirming what the operator had already known: the bridges were not going to build themselves, the NDA holders were not going to speak, and the record was not going to emerge through official channels. Ever.

This book is one result. A mathematics paper is another. More papers are coming.
```

### What changed

1. **Removed "They needed someone outside the classification regime. Someone who had never signed anything."** — Redundant with the new "select a civilian... no institutional ties" phrasing, which is stronger because it's part of the method description rather than a standalone lament.
2. **Replaced the trait shopping list** with the letter's method-first description: Socratic anchor → select civilian → ask questions over years → no documents → he publishes → legal logic → payoff.
3. **Added "The science gets out."** — The payoff sentence the book was missing.
4. **Added Socratic teaching anchor** — grounds the method in something every reader recognizes.
5. **Changed "guided deduction" to `\hovertip{guided deduction}`** — the term already exists in `hover-definitions.yaml`. First-fires here (or wherever it first appears in document order).
6. **Kept** the final two paragraphs nearly intact — the decade-spanning timeline and "This book is one result" are already strong.
7. **Preserved** the `\hovertip{bridges}` on the "bridges were never coming" line.

### What's preserved from the book that the letters don't have

- The NDA/classification framing (important context for readers who don't know Bruce personally)
- The five-field silo list (pedagogically load-bearing in the book, unnecessary in a personal letter)
- "The bridges were never coming" (one of the best sentences in the chapter)
- The timeline paragraph (1997-2006, three years, twenty years confirming)
- "This book is one result" closing

## Eigenvalue assessment

**This is a prose-quality improvement, not a content change.** The same information is communicated. The method description is clearer and lands harder.

| Persona | Before | After | Δ |
|---|---|---|---|
| Chen (physicist) | PASS — understands the method | PASS — Socratic anchor resonates (he's taught grad students this way) | +slight |
| Reeves (phil-of-science) | PASS | PASS — Socratic reference is epistemically precise | +positive |
| Arjun (CS) | PASS | PASS — cleaner prose, less padding | +slight |
| Doctorow | PASS | PASS — method-first is better journalism | +slight |
| Jane (generalist, L1) | PASS but trait list is dense | PASS — method reads as a story, not a job posting | +positive |
| Rachel (working parent) | PASS | PASS — tighter, less to wade through | +slight |
| Pastor Mike | PASS | PASS | Neutral |
| Amir | PASS | PASS | Neutral |
| Yusuf | PASS | PASS | Neutral |

**F-mode check:** No triggers. The Socratic anchor slightly reduces F-crank (established pedagogical method vs. spy-novel recruitment).

**C-violation check:** PASS. "Under Possibility C" is the opening frame. Method description is generic — works under all three possibilities.

**Verdict: stable eigenvalue, positive across readers who engage with the method.** Jane benefits most (story vs. list). Chen and Reeves benefit from the Socratic anchor.

**Distillation chain note:** The `\hovertip{guided deduction}` tooltip in `hover-definitions.yaml` is the *best* version across all reading depths: "It is what truth-telling looks like when the truth is classified and the classification will outlive everyone who knows it." The p3 rewrite must not be weaker than this tooltip. The two complement each other: the tooltip gives the *why*, the chapter gives the *how*.

## Scope

**Edit:** `manuscript/spine/why-relinquish.tex` — lines 107-117 only (section body).

**No other files touched.** The bridge version (`pos06-the-secret.tex`) does not contain this section.

**Regenerate:** `docs/downloads/Relinquishment.html`

## Phases (3)

### Phase 0 — Pre-flight

```bash
cd ~/software/relinquishment

# Confirm current text
grep -n 'Find someone with the right scientific background' manuscript/spine/why-relinquish.tex
# expect line 113

# Confirm Socratic not already in this file
grep -c 'Socratic' manuscript/spine/why-relinquish.tex
# expect 0

# Confirm hovertip for guided deduction exists
grep -c 'guided deduction' build/hover-definitions.yaml
# expect 1

# Confirm "The science gets out" not already present
grep -c 'The science gets out' manuscript/spine/why-relinquish.tex
# expect 0

# Confirm bridge version does NOT have this section
grep -c 'Getting the Record Out' manuscript/bridge/pos06-the-secret.tex
# expect 0
```

### Phase 1 — Edit

Replace the section body in `manuscript/spine/why-relinquish.tex` (lines 107-117) with the NEW text from the Proposed Edit above. Keep `\section*{Getting the Record Out}` and `\label{spine:wr-getting-the-record-out}` unchanged. Keep lines 119-126 (the Custodian's daily work paragraphs) unchanged.

### Phase 2 — Build + verify

```bash
cd ~/software/relinquishment

# New text present
grep -c 'Socratic teaching' manuscript/spine/why-relinquish.tex           # expect 1
grep -c 'The science gets out' manuscript/spine/why-relinquish.tex        # expect 1
grep -c 'no institutional ties' manuscript/spine/why-relinquish.tex       # expect 1

# Old text gone
grep -c 'Find someone with the right scientific background' manuscript/spine/why-relinquish.tex  # expect 0
grep -c 'They needed someone outside the classification regime' manuscript/spine/why-relinquish.tex  # expect 0

# Hovertip on guided deduction
grep -c 'hovertip{guided deduction}' manuscript/spine/why-relinquish.tex  # expect 2

# Build
make html

# Verifier
python3 build/verify-deep-links.py    # expect OK

# Word count delta (should be small — roughly neutral, slight compression)
```

**Smoke test:** Open HTML, expand "Why Relinquish?", scroll to "Getting the Record Out."

1. Opens with "Under Possibility C, the COWS had a second problem."
2. Socratic teaching anchor appears before method description.
3. "You select a civilian... Over years, you ask him questions..." — method reads as a story.
4. "A teacher who asks questions commits no crime." — legal logic is clear.
5. "The trail is clean. The science gets out." — payoff lands.
6. No trait shopping list.
7. "guided deduction" has hovertip styling.
8. Timeline paragraph and "This book is one result" closing unchanged.

### Commit

```bash
git add manuscript/spine/why-relinquish.tex docs/downloads/Relinquishment.html
git commit -m "Plan 0214: rewrite 'Getting the Record Out' — method-first, letter-quality prose

The guided-deduction description read like a job posting (trait list).
Rewrote to match the quality of Bruce's personal letters: Socratic
teaching anchor, method-first description, explicit legal logic,
'The science gets out' payoff. Same information, clearer delivery.

Eigenvalue: stable across 9 personas. Jane and Chen benefit most.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

## Acceptance

1. "Socratic teaching" appears in the section (method anchored)
2. "The science gets out" appears (payoff present)
3. No trait shopping list ("Find someone with the right scientific background" gone)
4. "A teacher who asks questions commits no crime" retained
5. `\hovertip{guided deduction}` present
6. HTML builds clean, verifier passes
7. Section reads naturally in browser

## Risks

- **Very low.** Single-section rewrite in one file. Same information, better prose.
- **\hovertip{guided deduction} dedup.** Plan 0213 (per-chapter re-triggering) has shipped. Both `\hovertip{guided deduction}` occurrences are in the same chapter, so the second gets italic-only styling — correct behavior (first fires the tooltip, second is emphasis).
- **"You" voice.** The letter uses second person ("You select a civilian..."). This is a slight register shift from the chapter's third-person expository voice. Acceptable: the "you" here is generic/instructional ("you" = anyone designing this operation), not addressing the reader directly. Same register as "You cannot recall a species" (line 22) already in this chapter.
