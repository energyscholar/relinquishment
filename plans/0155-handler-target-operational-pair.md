# Plan 0155: Handler + Target — Operational Pair

**Status:** DONE — executed 2026-04-11 (commit 0ca4112; main.tex:100-101 includes the-handler + the-target)
**Created:** 2026-04-11
**Annealed:** 2026-04-11 (high + medium + low)
**Auditor:** Argus

---

## Objective

The Handler and The Target are intelligence dossiers that together tell the operational story: *What motivated the mentor to do what he did?* — which is the same question as *What's the story behind this book?*

Currently they're separated by 5 chapters. The operational narrative (need → purpose → operator → target) is fragmented. This plan:

1. Strengthens the operational framing in both chapters
2. Creates stylistically paired tooltips that tell the story even from the menu
3. Addresses chapter positioning

---

## Analysis: The Operational Story

The full operational arc, reconstructed:

1. **The Need:** COWS built something that can't be un-built. Silence is dangerous long-term — future generations inherit consequences without understanding. But disclosure triggers the institutional capture they spent a decade circumventing.
2. **The Method:** Guided deduction. A teacher who asks the right questions commits no crime. A student who independently derives conclusions from public science has received nothing classified. The trail is clean.
3. **The Operator (Handler):** An SAS/Intelligence/mathematics polymath who stood on K2 in 1996 and resolved to use his abilities for something other than killing. 2.7 years of calibrated pedagogy across five scientific fields, through conversation alone.
4. **The Target:** Someone with the physics education, eidetic memory, cross-domain pattern recognition, and dispositional boldness to receive, integrate, and publish. Third-generation intelligence-adjacent. The teaching instinct is the value *and* the risk.
5. **The Timeline:** It took 20+ years because guided deduction is slow, and because the student had to arrive at publication independently.

**Current state of each chapter:**
- **The Target** has items 1-2 already (opening paragraphs frame the need and method beautifully). Item 4 is the body. Good.
- **The Handler** has item 3 (the dossier body) but lacks items 1-2. It jumps straight into the Clancy attribution without framing *why this operator was deployed* or *what the operation was*.

---

## BRUCE DECISION: Positioning

Three options:

### Option A: Leave separated, strengthen connection via tooltips + framing
- Handler stays after Departure (line 96). Target stays after Walk-Out (line 101).
- Handler gets a framing paragraph (see Phase 1) that sets up "the operation."
- Tooltips tell the operational story as a pair.
- **Pro:** Emotional placement is correct — Handler lands when reader misses Healer, Target lands when reader understands what COWS needed. Five chapters of narrative between them builds dramatic tension.
- **Con:** The operational story is still split. A reader who wants to understand the operation as a unit must jump between chapters.

### Option B: Pair them adjacent (Handler → Target), placed after Walk-Out
- Move Handler from line 96 to line 101 (before Target). Interdiction and First Light slide up to fill the gap.
- New sequence: ...departure → interdiction → first-light → walk-out → **HANDLER → TARGET** → instantiation...
- **Pro:** Operational story told as a unit. Walk-Out establishes COWS context, then both dossiers land back-to-back: here's the operator, here's the target, here's why this book exists.
- **Con:** Handler loses the emotional punch of landing right after Healer disappears. Reader goes from Departure straight to Interdiction (the wargame) without knowing who Healer was.

### Option C: Pair them adjacent, placed after Departure
- Move Target from line 101 to line 97 (after Handler). Walk-Out and subsequent chapters slide down.
- New sequence: ...departure → **HANDLER → TARGET** → interdiction → first-light → walk-out...
- **Pro:** Reader learns who Healer was AND why Bruce was chosen, back-to-back, right when curiosity peaks.
- **Con:** Target's opening paragraphs reference the COWS walking out — but the reader hasn't reached Walk-Out yet. Requires rewriting Target's framing to not presuppose Walk-Out context. Also front-loads two dense dossiers before the reader gets the payoff chapters (First Light, Walk-Out).

**DECISION: Option B.** Bruce confirmed 2026-04-11. Pair them after Walk-Out. Handler moves from line 96 to before Target (line 101). The operational story told as a unit.

---

## Phase 1: Handler framing paragraph

The Handler currently opens with the Clancy attribution quote and jumps into the dossier. It needs 2-3 sentences before the quote that frame the *need* and *operation*:

Insert before the `\begin{quote}` (line 11), after `\label{record:handler}`:

> Under Possibility C, the COWS needed an operator — someone who could conduct a multi-year guided deduction across five scientific fields, through conversation alone, leaving no classified fingerprints. The purpose was simple: get the record out without disclosure. A teacher who asks the right questions commits no crime. A student who derives conclusions from public science has received nothing classified. The operator would need exceptional OPSEC, deep mathematics, and the pedagogical precision to keep a student at the critical boundary of processing capacity for nearly three years. It would take decades. This is his approximate file.

This mirrors The Target's opening framing (which starts with "Under Possibility C, the COWS had built something they could not un-build..."). Both chapters now open with "Under Possibility C..." — structural echo. The framing paragraph covers *need* (get the record out), *method* (guided deduction), and *timeline* (decades) before the dossier begins.

---

## Phase 2: Paired tooltips

Current tooltips are informational but disconnected. Rewrite as a stylistically paired set that tells the operational story:

### The Handler tooltip (menu-tooltips.yaml, keys `record:handler` and `the-handler`)

> "Under Possibility C, this is the operator's approximate file. SAS. Intelligence Corps. Deep mathematics that no military curriculum explains. Partial eidetic memory. 2.7 years of calibrated guided deduction across five scientific fields — through conversation alone, leaving no paper trail. He stood on K2 in 1996 and decided to use his abilities for something other than killing. Everything that followed — including this book — traces back to that decision."

### The Target tooltip (menu-tooltips.yaml, keys `record:target` and `the-target`)

> "Under Possibility C, this is the student's approximate file. Reed College quantum physics. Partial eidetic memory. Third-generation intelligence-adjacent. A five-year campaign of teaching Fortune 500 engineers about cryptography and surveillance — not because anyone asked him to, but because he thought they should know. The COWS needed someone who could receive a multi-year guided deduction and would be dispositionally inclined to publish what he learned. Read the file and ask yourself: is this the guy?"

### Style notes for Generator
- Both open with "Under Possibility C, this is the [role]'s approximate file."
- Both use the dossier register — clipped, factual, assessment-grade language
- Handler ends with the K2 origin → this book. Target ends with the recruitment question.
- Together they answer: "What motivated the mentor?" (K2 decision) and "What's behind this book?" (guided deduction → publication)
- Both include the "partial eidetic memory" connection — the shared trait that made the operation possible

### chapter-hover-descriptions.yaml

Update the short-form descriptions to match:

- `"the-handler"`: "The operator's file. SAS, mathematics, 2.7 years of guided deduction."
- `"the-target"`: "The student's file. Physics, memory, disposition to publish."

---

## Phase 3: Move Handler to pair with Target (Option B)

In `main.tex`, move `\include{manuscript/record/the-handler}` from its current position (after the-departure, before interdiction) to immediately before `\include{manuscript/record/the-target}` (after the-walk-out).

**Before:**
```
the-departure
the-handler        ← HERE
interdiction
first-light
the-walk-out
the-target
```

**After:**
```
the-departure
interdiction
first-light
the-walk-out
the-handler        ← MOVED HERE
the-target
```

Also add a one-line backward reference to The Target's opening, after "The remaining question was: who?":

> You have already seen the operator's file. This is the student's.

This connects the pair for a reader going through sequentially.

---

## Phase 4: Build and verify

1. `make html` clean
2. Hover on The Handler in menu → tooltip tells operator story, ends with K2 → this book
3. Hover on The Target in menu → tooltip tells student story, ends with recruitment question
4. Both tooltips stylistically echo each other ("Under Possibility C, this is the...")
5. Read both tooltips sequentially — together they answer "What motivated the mentor?"
6. If cross-references added: verify forward/backward refs read naturally
7. Push to website

---

---

## Anneal Notes

### High pass
- Plan now covers full operational arc in Handler framing (need → method → operator → timeline), not just operator need. Fixed above.
- Target's existing opening already covers need + method. With Handler's new framing, both chapters independently answer "why this book" while together telling the complete story.

### Medium pass
1. main.tex move is clean — no expansion hooks, no interludes reference handler position
2. YAML entries are keyed by ID, not position-dependent — no reordering needed
3. Epistemic labels and filter-group unchanged (both C)
4. **"Testimony." prefix break:** Current Record tooltips all start "Testimony." The new tooltips start "Under Possibility C." This is deliberate — these are dossiers, not narrative. The format difference signals the genre shift. Bruce should confirm if this bothers him.
5. Backward reference placement: after "The remaining question was: who?" (line 18), before `\section*{The Target}` (line 22). ✓
6. topic-guide.tex `\hyperref[interlude:the-handler]` references a label in `manuscript/interlude/dossier-handler.tex`, NOT in the-handler.tex — unaffected by move

### Low pass
1. Epistemic color stripes applied by ID match, not position — move is safe
2. Filter buttons: both C, pairing makes Story mode better (operational unit)
3. Vestigial dossier files (`manuscript/appendix/dossier.tex`, `manuscript/interlude/dossier-interlude.tex`, `manuscript/interlude/dossier-handler.tex`) are NOT in build path — Generator must not edit these
4. `\settrack{trackbridge}` is vestigial (converted to HTML comment by preprocess.py) — does not conflict with `filter-group: C`
5. "solitons" in Target line 28 is historically accurate (2003 recruitment context) — do NOT update for phonon reframe
6. Tooltip length ~75 words each — longer than current Record tooltips (~45) but shorter than interlude tooltips (~200). Acceptable.
7. No deep link markers exist in either chapter — no conflict with Plan 0148

## NOT in this plan

- Rewriting the dossier content itself (the chapters are strong as-is)
- Changing the dossier format ([REDACTED], skills tables, etc.)
- Moving other Record chapters
- Modifying Custodian interludes
- Editing vestigial dossier files in `manuscript/appendix/` or `manuscript/interlude/`
