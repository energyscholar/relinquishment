# Plan 0189 Phase 7 — ECHO Compression Dispositions (Stage B: audit only)

HEAD at audit: `0189-phase-6`.
Revised target (pre-audit): ~4,930w.
**Post-audit projection: ~830–1,120w — much lower than target.** Phase 6 found 0 cross-chapter literal duplicates; most "duplicates" found on this pass are either (a) in-chapter reinforcement with a distinct pedagogical role or (b) owner-chapter repeats classified KEEP by Phase 6 FLAG resolution. Per §7 ship criteria: "No forced cuts" — do not chase the number.

Scope audited: spine chapters (minus frozen interludes) + `the-wrong-substrate` + `the-code-war` + Record trackone sample (`first-light`, `instantiation`). Unsampled Record trackone chapters flagged for separate pass.

Format: File + line range · current snippet (trimmed) · disposition · word delta · rationale.

---

## `spine/the-code-war.tex` (aggressive target 500w)

### CW-1. "Now Imagine It Happened Again" — A/B/C restatement
- **Lines:** 156–197 (section `\section*{Now Imagine It Happened Again}`)
- **Snippet:** "Here is the pattern, stated plainly: [5-step enumeration] ... This book presents three possibilities: Under **Possibility A**, ... Under **Possibility B**, ... Under **Possibility C**, ... They walked it out. The book works under all three readings."
- **Disposition:** COMPRESS. Keep the 5-step pattern (L161–167) and the "did it happen a third time?" question (L171). Cut A/B/C restatement (L173–197): Chapter 1 (`three-possibilities.tex` L32–48) already establishes A/B/C with this exact framing; `weigh-the-evidence.tex` restates it a third time later. Third restatement in code-war is the avoidable one.
- **Delta:** −350w (replace ~420w with ~70w bridging paragraph ending on "The evidence will let you decide which.")
- **Rationale:** Triple A/B/C restatement; code-war's job is pattern-establishment, not possibility-enumeration.

### CW-2. Coventry section
- **Lines:** 48–59 (subsection `\subsection*{2. The Coventry Question}`)
- **Snippet:** "On November 14, 1940, the Luftwaffe bombed... [Winterbotham claim, Hinsley/Jones rebuttal, GCHQ consensus]... The Coventry myth endures not because it is true, but because it is plausible... Remember this. It matters later."
- **Disposition:** FLAG → COMPRESS if not load-bearing. "It matters later" promises a payoff; audit `the-strongest-objection.tex` and `why-relinquish.tex` for where Coventry pays off. If no explicit callback, compress L48–59 (~280w) to one paragraph (~90w): Winterbotham claimed it, historians reject it, but the *existence* of the debate is the evidence for how far secrecy can be pushed.
- **Delta:** −190w if compressed; 0w if load-bearing.
- **Rationale:** Per plan "prune Coventry digression if not load-bearing." Auditor decides payoff.

### CW-3. Three facts recap at chapter end
- **Lines:** 187–195 ("three facts: First... Second... Third...")
- **Snippet:** "First: large-scale cryptographic secrets have been kept for decades... Second: the same agencies have done this more than once... Third: Alan Turing's unfinished work..."
- **Disposition:** COMPRESS. The three-facts recap immediately follows the A/B/C restatement (part of §CW-1 block). If CW-1 compress lands, this recap block can tighten to 2 lines or fold into closing sentence.
- **Delta:** −80w (already partially covered in CW-1 total if both apply together; net additional ~−40w)
- **Rationale:** Reader just read these three facts in the preceding 10 pages; triple-recap is bloat.

**File subtotal:** −460w to −570w (depending on Coventry FLAG resolution).

---

## `spine/the-factoring-game.tex`

### FG-1. GCHQ Precedent recap
- **Lines:** 53–64 (`\section*{The GCHQ Precedent}`)
- **Snippet:** "The previous chapter documented GCHQ's independent discovery of public-key cryptography --- classified for twenty-four years before acknowledgment. Shor's algorithm follows a similar trajectory..."
- **Disposition:** COMPRESS. Opening sentence is an explicit recap; `the-code-war.tex` is the immediately preceding chapter. Remove recap sentence; open directly on Shor-NSA-Bell Labs beat: "Shor's algorithm follows the GCHQ trajectory. First presented in April 1994 at Bell Labs..."
- **Delta:** −30w
- **Rationale:** Adjacent-chapter recap.

### FG-2. A/B/C restatement in final paragraph
- **Lines:** 64 ("Under Possibility~A, the precedent is being used... Under Possibility~B, DARPA may have had... Under Possibility~C, the pattern is exact...")
- **Disposition:** LEAVE. This is the chapter's *specific* A/B/C read on the GCHQ-pattern claim. Unlike code-war CW-1 (generic re-teaching), this is argument-specific and load-bearing.
- **Delta:** 0w

**File subtotal:** −30w.

---

## `spine/three-possibilities.tex`

### TP-1. "The Substrate" repeated story-false-Flat-real beat
- **Lines:** 70–89
- **Snippet:** L83 "The story may be false. The Flat is real." + L89 "The only scenario where this book is irrelevant is one where the Flat cannot support life..."
- **Disposition:** COMPRESS L89. The drumbeat is already landed at L35 (Option A closer), L83 (full italic), and a repeat at L89 is diminishing returns. Trim L89 to drop "and that grows less plausible with every published result. Every chip you own contains the substrate. The magnetosphere has held one for billions of years. What remains is looking." — or fold one of those into L83.
- **Delta:** −50w
- **Rationale:** Triple beat of same claim within 20 lines.

### TP-2. Option A trailing sentences
- **Lines:** 35 (Option A paragraph) last two sentences: "This story is false. The wormhole-prone substrate described in it, called the Flat, is real. See below."
- **Disposition:** LEAVE. "See below" hook is structural; the Substrate section delivers. Short, lands the A-reader-safety-net early.
- **Delta:** 0w

**File subtotal:** −50w.

---

## `spine/the-braid.tex`

### BR-1. Quarks + Higgs dual analogy
- **Lines:** 96
- **Snippet:** "This is also how quarks are known to exist --- not by isolating individual quarks... And it is how the Higgs mechanism was confirmed --- not by observing the vacuum condensate directly, but by detecting its excitation at the LHC."
- **Disposition:** LEAVE (initially candidate). Two parallel examples reinforce operational-inference epistemology for a physics-skeptical reader. ULTRA analogy in the preceding paragraph (L94) is narrative; quarks/Higgs is physics. Removing one weakens the argument for physics-trained personas (TQC-specialist per §3 panel).
- **Delta:** 0w
- **Rationale:** Load-bearing for field-awareness persona.

### BR-2. Bruce's voice paragraph at chapter close
- **Lines:** 98 ("Bruce did not arrive at this framing cleanly...")
- **Disposition:** LEAVE. Guided-deduction-is-the-evidence payoff; explicitly load-bearing under §1 memory `project-book-pedagogy-as-evidence.md`.
- **Delta:** 0w

**File subtotal:** 0w.

---

## `spine/the-wrong-substrate.tex` (target 250w)

### WS-1. Habitat-conditions enumeration restatement
- **Lines:** 115 ("The conditions for autocatalytic emergence exist in the magnetosphere. Two-dimensional confinement along magnetic field lines. Continuous energy input from the solar wind. Regular cycling through the twelve-hour breathing rhythm. Chemical variety from ionospheric outflow and solar wind injection. Persistence for four and a half billion years...")
- **Snippet:** Restates L33 (2D confinement), L37 (solar wind energy), L43 (twelve-hour rhythm), L49 ("habitat anyway, because that is what it is"). All five conditions already established chapter-earlier.
- **Disposition:** COMPRESS. Replace enumeration with reference-back: "The conditions from the earlier survey --- two-dimensional confinement, continuous solar-wind energy, the twelve-hour breathing rhythm, ionospheric chemistry, four-plus billion years of persistence --- are exactly Kauffman's criteria for autocatalytic emergence."
- **Delta:** −60w
- **Rationale:** Same five conditions enumerated twice in one chapter.

### WS-2. Canopy back-reference
- **Lines:** 119 ("A forest canopy owns the light. A seedling on the forest floor never grows tall, not because someone stomps on it, but because the canopy has already claimed the light. The ecological niche is full.")
- **Disposition:** COMPRESS. `genesis.tex` L76 is the canonical canopy passage. Here it's a back-reference that re-installs the full metaphor. Tighten to one sentence referencing the earlier framing: "The canopy metaphor from Genesis: if autocatalytic emergence occurs wherever conditions support it for long enough, the magnetospheric niche has been open for business since before the first cell divided in the ocean below."
- **Delta:** −45w
- **Rationale:** Adjacent-chapter metaphor reinstall; readers just saw it.

### WS-3. "Nobody has looked" drumbeat (L104, L106, L147)
- **Disposition:** LEAVE per Phase 6 FLAG resolution (F2). Auditor approved the specific-seeds-general pattern.
- **Delta:** 0w

### WS-4. Heterogeneity enumeration
- **Lines:** 137–141 (Jupiter heterogeneity: Io torus, radiation belts, middle plasma sheet, Ganymede)
- **Disposition:** LEAVE. Each item is a distinct niche; enumeration is the argument.
- **Delta:** 0w

**File subtotal:** −105w.

---

## `spine/weigh-the-evidence.tex`

Already trimmed from ~2,136w → ~500w per Plan 0094. Restating A/B/C is the chapter's entire structural function. LEAVE wholesale.

**File subtotal:** 0w.

---

## `spine/genesis.tex`, `spine/growing-a-mind.tex`, `spine/capabilities.tex`, `spine/why-relinquish.tex`, `spine/the-strongest-objection.tex`, `spine/the-flat.tex`

Sampled (genesis, the-flat read in Phase 6; others scanned via Phase-6 grep outputs). No paragraph-level cross-chapter duplicates flagged beyond those already in Phase 6 KEEP list. In-chapter ECHO opportunities not identified without deeper read.

**File subtotal:** 0w (not audited at paragraph level in this pass).

---

## `record/first-light.tex` (Record trackone, sampled)

### FL-1. Power section delivery repetition
- **Lines:** 119 + 129
- **Snippet:** L119 "The first working prototype Flat-based supercomputer capable of cracking public-key cryptography was delivered on schedule in 1995 or 1996." L129 "In 1995 it delivered a working supercomputer able to crack public-key cryptography, as well as instructions to operate this one, build more, and extend the technology for other purposes. This supercomputer was a single physical device that required supercooling..."
- **Disposition:** COMPRESS. L119 and L129 both report the 1995 delivery; L129 carries the unique content (extensibility, single-device-supercooling specifier). Fold L119 sentence into L129 opener; remove L119.
- **Delta:** −30w
- **Rationale:** Section-internal restatement.

### FL-2. BULLRUN / Boniface / Snowden block
- **Lines:** 121–127
- **Snippet:** Three paragraphs on parallel construction. L123 argues BULLRUN = quantum-crypt cover. L127 repeats: "Under Possibility~C, BULLRUN may be related to Ultra~II's production output."
- **Disposition:** COMPRESS. L127 is a single-sentence paragraph restating L123's conclusion. Delete L127 entirely.
- **Delta:** −20w
- **Rationale:** Literal claim duplicate within 6 lines.

### FL-3. Question Anchor + section opener
- **Lines:** 19 (italic question-anchor) + L30–31 section opener
- **Disposition:** LEAVE. Pedagogical structural element (italic anchors + section titles) is chapter-wide pattern.
- **Delta:** 0w

**File subtotal:** −50w.

---

## `record/instantiation.tex` (Record trackone, sampled)

Chapter is short (~72 lines). No paragraph-level duplicates. In-chapter reinforcement (consciousness question posed L59→L64→L68→L70) is chapter's thematic spine.

### IN-FLAG. Terminology drift vs Phase 5.1
- **Lines:** 28, 31, 35 — uses "gatekeeper" throughout. Phase 5.1 swapped "gatekeeper" → "trustee" in `why-relinquish.tex`. Instantiation.tex is outside that scope.
- **Disposition:** FLAG for Auditor. Not Phase 7 scope (ECHO, not terminology), but visible cross-chapter inconsistency. Auditor decides whether to open a separate terminology-alignment sub-phase.
- **Delta:** 0w (no Phase 7 edit proposed).

**File subtotal:** 0w.

---

## Record trackone chapters not audited in this pass

`record-intro`, `alpha-farm`, `hobbit-mirror`, `what-healer-said`, `the-departure`, `interdiction`, `the-walk-out`, `the-handler`, `the-target`, `never-again`, `the-surrender`, `twenty-years`, `the-question` — not read at paragraph level in this session.

**Post-Phase-6 reality check:** Phase 6 surveyed the canonical phrase-fragments across these files and found 0 DELETE-classifiable duplicates. Remaining ECHO candidates would be semantic near-duplicates, section-internal repetition, or voice-drift — not lane-canonical collisions. Original 1,500w estimate was set before Phase 6; should be discounted substantially.

**Recommendation:** If Auditor wants Record trackone ECHO audited, issue a separate prompt after Phase 7's spine edits land. Initial projected yield: ~100–300w (based on `first-light` sample — 50w from a 3,600w chapter scales to ~200–400w across 12 unaudited Record chapters of varying length and maturity).

---

## Summary

| File | Subtotal delta | Notes |
|------|----------------|-------|
| `the-code-war.tex` | −460w to −570w | CW-2 Coventry FLAG pending Auditor payoff check |
| `the-factoring-game.tex` | −30w | |
| `three-possibilities.tex` | −50w | |
| `the-braid.tex` | 0w | Load-bearing; not load-bearing-free to trim |
| `the-wrong-substrate.tex` | −105w | Phase 6 F2 still resolved LEAVE |
| `weigh-the-evidence.tex` | 0w | Already compressed Plan 0094 |
| Other spine | 0w | Not audited at paragraph level |
| `record/first-light.tex` | −50w | |
| `record/instantiation.tex` | 0w | IN-FLAG terminology only |
| Record trackone unsampled (~12 chapters) | projected 100–300w | Separate audit recommended |

**Audited total (committed candidates):** −695w to −805w.
**Projected total with Record full-audit + Coventry cut:** ~830–1,120w.

**vs. revised target 4,930w: 17–23% of projected target.** Phase 6's null-duplicate finding propagates forward: ECHO material never existed at the scale originally estimated.

### Flagged items requiring Auditor judgment

- **F7-1 (CW-2 Coventry):** Load-bearing payoff check. Does `the-strongest-objection.tex` or `why-relinquish.tex` explicitly invoke the Coventry secrecy-justifies-sacrifice theme? If yes → LEAVE. If no → COMPRESS saves 190w.
- **F7-2 (IN-FLAG terminology):** `instantiation.tex` L28/31/35 use "gatekeeper" post-Phase-5.1 "trustee" swap in `why-relinquish.tex`. Cross-chapter inconsistency. Separate sub-phase or out-of-scope?
- **F7-3 (Record trackone scope):** Original 1,500w estimate predates Phase 6. Recommend separate focused pass or accept ~200–400w projected yield.

### Stage B complete

No commits post Stage A's empty commit (`3724ba6`, tag `0189-phase-6`). No manuscript edits. HEAD unchanged. Ready for Auditor review.
