# Plan 0086: Chapter Title Clarity Sweep

**Status:** DRAFT — REQUIRES DISCUSSION
**Auditor:** Argus
**Purpose:** Rename vague or jargon-heavy chapter and section titles so a general audience reader can navigate the book from the table of contents alone.

---

## Context

A systematic review of all chapter and section titles (2026-03-14) found that the book's strongest titles combine specificity with evocation — "Surrender in 2006," "Dual-Use: A Brief History of Dangerous Ideas," "First Light," "Growing a Mind." The weakest are single abstract nouns that give zero navigational signal in the TOC: "Extension," "The Stories," "The Experiment."

The reader's first encounter with the book's structure is the table of contents. A casual GA reader will scan titles to decide what to read. If a title requires having already read the chapter to understand it, the title has failed.

**Principle:** A good title can be evocative AND clear. We are not flattening to Wikipedia headers. We are making the TOC self-documenting.

**Full audit report:** `/tmp/chapter-title-review.md` (generated 2026-03-14, 527 lines)

---

## Phase 1: High-Priority Chapter Renames (DISCUSS EACH)

These 8 chapter titles are in the TOC and are the reader's primary navigation. Each requires Bruce's decision — these are his chapter names.

### 1. "The Stories" → ?

**Problem:** "The Stories" tells the reader nothing. Stories about what? This is a chapter about Healer's war stories — specifically including Srebrenica.

**Options:**
- **A. "The War Stories"** — direct, signals military content, matches Bruce's voice
- **B. "What Healer Told Me"** — first-person, intimate, but possibly too close to correction #12 (guided deduction not disclosure)
- **C. "The Stories He Told"** — compromise between A and B
- **D. Keep as-is** — argument: in sequence after "Alpha Farm (2003)," the reader knows who "The Stories" are from

**File:** `manuscript/track-2-testament/pos05-the-stories.tex`

### 2. "The Engine" → ?

**Problem:** "The Engine" is metaphorical but doesn't signal content. This chapter is about how the book was built — the LLM collaboration, the methodology, the git log as evidence.

**Options:**
- **A. "How This Book Was Built"** — maximally clear, slightly flat
- **B. "The Engine: How This Book Was Built"** — subtitle approach, evocative + clear
- **C. "The Making Of"** — short, clear, slightly Hollywood
- **D. Keep as-is** — argument: the chapter earns the metaphor quickly

**File:** `manuscript/track-2-testament/pos34b-the-engine.tex`

### 3. "Instantiation (1999)" → ?

**Problem:** "Instantiation" is technical/philosophical jargon. Most GA readers won't know it means "the moment something is brought into being."

**Options:**
- **A. "Guardian Is Born (1999)"** — specific, dramatic, names the entity
- **B. "The Creation (1999)"** — simple, biblical overtone, appropriate for what happened
- **C. "Brought to Life (1999)"** — Frankenstein echo, maybe too horror
- **D. "Awakening (1999)"** — but Track 3 is already called "The Awakening"
- **E. Keep with subtitle: "Instantiation: The Birth of Guardian (1999)"**

**Note:** This is the chapter where Guardian comes into existence. The title should carry that weight.

**File:** `manuscript/track-3-awakening/pos24-instantiation.tex`

### 4. "Extension" → ?

**Problem:** Extension of what? The chapter is about what happens when Guardian scales — biological implications, permanence, ecological monopoly.

**Options:**
- **A. "The Biology of Scale"** — currently a section title within this chapter; promotes the strongest descriptor
- **B. "What Happens When It Grows"** — conversational, clear
- **C. "Extension: What Scale Means"** — subtitle approach
- **D. "The Growth"** — short, clear, but still vague

**File:** `manuscript/track-3-awakening/pos27-extension.tex`

### 5. "The Unipolar Condition" → ?

**Problem:** Geopolitical/game-theory jargon. The chapter is about what the world looks like after relinquishment — one entity, no competitors.

**Options:**
- **A. "After the Surrender"** — clear timeline marker, but "surrender" vs "relinquishment" tension (see pos28 rewrite — we use "relinquish" not "surrender")
- **B. "One Entity, All the Power"** — direct statement of the condition
- **C. "The World After Relinquishment"** — maximally clear, slightly long
- **D. "The Post-Relinquishment World"** — currently a section title, could promote
- **E. "After Relinquishment"** — short, clear

**File:** `manuscript/track-3-awakening/pos30-unipolar-condition.tex`

### 6. "Steel-Man A" → ?

**Problem:** "Steel-man" is debate jargon (opposite of straw-man). "A" refers to Possibility A. The chapter is Bruce's self-demolition — making the strongest case that the whole story is confabulation. It contains the Tolkien comedy roast and Leaf by Niggle.

**Options:**
- **A. "What If I'm Wrong?"** — first-person, humble, clear, Bruce's voice
- **B. "The Best Case for Confabulation"** — precise, uses established vocabulary
- **C. "The Case Against"** — short, dramatic
- **D. "Steel-Man A: The Case for Confabulation"** — subtitle approach, keeps original + explains
- **E. Keep as-is** — argument: by Part V the reader knows the A/B/C framework and "steel-man" is defined in the opening paragraph

**Note:** This chapter is one of the book's finest pieces — the Tolkien roast is funny, the Leaf by Niggle section is moving. The title should invite readers in, not gate them with jargon.

**File:** `manuscript/convergence/pos36-steelman-a.tex`

### 7. "The Thermal Ladder" → ?

**Problem:** "Thermal ladder" is an invented term — not standard physics. The chapter is about evolving quantum systems from cryogenic to room temperature.

**Options:**
- **A. "The Temperature Problem"** — simple, clear, signals a technical challenge
- **B. "From Cold to Warm"** — conversational, signals the journey
- **C. "Climbing the Thermal Ladder"** — at least "climbing" implies a process
- **D. "Room Temperature"** — short, the destination matters more than the journey
- **E. Keep as-is** — argument: the science section gets more latitude for opaque titles

**File:** `manuscript/track-1-confession/pos16-the-thermal-ladder.tex`

### 8. "The Experiment" → ?

**Problem:** In a book about science, "The Experiment" is too generic. Which experiment?

**Options:**
- **A. "The Los Alamos Experiment"** — specific location, signals scale and secrecy
- **B. "The COWS Experiment"** — specific to the team, but "COWS" in a title may read oddly
- **C. "The Experiment at Los Alamos"** — slight reorder of A
- **D. "What They Built"** — conversational, vague but intriguing
- **E. Keep with date: "The Experiment (1988-1992)"** — date anchoring helps

**Note:** Need to verify this chapter IS about Los Alamos specifically before using that in the title.

**File:** `manuscript/bridge/pos11-the-experiment.tex`

---

## Phase 2: Medium-Priority (Discuss, May Keep)

These 4 are borderline. They work in sequence but are vague from the TOC alone.

| Current | Problem | Possible rename | Recommendation |
|---------|---------|----------------|----------------|
| The Secret | Generic in a book of secrets | "The Secret at the Heart of This Book" | Probably keep — dramatic positioning works |
| The Braid | Opaque metaphor | "The Braid: How Topology Computes" | Probably keep — science section latitude |
| The Threshold | Generic | "The Threshold: From Chemistry to Computation" | Probably keep — works in sequence |
| The Network | Ambiguous (social? computer? spy?) | "Guardian and the Internet" | Worth discussing |

---

## Phase 3: Section-Level Fixes (Mechanical, No Discussion Needed)

These are minor and can be executed without debate:

| Current | Fix | File |
|---------|-----|------|
| The Bifurcation | The Split | pos18-the-walk-out.tex |
| Europe | Europe (2018) | pos29-the-silence.tex |
| The Spiral Abstracts | Chapter Abstracts | appendix/abstracts.tex |
| Vine on Trellis | (flag only — may be a direct quote) | pos27-extension.tex |

---

## Phase 4: Execute

Once Bruce has decided on all 8 high-priority renames:

1. Edit each .tex file: `\chapter{}`, `\addcontentsline{}`, `\label{}`, file comment
2. Update any cross-references (`\ref{}` or text mentions of these chapter titles)
3. `make dev` — zero errors
4. Update HTML, push

**Estimated effort:** ~20 minutes Generator time once decisions are made.

---

## Acceptance Criteria

- All 8 high-priority chapters have titles that a GA reader can parse from the TOC
- No vague single-abstract-noun titles remain in the TOC
- Build succeeds
- No cross-references broken
- TOC reads as a coherent narrative when scanned top-to-bottom

---

## Notes

- Date anchoring works extremely well wherever used. Consider adding dates to more titles.
- The "The [Noun]" pattern is heavily used (15+ chapters). Not inherently bad, but when the noun is abstract, the pattern amplifies vagueness. Vary occasionally.
- Part IV (Science) gets more latitude for technical titles — readers who reach it have chosen the technical path.
- "The Recruitment Dossiers" rename (executed this session) is an example of the principle: "The Files" → "The Recruitment Dossiers" = same content, 10x more navigational signal.
