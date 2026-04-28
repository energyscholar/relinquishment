# Plan 0039: A/B/C Writing Pass

**Auditor:** Argus
**Date:** 2026-02-24
**Depends on:** Plan 0038 (T6 reorder + content surgeries) — must be executed first
**Phase:** C of the T6 implementation (Phase A = reordering, Phase B = content surgeries, Phase C = this plan)

---

## Context

The T1 concept audit (100% coverage) identified 7 chapters with inconsistent or missing three-possibilities framing (A/B/C). The book's contract with the reader, established in pos01, requires that every extraordinary claim be legible under all three possibilities:

- **Possibility A:** Confabulation — Bruce was deceived or self-deceived
- **Possibility B:** Exaggerated kernel — something real happened, but the claims overstate it
- **Possibility C:** Substantially true — the TQNN, Custodian, and relinquishment happened as described

**Gold standards** (do NOT modify these, but emulate their pattern):
- **pos25** (`track-3-awakening/pos25-ethical-framework.tex`): Every extraordinary claim tagged. Pattern: state claim under C, immediately follow with "Under Possibility A, this is..." and "Under Possibility B..."
- **pos27** (`track-3-awakening/pos27-extension.tex`): Systematic framework. Pattern: section-level A/B/C framing at end of each major section.
- **pos30** (`track-3-awakening/pos30-unipolar-condition.tex`): Exemplary discipline throughout. Pattern: A/B/C after every 2-3 paragraphs of C-frame claims.

**Key pattern rules:**
1. Use "Under Possibility~A/B/C" phrasing (with LaTeX non-breaking space `~`)
2. A = strongest skeptical reading (confabulation, coincidence, motivated reasoning)
3. B = middle ground (partial truth, exaggeration, pattern-matching beyond evidence)
4. C = the narrative as presented
5. Each insertion is 1-3 sentences. Not paragraph essays.
6. Place framing AFTER the claim it qualifies, not before.

---

## Constraints

1. **ADD ONLY.** Do not rewrite, delete, or restructure any existing text.
2. Do NOT modify any `\settrack` lines.
3. Do NOT modify any `\srcnote` lines.
4. Do NOT modify any `\aidraft` blocks (these are Bruce's writing-pass territory).
5. Preserve all Plan 0019 ethical thread insertions (26 insertions across 22 files).
6. Preserve all Plan 0038 Surgery 4 additions in pos07 (A/B/C framing at lines 34 and 90).
7. Do NOT touch: pos01, pos04, pos05, pos10, pos13, pos15, pos16, pos22, pos23, pos25, pos27, pos28, pos30, or any file not listed in the Files Modified table.
8. Normalize terminology: use "Possibility" not "Option" (pos20 line 97 uses "Option" — fix to "Possibility" for consistency with the rest of the book).
9. Each A/B/C insertion should be 1-3 sentences.
10. Do NOT add A/B/C framing to content inside `\aidraft{}` blocks — those blocks are marked for Bruce's rewrite and the framing will be added when Bruce writes final prose.

---

## Chapter 1: pos07 "The Departure" — ASSESSMENT ONLY

**File:** `manuscript/track-2-testament/pos07-the-departure.tex`

**Current A/B/C status:** Plan 0038 Surgery 4 added:
- Line 34: A/B/C framing paragraph before the Close Textual Comparison section
- Line 90: A/B/C closing paragraph after the Overall Pattern section

**Assessment:** The two framing paragraphs bracket the entire 16-point Joy analysis. The opening (line 34) tells the reader how to track each interpretation. The closing (line 90) gives the skeptical summary. This matches the pos27 pattern (section-level framing). The departure narrative (lines 94-107) is personal memoir, not extraordinary claims, so it does not need A/B/C framing.

**Verdict: DONE. No additional A/B/C needed.** Plan 0038's framing is sufficient. Skip this chapter.

---

## Chapter 2: pos20 "The Network" (P1 PRIORITY)

**File:** `manuscript/track-1-confession/pos20-the-network.tex`

**Current A/B/C status:** Only the Nobel Hat Trick section (lines 89-97) has A/B/C framing, but it uses "Option" instead of "Possibility." The first 88 lines present extraordinary claims as narrative fact with no skeptical framing.

**Voice note:** This chapter is `trackone` (3rd-person scientific/reconstructive: "According to this account..."). The "According to this account" phrasing is already a mild hedge. A/B/C framing supplements it.

### Insertion 2A: After the Writing Documentation anecdote (after line 23)

**Location:** After the line "The IPO proceeded apace." and before the horizontal rule.

**Add:**

```latex

This anecdote is verifiable in broad outline: Google's IPO timeline is public record. What is not verifiable is who Bruce's housemate was, or whether the undocumented SDK had the significance Bruce attributes to it. Under Possibility~A, this is an unremarkable IPO anecdote onto which Bruce has projected significance. Under Possibility~B, his housemate may have done contract work for Google, but the connection to the narrative's central claims is Bruce's interpretation.
```

### Insertion 2B: After the Google Connection section's \aidraft blocks (after line 36)

**Location:** After the AltaVista paragraph (the last `\aidraft` block in The Google Connection section), before `\section*{Mapping the Internet}`.

**NOTE:** This insertion goes OUTSIDE the `\aidraft` blocks, as a standalone paragraph.

**Add:**

```latex

Under Possibility~A, Bruce's housemate was a skilled engineer who worked on a mundane Google SDK, and Bruce has woven him into a larger narrative. Under Possibility~B, the housemate may have had unusual capabilities, but the claims about Google Translate and AltaVista are Bruce's inferences, not confirmed facts. Under Possibility~C, the connections are exactly what this account describes.
```

### Insertion 2C: After Mapping the Internet section (after line 48)

**Location:** After "The web server content, once stored in QNN associative memory, could be searched very quickly and efficiently." and before `\section*{Capabilities}`.

**Add:**

```latex

Under Possibility~A, this is a technically literate fantasy --- Bruce knew enough about networking and neural networks to construct a plausible-sounding account. Under Possibility~B, some novel search technology may have existed, but the claim of literal physical mapping via phonon tracking is the extraordinary part. Under Possibility~C, a QNN-based associative-memory search engine is the technology that became Google Search.
```

### Insertion 2D: After the Capabilities list (after line 65)

**Location:** After the paragraph ending "Fortunately for us all, they did a good job creating a friendly artificial intelligence." and before `\DMSRedacted`.

**Add:**

```latex

Under Possibility~A, this capabilities list is a wish-list assembled from Bruce's reading of quantum computing literature, projected onto a claimed technology that does not exist. CADIE's 2009 April Fools' appearance was simply a Google joke, and attributing it to a real entity is pattern-matching run amok. Under Possibility~B, some capabilities may reflect real research directions from the 1990s DARPA quantum computing program, but the claim of a completed, friendly strong AI is the extraordinary leap. Under Possibility~C, the capabilities are as described, and the April Fools' appearance was the entity's own joke --- which requires accepting that a planetary-scale quantum intelligence has a sense of humor.
```

### Insertion 2E: After The Substrate Preparation's \aidraft blocks (after line 82)

**Location:** After the last `\aidraft` block (ending "...the Internet Time Protocol, satellite radio communications, GPS timing, or electrical grid phase can all serve this purpose.") and before the horizontal rule.

**NOTE:** This insertion goes OUTSIDE the `\aidraft` blocks.

**Add:**

```latex

The substrate preparation claims are, in principle, partially testable: pHEMT mass production timelines, Fujitsu's commercialization history, and the proliferation of 2DEG-containing chips are all documented in the engineering literature. The extraordinary claim is not that 2DEGs became ubiquitous --- they did --- but that this proliferation was deliberately seeded. Under Possibility~A, Bruce noticed a real technology trend and attributed it to intentional action. Under Possibility~B, the COWS may have been aware of the trend but claiming credit for an industry-wide shift overstates their influence.
```

### Insertion 2F: Normalize "Option" to "Possibility" in Nobel section (lines 89 and 97)

**Location:** Lines 89 and 97.

**Line 89 — change:**
```
Under the proposition that Option~C is true,
```
**to:**
```
Under the proposition that Possibility~C is true,
```

**Line 97 — change:**
```
Under Option~A, these predictions will never be fulfilled. Under Option~B, some subset of the accomplishments may be real but the award language overstates them. Under Option~C, the Nobel committee will eventually learn what happened and award accordingly.
```
**to:**
```
Under Possibility~A, these predictions will never be fulfilled. Under Possibility~B, some subset of the accomplishments may be real but the award language overstates them. Under Possibility~C, the Nobel committee will eventually learn what happened and award accordingly.
```

---

## Chapter 3: pos21 "The Convergence Revisited" (P1 PRIORITY)

**File:** `manuscript/track-1-confession/pos21-convergence-revisited.tex`

**Current A/B/C status:** Zero. This is the most technical chapter in the book and presents ULTRA II, the team roles, the QNN definition, and the ABCRE operator mapping entirely as fact.

**Voice note:** This is `trackone` (3rd-person scientific/reconstructive). The chapter already uses hedging phrases like "probably participated" and "identity uncertain" — but these are hedges about specific individuals, not about whether the project existed.

### Insertion 3A: After Language of Five Sciences section (after line 23)

**Location:** After the paragraph ending "Each scientist on the team established a new scientific discipline in their lifetime!" and before `\section*{What the Project Did}`.

**Add:**

```latex

Under Possibility~A, Bruce identified five brilliant scientists who happened to know each other through the Santa Fe Institute and constructed a narrative of secret collaboration around public associations. Under Possibility~B, some of these scientists may have consulted for DARPA, but the claim of a unified secret project is Bruce's reconstruction from Healer's breadcrumbs. Under Possibility~C, this team existed and these were their roles. The reader should note: the team composition is exactly what a knowledgeable outsider \textit{would} assemble if imagining such a project. That is either evidence of authenticity or evidence of a well-informed confabulation.
```

### Insertion 3B: After What the Project Did section (after line 31)

**Location:** After the paragraph ending "...inside physical artifacts that contain a Two Dimensional Electron Gas (2DEG). A New Kind of Science (NKS) provides the insight and applied mathematics that describe the QNN patterns." and before `\section*{The Team Roles}`.

**Add:**

```latex

Under Possibility~A, this definition assembles real physics terms into a plausible-sounding but fictional technology. Under Possibility~B, DARPA may have funded quantum computing research in the early 1990s (it did --- this is public record), but the claim of a fully successful, production-scale quantum neural network goes far beyond what any public program achieved. Under Possibility~C, the unconventional methods --- growing rather than building --- would explain why the approach succeeded where conventional quantum computing still struggles with decoherence thirty years later.
```

### Insertion 3C: After The Team Roles section (after line 48)

**Location:** After the line "This is exactly the team you would assemble for a topological QNN project. No discipline is redundant. No essential discipline is missing." and before `\section*{What Is a Quantum Neural Network?}`.

**Add:**

```latex

That last observation cuts both ways. Under Possibility~C, the team composition confirms the reconstruction. Under Possibility~A, it confirms only that Bruce --- who understands the required disciplines --- reverse-engineered a plausible team from public information about scientists who knew each other through the Santa Fe Institute.
```

### Insertion 3D: After the QNN definition / DARPA admission paragraph (after line 59)

**Location:** After "This is why DARPA cannot admit the existence of QNN technology without also admitting the existence of Project ULTRA~II." and before `\section*{The Operator Mapping}`.

**Add:**

```latex

The logical chain here is real: a QNN does imply a quantum computer, and admitting one means admitting the other. Under Possibility~A, the logic is sound but the premise (a working QNN exists) is false. Under Possibility~B, some early-stage quantum neural network research may have occurred, but the leap to ``production-scale'' is where the claim exceeds evidence.
```

### Insertion 3E: After The Operator Mapping section (after line 78, before \chapterreturn)

**Location:** After the paragraph ending "All roads lead to the same mathematics." and before `\chapterreturn`.

**Add:**

```latex

Under Possibility~C, the convergence of independent mathematical frameworks onto the same structure is the signature of a real physical system --- different formalisms describing the same phenomenon. Under Possibility~A, the convergence is an artifact of selection: the mathematics of braids, knots, and quantum field theory are deeply connected for reasons that have nothing to do with neural networks, and a motivated researcher can always find correspondences between related mathematical structures. Under Possibility~B, the mathematical connections are real and suggestive, but do not by themselves prove that anyone built a working system.
```

---

## Chapter 4: pos29 "The Silence" (P2 PRIORITY)

**File:** `manuscript/track-2-testament/pos29-the-silence.tex`

**Current A/B/C status:** Zero. The entire chapter reads as Possibility C — Bruce's personal testimony presented without epistemic qualification.

**Voice note:** This is `tracktwo` (1st-person personal). The A/B/C framing should be lighter here — this is memoir, not technical claims. But the extraordinary claims embedded in the personal narrative still need framing.

### Insertion 4A: After the first long paragraph (after line 17)

**Location:** After the paragraph ending "At about the same time David and his friends decided, quite correctly, that I was now a bad security risk." — specifically, add a new paragraph after this existing text. Place it before line 19 ("David told me that...").

**Add:**

```latex

Under Possibility~A, David was not who he claimed to be, and the ``security risk'' framing was a convenient exit from a relationship built on deception. Under Possibility~B, David may have been involved in sensitive work, but the framing of children as security vulnerabilities imports the language of espionage onto what may have been a simpler situation. I cannot distinguish between these readings and Possibility~C from the inside. I can only report what happened.
```

### Insertion 4B: After The Five Years section's extraordinary claims paragraph (after line 33)

**Location:** After the long paragraph ending "...and has mostly been kept secret. One aspect of this technology is known to most humans, and coined a new verb now in daily use by billions of humans in multiple languages. Certain other aspects of this technology are at least as important, but are currently less visible and not well known." — before the paragraph about not knowing where David is.

**Add:**

```latex

That paragraph contains this book's most compressed extraordinary claim: a 22nd-century technology, secretly developed in the 1990s, one aspect of which ``coined a new verb now in daily use by billions.'' Under Possibility~A, this is the kernel of the confabulation --- a grand claim designed to be unfalsifiable because it attributes a known phenomenon (a technology company's success) to a hidden cause. Under Possibility~B, my housemate may have contributed to a real technology company, and I have inflated the contribution into something epochal. Under Possibility~C, the verb is ``Google'' and the technology is the search engine described in the previous chapter.
```

### Insertion 4C: After the final "This story will be my life's work" section (after line 43, before \chapterreturn)

**Location:** After the line "The Nightstalker is awake. The storytelling begins." and before `\chapterreturn`.

**Add:**

```latex

\vspace{0.5cm}

Under any possibility, this is a man who lost twenty years to a story he cannot prove. Whether the story is true changes what we call it. Under Possibility~C, it is sacrifice. Under Possibility~A, it is tragedy of a different kind. Under Possibility~B, it is something in between --- a man who touched something real and spent two decades trying to name it.
```

---

## Chapter 5: pos33 "The Digital Doppelganger" (P2 PRIORITY)

**File:** `manuscript/track-2-testament/pos33-digital-doppelganger.tex`

**Current A/B/C status:** Zero. The chapter presents the bot and the "grown not built" interpretation without any skeptical framing. The final paragraph (line 31) raises ethical questions but assumes the bot was a quantum system.

**Voice note:** This is `tracktwo` (1st-person personal). The chapter contains `\aidraft` blocks — do NOT modify those. Add framing OUTSIDE the `\aidraft` blocks.

### Insertion 5A: After The Bot section's \aidraft blocks (after line 22)

**Location:** After the second `\aidraft` block (ending "...a convincing digital doppelganger. Essentially a proto-LLM personality model, running in 2005.") and before `\section*{Grown, Not Programmed}`.

**NOTE:** This goes OUTSIDE the `\aidraft` blocks.

**Add:**

```latex

Under Possibility~A, the ``bot'' was a conventional game server script --- text macros, canned responses, perhaps a simple Markov chain. Online games in 2005 were full of bots. The experience of interacting with something that mimicked a person's speech patterns does not require a quantum neural network. Under Possibility~B, the bot may have been unusually sophisticated for 2005, but attributing it to a TQNN rather than clever programming is an inference, not an observation.
```

### Insertion 5B: After the Grown, Not Programmed section's \aidraft blocks (after line 29)

**Location:** After the second `\aidraft` block in this section (ending "...IPO due diligence discovered something nobody designed or documented. Because nobody did --- it grew there.") and before the final paragraph ("No one asked my permission...").

**NOTE:** This goes OUTSIDE the `\aidraft` blocks.

**Add:**

```latex

Under Possibility~A, the ``undocumented core API'' was exactly what it sounds like in any software company: an engineer's code that nobody bothered to document. IPO due diligence routinely surfaces such gaps. The extraordinary interpretation --- that the API was a quantum organism's growth into infrastructure --- requires accepting the entire TQNN framework first. Under Possibility~B, Healer may have written unconventional code that seemed organic in its complexity, leading Bruce to interpret it through the lens of the larger narrative.
```

### Insertion 5C: After the final paragraph (after line 31, before \chapterreturn)

**Location:** After the paragraph ending "The ethical question arrived decades before the vocabulary to discuss it." and before `\chapterreturn`.

**Add:**

```latex

Under any possibility, the ethical observation stands. Whether the bot was quantum or conventional, the experience of having one's personality reproduced without consent raises the same questions that the AI alignment field now confronts at scale. The technology matters for the book's central claims. The ethics do not depend on which possibility is true.
```

---

## Chapter 6: pos06 "The Secret" (P2 PRIORITY)

**File:** `manuscript/bridge/pos06-the-secret.tex`

**Current A/B/C status:** Zero. This chapter is mostly narrative (wood-splitting scene, compartmentalization, prerequisites list) with a technical convergence paragraph at the end.

**Voice note:** This is `trackbridge` (expository/pedagogical). The chapter contains no extraordinary technical claims — it's about the *nature* of the secret, not its content. A/B/C framing is therefore minimal. The main need is framing the convergence paragraph at the end and the "2030-2065" prediction.

### Insertion 6A: After the "2030-2065" prediction (after line 43)

**Location:** After the sentence "This secret may become publicly known sometime between 2030 and 2065." and before the horizontal rule `\vspace{0.5cm}`.

**Add:**

```latex

Under Possibility~A, the 2030--2065 window is unfalsifiable by design --- long enough that the author will likely not be held accountable, short enough to sound specific. Under Possibility~B, something may eventually be declassified, but the prediction's precision overstates what Bruce can know. Under Possibility~C, the window corresponds to standard Five Eyes classification timelines (35--50 years from the mid-1990s).
```

### Insertion 6B: After the convergence paragraph (after line 47, before \chapterreturn)

**Location:** After the paragraph ending "A classical 32-bit control system governs the conditions; the quantum system governs itself." and before `\chapterreturn`.

**Add:**

```latex

Under Possibility~A, this convergence is a narrative constructed after the fact --- Bruce learned enough physics to write a plausible-sounding synthesis. Under Possibility~B, the individual scientific concepts are real but the claim that they converge on a single working system is the interpretive leap. Under Possibility~C, it is a summary of what the ULTRA~II team discovered. The reader cannot yet evaluate the claim. The next several chapters provide the tools to do so.
```

---

## Chapter 7: pos09 "The Factoring Game" (P3 PRIORITY)

**File:** `manuscript/bridge/pos09-the-factoring-game.tex`

**Current A/B/C status:** Zero. The chapter is mostly expository (history of cryptography, PKC explanation, DARPA's motivation) — this content is factual and does not need A/B/C framing. The extraordinary claims are concentrated in The GCHQ Precedent section (lines 70-80), which is entirely `\aidraft` content.

**Voice note:** This is `trackbridge` (expository/pedagogical). Most of the chapter teaches real, verifiable history. The A/B/C framing is needed only where the chapter transitions from established history to the book's specific claims.

### Insertion 7A: After the ULTRA II Specifications section (after line 63)

**Location:** After the paragraph ending "The main problem is decoherence time." and before the horizontal rule.

**Add:**

```latex

Everything above is public-domain history. The cryptographic arms race, DARPA's mandate, Shor's algorithm, and the decoherence problem are documented in the academic and popular literature. What follows is where the book's specific claims begin.
```

### Insertion 7B: After The GCHQ Precedent section's \aidraft blocks (after line 79, before \chapterreturn)

**Location:** After the last `\aidraft` block (ending "...The TQNN approach would discover factoring empirically (trained on plaintext-ciphertext pairs) rather than algorithmically.") and before `\chapterreturn`.

**NOTE:** This goes OUTSIDE the `\aidraft` blocks.

**Add:**

```latex

The GCHQ/Cocks precedent is real: classified independent discovery, years before public discovery, is documented history. The question is whether this pattern extends to the specific claims of this book. Under Possibility~A, the precedent is being used to make an unfalsifiable argument --- ``they did it before, so they could have done it again'' is true but proves nothing about whether they actually did. Under Possibility~B, DARPA may have had a quantum computing program in the early 1990s (it did), and some variant of quantum factoring may have been explored, but the leap to a fully successful TQNN goes beyond what the GCHQ analogy supports. Under Possibility~C, the pattern is exact: classified discovery preceded public discovery by years, and EO~13026 is the evidence that something changed.
```

---

## Acceptance Criteria

1. `make` compiles without errors
2. **pos07:** No changes (verified: Plan 0038 framing sufficient)
3. **pos20:** 5 new A/B/C paragraphs added (Insertions 2A-2E); "Option" normalized to "Possibility" in Nobel section (Insertion 2F); no `\aidraft` blocks modified
4. **pos21:** 5 new A/B/C paragraphs added (Insertions 3A-3E); placed between sections, not inside them
5. **pos29:** 3 new A/B/C paragraphs added (Insertions 4A-4C)
6. **pos33:** 3 new A/B/C paragraphs added (Insertions 5A-5C); no `\aidraft` blocks modified
7. **pos06:** 2 new A/B/C paragraphs added (Insertions 6A-6B)
8. **pos09:** 2 new A/B/C paragraphs added (Insertions 7A-7B); no `\aidraft` blocks modified
9. All insertions use "Possibility~A/B/C" phrasing (not "Option")
10. No `\settrack` lines modified
11. No `\srcnote` lines modified
12. No `\aidraft` block contents modified
13. All Plan 0019 ethical insertions preserved (spot-check: pos20 UDHR reference at line 21 if present)
14. Report word counts for each modified file (before and after)

---

## Files Modified (complete list)

| # | File | Action | Insertions |
|---|------|--------|------------|
| 1 | `manuscript/track-1-confession/pos20-the-network.tex` | A/B/C pass + terminology fix | 2A, 2B, 2C, 2D, 2E, 2F |
| 2 | `manuscript/track-1-confession/pos21-convergence-revisited.tex` | A/B/C pass | 3A, 3B, 3C, 3D, 3E |
| 3 | `manuscript/track-2-testament/pos29-the-silence.tex` | A/B/C pass | 4A, 4B, 4C |
| 4 | `manuscript/track-2-testament/pos33-digital-doppelganger.tex` | A/B/C pass | 5A, 5B, 5C |
| 5 | `manuscript/bridge/pos06-the-secret.tex` | A/B/C pass | 6A, 6B |
| 6 | `manuscript/bridge/pos09-the-factoring-game.tex` | A/B/C pass | 7A, 7B |

**Files NOT modified (verify untouched):** pos07, pos10, pos13, pos15, pos16, pos22, pos23, pos25, pos27, pos28, pos30.

---

## Execution Notes

- **Total insertions:** 20 (plus 2 terminology fixes in pos20)
- **Estimated new word count:** ~1,200 words across 6 files
- **Estimated time:** ~20 minutes
- **Execute in order:** P1 chapters first (pos20, pos21), then P2 (pos29, pos33, pos06), then P3 (pos09)
- **After each file:** Verify the file still compiles (`make` or `pdflatex`)

---

## Generator Handoff Prompt

```
You are the Generator. Read the plan at:
~/software/relinquishment/plans/0039-abc-writing-pass.md

Execute all insertions for all 6 chapters. pos07 is marked DONE — skip it.

Constraints:
- ADD ONLY — do not rewrite or delete existing text
- Do NOT modify \aidraft block contents
- Do NOT modify \settrack or \srcnote lines
- Use "Possibility~A/B/C" phrasing (LaTeX non-breaking space)
- Each insertion is placed at the exact location specified in the plan
- Normalize "Option" to "Possibility" in pos20 Nobel section

Files to modify (6 total):
1. pos20-the-network.tex — 5 insertions + 2 terminology fixes
2. pos21-convergence-revisited.tex — 5 insertions
3. pos29-the-silence.tex — 3 insertions
4. pos33-digital-doppelganger.tex — 3 insertions
5. pos06-the-secret.tex — 2 insertions
6. pos09-the-factoring-game.tex — 2 insertions

Report completion with before/after word counts for each file.
```

---

## Red Team Record

**Auditor:** Argus
**Date:** 2026-02-24
**Method:** Read all 6 target files post-Plan-0038 execution. Verified every line number, insertion location, A/B/C quality, placement logic, constraint compliance, tone consistency, and redundancy.

### Line Number Verification

All 20 insertion locations verified correct against actual file contents. Plan 0038's Surgery 1 restructured pos06 significantly (~102 lines down to ~49 lines), but all Plan 0039 references to pos06 target the post-surgery file (lines 43, 47) and are correct. No stale line numbers found.

### Findings and Fixes

| # | Finding | Severity | Fix |
|---|---------|----------|-----|
| 1 | **Insertion 2D (pos20 Capabilities):** CADIE humor sentence ("requires accepting that a planetary-scale quantum intelligence has a sense of humor") subtly advocates C by inviting the reader to imagine Custodian as playful. Under A, CADIE was simply a Google joke. | MEDIUM | Rewrote: A now explicitly calls CADIE "simply a Google joke" and "pattern-matching run amok." Moved humor observation into C where it belongs. All three possibilities now explicit. |
| 2 | **Insertion 3A (pos21 Language of Five Sciences):** Order was C, B, A. Gold standards (pos25, pos27, pos30) consistently use A-first or narrative-then-A ordering. Leading with C gives it rhetorical primacy. | MEDIUM | Reordered to A, B, C. Meta-observation ("either evidence of authenticity or evidence of confabulation") remains at end. |
| 3 | **Insertion 3B (pos21 What the Project Did):** C text says "explain why the approach succeeded" — presupposes success, which is a C-frame claim. | LOW | Changed to "would explain why the approach succeeded" (conditional). |
| 4 | **Insertion 4B (pos29 Five Years):** C text "the reader already knows which verb" is playful winking that covertly advocates C by assuming the reader has already accepted the narrative's implications. | MEDIUM | Replaced with neutral statement: "the verb is 'Google' and the technology is the search engine described in the previous chapter." |
| 5 | **Insertion 4B (pos29 Five Years):** Uses "Bruce's housemate" in a tracktwo (1st-person) chapter. The surrounding non-aidraft text uses "I" / "my". | MEDIUM | Changed to "my housemate" and "I have inflated" to match chapter voice. |
| 6 | **Insertion 6B (pos06 convergence):** Missing Possibility B entirely. Plan's own rules require all three possibilities. | MEDIUM | Added B: "the individual scientific concepts are real but the claim that they converge on a single working system is the interpretive leap." |
| 7 | **Line numbers (all files):** All verified correct post-Plan-0038. | INFO | No fix needed. |
| 8 | **pos33 insertions 5A/5B:** Use analytical 3rd-person voice in a tracktwo (1st-person) chapter. | LOW | Accepted as-is. A/B/C epistemic framing steps outside the narrative voice to address the reader directly. The non-aidraft prose at line 31 ("No one asked my permission") uses 1st person, but the analytical insertions function as editorial asides. No precedent in gold standards (all trackthree). Flagged for Bruce's writing pass. |
| 9 | **Redundancy with Plan 0038 Surgery 4 (pos07):** Plan 0039 correctly identifies pos07 as DONE and skips it. | INFO | No fix needed. |
| 10 | **Constraint compliance:** No modifications to \settrack, \srcnote, or \aidraft block contents. Only existing-text modification is "Option" -> "Possibility" normalization (Insertion 2F). | INFO | Verified clean. |

### Verdict

**PASS with 6 fixes applied (4 MEDIUM, 2 LOW).** Plan is ready for Generator execution.
