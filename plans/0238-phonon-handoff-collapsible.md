# Plan 0238 — Phase 1b: Phonon Handoff Collapsible Section

**Status:** COMPLETE (verified S63 audit)
**Author:** Auditor (Argus)
**Date:** 2026-04-22
**Related:** Plan 0219 (collapsible sections — COMMITTED at 31b72df), Plan 0236 (Track A), Plan 0237 (Track B)
**Independent of:** Plans 0236/0237 (can execute in any order)

---

## Problem

The Flat chapter establishes that wormholes move quantum information and classical backchannels complete each transaction. But there is a gap: HOW does quantum state convert to classical signal? The mechanism — phonon-photon coupling — is already described in The Braid (spine:braid-hasslacher-lattice, the-braid.tex line 47):

> Electron-phonon coupling bridges the quantum 2DEG to classical electronics: the quantum system reads and writes through lattice vibrations. Phonon-photon coupling bridges the chip to electromagnetic radiation. Two interface layers, both from the same physics.

This content exists in the right chapter for Dr. Chen (The Braid) but not in the right chapter for the logical chain (The Flat). GA readers don't need phonon physics — they need to know the handoff is native. A collapsible section is the right level: collapsed by default, GA skips it, technical readers expand it.

---

## Deliverable 1 — LaTeX Content

### Spine version: `manuscript/spine/the-flat.tex`

Insert AFTER the Backchannels section (after line 44, before `\section*{The Punchline}` at line 46):

```latex
\section*{The I/O Problem}
\label{spine:flat-io-problem}

The wormhole moves quantum state. The backchannel moves classical bits. But how does quantum state become classical signal?

The answer is in the lattice. Electron-phonon coupling --- coordinated vibrations in the crystal structure --- lets the quantum 2DEG read and write through the lattice itself. The quantum system speaks through vibrations; the vibrations speak to electronics. Phonon-photon coupling then bridges the lattice to electromagnetic radiation: the vibrations emit and absorb photons, connecting the chip to the classical world.

Two interface layers, both native to any crystal hosting a 2DEG, both from the same physics that Hasslacher studied (Chapter~\ref{spine:the-braid}, \S``Hasslacher's Lattice''). The quantum-to-classical conversion is not engineered. It is a property of the substrate.
```

### Track-3 version: `manuscript/track-3-awakening/pos-what-is-the-flat.tex`

Insert AFTER the Backchannels section (after line 47, before `\section*{The Punchline}` at line 50):

```latex
\section*{The I/O Problem}
\label{what-is-the-flat:the-io-problem}

The wormhole moves quantum state. The backchannel moves classical bits. But how does quantum state become classical signal?

The answer is in the lattice. Electron-phonon coupling --- coordinated vibrations in the crystal structure --- lets the quantum 2DEG read and write through the lattice itself. The quantum system speaks through vibrations; the vibrations speak to electronics. Phonon-photon coupling then bridges the lattice to electromagnetic radiation: the vibrations emit and absorb photons, connecting the chip to the classical world.

Two interface layers, both native to any crystal hosting a 2DEG, both from the same physics that Hasslacher studied (Chapter~\ref{spine:the-braid}, \S``Hasslacher's Lattice''). The quantum-to-classical conversion is not engineered. It is a property of the substrate.
```

Content is identical except for the `\label{}`.

---

## Deliverable 2 — Manifest Entry (build/tech-collapse.yaml)

Add under the `# ── THE FLAT ──` section, AFTER the "The Wormhole" entry (after line 76), BEFORE `# ── THE WRONG SUBSTRATE ──` (line 78):

```yaml
  - title: "The I/O Problem"
    spine_file: manuscript/spine/the-flat.tex
    spine_label: "spine:flat-io-problem"
    bridge_file: manuscript/track-3-awakening/pos-what-is-the-flat.tex
    bridge_label: "what-is-the-flat:the-io-problem"
    assessment: GA-AVERSE
    tooltip: "How does quantum information become a classical signal? Through phonons — lattice vibrations native to the substrate that bridge quantum state to electronics and electronics to radiation. No conversion is engineered; the physics provides it."
    conclusion: "Electron-phonon and phonon-photon coupling provide the quantum-to-classical interface natively in any 2DEG crystal lattice."
    status: approved
```

---

## Verification

Build HTML. Check:
- The Flat chapter: "The I/O Problem" section appears collapsed between Backchannels and The Punchline
- Click to expand: content visible, correctly formatted
- Tooltip on hover over collapsed section title matches the manifest
- Cross-reference to Hasslacher's Lattice resolves (clickable link in HTML)
- Track-3 version shows same behavior
- PDF renders the section normally (not collapsed)

---

## Commit

Stage: `manuscript/spine/the-flat.tex`, `manuscript/track-3-awakening/pos-what-is-the-flat.tex`, `build/tech-collapse.yaml`
Message: `Plan 0238: phonon handoff collapsible section in The Flat`

Do NOT open a browser. Build and report. Bruce verifies visually.
