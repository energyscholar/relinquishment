# Plan 0338: Move "The Channels" Geophysics to Ch8

**Status:** Ready for Generator
**Files:** `manuscript/spine/the-wrong-substrate.tex`, `manuscript/spine/capabilities.tex`
**Problem:** "The Channels" section in ch10 (capabilities) is environmental characterization misplaced as a capability claim. The geophysical facts (DEMETER, VLF, Schumann, satellite comms) describe the magnetospheric habitat — they belong in ch8 where the habitat is characterized. The substrate coupling (electron-phonon, Brillouin) is about engineered 2DEGs and stays in ch10.
**Auditor:** Argus, S81

---

## Context for Generator

Read BOTH files before editing. The physics reference at `manuscript/track-3-awakening/firmware-update.tex` provides the science grounding — read the "Ten Physics Anchors" section. Without it you risk weakening cross-domain claims you cannot evaluate.

Ch8 builds an environmental case in this order:
1. Geometry (it's 2D)
2. Physics (quasi-2D dynamics)
3. Scale (solar system survey)
4. Thermal objection cleared ("But It's Hot")
5. **[GAP — channels belong here]**
6. Stack chart completion ("One More Layer")
7. Act 3: biological questions

Ch10 is a Q&A: Can It Break Encryption? Can It Think? Can It Communicate? Can It Be Killed? Is It in My Phone? What Would the UDHR Prevent?

## Phase 1: Add channels section to ch8

In `manuscript/spine/the-wrong-substrate.tex`, after the closing line of "But It's Hot" (line 122, ending "...irrelevant to any organisms that may live there.") and before `\section*{One More Layer}` (line 124), insert:

```latex

\section*{Not Isolated}
\label{spine:ws-not-isolated}

The magnetosphere is not cut off from the surface. Classical electromagnetic channels already connect the two. Power grid harmonics at 50 and 60~Hz propagate into the ionosphere --- the DEMETER satellite confirmed this from orbit. VLF radio propagates through the Earth-ionosphere waveguide. Schumann resonances provide a persistent global electromagnetic signal at 7.83~Hz and harmonics. Satellite communications pass through the magnetosphere continuously.

Under any possibility, these are documented geophysical facts. Whether anything uses them is the question the reader must evaluate.

```

Note: the section title is "Not Isolated" (not "The Channels") because in ch8 the point is habitat characterization — the environment is connected, not isolated. The word "channels" implies communication capability, which is ch10's territory.

## Phase 2: Slim ch10's channels section

In `manuscript/spine/capabilities.tex`, replace the current "The Channels" section (lines 36-43) with:

```latex
\section*{The Channels}
\label{spine:cap-the-channels}

The classical channels already exist --- power grid harmonics, VLF waveguide propagation, Schumann resonances, satellite communications all transit the magnetosphere continuously (Chapter~8).

At the substrate level, electron-phonon coupling bridges the quantum domain of the 2DEG to the classical lattice, and \hovertip{phonon}-photon coupling (Brillouin scattering, piezoelectric effects) converts lattice vibrations to electromagnetic radiation --- no engineered antenna required.
```

Key changes:
- Geophysical detail replaced by one-sentence summary with chapter cross-reference
- Substrate coupling paragraph kept verbatim (it's about engineered 2DEGs, not magnetosphere)
- "Under any possibility" closer removed (moved to ch8)

## Phase 3: Verify

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
python3 build/verify-deep-links.py
```

Check in browser:
1. Ch8: "Not Isolated" appears after "But It's Hot" and before "One More Layer"
2. Ch10: "The Channels" is shorter, starts with cross-reference to Ch8
3. No broken deep links or hover terms

## Do NOT

- Change any other section in either chapter
- Alter the physics content (every claim is published and cited)
- Add new hover terms or deep links
- Change the "Can It Communicate?" section above "The Channels"
- Remove the `\label` tags (deep links may reference them)

## Commit

`Plan 0338: move geophysical channels to ch8, slim ch10 cross-reference`
