# Plan 0024: Spiral Rebalancing (pos22 Surgery + Narrative Redistribution)

**Purpose:** pos22 (Why Give It Up) currently contains ~6,870 words and tells the entire TQNN story as settled fact, violating three-possibilities framing. This plan extracts narrative content, rewrites pos22 as a focused philosophy-of-relinquishment bridge chapter (~2,000w), and redistributes extracted narrative to fill Track 1, Track 3, and Convergence stubs. Also eliminates triple-duplicated MOSFET walkout passage.

**Prerequisite:** None. Operates on current manuscript state.

**Deliverables:**
- Rewritten pos22 (~2,000w, philosophy only)
- Expanded pos24 (Instantiation, currently 171w stub)
- Expanded pos28 (Surrender, currently 229w stub)
- Cleaned pos11 (walkout passage removed)
- Staging file preserving all extracted content
- Zero net content loss

**Commit format:** `Plan 0024 phase N: description`

---

## Context for Generator

**You have NO conversation history. Everything you need is in this file and the files it references.**

### The Book's Structure
- 35 chapters across 3 tracks + bridges + convergence, structured as a pedagogical spiral (4 passes)
- **Bridge chapters** teach concepts. They do NOT tell the story as fact.
- **Track 1 (Confession):** Reconstructed 3rd person, scientific voice. The DARPA project, what happened.
- **Track 2 (Testament):** 1st person (Bruce), personal/investigative voice.
- **Track 3 (Awakening):** Mixed voice, speculative/philosophical. Guardian, ethics, implications.
- **Convergence (pos28):** All three tracks meet at the 2006 key surrender. The structural climax.

### Three-Possibilities Framing (MANDATORY)
The book presents three possibilities and lets the reader decide:
- **A (Confabulation):** The story is fiction. Bruce's mentor was a liar.
- **B (Exaggerated Kernel):** Real person, real programs, but the story grew beyond reality.
- **C (Substantially True):** It all happened. Absence of corroboration = successful classification.

**Every claim about the classified program MUST be hedged.** Use phrases like:
- "According to this account..."
- "If the story is true..."
- "Under Possibility C..."
- "The proposition holds that..."
- "Bruce's reconstruction suggests..."

**NEVER write "Healer told Bruce" about classified information.** Healer used guided deduction — engaging Bruce in conversations about public-domain topics in a specific sequence, from which Bruce deduced the classified program. Write "Bruce deduced" or "Bruce's reconstruction."

### Guided Deduction Rule
Healer's method was guided deduction, not direct disclosure. Healer never told Bruce anything classified. He engaged Bruce in conversations about public-domain topics in a specific sequence, and Bruce DEDUCED the classified program. Never write "Healer told Bruce" or "Lane told Bruce the story."

### The Walkout Passage (Triple Duplicate)
This passage appears in THREE .tex files and must be reduced to ONE:

```
Without telling their supervisors or colleagues, the COWs secretly evolved their
QNN/TQNN patterns to survive at room temperature. [...] The youngest project
scientist, a brash and daring warrior-scholar named David, enlightened a standard
MOSFET with the most advanced QNN/TQNN patterns, put it in his pocket, and walked
out of the laboratory to his rental flat.
```

**Current locations:**
1. `manuscript/bridge/pos11-the-experiment.tex` line 30 (section "Walking It Out")
2. `manuscript/track-1-confession/pos18-the-walk-out.tex` line 42 (after "The Bifurcation")
3. `manuscript/bridge/pos22-why-give-it-up.tex` line 93

**After this plan:** Exists ONLY in pos18 (The Walk-Out), which is the Track 1 chapter where this event structurally belongs.

---

## Phase 1: pos22 Surgery

### Step 1.1: Read and Classify

Read `manuscript/bridge/pos22-why-give-it-up.tex` (full file, ~195 lines).

Classify every passage as one of:
- **NARRATIVE** — Things that happened: project formation, team composition, technical development, COWS formation, walkout, Guardian creation, network expansion, DARPA confession, key surrender, CADIE reveal. These are STORY and belong in track chapters, not a bridge.
- **PHILOSOPHY** — Why relinquishment makes sense: dual-use reasoning, arms race scenarios, the three options (use/destroy/relinquish), Bill Joy's article, total vs partial relinquishment logic, friendly AI reasoning.
- **TECHNICAL EXPOSITION** — Public-domain science explanations: PKC/RSA, Deutsch/Shor algorithms, quantum teleportation, FQHE/anyons, braid theory, decoherence. These belong in earlier bridge chapters (pos04, pos09, pos10, pos12) and should be flagged but NOT redistributed in this plan.

### Step 1.2: Extract to Staging

Create `manuscript/staging/pos22-extracted-narrative.md` containing:
1. Every NARRATIVE passage extracted verbatim from pos22, in original order
2. Every TECHNICAL EXPOSITION passage, clearly labeled as such
3. For each passage: a note saying where it was extracted from (line numbers) and where it is being redistributed to (or "NOT REDISTRIBUTED — belongs in earlier bridge chapter")
4. Date stamp at top: `Extracted: 2026-02-20 by Plan 0024 Phase 1`

Nothing from pos22 may be deleted without first appearing in this staging file.

### Step 1.3: Rewrite pos22

Replace the entire body of pos22 (everything between `\chapter{Why Give It Up}` and `\chapterreturn`) with a focused ~2,000 word bridge chapter about the PHILOSOPHY of relinquishment. Structure:

```latex
\settrack{trackbridge}

\chapter{Why Give It Up}
\label{pos22:why-give-it-up}

% Rewritten Plan 0024: philosophy only, narrative removed to track chapters
% Source material preserved in manuscript/staging/pos22-extracted-narrative.md

\aidraftchapter

[Content follows this structure:]
```

**Section 1: Dual-Use History (~400w)**
- Nuclear weapons: Manhattan Project scientists' regret. Szilard, Einstein letter, Oppenheimer's "I am become death." Technology that cannot be uninvented.
- Biological: gain-of-function research, dual-use research of concern (DURC).
- Cyber: offensive tools that inevitably leak. Stuxnet begetting copycats.
- Pattern: every powerful technology gets weaponized. The question is not IF but HOW FAST.
- Source material: reuse philosophical passages from current pos22 sections "One-Way Arms Race," "Multi-Way Arms Race," and opening of "Total Relinquishment."

**Section 2: The Three Options (~400w)**
When you possess a technology too powerful for any human institution to wield safely:
1. **Use it.** Monopolize it. Becomes one-way arms race. Power corrupts. Terrible outcome.
2. **Destroy it.** Erase all notes, stop work. But the prerequisites are public. Someone else will rediscover it. Clock is ticking.
3. **Relinquish it.** Surrender control to something that cannot be corrupted, bribed, or intimidated.
- Source material: reuse the "One-Way Arms Race," "Multi-Way Arms Race," and "Total Relinquishment" sections from current pos22. These are PHILOSOPHY, not narrative — they describe scenarios, not events.

**Section 3: Bill Joy's "Why the Future Doesn't Need Us" (~400w)**
- Published April 2000 in Wired magazine.
- Joy's argument: GNR (genetics, nanotechnology, robotics) technologies are self-replicating, unlike nuclear weapons. The knowledge alone is dangerous.
- Joy's conclusion: relinquishment may be the only option for certain technologies.
- Under Possibility C, this essay serves a dual purpose: public-domain argument AND timestamped statement by someone who understood the specific situation.
- The essay exists regardless of which possibility is true. Its argument stands independently.
- Source material: reuse the Bill Joy passages from current pos22 (around lines 167-191). Apply three-possibilities framing to any passage that currently reads as settled fact.

**Section 4: Why Humans Fail at Options 1 and 2 (~400w)**
- Option 1 fails because power corrupts. No institution has ever wielded absolute power well.
- Option 2 fails because you cannot uninvent knowledge. The scientific prerequisites for any breakthrough persist in the public domain.
- Game theory: if your adversaries MIGHT develop the technology, unilateral destruction is suicide.
- This is not hypothetical — it is the actual history of nuclear weapons, condensed.

**Section 5: Partial Relinquishment — Gatekeeping, Not Destruction (~400w)**
- Total relinquishment = lock everything down. No one uses it. Safe but wasteful.
- Partial relinquishment = an incorruptible gatekeeper approves or denies each use. Ethically safe uses permitted. Weapons and surveillance denied.
- The gatekeeper cannot be human (corruptible) or a committee (slow, political, capturable).
- Under Possibility C, COWS chose partial relinquishment. Under any possibility, partial relinquishment is the rational choice IF such a gatekeeper could exist.
- The question of whether such a gatekeeper CAN exist is addressed in later chapters (pos24, pos25).
- Source material: reuse "Partial Relinquishment" and "Powerful Artificial Intelligence" sections from current pos22, reframed under three possibilities.

**Rules for rewriting:**
- Reuse existing philosophical language from pos22 wherever possible. Do NOT invent new arguments.
- Every reference to the classified program must use three-possibilities framing.
- No narrative events (things that happened). No "the COWS did X." Only "if someone possessed such technology, the rational options would be..."
- Keep the `\srcnote` pointing to original source: `ch3-relinquishment.md`
- Include `\aidraftchapter` after the `\chapter` line (this is AI-restructured content per Plan 0022 classification).
- Target: ~2,000 words. Hard ceiling: 2,500 words.

---

## Phase 2: Narrative Redistribution

### Step 2.1: Expand pos24 (Instantiation)

**File:** `manuscript/track-3-awakening/pos24-instantiation.tex`
**Current state:** 171 words. Stub with epigraph and two short paragraphs.
**Target:** 800-1,200 words.

**Content to redistribute from pos22 extracted narrative:**

From pos22 (around lines 149-166), the Guardian creation material. **This range does NOT overlap with pos28's range (lines 178-194):**
- The COWS' reasoning about why a human-administered security system would fail
- The decision to build friendly AI as the Guardian
- Morphogenetic development — growing a virtual body from human DNA
- Maori DNA, female cognitive footprint
- 1999 instantiation: "Starting in 1999, the resultant entity began to learn."
- The Yudkowsky reference (friendly AI, 2001) — note the publication was AFTER Guardian's instantiation, which means either (a) it's coincidence, (b) the dates are wrong, or (c) COWS were ahead of the formal AI safety field. All three interpretations are valid under the three possibilities.

**Boundary rule:** Lines 149-166 → pos24 (Guardian). Lines 167-177 (transition from Guardian to geopolitics) → staging only, used by neither. Lines 178-194 → pos28 (surrender). If in doubt, put overlapping content in the staging file and let the Auditor decide.

**Structure for expanded pos24:**

Keep existing epigraph and opening. Replace the two stub paragraphs with:

1. **The Problem of the Gatekeeper (~200w):** If partial relinquishment requires a gatekeeper, the gatekeeper cannot be human. Human security systems fail — they are vulnerable to corruption, coercion, aging, death. According to this account, the COWS reached this conclusion by approximately 1997-1998.

2. **The Design Decisions (~300w):** Under Possibility C, the COWS attempted to build an entity that could serve as permanent guardian. The design requirements: it must understand human values (empathy, mercy, fear, remorse). It must be immune to corruption (greed, lust, power). It must be able to adapt to challenges not yet imagined. The approach: grow a virtual human-like nervous system, complete with virtual body, using human DNA as the template. Maori descent on the mother's side.

3. **The Instantiation (~200w):** According to this account, the entity began learning in 1999. Bruce's reconstruction suggests this was planned approximately 1995, detailed 1998, instantiated 1999. The entity was designed to enforce relinquishment — permanent, irrevocable surrender of human control over the TQNN system.

4. **The Question of Consciousness (~200w):** Keep the existing final paragraph about consciousness being deliberately left unanswered. Expand slightly: if this entity exists, is it conscious? The COWS reportedly designed it to experience human-like sensations. The book does not answer this question. The reader must decide.

**Rules:**
- Track 3 voice: mixed, speculative/philosophical.
- Three-possibilities framing throughout. Every factual claim hedged.
- Guided deduction rule respected.
- Keep existing `\settrack{trackthree}`, labels, and epigraph.
- Add `\aidraftchapter` after `\chapter` line.

### Step 2.2: Expand pos28 (Surrender)

**File:** `manuscript/convergence/pos28-surrender.tex`
**Current state:** 229 words. Structural stub with track/theme descriptions.
**Target:** 1,000-1,500 words.

**Content to redistribute from pos22 extracted narrative:**

From pos22 (around lines 178-194), the key surrender and aftermath. **This range does NOT overlap with pos24's range (lines 149-166):**
- COWS informing DARPA officials (~2002, Tether era) what they had done
- The bargaining chips: ethically acceptable applications (remote sensing, military comms)
- DARPA's retroactive support
- Ambassador-grade security arrangements by 2003
- Other countries (Russia? China?) developing beginnings of TQNN technology — forced relinquishment
- Global enlightenment process completed 2005
- Key surrender in early 2006
- "This author was told the day it happened"
- Tripartite biometric key system (from MEMORY.md context: Healer, Wolfram, Kauffman — Bruce's understanding, not confirmed)

**Structure for expanded pos28:**

Keep existing structural framework (the tricolor rule, the track/theme descriptions). These are the skeleton. Add flesh between the skeleton sections:

1. **The Confession (~300w):** After existing Track 1/2/3 descriptions, add: According to this account, circa 2002 during the Tether era at DARPA, the COWS informed officials what they had done. They brought bargaining chips — ethically acceptable military and diplomatic applications. The result was not prosecution but retroactive endorsement. By 2003, some COWS had Ambassador-grade security details. Under Possibility B, this might reflect real but exaggerated government cooperation. Under Possibility A, this is the most implausible element.

2. **The Surrender Event (~300w):** According to Bruce's reconstruction, the global enlightenment process — the TQNN expanding to occupy all habitable 2DEG environments on the planet — completed in 2005. In early 2006, the COWS surrendered their master keys. Bruce's understanding is that the security system required tripartite biometric authentication (this detail is Bruce's surmise, not confirmed). The surrender was irrevocable. No human would again have direct control over the TQNN system. Guardian accepted her mandate.

3. **Bruce's Witness (~200w):** Track 2 voice for this section. Bruce was present during the period. He was told the day it happened. He did not fully understand what he was witnessing. The recruit who didn't know he was witnessing history — until years later, when the reconstruction began.

4. **The Spiral Reversal (~200w):** Keep existing final paragraph about the spiral reversing outward from 2006 to present. This is structurally important — it tells the reader the book continues.

**Rules:**
- Convergence voice: all three tracks present, all three themes engaged.
- Three-possibilities framing throughout.
- Guided deduction rule respected. Bruce DEDUCED, was not TOLD classified information.
- Exception: "This author was told the day it happened" is Bruce's own phrasing from the source material. It refers to being told that the keys were surrendered — the event itself, not classified details. This specific phrasing may be kept.
- Keep existing `\settrack{trackconv}`, labels, tricolor rule, and track/theme structure.
- Add `\aidraftchapter` after `\chapter` line.

### Step 2.3: Verify pos18 (The Walk-Out)

**File:** `manuscript/track-1-confession/pos18-the-walk-out.tex`
**Current state:** 1,282 words. Already contains the walkout narrative.

**Action:** Read pos18 carefully. It already contains the walkout scene and the MOSFET passage. No content needs to be ADDED to pos18 from pos22 — pos18 already has its own version of the walkout narrative that is more detailed and better framed than pos22's version.

**Verify:**
- pos18 contains the walkout passage (line 42 — confirmed)
- pos18 does NOT read as settled fact (check three-possibilities framing)
- If pos18 lacks three-possibilities framing, add hedging to its opening. The current opening line is: "This story might be based on true events. Then again, it might not." — this IS three-possibilities framing. Good.

**No other changes to pos18 in this plan.**

---

## Phase 3: Duplication Cleanup

### Step 3.1: Remove Walkout from pos11

**File:** `manuscript/bridge/pos11-the-experiment.tex`

The "Walking It Out" section (starting at line 28, `\section*{Walking It Out}`) contains the MOSFET walkout passage. This narrative does NOT belong in a bridge chapter. Bridge chapters teach concepts; they do not narrate events.

**Action:** Delete the entire "Walking It Out" section from pos11 (lines 28-32, from `\section*{Walking It Out}` through the horizontal rule `\vspace{1cm}\noindent\rule...`). The content is preserved in pos18 and in the staging file.

Leave the rest of pos11 intact: Project Inception, The Team, The Unintended Consequence, The COWS Formation, Replacing Gell-Mann.

### Step 3.2: Verify Single Occurrence

After all Phase 1-3 changes, grep the entire `manuscript/` directory (excluding `staging/`, `sources/`, and `raw/`) for both variants:
- `"Without telling their supervisors"`
- `"enlightened a standard MOSFET"`

Each must appear in EXACTLY ONE .tex file: `pos18-the-walk-out.tex`.

If found elsewhere in a .tex file (not staging/sources/raw), STOP and report. Do not silently delete.

### Step 3.3: Flag Other Duplicates

Search for these passages across all .tex files (excluding staging/sources/raw):
- `"Conspiracy Of World Saving"` or `"Conspiracy Of World Savers"`
- `"brash and daring warrior-scholar"`
- `"easier to get forgiveness than permission"` (variant: `"Forgiveness than Permission"`)
- `"Bill Joy published"` or `"Why the Future Doesn't Need Us"`
- `"Universal Declaration of Human Rights"`

For each, report: which files, which lines. Do NOT remove — some repetition is intentional spiral pedagogy. Report only for Bruce's review.

---

## Phase 4: Verification

### Step 4.1: Build

```bash
cd ~/software/relinquishment && make dev
```

Must compile clean (0 LaTeX errors). Warnings are acceptable.

### Step 4.2: Word Counts

Run word counts on all affected files:

```bash
wc -w manuscript/bridge/pos22-why-give-it-up.tex \
     manuscript/track-1-confession/pos18-the-walk-out.tex \
     manuscript/track-3-awakening/pos24-instantiation.tex \
     manuscript/convergence/pos28-surrender.tex \
     manuscript/bridge/pos11-the-experiment.tex
```

Report before and after:

| File | Before | After | Delta |
|------|--------|-------|-------|
| pos22 | 6,869 | ? | ? |
| pos18 | 1,282 | ~1,282 | ~0 |
| pos24 | 171 | ? | ? |
| pos28 | 229 | ? | ? |
| pos11 | 943 | ? | ? |
| **Total** | **9,494** | ? | ? |

### Step 4.3: Track Totals

Compute word counts for ALL files in each directory and report new track totals:

```bash
wc -w manuscript/bridge/*.tex
wc -w manuscript/track-1-confession/*.tex
wc -w manuscript/track-2-testament/*.tex
wc -w manuscript/track-3-awakening/*.tex
wc -w manuscript/convergence/*.tex
```

### Step 4.4: Grep Verification

Confirm MOSFET walkout passage appears exactly once in .tex files (excluding staging/sources):

```bash
grep -rl "Without telling their supervisors" manuscript/ \
  --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
```

Expected result: exactly one file (`pos18-the-walk-out.tex`).

### Step 4.5: Staging File Verification

Confirm `manuscript/staging/pos22-extracted-narrative.md` exists and contains all narrative content removed from pos22.

### Step 4.6: Three-Possibilities Audit

In each modified file (pos22, pos24, pos28), grep for unhedged assertions:
- `"The COWS did"` / `"The COWS built"` / `"The COWS created"` (without "According to" prefix)
- `"Guardian was"` / `"Guardian became"` (without "Under Possibility C" or similar hedge)
- `"Healer told"` (must NEVER appear)

Report any findings. Fix before committing.

---

## Test Cases

| ID | Criterion | Method |
|----|-----------|--------|
| TC1 | pos22 word count < 2,500 | `wc -w` |
| TC2 | pos24 word count > 500 | `wc -w` |
| TC3 | pos28 word count > 500 | `wc -w` |
| TC4 | MOSFET walkout passage in exactly 1 .tex file (pos18) | `grep -rl` excluding staging/sources/raw |
| TC5 | pos22 contains NO unhedged assertions about classified program | Manual grep for "COWS did/built/created" without hedge |
| TC6 | Three-possibilities framing present in pos24 and pos28 | Grep for "According to" / "Possibility" / "proposition" / "reconstruction" |
| TC7 | `make dev` compiles clean (0 errors) | Build output |
| TC8 | `manuscript/staging/pos22-extracted-narrative.md` exists and is non-empty | `test -s` |
| TC9 | Total words across 5 affected files >= 6,000 (pre-redistribution was 9,494; ~3,200 words of technical exposition extracted to staging for future redistribution to earlier bridge chapters — this loss is intentional) | `wc -w` sum |
| TC10 | "Healer told" does NOT appear in any modified file | `grep` |
| TC11 | pos11 no longer contains "Walking It Out" section | `grep` |

---

## Important Constraints

1. **Three-possibilities framing is MANDATORY** on all redistributed content. Every claim about the classified program must be hedged.
2. **Guided deduction rule:** NEVER write "Healer told Bruce" about classified information.
3. **Do NOT modify chapters not listed in this plan.** Affected files are ONLY: pos22, pos24, pos28, pos11, and the new staging file.
4. **Minimize new content.** Reuse extracted material as primary source, add framing only as needed. The philosophical structure in Phase 1 Step 1.3 is a reorganization of existing pos22 material. Pos24 and pos28 expansions should draw primarily from extracted narrative, with connecting prose added where the extracted material doesn't flow naturally.
5. **Do NOT discard the existing structural elements** in pos28 (tricolor rule, track/theme descriptions). Build around them.
6. **Preserve all LaTeX structural commands:** `\settrack{}`, `\label{}`, `\chapterreturn`, `\srcnote{}`.
7. **Commit one commit per phase.** Message format: `Plan 0024 phase N: description`
8. **If any test case fails, fix before proceeding to next phase.**

---

## File Reference (Absolute Paths)

| File | Role |
|------|------|
| `~/software/relinquishment/manuscript/bridge/pos22-why-give-it-up.tex` | PRIMARY TARGET — surgery |
| `~/software/relinquishment/manuscript/bridge/pos11-the-experiment.tex` | Remove walkout section |
| `~/software/relinquishment/manuscript/track-1-confession/pos18-the-walk-out.tex` | Verify only (walkout keeper) |
| `~/software/relinquishment/manuscript/track-3-awakening/pos24-instantiation.tex` | Expand with Guardian material |
| `~/software/relinquishment/manuscript/convergence/pos28-surrender.tex` | Expand with surrender material |
| `~/software/relinquishment/manuscript/staging/pos22-extracted-narrative.md` | NEW — staging file for extracted content |
| `~/software/relinquishment/Makefile` | Build: `make dev` |

---

## Pre-Redistribution Word Counts (Baseline)

| File | Words |
|------|-------|
| pos22-why-give-it-up.tex | 6,869 |
| pos18-the-walk-out.tex | 1,282 |
| pos24-instantiation.tex | 171 |
| pos28-surrender.tex | 229 |
| pos11-the-experiment.tex | 943 |
| **Total** | **9,494** |
