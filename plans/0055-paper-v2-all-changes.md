# Plan 0055: Criticality Paper v2 — All Changes

**Date:** 2026-03-07
**Status:** COMPLETE (verified S63 audit)
**Owner:** Generator
**Repo:** `/home/bruce/software/criticality-paper/`
**File:** `Stephenson_CrossDomainCriticality_2026.tex` (635 lines) + `.bib`
**FTM:** `/home/bruce/software/freethemath/index.html`

---

## Objective

Apply all four prepared drafts (A–D) to the paper, write the thermohaline/climate section, add missing citations, and hedge prediction claims on FreeTheMath website. All changes serve one goal: strengthen the paper for FACETS perspectives submission.

## Source Documents (Generator MUST read these)

- `~/software/aurasys-memory/research/paper-v2-draft-A-mandelbrot.md`
- `~/software/aurasys-memory/research/paper-v2-draft-B-terminology.md`
- `~/software/aurasys-memory/research/paper-v2-draft-C-hedging.md`
- `~/software/aurasys-memory/research/paper-v2-draft-D-metatron-isolation.md`
- `~/software/aurasys-memory/research/paper-v2-deep-research.md` (synthesis)
- `~/software/criticality-paper/TODO-v2.md` (thermohaline section plan)
- `~/software/aurasys-memory/research/mysak-correspondence.md` (Exchanges 6-9)
- `~/software/aurasys-memory/research/bury-correspondence.md` (Exchange 2)

---

## Order of Operations

Phases MUST execute in this order. Later phases depend on line numbers shifted by earlier phases.

### Phase 1: MD Isolation (Draft D)

**Rationale:** Structural change. Removes rows from Tables 1, 3, 4; changes domain count; restructures Appendix A. All later line references shift after this. Do first.

**Changes:**

1. **Table 1 (line 110):** Remove the row `Metatron Dynamics & Candidate (unvalidated) & See Appendix~\ref{app:correspondence} \\`

2. **Domain count (line 117):** Replace entire sentence starting "A candidate additional instance..." with: `The authors' own framework (Appendix~\ref{app:correspondence}), which motivated this survey, is presented separately and excluded from this count.`

3. **Abstract (line 44):** Change "between six and nine disciplines" to "between six and eight disciplines"

4. **Abstract (line 46):** Replace "We separately present Metatron Dynamics, a framework derived from distributed systems engineering, as a candidate additional instance in Appendix~A, classified as unvalidated given the authors' dual role." with: "The framework that motivated this investigation—derived from distributed systems engineering and presented in Appendix~A—is excluded from the survey count given the authors' dual role."

5. **Notation Divergence (line 278):** Remove ", while Metatron Dynamics defines its contraction factor $\kappa_m$" from the end of the first sentence.

6. **Table 3 (line 319):** Remove the row `Metatron & $\kappa_m$ & Contraction factor & $\kappa_m \to 1$ \\`

7. **Table 4 (line 376):** Remove the row `2024 & Metatron Dynamics & Macomber \& Stephenson \\`

8. **Introduction (after line 74):** Insert two-sentence origin pointer:
```latex
Our investigation was prompted by a specific case of apparent independent derivation (Appendix~\ref{app:correspondence}): a framework developed in distributed systems engineering whose critical-point behavior resembled established physics. We document the broader convergence pattern the resulting literature search uncovered.
```

9. **COI paragraph (line 445):** Add after first sentence: "This framework motivated the literature search underlying this survey."

10. **Appendix A (lines 453–462):** Restructure opening. New title: `\section{Metatron Dynamics: Motivating Framework}`. Add three subsections: "How This Paper Originated" (origin vignette from Draft D Section 2, ~140 words), "Framework Summary" (condensed from current text), "Disclosure" (strengthened, from Draft D Section 3). Keep correspondence demo and Ising test table unchanged below new subsections.

**Interaction check:** After this phase, Table 1 has 9 rows (was 10), Table 3 has 7 rows (was 8), Table 4 has 15 rows (was 16). Domain count says "six and eight." No "nine" anywhere.

**Verification:** Grep for "nine" in .tex file. Should appear only in "1944 and 1971" context or similar, NOT in domain counts.

---

### Phase 2: Mandelbrot Reframe (Draft A)

**Rationale:** Modifies Table 1 (now 9 rows after Phase 1) and the Finance section. Independent of other phases except Table 1 row count.

**Changes:**

1. **Classification definitions (line 79–86):** Add new category after "Empirical precursor":
```latex
\item[Foundational cross-domain contribution:] Development of a general mathematical framework (not domain-specific) whose concepts---scaling, self-similarity, power-law distributions---influenced multiple independent discovery lineages surveyed here.
```
Update "three classification categories" to "four classification categories" (verify exact count — may already list four).

2. **Table 1 (line 104, now shifted):** Replace the single `Finance & Domain transfer & Applied existing technique \\` row with two rows:
```latex
Finance (Mandelbrot 1963) & Foundational cross-domain & Fractal geometry; scaling laws \\
Finance (Peters 1994) & Domain transfer & Applied existing technique \\
```

3. **Finance section (lines 155–160, now shifted):** Replace the classification block and paragraphs with the text from Draft A Section 1. Keep lines 162 onward (Hurst exponent equation and bullet list) unchanged.

4. **Table 4 (now shifted):** Add row `1963 & Finance & Mandelbrot \\` between the 1944 Onsager row and the 1966 Kadanoff row.

5. **Optional — line 286 (now shifted):** In the Stanley paragraph, after "early econophysics contributions," consider adding clause: "a lineage traceable in part to Mandelbrot's fractal framework."

**Interaction check:** Table 1 now has 10 rows (9 after Phase 1, +1 split = 10). Table 4 now has 16 rows (15 after Phase 1, +1 Mandelbrot). The classification definition count must match the number of categories actually listed.

**Verification:** Count classification categories in Section 1.1 — should be exactly 4 (independent derivation, domain transfer, intra-field extension, empirical precursor) plus the new "foundational cross-domain contribution" = 5 total. But the current text says "three" and lists 4 + qualified. Check and fix the count to match reality.

---

### Phase 3: Thermohaline/Climate Section + Citations

**Rationale:** Adds new content. Requires .bib additions. Independent of Phases 1-2 except line numbers.

**Changes:**

1. **New section** after Traffic Flow (Section 2.8, currently ending ~line 235). Insert new subsection:

```latex
\subsection{Thermohaline Circulation / Climate Tipping Points (1961--2021)}

\noindent\textit{Classification: independent derivation within climate science; connected to physics through shared bifurcation theory but developed for domain-specific physical systems without awareness of equivalent biomedical or financial applications.}
\smallskip
```

Write 200–300 words covering the Stommel → Mysak → Rahmstorf → Lenton → Bury chain. Key content from TODO-v2.md and mysak-correspondence.md:

- Stommel 1961: two-box thermohaline circulation model, bistability
- Schmidt & Mysak 1996: multiple equilibria as cusp catastrophes
- Mysak et al. 2002 (Tellus 54A): subcritical Hopf bifurcation in Rooth three-box model — same bifurcation family as Glass 1977 cardiac pacemaker
- Wang & Mysak 2006 (Paleoceanography): MOC flip-flop as stochastic switching near bifurcation — D-O irregular periods = critical slowing down signature
- Rahmstorf et al. 2005 (GRL): 11 independent models all showing same hysteresis — convergent discovery WITHIN a domain
- Lenton et al. 2008: tipping elements framework, cites Rahmstorf/Mysak
- Bury et al. 2021 PNAS: deep learning EWS classifiers trained on normal form bifurcation data, generalize across ecology, cardiology, climate
- Bury et al. 2023 Nature Comms: validated on chick-heart tissue (Glass's system)

**The bus anecdote (use carefully):** Mysak and Glass are both McGill emeriti, both FRSC, both played in I Medici di McGill orchestra. Mysak: "I sometimes meet Leon on the bus and then I can talk about our 'related' work!" They did not know their math was the same until Bruce connected them from Costa Rica. This is the paper's thesis in one sentence. Include as a concrete example of institutional proximity without cross-domain awareness. Cite as personal communication only with Mysak's consent — Bruce has this on record (Exchange 6).

**Note on Bury's calculus analogy:** Do NOT use here. That goes in Phase 4 (terminology section). Avoid duplication.

2. **Add to Table 1 (now shifted):** New row:
```latex
Climate / Thermohaline & Independent derivation & Bifurcation analysis of AMOC \\
```

3. **Add to Table 4 (now shifted):** New rows:
```latex
1961 & Climate & Stommel \\
1996 & Climate & Schmidt \& Mysak \\
2005 & Climate & Rahmstorf et al. \\
2008 & Climate & Lenton et al. \\
2021 & Climate/DL & Bury et al. \\
```

4. **Update domain count (line 117, now shifted):** Change "six and eight" to "six and nine" — climate IS a new domain in the survey, replacing MD's slot in the count. Add climate to the enumeration.

5. **Add to .bib file** — all of these:
```
stommel1961, schmidt_mysak1996, mysak2002, wang_mysak2006,
rahmstorf2005, lenton2008, bury2021, bury2023,
wissel1984, gardiner1983, scheffer2009
```
(scheffer2009 already in .bib — verify. wissel1984 and gardiner1983 are new lineage nodes from Bury.)

6. **Add Wissel 1984 and Gardiner ~1983** to the thermohaline section or to the biomedical section as precursor references. Wissel 1984 is ecology (characteristic return time near thresholds, pre-Scheffer). Gardiner ~1983 is stochastic processes handbook. Both demonstrate the siloing — Bruce and Robin missed them from the physics/finance side.

**Interaction check:** Domain count goes back to "nine" but now it's nine LEGITIMATE surveyed domains, not eight-plus-MD. Table 1 gains a row. Table 4 gains 5 rows. The abstract's "six and eight" from Phase 1 must be updated to "six and nine" here. This is intentional — MD was removed, climate was added.

**Verification:** After this phase, grep for domain count. Abstract should say "six and nine." Body paragraph should enumerate climate as one of the nine. MD should NOT be in the count.

---

### Phase 4: Terminology Documentation (Draft B)

**Rationale:** Adds to Notation Divergence section and Table 3. Independent of other phases except line numbers.

**Changes:**

1. **After Notation Divergence section (line 280, now shifted):** Insert paraphrased calculus analogy paragraph from Draft B Section 1. Use exact LaTeX from draft. Include `(cf.\ Bury, personal communication, 2026)` — if permission not confirmed before submission, remove attribution.

2. **Table 3 (now shifted):** Add "Common name in domain" column per Draft B Section 2. Note: MD row was removed in Phase 1, so table has 7 rows. The new column adds English names for each domain's parameter.

3. **Future Directions (line 424, now shifted):** Append terminology standardization sentence from Draft B Section 3 after "producing a mapping across notations."

**Interaction check:** Table 3 now has 7 rows × 5 columns. May need `\small` or `\resizebox`. Check column widths after edit.

**Verification:** Table 3 should NOT contain an MD row. Should contain 7 rows with the new column. Calculus analogy paragraph should appear after Notation Divergence, not inside the thermohaline section.

---

### Phase 5: Prediction Hedging (Draft C)

**Rationale:** Language changes only. Does last because Appendix B line numbers may have shifted from Phase 1 (MD restructure). FTM website is separate file.

**Changes in paper (4 items):**

1. **Line 502 (now shifted):** Replace "predicts" / "predicts" with "detects the approach to" / "warns of" per Draft C item 1.

2. **Line 530 (now shifted):** Replace "predict" with "detect" per Draft C item 2.

3. **Line 546 (now shifted):** Full rewrite of Q&A answer per Draft C item 3.

4. **Line 565 (now shifted):** Full rewrite of Bottom Line per Draft C item 4.

**Changes in FreeTheMath (6 items):**

5. **index.html line 6:** Title — "Predicts" → "Warns of"
6. **index.html line 7:** Meta description — "predicting" → "detecting the approach to"
7. **index.html line 12:** OG description — "predicts" → "warns of"
8. **index.html line 17:** Twitter description — "predicting" → "detecting the approach to"
9. **index.html line 260:** Hero text — "predicts" → "warns of"
10. **index.html line 267:** Section 2 — rewrite per Draft C item 11. Add clarifying sentence.

**Do NOT change:**
- Line 176 (Sornette attribution — his claim, not ours)
- Line 344 ("predictive early warning signals" — standard terminology)
- Line 433 ("predictable outliers" — Sornette's term)
- FTM line 310 ("The math works" — no prediction claim)

**Optional:** Change FTM line 8 keywords from "tipping point prediction" to "tipping point detection, early warning signals" for consistency.

**Interaction check:** None with other phases. These are pure language swaps.

**Verification:** Grep paper for "predict" — every remaining instance should be either (a) standard terminology, (b) attribution of someone else's claim, or (c) statistical usage. No unhedged prediction claims in the paper's own voice.

---

### Phase 6: FACETS Submission Prep

**Rationale:** Research task. No file edits to the paper. Produces a new document.

**Deliverable:** Write `~/software/criticality-paper/FACETS-submission-notes.md` containing:

1. **FACETS fee schedule** — look up at https://www.facetsjournal.com/ or Canadian Science Publishing site. Note any reduced fees for independent researchers (Mysak mentioned this).

2. **Article category recommendation:** Perspectives vs. Retrospectives vs. Research Article. Based on deep research: Perspectives is the best fit. Explain why.

3. **Subject editor:** Kimberly Strong (physics, atmospheric scientist) — Mysak named her (Exchange 11). Note Mysak's credentials at FACETS (former editor, former Academy president).

4. **Submission pitch** (~200 words): Frame the paper as a perspectives piece documenting convergent discovery. Emphasize: quantitative citation analysis, historical documentation, the bus anecdote as concrete evidence, the pattern no one has mapped in full.

5. **Mysak distance rules:** Do NOT name Mysak as suggesting FACETS. Do NOT suggest Mysak as reviewer. He drew a clear boundary (via Glass, Exchange 9). Respect unconditionally.

6. **Timeline:** When to submit. Mysak said "do not revise forever." After v2 changes are applied and Bruce reviews, submit.

---

## Acceptance Criteria

1. All MD references removed from main text tables and counts
2. MD isolated in Appendix A with origin vignette
3. Mandelbrot properly elevated with new classification category
4. Thermohaline/climate section present with full Mysak chain
5. All new citations in .bib file
6. Calculus analogy paraphrased in Notation Divergence section
7. Table 3 has "Common name" column, no MD row
8. All prediction overclaims hedged in paper AND FTM website
9. Paper compiles without LaTeX errors
10. No "nine" in domain count that includes MD; "nine" OK if it includes climate
11. FACETS submission notes document exists

## Test Cases

- `grep -c "Metatron" *.tex` in Tables 1, 3, 4 = 0 hits (only in Appendix A/C and author footnote)
- `grep -i "nine" *.tex` — only in climate-inclusive domain count, not MD-inclusive
- `grep -i "predicts" *.tex` — no unhedged first-person prediction claims
- `grep -i "predicts" index.html` — 0 hits
- `pdflatex` compiles clean (warnings OK, errors NOT OK)
- Domain count in abstract matches domain count in body
- Table 1 row count matches number of domains discussed in Section 2
- Classification category count in Section 1.1 matches categories actually used in Table 1

## Commits

One commit per phase. Message format: `Plan 0055 phase N: description`

- Phase 1: `Plan 0055 phase 1: Isolate Metatron Dynamics from main text`
- Phase 2: `Plan 0055 phase 2: Reframe Mandelbrot as foundational cross-domain`
- Phase 3: `Plan 0055 phase 3: Add thermohaline/climate section + citations`
- Phase 4: `Plan 0055 phase 4: Document terminology fragmentation`
- Phase 5: `Plan 0055 phase 5: Hedge prediction claims in paper and FTM`
- Phase 6: `Plan 0055 phase 6: FACETS submission prep notes`
