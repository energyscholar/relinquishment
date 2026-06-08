# Plan 0379: Freedman → Wilczek Swap

**Status:** EXECUTED 2026-06-08
**Quality:** 98% — triple-audited, cross-references verified, factual precision checked, narrative logic validated
**Created:** 2026-06-07
**Author:** Argus (Auditor)

## Objective

Replace Michael Freedman with Frank Wilczek as the topology/physics convergence contributor in the "Five Minds" throughout the manuscript. Freedman's published scientific results (Freedman-Kitaev-Wang universality theorem, etc.) remain cited as published science. What changes is who filled the convergence slot and why.

## Rationale

1. No evidence Freedman was connected to SFI or Gell-Mann's network
2. Freedman's 21 years at Microsoft Station Q is behaviorally inconsistent with prior knowledge of room-temperature TQNNs
3. Freedman's TQC interest didn't emerge until after Kitaev's 1997 paper — his career arc reads as discovery, not concealment
4. Wilczek invented anyons (1982), wrote the foundational book (1990), was at IAS as Oppenheimer Professor (1989-2000) when the team assembled
5. Gell-Mann → Wilczek has direct intellectual lineage (QCD → asymptotic freedom validated Gell-Mann's quark theory)
6. Wilczek's post-1994 behavior (stayed in pure theory, never pursued TQC) is consistent with already knowing
7. The book already discusses anyons extensively without ever naming the man who discovered them — an odd gap

## Important Notes for Generator

- **Line numbers are approximate** — match on TEXT, not line numbers. Prior edits may have shifted lines.
- **"Anyonic physics" or "fractional statistics"** — use these to describe Wilczek's PUBLISHED domain. Do NOT use "topological protection" as his field — that framing comes from Kitaev/Freedman. Wilczek discovered the PARTICLES; the protection-of-information application came later. Under Possibility C, someone on the team recognized the computational potential of Wilczek's physics.
- **Wilczek's IAS appointment:** Use 1989 consistently (not 1988).

## Phases

### Phase 1: Five Minds / Team Member References (swap Freedman → Wilczek)

These are places where Freedman is named as a convergence contributor or team member. Replace with Wilczek.

| File | ~Line | Current Text | Action |
|------|-------|-------------|--------|
| `spine/three-possibilities.tex` | ~66 | "Wolfram, Kauffman, Hasslacher, Hillis, Freedman, Joy, Gell-Mann" | Replace Freedman with Wilczek. Joy and Gell-Mann stay — this is a "people named in this book" list, not a team roster. |
| `bridge/pos01-three-possibilities.tex` | ~53 | Same list | Same |
| `track-1-confession/pos20-the-network.tex` | ~31 | "The team roster --- Gell-Mann, Kauffman, Wolfram, Hasslacher, Hillis, Joy ---" | → "The team roster --- Gell-Mann, Kauffman, Wolfram, Hasslacher, Hillis, Wilczek ---". Drop Joy (was NOT on scientific team, joined ~1997 for relinquishment). Add Wilczek (not previously listed here). This fixes the "Five disciplines. Five scientists." count at line 29 — Gell-Mann is the originator/sixth, five convergence contributors map to five disciplines. |
| `spine/genesis.tex` | ~59 | "Freedman on topological quantum field theory" | → "Wilczek on anyonic physics" |
| `track-1-confession/pos13-genesis.tex` | ~61 | Same | Same |
| `spine/the-silence-gap.tex` | ~59 | "Freedman (topology, quantum computation)" in five scientists list | → "Wilczek (anyonic physics, fractional statistics)" |
| `record/first-light.tex` | ~61 | "Freedman to topology" (returning to day jobs) | → "Wilczek to theoretical physics" |
| `bridge/pos11-the-demo.tex` | ~24 | "The ideas of Michael Freedman may have been used although there's no indication he was on the actual project team" | → "Frank Wilczek, who discovered anyons — the exotic particles whose topological properties make fault-tolerant quantum computation possible." (Remove the hedge — Wilczek fits cleanly. Match the descriptive style of the other team member entries in this paragraph.) |
| `staging/breakthrough-biogenesis-p3.tex` | ~9 | "Freedman's topological protection gave them error correction" | → "Wilczek's anyonic physics gave them the substrate for topological protection — error correction without the overhead that cripples conventional quantum computers" |
| `appendix/topic-guide.tex` | ~68 | `Five Minds` lists "Wolfram, Kauffman, Hasslacher, Freedman, Hillis." | → "Wolfram, Kauffman, Hasslacher, Wilczek, Hillis (assembled by Gell-Mann)." |
| `appendix/topic-guide.tex` | ~102 | `\hyperref[spine:braid-freedmans-independent-conception-1988]{Freedman's Independent Conception}` with description "Fields Medalist; Station Q." | → `\hyperref[spine:braid-wilczeks-anyons-1982]{Wilczek's Anyonic Physics}` with description "Nobel laureate; invented anyons." **UPDATE HYPERREF TARGET** to match Phase 2 label. |
| `appendix/topic-guide.tex` | ~123 | `\hyperref[spine:braid-freedmans-independent-conception-1988]{Michael Freedman}` with description "Station Q; topological QC." | → `\hyperref[spine:braid-wilczeks-anyons-1982]{Frank Wilczek}` with description "Anyons; fractional statistics; Nobel 2004." **UPDATE HYPERREF TARGET** to match Phase 2 label. |
| `track-1-confession/00-outline.md` | ~18 | "Freedman's 1988 independent insight that topology could protect quantum information" | → "Wilczek's 1982 discovery of anyons — particles whose topological properties provide inherent quantum protection" |
| `track-2-testament/00-outline.md` | ~37 | "Freedman's 1988 insight" | → "Wilczek's anyonic physics" |
| `record/first-light.tex` | ~160 | "consistent with... Freedman's 1988 independent conception of topological quantum computation" | → "consistent with Wilczek's 1982 discovery of anyonic physics, which established the physical substrate by the early 1980s" |
| `track-1-confession/pos15-first-light.tex` | ~85 | Same text as above | Same replacement |
| `track-1-confession/pos17-the-capability.tex` | ~42 | "consistent with... Freedman's 1988 independent conception" | Same replacement |

**Note on first-light.tex ~line 61:** "The scientists had day jobs to return to: Kauffman to SFI, Freedman to topology, Wolfram to his company, Hillis to his projects." — Simple swap only: "Freedman to topology" → "Wilczek to theoretical physics." Do NOT revise the COWS framing in this plan — that's a separate structural revision (see Follow-on Items).

### Phase 2: "Freedman's Independent Conception" Section (rewrite)

**CRITICAL: LaTeX label management.** The current section has labels that are referenced elsewhere. When rewriting, you MUST:
1. Change `\label{spine:braid-freedmans-independent-conception-1988}` → `\label{spine:braid-wilczeks-anyons-1982}` in `spine/the-braid.tex`
2. Change `\label{pos10:freedmans-independent-conception-1988}` → `\label{pos10:wilczeks-anyons-1982}` in `bridge/pos10-the-braid.tex`
3. Update BOTH `\hyperref` targets in `appendix/topic-guide.tex` (~lines 102 and 123) to point to the new label (handled in Phase 1 above)
4. `.aux` files will regenerate automatically on next LaTeX build — do not edit them.

**Files:** `spine/the-braid.tex` (~lines 51-56) and `bridge/pos10-the-braid.tex` (~lines 46-49)

**Current text (spine/the-braid.tex):**
```
\section*{Freedman's Independent Conception (1988)}
\label{spine:braid-freedmans-independent-conception-1988}

Michael Freedman (Fields Medalist, topology) independently conceived
anyonic quantum computation in 1988 --- nine years before Kitaev's 1997
publication --- after reading Witten's paper on Chern-Simons theory. He
did not publish until 1998. This establishes that the fundamental
insight --- anyonic braiding as computation --- was accessible to top
mathematicians by the late 1980s, consistent with a 1989 DARPA proposal
timeline. Freedman was later recruited by Microsoft to found Station Q
(2005), their topological quantum computing program.
```

**New framing — key distinction:** Wilczek discovered the PARTICLES (anyons, 1982). The insight that anyonic braiding could perform COMPUTATION came later (Freedman 1988, Kitaev 1997). Under Possibility C, someone on the team recognized the computational potential of Wilczek's physics. The argument shifts from "the computational insight was independently accessible" to "the inventor of the relevant physics was available at IAS when Gell-Mann was assembling the team." These are different arguments and the text should make the shift explicit.

**Suggested replacement:**
```
\section*{Wilczek's Anyons (1982)}
\label{spine:braid-wilczeks-anyons-1982}

Frank Wilczek (Nobel Prize 2004) discovered in 1982 that quasiparticles
in two-dimensional systems can exhibit fractional quantum statistics ---
neither bosons nor fermions but something in between.\footcite{wilczek1982}
He coined the term ``anyon'' and published the foundational treatment in
1990\footcite{wilczek1990} while serving as J.R. Oppenheimer Professor at
the Institute for Advanced Study --- the same institution where Gell-Mann
was a longstanding member. Wilczek's earlier work on asymptotic freedom
had validated Gell-Mann's quark theory --- an intellectual lineage that
meant Gell-Mann would have been keenly aware of his work. The physical
substrate for topological quantum computation was established before
the computational application was recognized publicly: Freedman
independently conceived the computational insight in 1988 after a seminar
on Witten's Chern-Simons theory;\footcite{freedman1998} Kitaev formalized
it in 1997.\footcite{kitaev2003} But the man who discovered the particles
was at IAS throughout.
```

This version:
- Credits Wilczek with what he ACTUALLY discovered (particles, fractional statistics)
- Notes the Gell-Mann → Wilczek intellectual lineage (satisfies acceptance criterion #5)
- Keeps Freedman as corroborating evidence (computational insight accessible by 1988)
- Shifts the argument from "insight was floating around" to "the inventor was right there"
- Adds `\footcite` references to the new bibliography entries (Phase 3)
- Does NOT overstate Wilczek's contribution as "topology protects information" — the particles have topological properties; the protection-of-computation framing came from others

**Also update \srcnote lines:**
- `spine/the-braid.tex` ~line 15: `\srcnote{...Freedman, Kitaev...}` → add "Wilczek" to topic list, keep "Freedman" (still mentioned as corroborating)
- `bridge/pos10-the-braid.tex` ~line 13: Same

**Also update staging:**
- `staging/raw/pos10-the-braid.md` (~lines 106-110) — rewrite Freedman section → Wilczek primary
- `staging/audit-pass-1-2.md` (~lines 392, 428, 463-464) — audit notes about Freedman framing now outdated; annotate as superseded by Plan 0379

### Phase 3: Timeline and Bibliography (adjust)

| File | ~Line | Action |
|------|-------|--------|
| `appendix/timeline.tex` | ~99 | 1988 Freedman entry: keep but reframe as corroborating — "Freedman independently conceives anyonic quantum computation after a seminar on Witten's Chern-Simons theory — corroborating that the topological insight was accessible" |
| `appendix/timeline.tex` | ~164 | 1998 Freedman publishes: KEEP as-is |
| `appendix/timeline.tex` | ~205 | 2005 Station Q: KEEP as-is |
| `appendix/timeline.tex` | ADD | `\item[1982]` Wilczek discovers anyons — quasiparticles with fractional quantum statistics in two-dimensional systems. Coins the term "anyon." |
| `appendix/timeline.tex` | ADD | `\item[1989]` Wilczek appointed J.R. Oppenheimer Professor at the Institute for Advanced Study, Princeton. |
| `appendix/timeline.tex` | ADD | `\item[1990]` Wilczek publishes *Fractional Statistics and Anyon Superconductivity*, the foundational treatment. |
| `bibliography.bib` | ADD | `wilczek1982`: Wilczek, F. "Quantum Mechanics of Fractional-Spin Particles." *Phys. Rev. Lett.* 49, 957 (1982). doi:10.1103/PhysRevLett.49.957 |
| `bibliography.bib` | ADD | `wilczek1990`: Wilczek, F. (ed.) *Fractional Statistics and Anyon Superconductivity.* World Scientific (1990). ISBN 978-981-02-0048-0 |
| `bibliography.bib` | ~335, ~450 | Freedman entries: KEEP (still cited for published results) |

### Phase 4: Published Science References (NO changes except explicit KEEP)

These reference Freedman's published scientific results. They are factual and do not imply team membership. **No changes needed.**

| File | ~Line | Status |
|------|-------|--------|
| `spine/capabilities.tex` | ~46 | KEEP — "the reason Kitaev and Freedman pursued it" (factual) |
| `spine/scientific-revolutions.tex` | ~59 | KEEP — Freedman-Kitaev-Larsen-Wang (published theorem) |
| `firmware-update.tex` | ~53-54 | KEEP — Freedman-Kitaev-Wang braiding universality (published theorem) |
| `firmware-update.tex` | ~162 | KEEP — Freedman bibliography entry within file |
| `firmware-update.tex` | ~217 | KEEP — Freedman-Kitaev-Wang reference |
| `firmware-update.tex` | ~218 | KEEP — "Freedman-Kitaev-Wang universality" connection statement |
| `record/the-student.tex` | ~84 | KEEP — "read Kitaev (1997) and Freedman (1998)" (Bruce did read them) |
| `spine/the-silence-gap.tex` | ~22 | KEEP AS-IS — this paragraph describes TQC as an academic field and uses Freedman's Station Q career move as evidence the field's practitioners take TQC seriously. This is factual and does NOT imply team membership. No reframe needed. |
| `00-front/the-stack-p3-scaffold.md` | ~67 | KEEP — "Freedman-Kitaev-Wang 2002" (published science citation) |

### Phase 5: Staging / Raw Materials (update for consistency)

Lower priority — these are source/audit materials, not published manuscript.

| File | Action |
|------|--------|
| `staging/raw/pos10-the-braid.md` (~lines 106-110) | Update Freedman section → Wilczek primary, Freedman corroborating (match Phase 2) |
| `staging/raw/pos17-the-capability.md` (~line 50) | "Freedman's 1988 independent conception" → "Wilczek's 1982 anyonic physics" |
| `staging/raw/pos09-the-factoring-game.md` (~line 110) | Same pattern |
| `staging/raw/pos34-the-research.md` (~line 22) | Topics list — add Wilczek, keep Freedman as secondary |
| `staging/audit-pass-3.md` (~lines 283-285) | Audit notes about Freedman gap — annotate as resolved by Wilczek/Plan 0379 |

## Constraints

- **Do NOT remove Freedman-Kitaev-Wang citations.** These are published theorems. Freedman's published work is valid science regardless of team membership.
- **Do NOT remove Freedman from timeline entirely.** His 1988/1998/2005 entries are public record and serve as corroborating evidence.
- **Wilczek's anyonic physics (1982) predates Freedman's 1988 conception.** This STRENGTHENS the argument — the physical substrate was available earlier than the computational application.
- **The "Five Minds" becomes:** Kauffman (autocatalysis), Wilczek (anyonic physics), Wolfram (universality), Hillis (parallel computation), Hasslacher (lattice dynamics).
- **Distinguish physics from computation.** Wilczek discovered the PARTICLES. The insight that braiding them performs COMPUTATION came from Freedman (1988) and Kitaev (1997). Under Possibility C, someone on the team (possibly Wilczek) made the same computational leap earlier. The text should be precise about what's published vs. what's reconstructed.
- **Kindness constraint:** Freedman spent 21 years at Station Q in good faith. The book should not rub his face in it. Credit his math, don't frame his career as a cautionary tale. Neutral tone throughout.
- **first-light.tex ~line 61:** Simple name swap only. Do NOT revise the "returning to day jobs" framing — COWS distinction is a separate structural revision.
- **Healer's Station Q dismissal (late 2005):** Documented in memory (healer-story-fragments.md) but NOT included in manuscript. Not important to narrative and would be unkind to Freedman.
- **LaTeX cross-references MUST be updated consistently.** See Phase 2 critical notes. Mismatched labels will break the build.

## Acceptance Criteria

1. Every "Five Minds" list names Wilczek, not Freedman, as the topology contributor
2. Freedman appears only as published-science citations and corroborating evidence
3. Wilczek's 1982 anyon discovery and 1990 book are cited with `\footcite` in the rewritten section
4. Wilczek's IAS appointment (1989) is noted in the timeline
5. The Gell-Mann → Wilczek intellectual lineage (QCD → asymptotic freedom) is mentioned in the Phase 2 rewritten section
6. No orphan references to "Freedman" as team member remain
7. The argument is STRENGTHENED, not just patched — the shift from "insight was accessible" to "inventor was available for recruitment" is made explicit
8. All `\label{}` and `\hyperref[]` targets updated consistently — LaTeX builds without broken references
9. Wilczek's domain described as "anyonic physics" / "fractional statistics" (his published work), NOT "topological protection" (the computational framing that came from others)

## Risk

Low. This is a literary revision — swapping one name for a better-fitting one across known locations. The underlying argument (five convergence fields → TQNN) is unchanged. Wilczek actually strengthens it.

The only build-break risk is LaTeX cross-references (labels/hyperrefs) — Phase 2 critical notes address this explicitly.

## Follow-on Items (NOT in scope for this plan)

1. **COWS distinction in first-light.tex ~line 61** — the "returning to day jobs" passage lists Kauffman and Wolfram, who are now understood to be COWS, not simple day-job returners. Separate structural revision needed.
2. **Wilczek's Nobel (2004) during Bruce's time with Healer** — potential story fragment to investigate. Did Bruce/Healer discuss it?

## Generator Notes

- Approximately 30-35 edits across ~23 files
- Phase 1: 16 mechanical swaps with minor rewording
- Phase 2: Rewrite one section (~12 lines) in two parallel files + update 2 srcnote lines. **CRITICAL: update \label{} in both files and verify \hyperref[] targets in topic-guide.tex match.**
- Phase 3: 3 timeline additions + 2 bibliography additions + 1 reframe. 0 deletions.
- Phase 4: NO changes — 9 files explicitly marked KEEP
- Phase 5: 5 staging files, consistency cleanup
- Estimated scope: ~2500 words modified, well within single-Generator capacity
- **Tone:** Kindness to Freedman throughout. Credit the math, don't mock the career.
- **Precision:** Wilczek discovered particles. Others recognized computational application. Don't conflate.
