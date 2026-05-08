# Plan 0302: Firmware Update — Publishable-Grade Scholarship Audit

**Status:** READY FOR GENERATOR (Phase 1 first)
**Priority:** HIGH — scholarship corrections to the book's scientific credibility anchor
**Source:** S68 DOI verification during Plan 0297 annealing exposed reference errors
**Decision:** Fix all scholarship issues before new content (Plans 0297/0301) builds on this foundation

## Context

The Firmware Update chapter (`manuscript/track-3-awakening/firmware-update.tex`, 180 lines) is the book's scientific credibility anchor. The standalone copy-button source (`science-primer-for-llms.md`) has diverged: two wrong DOIs (bibliography only — inline partially fixed), wrong "demonstrated" claim for a theoretical paper, different Anchor 10 citation, "Si MOSFETs" instead of "Si/SiGe heterostructures."

Plan 0113 fixed these DOIs in firmware-update.tex but never propagated to science-primer-for-llms.md or derived files. The book chapter is correct; the standalone and derived files are not.

## Verified Findings

DOIs verified via live web resolution on 2026-05-08. All findings confirmed, not suspected.

---

## Phase 1: Fix science-primer-for-llms.md (copy-button source)

**File:** `~/software/relinquishment/science-primer-for-llms.md`

This file feeds the "Copy Science Reference" button via `build/preprocess.py` line 2156.

**1a. Fix Dean DOI in bibliography (line 103):**

Old:
```
1. Dean, C.R. et al. "Multicomponent fractional quantum Hall effect in graphene." Nature Physics 7, 693–696 (2011). doi:10.1038/nphys1938
```

New:
```
1. Dean, C.R. et al. "Multicomponent fractional quantum Hall effect in graphene." Nature Physics 7, 693–696 (2011). doi:10.1038/nphys2007
```

Note: Anchor 1 inline (line 25) already has the correct DOI (nphys2007). Verify; if wrong, fix there too.

**1b. Fix Freedman DOI (line 31 inline + line 105 bibliography):**

Line 31 — Old:
```
[Qualified — doi:10.1007/s00220-002-0698-z]
```
New:
```
[Qualified — doi:10.1007/s002200200635]
```

Line 105 — Old:
```
3. Freedman, M., Kitaev, A. & Wang, Z. "Simulation of topological field theories by quantum computers." Comm. Math. Phys. 227, 587–603 (2002). doi:10.1007/s00220-002-0698-z
```
New:
```
3. Freedman, M., Kitaev, A. & Wang, Z. "Simulation of topological field theories by quantum computers." Comm. Math. Phys. 227, 587–603 (2002). doi:10.1007/s002200200635
```

**1c. Fix "demonstrated" → "predicted theoretically" (Anchor 8, line 57):**

Old:
```
have been demonstrated in magnetized plasmas
```
New:
```
have been predicted theoretically in magnetized plasmas
```

**1d. Fix "Si MOSFETs" → "Si/SiGe heterostructures" (Anchor 1, line 25):**

Old:
```
Observed in graphene, ZnO, Si MOSFETs
```
New:
```
Observed in graphene, ZnO, Si/SiGe heterostructures
```

**1e. Sync Anchor 10 with book (lines 34-35 + bibliography item 13):**

Old Anchor 10 (lines 34-35):
```
**Anchor 10 — Coherence Precedent.** Room-temperature quantum coherence is experimentally established. NV-diamond and SiC devices maintain coherent quantum states at 300K in commercial products. Not theoretical — deployed. [Established — doi:10.1038/nmat4145]
*Christle et al., Nature Materials 2015*
```

New:
```
**Anchor 10 — Coherence Precedent.** Room-temperature quantum coherence is experimentally established. NV-diamond and SiC devices maintain coherent quantum states at 300K in commercial products. Not theoretical — deployed. [Established — doi:10.1038/nmat2420; doi:10.1126/sciadv.1501015]
*Balasubramanian et al., Nature Materials 2009; Klimov et al., Science Advances 2015*
```

Old bibliography item 13 (line 115):
```
13. Christle, D.J. et al. "Isolated electron spins in silicon carbide with millisecond coherence times." Nature Materials 14, 160–163 (2015). doi:10.1038/nmat4145
```

New (replace item 13 with two items):
```
13. Balasubramanian, G. et al. "Ultralong spin coherence time in isotopically engineered diamond." Nature Materials 8, 383–387 (2009). doi:10.1038/nmat2420
14. Klimov, P.V. et al. "Quantum entanglement at ambient conditions in a macroscopic solid-state spin ensemble." Science Advances 1(10), e1501015 (2015). doi:10.1126/sciadv.1501015
```

**Build + push after Phase 1.**

**Idempotency:** If science-primer-for-llms.md contains "s002200200635" (Freedman correct DOI) AND "predicted theoretically" AND "Balasubramanian" — phase is applied.

**Commit:** `Plan 0302 Phase 1: fix science-primer-for-llms.md (DOIs, terminology, citations)`

---

## Phase 2: Fix firmware-update.tex (book chapter)

**File:** `~/software/relinquishment/manuscript/track-3-awakening/firmware-update.tex`

**2a. F1 — "demonstrated" → "predicted theoretically" (Anchor 8, line 81):**

Old:
```latex
Topological band structures and edge modes have been demonstrated in magnetized plasmas.
```
New:
```latex
Topological band structures and edge modes have been predicted theoretically in magnetized plasmas.
```

**2b. F2 — Google 2023 citation (Distinction #6, line 34):**

First, add BibTeX entry to `~/software/relinquishment/manuscript/bibliography.bib`:
```bibtex
@article{andersen2023,
  author = {Andersen, T. I. and others},
  title = {Non-Abelian braiding of graph vertices in a superconducting processor},
  journal = {Nature},
  volume = {618},
  pages = {264--269},
  year = {2023},
  doi = {10.1038/s41586-023-05954-4}
}
```

Then in firmware-update.tex line 34, change:

Old:
```latex
Anyon braiding: demonstrated 2023 (Google).\footcite{nayak2008}\footcite{kitaev2003}
```
New:
```latex
Anyon braiding: demonstrated 2023 (Google Quantum AI).\footcite{andersen2023}\footcite{nayak2008}\footcite{kitaev2003}
```

Note: `\footcite{andersen2023}` goes FIRST — it is the actual experiment. nayak2008 and kitaev2003 are retained as background theory.

**2c. F3 — "Si MOSFETs" → "Si/SiGe heterostructures" (Anchor 1, line 47):**

Old:
```latex
Observed in graphene, ZnO, Si MOSFETs --- not only GaAs.
```
New:
```latex
Observed in graphene, ZnO, Si/SiGe heterostructures --- not only GaAs.
```

**2d. F4 — "energy gap, not temperature" (Criticality Bridge, line 99):**

Old:
```latex
Topological protection depends on energy gap, not temperature.
```
New:
```latex
Topological protection depends on the energy gap exceeding thermal energy ($\Delta \gg k_BT$).
```

**2e. F5 — Add Vattay et al. to manual bibliography:**

After item 14 (Klimov), add:
```latex
\item Vattay, G., Kauffman, S.\ \& Niiranen, S.\ ``Quantum Biology on the Edge of Quantum Chaos.'' \textit{PLoS ONE} 9(3), e89017 (2014). doi:10.1371/journal.pone.0089017
```

Note: The text (line 99) already says "proposed" for the Vattay claim — no additional qualifier needed.

**2f. F6 — Add Sze & Ng to manual bibliography:**

After Vattay, add:
```latex
\item Sze, S.M.\ \& Ng, K.K.\ ``Physics of Semiconductor Devices.'' 3rd ed.\ Wiley (2007). ISBN 978-0-471-14323-9
```

**2g. F7 — Add Google 2023 to manual bibliography:**

After Sze & Ng, add:
```latex
\item Google Quantum AI (Andersen, T.I.\ et al.)\ ``Non-Abelian braiding of graph vertices in a superconducting processor.'' \textit{Nature} 618, 264--269 (2023). doi:10.1038/s41586-023-05954-4
```

(Total bibliography: 17 items after Phase 2.)

**2h. F8 — Arnold Nobel Lecture URL (item 5, line 152):**

Old:
```latex
\item Arnold, F.H.\ Nobel Lecture: ``Innovation by Evolution'' (2018).
```
New:
```latex
\item Arnold, F.H.\ Nobel Lecture: ``Innovation by Evolution'' (2018). \url{https://www.nobelprize.org/prizes/chemistry/2018/arnold/lecture/}
```

Note: `\url{}` requires the `hyperref` package — verify it is loaded (it almost certainly is, given existing `\hyperref` usage).

**2i. F9 — MOSFET 2DEG passage precision (line 95):**

Old:
```latex
The 2DEG is not an exotic laboratory curiosity --- it is the substrate of every semiconductor device on Earth.
```
New:
```latex
The 2DEG is familiar technology --- every MOSFET contains one. What differs is the operating regime: at millikelvin temperatures under strong magnetic fields, the same substrate hosts the exotic collective states described above.
```

**2j. F10 — Line 19 credibility claim:**

Old:
```latex
Every claim is verifiable via the DOIs in the bibliography.
```
New:
```latex
Every physics result cited below is verifiable via the DOIs in the bibliography. Where this chapter draws connections between published results, it says so explicitly.
```

**Build + push after Phase 2.**

**Idempotency:** If firmware-update.tex contains "predicted theoretically in magnetized plasmas" AND "andersen2023" AND "Si/SiGe heterostructures" — phase is applied.

**Commit:** `Plan 0302 Phase 2: firmware-update.tex scholarship fixes (10 items)`

---

## Phase 3: Propagate DOI fixes to contaminated files

Simple find-and-replace in each file. Two substitutions:
- `nphys1938` → `nphys2007` (Dean)
- `s00220-002-0698-z` → `s002200200635` (Freedman)

**3a. hover-definitions.yaml:**
File: `~/software/relinquishment/build/hover-definitions.yaml`
Search for `nphys1938`. If found, replace with `nphys2007`.
Search for `s00220-002-0698-z`. If found, replace with `s002200200635`.

**3b. Spiral abstracts:**
- `~/software/relinquishment/spiral-abstracts/01-genesis.md` — both DOIs
- `~/software/relinquishment/spiral-abstracts/04-cryptanalysis.md` — Freedman DOI
- `~/software/relinquishment/spiral-abstracts/06-exodus.md` — Dean DOI

**3c. thermal-ladder-analysis.md:**
File: `~/software/relinquishment/thermal-ladder-analysis.md`
Both DOIs.

**3d. Argus memory file:**
File: `~/software/aurasys-memory/memory/reference-physics-anchors.md`
Both DOIs. Also fix:
- `Si MOSFETs` → `Si/SiGe heterostructures` (Anchor 1 line)
- `demonstrated in magnetized plasmas` → `predicted theoretically in magnetized plasmas` (Anchor 8 line)
- Replace Christle citation with Balasubramanian + Klimov (Anchor 10)

**3e. Verification sweep:**
After all fixes, run:
```bash
grep -rn "nphys1938" ~/software/relinquishment/ --include="*.md" --include="*.tex" --include="*.yaml"
grep -rn "s00220-002-0698-z" ~/software/relinquishment/ --include="*.md" --include="*.tex" --include="*.yaml"
```
Both should return ZERO results. If hits remain in `abstracts-standalone-v*.txt` files — those are archived historical versions, skip them.

Also run:
```bash
grep -rn "nphys1938\|s00220-002-0698-z" ~/software/aurasys-memory/ --include="*.md"
```
Should return ZERO results.

**Build after Phase 3** (the hover-definitions.yaml fix will propagate to hover-generated.tex on rebuild).

**Idempotency:** If the grep sweeps return 0 results (excluding archived .txt files) — phase is applied.

**Commit (relinquishment repo):** `Plan 0302 Phase 3: propagate DOI fixes to derived files`
**Commit (aurasys-memory repo):** `Plan 0302 Phase 3: fix DOIs and terminology in physics anchors memory`

---

## Phase 4: Build + Full Verification

```bash
cd ~/software/relinquishment && make dev
```

Verification checklist:
- [ ] Build compiles clean
- [ ] `verify-deep-links.py` passes
- [ ] firmware-update.tex: "predicted theoretically" in Anchor 8
- [ ] firmware-update.tex: `\footcite{andersen2023}` in Distinction #6
- [ ] firmware-update.tex: "Si/SiGe heterostructures" in Anchor 1
- [ ] firmware-update.tex: "$\Delta \gg k_BT$" in Criticality Bridge
- [ ] firmware-update.tex: bibliography has 17 items
- [ ] firmware-update.tex: Arnold item has `\url{}`
- [ ] firmware-update.tex: 2DEG passage says "familiar technology" not "every semiconductor device"
- [ ] firmware-update.tex: line 19 says "physics result cited below" not "Every claim"
- [ ] science-primer-for-llms.md: no `nphys1938`, no `s00220-002-0698-z`, no `nmat4145`
- [ ] science-primer-for-llms.md: Anchor 10 = Balasubramanian + Klimov
- [ ] grep sweep: zero hits for wrong DOIs in .md/.tex/.yaml files
- [ ] No regression in chapter content or other chapters

Push both repos.

**Commit:** `Plan 0302 Phase 4: build verification` (if any fix-ups needed; otherwise no commit)

---

## Acceptance Criteria

- [ ] A condensed matter referee reading the Firmware Update would find zero factual errors
- [ ] Every DOI in both bibliographies resolves to the paper claimed
- [ ] Every claim either (a) is verifiable via cited DOIs, or (b) is explicitly marked as the book's analysis
- [ ] The copy-button source distributed to AI systems has correct DOIs and citations
- [ ] No new content added — this plan is strictly a quality audit and fix

## What This Plan Does NOT Do

- Does not add Reconstruction Paths (Plan 0301)
- Does not create the bridge easter egg (Plan 0297)
- Does not modify Spiral Abstracts content (only fixes DOIs in their metadata)
- Does not add new anchors or remove existing ones
- Does not change the chapter's structure or voice
- Does not fix archived `abstracts-standalone-v*.txt` files (historical)

## Annealing Record

**Round 1 (HIGH): Are the DOI findings reliable?**
Yes. All DOI verifications done by live web resolution on 2026-05-08:
- Dean: nphys1938 → Bojowald (black holes). nphys2007 → Dean (FQHE graphene). Book correct.
- Freedman: s00220-002-0698-z → Elbau & Graf. s002200200635 → Freedman et al. Book correct.
- Christle: nmat4145 → Widmann (different SiC paper). Book avoids by using Balasubramanian+Klimov.
- Fu & Qin: confirmed theoretical-only (analytical + numerical, no experiments).

**Round 2 (HIGH): Does F10 (softening line 19) weaken the chapter?**
No. The current claim is too strong — original analysis (The Equivalence, Anchor 7 mapping) isn't "verifiable via DOIs." The softened version is more honest AND more defensible. The Equivalence is already labeled "[Structural analogy]" with "open question" language. Softened line 19 makes the scope explicit.

---

*Plan 0302 v2, rewritten S68, 2026-05-08. Auditor: Argus.*
*v1: DRAFT at 55% with EMERGENCY framing. v2: Generator-ready, tone corrected, exact edit specs, Bruce decisions incorporated.*
