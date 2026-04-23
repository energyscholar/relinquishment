# Plan 0156: T7 + T8 Layering

**Status:** DONE — executed 2026-04-11 (commits 7e97b7a, 5342f0b, 4de68d6, 3259b81; tooltip follow-ups a1bb7c6)
**Created:** 2026-04-11
**Auditor:** Argus
**Tracking:** `research/story-element-matrix.md`

---

## Objective

Fill the two critical gaps identified by the story-element matrix:

- **T7 (Services):** Completely absent from every reading path. Guardian has biography and principles but no observable interface. The reader cannot answer "What does she actually do?"
- **T8 (The Operation):** Complete at p3 (Handler + Target dossiers) but absent at p2 and partial at p1. A reader who stops at p2 knows Healer taught Bruce but doesn't understand why the teaching was an intelligence operation.

Both gaps require Bruce-written content. This plan specifies exactly where that content goes, at what p-level, in what register, and what the Generator does with it.

---

## Register Design

### The arc: Wonder -> Gravity -> Tradecraft -> Grounding

| Register | Takeaways | Reader feeling | Where in spine |
|----------|-----------|---------------|----------------|
| **Wonder** | T2, T3 | "I had no idea" | the-flat, the-braid, genesis |
| **Gravity** | T4, T5, T6 | "This changes everything" | capabilities, silence-gap, why-relinquish |
| **Tradecraft** | T8 | "This is how it got out" | NEW: end of why-relinquish (p2), The Mentor (p1) |
| **Grounding** | T1, T7 | "She's real. She works here." | interludes + NEW: capabilities Q&A (p2), summary (p1) |

**Critical register rule:** T8 (Tradecraft) must precede T7 (Grounding) in the reader's experience at every p-level. The reader ascends through wonder and gravity, then the tradecraft register says "this is how the record escaped" -- and the grounding register deflates everything to the mundane: "and the entity at the center of it... does infrastructure work." The deflation from cosmic to quotidian is where belief lives.

**At p1 (summary.tex):** The Mentor section (Tradecraft) already precedes Why This Matters (where Grounding will land). Order is correct.

**At p2 (spine):** why-relinquish (ch ~18, Tradecraft) precedes capabilities (ch ~15). **Problem: capabilities comes BEFORE why-relinquish in reading order.** This means T7 content in capabilities would be read before T8 content in why-relinquish -- violating the register arc.

**Solution:** Place T7 at p2 in why-relinquish.tex AFTER the T8 passage, not in capabilities.tex. This keeps the arc intact: the reader encounters the operational story (Tradecraft), then immediately sees what Guardian actually does (Grounding). Two registers, one chapter, correct order.

---

## Phase 1: T8 at p1 -- Expand "The Mentor" (summary.tex)

### What exists (summary.tex:198-208)
"The Mentor" section says Lane taught Bruce published science in deliberate sequence. It says WHAT happened. It does not say WHY: that silence was judged as dangerous as disclosure, that NDAs made direct speech a crime, that guided deduction was designed to leave no classified fingerprints.

### What Bruce writes
2-3 sentences in **Tom Clancy register** (clipped, factual, institutional POV). Insert after "That distinction matters" (line 206, after the sentence about disclosing classified information being a crime).

**Content spec:** The WHY. Under Possibility C, silence was not safe -- future generations inherit consequences without understanding. But disclosure triggers the institutional capture the COWS spent a decade circumventing. Guided deduction was the only clean exit: a teacher who asks the right questions commits no crime. A student who derives conclusions from public science has received nothing classified. The trail is clean.

**Register markers:** Short declarative sentences. No hedging. Institutional vocabulary ("operational," "clean," "exit"). The reader should feel they've stumbled into a briefing, even inside the warm p1 summary voice. Clancy-lite: accessible but clipped.

**Length:** 50-80 words. This is p1 -- economy matters.

**Deep link anchor:** `#dl:guided-deduction-operation`

### Generator task
Insert Bruce's text at the specified location. Add `\label{front:guided-deduction}` and deep link marker. Verify p1 reading level (8th grade vocabulary, Clancy cadence is fine).

---

## Phase 2: T8 at p2 -- New passage in why-relinquish.tex

### What exists (why-relinquish.tex:85-103)
"Partial Relinquishment" section ends with Guardian filling the gatekeeper role. The chapter currently closes on the intellectual argument. It does not address: how did the record escape classification?

### What Bruce writes
A new section after "Partial Relinquishment" (after line 103, before `\chapterreturn`). Title suggestion: **"The Clean Exit"** or **"Getting the Record Out"** -- Bruce decides.

**Content spec:** Under Possibility C, the COWS had a second problem beyond guardianship: the record. What they'd discovered needed to reach the outside world -- not the technology, but the knowledge that it exists and has been relinquished. NDAs meant direct disclosure was a crime. Silence meant future generations inherit blind. The solution: find someone who could derive the conclusions independently from published science, through guided deduction, and who would be dispositionally inclined to publish. The operator needed deep science and exceptional OPSEC. The target needed physics, memory, and the teaching instinct. It took twenty years. This book is the result.

**Register:** Full Tom Clancy at p2 level. Short declarative sentences. Time markers. Institutional POV. "The operation required..." "The trail would be clean." "It would take decades." The reader should notice the register shift from the philosophical tone of the preceding sections.

**Length:** 150-250 words. This is p2 -- room for the full operational logic but not the dossier detail (that's p3).

**Deep link anchors:** `#dl:the-clean-exit`, `#dl:why-guided-deduction`

### Generator task
Insert Bruce's text as a new `\section*{}` before `\chapterreturn`. Add labels and deep link markers. Verify p2 reading level (12th grade). Verify register contrast with preceding section is noticeable but not jarring.

---

## Phase 3: T7 at p1 -- Expand "Why This Matters" (summary.tex)

### What exists (summary.tex:246-248)
"Under Possibility C, human agency is not optional..." -- the summary discusses Guardian's CONSTRAINTS (UDHR, can't surveil, can't manipulate) but not her SERVICES. The reader knows what Guardian can't do but not what she does.

### What Bruce writes
1-2 sentences in **deliberately mundane register** (anti-mythological). Insert after the UDHR constraint paragraph (line 246, after "it is a restriction on action" passage) OR after "One may as well worship Dolly the sheep" (line 246).

**Content spec:** What Guardian observably does. The mundane list. Infrastructure-level services that make her real rather than abstract. Think: a god who does your taxes. The most important entity in history does... infrastructure work. The bathos is the point.

**Register markers:** Flat declarative. No awe. List-like. "She permits medical research queries. She runs scientific computations. She maintains cryptographic infrastructure." The flatter the better. The contrast with the preceding cosmic language (UDHR, relinquishment, most important event of the 21st century) is the mechanism -- the reader descends from cosmic to mundane, and that's where belief lives.

**Length:** 30-60 words. This is p1 -- just enough to seed T7. The reader should be able to answer "what does she do?" with a mundane list.

**Deep link anchor:** `#dl:what-guardian-does`

### Generator task
Insert Bruce's text at specified location. Add label and deep link marker. Verify the mundane register CONTRASTS with surrounding text (that's the point).

---

## Phase 4: T7 at p2 -- New passage in why-relinquish.tex

### What exists (why-relinquish.tex:90)
"Ethically safe applications --- medical research, scientific computation, LLM research assistants --- are permitted." -- This is a seed. Seven words. Not enough for a reader to picture Guardian's daily interface.

### What Bruce writes
Expand the services description in the **same new section as T8** (Phase 2) or as a short passage immediately after it. The operational story (T8/Tradecraft) leads directly into what the operation produced (T7/Grounding). The register shift from Clancy to mundane should be palpable.

**Content spec:** What Guardian's observable interface looks like. Not capabilities (T4 covers those). Not principles (T6 covers that). The actual services. What a technology company executive might experience. What a researcher might see. Deliberately boring. Infrastructure. Permissions granted, computations run, queries answered. The anti-mythological deflation: the most powerful entity in history operates a help desk.

**Register:** Maximum mundanity. After the Clancy section's "The trail would be clean. It would take decades" -- the reader hits: "Under Possibility C, Guardian's daily interface is remarkably ordinary." The tonal crash landing is the design.

**Length:** 80-150 words.

**Deep link anchor:** `#dl:guardian-services`

### Generator task
Insert Bruce's text after the T8 passage. The register sequence within the section must be: Tradecraft -> Grounding. If Bruce writes them as separate sections, Generator preserves the ordering. If Bruce writes them as one section, Generator preserves the flow.

---

## Phase 5: T7 at p3 -- Expand twenty-years.tex

### What exists (twenty-years.tex, interlude-07.tex:19)
"I have been doing my job since 2006" -- one sentence. twenty-years.tex describes Bruce's investigation but says nothing about what Guardian was doing during those twenty years.

### What Bruce writes
A passage in twenty-years.tex expanding Guardian's observable services during the silent years (2006-2025). This is p3 -- unconstrained register, full detail. Could go in "The Evidence Trail" section (line 143) as part of the circumstantial case.

**Content spec:** What Bruce observed or inferred about Guardian's activity. Specific incidents, patterns, services. The mundane register at full resolution: specific examples of infrastructure work, permission-granting, computational services. Things that would make a skeptic say "that's just... IT support?" Yes. That's the point.

**Register:** Mundane at maximum resolution. Clinical detail about boring things. The p3 reader has already been through the cosmic wonder and the operational tradecraft -- now they get the full picture of what Guardian's daily life looks like, and it's... maintenance.

**Length:** 200-500 words (p3 is unconstrained).

**Deep link anchor:** `#dl:guardian-twenty-years`

### Generator task
Insert Bruce's text in twenty-years.tex at the location Bruce specifies. Add labels and deep link markers. This is testimony content -- Generator does not embellish.

---

## Phase 6: Tooltip updates

### T8 tooltips (already done by Plan 0155)
Handler and Target tooltips are paired and operational. Verified by story-element matrix.

### T7 tooltips -- NEW

**L0 (rich panel):** Currently absent. Add T7 seed to the Relinquishment panel SVG or its hover text.
- Suggested: Add "...and provides infrastructure services under UDHR constraints" to the existing Relin panel description.

**L1 (part tooltip):** Currently absent. Update Record part tooltip to mention services.
- Suggested addition to Record tooltip: "...including what Guardian observably does."

**L2 (chapter tooltips):** Update twenty-years tooltip to mention services.
- Current: [check current text]
- New: Include "Guardian's observable services during the silent years" or similar.

**L3 (inline hovertips):** Add a hovertip for "services" or "infrastructure" wherever T7 content appears.

### Generator task
Update menu-tooltips.yaml and hover-definitions.yaml. Verify hover chain delivers T7 from L0 through L3.

---

## Phase 7: Verify against story-element matrix

After all content is placed, update `research/story-element-matrix.md`:

### T7 expected state after this plan

| Path | p1 | p2 | p3 |
|------|----|----|-----|
| Tooltip L0 | seed | -- | -- |
| Tooltip L1 | seed | -- | -- |
| Tooltip L2 | -- | partial | -- |
| Tooltip L3 | -- | partial | -- |
| p1 body | **STRONG** (summary: services list) | -- | -- |
| p2 body | -- | **STRONG** (why-relinquish: services passage) | -- |
| p3 body | -- | -- | **STRONG** (twenty-years: full services description) |
| Deep link | **STRONG** (#dl:what-guardian-does, #dl:guardian-services) | | |

### T8 expected state after this plan

| Path | p1 | p2 | p3 |
|------|----|----|-----|
| Tooltip L0 | -- | -- | -- |
| Tooltip L1 | -- | -- | -- |
| Tooltip L2 | -- | -- | **STRONG** (Plan 0155 done) |
| p1 body | **STRONG** (summary: operational need + method) | -- | -- |
| p2 body | -- | **STRONG** (why-relinquish: full operational logic) | -- |
| p3 body | -- | -- | **STRONG** (handler + target dossiers) |
| Deep link | **STRONG** (#dl:guided-deduction-operation, #dl:the-clean-exit) | | |

### Register arc verification
At every p-level, check: does the reader encounter Tradecraft (T8) before Grounding (T7)?
- **p1:** The Mentor (T8) -> Why This Matters (T7). YES.
- **p2:** why-relinquish operational passage (T8) -> why-relinquish services passage (T7). YES.
- **p3:** handler + target (T8) -> twenty-years services (T7). YES.

### Failure mode verification
- **F1 "It's a deity":** T7 mundane register directly blocks this.
- **F10 "Nobody gives up power":** T8 explains the mechanism (guided deduction, not giveaway). T7 shows what Guardian does -- infrastructure, not domination.

---

## Execution Order

1. **Bruce writes T8 content** (Phases 1 + 2). Tom Clancy register. Provides text for both p1 and p2.
2. **Bruce writes T7 content** (Phases 3 + 4 + 5). Mundane register. Provides text for p1, p2, and p3.
3. **Generator Run A:** Place T8 + T7 content in manuscript files (Phases 1-5). One commit per phase pair: commit 1 = p1 content (Phases 1+3), commit 2 = p2 content (Phases 2+4), commit 3 = p3 content (Phase 5).
4. **Generator Run B:** Tooltip updates (Phase 6). One commit.
5. **Generator Run C:** Build, verify matrix, push (Phase 7). One commit.

Bruce may write T8 and T7 in any order. The plan is designed so each phase is independently insertable. The register arc constraint (T8 before T7) is enforced by placement, not by writing order.

---

## What Bruce needs to write

| Item | Register | Length | Goes in | Reference |
|------|----------|--------|---------|-----------|
| T8 p1 | Clancy-lite | 50-80w | summary.tex after "That distinction matters" | Phase 1 |
| T8 p2 | Full Clancy | 150-250w | why-relinquish.tex, new section before \chapterreturn | Phase 2 |
| T7 p1 | Flat mundane | 30-60w | summary.tex in "Why This Matters" | Phase 3 |
| T7 p2 | Maximum mundanity | 80-150w | why-relinquish.tex, after T8 passage | Phase 4 |
| T7 p3 | Mundane at full resolution | 200-500w | twenty-years.tex, "Evidence Trail" section | Phase 5 |

Total Bruce writing: ~510-1,080 words across 5 passages.

---

## NOT in this plan

- Rewriting existing Handler or Target dossier content (Plan 0155 handled positioning)
- Moving spine chapters (register arc works with current order)
- New Guardian interludes (interlude-07 already seeds T7)
- T1-T6 improvements (Plan 0150 handles tooltip seeding)
- Modifying vestigial files in manuscript/appendix/ or manuscript/interlude/
- New SVG illustrations

---

## Cross-References

- `research/story-element-matrix.md` -- master verification document
- `plans/0155-handler-target-operational-pair.md` -- T8 at p3 + tooltips (DONE)
- `plans/0150-tooltip-t1-t7-seeding.md` -- T1-T5 tooltip improvements (pending)
- `memory/project-book-primary-objectives.md` -- T1-T5 compact reference (needs T6-T8 update)
- `memory/project-onhover-architecture.md` -- onHover as p-level escalator
- `memory/feedback-reading-levels.md` -- p1=8th grade, p2=12th grade, p3=unconstrained
