# Plan 0233 — Easter Eggs + Puzzle Engine

**Status:** ANNEALED (S64). Ready for phased execution. Some phases need Bruce/Gen decisions before Generator handoff.
**Author:** Auditor (Argus S64)
**Date:** 2026-04-24 (replaces S59/S63 draft)
**Absorbs:** Plan 0230 Change 2 (ULTRA II reduction) — destination architecture lives here, editorial decisions live here
**Related:** Plan 0230 (continental drift, unbuilt bridge), Plan 0232 (LLM verification prompts), existing copy-button infrastructure

---

## What This Plan Does

Two complementary systems that share a philosophy — the book rewards engaged readers:

1. **Easter eggs** — unlisted HTML pages containing ULTRA II reconstruction content, discoverable via URL puzzles. Attack-surface reduction: main text keeps the coined term + existence claim (~10%), reconstruction detail moves to hidden pages (~90%).

2. **Puzzle engine** — chapter-end puzzles on 13 A-spine chapters that gate Spiral Abstract reveals. Reader earns the spanning path by demonstrating understanding. Soft gate: Spiral Abstracts remain in the appendix for anyone who wants them without the puzzle.

These are technically independent systems. Easter eggs are standalone HTML pages at hidden URLs. Puzzles are interactive elements in the main HTML using localStorage. They ship in separate phases.

---

## Part 1: Easter Eggs (ULTRA II)

### The Problem

52 ULTRA II references across 20 manuscript files. This content is 100% Bruce's reconstruction — highest-risk under Possibilities A and B, easiest target for hostile reviewers. The main text currently stakes more on the reconstruction than the A/B/C framework requires.

### The Solution: 10/90 Split

**Main text keeps (~10%):**
- The coined term "ULTRA II" — essential for disambiguation from COWS
- That ULTRA II was a subset of scientists within COWS
- Enough relationship context for disambiguation
- The *why* (motivation, purpose, stakes)
- A hint — the puzzle that leads to the egg

**Easter egg gets (~90%):**
- Structural reconstruction: who they were, relationship to COWS, approximate timeline, purpose, outcome
- Detailed timeline (currently in timeline.tex: 292 lines, 13 references)
- Fictional classified abstracts (currently in abstracts.tex: 302 lines, 6 references)
- Interdiction reconstruction (pos26-interdiction.tex + record/interdiction.tex)

**Cut entirely (not moved — deleted):**
- Lab procedures, specific technical sequences of how things were done
- Procedural detail Bruce can't be confident of
- Any content that requires having been physically present to know

### URL Architecture

```
relinquishment.ai/eggs/[slug]
```

Pages are real, renderable HTML. Same CSS, fonts, epistemic color system, hover definitions as main book. Not linked from navigation, TOC, or any visible UI. Not password-protected. Not `noindex`'d. The puzzle is finding the URL, not bypassing security.

**Once someone shares the URL, everyone has it.** This is by design. The egg content is less-confident reconstruction, not secret material. The puzzle rewards curiosity; it's not a security gate.

### Easter Egg Manifest (CRITICAL)

All eggs tracked in `build/easter-egg-manifest.yaml`:
- Slug / URL path
- Content source file(s)
- Puzzle type and tier
- Hint location (file + line) in main text
- Answer/solution
- Status (planned / built / live)

Manifest referenced from landmark file. Updated every time an egg changes. Add manifest verification to `make check` — orphan eggs are lost eggs.

### Easter Egg Structure: Single Egg (Option A)

**Decision: Single egg, not chronological.** Rationale:
- One puzzle = one reward = one clear path for the reader
- Chronological eggs (Option B from prior draft) require 3-4 puzzles of escalating difficulty — too much design overhead for content the book is deliberately de-emphasizing
- If the reader finds the egg, they get the complete picture; if they don't, nothing is missing from the A/B/C argument
- A single egg is simpler to build, maintain, and verify

### Puzzle for URL Discovery: Tier 1 (Stated Path)

The hint lives in or near the passage that introduces the ULTRA II term. A phrase that IS the URL path but doesn't look like one to a casual reader.

**Bruce decides the specific phrasing.** Suggestion: something like "the record continues at ultra-two" embedded naturally in prose. Reader who understands URL structure tries `/eggs/ultra-two`.

Tier 1 is appropriate because:
- Low barrier = more readers find it
- The content is already flagged as lower-confidence reconstruction — no reason to gate it hard
- Harder tiers can be added for future eggs

### ULTRA II Content Audit (verified 2026-04-24)

| File | Hits | Action | Phase |
|------|------|--------|-------|
| appendix/timeline.tex | 13 | Most moves to egg. Main text keeps: existence + endpoint dates | 2b |
| appendix/abstracts.tex | 6 | Strong egg candidate — fictional classified papers reward invested readers | 2b |
| track-1/pos21-convergence-revisited.tex | 4 | Review: convergence argument, not reconstruction. Likely STAYS | 2c |
| track-1/pos20-the-network.tex | 3 | Review: capabilities chapter. May reduce but not move | 2c |
| spine/the-factoring-game.tex | 3 | STAYS — "ULTRA II Specifications" = the 10% spine (problem statement, not solution) | — |
| bridge/pos09-the-factoring-game.tex | 3 | STAYS — same as above, bridge version | — |
| bridge/pos11-the-demo.tex | 3 | Review | 2c |
| record/first-light.tex | 3 | Review — Record mirrors Track-1 | 2c |
| track-3/pos30-unipolar-condition.tex | 2 | Review | 2c |
| track-2/pos34-the-research.tex | 2 | Review — probability estimates | 2c |
| track-1/pos26-interdiction.tex | 1 | Heavy reconstruction → egg | 2b |
| record/interdiction.tex | 1 | Mirrors pos26 → egg | 2b |
| track-1/pos17-the-capability.tex | 1 | Review: BULLRUN structural argument may stay | 2c |
| track-1/pos15-first-light.tex | 1 | Review | 2c |
| track-2/pos23-the-weight.tex | 1 | STAYS — personal testimony, not reconstruction | — |
| track-3/pos27-extension.tex | 1 | Review | 2c |
| record/twenty-years.tex | 1 | Review | 2c |
| bridge/pos06-the-secret.tex | 1 | Review | 2c |
| appendix/topic-guide.tex | 1 | Update index to point to egg if content moved | 2d |
| spine/why-relinquish.tex | 1 | srcnote only — STAYS | — |

### Build System Integration

No standalone-page pipeline exists yet. The current build produces one monolithic HTML file. Options:

**Option A — Separate HTML file:** `build/eggs/ultra-two.html` built by a new make target. Uses same CSS but is a separate page. Simplest to implement. Reader navigates away from main book to the egg page, uses Back button to return.

**Option B — Hidden section in main HTML:** Egg content is in the same HTML file but with `display:none` and no TOC entry. Revealed via JS when the URL fragment matches. Keeps everything in one file. But: the content is in the source of every copy of the main HTML, defeating the purpose of hiding.

**Decision: Option A.** Separate page. The egg page is self-contained HTML built from a source file in `manuscript/eggs/`. New make target: `make eggs`.

---

## Part 2: Puzzle Engine (Spiral Abstract Rewards)

### Concept

Each A-spine chapter ends with a puzzle that tests comprehension. Solving reveals the chapter's Spiral Abstract — the meta-view summary connecting the chapter to the larger argument. The reader *earns* the spanning path.

### Scope

**13 A-spine chapters = 13 puzzles.** Interludes (7) do NOT get puzzles — narrative/emotional register, puzzles would break it.

### The Homework Problem

**Risk: puzzles feel like homework.** This is the plan's biggest threat. Mitigations:
1. Puzzles test insight, not recall. Pattern recognition > fill-in-the-blank.
2. "Aha" moment must reinforce learning.
3. Wrong answers get a hint (not just "try again").
4. Spiral Abstracts are ALSO in the appendix — puzzles are an enhancement, not a gate.
5. Gen's aesthetic veto applies. If Gen says it feels like gamification, redesign.

### Answer Validation Concern

SHA-256 hashing means exact match (after normalization: lowercase, trim, strip articles). This WILL frustrate readers who have the right idea but wrong wording.

**Mitigation:** Multiple acceptable answers → multiple hashes. For keyword-match puzzles: normalize aggressively. For some puzzles: multiple-choice format is safer than free-text. **Design each puzzle's answer validation carefully — this is where puzzles succeed or fail.**

Recommendation: start with multiple-choice (3-4 options) for most puzzles. Reserve free-text for puzzles with unambiguous single-word answers (like "universality" or "percolation").

### Technical Architecture

**State:** `localStorage` key `'relinquishment-puzzles'`, value `{ "ch01": true, ... }`. Follows existing reader.js pattern.

**HTML structure:**
```html
<div class="puzzle-block" data-puzzle-id="ch01" data-answer-hash="[sha256]">
  <div class="puzzle-locked">
    <h4>Chapter Puzzle</h4>
    <p class="puzzle-question">[question]</p>
    [input or multiple-choice buttons]
    <button class="puzzle-submit">Check</button>
    <p class="puzzle-hint" style="display:none">[hint]</p>
  </div>
  <div class="puzzle-unlocked" style="display:none">
    <h4>Spiral Abstract</h4>
    [content]
  </div>
</div>
```

**Engine:** `build/puzzle-engine.js` (~150-200 lines). Hash input, compare, reveal, update menu. Appended to reader.js or loaded separately.

**Data:** `build/puzzle-data.yaml` — question, answer hash(es), hint, chapter mapping, puzzle type.

**Menu integration:** Progress indicator in navigation: "7/13 abstracts unlocked." Locked entries grayed with lock icon.

**Graceful degradation:** If JS fails or localStorage unavailable, puzzle blocks show "See appendix for spiral abstract."

**PDF:** Puzzles rendered as boxed exercises at chapter end. Spiral Abstracts always visible (no unlock mechanism — PDF is fixed medium).

### The 13 Puzzles Need Creative Design

This is NOT a Generator task. Each puzzle requires:
- Deep understanding of the chapter's core concept
- A question that tests insight, not memorization
- An answer with clean validation
- A hint that guides without giving away
- Playtesting with non-scientists

**Process:** Bruce + Gen + Auditor design puzzles one at a time. Start with 2 prototypes (recommend: the-flat and genesis — one easy, one medium). Build puzzle engine MVP with those 2. Playtest. Then design remaining 11.

### Puzzle Types (toolbox)

| Type | When to Use | Validation |
|------|-------------|-----------|
| Multiple choice (3-4 options) | When wrong answers are instructive | Button click |
| Free-text keyword | When answer is one unambiguous word | Hash after normalization |
| Pattern completion | Sequences, mathematical relationships | Exact match |
| Analogy completion | Cross-domain connections | Keyword match |

Start with multiple choice + free-text keyword only. Add fancier types later.

---

## Phases

### Phase 1: Puzzle Engine MVP (independent of Easter eggs)

**Scope:** Build the puzzle engine + 2 prototype puzzles (the-flat + genesis). Test in browser.

**Prerequisite:** Bruce + Gen approve concept and design 2 puzzles (question, answer, hint for each).

**Generator work:**
- puzzle-engine.js (~150-200 lines)
- puzzle-data.yaml (2 entries)
- CSS for puzzle blocks
- Menu progress indicator
- Inject puzzle blocks at end of 2 chapters via preprocess.py
- PDF rendering of puzzle blocks

**Acceptance:**
1. Both puzzles work in browser (wrong answer → hint → right answer → reveal)
2. localStorage persistence across page reload
3. Menu shows "0/2" → "1/2" → "2/2" as puzzles solved
4. PDF shows exercises without unlock mechanism
5. Graceful degradation without JS

**Estimate:** ~2-3 hours Generator time.

### Phase 2a: Easter Egg Infrastructure

**Scope:** Build the /eggs/ directory, build pipeline, manifest, make target. No content yet.

**Generator work:**
- `manuscript/eggs/` directory
- `build/easter-egg-manifest.yaml` (empty template)
- New make target: `make eggs` (builds egg pages with same CSS/fonts)
- Manifest verification in `make check`
- One test egg (`/eggs/test`) with placeholder content to validate pipeline

**Acceptance:**
1. `make eggs` produces `docs/downloads/eggs/test/index.html`
2. Test egg page renders with book styling
3. `make check` verifies manifest ↔ built eggs consistency
4. Test egg is not linked from main HTML

**Estimate:** ~1.5 hours Generator time.

### Phase 2b: ULTRA II Content Migration (heaviest phase)

**Scope:** Move reconstruction content from 4 manuscript files to egg page. Trim main text to ~10% spine.

**Prerequisite:** Bruce reviews the content audit (above) and confirms:
- What stays in main text (10% spine boundaries)
- What moves to egg
- What gets cut entirely (procedural detail)

**Files affected:**
- `appendix/timeline.tex` — project ULTRA II section (lines 104-215) → egg
- `appendix/abstracts.tex` — ULTRA II-clearance abstracts → egg
- `track-1/pos26-interdiction.tex` — reconstruction detail → egg
- `record/interdiction.tex` — mirrors pos26 → egg
- `manuscript/eggs/ultra-two.tex` — NEW: assembled egg content with epistemic color

**Generator work:**
- Assemble egg page from moved content
- Apply epistemic color system (guided-deduction confidence level)
- Trim main text files: keep coined term + existence + relationship + motivation
- Insert Tier 1 URL hint in prose near ULTRA II introduction
- Update easter-egg-manifest.yaml
- Update topic-guide.tex if index entries changed

**Acceptance:**
1. Main text "ULTRA II" count drops from 52 to ~15-20 (term usage + existence claims)
2. Egg page renders correctly at `/eggs/ultra-two`
3. Tier 1 hint is natural-sounding prose
4. `make html` + `make eggs` + `make check` all clean
5. PDF renders normally (egg content not in PDF — acceptable, same as other HTML-only features)
6. Egg page carries epistemic color system

**EDITORIAL NOTE:** The egg page must work as a standalone read. A reader arriving via the URL puzzle has no guarantee of having read the surrounding chapters. Open with enough context to orient.

**Estimate:** ~4-5 hours Generator time across 2 sessions. Judgment-heavy — may need halt-and-report.

### Phase 2c: Remaining ULTRA II Reference Review

**Scope:** Review the ~15 files with 1-3 ULTRA II references each. Most stay; some may need light trimming.

**Prerequisite:** Phase 2b complete.

**Files:** pos21, pos20, pos11, first-light, pos30, pos34, pos17, pos15, pos27, twenty-years, pos06.

**Decision rule:** If the reference is structural argument (convergence, capabilities, probability estimates) → stays. If the reference is reconstruction detail → trim or redirect to egg.

**Estimate:** ~1.5 hours Generator time. Mostly mechanical with a few judgment calls.

### Phase 2d: Post-Migration Verification

**Scope:** Full audit, topic-guide update, manifest finalization.

**Generator work:**
- `grep -rn "ULTRA.*II" manuscript/ --include="*.tex"` — every remaining hit must be justified
- Update topic-guide.tex index entries
- Finalize easter-egg-manifest.yaml
- `make html` + `make eggs` + `make check`
- Browser verification: egg page renders, main text reads naturally, PDF clean

**Estimate:** ~1 hour.

### Phase 3: Remaining 11 Puzzles (after MVP playtest)

**Scope:** Design and implement remaining 11 chapter puzzles.

**Prerequisite:** Phase 1 MVP playtested and approved. Bruce + Gen have designed all 13 puzzles (11 remaining).

**Generator work per puzzle:**
- Add entry to puzzle-data.yaml
- Verify hash(es)
- Test in browser

**Estimate:** ~30 min per puzzle = ~5.5 hours total across 2-3 sessions.

---

## Open Questions (for Bruce + Gen)

### Easter Eggs
1. ~~URL prefix~~ → `/eggs/` confirmed.
2. ~~Single vs chronological~~ → Single egg (annealed out).
3. Should the book ever acknowledge that easter eggs exist? Or pure discovery?
4. Bruce: review the content audit table above and confirm 10/90 split boundaries.
5. Bruce: what procedural detail should be CUT ENTIRELY (not moved)?

### Puzzles
6. Gen's aesthetic veto: does this feel like playful discovery or unwanted gamification?
7. Multiple-choice (safer validation) vs free-text (more satisfying) — default to MC for most?
8. Should wrong answers get hints? → Plan says yes, 1 hint per puzzle.
9. Progress indicator visible in main menu or only on dedicated page?
10. Puzzle difficulty: all p2 (12th grade) or early chapters p1?
11. Design 2 prototype puzzles (the-flat + genesis) before Phase 1.

### PDF
12. Exercises-at-chapter-end in PDF: include or omit entirely?
13. If included, answer in footnote, end-of-chapter, or appendix?

---

## Annealing Log (S64, 5-pass — one past comfort)

### HIGH — all candidates:
1. ✓ Easter eggs (ULTRA II) — strategic value high, attack-surface reduction
2. ✓ Puzzle engine — reader engagement, earning the spanning path
3. ✗ Chronological eggs (4 eggs) — killed. Scope creep. Single egg suffices.
4. ✗ Tier 2-4 puzzles for URL discovery — killed. Tier 1 only for now.
5. ✗ Future egg candidates (ChatGPT transcript, Custodian's letter, real acknowledgments) — deferred. Only ULTRA II is ready.
6. ✗ Preview SVGs for all 18 collapsed sections — killed (was in prior draft). Genesis previews done in S63.
7. ✗ Drag-and-drop puzzle type — killed. Too complex for MVP. Add later if needed.

### MEDIUM — test each component:
- Easter egg infrastructure: one-time cost, reusable for future eggs. ~1.5 hrs. KEEP.
- ULTRA II content migration: largest single task. 4-5 hrs. Judgment-heavy. KEEP — this is the strategic payoff.
- Puzzle engine MVP: ~2-3 hrs. Net-new JS but small footprint. KEEP — but needs Gen approval.
- 13 puzzle designs: creative task, not Generator work. Phase 3 gated on Bruce+Gen. KEEP but gate.

### LOW pass 1 — interactions:
- Easter eggs ↔ puzzles: technically independent. Easter egg URL discovery is a puzzle but uses a different mechanism (URL navigation, not localStorage). No code overlap. ✓
- Easter eggs ↔ 0230: ULTRA II reduction absorbed from 0230 into here. 0230 Change 2 eliminated. ✓
- Easter eggs ↔ 0232: independent. 0232's copy-button prompts don't interact with egg pages. ✓
- Puzzles ↔ PDF: graceful degradation designed in. ✓
- Phase order: 1 (puzzle MVP) and 2a (egg infrastructure) are independent — can run in parallel. 2b depends on 2a. 2c depends on 2b. 3 depends on 1 playtest. ✓

### LOW pass 2 — failure modes:
- Gen vetoes puzzles: Easter eggs still ship. Plans are independent. ✓
- ULTRA II 10/90 split too aggressive: egg content can be moved back. Git revert on Phase 2b. ✓
- Puzzle answer validation frustrates readers: multiple-choice default reduces this. ✓
- Easter egg URL leaks publicly: by design. Not security, just discovery. ✓
- SHA-256 for answer validation feels overengineered: it's anti-spoiler, not security. Source-view shows hashes, not answers. Determined readers check appendix. Acceptable. ✓

### LOW pass 3 — extra pass (past comfort):
- **End-to-end reader experience, puzzles:** Reader finishes the-flat, sees puzzle block, reads question, thinks, types answer, wrong, sees hint, thinks again, types, correct, abstract reveals with animation, menu updates. Is this actually FUN? Or does it feel like a quiz? The "aha" depends entirely on puzzle quality. Bad puzzles = homework. Good puzzles = discovery. This means puzzle DESIGN is the bottleneck, not puzzle ENGINEERING. The engine is ~150 lines of JS. The designs are 13 creative acts.
- **End-to-end reader experience, eggs:** Reader notices an unusual phrase near "ULTRA II." Curious. Types URL. Gets a standalone page with full reconstruction. Reads it. Returns to main book. Did the hint need to be explicit enough? Tier 1 (stated path) means the prose almost says it. But: how many readers actually try typing URLs? In 2026, URL-bar navigation is declining — most people click links. The hint might need to be more explicit than the plan assumes: "for the full reconstruction, look where records are kept" + `/eggs/the-full-reconstruction` or similar. Bruce decides.
- **PDF gap:** Easter egg content is HTML-only. PDF readers lose ~90% of ULTRA II reconstruction. Is this acceptable? Yes — the book is stronger without it. But: a PDF-only reader who cares about ULTRA II has no path to the content. One possible fix: a footnote in PDF like "Additional reconstruction at relinquishment.ai/eggs/..." — but this defeats the puzzle. Another: print the egg content as an appendix in PDF only (excluded from HTML TOC). Bruce decides.
- **Google indexing:** The egg page WILL be indexed by Google. Someone searching "relinquishment ULTRA II" will find it directly. The "hidden" page is only hidden from the book's navigation, not from the internet. Is this a problem? Probably not — the content is openly published under CC BY-ND 4.0. But it does mean the "puzzle discovery" experience only works for readers who DON'T Google first. For the kind of reader who Googles everything, the puzzle is meaningless. This is OK — those readers are already engaged enough to seek out extra content.
- **Puzzle engine and Firmware Update interaction:** The Firmware Update chapter has copy buttons for LLM priming. The puzzle engine has its own interactive elements. Two different interactive systems in the same HTML. Need to ensure they don't conflict: different CSS namespaces, different localStorage keys, different JS event handlers. Verify in Phase 1.

**Rating: 7/10.** (Down from prior 9/10 — honest assessment after thorough annealing.) Infrastructure is clear. ULTRA II migration is high-value but heavy. Puzzle design is the creative bottleneck, not engineering. Gen's aesthetic veto is unresolved. Multiple decisions pending. Phases are executable once decisions land.

---

## Connection to Other Plans

- **Plan 0230:** ULTRA II reduction (Change 2) absorbed here. 0230 now contains only Continental Drift + Unbuilt Bridge.
- **Plan 0232:** Independent. Copy-button prompts don't interact with eggs or puzzles. But philosophically aligned (reader-as-active-participant).
- **Plan 0101 (Firmware Update):** Copy-button infrastructure already exists. Puzzle engine is net-new but follows same patterns.
