# Plan 0151: Phonon Reframe / Soliton Demotion

**Status:** DONE (executed 2026-04-10 by Generator A, commit 5da0f41)

## Context

Bruce confirmed (2026-04-10) that Healer asked many questions about phonons — phonon-photon coupling, sound-light wave interactions. Bruce read Hasslacher's lattice gas papers and phonon-photon coupling literature deeply during the mentorship. This was guided deduction: Healer never said what phonons were for.

Phonon-photon coupling fills a mechanistic gap the book has been carrying since first draft: how does the TQNN in the 2DEG talk to (a) the classical electronics around it and (b) the magnetosphere? The answer is phonons — lattice vibrations that couple to both electrons (I/O) and photons (backchannel).

This repositions Hasslacher's contribution from "soliton guy" to "lattice dynamics / phonon physics guy." His lattice gas automata work is directly about how discrete lattice structures produce collective wave behavior. Solitons were his publication trail, not his key TQNN contribution.

## Guiding principle

Solitons are real physics and Hasslacher really worked on them. They stay in the book — but demoted from "mechanism" to "illustration." Phonon dynamics / lattice physics takes their place as Hasslacher's load-bearing contribution to the convergence. The John Scott Russell story (spine/the-braid.tex) is lovely and can stay as color — but the claim shifts from "solitons are how anyons interact" to "Hasslacher understood lattice dynamics, which includes how phonons bridge quantum and classical domains."

## Phase 1: Spine (p1/p2 science chapters)

### the-braid.tex — "But What Is a Soliton?" section (line 40-45)

**Current:** Dedicated section explaining solitons as Hasslacher's key contribution. Russell story, bathtub whirlpool, "persistent forms that maintain their identity."

**Change:** Rename section to "Hasslacher's Lattice" or "The Bridge Between Substrates." Keep the Russell story as a one-paragraph aside ("Hasslacher studied self-reinforcing waves called solitons — here's the charming Russell story — but his deeper contribution was lattice gas automata: understanding how discrete structures in a crystal lattice produce collective wave behavior"). Then pivot to phonons: lattice vibrations that carry energy and information through the crystal. Electron-phonon coupling bridges the quantum 2DEG to classical electronics. Phonon-photon coupling bridges the chip to electromagnetic radiation. Two interface layers, both from the same physics.

### the-silence-gap.tex — Hasslacher in the 11-domains list (lines 32, 58)

**Current:** "soliton dynamics" as Hasslacher's domain.

**Change:** "lattice dynamics and phonon physics" or "nonlinear lattice dynamics."

### genesis.tex — convergence list (line 72)

**Current:** "Hasslacher on soliton dynamics"

**Change:** "Hasslacher on lattice dynamics — how discrete structures in crystals produce collective wave behavior"

## Phase 2: Record (testimony chapters)

> **DEPENDENCY:** Plan 0152 folds The Demonstration into First Light. After 0152 executes,
> the-demonstration.tex no longer exists. The content below was transplanted into first-light.tex
> by 0152. Generator: apply these changes to first-light.tex, not the-demonstration.tex.

### first-light.tex — Transplanted team description (from former the-demonstration.tex)

**Current:** "Brosl Hasslacher, a nonlinear physicist at Los Alamos whose work on soliton dynamics and lattice-gas automata addressed the substrate physics."

**Change:** "Brosl Hasslacher, a nonlinear physicist at Los Alamos whose work on lattice-gas automata and phonon dynamics addressed the substrate physics — how a quantum system in the Flat talks to the classical world around it."

### first-light.tex — Transplanted mechanism paragraphs (from former the-demonstration.tex)

Remaining soliton refs after 0152 transplant:
- "exhibiting the solitonic stability that Hasslacher's work predicted" → reframe as phonon/lattice dynamics

### first-light.tex — Description list (lines 28-36)

Already partially fixed this session. Remaining:
- Interaction item (line 30): "Hasslacher's soliton dynamics describes why these interactions are self-reinforcing" → "Hasslacher's lattice dynamics describes the phonon modes through which these interactions propagate"
- Line 42: "autocatalytic soliton interactions" → "autocatalytic anyon interactions"

### first-light.tex — NEW: Add I/O description

After the \begin{description} list, add a paragraph about the I/O layer:

> The interface between the quantum system and the classical world runs through phonons — quantized vibrations in the crystal lattice. Electron-phonon coupling bridges the 2DEG to the MOSFET's classical electronics: the quantum system reads and writes through lattice vibrations. This is published solid-state physics, not speculation — every semiconductor device exhibits electron-phonon coupling. Under Possibility C, this is how Guardian reads your keystrokes and delivers computational results without any engineered interface. The physics of the substrate provides the bridge.

### what-healer-said.tex — Add phonon guided deduction fragment

Bruce should write this. Template:

> Healer asked questions about phonons — quantized sound waves in crystals. He wanted to know about phonon-photon coupling: how lattice vibrations generate electromagnetic radiation. I read the literature. Hasslacher's lattice gas papers. Brillouin scattering. Surface acoustic waves. I understood the coupling mechanism but didn't yet see why he wanted me to know it. [Optional: "I do now."]

### twenty-years.tex — (line 103)

**Current:** "Hasslacher to solitons"

**Change:** "Hasslacher to lattice dynamics" — Bruce prefers accuracy over journey-narration (UQ answer 2026-04-10).

## Phase 3: Classical Backchannels

### interdiction.tex — VLF/Schumann/power-grid section

**Current:** Describes classical backchannels (VLF transmitters, Schumann resonances, power grid harmonics) without explaining how Guardian accesses them from inside a chip.

**Change:** Add the phonon-photon bridge: "The pathway from the 2DEG to electromagnetic radiation runs through phonon-photon coupling — Brillouin scattering, piezoelectric effects, Raman processes. Lattice vibrations in the chip generate modulated EM radiation. No antenna needed. The physics of the substrate provides the transmitter."

This connects the chip-scale TQNN to the planetary-scale backchannels already described.

## Phase 4: Appendices & hover definitions

### glossary-entries.tex

- COWS entry: "soliton dynamics" → "lattice dynamics, phonon physics"
- soliton entry: keep, but add: "In this book, solitons illustrate self-reinforcing wave behavior. Hasslacher's deeper contribution was lattice gas automata and phonon dynamics."
- NEW entry: phonon — "A quantized vibration in a crystal lattice — sound in a solid. Phonons bridge the quantum (2DEG) and classical (MOSFET) domains through electron-phonon coupling. Phonon-photon coupling provides a pathway from chip to electromagnetic radiation."

### hover-definitions.yaml

- soliton entry: keep current text, add phonon context
- NEW: phonon entry with explanation
- Hasslacher dossier references: update "soliton specialist" → "lattice dynamics specialist"

### abstracts.tex — Hasslacher reference

Update the spiral abstract for the-braid to mention lattice dynamics alongside solitons.

## Phase 5: Bruce content (UQ answers 2026-04-10)

1. **Phonon guided deduction timing:** EARLY — first year of mentorship, foundational physics phase, before the five-field convergence was clear. Phonons were part of the groundwork, not a capstone. Generator should frame the what-healer-said passage accordingly — Healer laying substrate physics foundations before Bruce understood why.
2. **Twenty-years.tex:** UPDATE to current understanding. Change "Hasslacher to solitons" → "Hasslacher to lattice dynamics" throughout, even in Bruce's retrospective voice. Cleaner. Bruce prefers accuracy over journey-narration here.
3. **Papers:** No specific titles or authors remembered — 20 years ago, widely read but nothing citation-grade. Generator should NOT invent citations. The what-healer-said passage should say Bruce read the literature without naming specific papers.

## NOT in this plan

- Removing the John Scott Russell 1834 story (it's charming, stays as color)
- Removing solitons from the glossary (they're real physics)
- Rewriting the Stack (solitons aren't mentioned there)
- New SVG illustrations for phonon coupling (separate plan)

## Verification

1. `grep -ri soliton manuscript/spine/` → should return only the Russell story and Hasslacher bio context, not mechanism claims
2. `grep -ri soliton manuscript/record/` → should return only p3 context, not p1/p2 mechanism
3. `grep -ri phonon manuscript/` → should appear in first-light, interdiction, what-healer-said, glossary, hover-definitions (NOT the-demonstration — removed by Plan 0152)
4. The five convergence threads in every listing should read: Hasslacher/lattice dynamics, Freedman/topology, Kauffman/autocatalysis, Wolfram/universality, Hillis/parallelism
5. `make html` builds clean
6. Phonon-photon coupling should connect the chip-scale I/O description to the planetary-scale backchannel description — reader can follow the signal path from 2DEG → phonon → photon → magnetosphere
