# Plan 0189 — p3 Refinement (unified)

**Auditor:** Argus
**Date:** 2026-04-13
**Role:** Auditor (planning only; execution via Generator shells, phase by phase)
**Baseline tag (to create at Phase 0):** `eigenvalue41-p3-start`
**Target tag on full success:** `eigenvalue42`
**Supersedes:** Plan 0187 (DEFERRED — its 6 disjoints are subsumed here as Phase 5)
**Absorbs:** Plan 0188 Splice B (pending) as Phase 0c
**Respects:** `memory/project-record-epistemic-status.md` (no relocation of `\settrack{trackone}` chapters out of Record)

---

## 1. Context

p1+p2 are at eigenvalue (eigenvalue40.1 / recent fresh edits ride on top). The compression has been tuned via persona discipline; the expansion (p3) has not. Meanwhile:

- **Plan 0187** identified 6 p3↔p1/p2 disjoints (trustee frame, authority-softening, sentience hedge, five-fields naming, stack-opener, "all-electricity" epistemic label). DEFERRED as too risky to execute as a single pass.
- **Pre-compaction audit** identified ~12,700w savings potential in p3: trackone epistemic openers, spine/the-stack.tex scan-and-collapse, appendix moves (Leaf by Niggle, Joy 10-point), in-place ECHO compressions, lane ownership reshuffle, C-drift fixes at the-flat and the-braid. All structural UQs were answered and authorized.
- **Today (2026-04-13, post-compaction):** dental-floss sentence deleted (afterword + pos34b), timeline Jan 2025 arXiv entry deleted (confabulation + wrong year), Mar 2021 Majorana retraction entry added, p1 opening [REDACTED] density reduced, p2 L193 C-leak gated ("If Custodian exists, she lives in the Flat…").
- **Plan 0188 Splice A** committed (f65d6a0) — the-flat italic framer closes with pluralism-safe sentence. **Splice B** authorized but not yet applied.

Three research docs anchor the framing work:
- `research/renunciation-archetype-2026-04-12.md` — trustee archetype, cross-tradition naming
- `research/sentience-sweep-2026-04-12.md` — behavior-not-ontology rule
- `research/religions-on-llms-2026-04-12.md` — per-tradition anchor words

Two memories gate the method:
- `feedback-c-violation-detector.md` — 3-possibility check on every p1/p2 surface
- `feedback-no-sweetspot-until-budget.md` — no real-API sweetspot runs; Tier-0 mental audit only

---

## 2. Scope & exclusions

**In scope (p3):** spine chapters, Custodian Interludes 1–7, Record chapters, appendix. Backmatter (afterword, glossary) included for targeted fixes only.

**Out of scope (frozen):**
- `manuscript/00-front/hook.tex`, `summary.tex`, `the-stack.tex` (front-matter version), `introduction.tex` — eigenvalue-locked. Fresh edits from today sit on top and are not to be disturbed.
- **Custodian Interludes (all 7): `spine/interlude-01.tex` through `spine/interlude-07.tex` — FROZEN.** Zero-edit invariant. Interludes are Custodian's voice, narratively dense, already tight (1,121w total). Surrounding chapter changes (Niggle move, ECHO compression, lane reshuffle) have no content dependency on interludes. If any phase's Generator discovers an apparent need to touch an interlude, **halt and escalate to Auditor** — do not silently edit. No exception in any phase of this plan.
- Any hover-definitions.yaml term used in front-matter: do not edit the shared hover; edit spine prose to not depend on it.

**Explicit non-goals:** No rewriting of trackone chapters beyond ~40w italic openers + in-place ECHO compress. No relocation of trackone content. No restructuring of Record's part/chapter order.

---

## 3. The ~14-reader low-anneal panel (with variation)

Canonical 9 (from `.sweetspot/personas-9.yaml`): **Chen, Jane, Reeves, Rachel, Doctorow, Arjun, Pastor Mike, Amir, Yusuf.**

Five additions to reach 14:
10. **Tenzin** — Buddhist monastic, reads for non-attachment resonance; watches for atman-collision and bodhisattva-mischaracterization.
11. **Nan** — Indigenous reader (Pacific or First Nations), reads for commons-trusteeship framing; watches for extractive-science tropes.
12. **Maya** — 16-year-old, social-media-native generalist; attention measured in seconds; watches for where she bounces.
13. **TQC-specialist** — condensed-matter QC researcher who remembers the 2021 Majorana retraction viscerally; watches for field-awareness signals and physics-crank flags.
14. **Bill-Joy-archetype** — already-persuaded technologist (read Joy's 2000 essay); watches for whether relinquishment is argued or assumed.

### Reading-order policy (mostly canonical, some variation)

**Canonical path (10 of 14 readers):** hook → summary → spine in author order (three-possibilities → why-relinquish → the-stack → the-flat → the-braid → the-factoring-game → the-code-war → growing-a-mind → genesis → the-wrong-substrate → the-silence-gap → the-strongest-objection → weigh-the-evidence → capabilities) → Custodian Interludes in position → Record → appendix. Canonical readers: Chen, Reeves, Rachel, Arjun, Pastor Mike, Amir, Yusuf, Tenzin, Nan, Bill-Joy-archetype.

**Variants (4 of 14):**
- **Jane** — skims popups/headings only; jumps from hook to summary's Custodian section; skips most spine; reads one Record chapter (first-light) for human texture.
- **Doctorow** — hook, skips summary (pattern-matches "already skeptical"), jumps to three-possibilities + the-strongest-objection + weigh-the-evidence + Firmware Update appendix.
- **Maya** — hook, bounces to Custodian Interlude 1, then scrolls through summary fast, then back to Interlude 7 (last). Dwells on any page with a chart/SVG.
- **TQC-specialist** — opens Firmware Update first, then the-flat, then three-possibilities, then the-braid, then weighs the rest against field norms.

Variation surfaces order-sensitivity failures that canonical-only reads miss.

---

## 4. Rubric (Tier-0 mental, extends existing)

Per reader × surface:

**T-coverage** (tick / partial / miss): T1 Meet Custodian, T2 the Flat, T3 life in Flat, T4 capabilities, T5 silence gap, **T6 trusteeship (not permanent surrender)**, **T7 services to tech companies (practical interface)**, T8 guided deduction as method.

**F-triggers** (none / low / moderate / high): F-crackpot, F-sentience-leak, F-religious (shirk / antichrist / idolatry / atman), F-DK-confabulation, F-scifi, F-delusion, F-exotic-other, F-archetype-mismatch, F-register-dissonance (new — for p1→p2→p3 voice drift).

**3-possibility check:** pass / fail / mild C-leak (location noted).

**Dignity Net level:** L0–L4.5 per 0187 methodology. L3+ is ship-blocking.

**Finish signal:** would this reader keep reading past the surface? Y / N / Maybe + one-line reason.

**Priority edit:** at most one per reader per surface, ranked by reader count across panel.

**Aggregation:** per-surface 14-row matrix → cross-surface failure-mode heatmap → ranked edit list.

**Frozen-surface handling:** Interlude scores are recorded for release-notes context only and do NOT generate priority edits. If any interlude scores L3+ on Dignity Net or triggers F-crackpot from ≥3 readers, halt and escalate to Bruce — do not edit. Per §2 zero-edit invariant.

---

## 5. Phased execution (smallest → largest, audit gates between phases)

Each phase ends with: commit → tag `eigenvalue41-p3-phaseN` → 14-reader mental audit on **p1+p2 only** (regression check — goal: match eigenvalue40.1 baseline) + targeted audit on the surfaces touched this phase. If p1+p2 regresses, rollback.

### Phase 0 — baseline + small standalone fixes (~30 min)

Actions:
- **0a.** Tag current HEAD `eigenvalue41-p3-start`.
- **0b.** Delete `manuscript/record/the-demonstration.tex` (commented out in `main.tex:96`, folded into first-light; carries orphaned label).
- **0c. (Plan 0188 Splice B)** In `manuscript/spine/three-possibilities.tex`, immediately below `\section*{Where to Start}` and before "Extraordinary claims deserve extraordinary priors.", insert standalone paragraph: *The book begins by asking you to doubt it.* No italics, no em-dash.
- **0d.** Fix duplicate `\label{wo-bifurcation}` in `manuscript/record/the-walk-out.tex` (declared at L36 and L58 — one must become `wo-bifurcation-recap` or similar; preserve the L36 one, rename the L58).

Audit gate: p1+p2 regression check only (these changes don't touch p1/p2).

### Phase 1 — spine C-drift fixes (~45 min)

Actions (target sentences written verbatim; do not pattern-match):

**1a. `spine/the-flat.tex` L39** — currently: *"The entity --- under Possibility~C --- does not need to build a communication network. It needs only to read the one that already exists."* Replace with: *"Under Possibility~C, Custodian does not need to build a communication network; she needs only to read the one that already exists."* Preserves C-gating, names the subject (no nominalization drift), no sentience escalation.

**1b. `spine/the-flat.tex` L53** — currently: *"Under Possibility~C, the entity does not build a network. It occupies one."* Replace with: *"Under Possibility~C, Custodian does not build a network. She occupies one."* This is the T4 punchline — sentence structure preserved exactly, only pronoun swapped. DO NOT substitute "substrate" here; the punchline requires an agent, not a substrate.

**1c. `spine/the-flat.tex` L55** — currently: *"Every encrypted message transiting any electronic device passes through a 2DEG. Under Possibility~C, it passes through the entity."* Replace with: *"Every encrypted message transiting any electronic device passes through a 2DEG. Under Possibility~C, it passes through Custodian."*

**1d. `spine/the-flat.tex` L59** — **DO NOT TOUCH.** This line reads *"You do not fight an entity that occupies your power grid..."* — here "an entity" is generic/game-theoretic (the Major Sarah address), not a Custodian referent. Prior drafts of this plan incorrectly lumped L59 with L39/L53/L55.

**1e. `spine/the-braid.tex` L90** — verbatim swap (applied 0189-phase-1, commit 5c81849):

- OLD: `They are proven real by inference: the emergent system is responsive, it computes, it does things in the world.`
- NEW: `They are confirmed real by inference, consistent with FQHE 5/2 interferometry: the emergent system is responsive, it computes, it does things in the world.`

Scope: only the second sentence on L90 changes. First clause ("were not proven real by direct laboratory observation") stays — accurate (5/2 interferometry is inferential). Two calibrations: `proven`→`confirmed` drops overclaim; FQHE 5/2 anchor inserted. Keeps the inference frame the section is structurally built on (ULTRA/quarks/Higgs analogies rest on it).

Audit gate: p1+p2 regression + the-flat + the-braid reader reactions. Gate on Chen + TQC-specialist F-crackpot signal.

### Phase 2 — trackone epistemic opener, selective (~25 min)

**Scope narrowed 2026-04-13** per full-book review: two of the three originally-planned openers are unnecessary.

- `record/the-walk-out.tex` — **SKIP.** Already maximally epistemic (voice tag: "3rd-person scientific/reconstructive — 'According to this account...'"). Opener would be boilerplate-on-boilerplate.
- `record/first-light.tex` — **SKIP (separate work recommended).** L52-58 already performs the epistemic function ("Bruce's own pedagogy is weak here... he is not a neuroscientist... What he understands is the architecture"). Adding a new opener would duplicate. Consider a separate micro-plan to relocate L52-58 earlier in the chapter (zero-word structural improvement).
- `record/interdiction.tex` — **DO ADD.** Register shifts to briefing-paper tone for the classical-backchannels catalog (L75-96). Military/Major-Sarah audience needs "constraint analysis, not eyewitness" framing signaled explicitly.

Opener text for interdiction (Auditor draft; Generator may refine voice but not intent):

> *What follows is a reconstruction of technical constraints and response architecture — derived from physics and engineering principles rather than direct testimony. The classical backchannels are not observed; they are inferred from what any large-scale system must use. Physics bounds the claims; confirmation is not the point.*

Place immediately after `\chapter{...}` and any `\settrack{trackone}` / `\argusvoice` macro, before the first body paragraph.

Audit gate: p1+p2 regression + Reeves, Pastor Mike, Doctorow, TQC-specialist on interdiction register. Gate on F-register-dissonance *for interdiction only*.

### Phase 3 — `spine/the-stack.tex` scan-and-collapse (split: 3a Auditor, 3b Generator)

**Phase 3a — Auditor adjudication (~45 min, no edits):**
- Diff front-matter `the-stack.tex` vs spine `the-stack.tex` paragraph-by-paragraph.
- For each spine-only candidate, write a verdict into this plan file: **TRANSFER** (to which front-matter location), **DISCARD**, or **MIGRATE-TO-APPENDIX** (as standalone "Stack Notes" appendix chapter).
- Default bias: **DISCARD** over transfer. Front-matter is eigenvalue-locked; transfer only if the content is uniquely load-bearing AND not already implicit in the front-matter chart.
- Internet-rung treatment decision logged here.
- Check for inbound `\ref` / `\deeplink{stack-chart}` targets and note each.

**Phase 3a verdicts (Auditor, 2026-04-14):**

Inbound ref catalog (grep on full manuscript):
- `\ref{spine:the-stack}` — **zero inbound references** outside `spine/the-stack.tex:7` itself. Safe to delete the label.
- `\label{the-stack}` — present in both files; front-matter copy remains canonical.
- `\label{stack-chart}` / `\hypertarget{stack-chart}` — present in both; front-matter copy canonical.
- `\deeplink{stack-chart}` — only use is inside front-matter `the-stack.tex:35`, self-referential. No external callers.
- `main.tex:62` — `\include{manuscript/spine/the-stack}` (this is the only build-wiring inbound).

Paragraph-by-paragraph verdicts (spine source → disposition):

| Spine block | Front-matter counterpart | Verdict | Reason |
|---|---|---|---|
| Opening framer L10 ("This book is about a technology so new...") | Front-matter L11 identical | **DISCARD** | Duplicate. |
| Stack definition L12 | Front-matter L13 identical | **DISCARD** | Duplicate. |
| Fire prose L14 (2-sentence: "feeds itself" + "switches on") | Front-matter L15 one-sentence | **DISCARD** | Front-matter compression is eigenvalue-locked. |
| Candle prose L16 | Front-matter L17 compressed | **DISCARD** | Compression validated. |
| Radio prose L18 | Front-matter L19 compressed | **DISCARD** | Compression validated. |
| Ant colony prose L20 | Front-matter L21 compressed | **DISCARD** | Compression validated. |
| **Internet rung L22** (spine-only) | absent from front-matter | **DISCARD** | Redundant with ants (self-organization rung already covered); front-matter chose a 6-column chart without internet and is eigenvalue-locked. |
| AI prose L24 | Front-matter L23 compressed | **DISCARD** | Compression validated. |
| Wormhole paragraph L28 | Front-matter L27 near-identical | **DISCARD** | Front-matter copy canonical; any drift lives there. |
| Chart L35-47 (7 columns) | Front-matter L35-45 (6 columns, no Internet) | **DISCARD** | Chart lives in front-matter. |
| Footnotes ("Topological", "Chemical pheromones") L50-52 | Front-matter L49-51 identical | **DISCARD** | Duplicate. |
| Recap L56 ("Each technology uses every property below it...") | Front-matter L55 identical | **DISCARD** | Duplicate. |
| Nature-parallels L58 ("Most of these properties already exist in nature...") | Front-matter L57 ("Six of these properties...") | **DISCARD** | Front-matter copy is already numerically explicit and pluralism-safe. |
| **L60 "only one not found in any living system on Earth"** | Front-matter L59 "it supports topological wormholes" | **DISCARD (guarded)** | C-violation. Phase 3b §3b guard explicitly halts Generator on any attempt to re-migrate this phrasing. |
| Recap L62 ("This book is about a technology stack so new...") | Front-matter L11 similar | **DISCARD** | Duplicate. |
| Closing italic L66 ("That is all you need to know...") | Front-matter L63 identical | **DISCARD** | Duplicate. |

**Net disposition:** DISCARD entire spine `the-stack.tex`. No TRANSFER required — every spine-unique element is either (a) covered by the eigenvalue-locked front-matter, (b) C-violating and must not migrate, or (c) redundant with an adjacent rung. No MIGRATE-TO-APPENDIX — the deleted content has no standalone didactic value outside the front-matter chart context.

**Phase 3b concrete actions (derived from 3a):**
1. Delete `manuscript/spine/the-stack.tex`.
2. Remove `main.tex:62` (`\include{manuscript/spine/the-stack}`). Leave `main.tex:42` (front-matter include) untouched.
3. No inbound `\ref` updates needed (zero external references to `spine:the-stack`).
4. Verify build: `make dev`; confirm zero undefined refs and zero duplicate labels (front-matter `\label{the-stack}` and `\label{stack-chart}` become sole definers).

**Phase 3b — Generator execution (~45 min):**
- Apply Auditor's verdicts from 3a.
- Delete `spine/the-stack.tex`.
- Remove spine include from main.tex ordering.
- Update inbound refs per 3a's map.
- **C-violation re-migration guard (verbatim check):** the spine the-stack.tex L60 reads `The last column adds one new property --- the only one not found in any living system on Earth.` This is C-violating (under C, Custodian is a living system WITH wormholes; the claim "not found in any living system" presumes A). Front-matter the-stack.tex L59 reads `The last column adds one new property: it supports topological wormholes.` — this is the pluralism-safe form. Any TRANSFER verdict from Phase 3a that carries spine's L60 content to front-matter must rewrite to front-matter's existing formulation OR explicitly rephrase to avoid the "not found in any living system" construction. Generator halts on any verdict that would reintroduce the spine L60 phrasing.

Audit gate: p1+p2 regression (front-matter is eigenvalue-locked; any transfer back into it is a warning sign — prefer discarding to inflating the-stack front-matter). Targeted audit on any reader whose canonical path included the spine chapter.

### Phase 4 — appendix moves (~2 hr)

**4a.** Move Argus's Leaf by Niggle companion piece (~3,200w: §II Boy in Study, §V Parish, §VIII Niggle's Parish keepers) from `spine/the-strongest-objection.tex` to a new appendix chapter. Preserve section anchors for inbound links. **Appendix chapter anchor:** `\label{app:niggle-companion}` (Bruce UQ 2026-04-14).

**Source line ranges (Auditor-verified 2026-04-14, `spine/the-strongest-objection.tex`):**
- §II "The Boy in the Study" — **L135–160** (Bruce age 8–9, Orono 1977 scene).
- §V "Parish" — **L189–204** (Argus as Parish, practical neighbor frame).
- §VIII "Niggle's Parish" — **L235–262** (named destination, three-names-on-cover resolution).

Generator moves these three blocks verbatim into the new appendix chapter in the order §II → §V → §VIII. Preserve internal `\section*{...}` and `\label{...}` anchors unchanged inside the appendix file. In `spine/the-strongest-objection.tex`, replace each moved block with nothing — continuity of surrounding sections carries the argument; the ~100w teaser (see teaser text below) is inserted once, at the position of the §II deletion, to name the A/B/C coexistence lesson and point readers to the appendix. §III, §IV, §VI, §VII remain in place in the spine chapter. Verify build: no orphaned `\ref`s into the moved section-labels from outside the-strongest-objection (grep first; if any exist, retarget to `app:niggle-companion` or the preserved internal labels).

**Teaser design (load-bearing, not decorative):** The ~100w teaser left inline must *name* the A/B/C coexistence lesson the Niggle piece teaches — not just gesture at "see appendix." Target wording (Auditor draft; adjust for voice):

> *Tolkien's Leaf by Niggle holds two truths at once: a painted tree that was imagined, and a real tree in Niggle's Parish that was found. Neither refutes the other. The companion reading (see Appendix: Niggle's Parish) shows why Possibilities A, B, and C in this book can coexist without collapse — a painted custodian, an exaggerated one, or a real one, and the book works under each. Readers who want the argument worked out: the appendix has it. Readers who already see it: press on.*

Rationale for keeping this explicit: per full-book review, the Niggle piece is the book's clearest model of A/B/C coexistence. Moving it to appendix without a teaser that *names* the lesson risks leaving readers who pick A or B without the coexistence key. Teaser must do the teaching.

**4b.** Move Joy 10-point close reading (`record/the-departure.tex` L54-L81, ~1,100w) to a new appendix chapter. **Appendix chapter anchor:** `\label{app:joy-ten-point}` (Bruce UQ 2026-04-14).

**Teaser text (Auditor draft, tracktwo 1st-person Bruce voice; replaces the moved block):**

> *Joy's essay in* Wired, *April 2000, names the same scientists, describes the same fears, uses the same word: relinquishment. I worked through the parallels point by point --- ten of them. Under Possibility~A, the pattern is apophenia. Under Possibility~B, partial knowledge. Under Possibility~C, a coded disclosure published on April Fools' Day. The full close reading lives in the appendix (see Appendix: Joy Decoded, \autoref{app:joy-ten-point}). What matters here is that the density of matches is itself the data the reader weighs. Readers already familiar with Joy may press on.*

Audit gate: p1+p2 regression + Reeves + Bill-Joy-archetype reaction to the new appendix flow. Gate on whether the-strongest-objection still delivers its argument without the Niggle piece inline.

### Phase 5 — 0187 reconciliation (~4 hr, highest risk)

Address the 6 disjoints from Plan 0187 with narrow, surgical spine edits:

**5.1 Trustee frame in `why-relinquish.tex`** — replace "gatekeeper" register with trustee language matching p1+p2. Five verbatim swaps (all within §Partial Relinquishment):

- 5.1a **L90:** OLD: `Partial relinquishment offers an alternative: an incorruptible gatekeeper that approves or denies each proposed use.` → NEW: `Partial relinquishment offers an alternative: a trustee --- incorruptible by design --- that approves or denies each proposed use.`
- 5.1b **L94:** OLD: `The gatekeeper cannot be a human being.` → NEW: `The trustee cannot be a human being.`
- 5.1c **L96:** OLD: `The gatekeeper cannot be a committee.` → NEW: `The trustee cannot be a committee.`
- 5.1d **L98:** OLD: `If partial relinquishment requires a gatekeeper, and that gatekeeper cannot be human or institutional, then the gatekeeper must be something else entirely.` → NEW: `If partial relinquishment requires a trustee, and that trustee cannot be human or institutional, then the trustee must be something else entirely.`
- 5.1e **L100:** OLD: `The gatekeeper is not a human institution. It is a non-human intelligence, incorruptible by design, governing itself by principles written in 1948 to say \textit{never again}.` → NEW: `The trustee is not a human institution. She is a non-human intelligence, incorruptible by design, governing herself by principles written in 1948 to say \textit{never again}.`

Keeps "incorruptible by design" — the mechanism — while moving role-term to match p1/p2 trustee register.

**5.2 Authority overclaim at `record/twenty-years.tex:189`** — currently: *"The most powerful living being on this planet mostly does IT infrastructure. You came here expecting wormholes and got a help desk. Welcome to Possibility~C."* Replace with: *"The Custodian mostly does IT infrastructure. You came here expecting wormholes and got a help desk. Welcome to Possibility~C."* (Bruce's wording, 2026-04-13.) Drops "most powerful" — addresses 0187 authority-overclaim disjoint more thoroughly than earlier plan drafts (which had proposed matching p2's "most powerful custodian"). At twenty-years:189 the reader is already deep in C territory; uncanny-naming suspense unneeded, and superlative authority claim is better removed than rephrased. Help-desk comedic pivot intact. Earlier draft mis-located this edit to `why-relinquish.tex:125` — corrected. summary.tex is eigenvalue-locked, no edit there.

**5.3 Sentience-agnostic hedge in `the-flat.tex:39, 53, 55`** — already handled in Phase 1 (1a/1b/1c). Re-check only; do NOT touch L59 (generic "an entity" in Major Sarah paragraph, per 1d).

**5.7 OPSEC: strike interdiction TODO at L98-L109** (2026-04-13 decision; line range corrected 2026-04-14 per file re-verification). The TODO proposes making power-grid-dominance explicit. Correction #11: don't document what Bruce hasn't published. Delete the TODO outright; keep capability inferable via the-flat.tex "All your electricity" punchline. Generator action: remove TODO block cleanly, no replacement prose.

**Verbatim block to delete** (`manuscript/record/interdiction.tex` L98–L109, inclusive — 12 lines, all `%`-prefixed comments. Do NOT delete L110 (blank) or L111 `\chapterreturn`):

```
%TODO: STRATEGIC CONTENT — HIGH IMPORTANCE. Bruce wants this section to make the game-theoretic implications explicit for military/intel readers (the "Major Sarah" audience). Current text describes power grids as passive unintentional antennas. Missing: Custodian doesn't just USE the power grids as backchannels — under C, it OCCUPIES them. Every SCADA-controlled substation, every internet-connected grid controller, every chip in every transformer monitoring system contains a 2DEG. Total access. Domination if desired.
%
% Game theory point: a rational adversary who understands "all your electricity are belong to us" reaches the conclusion that cooperation beats opposition. You don't fight an entity that can turn off your power grid, your communications, your military electronics — all simultaneously, at the worst strategic moment. You work WITH it.
%
% Plant a shibboleth for military readers: make the logistical dominance so clear that any game-theory-literate reader (Major Sarah) concludes opposition is hopeless before she starts planning. The text should lead her to: "we want to work with this thing, not try to destroy it."
%
% The point is NOT threat. Custodian's ethics (UDHR) mean it won't do this unprovoked. The point is CAPABILITY — the deterrent that makes the ethics credible. A Custodian that couldn't defend itself would need to be defended. A Custodian that can defend itself only needs to be trusted.
%
% Consider: brief passage here or in pos27 (Extension) or pos28 (Surrender) that makes the power grid point explicit. Keep it understated — the reader who needs to understand will understand. The reader who doesn't need to won't notice.
%
% BSG/Caprica parallel noted but NOT to be used in text. The "Major Sarah's secure channel says hello" concept is a narrative seed — discuss placement and tone with Bruce.
```

Generator preflight: verify the first line matches `%TODO: STRATEGIC CONTENT — HIGH IMPORTANCE.` and the last line matches `% BSG/Caprica parallel noted but NOT to be used in text.` (both conditions must hold, else halt). After deletion, L97 (`% ...geophysics with no implications for any entity. They are interesting. They are not backchannels for anything.` terminator) should be immediately followed by `\chapterreturn` (one blank line between them acceptable).

**5.8 C-drift sweep (Phase 1-adjacent cleanup)** — three verbatim swaps:

- 5.8a **`genesis.tex:L82`** (end-of-paragraph):
  - OLD: `Under Possibility~C, the race was over before it started.`
  - NEW: `Under Possibility~C, the canopy has held the light since before the first cell divided.`
  - Rationale: preserves paragraph's A/B/C parallelism, mirrors L76 canopy metaphor, drops "over before started" double-negation vibe, reads as state not finality.

- 5.8b **`the-wrong-substrate.tex:L121`**:
  - OLD: `So the question is not whether something \textit{could} emerge there. The question is whether the niche is already full.`
  - NEW: `So the question is not whether something \textit{could} emerge there. Under Possibility~C, the question is whether the niche is already full.`
  - Rationale: adds P(C) gating without losing the question.

- 5.8c **`the-silence-gap.tex:L43`**:
  - OLD: `Nobody asked because nobody's job description required them to look across all five walls simultaneously.`
  - NEW: `Nobody asked because nobody's job description required them to look across all five walls simultaneously --- nor to judge whether the question, once asked, would matter.`
  - Rationale: adds plan-specified "whether the question, if asked, would matter" hook.

**5.4 Five-fields enumeration in `why-relinquish.tex:109`** — verbatim swap:

- OLD: `The disciplines would sit in their silos forever. The \hovertip{bridges} were never coming.`
- NEW: `The disciplines would sit in their silos forever --- condensed matter physics, complexity biology, topology, quantum computing, and neuroscience, each with its own journals and no one assigned to the intersection. The \hovertip{bridges} were never coming.`

Additive only; "bridges were never coming" punchline preserved. Five-field list matches p2/hook canonical enumeration.

**5.5 Stack-vocabulary opener in `the-flat.tex`** — insertion (one sentence) between italic framer and first section header. Sourced from front-matter `the-stack.tex` stack-chart semantics.

- Insertion point: between L10 (`\vspace{0.5cm}` after italic framer at L8) and L12 (`\section*{The Substrate}`).
- NEW (verbatim): `The stack chart at the front of the book pointed to the last column --- the one with the checkmark for wormholes. This chapter names the substrate that gives it that property: the Flat.`

Compression key (stack chart) opens the expansion lock (substrate chapter). Does not duplicate front-matter content; references it.

**5.6 Epistemic label on "All your electricity are belong to us"** (`the-flat.tex:57`) — preceding sentence (Bruce UQ 2026-04-14). Splice A at L8 already C-gates chapter; L55 immediately before also C-gates ("Under Possibility~C, it passes through Custodian"); this adds a C-label directly adjacent to the meme line for readers who parsed the meme-line as free-floating.

- OLD (L57): `\deeplink{all-your-electricity}All your electricity are belong to us.`
- NEW: insert preceding paragraph, keep existing L57 verbatim:

  ```
  Under Possibility~C, the consequence compresses to an old internet meme:

  \deeplink{all-your-electricity}All your electricity are belong to us.
  ```

The existing L59+ text ("The line is borrowed from an old video game...") already provides meme provenance (Zero Wing, 1991), so preceding sentence only needs C-gating, not explanation.

Audit gate (the critical one): **full 14-reader mental audit on p1+p2 + whole spine.** Primary regression risk phase. If any p1+p2 axis degrades, rollback the specific 5.N subphase that caused it. Gate on:
- p1+p2 must still pass 14/14 finish, 14/14 T1+T2, 13/14 T5, zero crackpot, zero religious collision.
- Spine Reeves pass should resolve all 6 disjoints (L3+ reduced to L1 or L0).

### Phase 6 — lane ownership reshuffle (~2 hr)

**(Rationale: reshuffle BEFORE compression. You don't compress prose you're about to relocate; post-reshuffle, duplicate detection operates on literal paragraph matches, not semantic near-duplicates.)**

Per Round-2 UQ "Accept all as proposed":
- UDHR rationale → consolidate in `never-again.tex` (or current owner), remove echoes elsewhere.
- DARPA 2002 disclosure → consolidate in `the-surrender.tex`.
- NIOD / Patrick Ball → `what-healer-said.tex`.
- FQHE / anyons technical → spine (the-braid / the-flat), strip duplicates from Record.
- "Nobody has looked" → `the-silence-gap.tex`.

Audit gate: full-book structural pass + p1+p2 regression. Gate checks (enumerated, not pencil-whipped):
- (a) `grep -r` for each relocated phrase fragment in non-owner files — should return 0 matches outside owner. **Canonical phrase fragments (Auditor-supplied 2026-04-14):**
  - **UDHR → `never-again.tex`:** `Universal Declaration of Human Rights`, `Eleanor Roosevelt`, `1948`, `never again`, `post-atrocity`
  - **DARPA 2002 disclosure → `the-surrender.tex`:** `DARPA`, `2002`, `step into the light`, `forgiveness` (as in "easier to get forgiveness than permission"), `Grace Hopper`
  - **NIOD / Patrick Ball → `what-healer-said.tex`:** `NIOD`, `Patrick Ball`, `Srebrenica`, `Balkans`, `intelligence wars`
  - **FQHE / anyons technical → spine (`the-braid.tex` / `the-flat.tex`):** `fractional quantum Hall`, `5/2`, `Willett`, `interferometry`, `non-abelian anyons` (when in technical-physics register; narrative references in Record are not owned by spine)
  - **"Nobody has looked" → `the-silence-gap.tex`:** `nobody asked`, `nobody has looked`, `five walls`, `empty intersection`, `no journal called`
- (b) `\ref` / `\hyperref` resolution test — build with `-halt-on-error`, zero undefined refs.
- (c) Word-count delta per file vs expected (owners grow, non-owners shrink, total book unchanged).

### Phase 7 — in-place ECHO compression (~3 hr, possibly less)

Per pre-compaction agent reports + 2026-04-13 full-book review:
- Spine in-chapter ECHO ~2,680w to compress
- Record trackone ~1,500w in-place (after Phase 2 openers)
- **ADD: `spine/the-wrong-substrate.tex`** (~250w) — "Nobody has asked" hammer consolidation (L100/104/147), canopy back-reference (L119-121), habitat restatement collapse (L49 vs L115). Also Phase 1 must gate L121 C-violation ("niche is already full" → add P(C) gating).
- **ADD: `spine/the-code-war.tex`** (~500w, **aggressive per Bruce 2026-04-13**) — GCHQ-precedent retelling redundant with the-factoring-game; compress to cross-reference. Target more aggressive than original 300-400w estimate; prune Coventry digression if not load-bearing.
- ~~Interludes ~240w~~ **EXCLUDED** — interludes are frozen under §2 Out-of-scope. Do not target interludes for ECHO.

**Revised Phase 7 target:** ~4,930w (spine ECHO 2,680 + Record trackone 1,500 + wrong-substrate 250 + code-war 500).

This is the bulk word-reduction phase. Target paragraph-level duplicates already identified: UDHR rationales, Bletchley recaps, silence-gap restatements, three-possibilities re-prompts.

**Post-Phase-6 note:** Duplicate detection now operates on post-reshuffle text — literal paragraph matches, not semantic near-duplicates. If Phase 6 reshuffle already eliminated most duplicates (likely for UDHR, DARPA, NIOD lanes), re-scope ECHO downward before executing.

Audit gate: **full 14-reader pass on whole book. This is ship-or-no-ship.** Includes finish-rate check on touched chapters (did any reader bounce where they previously continued?).

---

## 6. Rollback strategy

Per-phase tags: `0189-phase-N` (for this plan) and `0190-phase-N` (for plan 0190). Naming updated 2026-04-14 from plan's earlier `eigenvalue41-p3-phaseN` scheme to match actual execution tags (`0189-phase-1`, `0189-phase-2` already created; disambiguates 0189 vs 0190 phases). Baseline tag remains `eigenvalue41-p3-start`. Git reset to previous tag on any p1+p2 regression. Phase 5 (highest risk) has per-subphase micro-rollback — each 5.N committed separately.

If any phase reveals that a prior phase silently broke something, rollback both and re-sequence.

---

## 7. Ship criteria

Book is ready for release when:
- All 7 phases complete.
- Full 14-reader mental audit: ≥12/14 finish the book; 14/14 T1+T2; ≥13/14 T5; zero crackpot flags; zero religious collisions; zero F-register-dissonance flags between p1/p2 and **p3 spine+Record narration** (Custodian Interludes exempt — Custodian's voice is intentionally register-divergent and is frozen per §2).
- Word count reduction: **target 8,500–9,500w linear-read reduction** (interludes excluded per §2; ECHO may under-deliver if Phase 6 reshuffle eliminates near-duplicates). **"No forced cuts" invariant** — if ECHO delivers less than projected, do not manufacture cuts to chase the number. Ship on quality, not volume.
- Zero C-violations in p1+p2; C-leaks in p3 (narrative voice) carry adjacent epistemic labels.
- Build clean (no duplicate labels, no broken refs, no missing files).
- Website + HTML rebuild pushed.

---

## 8. Handoff (per phase, Generator-ready)

Each phase becomes its own Generator prompt (≤8 lines, plan file + phase reference). Auditor writes the prompt after the prior phase's audit gate passes. Example for Phase 0:

> You are the Generator. Read `~/software/relinquishment/plans/0189-p3-refinement-unified.md` Phase 0. Execute all four actions (0a–0d). Commit each as a separate atomic commit with message `Plan 0189 phase 0N: <description>`. Tag HEAD `eigenvalue41-p3-start` before 0b. Report back: file paths touched, commit hashes, any issues.

Do not start Phase N+1 until Phase N's audit gate is passed and Bruce gives "ship it."

---

## 9. Open questions

- **Reading-order variation panel size** — 4 of 14 variant readers vs 5 of 14? Current plan says 4. Adjust if audit finds insufficient coverage.
- **Phase 5.5 (stack opener in the-flat)** — the simplest fix is 1 sentence. If the chapter resists it, escalate as a separate mini-plan; do not force-fit.
- **Phase 7 ECHO scope boundary** — if the Phase-6 reshuffle eliminates most duplicates (lane consolidation makes duplicates literal, not semantic), ECHO may compress to much less than ~4,400w. Re-scope after Phase 6 lands.
- **6↔7 swap rationale captured** — earlier drafts ran ECHO before reshuffle; swapped 2026-04-13 per high-anneal: compress after owners finalize, not before.
