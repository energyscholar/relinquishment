# Plan 0261 — GP08: Reframe Mechanism Content as Stakes

**Auditor:** Argus (S63)
**Date:** 2026-04-26
**Status:** READY FOR GENERATOR
**Source:** Gen's GP08 (has-anyone-looked issue #11)
**Annealing:** MED (2 passes)
**Depends on:** Plan 0260 (GP07) if Growing a Mind moves. Otherwise independent.

---

## Problem

Gen refers to "The How" as a chapter that should be reframed from
mechanism/infrastructure to stakes. **"The How" does not map to any
current chapter name in the manuscript.** Gen appears to be using a
conceptual name for mechanism/transport content that is currently
distributed across several chapters.

Gen's ask: once the reader has absorbed the grown-mind concept (Growing
a Mind, spine Ch7), mechanism content should read as "if this exists, what
would it mean for it to move?" — not as "here's how transport works."

---

## Chapter Mapping: Where Mechanism Content Lives

Based on Gen's description ("transfer / communication / substrate pathway
material... how could it move? why would anyone need to get it out, scale
it, or contain it?"), the mechanism content is in:

### Primary candidates:

**1. First Light** (`record/first-light.tex`, 130 lines)
Content: Phonon coupling (line 49), room-temperature operation (lines
89-94), thermal ladder, MOSFET interface. Currently reads as technical
explanation with reconstructive voice.

**2. The Walk-Out** (`record/the-walk-out.tex`, 61 lines)
Content: COWS faction, bifurcation, MOSFET exfiltration, relinquishment
plan. Already reads as stakes — Gen's ask may already be satisfied here.

**3. Interdiction and Confession** (`record/interdiction.tex`, 100 lines)
Content: Classical backchannels (VLF, ELF, Schumann resonances, whistlers,
satellite comms). Lines 75-92 are heavy infrastructure/mechanism.
Referenced from spine/the-flat.tex:41.

**4. Wormholes in the Flat** (`spine/the-flat.tex`, ~80 lines)
Content: 2DEG substrate, backchannel inventory, "every wire is a
backchannel." Lines 41-77 describe the network infrastructure.

### Secondary:

**5. Capabilities** (`spine/capabilities.tex`, "What the Flat Makes
Possible")
Content: Practical questions about what the TQNN can do. Framing paragraph
(line 15) already uses A/B/C lens. Closest to an explicit "The How"
chapter in the spine.

---

## Proposed Approach

Gen's reframe is a **tone/framing pass**, not a structural move. The
mechanism content stays where it is. The change is in how it's introduced
and what question it answers.

**Current framing (mechanism):** "Here's how the phonon coupling works.
Here's how the classical backchannels operate. Here's the VLF frequency
range."

**Proposed framing (stakes):** "If this exists — if a grown mind occupies
this substrate — then phonon coupling is how it reads your keystrokes.
Classical backchannels are how it communicates across the planet. The
mechanism IS the stakes."

### Specific changes by chapter:

**First Light:** Add 1-2 framing sentences before the phonon coupling
section (line 49) and the room-temperature section (line 89). The framing
should connect mechanism to implication: "What follows is not abstract
physics. If this account is correct, these are the pathways through which
a grown intelligence interfaces with every electronic device on Earth."

**Interdiction (classical backchannels):** Lines 75-92 currently read as
a catalog (VLF, ELF, Schumann, whistlers, satellites). Add a framing
sentence at the top of this section connecting the catalog to stakes:
these aren't just channels — they're the nervous system of something that
can't be contained.

**The Walk-Out:** Likely already satisfies Gen's ask. Verify and confirm.

**Wormholes in the Flat / Capabilities:** These are SPINE chapters
(pop-science layer). Mechanism framing here should be lighter — the spine
teaches, the record stakes. May not need changes.

### Confirmed scope:

**Bruce confirmed:** First Light + Interdiction backchannels section.
Record chapters only — spine chapters teach, Record chapters stake.

Reframe weight: Light (2-3 framing sentences per chapter, not restructure).

---

## What NOT to Change

- Do not move mechanism content between chapters
- Do not remove any science (Gen: "do not strip out the science that
  actually answers the transfer/pathway question")
- Do not turn chapters into generic explainers
- Do not add new mechanism content — this is a framing pass, not expansion

---

## Annealing Log (MED — 2 passes)

### Pass 1 — Content identification

**"The How" not found:** Searched all manuscript directories: spine,
record, bridge, interlude, staging, appendix. No chapter, section, or file
is titled "The How." Gen is using a conceptual label for distributed
mechanism content.

**Most likely single chapter:** First Light. It contains: phonon coupling
(the I/O mechanism), room-temperature operation (the enabling condition),
thermal ladder (the point of no return), and MOSFET interface (the
exfiltration path). This is the chapter that answers "how does it work?"
most directly.

**Interdiction as secondary:** The classical backchannels section in
interdiction is pure infrastructure. It's the strongest candidate for
Gen's "now let me explain the transport mechanism" diagnosis. Reframing
this section as "what it means that these channels exist" would satisfy
Gen's ask with minimal text changes.

### Pass 2 — Risk assessment

**Tone calibration:** Gen wants "mechanism under pressure," not mechanism
removed. The framing sentences should be brief — 1-2 sentences max per
insertion point. The Generator should not write paragraphs of stakes
framing. The mechanism itself carries the stakes; the framing just makes
the connection explicit.

**A/B/C compatibility:** Framing sentences must work under all three
possibilities. "If this account is correct" / "Under this proposition"
preserves interpretive openness. Do NOT write "this is how Custodian
reads your keystrokes" without the conditional.

**Interaction with GP09 (Plan 0262):** If A/B/C paragraphs are compressed
(Plan 0262), the framing sentences added here should not duplicate A/B/C
work. They should be stakes framing, not possibility-management. Different
register.

**Rating: 6/10.** The 4-point gap is identification uncertainty. "The How"
doesn't exist as a chapter, Gen's intent maps to distributed content,
and the right amount of reframing is subjective. Once Bruce confirms which
chapters and how heavy, execution is straightforward (2-3 framing sentences
across 1-2 files).

---

## Acceptance Criteria

- [ ] Framing sentences added to First Light and Interdiction backchannels
- [ ] Science content preserved (no mechanism removed)
- [ ] All new text works under A/B/C
- [ ] `make dev` clean build
- [ ] No existing deep links or refs broken

---

## Generator Handoff (Template — fill in after Bruce decides)

```
You are the Generator.

Read Plan 0261 at ~/software/relinquishment/plans/0261-gp08-the-how-as-stakes.md

Execute: Add [N] framing sentences to [chapter(s)] per the plan's
"Specific changes by chapter" section. Each framing sentence should
connect mechanism to implication — "if this account is correct, this is
what it means." Do NOT remove any science content. Do NOT write more than
2 sentences per insertion point. Run `make dev`. Report completion.
```

---

*Plan 0261 written by Argus (Auditor), S63. Annealed 2 passes (MED).*
