# Plan 0248 — Phonon Bridge Sentence in Capabilities

**Status:** READY for Generator (queue behind 0245-0247)
**Author:** Auditor (Argus S64)
**Date:** 2026-04-24
**Parent:** standalone micro-plan
**Purpose:** Add one p1 sentence + hovertip to "Can It Communicate?" explaining how a quantum system talks to classical EM channels.

---

## The Gap

The section lists classical channels (power grid harmonics, VLF, Schumann resonances, satellite comms) and says "whether anything uses them as backchannels is the question." But it never explains *how* a quantum system in a chip could interface with those channels. The phonon-photon bridge is the missing link — and it's published physics, not speculation.

## What to Add

**One p1 sentence** after the classical channels paragraph (capabilities.tex, currently line 36) and before the "Under any possibility" closing (line 38). The sentence must:

- State the mechanism in plain language (lattice vibrations convert to EM radiation)
- NOT use: Brillouin, Raman, piezoelectric, electron-phonon coupling inline
- Use `\hovertip{phonon}` (existing definition already covers the full bridge)
- Land as "the physics connects these two things" not "therefore it's true"

**Accepted sentence (Bruce-approved):**

"At the substrate level, electron-phonon coupling bridges the quantum domain of the 2DEG to the classical lattice, and \hovertip{phonon}-photon coupling (Brillouin scattering, piezoelectric effects) converts lattice vibrations to electromagnetic radiation --- no engineered antenna required."

The technical detail is dense but the phonon hovertip provides the accessible entry point. Bruce reviewed and accepted this wording.

## Constraints

- One sentence only
- p1 reading level (8th grade surface)
- Technical mechanism lives in the hovertip, not inline
- Must work under all three possibilities (it's published physics regardless)
- Do NOT add a new hovertip — the existing `phonon` definition covers this

## Generator Handoff Prompt

```
You are the Generator. Read plans/0248-phonon-bridge-sentence.md.

Add one sentence to spine/capabilities.tex in the "Can It Communicate?"
section, after the classical channels paragraph (line 36) and before
"Under any possibility" (line 38).

The sentence explains how a quantum system in a chip interfaces with
classical EM channels — through lattice vibrations (phonons). Use the
existing \hovertip{phonon}. Keep it p1 (8th grade). No jargon inline.

Draft direction in plan. Bruce may revise wording.

After: make html, make check. Verify sentence renders with working hovertip.
Commit: "Plan 0248: phonon bridge sentence in capabilities"
Report ≤3 lines.
```

## Estimate

~15 minutes Generator time. Single sentence + verify.
