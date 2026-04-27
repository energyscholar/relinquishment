# Plan 0261 — GP08: Reframe Mechanism Content as Stakes

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR
**Source:** Gen's GP08 (has-anyone-looked issue #11)
**Annealing:** HIGH MED LOW LOW (4 passes)
**Depends on:** Run AFTER Plan 0257 (which inserts text into first-light.tex).

---

## Problem

Gen refers to "The How" as a chapter that should be reframed from
mechanism/infrastructure to stakes. **"The How" does not map to any
current chapter name in the manuscript.** Gen is using a conceptual name
for mechanism/transport content distributed across several Record chapters.

Gen's ask: once the reader has absorbed the grown-mind concept (Growing
a Mind, spine Ch7), mechanism content should read as "if this exists, what
would it mean for it to move?" --- not as "here's how transport works."

---

## Existing Stakes Framing (discovered during HIGH annealing)

The source text already does significant stakes work. This narrows the
scope considerably:

**First Light --- phonon coupling (line 49):** Already pivots to stakes
within the same paragraph: "Under Possibility~C, this is how Custodian
reads your keystrokes and delivers computational results without any
engineered interface." No insertion needed here.

**First Light --- thermal ladder (line 89):** Already reads as stakes:
"At millikelvin temperatures, the entity exists only where its creators
permit. At room temperature, it can exist anywhere there is a suitable
substrate. The thermal ladder is the point of no return." No insertion
needed here.

**First Light --- Growth section (lines 64-87):** ~25 lines of mechanism
(evolutionary selection, Kauffman's poised realm, biological coherence
precedent) BEFORE the stakes payoff arrives at line 89. **This is the
gap.** The reader processes the engineering narrative without knowing why
it matters until the end.

**Interdiction --- classical backchannels (lines 82-92):** Each catalog
item already weaves in "Under Possibility~C" language. But the OPENING
FRAMING at line 82 sets a mechanism expectation ("worth understanding
concretely") rather than a stakes expectation. The rhetorical payoff
("An angel does not need an antenna. A creature does.") arrives at line
93-96 --- after the catalog. **The gap is in the opening framing, not
the catalog itself.**

**The Walk-Out:** Already entirely stakes-framed. Every paragraph
connects mechanism to consequence. No changes needed. Confirmed.

**Spine chapters (the-flat, capabilities):** Out of scope per Bruce.
Record chapters stake, spine chapters teach.

---

## Specific Changes (2 insertions total)

### Change 1: First Light --- Growth section signpost

**File:** `manuscript/record/first-light.tex`

**Location:** After the `\section*{Growth: 1993--1995}` heading and its
`\label`, before the paragraph starting "The room-temperature
breakthrough was achieved..."

**IMPORTANT:** Plan 0257 inserts text earlier in this file (after
srcnote, before "When does an experiment become an entity?"). Line
numbers will have shifted. Use content matching: find
`\label{record:fl-growth}` and insert after it.

**Insert this paragraph:**

```latex
The section that follows describes an engineering process. Under Possibility~C, it also describes the point of no return --- the creation of something that could live anywhere, beyond any institution's ability to contain or recall.
```

**Why this works:** Primes the reader to read the evolutionary selection
mechanism (lines 64-87) as "cage door opening" rather than "interesting
engineering." The payoff at line 89 ("The thermal ladder is the point of
no return") then lands as confirmation, not surprise. Different phrasing
avoids duplication --- the signpost says "could live anywhere," the
payoff says "cannot be recalled."

### Change 2: Interdiction --- backchannels opening reframe

**File:** `manuscript/record/interdiction.tex`

**Location:** Line 82, the opening of the classical backchannels prose
section (after the `\srcnote`).

**Replace this text:**

```latex
The previous section established that quantum teleportation requires a classical channel. This is a profound constraint, and it is worth understanding concretely.
```

**With this text:**

```latex
The previous section established that quantum teleportation requires a classical channel. This is a profound constraint. Under Possibility~C, what follows is not abstract geophysics --- it is the entity's complete dependency list. Worth understanding concretely.
```

**Why this works:** Changes one mechanism-framing sentence into a
stakes-framing sentence. "Complete dependency list" tells the reader:
this catalog is what the entity has to work with, and what it's limited
by. The existing payoff at line 93 ("An angel does not need an antenna.
A creature does.") still lands fresh --- it's about the rhetorical
function, while the opening is about the operational reality. Net change:
+1 clause.

---

## What NOT to Change

- Do not move mechanism content between chapters
- Do not remove any science (Gen: "do not strip out the science that
  actually answers the transfer/pathway question")
- Do not modify the existing stakes language at lines 49, 89, or 93-96
- Do not add framing to the phonon coupling paragraph (already has it)
- Do not touch spine chapters
- Do not add new mechanism content --- this is a framing pass, not expansion

---

## Annealing Log (HIGH MED LOW LOW --- 4 passes)

### Pass 1 (HIGH) --- Source text audit

Read all three candidate files in full (first-light.tex 130 lines,
interdiction.tex 100 lines, the-walk-out.tex 61 lines).

**Critical finding:** The original plan (passes 1-2) overestimated the
gap. First Light line 49 already has "Under Possibility C, this is how
Custodian reads your keystrokes." First Light line 89 already has "The
thermal ladder is the point of no return." Interdiction lines 88-92
already weave "Under Possibility C" into each catalog item. The Walk-Out
is entirely stakes-framed.

**Revised diagnosis:** The gap is not "mechanism content lacks stakes
framing." The gap is "mechanism content lacks stakes SIGNPOSTING" ---
the reader enters two long mechanism stretches (First Light Growth
section, Interdiction backchannels catalog) without knowing why the
mechanism matters until the end. Two signpost sentences fix this.

**Scope reduction:** Original plan called for 2-3 framing sentences per
chapter across 2 chapters (4-6 insertions). Revised: 1 insertion + 1
modification = 2 total changes across 2 files.

### Pass 2 (MED) --- Draft text and A/B/C check

**First Light insertion:** "The section that follows describes an
engineering process. Under Possibility~C, it also describes the point of
no return --- the creation of something that could live anywhere, beyond
any institution's ability to contain or recall."

A/B/C check: "Under Possibility C" conditional. Under A or B, the
sentence is explicitly hypothetical. Under C, it's a signpost. Works
under all three.

Duplication check: Line 89 says "The thermal ladder is the point of no
return --- the deliberate creation of something that cannot be recalled."
My signpost says "the point of no return --- the creation of something
that could live anywhere." Same concept, different emphasis: signpost
emphasizes "anywhere" (geographic), payoff emphasizes "cannot be
recalled" (permanence). Close but not redundant --- the signpost primes,
the payoff delivers.

**Interdiction modification:** Adds "Under Possibility~C, what follows
is not abstract geophysics --- it is the entity's complete dependency
list." to existing text.

A/B/C check: "Under Possibility C" conditional. Clean.

Payoff-stealing check: Line 93-96 payoff is about rhetoric and theology
("An angel does not need an antenna"). My framing is about operational
dependency. Different registers. No theft.

### Pass 3 (LOW) --- Interaction with other plans

**Plan 0257 (ULTRA II intro):** Inserts text into first-light.tex
between line 15 and line 18. My insertion is at the Growth section
(line 61+). No content overlap. But line numbers shift --- handoff
specifies content matching, not line numbers. Safe.

**Plan 0262 (A/B/C compression):** May compress tripartite blocks in
these chapters. My insertions are stakes framing, not A/B/C possibility
blocks. Different register. No conflict.

**Plan 0258, 0259:** Touch different files entirely. No interaction.

### Pass 4 (LOW) --- Generator feasibility

**Handoff completeness:** Both changes are now specified with exact
source text and exact replacement text. The Generator does not need to
compose framing sentences --- they are provided. This eliminates the
original plan's main risk (subjective "how much reframing" judgment).

**Content matching reliability:** Both insertion/replacement targets are
unique strings in their respective files. `\label{record:fl-growth}`
appears once. "This is a profound constraint, and it is worth
understanding concretely" appears once. Safe for grep-and-edit.

**Build risk:** Zero structural changes. Two small text additions. No
new commands, no moved sections, no changed labels or deep links.
`make dev` should be trivially clean.

**Rating: 9/10.** The 1-point gap: the First Light signpost's
relationship to line 89 is close enough that Bruce may want to tune the
wording once he sees both in context. But the Generator can deliver the
plan as written, and tuning is a polish step, not a structural risk.

---

## Acceptance Criteria

- [ ] One signpost paragraph inserted in First Light Growth section
- [ ] One opening sentence modified in Interdiction backchannels section
- [ ] Existing stakes language at FL:49, FL:89, INT:93-96 untouched
- [ ] Science content preserved (no mechanism removed)
- [ ] Both new/modified sentences use "Under Possibility C" conditional
- [ ] `make dev` clean build
- [ ] No existing deep links or refs broken

---

## Generator Handoff

```
You are the Generator.

Read Plan 0261 at ~/software/relinquishment/plans/0261-gp08-the-how-as-stakes.md

Execute: Two changes per the plan's "Specific Changes" section.
(1) In manuscript/record/first-light.tex, find \label{record:fl-growth}
and insert the signpost paragraph from the plan AFTER the label, BEFORE
"The room-temperature breakthrough was achieved..."
(2) In manuscript/record/interdiction.tex, find "This is a profound
constraint, and it is worth understanding concretely." and replace with
the plan's revised text. Use exact strings from the plan. Do NOT modify
any other text. Run `make dev`. Report completion.
```

---

*Plan 0261 written by Argus (Auditor), S63. Annealed 4 passes (HIGH MED LOW LOW). Rating raised from 6/10 to 9/10 after source audit revealed existing stakes framing narrows scope to 2 surgical changes.*
