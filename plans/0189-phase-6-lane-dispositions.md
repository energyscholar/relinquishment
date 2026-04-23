# Plan 0189 Phase 6 — Lane-Ownership Dispositions (Stage 1: audit only)

HEAD at audit: `0189-phase-5`.
Scope: files included in `main.tex`. Excluded: `bibliography.bib`, `versions/*.md`, `sources/*.md`, `track-1-confession/*`, `track-2-testament/*`, `track-3-awakening/*` (except `firmware-update.tex`), `bridge/*`, `convergence/*`, `interlude/*`, `staging/*`.

Classifications: DELETE (literal duplicate of owner passage), KEEP (unique contextual mention), REWRITE (paraphrase to remove canonical fragment), FLAG (structural judgment required).

---

## Lane 1 — UDHR / Never Again / Post-Atrocity

**Owner:** `manuscript/record/never-again.tex` (L39 skeleton metaphor; L43 Srebrenica→UDHR link; L45 Hacktivismo connection).

### Non-owner hits in build

1. `00-front/hook.tex:32` — "anchored the custodian's charter on the \hovertip{Universal Declaration of Human Rights} --- the principles written in 1948 to say \textit{never again}"
   - **Classification:** KEEP. Brief framing mention; hook-chapter job is to name the charter.

2. `00-front/summary.tex:197-198` — UDHR paragraph listing articles (life, privacy, freedom of thought)
   - **Classification:** KEEP. Summary-chapter role introduces all major beats; article listing is unique (owner uses skeleton metaphor, not article enumeration).

3. `00-front/summary.tex:212` — "principles written in the ruins of the worst thing humanity had ever done to itself, designed to say: \textit{never again}"
   - **Classification:** KEEP. Closing beat of UDHR section in summary; different rhetorical register from owner.

4. `00-front/introduction.tex:11` — "governed it by the Universal Declaration of Human Rights"
   - **Classification:** KEEP. Single-clause framing mention.

5. `spine/why-relinquish.tex:100` — "They gave it the Universal Declaration of Human Rights as its ethical framework and placed the master cryptographic keys... governing herself by principles written in 1948 to say \textit{never again}"
   - **Classification:** KEEP. A-spine's only UDHR mention; structurally essential; "never again" phrase is the canonical through-line that appears by design across spine.

6. `spine/capabilities.tex:61` — "The Universal Declaration of Human Rights (1948)\footcite{udhr1948} was written for nation-states... articles become operational constraints"
   - **Classification:** KEEP. Unique angle (articles-as-operational-constraints); owner does not cover this framing.

7. `record/the-walk-out.tex:31, 33` — "The COWS used the 1948 UDHR as a guide to what was, and was not, acceptable peaceful functionality." + "Why the UDHR? Because it is a post-atrocity document. Eleanor Roosevelt's committee drafted it in 1948..."
   - **Classification:** FLAG. L33 is a substantial UDHR passage (Geneva/Nuremberg contrast, Srebrenica gloss) that overlaps thematically with owner but gives distinct legal-history framing. Owner (never-again.tex) says "UDHR is her skeleton"; walk-out says "UDHR as operational guide + post-atrocity logic." Two different jobs. Keep-by-default, but Auditor may consolidate if single-source is preferred.

8. `record/the-handler.tex:53` — "In 1996, subject stood on the summit of K2 and resolved... He anchored this vow to the Universal Declaration of Human Rights."
   - **Classification:** KEEP. Character-origin beat; different lane function (Handler/Healer backstory, not Custodian ethics).

9. `record/what-healer-said.tex:169` — "A human rights statistician who testifies about genocide and advises a hacker collective dedicated to the Universal Declaration of Human Rights. That is not a contradiction. That is a through-line."
   - **Classification:** KEEP. Patrick Ball chapter closer; UDHR used as connective rhetoric.

10. `99-back/afterword.tex:47` — "Custodian requires understanding AI, five convergent sciences, enforcement, relinquishment, and the 1948 Universal Declaration of Human Rights."
    - **Classification:** KEEP. Meta-context (complexity-budget bullet), not an ethical-framework definition.

11. `appendix/timeline.tex:53` — "[1948] UN adopts the Universal Declaration of Human Rights --- later the ethical framework for a creation described below."
    - **Classification:** KEEP. Timeline-entry format; required for chronological spine.

12. `appendix/glossary-entries.tex:16, 42, 137` — Glossary definitions (Custodian, UDHR, Hacktivismo).
    - **Classification:** KEEP (×3). Glossary role; each entry is a definition, not a duplicate of owner prose.

**Lane 1 counts:** DELETE 0 · KEEP 13 · REWRITE 0 · FLAG 1 (walk-out L33).

---

## Lane 2 — DARPA 2002 Confession / Forgiveness than Permission

**Owner (DARPA 2002 reorg):** `manuscript/record/interdiction.tex` (L8-9 Grace Hopper epigraph; L46-62 2002 reorg + Tether).
**Owner (confession event):** `manuscript/record/the-surrender.tex` (L29-34 "The Confession" section).

Two owners with distinct functions: interdiction owns the Tether/QuIST mechanism; the-surrender owns the confession as narrative event. Both retained.

### Non-owner hits in build

1. `00-front/summary.tex:166` — "\"It is easier to get forgiveness than permission.\" That was their philosophy. Bill Joy would publish..."
   - **Classification:** KEEP. Unique framing (Bill Joy contrast); summary-chapter function.

2. `00-front/summary.tex:214` — "Around 2002, COWS confessed... DARPA, which was then led by Director Tony Tether. And in 2006..."
   - **Classification:** KEEP. Summary-chapter function introduces 2002 + 2006 beats; duplicates interdiction factually but plays different structural role.

3. `99-back/afterword.tex:89` — "It is easier to get forgiveness than permission. The COWS knew that. So do I."
   - **Classification:** KEEP. First-person afterword closer; unique voice (Bruce claims the phrase).

4. `99-back/colophon.tex:27` — Epigraph "\textit{It is easier to get forgiveness than permission.}"
   - **Classification:** KEEP. Structural epigraph of closing colophon; intentional through-line.

5. `record/the-departure.tex:26` — "Healer told me that he and his colleagues wanted to \"step into the light\" and say \"we did this.\""
   - **Classification:** KEEP. Distinct beat (disclosure motivation, not DARPA 2002 reorg).

6. `record/the-walk-out.tex:66` — "Under Possibility~C, \textit{it is easier to get forgiveness than permission.} This is the COWS' dispositional stance..."
   - **Classification:** KEEP. Dispositional-stance gloss unique to walk-out; owner (interdiction) is epigraph-only, no interpretive gloss.

7. `record/the-question.tex:11, 116, 138, 142` — Epigraph + interpretive riff + closing Q&A.
   - **Classification:** KEEP (×4). Closing-chapter's repeated-epigraph pattern is intentional book structure; L116 interprets the phrase for readers; L138 and L142 are the book's closing drumbeat.

8. `appendix/topic-guide.tex:85` — "DARPA Reorganization (2002): Tether, TIA, QuIST, ARDA."
   - **Classification:** KEEP. Cross-reference index entry.

9. `appendix/timeline.tex:189` — "[2002] (Author's Hypothesis) COWS get right with DARPA... \textit{It is easier to get forgiveness than permission.}"
   - **Classification:** KEEP. Timeline-entry format.

10. `appendix/abstracts.tex:123, 235, 241` — Classified-style abstract mock-ups using the phrase.
    - **Classification:** KEEP (×3). In-universe redaction document pastiche; intentional format.

**Lane 2 counts:** DELETE 0 · KEEP 13 · REWRITE 0 · FLAG 0.

---

## Lane 3 — NIOD / Patrick Ball / Srebrenica

**Owner:** `manuscript/record/what-healer-said.tex` (L106-137 Srebrenica Witness verbatim; L160-180 Patrick Ball Nexus).

### Non-owner hits in build

1. `00-front/summary.tex:235` — "It is July 1995, over the mountains of Bosnia. Below him, in a town called Srebrenica, eight thousand people are about to be murdered..."
   - **Classification:** KEEP. Summary-chapter opens with HALO beat; owner carries the Witness voice; summary paraphrases.

2. `record/alpha-farm.tex:11, 13` — HALO-jump flash-forward epigraph.
   - **Classification:** KEEP. Established structural pattern (epigraph → later expansion); not content duplicate.

3. `record/never-again.tex:43` — "I infer that the moral weight of Srebrenica informed... the choice of the UDHR"
   - **Classification:** KEEP. UDHR-lane chapter uses Srebrenica as one-sentence motivator; different function from owner.

4. `record/the-question.tex:84, 85` — Evidence bullet list (NIOD SAS-at-Srebrenica confirmation + Patrick Ball cross-examination).
   - **Classification:** KEEP (×2). Closing-chapter evidence-list role; owner does not present these as evidence bullets.

5. `appendix/topic-guide.tex:104, 105, 127` — Cross-references to owner labels.
   - **Classification:** KEEP (×3). Index-entry role.

6. `appendix/glossary-entries.tex:57` — ICTY definition referencing Patrick Ball.
   - **Classification:** KEEP. Glossary role.

7. `appendix/timeline.tex:152, 187` — Timeline entries ("[July 1995] Healer HALO-jumps..." + "[Mar 2002] Patrick Ball testifies...").
   - **Classification:** KEEP (×2). Timeline-entry format.

**Lane 3 counts:** DELETE 0 · KEEP 10 · REWRITE 0 · FLAG 0.

---

## Lane 4 — FQHE / Anyons / 5/2 State

**Owner:** `manuscript/spine/the-braid.tex` (L57 Kitaev 1997; L90 FQHE 5/2 interferometry; operational-proof argument). Substrate-definition co-owner: `spine/the-flat.tex` (L21 topological-order paragraph) — intentional two-chapter spine pair.

### Non-owner hits in build

1. `spine/the-silence-gap.tex:20, 22` — "Two-dimensional electron gases, the fractional quantum Hall effect, anyon excitations... 1998 Nobel Prize went to Laughlin, Stormer, and Tsui..."
   - **Classification:** KEEP (×2). Silence-gap owns the five-field map; FQHE appears as field-cluster label, not substrate explanation.

2. `spine/genesis.tex:63` — "A two-dimensional electron gas in a fractional quantum Hall state is not a beaker of organic molecules. But it is a system with a large number of interacting components... anyonic quasiparticles..."
   - **Classification:** KEEP. Genesis-chapter bridges Kauffman chemistry to 2DEG; FQHE context is unique to this Kauffman-parallel argument.

3. `record/first-light.tex:36, 86` — "Substrate: Cryogenic 2DEG... exhibiting the \hovertiphtml{fractional quantum Hall effect}" + "The proposition is not standard fractional quantum Hall effect at room temperature..."
   - **Classification:** KEEP (×2). First-light spec uses FQHE as substrate label; L86 argues Kauffman-style-poised-state vs standard FQHE — a distinct physics argument not in owner.

4. `track-3-awakening/firmware-update.tex:41, 91, 136` — "Anchor 3 — Braiding Universality" + qualified FQHE statements + Dean 2011 graphene reference.
   - **Classification:** KEEP (×3). Firmware primer's explicit job is to catalogue these anchors with qualifiers; the primer role.

5. `appendix/predictions.tex:70` — "Experimental confirmation of non-abelian anyons at ν = 5/2 (2026–2029)"
   - **Classification:** KEEP. Prediction-register line item.

6. `appendix/glossary-entries.tex:6, 62` — TQNN and 2DEG glossary definitions.
   - **Classification:** KEEP (×2). Glossary role.

7. `appendix/abstracts.tex:25-26, 214` — Abstract-format content using FQHE framing.
   - **Classification:** KEEP (×2). In-universe-abstract format.

**Lane 4 counts:** DELETE 0 · KEEP 13 · REWRITE 0 · FLAG 0.

---

## Lane 5 — Silence Gap / Nobody Has Looked / Empty Intersection

**Owner:** `manuscript/spine/the-silence-gap.tex` (L41 "no journal called"; L43 "Nobody asked"; full chapter is the canonical argument).

### Non-owner hits in build

1. `spine/the-flat.tex:8` — "a question five scientific fields have never put together --- an empty intersection in the literature, not a refutation"
   - **Classification:** KEEP. Prelude-framing one-line at the-flat chapter opening; positions the claim rather than duplicating owner's argument. The owner's canonical "empty intersection" phrase does appear but compressed.

2. `spine/the-wrong-substrate.tex:104, 106, 147` — "But nobody has asked the pattern-formation question. Nobody has looked at the magnetospheric plasma..." + "And nobody has looked." + chapter-closer "Nobody has looked."
   - **Classification:** FLAG. The-wrong-substrate uses the silence-gap canonical phrase "nobody has looked" as its own drumbeat — three times, including the final line of the chapter. Two plausible readings: (a) wrong-substrate is a specific instance (nobody looked at *magnetospheric* pattern formation) of the silence-gap general claim (nobody looked across five fields); keep both with the specific-vs-general split. (b) Phrase is being used in two chapters, which risks reader hearing it as repeated quote rather than cumulative argument. Auditor decision. Default-KEEP if no change: the specific/general split is defensible and chapter order (wrong-substrate before silence-gap) means wrong-substrate seeds the motif, silence-gap generalizes.

3. `spine/the-strongest-objection.tex:52` — "the quest nobody asked you to undertake"
   - **Classification:** KEEP. Unrelated usage (Tolkien-scouring context); phrase "nobody asked" is incidental English, not silence-gap canonical fragment.

**Lane 5 counts:** DELETE 0 · KEEP 3 · REWRITE 0 · FLAG 1 (wrong-substrate L104/L106/L147 drumbeat).

---

## Summary

| Lane | DELETE | KEEP | REWRITE | FLAG |
|------|--------|------|---------|------|
| 1 UDHR | 0 | 13 | 0 | 1 |
| 2 DARPA 2002 / Forgiveness | 0 | 13 | 0 | 0 |
| 3 NIOD / Patrick Ball | 0 | 10 | 0 | 0 |
| 4 FQHE / Anyons | 0 | 13 | 0 | 0 |
| 5 Silence Gap | 0 | 3 | 0 | 1 |
| **Total** | **0** | **52** | **0** | **2** |

### FLAG items for Auditor

- **F1 (Lane 1):** `record/the-walk-out.tex:33` post-atrocity UDHR paragraph. Substantial legal-history content (Geneva/Nuremberg/Srebrenica) that overlaps thematically with never-again.tex owner but plays distinct operational-guide role. Auditor decides: keep dual angles, or consolidate to never-again.tex.

- **F2 (Lane 5):** `spine/the-wrong-substrate.tex:104/106/147` "nobody has looked" drumbeat. Reads as specific instance (magnetospheric pattern formation) of the-silence-gap general claim. Chapter order is wrong-substrate → interlude → silence-gap. Auditor decides: leave as specific-seeds-general, or soften wrong-substrate to reduce phrase collision with silence-gap owner.

### Stage 1 complete

No commits. No manuscript edits. HEAD unchanged (`0189-phase-5`). Ready for Auditor review + Stage 2 prompt.
