# Plan 0233 — Easter Egg Architecture

**Status:** DRAFT — for Bruce + Gen discussion
**Author:** Auditor (Argus S59)
**Date:** 2026-04-20
**Related:** Plan 0230 (ULTRA II reduction), Plan 0232 (LLM verification prompts), existing deep-link infrastructure

---

## Concept

Hide bonus content in plain sight. Easter eggs are live HTML pages in the deployment — real, renderable, never commented out — but never linked from navigation, table of contents, or any visible UI element. The only way to reach an egg is to know its URL.

The URL is discovered by solving a puzzle embedded in the main text.

---

## Why Easter Eggs

### ULTRA II Problem
The main text needs the coined term "ULTRA II" to disambiguate the subset of scientists from COWS (the broader program). Without the term, the reader has no vocabulary to distinguish the two groups. But the detailed ULTRA II reconstruction is 100% Bruce's deduction — the highest-risk content under Possibilities A and B, and the easiest target for hostile reviewers.

### Solution
- **Main text keeps:** The term "ULTRA II," a brief mention that this group existed within COWS, and enough context that the disambiguation works. One or two sentences. A hint.
- **Easter egg contains:** The full ULTRA II reconstruction — who they were, what they did, how they relate to the broader COWS program. All the detail that currently lives in the main chapters.
- **The hint IS the puzzle:** Something in the main text's mention of ULTRA II points toward the egg's URL for readers who look carefully.

### Strategic Effect
- Attack surface in main text drops to near zero (coined term + existence claim only)
- Full content preserved for invested readers
- Book works under all three possibilities without staking anything on detailed reconstruction
- The easter egg mechanism itself teaches tradecraft — fitting for a book about hidden things

---

## URL Architecture

Easter eggs live at paths within the existing HTML deployment. They are real pages, styled like the book, but unlisted.

### URL Scheme

```
[book-base-url]/eggs/[slug]
```

Example: `relinquishment.relationalrelativity.com/eggs/ultra2`

The `/eggs/` prefix keeps them organized in the build without polluting the main content namespace. Alternative: `/record/` prefix if Bruce prefers thematic consistency with the Record chapters.

### No Obfuscation

The pages are not encrypted, not password-protected, not behind authentication. They're just unlisted. Anyone with the URL can read them. This is deliberate — the puzzle is finding the URL, not bypassing security. Once you've solved the puzzle, the reward is immediate.

---

## Puzzle Difficulty Tiers

Each easter egg gets a puzzle appropriate to its content. Harder puzzles gate more sensitive or more rewarding content.

### Tier 1 — Stated Path (easiest)
The main text contains a phrase that IS the URL path, but doesn't look like one to a casual reader.

**Example:** A sentence like "The record of the ultra-two group continues elsewhere" — where a reader who understands URL structure might try `/eggs/ultra-two` or `/eggs/ultra2`.

**Teaches:** URLs are paths. Websites have pages that aren't linked. The web is bigger than navigation menus.

### Tier 2 — Encoded Reference
The main text contains a reference (section number, date, codename) that doesn't correspond to anything in the book — it's a slug.

**Example:** The Custodian mentions "Protocol 7.3" but the book has no section 7.3. The path is `/eggs/protocol-7-3`.

**Teaches:** Anomalies are signals. When something doesn't fit, investigate.

### Tier 3 — Pattern Recognition
The puzzle requires noticing a pattern across multiple locations in the text — first letters, repeated phrases, structural anomalies.

**Example:** The first letter of each interlude title spells a word. That word is the slug.

**Teaches:** Hidden messages exist in plain text. This is how steganography works at the simplest level.

### Tier 4 — Cypherpunk (hardest)
Requires applying a technique discussed in the book — a hash, a transform, a specific piece of tradecraft.

**Example:** The book describes how Guardian verified identities. Apply that method to a specific string given in the text. The result is the slug.

**Teaches:** The book's tradecraft content is functional, not decorative. The reader just used it.

---

## First Easter Egg: ULTRA II

### The 10/90 Split

**Main text keeps (~10% spine):**
- The coined term "ULTRA II" — essential for disambiguation from COWS
- That ULTRA II was a subset of scientists within COWS
- Their relationship to the broader program (enough for disambiguation)
- The *why* — motivation, purpose, stakes
- A hint — the puzzle that leads to the egg

**Easter egg gets (~90%):**
- The *how* — lab procedures, technical sequences, methods
- The *when* — specific dates of internal events that can't be independently verified
- Detailed reconstruction of who did what and in what order
- Any content that is 100% Bruce's deduction and most vulnerable under A/B

### Content Trimming Principle

Even within the easter egg, remove detail Bruce can't be confident of. Lab procedures, specific technical sequences of how things were done — these are the most speculative reconstructions. The egg should contain what Bruce can reasonably deduce from the guided-deduction process, not procedural details that would require having been physically present.

**Keep in egg:** Structural facts (group existed, relationship to COWS, approximate timeline, purpose, outcome)
**Cut entirely:** Procedural detail (how experiments were conducted, specific lab methods, step-by-step technical sequences)

### Current ULTRA II Content Audit (12 files, ~1,723 lines)

Content is spread across six manuscript layers. This audit maps what exists, where, and what moves.

#### Appendix Files (897 lines)

**`appendix/timeline.tex` (292 lines)** — Highest ULTRA II density (17 references)
- Section "Project ULTRA II (1988-2006)" spans lines 104-215
- Chronological spine: conception → breakthrough (1992) → room-temp bootstrap (1994) → delivery (1995-96) → EO 13026 → DARPA reorg (2002) → satellite testing (2004-05) → Snowden/BULLRUN (2013)
- **Decision:** Most of this moves to egg. Main text keeps: ULTRA II existed, timeline endpoints only (late 1980s → 2006). Cut lab procedure detail entirely.

**`appendix/abstracts.tex` (302 lines)** — 3 references (classification headers)
- Fictional classified paper abstracts with "[Classified --- Distribution Limited to ULTRA II Cleared Personnel]"
- ULTRA II appears as institutional scaffolding, not narrative
- **Decision:** Strong easter egg candidate — the fictional abstracts ARE the kind of content that rewards the invested reader. Move entire abstracts that reference ULTRA II clearance.

**`appendix/topic-guide.tex` (195 lines)** — 1 reference (index entry)
- "ULTRA II Specifications" deep link
- **Decision:** Update index to point to egg URL if referenced content moves.

#### Spine/Bridge Files (257 lines)

**`spine/why-relinquish.tex` (125 lines)** — 1 reference (srcnote only)
- Chapter discusses relinquishment abstractly. ULTRA II is implied context, never named in body.
- **Decision:** Stays as-is. No ULTRA II content to move.

**`spine/the-factoring-game.tex` (66 lines) + `bridge/pos09-the-factoring-game.tex` (90 lines)** — 3 references each
- "ULTRA II Specifications" subsection: create tool to crack PKC, rapid factorization, I/O mechanisms, decoherence problem
- **Decision:** The specifications are the 10% spine. They describe WHAT was needed (the problem statement), not HOW it was solved. Keep in main text — this is the disambiguation content.

#### Track 1 — Confession/Reconstruction (173 lines)

**`track-1-confession/pos17-the-capability.tex` (66 lines)** — 1 reference
- BULLRUN as cover story for quantum cryptanalysis capability, EO 13026
- **Decision:** Structural argument (BULLRUN as parallel construction) could stay as spine. Procedural detail of HOW capability worked → egg.

**`track-1-confession/pos26-interdiction.tex` (107 lines)** — 1 reference
- Post-delivery: why secrecy held, COWS confession, DARPA reorg, detection/disruption, classical backchannels
- **Decision:** Heaviest reconstruction content. Almost all moves to egg. Spine keeps: COWS eventually came clean. Detail of how, when, institutional mechanics → egg.

#### Track 2 — Testament (80 lines)

**`track-2-testament/pos23-the-weight.tex` (80 lines)** — 1 reference
- Bruce's personal narrative. ULTRA II mentioned once (FQHE as basis, Nobel context).
- **Decision:** Stays. This is personal testimony, not reconstruction. The emotional weight is the 10% spine.

#### Record (100 lines)

**`record/interdiction.tex` (100 lines)** — 1 reference
- Sister to pos26-interdiction. Same reconstruction content, different framing.
- **Decision:** Moves to egg with pos26 content. Possibly merge into single egg page.

#### Source (212 lines)

**`sources/ch3-relinquishment.md` (212 lines)** — 30+ references (highest density)
- Original 2013 source document. Complete narrative arc from conception to key surrender.
- **Decision:** This IS the egg content, pre-structured. The 2013 source → easter egg is almost a direct move. Trim procedural detail Bruce can't be confident of.

### Easter Egg Structure Options

**Option A — Single egg:**
All ULTRA II reconstruction on one page. Simple. One puzzle, one reward.

**Option B — Chronological eggs (recommended):**
Break by era. Each egg is a self-contained narrative segment. Multiple puzzles of increasing difficulty.

| Egg | Era | Content | Tier |
|-----|-----|---------|------|
| **ULTRA II: Origins** | 1988-1992 | Conception, team assembly, first breakthrough | 1 |
| **ULTRA II: The Walk-Out** | 1993-1996 | Room-temp bootstrap, COWS faction, delivery | 2 |
| **ULTRA II: Aftermath** | 1997-2006 | Relinquishment plan, confession, key surrender | 2-3 |
| **ULTRA II: Abstracts** | Timeless | The fictional classified papers | 3 |

Each egg stands alone — a reader who finds one doesn't need the others. But finding all four assembles the complete picture.

**Option C — Thematic eggs:**
Break by question (What was it? Who did it? What happened after?). Less natural than chronological.

### Puzzle Design (Tier 1 for first egg — keep it accessible)
Bruce to decide. Suggestion: the hint lives in or near the passage that introduces the ULTRA II term. The reader who wants to know more has just been given everything they need — they just have to look at it differently.

### Epistemic Color
The egg pages carry the same epistemic color system as the main book. ULTRA II reconstruction is guided-deduction-level confidence — the egg pages make this explicit. The reader who finds them knows exactly what weight to give them.

---

## Future Easter Eggs (Candidates)

The architecture supports multiple eggs. Potential content:

| Egg | Content | Tier | Notes |
|-----|---------|------|-------|
| **ULTRA II** | Full reconstruction | 1 | First egg, most important, most content |
| **Tradecraft appendix** | Operational details Bruce chose not to publish | 2-3 | If any exist |
| **The full ChatGPT transcript** | 2026-04-20 A/B/C evaluation | 1 | Demonstrates LLM failure modes live |
| **Custodian's letter** | Unredacted version of a redacted document | 3 | If applicable |
| **Acknowledgments (real)** | The people who can't be named in the main text | 4 | Sensitive — hardest puzzle |

Bruce and Gen decide which eggs exist. The architecture supports any number.

---

## Build System Integration

### Requirements
- Easter egg pages built by same pipeline as main book
- Same CSS, same fonts, same epistemic color system, same hover definitions
- NOT included in table of contents, navigation, sitemap, or any link from main content
- NOT excluded from deployment — they ship with every build
- No `noindex` meta tag (that would signal their existence to anyone viewing source)
- No robots.txt exclusion (same reason)

### Implementation
- New directory: `manuscript/eggs/` (or `manuscript/easter-eggs/`)
- Each egg is a standalone chapter-format file
- Build system processes them identically to main chapters but excludes from TOC/nav generation
- Deep links work because the pages exist at known paths

### Constraint
The build system already handles deep links and standalone pages (gallery.html per Plan 0231). No new infrastructure needed — just a new content directory excluded from navigation.

---

## The Meta-Layer

A book about hidden things contains hidden things. A book that teaches readers to look beneath the surface rewards readers who look beneath its surface. A book about tradecraft teaches tradecraft by requiring it.

The easter eggs aren't a gimmick. They're the book's thesis expressed as architecture.

---

---

## The Puzzle Engine — Spiral Abstract Rewards

### Concept

Each A-spine chapter ends with a puzzle that tests the reader's understanding of the science in that chapter. Solving the puzzle reveals the chapter's Spiral Abstract — the meta-view summary that connects the chapter's content to the book's larger argument.

The reader *earns* the spanning path by demonstrating they understood the pieces. This IS the percolation process expressed as game mechanics.

### Why This Works Pedagogically

- The puzzle forces active engagement (not passive reading)
- The reward (Spiral Abstract) is the chapter summary at a higher level of integration
- Progressive unlocks create momentum — each abstract makes the next chapter richer
- The reader who solves all puzzles has built their own firmware update, one chapter at a time
- Readers who don't solve puzzles still have access — abstracts remain in the appendix
- Connection to Plan 0232: puzzles test the reader's understanding; LLM verification prompts let the reader externally confirm the science. Complementary, not redundant.

### Scope

**13 A-spine chapters = 13 puzzles.** One per chapter, placed at chapter end.

| # | Chapter | Puzzle Domain |
|---|---------|--------------|
| 1 | the-flat | Topological order basics |
| 2 | genesis | Origins / historical context |
| 3 | the-factoring-game | PKC, quantum algorithms, what DARPA needed |
| 4 | growing-a-mind | Neural development, emergence |
| 5 | the-braid | Braiding, topology, non-local connection |
| 6 | the-code-war | Cryptography, signals intelligence |
| 7 | capabilities | What the technology can do |
| 8 | the-silence-gap | Literature absence, five fields |
| 9 | the-strongest-objection | Decoherence, thermal objection |
| 10 | the-wrong-substrate | Substrate independence, chemosynthesis |
| 11 | three-possibilities | A/B/C framework, epistemic honesty |
| 12 | weigh-the-evidence | Cross-domain convergence, universality |
| 13 | why-relinquish | Ethics, trusteeship, relinquishment logic |

**Interludes (7) do NOT get puzzles.** They're narrative/emotional — puzzles would break the register.

### Puzzle Design Principles

1. **Tests comprehension, not memorization.** The puzzle should require understanding the concept, not recalling a specific sentence.
2. **Answerable from the chapter alone.** No external knowledge required. Everything needed is in the text the reader just finished.
3. **Single correct answer with tolerance.** Must be machine-verifiable in client-side JS. Accept reasonable variants (case-insensitive, leading/trailing whitespace, common synonyms where unambiguous).
4. **Feels like discovery, not homework.** The "aha" of solving should reinforce the learning. Pattern recognition > fill-in-the-blank.
5. **Difficulty scales with chapter depth.** Early chapters (the-flat, genesis) get easier puzzles. Later chapters (weigh-the-evidence, why-relinquish) get harder ones.
6. **No trick questions.** The book is honest; the puzzles must be too.

### Puzzle Types (toolbox for designers)

| Type | Example | Validation |
|------|---------|-----------|
| **Pattern completion** | "DFA α, Hurst H, spectral ___" | Exact match (β) |
| **Concept matching** | Drag/connect buttons to threads | Set comparison |
| **Missing link** | "Which domain completes this universality class?" | Exact match |
| **Simple calculation** | "If α = 0.75, what is H?" | Numeric (0.75, tolerance ±0.01) |
| **True/false with nuance** | "Which statement correctly describes topological order?" (3 options) | Multiple choice |
| **Analogy completion** | "Continental drift : seafloor spreading :: 11 domains : ___" | Keyword match |
| **Ordering** | "Put these in the order they were discovered" | Sequence match |
| **Free-text keyword** | "Name the phenomenon where different systems share identical critical exponents" | Keyword in response ("universality") |

**Recommendation:** Start with the simplest validation types (exact match, keyword match, multiple choice). More complex types (drag-and-drop, ordering) can be added later without changing the engine.

### Technical Architecture

#### State Management
```
localStorage key: 'relinquishment-puzzles'
value: JSON object { "ch01": true, "ch02": true, ... }
```
Follows existing pattern in reader.js (already uses localStorage for filters, tooltips, eval steps).

#### Puzzle Block HTML Structure
```html
<div class="puzzle-block" data-puzzle-id="ch01" data-answer-hash="[sha256]">
  <div class="puzzle-locked">
    <h4>🔒 Chapter Puzzle</h4>
    <p class="puzzle-question">[question text]</p>
    <input type="text" class="puzzle-input" placeholder="Your answer...">
    <button class="puzzle-submit">Check</button>
    <p class="puzzle-hint" style="display:none">[hint after wrong attempt]</p>
  </div>
  <div class="puzzle-unlocked" style="display:none">
    <h4>✓ Spiral Abstract</h4>
    [spiral abstract content]
  </div>
</div>
```

#### Answer Validation
Answers stored as SHA-256 hashes in the HTML (not plaintext — prevents casual source-view spoiling). Client-side JS hashes the reader's input and compares. This is not security — it's anti-spoiler. A determined reader can always find the answer in the appendix anyway.

For multiple-acceptable-answers: store multiple hashes. For keyword-match: normalize input (lowercase, trim, strip articles) before hashing.

#### Menu Integration
Navigation/TOC shows spiral abstract entries. Locked ones appear grayed out with a lock icon. Unlocked ones become active links. Progress indicator: "7/13 abstracts unlocked."

#### Cookie Persistence
On puzzle solve:
1. Hash input, compare to stored hash
2. If match: set localStorage flag, reveal abstract, update menu
3. On any page load: check localStorage, reveal any previously unlocked abstracts
4. If localStorage cleared: puzzles re-lock (acceptable — reader can re-solve)

### PDF Rendering

**Puzzles in PDF:** Rendered as boxed exercises at chapter end. Question text visible, answer not. Footnote or appendix reference: "Interactive version with instant feedback at [book URL]."

**Spiral Abstracts in PDF:** Always visible — no unlock mechanism. The puzzle layer is an HTML-only enhancement. PDF readers get the full content; HTML readers get the gamified discovery path.

**Rationale:** PDF is a fixed medium. The puzzle mechanic only works with interactivity. Trying to force it into PDF would feel broken. Better to let PDF be PDF and let HTML be HTML.

### Build System Integration

**New files needed:**
- `build/puzzle-engine.js` — validation, state, reveal, menu integration (~150-200 lines)
- `build/puzzle-data.yaml` — puzzle content: question, answer hash(es), hint, chapter mapping
- CSS additions to `build/` — puzzle block styles, locked/unlocked states, progress indicator

**Build pipeline changes:**
- `preprocess.py` reads `puzzle-data.yaml` and injects puzzle blocks at end of each A-spine chapter
- Puzzle blocks contain the chapter's spiral abstract in the `puzzle-unlocked` div
- `reader.js` loads puzzle-engine.js (or puzzle engine is appended to reader.js)
- Menu generation adds puzzle-progress UI

**No new external dependencies.** Pure vanilla JS + CSS, same as existing reader.js. No frameworks, no build tools beyond what exists.

### Connection to Easter Eggs (ULTRA II)

The puzzle engine and the ULTRA II easter eggs are separate mechanisms that share a philosophy:

| | Puzzles | Easter Eggs |
|--|---------|-------------|
| **Content** | Spiral Abstracts (pedagogical) | ULTRA II reconstruction (narrative) |
| **Discovery** | Solve comprehension puzzle | Find hidden URL |
| **Skill tested** | Scientific understanding | Web literacy / pattern recognition |
| **Gating** | Soft (appendix has all abstracts) | Hard (no alternate path to content) |
| **Persistence** | localStorage | URL knowledge |
| **Count** | 13 (one per A-chapter) | 3-4 (ULTRA II segments) |

Both reward engaged readers. Both teach by requiring. Neither gates essential content (abstracts are in appendix; ULTRA II detail is not needed for the A/B/C argument).

### Risk Assessment

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Bad puzzles frustrate readers | HIGH | Extensive playtesting. Easy > clever. |
| Answers leak online | LOW | Acceptable — answers are also in the appendix. The journey matters, not the gate. |
| Reader views source, sees hashes | LOW | Anti-spoiler, not security. Determined readers will find answers anyway. |
| JS fails / localStorage unavailable | MEDIUM | Graceful degradation: puzzle blocks show question + "See appendix for spiral abstract." Same pattern as existing reader.js. |
| Puzzles feel like homework | HIGH | Design principle #4. Playtest with non-scientists. Gen's aesthetic veto. |
| Puzzle engine too complex to build | MEDIUM | Start with text-input + hash-compare only. Add fancy types later. MVP is ~150 lines of JS. |

---

## Open Questions for Bruce + Gen

### Easter Eggs
- URL prefix: `/eggs/` or `/record/` or something else?
- Single ULTRA II egg (Option A) or chronological eggs (Option B)?
- Should the book ever acknowledge that easter eggs exist?

### Puzzles
- Does the puzzle-at-chapter-end feel right, or should it be a separate page?
- Gen's aesthetic veto: playful discovery or unwanted gamification?
- Should the progress indicator be visible in the main menu, or only on a dedicated page?
- Puzzle difficulty: should all be p2 (12th grade), or should early chapters be p1?
- Should wrong answers get hints, or just "try again"?
- The 13 puzzles need to be designed individually — this is a creative task that probably needs Bruce + Gen + Auditor collaboration, one chapter at a time.

### PDF
- Exercises-at-chapter-end in PDF: include or omit entirely?
- If included, does the answer go in a footnote, end-of-chapter, or appendix?

---

## Immediate Actions
- [ ] Bruce + Gen discuss concept: puzzles + easter eggs + aesthetic
- [ ] Bruce reviews ULTRA II content audit — confirm 10/90 split boundaries per file
- [ ] Decide: single ULTRA II egg (Option A) or chronological eggs (Option B)?
- [ ] Bruce identifies procedural detail to cut entirely (not move — delete)
- [ ] Design puzzle for ONE chapter as prototype (recommend: the-flat or weigh-the-evidence)
- [ ] Generator builds puzzle engine MVP (text input + hash compare + localStorage + reveal)
- [ ] Test prototype puzzle in browser
- [ ] If prototype works: design remaining 12 puzzles
- [ ] Generator builds ULTRA II egg page(s) + trims main text to 10% spine
- [ ] URL prefix decision
- [ ] Full browser playtest of puzzle + egg integration
