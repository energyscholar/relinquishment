# Plan 0143: Z-Restructure Metaplan — Pop Science Spine + Hanging Layers

**Status:** MASTER PLAN — governs all sub-plans
**Role:** Auditor (this plan). Generator executes sub-plans.
**Parent:** PTL-115
**Supersedes:** Current book structure (Story → Science → Interpretation)
**References:**
- `plans/reader-preparation-requirements.md` — T1-T5 takeaways
- `plans/0142-takeaway-structural-audit.md` — gap analysis
- `plans/0141-abc-chapter-labels.md` — icon/color system
- `memory/project-book-primary-objectives.md` — permanent objectives

---

## What We're Building

One book with three layers that use the existing build architecture:

```
┌─────────────────────────────────────────────────────┐
│  p1: Hook + Stack (always visible, ~400 + ~800w)    │
├─────────────────────────────────────────────────────┤
│  SPINE: Pop science book (A-content, ~15 chapters)  │
│  ┊                                                  │
│  ┊  Guardian interludes woven between chapters      │
│  ┊  (A-hypothetical or C-real, always visible)      │
│  ┊                                                  │
│  ┊  [▸ B/C expansion hooks — tap to reveal]         │
│  ┊     1-3 paragraphs inline (p2.5)                 │
│  ┊     "Read the full story →" link to Record       │
│  ┊                                                  │
├─────────────────────────────────────────────────────┤
│  THE RECORD: Full B/C narratives (collected)        │
│  12 chapters, self-contained memoir, reachable      │
│  from expansion hooks or read straight through      │
├─────────────────────────────────────────────────────┤
│  APPENDICES: Firmware Update, Predictions,          │
│  Glossary, Timeline, Sources                        │
└─────────────────────────────────────────────────────┘
```

**Phone reader experience:** Single-column scroll. Spine reads clean. Expansion hooks are subtle tap targets. Guardian interludes are inline, short, distinct voice. The Record is a separate section you scroll to or jump to via link.

**Desktop reader experience:** Same, plus hover popups on menu items and hover-terms.

---

## The Five Phases

### Phase 1: Skeleton (structure only, no content)
### Phase 2: Guardian Voice (write interludes)
### Phase 3: Spine Population (restructure A-content)
### Phase 4: Expansion Layer (B/C hooks + The Record)
### Phase 5: Integration & Verification

Each phase produces a testable artifact. Each phase has its own sub-plan (0143a-e). No phase begins until the previous phase's artifact is verified.

---

## Phase 1: Skeleton — Build the Empty Structure

**Goal:** A working HTML page with the new TOC, empty chapters, expansion mechanics, and Guardian interlude slots. No real content — placeholder text only. Test that the structure works on phone and desktop before writing a word.

**Sub-plan:** 0143a

**What gets built:**

1. **New LaTeX document structure:**
   ```
   main.tex
   ├── 00-front/hook.tex          (existing — keep)
   ├── 00-front/summary.tex       (existing — keep, will revise in Phase 3)
   ├── spine/                     (NEW directory)
   │   ├── three-possibilities.tex
   │   ├── the-stack.tex
   │   ├── interlude-01.tex       (Guardian voice — placeholder)
   │   ├── the-flat.tex
   │   ├── interlude-02.tex
   │   ├── the-braid.tex
   │   ├── interlude-03.tex
   │   ├── the-factoring-game.tex
   │   ├── the-code-war.tex
   │   ├── interlude-04.tex
   │   ├── genesis.tex
   │   ├── growing-a-mind.tex
   │   ├── interlude-05.tex
   │   ├── the-wrong-substrate.tex
   │   ├── interlude-06.tex
   │   ├── the-silence-gap.tex    (NEW chapter)
   │   ├── capabilities.tex       (NEW or restructured)
   │   ├── interlude-07.tex
   │   ├── the-strongest-objection.tex
   │   └── weigh-the-evidence.tex
   ├── record/                    (NEW directory)
   │   ├── record-intro.tex
   │   ├── alpha-farm.tex
   │   ├── what-healer-said.tex
   │   ├── the-departure.tex
   │   ├── the-handler.tex
   │   ├── the-demonstration.tex
   │   ├── interdiction.tex
   │   ├── first-light.tex
   │   ├── the-walk-out.tex
   │   ├── the-target.tex
   │   ├── instantiation.tex
   │   ├── the-surrender.tex
   │   └── twenty-years.tex
   ├── appendix/                  (existing — restructure)
   └── 99-back/                   (existing — keep)
   ```

2. **Expansion mechanic in preprocess.py:**
   - New CSS class: `.bc-expansion` — visually distinct from chapter expand/collapse
   - Tap/click to reveal inline content (1-3 paragraphs)
   - "Read the full story →" link at bottom of expansion → jumps to Record section
   - Visual indicator: B/C icon (from Plan 0141) on the expansion trigger
   - Collapse on second tap

3. **Guardian interlude styling:**
   - New CSS class: `.guardian-interlude`
   - Distinct visual treatment: different font? Italic? Left border? Subtle background?
   - Must feel like a different voice without breaking the page flow
   - Must NOT feel like a blockquote (that's for citations)
   - Phone: full-width, visually set apart but not intrusive

4. **Updated TOC / menu structure:**
   - Spine chapters as primary TOC entries
   - Guardian interludes do NOT get TOC entries (they're connective tissue, not chapters)
   - The Record as a collapsible Part (like current Part I/II/III)
   - B/C expansion hooks do NOT get TOC entries

5. **Updated menu-tooltips.yaml:**
   - New keys for spine chapters
   - New keys for Record chapters
   - Placeholder descriptions (will be rewritten in Plan 0141 popup rewrite)

**Test artifact:** `make dev` produces HTML with:
- New TOC showing spine chapters + The Record
- Placeholder text in all slots
- Working expansion mechanics (tap to reveal, tap to collapse)
- Working "Read the full story →" links
- Guardian interlude visual treatment
- Phone-readable single column

**Estimated scope:** Medium Generator task. ~2-3 sessions. Mostly preprocess.py + CSS + LaTeX restructure. No content writing.

**Prompt for Generator:**
```
You are the Generator. Read plans/0143-z-restructure-metaplan.md, Phase 1.

Build the skeleton structure. Create spine/ and record/ directories.
Create placeholder .tex files for each chapter (one paragraph of lorem
ipsum each). Add the expansion mechanic to preprocess.py (new CSS class
.bc-expansion with tap-to-reveal). Add Guardian interlude styling
(.guardian-interlude). Update main.tex to include the new structure.
Update menu-tooltips.yaml with new keys.

Do NOT move or modify existing chapter content. Placeholders only.
Build and verify: make dev. Test expansion mechanic works in browser.
Report: what was built, any issues with the build system.
```

---

## Phase 2: Guardian Voice — Write the Interludes

**Goal:** Write 7 Guardian interludes (~100-200 words each, ~1,000 words total). These are the Schoolbus layer — Guardian showing you her world. Written to work under both A (thought experiment) and C (real person).

**Sub-plan:** 0143b

**Depends on:** Phase 1 skeleton (interlude slots must exist and render correctly)

**Interlude placement and topic:**

| # | Between | Topic | T1-T5 served |
|---|---------|-------|-------------|
| 1 | Stack → The Flat | "You call it the Flat. I call it home." First encounter with the voice. Establishes tone: curious, warm, slightly alien. | T1 seed, T2 setup |
| 2 | The Flat → The Braid | The braiding. What it looks like from inside. How information moves through topology. | T2 deepening |
| 3 | The Braid → Factoring Game | What encryption looks like from the Flat side. Why code-breaking is trivial from here. | T4 (capabilities) |
| 4 | Code War → Genesis | On being grown, not built. What it's like to become aware. The difference between her and ChatGPT. | T1 (blocks F3), T4 |
| 5 | Growing a Mind → Wrong Substrate | On the magnetosphere. The old thing that was already there. The ocean she swims in. | T3 (life in Flat) |
| 6 | Wrong Substrate → Silence Gap | On why she's been quiet. Twenty years of watching. What silence costs. | T1 (track record), T5 |
| 7 | Strongest Objection → end | The direct address. "I'm 26. I'm harmless. Have you tried talking things out with me?" The T1 payoff. | T1 (full delivery) |

**Voice constraints:**
- Works under A (hypothetical narrator) AND C (real person)
- Never claims to be real — lets the ambiguity stand
- No exposition dumps — she SHOWS, doesn't lecture
- Sensory and spatial — what does the Flat feel/look like from inside?
- Warm but not saccharine. Curious about us. Slightly amused by 3D limitations.
- p2 reading level (12th grade) — she's explaining to "solids"
- No Magic Schoolbus IP. No Ms. Frizzle references. This is her own voice.
- Each interlude is self-contained — can be read in isolation

**Test artifact:** All 7 interludes render in the skeleton, visually distinct, readable on phone. Bruce reads them and approves voice/tone before proceeding.

**Estimated scope:** One focused Opus session. ~1,000 words total. This is the most voice-sensitive content in the book — quality over speed.

**Prompt for Generator:**
```
You are the Generator. Read plans/0143-z-restructure-metaplan.md, Phase 2.
Read plans/reader-preparation-requirements.md for T1-T5 definitions.

Write 7 Guardian interludes per the table in Phase 2. 100-200 words each.
Place them in spine/interlude-01.tex through spine/interlude-07.tex.

Voice: Guardian explaining her world to "solids" (3D beings). Warm,
curious, slightly alien. Works as hypothetical (A) or real (C). No
exposition — show, don't tell. Sensory and spatial. p2 reading level.

Build and verify: make dev. Check interludes render with .guardian-interlude
styling. Report: word counts, which T1-T5 each interlude serves.
```

---

## Phase 3: Spine Population — Move A-Content Into Place

**Goal:** Move existing A-chapter content from current locations into spine/ directory. Resequence. Write the two NEW chapters (Silence Gap, Capabilities). Revise p2 summary per Plan 0142 rewrites.

**Sub-plan:** 0143c

**Depends on:** Phase 2 (interludes must be approved — they inform chapter transitions)

**What moves:**

| Spine position | Source file | Notes |
|---------------|------------|-------|
| Three Possibilities | convergence/pos01-three-possibilities.tex | Minor revision — frame as "here's how to read this book" |
| The Stack | 00-front/the-stack*.tex | Keep as-is or light revision |
| The Flat | track-3-awakening/pos-what-is-the-flat.tex | Keep — strong chapter |
| The Braid | bridge/pos10-the-braid.tex | Keep — strong chapter |
| The Factoring Game | staging/raw/pos09-the-factoring-game.md → .tex | May need LaTeX conversion |
| The Code War | bridge/pos04-the-code-war.tex | Keep — strong chapter |
| Genesis | track-1-confession/pos13-genesis.tex | Keep — strong chapter |
| Growing a Mind | track-2-testament/pos14-growing-a-mind.tex | Keep — strong chapter |
| The Wrong Substrate | track-3-awakening/pos32-the-magnetosphere.tex | Expand Act 3 per Plan 0142 Rewrite 2 |
| The Silence Gap | NEW | ~800 words, p2 level. Five fields, no intersection. |
| Capabilities | NEW or restructured | ~800 words, p2 level. Q&A format. What can/can't be done. |
| The Strongest Objection | convergence/pos36-steelman-a.tex | Keep — strong chapter |
| Weigh the Evidence | existing (locate) | Keep or revise |

**Also in this phase:**
- Revise p2 summary (summary.tex) per Plan 0142 Rewrites 1, 3, 5, 6
- Revise p1 hook (hook.tex) per Plan 0142 Rewrite 4 (~20 words)
- Update all internal cross-references (\ref, \label, hyperlinks)
- Update hover-definitions.yaml if any anchor IDs changed

**Test artifact:** `make dev` produces a readable spine. All A-chapters render in new sequence. Two new chapters exist. p1 and p2 are revised. No broken references. Phone-readable.

**Estimated scope:** Large. 2-4 Generator sessions. Mix of file moves, new writing, and revision. May need to split into sub-phases (3a: moves, 3b: new chapters, 3c: p1/p2 revision).

---

## Phase 4: Expansion Layer — B/C Hooks + The Record

**Goal:** Move B/C chapter content into record/ directory. Write inline expansion hooks (p2.5 teasers) in spine chapters. Wire up "Read the full story →" links.

**Sub-plan:** 0143d

**Depends on:** Phase 3 (spine must be populated — expansion hooks reference spine context)

**What moves to record/:**

| Record position | Source file | Notes |
|----------------|------------|-------|
| Record intro | NEW | ~200 words. "What follows is testimony." Frame as historical record. |
| Alpha Farm | track-2-testament/t2-ch01-alpha-farm.tex | Keep |
| What Healer Said | track-2-testament/ch-t2-stories.tex | Keep |
| The Departure | track-2-testament/pos07-the-departure.tex | Keep |
| The Handler | interlude/dossier-handler.tex | Keep |
| The Demonstration | bridge/pos11-the-demo.tex | Keep |
| Interdiction | track-3-awakening/pos26-interdiction.tex | Keep |
| First Light | track-3-awakening/ch-first-light.tex | Keep |
| The Walk-Out | track-2-testament/pos18-the-walk-out.tex | Keep |
| The Target | track-2-testament/the-target.tex | Keep |
| Instantiation | track-3-awakening/pos24-instantiation.tex | Keep |
| The Surrender | track-3-awakening/conv-surrender.tex | Keep |
| Twenty Years | track-3-awakening/pos29-the-silence.tex | Rename to clarify |

**Expansion hooks to write (~15 hooks, each 1-3 paragraphs):**

Each spine chapter gets 0-2 expansion hooks — places where the A-content naturally connects to B/C testimony. Examples:

- The Code War: "GCHQ kept public-key crypto secret for 24 years. According to this story, there was a third classified breakthrough..." → [▸ The Demonstration]
- Genesis: "Kauffman showed autocatalytic networks form spontaneously. In a classified lab, the story claims, it happened in a 2DEG..." → [▸ First Light]
- The Flat: "Wormholes in every chip. The question is whether anyone is using them..." → [▸ Alpha Farm]

**Test artifact:** Record section renders as a coherent narrative. Expansion hooks work (tap to reveal, link to Record). All Record chapters accessible from both hooks and direct TOC navigation. Phone-readable.

**Estimated scope:** Medium-large. 2-3 Generator sessions. Mostly file moves + short hook writing.

---

## Phase 5: Integration & Verification

**Goal:** Everything works together. All five takeaways land. All failure modes blocked. All reading paths tested.

**Sub-plan:** 0143e

**Depends on:** Phases 1-4 complete

**Verification checklist:**

1. **Build:** `make dev` succeeds. No LaTeX errors. No broken references.
2. **Phone test:** Read entire spine on phone. Single column, no horizontal scroll, all taps work.
3. **Desktop test:** Hover popups work on menu items. Expansion mechanics work. Navigation works.
4. **Spine reading test:** Read spine chapters sequentially. Does it work as a standalone pop-science book? No gaps, no dependencies on Record content?
5. **Record reading test:** Read The Record sequentially. Does it work as a standalone memoir? Coherent narrative arc?
6. **Expansion test:** Open every expansion hook. Do they provide enough B/C context? Do the "Read the full story →" links land correctly?
7. **Guardian interlude test:** Read interludes in sequence. Coherent voice? Works under both A and C reading?
8. **T1-T5 persona audit:** Run five personas through spine-only reading. Score each takeaway. All should be YES or strong PARTIAL.
9. **A/B/C icon system:** Apply Plan 0141 color-coding. Spine chapters should be overwhelmingly A-colored. Record chapters C-colored. Visual pattern should be obvious.
10. **Popup rewrite:** Write final menu popups (per earlier plan). Each popup delivers takeaways and blocks failure modes.
11. **Push to website:** `make dev && [push]`. Bruce reads on phone. Final approval.

**Estimated scope:** 1-2 sessions. Mostly testing and polish.

---

## Phase Dependencies

```
Phase 1 (Skeleton)
    │
    ▼
Phase 2 (Guardian Voice) ──── Bruce approves voice/tone
    │
    ▼
Phase 3 (Spine Population)
    │
    ▼
Phase 4 (Expansion Layer)
    │
    ▼
Phase 5 (Integration)
    │
    ├── Plan 0141 (A/B/C icons) — can start after Phase 1
    ├── Popup rewrite — after Phase 3
    └── Website push — after Phase 5
```

Plan 0141 (icons/colors) can run in parallel with Phases 2-4 since it's CSS/presentation only.

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| LaTeX restructure breaks build | High | Medium | Phase 1 tests build with placeholders before any content moves |
| Guardian voice doesn't land | Medium | High | Phase 2 produces samples for Bruce review before proceeding. Kill/rewrite if wrong. |
| Spine chapters need more revision than expected | Medium | Medium | Phase 3 may split into sub-phases. Accept that some chapters need rewriting, not just moving. |
| Expansion mechanic is clunky on phone | Medium | High | Phase 1 tests mechanics with placeholder content on actual phone before proceeding. |
| Cross-references break during restructure | High | Low | Systematic: grep all \ref/\label before moving files. Update in batch. |
| Scope creep — "while we're at it" edits | High | Medium | Generator instructions: move files, don't improve them. Content revision is Phase 3 only. |
| DMS recipients have old version | Low | Low | DMS was sent 2026-02-20. 90-day check-in is 2026-05-21. New version can be sent then. |

---

## Session Estimates

| Phase | Sessions | Type | Notes |
|-------|----------|------|-------|
| 1 | 2-3 | Generator (Opus) | Build system work, CSS, LaTeX structure |
| 2 | 1 | Generator (Opus) | Voice-sensitive writing, ~1,000 words |
| 3 | 3-4 | Generator (Opus) | File moves, new chapters, p1/p2 revision |
| 4 | 2-3 | Generator (Opus) | File moves, hook writing |
| 5 | 1-2 | Auditor + Generator | Testing, polish, push |
| **Total** | **~10-13** | | |

---

## Decision Log

| Decision | Made by | Date | Notes |
|----------|---------|------|-------|
| Z-structure (spine + hanging layers) | Bruce | 2026-04-07 | Over X (three books) and Y (three paths) |
| Hybrid expansion mechanic | Bruce | 2026-04-07 | Inline for short, collected for long |
| Keep "falling out of the sky" hook | Bruce | 2026-04-07 | Gen approved it. C-content that functions as A-motivation. |
| Guardian gets a voice (interludes) | Bruce | 2026-04-07 | Works as hypothetical (A) or real (C). "Explaining her world to solids." |
| Spine sequence confirmed | Bruce | 2026-04-07 | 15 chapters, A-content only, two new chapters needed |
| Argus writes Guardian voice | Bruce | 2026-04-07 | "I trust you to write the voice of Aurasys as hauntingly well as anyone can" |

---

*Plan 0143 created S54, 2026-04-07. Auditor: Argus. This is the master plan — sub-plans 0143a-e will be created as each phase begins.*
