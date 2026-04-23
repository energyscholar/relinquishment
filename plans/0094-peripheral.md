# Plan 0094: Peripheral — Relocations, Trims, Front Matter, Cuts

**Status:** DRAFT
**Auditor:** Argus, Session 43
**Parent:** Plan 0090 (Master Restructure)

---

## Scope

Everything that isn't a merge or new chapter: relocating content to appendix/afterword, trimming existing pieces, front matter consolidation, and one cut.

## Relocations

### Dossier Interlude → Appendix
- **Source:** interlude/dossier-interlude.tex (4,526w)
- **Destination:** appendix/dossier.tex
- **Rationale:** Character bios are reference material. Currently breaks flow between Parts II and III. In appendix, accessible when needed without interrupting the read.
- **Execution:** Move file, update build order, add "See Appendix: Dossiers" note at the relevant point in the narrative.

### The Engine → Afterword
- **Source:** pos34b The Engine (1,935w)
- **Destination:** 99-back/afterword.tex (new file)
- **Rationale:** Meta-commentary about building the book with AI. Valuable but not narrative, investigation, or interpretation. Perfect as afterword: "How This Book Was Made."
- **Execution:** Move file, update build order. Consider expanding slightly with Argus naming story.

## Trims

### Three Possibilities Interlude: 2,136w → ~800w
- **Location:** Between Part I and Part II
- **Current function:** Re-presents A/B/C framework after the story
- **Problem:** The reader just learned A/B/C in pos01 (655w). 2,136 words of re-grounding is too much.
- **Trim to:** Brief checkpoint (~800w) — "Now that you've heard what happened, let's revisit the three possibilities." Hit the key update (what's changed now that the reader has narrative context) and move on.

### Front Matter: ~10,500w → ~7,500w

**Move:** "The Most Important Story Never Told" summary (3,275w) → appendix. It reads as a standalone essay, not orientation. Introduction (1,409w) + hook (412w) provide sufficient entry.

**Merge:** author's note (105w) + preface (128w) + not-claimed (357w) → one piece (~400w). Three tiny items saying similar things: "here's who I am, here's what this is, here's what it isn't." One piece does all three.

**Keep unchanged:** hook, introduction, how-to-read, Gen's preface, copyright, corrections, legal note, title, cover.

## Cuts

### RLHF Bias Analysis (appendix, 1,455w)
- Cut entirely from the book
- Peripheral meta-commentary about LLM alignment bias
- Doesn't serve story, investigation, or interpretation
- Could become a blog post or separate publication

## Execution Order

1. Front matter merge (author's note + preface + not-claimed) — no dependencies
2. Move Summary to appendix — no dependencies
3. Move Dossier to appendix — no dependencies
4. Move Engine to afterword — depends on Twenty Years merge (Plan 0093) being done first, since Engine content must NOT be in the merged chapter
5. Trim Three Possibilities interlude — no dependencies
6. Cut RLHF Bias — no dependencies
7. Update build system for all moves

## Gap Risks

1. **Summary relocation:** Some readers may start with the summary. Moving it to appendix means they won't find it unless they look. Mitigation: introduction provides orientation.
2. **Dossier relocation:** Readers encountering unfamiliar names mid-book may want bios. Mitigation: brief footnotes at first mention + "See Appendix: Dossiers."
3. **Engine separation from Twenty Years:** If Engine moves to afterword, verify no narrative thread is broken. The Engine content (building with AI) should NOT overlap with Digital Doppelganger content being merged into The Question (Plan 0093).
