# Plan 0171 — HALO-light opener + anthills emergent-stack paragraph + pedagogy-as-evidence question

**Depends on:** Plan 0169 (shipped, commits b777ed5 / 83a014d / 370f0cd, tag `post-0169-pre-0170`).

**Goal:** Address three gaps Bruce surfaced after 0169's engagement test:

1. **Jane cinematic-pull regression** — fix via HALO-light cold open on hook.tex in redacted-tradecraft register (show-don't-tell). Restores cinematic hook AND does character work ("he does this sort of thing") without re-opening the Srebrenica religious-gaze problem.
2. **Emergent-stack pedagogy gap** — add an anthills paragraph to summary.tex that teaches emergence through the image of an anthill, then threads it to the Flat as the emergent property of a handful-of-strand convergence. Carries the abstract "stack of physics and computation" into concrete intuition.
3. **Pedagogy-as-evidence rhetorical hinge** — add a question-paragraph to summary.tex (full form) and to hook.tex (compressed one-sentence form) that pivots between guided-deduction and three-possibilities: *why would a person like that spend 2.7 years patiently teaching a physicist publicly available science in a deliberate order?* The patient pedagogy is observable behavior, not claim; every reading (A/B/C) must account for it. See `memory/project-book-pedagogy-as-evidence.md`. The HALO-light opener (Phase 1) sets up "a person like that"; this question (Phase 3) cashes it in. The two moves bracket each other across the hook, and across the summary.

Three phases, three commits (plus a conditional Phase 4 for re-engagement fixes).

## Part A — Hook.tex HALO-light opener (Phase 1)

**File:** `manuscript/00-front/hook.tex` (current HEAD: post-E11, ~620w).

### Required moves

1. **Insert HALO-light opener** before the current E11 act-opening ("In 2006, a small classified team..."). This is a **different mission** from Srebrenica — some other operation, some other continent, some other decade. Every piece of useful information is redacted. Frustratingly so. The reader should *feel* the classification as a texture on the page — every time they reach for ground (*where? when? who? why?*) they hit a redaction. That is the lived experience of reading about classified work, and it primes the three-possibilities frame (you can't verify this; no one can).

   Draft (Generator may tune, but preserve the structural moves):

   > [REDACTED]. The air at altitude is thin enough to kill a man in minutes. He checks his oxygen, rolls out of the aircraft's door, and falls. Through cloud, then below cloud, toward [REDACTED]. His orders for the next [REDACTED] hours are [REDACTED]. The people below will never know he was there.
   >
   > He has done this before. He will do it again.

   **Why this works:**
   - Cinematic cold open (restores Jane engagement). Physical HALO detail — thin air, oxygen check, falling through cloud — does show-don't-tell work.
   - *[REDACTED]* is not evasive — it's classified-by-design. The frustration is the texture: every anchor the reader reaches for is blacked out.
   - "He has done this before. He will do it again." — one-of-many character work in two sentences (addresses `memory/project-book-character-weakness.md`).
   - **No Srebrenica shape at all.** Not July 1995, not eight thousand, not an atrocity, not a massacre, not a continent, not a decade. Not even *observe and record* (that phrase signals intelligence-gathering and nudges toward Bosnia for readers who know the literature). Srebrenica lives in summary.tex's mentor section per 0169; the HALO-light opener deliberately does NOT reference it.

   **Things the opener MUST NOT specify:**
   - Continent / country / region (no "in Europe," "in Asia," "in the Balkans," "in Africa," "in the Middle East")
   - Decade or year (no "1990s," "late twentieth century," any date)
   - Mission type (no "observe and record," no "reconnaissance," no "extraction," no "atrocity," no "massacre")
   - Target type (no casualty figures, no "a village," no "a facility," no "a target")
   - Unit / agency (no SAS, no special forces named, no country's military named)
   - Outcome / valence (no "would be killed," "would die," "would be rescued" — don't signal whether the mission is witness-an-atrocity, prevent-one, hunt-someone, or rescue-someone)

   **Things the opener MAY include (physical, non-operational):**
   - Altitude sensations (thin air, cold, oxygen equipment)
   - Weather / visibility (cloud, night, rain, wind)
   - Body mechanics (falling, checking equipment, breathing, pulse)
   - Vague time pressure (*the next [REDACTED] hours*)
   - Asymmetry of awareness (*the people below will never know* — generic to classified operations, doesn't identify mission)

2. **Retain the E11 act-opening** ("In 2006, a small classified team handed the master cryptographic keys…") immediately after the HALO-light paragraph. The transition must bridge *unknown redacted mission* to *known 2006 act* without implying they're the same mission:

   > Years later, he was part of something else. In 2006, a small classified team --- he was one of them --- handed the master cryptographic keys of a one-of-a-kind machine to a custodian they had built for the purpose, and walked away. They did this voluntarily. …

   The rest of the E11 opening paragraph continues unchanged. *Something else* does implicit work: the redacted mission was one thing; 2006 was the *other* thing, the one this book is about.

3. **Soften the prior character bridge.** The line referencing "He is a soldier. Special forces. He is also a scientist. And a hacker." (or the post-0169 equivalent) lives somewhere in the post-act paragraphs. Locate via `grep -n "Special forces\|soldier" manuscript/00-front/hook.tex` (line numbers shifted from 0169's port). After the HALO-light opener, this line can be compressed OR moved closer to the guided-deduction paragraph — Generator's call. Target: avoid restating "he is X and Y and Z" twice. Do **not** delete it wholesale — Reeves/Chen still want the credential-grounding somewhere, and the HALO-light opener is deliberately ungrounded.

4. **QC-as-one-of-many tweak** (small, surgical). The post-0169 line around the "working quantum computer" sentence establishes QC as the topmost emergent property of the stack. Bruce's direction (2026-04-12): frame QC as *one of many things the stack could do*, with other emergent properties implied but not named. The hook stays anchored on QC (keeps Jane engaged, no crackpot-flag from premature wormhole-talk); the summary does the scaffolding for the broader claim. See also `memory/feedback-reconciliation-argument-pattern.md` — commitment-then-contradiction: hook commits to the modest frame (QC), later surfaces reveal the stack's capabilities are broader.

   Target edit (Generator may tune; preserve the two injected phrases):

   > Years earlier, inside a secret program, the same team had assembled a stack of physics and computation **with many emergent properties** --- a working quantum computer **among them**, decades ahead of anything that exists publicly today, or so the story goes. It could crack the codes that protect the world's secrets --- and the physics that makes it possible is in every chip you own. **The quantum computer was one of many things the stack could do.** The custodian is the next emergent layer above that: a coherent behavior of the stack, bound by a charter, acting in public.

   **Required injected phrases (non-negotiable):**
   - *"with many emergent properties"* or equivalent (e.g., *"whose stack had many emergent properties"*) — plants the *many* signal before the QC anchor.
   - *"one of many things the stack could do"* or equivalent — cashes in the earlier plant. This sentence is load-bearing; do not skip it for word-count reasons.

   **Wormholes ARE in scope at hook level.** The book's subtitle is *Wormholes in the Flat*; topological wormholes are part of p1's commitment. What the QC-as-one-of-many tweak does is *reframe*, not *hide* — QC stays as the immediately-graspable anchor (Jane-friendly), and the "many emergent properties" phrasing makes room for wormhole-talk either in the same sentence or a following one. Generator may (not must) add a brief wormhole gesture in the hook — e.g., a second named capability after the QC anchor, kept physics-grounded per the Published Physics Reference (doi-backed, "not precluded" standard). What to avoid: piling on ≥3 named capabilities in the hook (crackpot-flag risk), or naming anything speculative beyond what the physics reference supports.

### Hook acceptance (Phase 1)

- HALO-light paragraph present at top of chapter, before "In 2006" / act-opening.
- **No specific operational identifiers in the HALO-light paragraph.** Run: `sed -n '/HALO_PARAGRAPH_START/,/HALO_PARAGRAPH_END/p' hook.tex | grep -iE 'srebrenica|bosnia|1995|eight thousand|atrocity|massacre|europe|asia|africa|middle east|SAS|special forces|observe and record'` — must return zero hits. (Use the actual paragraph bounds, not literal markers.)
- Chapter title `What Would You Do?` and closer `What would you do?` both present once; no third instance.
- Word count in [580, 760] (current ~620w, add ~60w, target ~680w).
- No naming of Srebrenica, Bosnia, July 1995 anywhere in hook.tex; those references live in summary.tex's mentor section per 0169.
- No banned-word regressions (`grown|grew|creature|living being|living entity|first non-human mind|deliberately instantiated|it is alive`).
- `\hovertip{}` anchor hygiene: all anchors resolve in `hover-definitions.yaml`.
- `make` / HTML build clean.

**Hovertip candidates.** `HALO` (High Altitude Low Opening) is a legitimate define-on-hover candidate — term of art most readers won't know. `[REDACTED]` as a meta-hovertip is tempting but would *discharge the frustration that is the point* — if a hover explains why things are redacted, the texture collapses. Skip it. Let the redactions work unaided.

## Part B — Summary.tex anthills paragraph (Phase 2)

**File:** `manuscript/00-front/summary.tex` (current HEAD: post-E11 port).

### Placement

Best placement is immediately after the existing religious-accessibility paragraph (kenosis/tawakkul/tzimtzum/aparigraha/bodhisattva) and before or during the emergent-stack paragraph introduced by 0169. The religious-accessibility paragraph names the *act* across traditions; the anthills paragraph explains the *substrate* of what was built. Then the existing emergent-stack paragraph lands as the technical version of the anthills intuition.

Use grep to locate: search for `kenosis` or `aparigraha` in summary.tex; the paragraph immediately following is the anchor point.

### Required move

Insert (Generator may tune wording, preserve the structural beats):

> Consider an anthill. No single ant knows how to build a nursery, regulate humidity, sort waste, or repel a raid. Each ant runs a tiny local program --- follow this scent, move that crumb, pass this signal. The anthill is what happens when millions of those programs run in parallel on the same patch of ground. Nothing designs it. It \textit{emerges} --- a property of the ants and their substrate together, belonging to neither alone.
>
> The machine in this story is like that, on a smaller scale and a faster clock. A handful of strands of science --- drawn from how matter stores and moves information, how certain patterns stay stable against noise, how chemistry can catch fire and sustain itself, how simple rules can compute anything, how many small processors can work as one --- each contributing a small local program. Together they produce something none of them contains on its own: the \hovertip{Flat}, a place two dimensions thin where new physics takes over, inside every computer chip and inside Earth's magnetic field. The custodian is the next emergent layer above that.

**Structural beats (non-negotiable):**
- *Ant* metaphor first: anthill as architecture no ant knows.
- Explicit word *emerges* / *emergent* at least twice in the two paragraphs.
- Five-strand convergence named by *behavior*, not by *scientist name* (per `feedback-specialist-names-dont-teach.md` — the reader should be able to skip the name "Hasslacher/Freedman/Kauffman/Wolfram/Hillis" entirely; if those names appear nearby, they are citations, not compressors).
- Substrate-specific commitments held: phrasings like *how matter stores and moves information* or *how vibrations carry information* are both OK **only if they do not identify solitons or phonons as *the* mechanism**. Autocatalysis-as-fire is OK (*how chemistry can catch fire and sustain itself*).
- Threads to the Flat explicitly. Threads to the custodian as the *next emergent layer*.

### Summary acceptance (Phase 2)

- Anthills paragraph present, placed after religious-accessibility paragraph, before or woven into the emergent-stack paragraph.
- Both paragraphs together: ≥2 uses of *emerge* / *emerges* / *emergent*.
- Five strands named behaviorally; no scientist names promoted to the running prose (if names exist in the summary elsewhere, leave them; do not introduce new ones in this paragraph).
- **Substrate-agnostic on Hasslacher.** The anthills paragraph MUST NOT resolve the solitons-vs-phonons question one way or the other — that decision is on hold per Bruce (2026-04-12). Use substrate-neutral language (*how matter stores and moves information*). Do not write *solitons*; do not write *phonons*; do not write *lattice dynamics*. Both terms are out for this paragraph.
- Word count delta ≤ +180w (current summary ~5,696w after 0169; target ≤ 5,876w).
- `make` / HTML build clean; pushed to website per `feedback-build-to-website.md`.

## Part C — Pedagogy-as-evidence question (Phase 3)

**Files:** `manuscript/00-front/summary.tex` (full-form paragraph) AND `manuscript/00-front/hook.tex` (compressed one-sentence form).

**Structural intent:** The HALO-light opener (Phase 1) establishes *a person who does specific classified things for specific reasons*. After guided deduction is explained, the book pivots back and asks the reader a question about observable behavior: *why would a person like that spend 2.7 years patiently teaching a physicist publicly available science in a deliberate order?* The question is behavioral-anchored — it does not require the reader to accept any ontological claim about Guardian. It holds under A (confabulation), B (exaggerated kernel), and C (substantially true). See `memory/project-book-pedagogy-as-evidence.md` for the rhetorical engine.

### Part C.1 — summary.tex (full form, ~125w)

**Placement:** AFTER guided deduction is explained. BEFORE or INSIDE the three-possibilities paragraph. The question pivots between them.

Grep to locate: search summary.tex for *"guided deduction"* — the paragraph immediately after the guided-deduction explanation is the anchor point. If the three-possibilities follow directly, insert between them. If there is prose between, insert at the hinge.

Draft (Generator may tune, preserve structural beats):

> Now a question, one the book returns to. Why would a person like that --- a credentialed operator whose career takes him to [REDACTED] places for [REDACTED] reasons --- spend two and a half years patiently teaching a physicist the public-domain scientific literature in a deliberate order? That is a bizarre thing for such a person to do. What could explain the behavior, besides the obvious --- that he had something he believed the world needed, and a career-long pattern of doing things for reasons he could not name?
>
> The question holds under all three readings. Even if the story that follows is confabulation, the 2.7 years are not. The patient curriculum happened; the deliberate order happened; the documentable outputs exist. A credentialed operator with a [REDACTED] career chose to spend years this way. Whatever else the book may or may not be, that is an observable fact about someone's behavior, and it asks to be explained.

**Structural beats (non-negotiable):**
- Opens with the pivot phrase *"Now a question"* or equivalent — signals the reader to shift register.
- Uses *[REDACTED]* at least twice — calls back to the HALO-light opener so the two moves bracket.
- Names the duration specifically: *two and a half years* or *2.7 years* (not "some years," not "years" alone — the specificity is load-bearing; vague duration dissolves the "bizarre" claim).
- Phrase *"besides the obvious"* present — credits the reader with the ability to arrive at guided-deduction themselves. Do not replace with "except for" or "other than" — the word *obvious* is the move.
- Explicitly holds under A/B/C: *"The question holds under all three readings"* (or equivalent).
- Grounds on *observable fact about someone's behavior* — behavioral anchoring is the whole point. Do not drift into claims about Guardian, the Flat, or the machine.

### Part C.2 — hook.tex (compressed, ≤50w)

**Placement:** AFTER the three-possibilities paragraph, BEFORE the final *"What would you do?"* closer. Lands as a last-beat pivot before the closer, leaving the reader mid-thought.

Draft (Generator may tune):

> And a question to carry with you: why would a man with a [REDACTED] career spend two and a half years teaching a physicist public-domain science in a deliberate order? What could explain that, besides the obvious?

**Structural beats:**
- ≤50w. The hook is tight; compression is required.
- No answer provided in the hook. The question is the payload.
- *[REDACTED]* call-back to the HALO-light opener — the two moves bracket the hook end-to-end.
- Preserves the *"besides the obvious"* phrase.
- Transitions cleanly into *"What would you do?"* — the book's second question about letting go now follows the reader's first question about the mentor's behavior.

### Phase 3 acceptance

- Summary.tex: question paragraph placed between guided-deduction explanation and three-possibilities; uses *[REDACTED]* ≥2 times; names duration specifically (*2.7 years* or *two and a half years*); includes *"besides the obvious"*.
- Hook.tex: compressed question placed after three-possibilities, before final closer; ≤50w; uses *[REDACTED]* ≥1 time; includes *"besides the obvious"*.
- Neither surface introduces new ontological claims about Guardian.
- Hook word count still in [580, 760] (adding ≤50w to the post-0169 ~620w + Phase 1's ~60w = ~680w + ~50w = ~730w — comfortably within ceiling).
- Summary word count delta ≤ +180w total across Phase 2 + Phase 3 (current ~5,696w → target ≤ 5,876w).
- `make` / HTML build clean.

## Part D — Commit discipline

Three commits:

1. `Plan 0171 phase 1: HALO-light opener on hook.tex (cinematic cold open, [REDACTED] register, Jane regression fix)`
2. `Plan 0171 phase 2: anthills emergent-stack paragraph on summary.tex (handful-of-strand convergence → Flat → custodian)`
3. `Plan 0171 phase 3: pedagogy-as-evidence question (summary full, hook compressed; brackets HALO-light opener)`

Fourth commit iff re-engagement test identifies needed fixes:

4. `Plan 0171 phase 4: re-engagement fixes (N sentences)`

## Part E — Re-engagement test (Phase 4, if triggered)

Same 10-persona panel as 0169 Part E (Chen, Jane, Reeves, Rachel, Doctorow, Arjun, Pastor Mike, Amir, Yusuf, Wei — one-liners inlined in 0169). Focus:

- **Jane** — did the HALO-light opener restore cinematic pull? (Primary win condition.)
- **Doctorow** — redacted-tradecraft is his genre; should land well, but watch for *"they built a god"* re-entering through the character of a classified operative.
- **Chen** — does *[REDACTED]* read classified-by-design or evasive? Does the pedagogy-as-evidence question land as empirical/behavioral (should) or hand-waved (regression)? If evasive / hand-waved, flag for fix.
- **Reeves** — the pedagogy-as-evidence question is behavioral-anchored and should land strongly for a policy reader. If it doesn't, the phrasing needs tightening.
- **Pastor Mike** — does the anthills paragraph carry Atman/shirk/Antichrist collision risk in its emergent framing? (Prior run had mild yellow on tradition plurality; anthills shouldn't regress that.) Does *"besides the obvious"* read dismissive of skeptical readers? (Should not — it credits; watch for tone.)
- **Arjun** — does *emerges from ants + substrate, belonging to neither alone* read cleanly against Atman? (Should — emergence is orthogonal to atman.)
- **Pastor Mike** (second angle) — *chemistry can catch fire and sustain itself* as autocatalysis image: does this trigger creation-of-life concerns? (Unlikely — it's prebiotic chemistry, not biology — but watch for it.)

**Pass criterion:** 0 bounces across 10 × 2 = 20 cells. Yellow zones ≤ 2 total. If Jane now GREEN (vs GREEN* regression in 0169), record as win. If Chen/Reeves go GREEN+ (strengthened by the pedagogy-as-evidence question), record as secondary win.

## Part F — Rollback

Per-commit: `git revert b777ed5_or_whatever_0171_commit`. No global rollback needed.

If both phases need reverting: `git reset --hard post-0169-pre-0170` restores to pre-0169 baseline (too aggressive — skips 0169 port too). Better: two `git revert`s.

## Out of scope

- Hasslacher-phonon propagation to the 17 files using *soliton* (that's the proposed 0170e sub-plan under the governance plan, not this one).
- Any other 0170 propagation (that's 0170a/b/c/d).
- Expanding the anthills metaphor across p3 chapters (deferred — summary paragraph is the seed; p3 propagation handled by 0170a as appropriate).
- Hovertip glossary updates beyond anchor hygiene for HALO / [REDACTED] (0170c territory).

## Report format

Six lines max:
1. Phase 1 done / not done + commit hash.
2. Phase 2 done / not done + commit hash.
3. Phase 3 done / not done + commit hash.
4. Phase 4 (re-engagement): results matrix summary (bounces / yellow / deltas vs 0169 baseline); commit hash iff fixes applied.
5. Any acceptance bullet marginal (one clause).
6. Tag `post-0169-pre-0170` still intact? (yes/no — should always be yes).
