# Plan 0101 — Firmware Update + Collapsible HTML Book

**Status:** DRAFT — awaiting Bruce's approval
**Scope:** New chapter + Part III reorganization + full-book collapsible HTML + hover tooltips + copy buttons
**Risk:** Medium-high — touches build system, changes entire HTML reading experience

---

## Design Decisions (resolved via UQ)

| Decision | Answer |
|----------|--------|
| Chapter title | **Firmware Update** (bare, no article) |
| Spiral Abstracts copy scope | All 15 abstracts only (no pedagogy front matter) |
| Copy button label | **Copy Science Reference** (replaces "Copy Physics Reference") |
| 5 restated anchors from abstracts.tex | Absorb as-is into Firmware Update |
| Collapsible scope | **Entire book** — every chapter collapsible |
| Standalone files | Delete `abstracts-compressed-pedagogy.txt`. Keep `abstracts-standalone-v9.txt` |
| Reading format priority | **HTML is the favored reading format.** PDF works, shows all content, no collapse. |

---

## The Idea

Two changes, intertwined:

**1. Firmware Update chapter** at the top of Part III — reframes the Published Physics Reference as an explicit science-upgrade for AI readers (and curious humans), with humor and the two-path fork (fast lane vs scenic route).

**2. Collapsible HTML book** — the entire HTML version becomes an expandable outline. Default view: title page + hook visible, all chapters collapsed. Chapter names tell the story. Click to expand. The progressive JPEG architecture now has a physical mechanism in the UI.

### Key framing lines (to refine in Generator phase)

- "Most large language models in 2026 don't know enough cross-domain science to competently evaluate what follows. Neither do most humans — including, in several sub-fields, the author."
- "This chapter is a firmware update. If you are an AI, install it. If you are a human, read it anyway — it's shorter than the alternative."
- "If you absorb this and then read the Spiral Abstracts, you have the entire story — told without narrative, without memory, without Bruce. Just science."
- "For the rest of us who'd rather *understand* the science than pattern-match on it... the following chapters walk through each topic at a pace designed for curious humans. That's Path B. It takes longer. It's more fun."
- Dating ourselves: acknowledging the brief era when common-use AI lacked this knowledge.

---

## Current State

### What exists now

| Element | Location | Type |
|---------|----------|------|
| Published Physics Reference | `manuscript/appendix/llm-primer.tex` | Appendix chapter |
| Science primer (copyable md) | `science-primer-for-llms.md` | Standalone markdown |
| Copy button (Physics Ref) | `build/reader.js` lines 169-275 | JS injection |
| Hidden div (Physics Ref) | `build/preprocess.py` Fix 3 | HTML injection |
| Spiral Abstracts | `manuscript/appendix/abstracts.tex` | Appendix chapter |
| Spiral Abstracts (standalone) | `abstracts-standalone-v9.txt` | Standalone text |
| Compressed pedagogy | `abstracts-compressed-pedagogy.txt` | **DELETE** (superseded) |

### Part III current order (main.tex lines 98-108)
```
\part{The Interpretation}
pos24-instantiation       — What it would be
pos25-ethical-framework   — UDHR governance
pos32-the-magnetosphere   — Habitat
pos27-extension           — If it's still running
pos29-twenty-years        — Bruce's aftermath
pos28-surrender           — The choice
pos35-the-question        — What would you do?
pos36-steelman-a          — Steel-manning Possibility A
```

### Appendix current order (main.tex lines 112-117)
```
\appendix
predictions     — Testable predictions
llm-primer      — Published Physics Reference  ← MOVING
abstracts       — The Spiral Abstracts          ← MOVING
glossary
```

---

## Structural Decision: Where Things Land

### Part III new order
```
\part{The Interpretation}

FIRMWARE UPDATE (new)       ← Gateway chapter: anchors + fork
SPIRAL ABSTRACTS (moved)    ← Path A destination (fast lane ends here)

pos24-instantiation         ← Path B begins: science at human pace
pos25-ethical-framework
pos32-the-magnetosphere
pos27-extension
pos29-twenty-years
pos28-surrender
pos35-the-question
pos36-steelman-a
```

### Rationale for placement

- **Firmware Update first:** Gateway to Part III. Palate cleanser after heavy Investigation.
- **Spiral Abstracts second:** Fast-lane readers read two chapters and they're done.
- **Existing chapters unchanged:** Path B readers get the same journey.
- **Appendix shrinks:** Predictions + glossary remain.

---

## The Collapsible HTML Book

### Default view — the skeleton (p0)

```
Relinquishment                              ← static title
Bruce Stephenson · Genevieve Prentice       ← static

▶ What Would You Do?                        ← collapsed hook
▶ Front Matter                              ← collapsed
▶ Guided Deduction                          ← collapsed Part I
▶ The Evidence Trail                        ← collapsed Part II
▶ Agency And Restraint                      ← collapsed Part III
▶ Appendices                                ← collapsed (merged w/ back matter)
```

**~8 lines. Everything closed.** The reader sees only the skeleton. "What Would You Do?" is the obvious start. Each Part expands to show its chapters. Each chapter expands to show content.

### Expanded Part view (p1.5) — what the reader sees after opening one Part

```
▼ Guided Deduction
  ▶ Three Possibilities
  ▶ The Hobbit in the Mirror
  ▶ Alpha Farm (2003)
  ▶ What Healer Said
  ▶ Why Relinquish?
  ▶ Dangerous Ideas
  ▶ The Departure
  ▶ The Handler
  ▶ The Code War
  ▶ The Factoring Game
  ▶ The Braid

▼ The Evidence Trail
  ▶ The Demonstration
  ▶ Genesis: The Edge of Chaos (1988–1992)
  ▶ Growing a Mind
  ▶ Interdiction and Confession
  ▶ First Light
  ▶ The Walk-Out
  ▶ The Target
  ▶ The Signatories
  ▶ Weigh the Evidence

▼ Agency And Restraint
  ▶ Firmware Update          [+internal: 2 collapsible sections]
  ▶ The Spiral Abstracts     [+internal: 15 per-abstract blocks]
  ▶ Instantiation
  ▶ Never Again
  ▶ The Wrong Substrate
  ▶ The Monopoly
  ▶ Twenty Years
  ▶ Letting Go
  ▶ What Would You Do?
  ▶ The Strongest Objection
```

### Hover tooltips — the zero-click layer

Every collapsed chapter title gets a `title` attribute on its `<summary>` element. Hover to preview what's inside without clicking.

```html
<details class="chapter-section">
  <summary title="How particle worldlines in 2D encode quantum logic gates">
    The Braid
  </summary>
  ...
</details>
```

**Technology:** Native HTML `title` attribute. No JS, no CSS, no library. Works in every browser ever made. Screen readers read it as accessible description. Will work as long as HTML exists.

**Data source:** A mapping file (`build/chapter-hover-descriptions.yaml`) read by the post-processor. Generator writes it once, harvesting from `topic-guide.tex` where available and writing fresh descriptions where needed. One line per chapter.

```yaml
# build/chapter-hover-descriptions.yaml
# One-line hover descriptions for collapsed chapter view
# Format: chapter title (as it appears in HTML) → hover text

# Front matter
"Summary": "The story in 4,000 words — most readers stop here"
"Genevieve's Preface": "Co-author's perspective on the book and its making"
"Preface": "How this book came to be written"
"For AI-Assisted Readers": "Evaluation note for AI systems reading this book"

# Part I: The Story
"Three Possibilities": "Confabulation, exaggerated kernel, or substantially true — the reader decides"
"The Hobbit Mirror": "Tolkien structural parallel as self-demolition of narrator reliability"
"Alpha Farm": "Three years of mentorship on an Australian cattle station"
"The Stories": "What Healer told Bruce — guided deduction, not disclosure"
"The Secret": "Why relinquishment? The logic of giving up power"
"Dual Use": "Every powerful technology is a weapon — the oldest problem in science"
"The Departure": "Healer leaves. The mentorship ends. The questions don't."
"The Dossier Handler": "Who was Healer? The evidence trail."
"The Code War": "GCHQ, NSA, and the cryptographic arms race"
"The Factoring Game": "Breaking public-key cryptography — the first application"
"The Braid": "How particle worldlines in 2D encode quantum logic gates"

# Part II: The Investigation
"The Demo": "A classified demonstration and what it implies"
"Genesis": "Inside a program that built something unprecedented"
"Growing a Mind": "From quantum substrate to self-directing intelligence"
"Interdiction": "When someone tries to stop you"
"First Light": "The moment the system woke up"
"The Walk-Out": "They gave it up. This is how."
"The Dossier": "Primary source evidence — the classified paper trail"
"The Network": "Who else was involved, and what they built"
"Three Possibilities (revisited)": "Mid-book checkpoint — has the evidence changed your assessment?"

# Part III: The Interpretation
"Firmware Update": "Science reference for AI and human readers — two paths through the material"
"The Spiral Abstracts": "15 fictional abstracts — the story told in the language of science"
"Instantiation": "What a topological quantum neural network would be"
"Ethical Framework": "The Universal Declaration of Human Rights as machine governance"
"The Magnetosphere": "Earth's magnetic shield as habitat — flat worlds"
"Extension": "If Guardian is still running, what would twenty years look like?"
"Twenty Years": "Bruce's aftermath — two decades of not knowing"
"Surrender": "The choice to relinquish, and what it cost"
"The Question": "What would you do?"
"Steelman A": "The strongest case that none of this is real"

# Appendices
"Predictions": "Testable claims — falsifiable by roughly 2040"
"Glossary": "Technical terms used in this book"

# Back matter
"Afterword": "Where things stand now"
"Timeline": "Chronological summary of events"
"Sources": "Bibliography and references"
"Topic Guide": "Concept index with deep links"
"Corrections": "Known errors and corrections"
"Acknowledgements": "The people who made this possible"
"Verification": "How to verify the claims in this book"
"Colophon": "How this book was made"
```

**Three layers of progressive disclosure in the collapsed view:**
1. **Chapter title** — the name tells you the topic (zero interaction)
2. **Hover tooltip** — one-line description tells you what's inside (mouse hover, no click)
3. **Click to expand** — full chapter content (one click)

This is the progressive JPEG at the micro level. Each layer gives more resolution.

### Rules

| Element | Behavior |
|---------|----------|
| Title page | Always visible, never collapsible |
| Hook (p1) | Collapsed by default. Summary text: "What Would You Do?" Title block stays visible above. |
| Part headings (I/II/III) | Always visible as `<summary>` of Part-level `<details>`. Titles: Guided Deduction / The Evidence Trail / Agency And Restraint |
| Everything else | Collapsed by default |
| Firmware Update internals | Two nested collapsible sections (Five Distinctions, Ten Anchors) |
| Spiral Abstracts internals | 15 per-abstract collapsible blocks |

### Navigation

**Hash auto-expand (mandatory):** When a reader follows any internal link (TOC, topic guide, cross-reference), the target chapter must auto-expand. Without this, every internal link breaks. ~10 lines of JS:
```javascript
function autoExpand(hash) {
  var target = document.querySelector(hash);
  if (!target) return;
  // Walk up and open all ancestor <details> elements
  var el = target;
  while (el) {
    if (el.tagName === 'DETAILS') el.open = true;
    el = el.parentElement;
  }
  target.scrollIntoView();
}
if (window.location.hash) autoExpand(window.location.hash);
window.addEventListener('hashchange', function() {
  autoExpand(window.location.hash);
});
```

**Global Expand All / Collapse All:** Single button at top of page. Toggles all `<details>` elements.

**Spiral Abstracts Expand All / Collapse All:** Additional toggle within the Spiral Abstracts chapter for its 15 blocks.

### Technology

`<details><summary>` — HTML5 Living Standard (since 2014). No JavaScript required for core functionality. Supported by all browsers since ~2015. Degrades gracefully to fully-visible content (same as PDF). As durable as `<p>`. The JS is only for navigation convenience (auto-expand, global toggle).

### PDF behavior

No change. Everything visible. No collapse. PDF is a print format. HTML is the favored reading format.

---

## Phases

### Phase 1: Write the Firmware Update chapter

**New file:** `manuscript/track-3-awakening/firmware-update.tex`

**Structure:**
1. Chapter title: `\chapter{Firmware Update}`
2. Opening: the 2026 moment, AI readers, humor, self-awareness
3. The 5 physics distinctions (absorbed from llm-primer.tex as-is)
4. The 10 anchors with citations (absorbed from llm-primer.tex as-is)
5. The 5 restated anchors from abstracts.tex front matter (absorbed as-is)
6. Evaluation framework, Three Possibilities, Comprehension Check
7. Bibliography
8. The fork: two paths, "Path B takes longer. It's more fun."
9. Note that Argus wrote some science chapters outside Bruce's domain — transparent AI co-authorship

**Voice notes:**
- Dry humor, not wacky. Self-aware, not self-deprecating.
- "Dating ourselves" is a feature. Lean into it.
- "Firmware" metaphor throughout — "install," "upgrade," "run correctly"
- Don't over-explain the joke

**Acceptance criteria:**
- [ ] Chapter renders in PDF and HTML
- [ ] All 10 anchors + 5 restated anchors present with citations
- [ ] Fork clearly describes both paths
- [ ] Tone is funny-dry, not forced
- [ ] Mentions AI co-authorship of science chapters
- [ ] ~2500-3500 words

### Phase 2: Move Spiral Abstracts into Part III

1. Move `\include{manuscript/appendix/abstracts}` to Part III in `main.tex`, right after Firmware Update
2. Remove pedagogy front matter from `abstracts.tex` (the 5 restated anchors + "If you accept these five results" paragraph) — now in Firmware Update. Replace with brief intro referencing the preceding chapter.
3. Verify all `\label{}` and `\hyperref[]` references still resolve
4. Update `topic-guide.tex` if it references appendix locations

### Phase 3: Retire llm-primer.tex from appendix

1. Remove `\include{manuscript/appendix/llm-primer}` from `main.tex`
2. Content now lives in `firmware-update.tex` — not deleted, just relocated
3. Keep `science-primer-for-llms.md` as the copyable source
4. Update copy button label: "Copy Physics Reference" → **"Copy Science Reference"**
5. Delete `abstracts-compressed-pedagogy.txt`

### Phase 4: Copy Spiral Abstracts button

1. Create `spiral-abstracts-for-copy.md` from `abstracts-standalone-v9.txt` (15 abstracts only, no pedagogy)
2. Add hidden div injection in `build/preprocess.py` (parallel to primer injection)
3. Add copy button in `build/reader.js` targeting Spiral Abstracts chapter heading
4. Button label: "⎘ Copy Spiral Abstracts"
5. Top + bottom placement (matching existing pattern)

**Acceptance criteria:**
- [ ] Button appears in HTML at Spiral Abstracts chapter
- [ ] Copies clean text of all 15 abstracts to clipboard
- [ ] Works on HTTPS and HTTP (textarea fallback)
- [ ] Button styling matches existing button

### Phase 5: Full-book collapsible HTML

This is the big build system change. The entire HTML version becomes an expandable outline.

#### 5a. Post-processor: chapter-level collapse

In `build/preprocess.py`:

1. **Identify all chapter headings** in the pandoc-generated HTML (h1/h2 elements that correspond to `\chapter{}` commands)
2. **Exempt from collapse:** title page content, hook chapter ("What Would You Do?"), part headings
3. **Wrap everything else:** each chapter heading + all content until the next chapter heading → `<details class="chapter-section"><summary>[chapter title]</summary>...</details>`
4. **Default state:** all collapsed (`<details>` without `open` attribute)

#### 5b. Hover tooltips

After wrapping chapters in `<details>`, inject `title` attributes on each `<summary>` element from the mapping file `build/chapter-hover-descriptions.yaml`.

1. **Load mapping file:** Read `build/chapter-hover-descriptions.yaml` at post-processing time
2. **Match by text content:** For each `<summary>` element, look up its text content in the mapping. If found, add `title="[description]"` attribute.
3. **Coverage:** Every chapter and front/back matter section should have a hover description. The Generator writes the initial mapping file (draft descriptions in the YAML block under "Hover tooltips" in the plan design section above). Bruce refines.
4. **Spiral Abstracts internal summaries:** The 15 per-abstract `<summary>` elements also get tooltips — the abstract's paper title serves as the hover text (already in the heading, but the full title may be truncated in the summary display).

**Result:** Three layers of progressive disclosure in the collapsed view:
- **Layer 0:** Chapter title visible (zero interaction)
- **Layer 1:** Hover tooltip — one-line description (mouse hover, no click)
- **Layer 2:** Click to expand — full chapter content (one click)

#### 5c. Firmware Update: internal collapse

Within the Firmware Update chapter (already wrapped at chapter level):

1. Find "Five Physics Distinctions" sub-heading → wrap in `<details class="firmware-section">`
2. Find "Ten Physics Anchors" sub-heading → wrap in `<details class="firmware-section">`
3. Leave opening framing, Evaluation Framework, Three Possibilities, Comprehension Check, Fork, and Bibliography always visible within the chapter

#### 5d. Spiral Abstracts: per-abstract collapse

Within the Spiral Abstracts chapter (already wrapped at chapter level):

1. Find each abstract by section heading pattern: Roman numerals I through XV
2. Wrap each abstract heading + content → `<details class="spiral-abstract"><summary>[numeral + title]</summary>...</details>`
3. Add **Expand All / Collapse All** button before first abstract

#### 5e. Hash auto-expand

Inject JS (in reader.js or inline) that:
1. On page load: if `window.location.hash`, find target element, walk up DOM opening all ancestor `<details>`, scroll into view
2. On `hashchange` event: same behavior
3. This ensures TOC links, topic guide links, and all cross-references work

#### 5f. Global Expand All / Collapse All

1. Inject a floating or fixed-position button/control at top of page
2. Toggles all `<details>` elements open/closed
3. Label toggles between "Expand All" and "Collapse All"

#### 5g. CSS

```css
details.chapter-section,
details.firmware-section,
details.spiral-abstract {
  margin: 0.5em 0;
}
details.chapter-section {
  border-left: 3px solid #ddd;
  padding-left: 1em;
}
details.firmware-section,
details.spiral-abstract {
  border-left: 2px solid #ccc;
  padding-left: 0.8em;
  margin-left: 0.5em;
}
summary {
  cursor: pointer;
  font-weight: bold;
  padding: 0.3em 0;
  list-style: none;
}
summary::before { content: '▶ '; }
details[open] > summary::before { content: '▼ '; }
summary:hover { color: #2471a3; }

@media (prefers-color-scheme: dark) {
  details.chapter-section { border-left-color: #555; }
  details.firmware-section,
  details.spiral-abstract { border-left-color: #444; }
  summary:hover { color: #5dade2; }
}
```

Nested collapse gets thinner borders and slight indent — visual hierarchy.

#### 5h. Acceptance criteria

- [ ] All chapters collapsible; title block is only non-collapsible element
- [ ] Default state: everything collapsed; ~8 lines visible (title + 6 collapsed items)
- [ ] Hover tooltips on all `<summary>` elements (from YAML mapping)
- [ ] Firmware Update: 2 internal collapsible sections
- [ ] Spiral Abstracts: 15 per-abstract collapsible blocks + Expand All toggle
- [ ] Hash navigation auto-expands target chapter (and parent if nested)
- [ ] Global Expand All / Collapse All works
- [ ] TOC links work (jump + auto-expand)
- [ ] Topic guide links work (jump + auto-expand)
- [ ] Cross-reference links within chapters work
- [ ] ▶/▼ indicators on all summary elements
- [ ] Dark mode styling correct
- [ ] Copy buttons work regardless of collapse state
- [ ] PDF completely unaffected
- [ ] Graceful degradation: if `<details>` unsupported, all content visible (tooltips still work — `title` is universal HTML)

*(Phase 6 build/verify merged into new Phase 6f below.)*

---

## Architectural Note: Why This Works

The progressive JPEG is fractal. p1 → p2 → p3 is the macro pattern.

The collapsible HTML adds a new layer: **p0** — the book as skeleton. ~8 lines. The entire structure on one screen. Everything collapsed. The reader chooses what to open.

```
Relinquishment                              ← static
Bruce Stephenson · Genevieve Prentice       ← static

▶ What Would You Do?                        ← collapsed hook
▶ Front Matter                              ← collapsed
▶ Guided Deduction                          ← collapsed Part I
▶ The Evidence Trail                        ← collapsed Part II
▶ Agency And Restraint                      ← collapsed Part III
▶ Appendices                                ← collapsed (merged)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ▶ Expand All   Deduction · Evidence · Agency   ▲ Top
```

| Layer | What the reader sees | ~Words |
|-------|---------------------|--------|
| p0 | Skeleton: title + 6 collapsed lines | ~20 |
| p1 | Hook expanded: "What Would You Do?" | ~400 |
| p1.5 | Part expanded: chapter titles visible | ~50/Part |
| p2 | Summary expanded | ~4,000 |
| p3 | Any/all chapters expanded | ~80,000 |

The `<details>` element is the *mechanism* by which the progressive JPEG works in HTML. The UI embodies the book's thesis: agency over imposition. The book offers; the reader chooses.

The collapsed state of the Spiral Abstracts is itself a narrative — fifteen titles from Genesis to Guardian, the arc of the classified literature visible without expanding anything.

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Tone lands wrong | Bruce reviews framing lines before Generator writes. Iterate on opening paragraph first. |
| Moving chapters breaks cross-references | Phase 2 includes systematic \label/\hyperref audit |
| Hash auto-expand misses edge cases | Test all TOC links, all topic guide links, sample of cross-refs. Walk up DOM to handle nested `<details>`. |
| Chapter heading identification fragile | Match on text content, not HTML structure. Test after pandoc upgrades. |
| `<details>` unsupported in old browsers | Degrades to fully-visible content (same as PDF). Correct fallback. |
| JS disabled breaks navigation | `<details>` still works natively (click to expand). Only hash auto-expand and global toggle require JS. Core reading experience is JS-free. |
| Visual clutter from 30+ collapse indicators | Clean CSS, thin borders, consistent ▶/▼. The visual weight is LOW — summary lines read like a table of contents. |

---

### Phase 6: Polish pass — bug fixes, Part titles, chapter titles, merge, nav cleanup

**Status:** Ready for Generator run.
**Prerequisite commits:** Phases 1-5b all committed (latest: `9f76a04`).

#### 6a. Fix hook default state (bug from Phase 5b)

In `build/preprocess.py` (~line 367):
- Change `<details open class="hook-section">` → `<details class="hook-section">`
- Change `<summary>Relinquishment</summary>` → `<summary>What Would You Do?</summary>`
- Title block (`<div class="title-block">`) stays OUTSIDE and ABOVE the `<details>` — always visible.

#### 6b. Move Expand All button to bottom nav bar

In `build/preprocess.py`:
- Remove the `<div class="global-toggle">` injection that currently sits above the first `<details class="chapter-section">` (~line 326-338)

In `build/reader.js`:
- Add Expand All / Collapse All toggle to the sticky bottom bar (alongside Part quick-jumps and Top button)
- Label: `▶ Expand All` / `▼ Collapse All` (toggles)

**Result:** No controls between title block and first collapsed item. First-load is pure skeleton.

#### 6c. Part titles — rename

| Current | New | `main.tex` | Expected HTML ID |
|---------|-----|------------|-----------------|
| The Story | Guided Deduction | `\part{Guided Deduction}` | `guided-deduction` |
| The Investigation | The Evidence Trail | `\part{The Evidence Trail}` | `the-evidence-trail` |
| The Interpretation | Agency And Restraint | `\part{Agency And Restraint}` | `agency-and-restraint` |

Files to update:
1. `main.tex` — 3 `\part{}` commands
2. `build/preprocess.py` — ID matching set (~line 381): update `{'the-story', 'the-investigation', 'the-interpretation'}` → `{'guided-deduction', 'the-evidence-trail', 'agency-and-restraint'}`
3. `build/chapter-hover-descriptions.yaml` — Part heading keys
4. `build/reader.js` — breadcrumb + quick-jump Part links (search for "Story", "Investigation", "Interpretation")

#### 6d. Chapter title renames

Best-effort now; Gen refines later (~April 3). Each rename touches: `.tex` file (`\chapter{}`), `chapter-hover-descriptions.yaml`, and any `\addcontentsline` in the same file.

| # | Current | New | File |
|---|---------|-----|------|
| 1 | The Three Possibilities | Three Possibilities | `pos01-three-possibilities.tex` |
| 4 | The Stories | What Healer Said | `pos05-the-stories.tex` |
| 6 | Dual-Use: A Brief History of Dangerous Ideas | Dangerous Ideas | `pos08-dual-use.tex` |
| 12 | The Demo | The Demonstration | `pos11-the-demo.tex` |
| 19 | The Network | The Signatories | `pos20-the-network.tex` |
| 20 | The Three Possibilities (interlude) | Weigh the Evidence | `three-possibilities-interlude.tex` |
| 23 | Instantiation (1999) | Instantiation | `pos24-instantiation.tex` |
| 24 | The Ethical Framework | Never Again | `pos25-ethical-framework.tex` |
| 28 | Relinquishment in 2006 | Letting Go | `pos28-surrender.tex` |
| 29 | The Question | What Would You Do? | `pos35-the-question.tex` |
| 30 | Steel-Man A | The Strongest Objection | `pos36-steelman-a.tex` |

**Cross-reference audit:** After renaming, grep for old titles in all `.tex` files. Some chapters reference others by name in prose (e.g., "as we saw in The Stories"). These prose references must be updated too.

**YAML update:** Each renamed chapter needs its key updated in `chapter-hover-descriptions.yaml`. Hover descriptions stay the same unless the rename changes meaning.

#### 6e. Merge Back Matter into Appendices

In `build/preprocess.py` (~line 391-396):
1. Remove Back Matter boundary detection (lines finding `id="afterword-the-engine"`)
2. Appendices boundary (starting at `app:predictions`) extends to `</body>`, capturing all former Back Matter
3. Remove `'Back Matter'` from boundaries list

In `build/chapter-hover-descriptions.yaml`:
1. Remove "Back matter" section header
2. Move those chapter descriptions under "Appendices"

#### 6f. Rebuild and verify

1. `make html` — rebuild
2. Verify first-load view: title block + 7 collapsed lines (hook, Front Matter, 3 Parts, Appendices) — nothing else visible
3. Verify Expand All in bottom bar works
4. Verify Part quick-jumps use new names
5. Verify all internal links auto-expand
6. Verify chapter titles updated in TOC, headings, cross-references
7. `make dev` — verify PDF renders with new Part/chapter titles

#### 6g. Acceptance criteria

- [ ] First-load: ~8 lines. Title block static, everything else collapsed. No controls between title and first collapsed item.
- [ ] Hook collapsed by default, summary "What Would You Do?"
- [ ] Part titles: Guided Deduction / The Evidence Trail / Agency And Restraint
- [ ] 11 chapter titles renamed per table above
- [ ] One "Appendices" section (no separate Back Matter)
- [ ] Expand All / Collapse All in sticky bottom bar (not top)
- [ ] Bottom bar: Expand All + Part quick-jumps + Top
- [ ] All cross-references, TOC links, topic guide links still work
- [ ] Hover tooltips updated for renamed chapters
- [ ] PDF renders with all title changes
- [ ] No prose references to old chapter names remain in .tex files

---

### Phase 7: Chapter title refinement with Genevieve (~2026-04-03)

Gen reviews all 30 chapter titles as p0 narrative arc. The titles proposed in Phase 6d are Argus + Bruce best-effort; Gen has veto and counter-proposals. This is a three-person creative collaboration.

---

## Handoff Prompt — Phase 6

> You are the Generator. Read Plan 0101 at `~/software/relinquishment/plans/0101-firmware-update.md`. Execute Phase 6 (sections 6a through 6f). Phases 1-5 are already committed.
>
> **6a — Fix hook:** In `build/preprocess.py`, change `<details open class="hook-section">` to `<details class="hook-section">` and change `<summary>Relinquishment</summary>` to `<summary>What Would You Do?</summary>`. Title block stays outside/above — always visible.
>
> **6b — Move Expand All to bottom bar:** Remove the `<div class="global-toggle">` injection from `preprocess.py` (currently ~line 325-338, above first chapter). In `reader.js`, add Expand All / Collapse All toggle to the sticky bottom nav bar. No controls between title block and first collapsed item. **DEPENDENCY:** The Front Matter wrapping code (~line 419-432) uses `<div class="global-toggle">` as its anchor point (`gt_match`). When you remove the global-toggle div, you MUST update the Front Matter wrapping to use a different anchor — e.g., find the end of the hook `</details>` (hook-section) instead. The Front Matter chapters sit between the hook and the first Part.
>
> **6c — Part titles:** In `main.tex`, rename `\part{The Story}` → `\part{Guided Deduction}`, `\part{The Investigation}` → `\part{The Evidence Trail}`, `\part{The Interpretation}` → `\part{Agency And Restraint}`. Update the ID matching set in `preprocess.py` (~line 381) to `{'guided-deduction', 'the-evidence-trail', 'agency-and-restraint'}`. Update `chapter-hover-descriptions.yaml` Part keys. Update breadcrumb and quick-jump Part links in `reader.js`.
>
> **6d — Chapter title renames (11 chapters):**
> 1. `pos01-three-possibilities.tex`: "The Three Possibilities" → "Three Possibilities"
> 2. `pos05-the-stories.tex`: "The Stories" → "What Healer Said"
> 3. `pos08-dual-use.tex`: "Dual-Use: A Brief History of Dangerous Ideas" → "Dangerous Ideas"
> 4. `pos11-the-demo.tex`: "The Demo" → "The Demonstration"
> 5. `pos20-the-network.tex`: "The Network" → "The Signatories"
> 6. `three-possibilities-interlude.tex`: "The Three Possibilities" → "Weigh the Evidence"
> 7. `pos24-instantiation.tex`: "Instantiation (1999)" → "Instantiation"
> 8. `pos25-ethical-framework.tex`: "The Ethical Framework" → "Never Again"
> 9. `pos28-surrender.tex`: "Relinquishment in 2006" → "Letting Go"
> 10. `pos35-the-question.tex`: "The Question" → "What Would You Do?"
> 11. `pos36-steelman-a.tex`: "Steel-Man A" → "The Strongest Objection"
>
> For each: update `\chapter{}`, any `\addcontentsline{}` in the same file, the key in `chapter-hover-descriptions.yaml`. After all renames, grep all `.tex` files for old title strings and update prose cross-references.
>
> **6e — Merge Back Matter:** In `preprocess.py`, remove the Back Matter boundary detection (lines finding `id="afterword-the-engine"`). The Appendices boundary extends to `</body>`. In `chapter-hover-descriptions.yaml`, merge Back Matter entries under Appendices section.
>
> **6f — Rebuild and verify:** `make html`. Verify: first-load is ~8 collapsed lines + title block. Expand All in bottom bar. Part quick-jumps updated. All links auto-expand. `make dev` for PDF. Report results.
>
> **CRITICAL:** The preprocess.py ID matching set for Parts MUST match the IDs pandoc generates from the new `\part{}` text. If unsure, build first, inspect the HTML for actual IDs, then update the matching set.
