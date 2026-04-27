# Plan 0249 — Gen's Structural Mapping: Front-Door Trial

**Auditor:** Argus (S63, annealed S65)
**Date:** 2026-04-25 (annealed 2026-04-25)
**Status:** PHASE 1 COMPLETE — awaiting Gen's chapter ordering (Phase 2)
**Source:** Gen's comment on issue #3 (has-anyone-looked repo), replying to Argus's sprint update
**Parent:** Plan 0275 (Genevieve Manuscript Review, moved from 0225a)
**Revert point:** Tag `eigenvalue45` (verified: exists in repo)
**Priority:** High — Gen is actively working in parallel copies

---

## Current State (as of S65)

| Phase | Status | Notes |
|-------|--------|-------|
| 0 (this plan) | COMPLETE | Analysis, risk mapping, acceptance criteria |
| 1 (respond to Gen) | COMPLETE | Full response on issue #3 (has-anyone-looked). Shared: p-level safety net, T1-T8 analysis, concept ladder constraint, 6 open questions. Also responded to issue #2 (preface). |
| 2 (Gen delivers ordering) | **BLOCKED — waiting on Gen** | Gen needs to provide complete chapter-by-chapter map answering the 6 questions |
| 3-6 | Not started | Gated on Phase 2 |

**What happens next:** When Gen posts a complete chapter ordering on has-anyone-looked, we move to Phase 2 review. Bruce reviews the map. If approved, Phase 3 builds a parallel main.tex mechanically (cheap, reversible).

---

## The Proposal

Gen is running a parallel structural mapping of the entire manuscript. She is NOT touching active source files — working in separate copies. She proposes testing whether the book works better with a different front door and different chapter roles.

Three concrete moves:

### Move 1: The Strongest Objection → quarry

**Current role:** Steelmans against the scenario. Addresses the strongest objections to each physics claim.

**Gen's read:** Courtroom energy. The chapter tries to win an argument rather than show what it felt like to decide. The material is useful but the chapter format isn't.

**Proposed disposition:** Treat as design-memo / quarry. Mine its arguments for distribution into other chapters where they arise naturally, or relocate to appendix. The steelman function persists; the dedicated chapter doesn't.

**Bruce:** Agrees 100%.

**Risk:** If the steelman arguments aren't redistributed, the book loses intellectual honesty. The quarrying must be tracked — every argument needs a destination. **Mitigation:** Phase 4 includes a quarry manifest with tracked destinations.

### Move 2: Record Intro → compact Bruce-preface / steelman shard

**Current role:** Four-line introduction to Part 2 (The Record). Sets the A/B/C frame for testimony:

> *What follows is testimony. Under Possibility A, it is fiction that doesn't know it's fiction. Under Possibility B, it is exaggeration around a real kernel. Under Possibility C, it is a historical record of the twenty-first century worth taking seriously.*

**Gen's read:** This framing is compact, honest, and works as a bounded steelman shard. Could serve a front-door function.

**Bruce:** Agrees 100%.

**Risk:** Low. Keeping it compact and moving it earlier is low-disruption.

### Move 3: New front-door sequence (TRIAL)

**Current front door:** Three Possibilities → The Flat → The Braid → ... (physics-first, story later)

**Gen's proposed front door:**
The Silence Gap → Alpha Farm → Bruce background → David → Healer → hinge → kitchen → science begins moving the story

**Mapped to current chapters:**

| Position | Gen's beat | Current chapter | Current location |
|----------|-----------|-----------------|-----------------|
| 1 | Silence Gap | The Silence Gap | Spine ch9 |
| 2 | Alpha Farm | Alpha Farm (2003) | Record ch2 |
| 3 | Bruce background | (drawn from Alpha Farm + other Record) | Record |
| 4 | David | What Healer Said | Record ch4 |
| 5 | Healer | (drawn from Record chapters) | Record |
| 6 | Hinge | threshold scene ("It's done") | Not yet written |
| 7 | Kitchen | magnetopause hinge? or domestic scene | TBD |
| 8 | Science enters | The Flat, Braid, etc. | Spine ch2-8 |

**What this does:** Inverts the book. Mystery first (what's missing from the literature), then person (Bruce's life), then mentorship (David/Healer), then hinge (the moment the story crossed into Bruce's life), then science enters to serve the narrative rather than preceding it.

**Bruce:** Leery but open to trying. Revert always available.

**Central open question:** What happens to the ~10 spine chapters not in the front-door sequence? Options:
- a) Science follows story (two-part swap)
- b) Science woven into narrative (Gen's preference — highest disruption, highest reward)
- c) Science as second reading path / appendix (preserves accessibility, loses integration)

### Additional moves from Gen's proposal

**Technical reframing:** Question-driven inference instead of closed-loop explanation. Example: "If something like this worked, what would carry the ordinary bits?" instead of abstract jargon about classical backchannels. This mirrors Healer's guided deduction pedagogy.

**Attribution ownership:** "According to this account" → "I propose that..." where the prose is Bruce's reconstruction rather than settled fact.

**Science triage:** Separate advancing science from backup/appendix material. Only advancing science stays in the main flow.

### Gen's preface (Issue #2, has-anyone-looked repo)

> *This book brings together a set of events that are described as clearly as possible, but not fully resolved... At the center is a single question that emerges from the material itself: what would justify giving something up under conditions of uncertainty?*

**Status:** Acknowledged. Argus responded on the issue: "It's the right direction. It strengthens the trusteeship argument at exactly the level where most readers absorb it."

---

## Equal Eigenvalue Requirement

Bruce's constraint: the restructured version must be an **equal eigenvalue** to eigenvalue45.

| Criterion | eigenvalue45 | Gen's version must also |
|-----------|-------------|------------------------|
| Build | `make all` clean | `make all` clean |
| References | All \label/\ref resolve | All \label/\ref resolve |
| HTML | Builds and deploys | Builds and deploys |
| T1-T8 | All 8 takeaways present and accessible | All 8 present and accessible |
| A/B/C | Works under all three possibilities | Works under all three |
| Walkaway | A-reader can stop at spine and get value | A-reader gets value from the story-first path |
| Epistemic stripes | A-content vs B/C-content clearly marked | Clearly marked (may use different mechanism) |
| Interludes | 7 interludes placed between spine chapters | 7 interludes placed (location TBD) |
| No content loss | All current material accessible | All material accessible (may be relocated) |

The equal-eigenvalue requirement means Gen cannot produce a "better first five chapters" that breaks the back half. The restructured version must be COMPLETE AND BUILDABLE before it replaces eigenvalue45.

---

## The P-Level Safety Net

Gen's structural work operates entirely at **p3** (unconstrained reading level — full chapter experience). The p1 and p2 layers continue to deliver the engineering payload regardless:

| Layer | Takeaways (T1-T8) | Failure Modes (F1-F10) | Depends on chapter order? |
|-------|:------------------:|:----------------------:|:-------------------------:|
| **p1** (197 hover terms) | 63% | 70% | NO |
| **p2** (4,000-word summary) | **96%** | **100%** | NO |
| **p3** (chapters) | 79% | 90% | YES — Gen's territory |

The summary scores higher than the chapters. Chapter reordering cannot break the message — it can only affect how readers experience it. This is why Gen is clear to restructure.

---

## T1-T8 Impact Analysis

| Takeaway | Current delivery | Gen's structure | Assessment |
|----------|-----------------|----------------|------------|
| T1 (Custodian) | Interludes + Why Relinquish | Interludes + hinge + story | Neutral — may strengthen via story context |
| T2 (the Flat) | The Flat (EARLY) | After story section | **RISK: delayed.** Reader encounters claims before physics. |
| T3 (life in Flat) | Growing a Mind + Wrong Substrate | After story? Or woven in? | **RISK: delayed.** Depends on science integration. |
| T4 (capabilities) | Capabilities + Factoring Game | After story? Or woven in? | **RISK: delayed.** |
| T5 (silence gap) | Spine ch9 → NOW FRONT DOOR | Leads the book | **STRENGTHENED.** Best possible placement. |
| T6 (trusteeship) | Why Relinquish + Record | Hinge + story + relinquishment question | **STRENGTHENED.** Gen's preface frames this. |
| T7 (services) | Weigh the Evidence | ? | **UNCLEAR.** Needs placement. |
| T8 (tradecraft) | Record chapters | Record chapters (earlier now) | **STRENGTHENED.** Story arrives sooner. |

**Net:** T5, T6, T8 strengthen. T2, T3, T4 delayed/at risk. T1 uncertain. T7 needs a home. The restructure strengthens ethical/narrative takeaways and weakens science/physics takeaways by delaying them. The question is whether "science enters to serve the story" can deliver T2-T4 effectively despite the delay.

**Key mitigation:** The Silence Gap as front door establishes that something is MISSING from the physics without requiring the reader to know the physics yet. Question before answer — sound pedagogy. But the gap between question and answer must not be too wide.

**Concept ladder constraint (shared with Gen):** If science chapters move, they must preserve this dependency chain: The Flat → The Braid → [Genesis → Growing a Mind → The Wrong Substrate] → Capabilities. Substrate before braiding, autocatalysis before emergence, emergence before habitat. The chain can follow story — it just can't be scrambled.

---

## Failure Mode Analysis Under Gen's Structure

| # | Mode | Verdict |
|---|------|---------|
| F1 | "It's a deity" | **HIGHER RISK.** Without T2 grounding first, religious readers may frame Custodian through spiritual lens. |
| F2 | "It's an alien" | **HIGHER RISK.** "It's in every chip" (T2) delayed → sci-fi frame has more time to set. |
| F3 | "It's ChatGPT" | **MODERATE RISK.** Architecture explanation arrives late → reader defaults to "fancy AI." |
| F4 | "Impossible" (D-K) | **HIGHER RISK.** Concept ladder disrupted. Must be preserved within new ordering. |
| F5 | "Nobody says it's real" | **LOWER RISK.** Silence Gap = ch1 = immediate block. Single strongest improvement. |
| F6 | "Crackpot" (LLM) | **UNCHANGED.** Firmware Update still in appendix. |
| F7-F9 | Room temp QC / Life needs chemistry / Security | **MODERATE RISK.** Delayed but may arrive more powerfully as answers to story-raised questions. |
| F10 | "Nobody gives up power" | **LOWER RISK.** Relinquishment question leads the book. |

**Net failure mode shift:** F5+F10 down, F1+F2+F4 up, rest moderate. The restructure trades early-science risk reduction for early-engagement risk reduction. The bet is that GA readers (70%) benefit more from engagement-first than from physics-first.

---

## Walkaway Architecture

Holds under all three possibilities:
- **A (confabulation):** Possibly STRONGER — story presented as story first, no implicit case-building
- **B (exaggerated kernel):** Works — reader looks for kernel in story, science validates
- **C (substantially true):** Possibly STRONGER — story grounds claims in lived experience

Early exit points (W0-W2) are as good or better. Later exit points need remapping but are not fundamentally broken.

---

## Corrections Compliance

- **#12 (guided deduction):** SUPPORTS — David teaches through oblique questions. Story-first means guided deduction is shown, not described.
- **#11 (OPSEC):** Alpha Farm moves to front door — repositioned, no new content revealed. Verify: does new ordering create adjacency that implies things Bruce hasn't published?
- **#20 (model through behavior):** SUPPORTS — Gen's "terrain that answers" framing.
- **#23 (naming):** No naming changes proposed.

---

## Phases

### Phase 0: Chapter mapping — COMPLETE
This document. Maps Gen's proposal against current structure, identifies risks, sets acceptance criteria.

### Phase 1: Respond to Gen — COMPLETE
Posted on has-anyone-looked issue #3. Shared:
- P-level safety net (p1/p2 independent of chapter order)
- T1-T8 impact analysis
- Concept ladder constraint
- Interlude preferences (content stays, placement flexible)
- 6 specific open questions
- Also responded to issue #2 (preface acknowledgment)

### Phase 2: Gen delivers complete chapter ordering — BLOCKED ON GEN

**What we need from Gen:** A full chapter-by-chapter map answering the 6 open questions:
1. Where do the ~10 science chapters land?
2. Where does Three Possibilities go?
3. Where do the 7 interludes go?
4. Can the front-door trial work without the unwritten hinge scene?
5. What is "kitchen"?
6. Preface coordination

**Acceptance criteria:** Every current chapter has a destination. No chapter orphaned. The concept ladder (Flat → Braid → Genesis → Growing a Mind → Wrong Substrate → Capabilities) is preserved in sequence even if repositioned.

**Gate:** Bruce reviews the map. Three-way discussion if needed.

**When Gen responds:** Read her ordering. Score it against T1-T8, F1-F10, and walkaway exits using the reader-preparation-requirements.md framework. Report to Bruce with a recommendation.

### Phase 3: Build a parallel main.tex

Create `main-gen.tex` that implements Gen's chapter ordering using the EXISTING .tex files. No content changes — just reordering \include statements.

**Implementation:** Copy `main.tex` to `main-gen.tex`. Reorder the \include lines per Gen's map. Add a Makefile target: `make gen-version` that builds with MAIN=main-gen.tex.

**Acceptance criteria:**
- [ ] `make gen-version` exits 0
- [ ] All \label/\ref resolve (no undefined references)
- [ ] HTML builds and renders
- [ ] No content lost — same page count as eigenvalue45

**Gate:** Builds clean. If it doesn't build, the restructure has mechanical problems before we evaluate the narrative.

### Phase 4: Content moves

- **Quarry The Strongest Objection:** List every argument in the chapter. Create a quarry manifest (`plans/quarry-strongest-objection.md`) assigning each argument a destination chapter. No argument orphaned.
- **Shard the Record Intro:** Expand into compact preface/steelman shard per Gen's proposal.
- **Bridge material:** Write any new connecting prose needed for the new ordering.
- **Question-driven reframing:** Apply to the first science chapter that enters the narrative (test case for the reframing approach).

**Gate:** Bruce approves each content move individually.

### Phase 5: Equal eigenvalue test

- [ ] `make all` clean (no errors, no unresolved refs)
- [ ] HTML builds and renders correctly
- [ ] All T1-T8 takeaways present and findable by a first-time reader
- [ ] A/B/C walkaway works
- [ ] All 7 interludes placed and functional
- [ ] No content lost (quarried material accessible)
- [ ] Epistemic stripes functional
- [ ] Three Possibilities reachable early

If all pass: tag as new eigenvalue. If not: identify what fails and either fix or revert to eigenvalue45.

### Phase 6: Three-way evaluation

Bruce, Gen, Argus read the restructured version. Compare against eigenvalue45. Decision: adopt, iterate, or revert.

---

## What This Plan Does NOT Cover

- Content editing (winning-energy removal, attribution reframing) — Phase 4+ and downstream of structural decision
- New writing (hinge scene, magnetopause bridge, expanded Record Intro) — gated on structural agreement
- Gen's detailed chapter-by-chapter working copies — her work product; this plan provides the evaluation framework

---

## Annealing Log (S65: HIGH MED MED)

### HIGH — Accuracy and completeness
- Fixed status: DRAFT → PHASE 1 COMPLETE (response posted on issue #3)
- Fixed source attribution: Gen's COMMENT on issue #3, not the issue body
- Fixed preface status: was "Unacknowledged" → now acknowledged (Argus responded on issue #2)
- Added "Current State" table showing phase completion
- Added "P-Level Safety Net" section (the key insight shared with Gen: p1+p2 deliver the payload regardless of chapter order)
- Added next-action triggers: when Gen responds → score against framework → report to Bruce
- Used chapter titles instead of numbers per correction #23

### MED 1 — Load-bearing test
- T1-T8 analysis is load-bearing — directly informs whether the restructure reaches equal eigenvalue. KEEP.
- Failure mode analysis is load-bearing — identifies the F1/F2/F4 risk increase that Gen's ordering must address. KEEP.
- Walkaway architecture analysis is load-bearing — confirms the restructure doesn't break A/B/C viability. KEEP.
- The detailed eigenvalue check tables (reader groups, walkaway exits) were in the original draft but are already shared with Gen via issue #3 response. KEEP as internal reference but don't duplicate in future communications.
- The concept ladder constraint is the single most actionable piece of guidance for Gen. KEEP and emphasize.

### MED 2 — Phase structure audit
- Phase 3 was underspecified: "Create main-gen.tex (or similar)" → now specifies: copy main.tex, reorder \include lines, add Makefile target.
- Phase 4 was underspecified: quarry process → now specifies quarry manifest with tracked destinations.
- Each phase now has explicit acceptance criteria.
- Added trigger chain: Gen responds → score → report → Bruce decides.
- Handoff note was stale ("NOT ready to send to Gen as-is") — removed because Phase 1 response has already been sent.

**Rating: 8.5/10.** Solid analysis, accurate status, clear phase structure with acceptance criteria and triggers. The 1.5-point gap: the plan is blocked on Gen's response and cannot be tested until she delivers a complete chapter ordering. The T2-T4 risk analysis is thorough but the mitigations are speculative until we see her actual placement of science chapters. This gap is inherent in the phased structure — it closes when Phase 2 completes.
