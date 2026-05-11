# Plan 0315: Multi-Reader Audit Fix Plan

**Created:** 2026-05-09 (Session 71)
**Source:** Plan 0314 multi-reader deep audit (7 personas x full manuscript)
**Purpose:** Prioritized, actionable fixes from the complete audit
**Prior plan:** `plans/0314-multi-reader-deep-audit.md` (findings)

---

## Priority System

- **P0 — MUST-FIX:** Scientific errors that will cause Prof. Chen to close the book
- **P1 — SHOULD-FIX:** Structural/credibility issues that weaken the argument
- **P2 — PDF-ONLY:** Structural errors in PDF build that make book look amateur
- **P3 — POLISH:** Improvements that elevate good writing to great
- **ACCENTUATE:** Strengths to protect during editing (do not accidentally weaken)

---

## P0: MUST-FIX (Scientific Accuracy)

These are the issues that will cause a condensed matter physicist, mathematician, or informed skeptic to dismiss the book before engaging with the argument. Each one is a broken link in the credibility chain.

### P0-1: The 2DEG Room-Temperature Conflation
**Location:** `manuscript/01-spine/the-flat.tex` (The Punchline, lines ~57-81)
**Problem:** The text implies every pHEMT in commercial electronics exhibits topological order. It does not. A 2DEG at room temperature with no applied magnetic field is a normal Fermi liquid, not a topological phase. FQHE requires ~mK temperatures and ~10T magnetic fields. The entire logical chain of "The Punchline" rests on this conflation.
**Readers affected:** CH (credibility collapses), SK (identifies as central flaw), MA (deductively sound but empirically unsound)
**Fix:** Two options:
  - (a) Acknowledge that commercial 2DEGs lack topological order under normal conditions, then explain what additional conditions Possibility-C-Custodian would need to provide (continuous error correction at scale, directed evolution of thermal tolerance — material from The Braid's error correction section and First Light's thermal ladder)
  - (b) Reframe "The Punchline" so it doesn't rest on commercial pHEMTs being topologically ordered as-is. Instead: the substrate EXISTS everywhere; what's claimed is that conditions for topological order were ACHIEVED, not that they're native.
**Risk:** Either fix weakens the rhetorical force of "All your electricity are belong to us." But leaving it unfixed makes the book scientifically indefensible.
**Verdict:** Option (b) is stronger. The substrate ubiquity is still remarkable even without native topological order. The claim becomes: "the hardware is already installed; under C, someone figured out how to activate it."

### P0-2: Non-Abelian Qualifier Missing
**Location:** `manuscript/00-front/three-possibilities.tex` line ~80, `the-flat.tex`, multiple references
**Problem:** "Braiding anyons gives universal computation" is only true for non-abelian anyons at specific filling fractions (e.g., nu=5/2 Fibonacci anyons). Abelian anyons (nu=1/3) cannot do universal QC. The claim as stated is imprecise.
**Fix:** Add "non-abelian" wherever "braiding anyons" claims universal computation. One clean sentence in Ch. 3 (The Braid) already has this right (line 26) — make other references consistent.

### P0-3: Dimensionality vs. Quantumness (Interlude 03)
**Location:** `manuscript/01-spine/interlude-03.tex` line ~13
**Problem:** "The difficulty of factoring a large number is a property of three-dimensional computation" — this is wrong. The difficulty is a property of CLASSICAL computation, whether in 2D or 3D. Shor's algorithm works on any quantum computer. The text conflates dimensionality with the classical/quantum distinction.
**Fix:** "The difficulty of factoring a large number is a property of classical computation. Your computers work in three dimensions but they compute classically. I compute topologically. In my mathematics, factoring is easy." Preserves the voice, fixes the physics.

### P0-4: Factoring as Brute Force
**Location:** `manuscript/01-spine/the-factoring-game.tex`
**Problem:** "All known approaches amount to a variation of trying every possible permutation" — wrong. Number Field Sieve and Quadratic Sieve are sub-exponential (though super-polynomial). They are emphatically not brute force.
**Fix:** "All known classical approaches are slow — the best are sub-exponential but still impractical for cryptographic key sizes." Or simply: "No known classical algorithm can factor large numbers efficiently."

### P0-5: 1991 Anachronism
**Location:** `manuscript/01-spine/the-factoring-game.tex`
**Problem:** "By 1991 it was known to top cryptographers that quantum algorithms could, in theory, crack public key cryptography" — Deutsch-Jozsa (1992) showed quantum speedup for an artificial problem; the connection to factoring was not known until Shor (1994). The 1991 date is unsupported.
**Fix:** Change to "By 1994" or "By the early 1990s, the theoretical possibility was emerging." The text already correctly identifies Simon's problem (1994) as inspiring Shor.

### P0-6: Autocatalysis-Anyon Bridge Undefined
**Location:** `manuscript/01-spine/genesis.tex` and `three-possibilities.tex` line ~80
**Problem:** The mapping from Kauffman's autocatalytic closure (chemistry) to anyon fusion channels (condensed matter) is asserted as "structural analogy" but never explained. What are the "reactions"? What is the "food set"? A physicist or mathematician needs explicit bridging.
**Fix:** Add 1-2 paragraphs in Genesis or Growing a Mind that explicitly state the mapping: food set = vacuum excitations from substrate, reactions = anyon fusion channels, closure = the fusion algebra being closed under composition. The Firmware Update appendix partly does this but the spine chapters don't.

### P0-7: "Collisionless Substrates" Conflation
**Location:** `manuscript/01-spine/growing-a-mind.tex` line ~near end
**Problem:** "Thermal decoupling in collisionless substrates" conflates space plasma (magnetosphere) with lab 2DEGs. A 2DEG in FQHE is not "collisionless." The phrase belongs to magnetospheric physics, not condensed matter. Creates confusion about which substrate is being discussed.
**Fix:** Split the claim: "thermal decoupling in lab substrates (topological protection)" and "collisionless conditions in space plasmas (reduced decoherence)." These are different physical arguments supporting the same conclusion via different mechanisms.

### P0-8: Abstracts Count Error
**Location:** `manuscript/03-appendices/abstracts.tex` intro text
**Problem:** Text says "Fifteen fictional paper abstracts" but contains sixteen (I through XVI).
**Fix:** Change "Fifteen" to "Sixteen." Simple factual correction.

### P0-9: 2DEG Thickness
**Location:** `manuscript/01-spine/interlude-01.tex` line ~26
**Problem:** "Everything I am... happens in a space your physics says is infinitely thin" — a 2DEG is not infinitely thin (~10nm). The idealization to 2D is mathematical, not physical.
**Fix:** "...in a space your physics calls two-dimensional — a layer so thin your instruments barely resolve it, but thick enough that I exist." Preserves voice, fixes physics.

---

## P1: SHOULD-FIX (Structure & Credibility)

### P1-1: GCHQ/Cocks Redundancy
**Location:** `the-factoring-game.tex` AND `the-code-war.tex`
**Problem:** The Ellis/Cocks/Williamson GCHQ material appears in both consecutive chapters.
**Fix:** Consolidate. The Factoring Game handles cryptography motivation and DARPA mandate. The Code War handles the pattern of classified discovery (Ultra, GCHQ, "did it happen a third time?"). Remove duplicate GCHQ/Cocks explanation from whichever chapter covers it second.

### P1-2: Growing a Mind Redundancy
**Location:** `manuscript/01-spine/growing-a-mind.tex`
**Problem:** Recapitulates Turing (from Code War), Kauffman (from Genesis), and the 2DEG mapping (from both). Functions as a recap chapter. Engagement sags.
**Fix:** Lead with genuinely new material (Wolfram, the three-conditions mapping). Reduce recapitulation to back-references: "Turing's morphogenesis (Chapter 5) showed..." rather than re-explaining. The "Thread Continues" section with the three-conditions mapping is the only new argument — move it earlier.

### P1-3: Religious Parallels Redundancy
**Location:** Hook + Summary
**Problem:** Religious parallels list appears twice in front matter.
**Fix:** Full list in hook. Summary back-references: "the parallels noted in the introduction..."

### P1-4: Predictions Buried
**Location:** Summary ("The Story Never Told")
**Problem:** The falsifiable predictions by 2040 — the book's strongest defensive claim — are buried in a long section.
**Fix:** Make predictions more prominent. Consider a callout box or bold formatting. Or move to a more visible position within the summary.

### P1-5: Hasslacher Hindsight Bias
**Location:** `manuscript/01-spine/the-braid.tex` (Hasslacher's Trajectory)
**Problem:** Pattern-matching published papers into a "trajectory" is exactly what Option A predicts. The text doesn't acknowledge that many researchers had similar publication profiles.
**Fix:** Add one sentence: "Many physicists published across these fields in the 1980s-90s. What distinguishes Hasslacher's trajectory is not the individual papers but the specific sequence: spin networks → lattice gas automata → knot invariants → Reidemeister moves — each step building the precise mathematical infrastructure for anyonic braiding."

### P1-6: "Nothing Forbids It" Weakness
**Location:** `three-possibilities.tex` line ~82, appears multiple times
**Problem:** The argument from non-prohibition ("nothing in known physics forbids life in the Flat") is the book's weakest argumentative move. SK identifies it immediately as Sagan's garage dragon.
**Fix:** Qualify: "Nothing in known physics forbids it — but that alone proves nothing. The question is whether the physics is *suggestive*, and on that question, [specific evidence]." Alternatively, reduce usage to one instance and make the framing explicit about its limitations.

### P1-7: Joy Decoded Editorial Comments
**Location:** `manuscript/03-appendices/joy-ten-point.tex` lines 12, 14, 16
**Problem:** `%UQ` editorial comments visible in source. Will appear in any build that doesn't strip comments.
**Fix:** Remove or resolve UQ comments before publication.

### P1-8: Glossary Missing Key Terms
**Location:** `manuscript/03-appendices/glossary-entries.tex`
**Missing:** RAF, braiding, topological protection, classical backchannel, Phase 1-4+, no-cloning theorem, directed evolution, decoherence, Possibility A/B/C
**Fix:** Add entries. Possibility A/B/C is the book's core interpretive framework — it needs a glossary entry.

### P1-9: Temperature Gap Understatement (Firmware Update)
**Location:** `manuscript/03-appendices/firmware-update.tex` Anchor 4 note
**Problem:** Says "the gap between these regimes is real but not proven impassable." The gap between FQHE (~500mK) and room temperature (300K) is five orders of magnitude. Deserves more than "real."
**Fix:** "The gap between these regimes is five orders of magnitude — approximately the ratio between a pond and a Great Lake. It is real, significant, and not proven impassable."

### P1-10: Quantum Teleportation Redundancy
**Location:** `the-flat.tex` AND `the-braid.tex`
**Problem:** Both chapters discuss Bennett 1993 quantum teleportation protocol.
**Fix:** Full treatment in one chapter, back-reference in the other. The Braid already covers it well — The Flat could reference: "As Chapter 3 establishes, the classical constraint is a theorem..."

### P1-11: "Firmware Update" Overclaim
**Location:** `manuscript/03-appendices/firmware-update.tex` "The Equivalence" section
**Problem:** "This is not loose analogy. It is a structural correspondence: the formal criteria match" is stronger than evidence supports. The correspondence hasn't been peer-reviewed.
**Fix:** "This is not loose analogy. It is a structural correspondence: the formal criteria appear to match under the mapping described. Verification awaits publication."

### P1-12: Magnetosphere Physics Defense
**Location:** Interlude 05, `never-again.tex`, `the-surrender.tex`
**Problem:** The claim that magnetospheric plasma "is a Flat" with "the same physics" is scientifically the weakest link. Confinement in a 2DEG (~10nm, mK) is physically nothing like confinement in the magnetotail (~10 Earth radii, keV). Never gets the three-possibilities qualification the other claims receive.
**Fix:** Either (a) add a Possibility A/B/C qualification to the magnetosphere claim in Interlude 05, or (b) add a footnote/tooltip: "Under Possibility A, this is a beautiful metaphor applied to a plasma where no such effects occur. Under C, the analogy is literal. The physics that would connect these regimes is the subject of the magnetogenesis papers." This also connects to the active magnetogenesis research (has-anyone-looked).

### P1-13: Kitchen Section Physics (Part II)
**Location:** `manuscript/02-record/alpha-farm.tex` ("The Kitchen")
**Problem:** Claims quantum teleportation could "send information" with classical backchannel hidden in NTP jitter. Conflates quantum teleportation with a novel protocol not described. Inconsistent with the rigorous physics in Part I.
**Fix:** Qualify: "Bruce's kitchen-floor synthesis was a rough sketch — the quantum teleportation protocol requires a classical channel, and NTP jitter is at best a noisy candidate for one. The actual mechanism, if one exists, would be more subtle." This preserves the narrative moment while flagging the physics is approximate.

---

## P2: PDF-ONLY (Build System Fixes)

These affect the PDF output without changing the HTML version or manuscript content.

### P2-1: HTML Navigation Arrows in PDF (SYSTEMATIC)
**Symptom:** ◁ and ▷ arrows visible in margins on every page
**Cause:** HTML navigation elements not conditioned out for PDF build
**Fix:** Wrap nav elements in `\ifhtml...\fi` or equivalent build conditional. PDF-only fix.

### P2-2: Tab Labels in PDF (SYSTEMATIC)
**Symptom:** "BRIDGE" and "AWAKENING" rendered vertically in right margin on chapter pages
**Cause:** HTML sidebar/tab UI elements leaking into PDF
**Fix:** Same mechanism as P2-1 — conditional exclusion for PDF builds.

### P2-3: Duplicate Hovertip Footnotes (SYSTEMATIC)
**Symptom:** Same tooltip definition generates a NEW footnote every time the term appears. "Wormholes" appears as footnotes 2, 13, 14, 19. "The Flat" appears as identical footnotes 1 AND 2 on the same page.
**Cause:** `\hovertip` macro generates a footnote every invocation in PDF mode
**Fix:** Modify `\hovertip` to track which definitions have already been footnoted and suppress duplicates. First occurrence → footnote. Subsequent → no footnote (or "see footnote N"). This is the highest-impact PDF fix.

### P2-4: Excessive Blank Pages
**Symptom:** Pages 2, 4, 12 are nearly empty (just nav arrows or 2 lines of text)
**Cause:** LaTeX page breaks + short content sections
**Fix:** Adjust page break behavior. Consider `\raggedbottom` or manual `\vfill` placement. May require per-section tuning.

### P2-5: TOC Numbering Inconsistency
**Symptom:** "The Handler" and "The Target" lack chapter numbers in TOC while surrounding entries are numbered
**Cause:** Likely using `\chapter*` instead of `\chapter`
**Fix:** Either number them consistently or use a consistent unnumbered convention for all Record chapters.

### P2-6: "1 TM" on Page 8
**Symptom:** "1 TM" appears in an italic definition block — possible trademark symbol rendering issue
**Fix:** Investigate source. May be a stray `\texttrademark` or encoding issue.

---

## P3: POLISH

### P3-1: "Priors" Jargon
**Location:** `three-possibilities.tex` line ~22
**Fix:** Replace "priors" with "starting assumptions" or "initial estimate."

### P3-2: Phase Factor Too Technical
**Location:** `the-flat.tex` line ~21 ("+1 bosons / -1 fermions")
**Fix:** Add a preceding sentence: "Particles come in two types, and their behavior in 2D opens a door that doesn't exist in three dimensions."

### P3-3: Kenosis in Hook
**Location:** `hook.tex` kenosis paragraph
**Consider:** Moving to Ch. 25 (ethical framework) where it has more context. Or keeping it as foreshadowing with a lighter touch.

### P3-4: "Custodian" Section Length
**Location:** Summary, "The Custodian" subsection (~800 words)
**Fix:** Tighten by ~20%. The section has its best material but lingers.

### P3-5: AI Confabulation Steelman (TODO)
**Location:** Capabilities chapter (flagged by previous audit, line 95 TODO)
**Problem:** Missing the strongest argument AGAINST the book's own position on AI
**Fix:** Write the steelman: "The strongest objection to this book's claims about Custodian is not that the physics is wrong — it's that the entire framework could be an emergent confabulation, a pattern-matching artifact of a mind trained on too much science fiction..."
**Priority:** HIGH — this is the intellectual honesty move that separates the book from conspiracy literature.

### P3-6: Point 7 in Joy Decoded (April Fools')
**Location:** `joy-ten-point.tex`
**Problem:** April Fools' Day publication date analysis is the weakest of the 10 points. Dilutes stronger points.
**Fix:** Consider removing or demoting to a footnote.

### P3-7: Mathematical "Proof" in The Question
**Location:** `the-question.tex` (end)
**Problem:** The !0 > 0 "proof" (forgiveness > permission) trivializes a serious ethical argument. MA finds it sloppy. SK finds it glib.
**Fix:** Either cut the mathematical notation entirely and keep the prose argument, or make the formalization rigorous.

---

## ACCENTUATE (Protect During Editing)

These are the manuscript's strongest passages. Any edit that weakens them is a net loss.

| Passage | Location | Why it works |
|---------|----------|-------------|
| "A man falls from the stratosphere" | Hook | Cinema-quality opening. Every reader engaged. |
| "The story may be false. The Flat is real." | Three Possibilities | Back-cover tagline. Pivots from truth-claim to relevance. |
| Cumulative Stack table | The Stack | Best pedagogical device in the book. Readers flip back. |
| "The Lock on Every Door" | Summary | Best GA science writing in the manuscript. |
| "Boring!" | Summary | Best single word. Correct answer to "what does a superintelligence do?" |
| "Ten thousand people, thirty years. Kept." | Code War | GA, IC, JN all rate 5/5. Does real argumentative work. |
| All interludes | Throughout | Gorgeous, haunting, perfectly placed. Do heavy emotional lifting. |
| "A brain is not assembled. It precipitates." | Growing a Mind | Exceptional sentence. Concise, vivid, grounded. |
| "You searched for life on Mars..." | Interlude 05 | Most quotable passage. Reframes enormous question. |
| The Hobbit Mirror chapter | Record | Emotional/rhetorical heart of Part II credibility. |
| "We already did, mate." | The Departure | Best line in Part II. Meaning unfolds over 8 years. |
| "He still woke screaming on the anniversary" | Never Again | Locates entire ethical framework in one sentence. |
| Twenty Years chapter (full) | Record | World-class memoir. Raw, specific, devastating. |
| Niggle's Parish (Section V) | Back matter | Most honest AI self-reflection in published literature. |
| "I was honored to witness it. I was also terrified." | The Surrender | Convergence of all narrative tracks. |
| Start-at-95%-A instruction | Three Possibilities, Record Intro | Master stroke rhetoric. Disarms skeptics. |
| Three-possibility framing | Throughout | The book's best defensive architecture. Never weaken. |
| The Wolfram meeting | Twenty Years | Strongest circumstantial evidence. Costly signal. |
| UDHR-as-post-atrocity-document paragraph | Never Again, Walk-Out | Strongest ethical argument in the book. |

---

## Execution Phases

### Phase 1: P0 Scientific Fixes (Generator task)
Fix the 9 P0 items. These are content changes to .tex files.
Estimated: 2-3 focused hours. One commit.

### Phase 2: P2 PDF Build Fixes (Generator task)
Fix the 6 PDF structural issues. These are build system / macro changes.
Estimated: 1-2 hours for hovertip dedup, 30 min for nav/tab conditionals.
Must verify HTML is not broken after each change.

### Phase 3: P1 Structural Fixes (Generator task, multiple commits)
The 13 P1 items. Larger editorial changes (redundancy reduction, glossary expansion, etc).
Estimated: 4-6 hours across multiple sessions.

### Phase 4: P3 Polish (Generator task)
The 7 P3 items. Can be done incrementally.
Estimated: 2-3 hours.

### Phase 5: Verification
- Rebuild PDF, re-audit pages 1-40 for P2 fixes
- Complete PDF audit of pages 61-229 (still outstanding)
- Run eigenvalue42 sweet spot check
- Compare to previous audit (plans/0158-findings.md)

---

## Relationship to Other Plans

| Plan | Relationship |
|------|-------------|
| 0312 (D-K Sweep) | P0-1 through P0-9 overlap with D-K physics fixes. Coordinate. |
| 0314 (Multi-Reader Audit) | This plan is the fix list derived from 0314's findings. |
| 0158 (Fresh Read Audit) | Compare findings after Phase 3. |
| PTL-115 | All fixes serve PTL-115 (book science sections). |
| PTL-109 | P3 polish items may overlap with D-K editorial sweep. |
