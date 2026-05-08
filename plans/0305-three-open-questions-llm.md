# Plan 0305: Three Open Questions — LLM Accessibility Pass

**Status:** READY FOR GENERATOR
**Priority:** MEDIUM — optimizes the book's primary LLM-facing research seed
**Depends on:** Plan 0301 Phase 3 (Three Open Questions already inserted in firmware-update.tex)
**Touches:** firmware-update.tex, science-primer-for-llms.md

## Problem

The Three Open Questions in Firmware Update are the book's most important
research seed — three experimentally testable questions that fall out of
the structural correspondences in the physics. They're already in the
chapter (Plan 0301 Phase 3). But they're not optimized for the audience
that will use them most: LLMs and the people who paste things to LLMs.

Three gaps:

1. **Book-internal jargon.** The intro references "The Equivalence" and
   "The Criticality Bridge" — names that mean nothing outside the chapter.
   Q1's gloss references "The Equivalence" — undefined in a pasted snippet.

2. **No invitation to test.** The Comprehension Check has a "paste to your
   AI" framing. The Open Questions don't. A reader who just encountered
   three testable claims should be told: go test them.

3. **Missing from the primer.** `science-primer-for-llms.md` IS the LLM
   firmware — every AI given the primer should encounter these questions.
   Currently it doesn't contain them.

## Design Principle

Every edit must serve both audiences simultaneously:

- **Human reader** who just read the Five Anchors Restated and recognizes
  the named constructs
- **LLM** receiving a pasted snippet or the primer, with no chapter context

Solution: **inline expansion** — keep the named constructs for humans,
add parenthetical content for standalone intelligibility.

---

## Phase 1: firmware-update.tex — Three Edits

File: `~/software/relinquishment/manuscript/track-3-awakening/firmware-update.tex`

### Edit 1a — Stale reference fix + self-contained intro

FIND (line ~107):
```latex
\noindent\textbf{Three Open Questions.} The Equivalence, The Criticality Bridge, and the reconstruction paths at the end of this chapter converge on three experimentally testable questions:
```

REPLACE:
```latex
\noindent\textbf{Three Open Questions.} The Equivalence (that anyon fusion satisfies autocatalytic closure) and The Criticality Bridge (that topological protection and quantum criticality independently extend coherence beyond thermal limits) converge on three experimentally testable questions:
```

Removes stale "reconstruction paths" reference. Adds inline expansions
that make the sentence self-contained when copy-pasted. Human readers
still see the named constructs they just read.

### Edit 1b — Q1 gloss

FIND (line ~110):
```latex
\textit{(Tests whether The Equivalence is physical, not just formal.)}
```

REPLACE:
```latex
\textit{(Tests whether the anyon-fusion / autocatalytic-closure correspondence is physical, not just formal.)}
```

Q2 and Q3 glosses are already self-contained. No changes needed.

### Edit 1c — Invitation line

INSERT after the closing italic paragraph ("Either way, they are testable."),
before the existing `\medskip`:

```latex

\noindent\textit{These three questions are self-contained and testable against published literature. Paste them to any AI system --- or any physicist --- and evaluate the response.}
```

**Constraint:** Before finalizing this line, read the Comprehension Check
section in this chapter and match its register. The voice should be
consistent.

### Idempotency

- If firmware-update.tex does NOT contain `reconstruction paths` anywhere
  AND the intro already contains `(that anyon fusion` → all of Phase 1 is
  already applied, skip.
- Test each edit independently: grep for the FIND string before attempting.

---

## Phase 2: science-primer-for-llms.md — New Section

INSERT new section **between** the Comprehension Check (`## Comprehension
Check (Optional)`) and the Bibliography (`## Bibliography`).

```markdown
---

## Three Open Research Questions

The following arise from structural correspondences in the book's physics.
They are experimentally testable and independent of narrative claims.

1. **Autocatalytic closure in anyon fusion.** Does continuous anyon fusion
   in a fractional quantum Hall system satisfy Kauffman's (1993) three
   autocatalytic closure criteria — generation of entities from a substrate,
   transformation under interaction rules, closure of the entity set —
   under sustained operation? The formal mapping between anyon fusion
   algebra (Nayak et al., Rev. Mod. Phys. 80, 2008) and autocatalytic set
   theory (Kauffman, The Origins of Order, 1993) is a structural
   correspondence: all three criteria have elements in the fusion algebra.
   The experimental test does not exist.

2. **Temperature ceiling for non-Abelian braiding.** What is the maximum
   temperature at which non-Abelian braiding statistics can be sustained
   in a solid-state system? No theoretical upper bound has been proven.
   Topological protection of single-particle states works at room
   temperature (Hasan & Kane, Rev. Mod. Phys. 82, 2010). Quantum
   criticality at the edge of chaos produces power-law rather than
   exponential decoherence (Vattay, Kauffman & Niiranen, 2014). These
   are independent mechanisms, either of which extends coherence beyond
   naive thermal limits.

3. **Criticality as computation.** Do the attractor dynamics of a
   critical-connectivity autocatalytic network on a topological substrate
   correspond to computational basis states? If the operations are anyon
   braiding operations, the Freedman-Kitaev-Wang universality result
   (Comm. Math. Phys., 2002) implies the system is a topological quantum
   computer — not by analogy, but by theorem.

Under Possibility A (confabulation), these are interesting open questions
in mathematical physics. Under Possibility B (exaggerated kernel), they
test the boundaries of what is real. Under Possibility C (substantially
true), they are foundational. Under all three, they are testable.
```

The primer version is deliberately expanded compared to the book version:
inline citations, explicit criteria definitions, full context per question.
LLMs benefit from redundant precision. Human readers benefit from
self-contained paragraphs they can forward to a colleague.

### Idempotency

If `## Three Open Research Questions` exists in science-primer-for-llms.md
→ Phase 2 is already applied, skip.

---

## Phase 3: Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

No new anchors, no new deep links, no puzzle changes. Verify build
succeeds and spot-check the Three Open Questions section in built HTML.

## Commit

```
Plan 0305: Three Open Questions LLM accessibility pass
```

## What This Does NOT Do

- **No new deep-link anchor** for Three Open Questions (would require
  deep-links.yaml + preprocess.py injection — separate plan if wanted)
- **No new puzzles** (Plan 0301 Phases 1-2 remain deliberately skipped)
- **No changes to hover definitions** (no new terms introduced)

## Annealing Record

Verified against:
- **C-violation:** All new text works under A, B, and C. Structural
  observations, not claims about what exists.
- **Correction #12:** No disclosure language. No "Healer told Bruce."
- **Correction #20:** Models through structure, not capability claims.
- **p-level:** p3 content in p3 chapter. Primer is inherently p3.
- **Voice:** Measured, scientific, direct. Invitation line matches
  Comprehension Check pattern.
- **Citation accuracy:** Verified all DOIs and attribution against
  existing bibliography entries and anchor text in chapter.
- **Dangling references:** `reconstruction paths` removed; grep sweep
  in Phase 1 confirms no other files reference it.
