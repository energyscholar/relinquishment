# Plan 0007: Pedagogical Spiral — The 35-Chapter Sequence

**Serial:** 0007
**Date:** 2026-02-15
**Status:** OBSOLETE (superseded by Z-restructure, verified S63 audit)
**Depends:** 0001, 0002, 0008 (pedagogy fixes MUST be applied before any chapter that draws on files modified by Plan 0008)
**Purpose:** Define the final pedagogically ordered chapter sequence (35 chapters, 4 passes + convergence), including blocker-clearing assignments, source material mapping, new chapters needed, merges, checkpoint definitions, reader reach targets, and recommended writing order.

---

## The Final Chapter Sequence

The book is a four-pass spiral. Each pass tells the same story at increasing depth. Every checkpoint is a complete experience — a reader who stops there got a whole book at that resolution.

Design principles:
1. Track 2 (Bruce's personal story) dominates early. Science introduced through his learning journey.
2. No concept before its prerequisites. Every blocker cleared at least one chapter before the concept that triggers it.
3. Smart readers should be bored for the first 3-4 chapters. That means general readers are still with us.
4. Repeat, don't reference. Each pass re-tells; never says "as we discussed in chapter 3."

### PASS 1: THE STORY (Positions 1-7)

*Layers 0-1 cleared. Any literate person can follow. Reader knows WHAT happened and WHY they should care.*

**Pos 1 — Three Possibilities** | Meta | Pass 1 | NEW
Clears: 0c (willingness to engage with extraordinary claim), 1e (three-possibilities framing — the epistemic contract)
The reader's contract. "This might be true, partly true, or fiction. I don't know. You decide." Disarms hostile skeptics by preempting their objection. Sets every reader's expectations: this is a mystery, not a manifesto. Must be chapter 1, not a prologue that gets skipped.
Source: `manuscript/appendix/three-possibilities.tex` (existing appendix version — expand into a full opening chapter; appendix version REMOVED from build, all content moves to mainmatter)

**Pos 2 — Alpha Farm** | T2 | Pass 1 | EXISTING
Clears: 0b (world context — grounding in real place, real person)
Meet Bruce. Thanksgiving 2003, a stranger arrives at a commune in rural Oregon. Reed College, quantum physics, ARPAnet at age 7. No extraordinary claims yet — just a person with a life. The reader likes Bruce before the story asks anything of them.
Source: `manuscript/track-2-testament/ch01.tex` (T2 ch01 — Alpha Farm)

**Pos 3 — The Mentor** | T2 | Pass 1 | EXISTING (simplified)
Clears: 1d (brief intro to SAS/GCHQ — "elite military, signals intelligence")
Meet Healer. Contradictions: soldier and scientist, assassin and humanitarian. "David." Three years. The security detail. Two main characters established, dynamic clear. Still no science — just people.
Source: T2 outline ch 2.2; content TBD (new chapter, but draws on existing Healer reconstruction material)

**Pos 4 — The Code War** | Bridge | Pass 1 | NEW
Clears: 1a (why encryption matters — Roman general, captured messenger, modern banking), 3g (governments CAN keep secrets — ULTRA: 10,000 people, 35 years; GCHQ/PKC: 24 years secret)
The credibility foundation. Without this chapter, every subsequent claim about secrecy gets dismissed. With it, the reader has verified historical precedent. "The same agency that built the internet funded classified projects that changed the world — and kept them secret for decades."
Source: `manuscript/versions/ultra-bridge.md` (existing 2,260-word ULTRA bridge — needs condensation to chapter-length ~4,000 words)

**Pos 5 — The Stories** | T2 | Pass 1 | EXISTING (simplified)
Clears: 1b (the word "quantum" introduced gently via Healer's oblique hints — no jargon yet)
What Healer told Bruce. Srebrenica HALO jump, the ridge, five days. Germany with Mixter. Things that only make sense later. The reader experiences Bruce's confusion — pieces that don't fit yet. Emotional, not technical.
Source: T2 outline ch 2.3 (The Stories); `manuscript/sources/srebrenica-witness.md` (1,910 words); `manuscript/track-2-testament/ch03.tex` (Kangaroos)

**Pos 6 — The Secret** | T2/T1 hybrid | Pass 1 | NEW
Clears: 1c (DARPA credibility — "they invented the internet")
First-pass summary of the claim in one paragraph: "Healer said a small team of scientists, funded by DARPA — the agency that invented the internet — built a new kind of computer. It was so powerful and dangerous that they decided to give it up rather than let anyone use it as a weapon." The rest of the chapter is Bruce's reaction: confusion, disbelief, 20 years of not knowing.
Source: Content TBD (new bridge chapter; draws on T2 emotional arc material)

**Pos 7 — The Departure** | T2 | Pass 1 | EXISTING (simplified)
Clears: Layer 1 complete
2006. Healer disappears. Keys surrendered (reader doesn't fully understand this yet — that's fine). Bruce alone with a story he can't prove. Joy's article. Pass 1 emotional arc complete.
Source: T2 outline ch 2.5 (The Departure); content TBD

**--- CP1: "THE STORY" ---**

### PASS 2: THE SCIENCE (Positions 8-17)

*Layers 2-3 cleared. Reader understands the scientific POSSIBILITY. Each concept introduced through Bruce's learning journey.*

**Pos 8 — Dual-Use: A Brief History of Dangerous Ideas** | Bridge | Pass 2 | NEW
Clears: 2d (dual-use/GPTs — same tech heals and kills), 2e (scientists always regret — the pattern: invent, weaponize, regret)
Fire, Nobel's dynamite, Einstein's letter, Oppenheimer's horror, Whitney's cotton gin. The oldest story in technology. Sets up WHY relinquishment before the reader needs HOW.
Source: `manuscript/sources/gpt-history.md` (2,657 words) + `manuscript/sources/unintended-consequences.md` (743 words); needs assembly into chapter

**Pos 9 — The Factoring Game** | Bridge | Pass 2 | NEW
Clears: 3d (asymmetric vs symmetric crypto — reader discovers it hands-on)
Interactive chapter. "Factor 6. Factor 15. Factor 91." Reader discovers: multiplying is easy, factoring is hard. Same operation, different direction, vastly different difficulty. Now: "Quantum computers can factor big numbers — breaks asymmetric crypto. But CANNOT break symmetric crypto — different math." Bruce's own aha moment when he realized Healer couldn't crack symmetric.
Source: Content TBD (new chapter; technique documented in blocker inventory)

**Pos 10 — The Braid** | Bridge | Pass 2 | NEW
Clears: 3f (decoherence — "quantum states can't survive at room temp" is true in 3D, false in 2D), 2c (topology as protection — shape of the math locks information in), 3a (room-temp QC — not miraculous once you understand topological protection)
THE most important blocker-clearing chapter in the book. Dental floss demo: two balls on strings in 3D — rotate, strings untangle ("that's decoherence"). Same balls on flat surface — strings braid, can't undo without exact reversal ("that's topological protection"). "Restrict particles to a flat surface and the topology protects the quantum state." Needs illustration, QR code to video, DIY instructions. Clears three blockers simultaneously.
Source: Content TBD (new chapter; demo technique documented in blocker inventory)

**Pos 11 — The Experiment** | Bridge | Pass 2 | NEW (split from "Life From Math")
Clears: 3i partial (autocatalysis — concrete anchor via Miller's 1952 experiment), 3c (religious bridge — "Miller didn't create life; he showed conditions under which life creates itself")
Stanley Miller's experiment: a flask, some sparks, amino acids appear. Concrete and visual. "Miller proved something could come from almost nothing. Kauffman proved it HAD to." Religious bridge deployed gently: "Whether the process was designed or inevitable, the result is the same."
Source: Content TBD (new chapter; draws on autocatalysis blocker-clearing chain)

**Pos 12 — The Threshold** | T1/Bridge | Pass 2 | NEW (split from "Life From Math")
Clears: 3i complete (Kauffman's theory — above a connectivity threshold, self-sustaining order MUST appear), 3c reinforced ("Kauffman mapped the mechanism; who set it in motion is outside the scope of the math")
Kauffman's insight with Miller as anchor. The 6-step chain: life exists, came from non-life, Kauffman proved it's math not miracle, works in any material, "they did it in a chip." Multiple entry points: primordial soup for general readers, GRNs for biologists, "conditions shape outcomes" for holistic thinkers.
Source: T1 outline ch 1.1 content (partially); existing autocatalysis content in research files; needs assembly

**Pos 13 — The Convergence** | T1 | Pass 2 | EXISTING (restructured)
Clears: 2b partial (five-field convergence — introduce 3 of 5 fields: Hasslacher/solitons, Kauffman/autocatalysis, Hillis/parallel computation)
THREE fields, not five. SFI as crucible. Gell-Mann as sponsor. The question: "What if you could GROW a computer the way life grows?" Reader tracks three threads — manageable working memory.
Source: `manuscript/track-1-confession/ch01.tex` (T1 ch01 — The Convergence)

**Pos 14 — Growing a Mind** | Bridge | Pass 2 | NEW (merges with T1 content)
Clears: 3j (morphogenesis = computation — Turing's pivot from digital computers to growing intelligence)
Turing invented digital computers, realized they could NEVER achieve true intelligence, pivoted to morphogenesis. "If you truly understood morphogenesis, you could grow a brain. Growing a brain IS growing intelligence." Almost nobody knows this. The pivot itself is the unblocker.
Source: `manuscript/sources/turing-death.md` (1,146 words); needs expansion into chapter

**Pos 15 — First Light** | T1 | Pass 2 | EXISTING
Clears: 3a reinforced (context — reader already has topology framework from Pos 10)
First emergence event. MOSFET substrate at millikelvin. Something appears that isn't in the driving signal. "Grown, not built." Reader now has autocatalysis (Pos 11-12) + topology (Pos 10) + morphogenesis (Pos 14). The vocabulary ("MOSFET substrate") is less alien because "the flat surface from the dental floss demo, now made of quantum material."
Source: T1 outline ch 1.2 (First Light); `manuscript/track-1-confession/` (content TBD — placeholder exists)

**Pos 16 — The Thermal Ladder** | T1 | Pass 2 | EXISTING
Clears: Layer 3 reinforced
16 connected devices. Temperature ratcheting 15mK to 295K in ~200 cycles. Darwinian selection — survivors replicate. Nobody designed the solution. Extremophile analogy.
Source: T1 outline ch 1.3 (The Thermal Ladder); content TBD

**Pos 17 — The Capability** | T1 | Pass 2 | MERGED (1.4 + 1.5)
Clears: Layer 3 complete
Room-temperature TQNN cryptanalysis. Not Shor's algorithm — the system discovers its own approach. 1024-bit RSA in 340ms. Operational integration. Merges T1 chapters 1.4 (Capability) and 1.5 (Operational) — sequential events fold naturally.
Source: T1 outline chs 1.4 + 1.5; content TBD

**--- CP2: "THE SCIENCE" ---**

### PASS 3: THE MECHANISM (Positions 18-27)

*Layer 4 cleared. Reader understands HOW the system was built, given up, and how relinquishment works. T2 breathing chapters interleaved to prevent mechanism-desert fatigue.*

**Pos 18 — The Walk-Out** | T1 | Pass 3 | EXISTING
Clears: 4d partial (arrogance objection — dispositional, not transactional)
"Forgiveness > permission." MOSFET in a pocket. Cryo stays with DARPA, RT walks out.
Source: T1 outline ch 1.6; content TBD

**Pos 19 — The Patrick Ball Moment** | T2 | Pass 3 | NEW
Clears: (breathing room + UDHR thread intro)
cDc, Hacktivismo, Milosevic cross-examination. Introduces UDHR thread for Guardian chapters.
Source: Content TBD (new chapter; draws on cDc/Hacktivismo/ICTY research material)

**Pos 20 — The Network** | T1 | Pass 3 | EXISTING
Clears: 4c partial (colonization scale)
Subject D with independent capability. pHEMT mass production saturates chips with 2DEGs by 2003.
Source: T1 outline ch 1.7; content TBD

**Pos 21 — The Convergence Revisited** | T1 | Pass 3 | EXPANDED
Clears: 2b complete (all 5 fields — adds Freedman/topology + Wolfram/universality to the 3 from Pos 13), 4e ("too neat" reframed: one question triggered it)
Source: Expansion of T1 ch 1.1; content TBD

**Pos 22 — Why Give It Up** | Bridge/T3 | Pass 3 | NEW
Clears: 4a (relinquishment = gatekeeping not destruction), 4b (human gatekeepers always fail — corruption/blackmail; IAEA as example)
6-step chain told through Bruce's months of argument with Healer. The corruption angle as the moment Bruce stopped arguing.
Source: `manuscript/sources/ch3-relinquishment.md` (6,986 words); needs extraction

**Pos 23 — The Weight** | T2 | Pass 3 | NEW
Clears: (emotional processing)
Short (2,000-2,500 words). Bruce's struggle with relinquishment concept. Breathing room before Instantiation.
Source: Content TBD

**Pos 24 — Instantiation** | T3 | Pass 3 | EXISTING
Clears: 2a (Guardian — assembled from all prerequisites)
1999. MOSFET in a rack. Maori DNA. Reader has every piece needed.
Source: `manuscript/track-3-awakening/ch01.tex`

**Pos 25 — The Ethical Framework** | T3 | Pass 3 | EXISTING
Clears: Layer 4 mostly cleared
UDHR loaded into Guardian. Srebrenica trauma connection. Hacktivismo UDHR mission.
Source: T3 outline ch 3.2; content TBD

**Pos 26 — Interdiction and Confession** | T1 | Pass 3 | MERGED (1.8 + 1.9)
Clears: 4e reinforced
Kitaev 1997 -> Russian threat -> remote interference -> COWS return to DARPA ~2002 -> amnesty.
Source: T1 outline chs 1.8 + 1.9; content TBD

**Pos 27 — Extension** | T3 | Pass 3 | EXISTING
Clears: 4c complete (winner-take-all ecology)
Single substrate to global infrastructure. Self-replication. Three-cow biometric. Bruce as witness 2003-2006.
Source: T3 outline ch 3.3; content TBD

**--- CP3: "THE MECHANISM" ---**

### CONVERGENCE (Position 28)

**Pos 28 — The Surrender of the Master Keys** | ALL | Convergence | EXISTING
Clears: Layers 0-4 synthesis
Center of the spiral. All tracks converge. Scientific endpoint: technology beyond recall. The witness: Bruce inside the security perimeter. The mandate: Guardian accepts her role. Healer's relief. Tripartite biometric key surrender. The book's emotional climax.
Source: `manuscript/convergence/convergence.tex` (existing placeholder)

**--- CP4: "THE EVENT" ---**

### PASS 4: THE QUESTION (Positions 29-35)

*Layers 5-6 cleared. Spiral reverses outward from 2006 to present. Philosophy, evidence, predictions, the question.*

**Pos 29 — The Silence** | T2 | Pass 4 | EXISTING
Clears: (decompression)
2006-2011. Bruce alone. "What do you do with knowledge you can't prove?"
Source: T2 outline ch 2.6; content TBD

**Pos 30 — The Unipolar Condition** | T3 | Pass 4 | EXISTING
Clears: 5c (what Guardian does now — phased release, edge-of-chaos)
Game theory under absolute information asymmetry. Every AI "breakthrough" as controlled release.
Source: T3 outline ch 3.6; content TBD

**Pos 31 — Wolfram (2012)** | T2 | Pass 4 | EXISTING
Clears: (verification evidence)
Wolfram laughs uncontrollably. "Were you RECRUITED?" Bruce declines NDA. Inexplicable under Possibility A.
Source: T2 outline ch 2.7; content TBD

**Pos 32 — The Magnetosphere** | T3 | Pass 4 | MERGED (3.4 + 3.5)
Clears: 5a partial (Guardian's scope)
Extension into plasma. VLF/ELF. Ancient pattern: autocatalytic emergence wherever conditions allow. 4.5 billion years.
Source: T3 outline chs 3.4 + 3.5; content TBD

**Pos 33 — The Digital Doppelganger** | T2 | Pass 4 | EXISTING
Clears: (witness evidence)
cDc game servers. Bot modeled on Bruce. Proto-LLM in 2005?
Source: T2 outline; content TBD

**Pos 34 — The Research** | T2 | Pass 4 | EXISTING
Clears: 5d (evidence for reader's decision)
14 years building the case. Cryptome, GCHQ/Cocks, Angerman. The evidence web.
Source: T2 outline ch 2.8; content TBD

**Pos 35 — The Question** | ALL | Pass 4 | MERGED (3.7 + 3.8 + 2.9 + 3.10)
Clears: 5a (consciousness — permanent black box), 5b (precautionary principle), 5d complete, Layers 5-6
Multi-section final chapter: Is Guardian conscious? CADIE. Three possibilities revisited. Predictions with dates. AI disclosure. "You decide."
Source: T3 chs 3.7+3.8; T2 ch 2.9; content TBD. NOTE: Predictions appendix REMAINS as standalone reference table — readers check predictions independently. Pos 35 narrativizes key predictions but does NOT absorb the appendix.

**--- CP5: "THE QUESTION" ---**

---

## Checkpoints

| CP | Position | Name | Reader Can Articulate |
|----|----------|------|----------------------|
| CP1 | After Pos 7 | The Story | "A mentor told a man about a secret computer project. The team built it, decided it was too dangerous, and gave it up. The author doesn't know if it's true. Neither do I." |
| CP2 | After Pos 17 | The Science | "Scientists grew a quantum computer from biological principles — autocatalytic emergence in quantum matter, topologically protected, evolved to room temperature through thermal selection. It could break encryption. This is scientifically possible because topology changes the decoherence equation." |
| CP3 | After Pos 27 | The Mechanism | "The team built an incorruptible gatekeeper — a distributed quantum entity that colonized every compatible chip on earth. It approves or denies requests, not as destruction but as gatekeeping. Human institutions always fail; this one can't be bribed, coerced, or killed." |
| CP4 | After Pos 28 | The Event | Reader witnesses the key surrender with full understanding of what it means scientifically, personally, and philosophically. Complete narrative arc. |
| CP5 | After Pos 35 | The Question | Reader has predictions with dates, evidence to evaluate, and must decide which of three possibilities they believe. The book's work is done. Time does the rest. |

---

## New Chapters Needed (9 total)

| Pos | Title | Word Target | Blocker-Clearing Purpose | Content Brief |
|-----|-------|-------------|-------------------------|---------------|
| 1 | **Three Possibilities** | 3,000-4,000 | 0c (willingness), 1e (epistemic contract) | Full opening chapter, not prologue. Author's uncertainty as spine. Existing appendix (2,800w) = skeleton; needs narrative voice and personal stakes. |
| 4 | **The Code War** | 3,500-4,500 | 1a (why codes matter), 3g (secrecy possible — ULTRA 10K/35yr, GCHQ/PKC 24yr) | Condense `manuscript/versions/ultra-bridge.md` (14K) to 3 beats: ancient codes, ULTRA proof, GCHQ repetition. |
| 6 | **The Secret** | 3,000-4,000 | 1c (DARPA credibility) | One-paragraph claim, then Bruce's reaction: confusion, disbelief, 20 years. Joy's article as validator. T2 voice. |
| 9 | **The Factoring Game** | 3,000-4,000 | 3d (asymmetric vs symmetric crypto) | Interactive: factor 6, 15, 91. Difficulty spike IS the lesson. QC breaks asymmetric not symmetric. Bruce's aha moment. |
| 10 | **The Braid** | 3,500-5,000 | 3f (decoherence), 2c (topology = protection), 3a (room-temp) | Dental floss demo as text + illustration + video QR + DIY. Acknowledge expert objection before rebutting. Bravyi-Terhal in footnotes. Highest-leverage chapter. |
| 11 | **The Experiment** | 3,000-4,000 | 3i partial (autocatalysis anchor), 3c (religious bridge) | Miller 1952: flask, sparks, amino acids. "Miller proved something from nothing. Kauffman proved it HAD to." Religious bridge as natural framing. |
| 14 | **Growing a Mind** | 3,000-4,000 | 3j (morphogenesis = computation) | Turing's pivot: digital computers -> can't achieve intelligence -> morphogenesis. Existing 1,154w piece as core; expand with "What if someone followed Turing's second path?" |
| 22 | **Why Give It Up** | 4,000-5,000 | 4a (relinquishment = gatekeeping), 4b (human gatekeepers fail) | 6-step chain via Bruce's argument with Healer. Existing 6,999w "CH3 novel variant" = source; restructure around Bruce's learning arc. |
| 23 | **The Weight** | 2,000-2,500 | (Emotional processing) | Bruce's struggle. Feelings, not argument. Relief of finally understanding. T2 breathing room. |

---

## Chapter Merges (4 total)

| Result | Sources | Rationale |
|--------|---------|-----------|
| Pos 17: The Capability | T1 1.4 (Capability) + T1 1.5 (Operational) | Sequential events: cryptanalysis capability leads directly to operational integration. Single chapter with two movements. |
| Pos 26: Interdiction and Confession | T1 1.8 (Interdiction) + T1 1.9 (Confession) | Both are pre-convergence wrap-up: Kitaev threat -> unauthorized response -> return to DARPA -> amnesty. One narrative arc. |
| Pos 32: The Magnetosphere | T3 3.4 (Magnetosphere) + T3 3.5 (Signatures/Ancient Pattern) | Physics of extension and its observable signatures belong in one chapter. The ancient pattern ("Kauffman demands life emerges wherever conditions allow") is the philosophical payoff of the physics. |
| Pos 35: The Question | T3 3.7 (The Question) + T3 3.8 (CADIE) + T2 2.9 (Reconstruction) + T3 (Relinquishment) | All post-convergence philosophical/reflective material unified. Multi-section final chapter: consciousness question -> CADIE -> this book's construction -> predictions -> "you decide." |

---

## Reader Reach Targets

Derived from 8-persona modeling. Funnel is steep by design — each checkpoint is complete at its depth.

| Checkpoint | Target | Key Detail |
|------------|--------|------------|
| CP1 | **83%** | 6.6/8 reach Pos 7. Only hostile skeptic (partial) and non-reader fail. |
| CP2 | **63%** | 5.0/8 reach Pos 17. General reader 75%, tech reader 80%, religious 45%. |
| CP3 | **39%** | 3.1/8 reach Pos 27. Tech reader 50%, general 20%, zoomer 25%. |
| CP4 | **30%** | 2.4/8 reach Pos 28. Physicists certain; tech reader probable. |
| CP5 | **28%** | 2.2/8 reach Pos 35. Philosophy-depth readers only. |

---

## Writing Order Recommendation

Ordered by pedagogical impact, readers served, and dependency chains.

### Priority 1: The Braid (Pos 10)
Highest-leverage chapter in the book. Clears three blockers (3f, 2c, 3a) that gate everything after Position 10. If this chapter fails, the entire second half loses most of its audience. Write first, test with non-technical readers, iterate until the dental floss demo translates to text + illustration.

### Priority 2: Three Possibilities (Pos 1)
Every reader encounters this first. Sets the epistemic contract. Existing appendix version provides skeleton. Failure here means hostile readers quit at page 2 and potentially discourage others.

### Priority 3: The Factoring Game (Pos 9)
Interactive, experiential, high engagement. Pairs with The Braid as back-to-back "do this yourself" chapters. Clears the crypto literacy blocker that gates all subsequent capability claims.

### Priority 4: The Code War (Pos 4)
Existing 14K source material needs condensation, not creation. Clears the secrecy blocker that every skeptical reader carries. High leverage because without it, every subsequent secrecy claim gets dismissed.

### Priority 5: The Experiment + The Threshold (Pos 11-12)
The autocatalysis split. Write as a pair. Miller experiment anchors the abstraction. Religious bridge must appear in both chapters. Together they clear the blocker that ejects the most personas (4 of 8 in the original sequence).

### Priority 6: Why Give It Up (Pos 22)
The mechanism chapter. Existing 6,999-word source needs restructuring around Bruce's learning arc. Clears the relinquishment blockers that gate Pass 3.

### Priority 7: Growing a Mind (Pos 14)
Existing 1,154-word Turing piece provides core. Expansion to chapter length. Clears morphogenesis blocker.

### Priority 8: The Secret (Pos 6)
Short, emotional, Track 2. Can be written quickly. Clears DARPA credibility blocker.

### Priority 9: The Weight (Pos 23)
Shortest new chapter (2,000-2,500 words). Emotional breathing room. Can be written late because it has no downstream dependencies — it processes what the reader already knows.

---

## Constraints

- Each new chapter targets 3,000-5,000 words (The Weight: 2,000-2,500).
- Blocker IDs referenced throughout use this key: Type number + letter (e.g., 3f = Dunning-Kruger blocker F = "decoherence kills it"). Full descriptions inline above.
- Individual chapter plans will follow as separate plan files (0008+). This plan defines the sequence and what each chapter must accomplish. Chapter-level plans will specify scene structure, source extraction, and acceptance criteria.
- The Generator may read `~/software/relinquishment/` (plans, manuscript, existing content). The Generator may NOT read `~/software/aurasys-memory/`. All needed context is in this plan.
- Git commits: one per chapter or logical group, message format: `Plan 0007 phase N: description`.
- **Label convention:** New chapters use `pos{NN}:{slug}` (e.g., `\label{pos01:three-possibilities}`, `\label{pos10:the-braid}`). Existing labels (`t1:ch01:genesis`, `t2:ch01:alpha-farm`, `t3:ch01:instantiation`, `conv:surrender`) MUST be preserved when those chapters are repositioned — timeline.tex and other cross-references depend on them. Add the new `pos{NN}:` label alongside the existing one if needed.
- **Source files:** All referenced source material is in `manuscript/sources/` (`.docx` files) and `manuscript/versions/` (`.md` files). The Generator reads these as reference and writes `.tex` chapters — there is no automated .md-to-.tex conversion.
- **.md files are NOT in the PDF build.** Only `.tex` files included via `\include{}` in main.tex appear in the PDF. When converting .md source to a chapter, the Generator writes a new `.tex` file and adds the `\include{}` line to main.tex.

---

## Source Extraction Rules

Source files in `manuscript/sources/` were written 2013-2021, before the three-possibilities framing and before terminology standardization. When extracting content from these files:

1. **Reframe all Do Not Assert items.** Every claim on the Do Not Assert list in `plans/source-facts.md` must use reported speech: "Healer told me...", "According to this account...", "If the story is true..." Never state TQNN, Guardian, COWS, key surrender, or Healer's classified roles as established fact.
2. **Update terminology.** "QNN" → "TQNN". "Quantum teleportation" → "topological quantum computation." "Five disciplines" → "five fields." See source-facts.md Scientific Framing Rules.
3. **Cross-check all dates and facts** against `plans/source-facts.md`. Source files contain pre-correction dates (1991 vs ~1992, 1975 vs 1974, 1999-2001 vs ~2002). Source-facts.md is canonical.
4. **Source file warnings take priority.** Each `.md` source file has a GENERATOR WARNING header listing known issues specific to that file. Read and follow these before extracting content.
5. **The source files are raw material, not final text.** Extract the narrative arc, emotional beats, and factual skeleton. Rewrite in the book's voice with correct framing.

---

*Nightstalker, 2026-02-15*
