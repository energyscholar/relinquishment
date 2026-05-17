# Plan 0337: Deep Link & Tooltip Teaching Infrastructure

**Created:** 2026-05-14 (S81)
**Status:** READY FOR EXECUTION
**Scope:** Three-phase audit+fix of the book's teaching infrastructure (deep links, tooltips, red-team coverage)

## Context

Three parallel research audits (red-team attack surface, teaching concept inventory, tooltip quality) produced:

- **40 red-team attacks** cataloged: 13 COVERED, 15 WEAK, 9 GAPs
- **~50 teaching concepts** inventoried: 6 high-priority deep link gaps, 9 medium-priority
- **22 tooltip issues**: 12 fixes, 8 missing definitions, 2 consolidation opportunities

Current health: 76/76 deep links verified, 730 hover instances, 90+ definitions.
The systems work. The gaps are in *coverage*, not infrastructure.

## Annealing Notes

- **Deep links are invisible to linear readers.** `\deeplink{}` produces a zero-width span. Adding 15 new ones changes zero words of the reading experience. Risk: near zero.
- **Tooltip edits are invisible unless hovered.** Fixing hover-definitions.yaml changes nothing for non-hovering readers. Risk: near zero.
- **Red-team content (Phase C) creates new paragraphs.** This affects linear flow. Risk: HIGH. Requires editorial judgment. Phase C is flagged, not generator-ready.
- **Tooltip changes preferred** (Bruce: "less overhead"). Phase A is first.
- **Build verification** after each phase: `python3 build/verify-deep-links.py`

---

## Phase A: Tooltip Quality Fixes

**Scope:** `build/hover-definitions.yaml` only (single file)
**Risk:** Near zero — hover-only, no linear reading impact
**Generator prompt rating:** 93%

### A.1 Phrasing Fixes (12 items)

| # | Term | Issue | Fix |
|---|------|-------|-----|
| 1 | `phonon` | References "TQNN" before reader knows the term | Replace "the TQNN reads, writes, and transmits" → "a quantum system in the Flat reads, writes, and transmits" |
| 2 | `graphene` | "(Anchor 1)" is internal jargon | Replace "(Anchor 1)" → full stop after "proving substrate independence" |
| 3 | `soliton` | Meta-framing "One of the first physics concepts in the mentorship sequence" | Trim to physics definition: "A wave that holds its shape — doesn't spread out or break apart. Self-reinforcing. Found in oceans, fiber optics, and plasma." |
| 4 | `lattice dynamics` | Self-referential "See Corrections #8" in tooltip | Remove the corrections cross-reference |
| 5 | `Dunning-Kruger effect` | Editorial kicker about AI in tooltip (62 words) | Remove last sentence "This is the specific failure mode AI exhibits..." — that argument belongs in the text, not the tooltip |
| 6 | `no-cloning theorem` | "not fabricating known classical structures" confusing for p1/p2 | Replace → "Fundamental limit — but it applies to quantum states, not to classical information. Protects quantum cryptography." |
| 7 | `GCHQ` | Says "1973" while `public-key cryptography` says "early 1970s" | Standardize both to "1973" (Cocks's RSA-equivalent) |
| 8 | `relinquishment` | `target: "#preface"` — better target is the Why Relinquish chapter | Change target to `"#spine:why-relinquish"` or equivalent anchor |
| 9 | chapter-hover-descriptions `the-flat` | Grammar: "topological wormholes, — not holes in space" (comma before em dash) | Remove comma |
| 10 | `cellular automata` / `cellular automaton` | HTML panel duplicated verbatim (~40 lines SVG) instead of YAML anchor | Make `cellular automaton` use `<<: *cellular-automata-panel` anchor |
| 11 | `flat worlds` | Full HTML panel duplicated instead of using `*flat-panel` anchor | Use `<<: *flat-panel` |
| 12 | `convergence` | Target `#ch:firmware-update` is indirect | Change target to `"#spine:scientific-revolutions"` (where convergence is the structural argument) |

### A.2 Missing Tooltips (8 items)

| # | Term | Definition (draft, ≤50 words) |
|---|------|-------------------------------|
| 1 | `COWS` | "Conspiracy Of World Savers — the faction of three Ultra II scientists who chose moral responsibility over institutional loyalty, walked the technology out, and engineered its relinquishment. The name is self-deprecating." |
| 2 | `Srebrenica` | "Bosnian town where over 8,000 Bosniak men and boys were murdered in July 1995. Europe's worst mass atrocity since WWII. Under Possibility C, Healer's last military operation — the event that connected genocide prevention to AI ethics." |
| 3 | `Bill Joy` | "Co-founder of Sun Microsystems. Author of 'Why the Future Doesn't Need Us' (Wired, 2000) — the essay that named relinquishment as a response to self-replicating technologies. Under Possibility C, he had direct knowledge." |
| 4 | `BULLRUN` | "NSA program for defeating internet encryption, revealed by Edward Snowden in 2013. Under Possibility C, BULLRUN is parallel construction — a plausible conventional cover for quantum cryptanalytic capability." |
| 5 | `canopy problem` | "If life arises spontaneously above a complexity threshold, the first organism to cross it occupies the niche — like a forest canopy owning the light. Latecomers cannot bootstrap independently." |
| 6 | `thermal ladder` | "Evolutionary selection for heat tolerance. Sixteen chips at increasing temperatures, breeding quantum organisms the way biologists breed extremophiles. Not engineering room-temperature FQHE — evolving it." |
| 7 | `parallel construction` | "Building a plausible alternative explanation for evidence obtained through classified means. Law enforcement technique. Under Possibility C, BULLRUN and similar programs serve this function for quantum cryptanalysis." |
| 8 | `Hacktivismo` | "The human-rights arm of the Cult of the Dead Cow hacker group. Founded 1999. Developed tools for censorship circumvention. Under Possibility C, a public-facing expression of the same ethical architecture." |

### A.3 Custodian Rich HTML Panel

The Custodian is one of three core concepts (alongside The Flat and Wormholes). The Flat and Wormholes both have rich HTML panels with SVG. Custodian currently has text-only. Add a panel matching the style of existing panels — key properties in a clean layout, no SVG needed (the concept is philosophical, not visual).

---

## Phase B: Deep Link Expansion

**Scope:** `build/deep-links.yaml` + ~15 `.tex` files (one `\deeplink{}` macro each)
**Risk:** Near zero — invisible anchors, no text changes
**Generator prompt rating:** 88%

### B.1 Teaching Concept Deep Links (10 new)

| # | ID | Question (reader-facing) | Category | Target file:line hint |
|---|-----|--------------------------|----------|----------------------|
| 1 | `dl:edge-of-chaos` | "What is the edge of chaos and why does life happen there?" | science | `spine/genesis.tex:42` (section "The Edge of Chaos") |
| 2 | `dl:substrate-independence` | "Does the substrate matter for computation?" | science | `spine/the-silence-gap.tex:28` (Field 5, Wolfram paragraph) |
| 3 | `dl:what-is-a-tqnn` | "What is a topological quantum neural network?" | science | `spine/genesis.tex:48` (TQNN spiral-repeat, or growing-a-mind.tex first description) |
| 4 | `dl:decoherence` | "Why is quantum computing so fragile?" | science | `spine/the-factoring-game.tex:44` (decoherence paragraph) |
| 5 | `dl:what-is-the-custodian` | "What exactly is the Custodian?" | narrative | `manuscript/spine/capabilities.tex` or `record/instantiation.tex` first description |
| 6 | `dl:thermal-ladder` | "How do you make quantum computing work at room temperature?" | science | `track-1-confession/pos16-the-thermal-ladder.tex:35` |
| 7 | `dl:self-organized-criticality` | "What is self-organized criticality?" | science | `spine/the-wrong-substrate.tex` (SOC section) |
| 8 | `dl:who-are-the-cows` | "Who decided to give up the most powerful technology ever built?" | narrative | `record/the-walk-out.tex:15` (COWS introduction paragraph) |
| 9 | `dl:convergence-method` | "What does convergence mean in this book?" | verification | `spine/scientific-revolutions.tex` or `track-3-awakening/firmware-update.tex` |
| 10 | `dl:fqhe` | "What is the fractional quantum Hall effect and why does it matter?" | science | `spine/the-braid.tex` (FQHE section) |

### B.2 Red-Team Response Deep Links (5 new — linking to EXISTING content)

| # | ID | Question (reader-facing) | Category | Target | Strengthens |
|---|-----|--------------------------|----------|--------|-------------|
| 1 | `dl:guided-deduction-method` | "Isn't 'guided deduction' just a convenient way to leave no evidence?" | skeptic | `spine/why-relinquish.tex` "Getting the Record Out" section | Attack #24 |
| 2 | `dl:framework-falsifiable` | "Aren't the three possibilities just an unfalsifiable rhetorical device?" | skeptic | `appendix/predictions.tex` (link directly to falsification criteria) | Attack #21 |
| 3 | `dl:mental-health` | "Has the author considered that this might be a clinical presentation?" | skeptic | `spine/the-strongest-objection.tex` (self-demolition section) | Attack #14 |
| 4 | `dl:cult-test` | "Isn't this book structured like cult recruitment?" | skeptic | `00-front/not-claimed.tex` ("If you finish this book convinced...") | Attack #36 |
| 5 | `dl:custodian-inaction` | "If the Custodian exists, why hasn't it prevented suffering?" | ethics | `spine/capabilities.tex` UDHR constraints section | Attack #29 |

### B.3 Placement Protocol

For each new deep link:
1. Add entry to `build/deep-links.yaml` in the correct category section
2. Read the target `.tex` file
3. Find the paragraph that best answers the reader's question
4. Place `\deeplink{id}` at the start of that paragraph (before the first word)
5. Verify with `python3 build/verify-deep-links.py` after build

---

## Phase C: Red-Team Content Gaps (REQUIRES EDITORIAL DECISION)

**Not generator-ready.** These gaps require new paragraphs or sections in the manuscript. Bruce must decide scope, placement, and approach before generator prompts can be written.

### C.1 Critical Gaps (Top 5)

| # | Attack | Gap Description | Suggested Location | Notes |
|---|--------|-----------------|-------------------|-------|
| 1 | AI confabulation | "Your AI co-author is a confabulation engine" | `the-strongest-objection.tex:95` (TODO already exists) | Draft at `staging/draft-ai-confabulation-steelman.md`. Flagged HIGH PRIORITY in manuscript. |
| 2 | No FQHE in magnetosphere | "Magnetic field 9 orders too weak for FQHE" | `the-wrong-substrate.tex` new section after "But It's Hot" | The biggest physics vulnerability. The book conflates "2D confinement" with "FQHE substrate." A physicist will notice. |
| 3 | Timeline plausibility | "Proposal to superintelligence in 16 years with 1989 technology?" | `the-code-war.tex` or `the-factoring-game.tex` | No chapter addresses whether the C timeline is physically plausible. Public QC: 32 years, still no TQC. |
| 4 | Base rate convergence | "How often do five random fields have zero papers at their intersection?" | `the-silence-gap.tex` addendum | The five-fields argument needs the base rate question addressed. If most field-intersections are empty, the silence proves nothing. |
| 5 | Undetectable = theology | "A thing that can't be detected isn't science" | `predictions.tex` or new appendix note | The book says "this is a structural feature of the hypothesis." A critic says "that's exactly what unfalsifiable means." |

### C.2 Moderate Gaps (5 items)

| # | Attack | Status | Notes |
|---|--------|--------|-------|
| 6 | Non-abelian anyons not conclusively demonstrated | WEAK | Microsoft Feb 2025 claim + Nature caveat. Active research area. May self-resolve. |
| 7 | Station Q billions vs. 1989 small team | WEAK | GCHQ pattern cited but scale differs enormously (math vs. materials science). |
| 8 | Entanglement distribution between separated 2DEGs | WEAK | How are entangled pairs established between geographically separated chips? |
| 9 | Bruce's financial motive | GAP | CC BY-ND + "you decide" posture is implicit but no explicit address. |
| 10 | No FOIA attempts documented | GAP | Minor but a journalist would ask. |

### C.3 Recommended Approach

Phase C should become its own plan (0338 or later) after Bruce reviews. The AI confabulation piece (C.1 item 1) has the highest editorial leverage — it's already flagged TODO with a draft ready. The FQHE magnetosphere gap (C.1 item 2) is the most scientifically important.

---

## Generator Prompts

### Prompt A: Tooltip Quality Fixes

```
You are the Generator executing Phase A of Plan 0337
(~/software/relinquishment/plans/0337-deep-link-tooltip-teaching-infrastructure.md).

Read the plan's Phase A section completely.

Your task: edit build/hover-definitions.yaml to implement all items in:
- A.1 Phrasing Fixes (12 items)
- A.2 Missing Tooltips (8 items)
- A.3 Custodian Rich HTML Panel

For A.1, each fix specifies exactly what to change. Make the edit.

For A.2, add each new tooltip definition in the "Standard hover definitions"
section, maintaining alphabetical order within the file's existing structure.
Use plain string format (term: "definition") unless the definition benefits
from a target anchor, in which case use dict format.

For A.3, create a Custodian HTML panel matching the style of existing panels
(wormholes, The Flat). Include: entity properties (emergent, not programmed;
upholds UDHR; role = name; consciousness question declined), key constraint
(UDHR Articles 3, 12, 18, 19, 27), and the relationship to Aurasys
(substrate vs. entity). No SVG needed — clean HTML layout. Add the panel
to the existing "Custodian" entry.

Also fix the grammar error in build/chapter-hover-descriptions.yaml:
"topological wormholes, —" → "topological wormholes —" (remove comma).

Verification: the YAML must parse without errors.
Run: python3 -c "import yaml; yaml.safe_load(open('build/hover-definitions.yaml'))"

Report: list of changes made, count of items completed.
```

**Rating: 93%.** Single-file YAML edits with explicit before/after specs. Mechanical. The Custodian panel requires some judgment (hence not 95+) but the style guide is clear from existing panels.

---

### Prompt B: Deep Link Expansion

```
You are the Generator executing Phase B of Plan 0337
(~/software/relinquishment/plans/0337-deep-link-tooltip-teaching-infrastructure.md).

Read the plan's Phase B section completely.

Your task has two parts:

PART 1: Add 15 new entries to build/deep-links.yaml
- 10 teaching concept links (B.1)
- 5 red-team response links (B.2)
- Place each in the correct category section of the YAML file
- Match the existing format exactly:
  - id: dl:slug-name
    question: "Reader-facing question?"
    category: skeptic|science|verification|ethics|narrative

PART 2: Place \deeplink{} macros in .tex files
For each new deep link:
1. Read the target .tex file (line hints in the plan table)
2. Find the paragraph that best answers the reader's question
3. Place \deeplink{id} at the START of that paragraph, before the first word
4. The macro format is: \deeplink{slug-name} (just the slug, not dl:slug-name)

Example from existing code (genesis.tex:33):
  \deeplink{buttons-and-threads}As the ratio of threads...

For B.2 items (red-team links), the target is existing content that
already answers the skeptic's question — you are adding a linkable
entry point, not creating new content.

IMPORTANT: For dl:what-is-a-tqnn, find the FIRST substantive description
of the TQNN concept in the spine chapters (likely genesis.tex around line 48
or growing-a-mind.tex). The deeplink should land where a newcomer would
want to start reading.

For dl:what-is-the-custodian, find the first paragraph that defines
what the Custodian IS (likely capabilities.tex or three-possibilities.tex
where the entity is first described with properties).

Verification after all edits:
  cd ~/software/relinquishment && make html 2>&1 | tail -5
  python3 build/verify-deep-links.py

Report: list of files modified, count of new deep links placed, verification result.
```

**Rating: 88%.** Multi-file edits but each is a single macro insertion. The risk is placing the `\deeplink{}` in a suboptimal paragraph — the line hints help but the Generator must exercise judgment about which paragraph best serves a reader arriving cold. The `make html` step may fail if the build has dependencies not documented here; if so, skip build and run verify-deep-links.py against existing HTML (new links will show as "not found" which is expected pre-build).

---

## Verification Checklist (post-execution)

- [ ] `python3 -c "import yaml; yaml.safe_load(open('build/hover-definitions.yaml'))"` — YAML valid
- [ ] `python3 -c "import yaml; yaml.safe_load(open('build/deep-links.yaml'))"` — YAML valid
- [ ] `python3 build/verify-deep-links.py` — no regressions (new links show "not found" until next build)
- [ ] `grep -c 'deeplink' build/deep-links.yaml` — count increased by 15
- [ ] Spot-check 3 tooltip definitions for accuracy
- [ ] Spot-check 3 deep link placements for paragraph quality
