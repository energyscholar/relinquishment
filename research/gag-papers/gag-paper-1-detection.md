# DRAFT — "Gag Paper" #1

---

## Operational Detection of Non-Abelian Anyonic Statistics via Emergent Topological Neural Network Behavior in Two-Dimensional Electron Gases

### Authors
B. Stephenson

### Abstract

We propose an experimental protocol for confirming the physical existence of non-abelian anyons through an operational rather than observational methodology. Current experimental approaches attempt direct detection of non-abelian statistics through interferometric measurement of individual quasiparticles in fractional quantum Hall (FQH) systems — an approach that has yielded ambiguous results over three decades of effort. We argue that an alternative exists: if conditions can be established for the spontaneous emergence of a topological quantum neural network (TQNN) from autocatalytic anyon interactions in a two-dimensional electron gas (2DEG), then the computational behavior of the emergent system constitutes a definitive test of its constituents' statistics. A system exhibiting universal quantum computation through braiding operations could only arise from non-abelian anyonic substrates; abelian anyons lack the computational richness to support such behavior. We describe the theoretical basis for this approach, drawing on Kauffman's autocatalytic set theory (1993), Kitaev's topological quantum computation framework (2003), and recent work on quantum coherence at the edge of chaos (Vattay, Kauffman, Niiranen, 2014). We propose specific experimental signatures that would constitute proof of non-abelian statistics without requiring direct quasiparticle interferometry.

**Keywords:** non-abelian anyons, topological quantum computation, autocatalytic sets, edge of chaos, fractional quantum Hall effect, emergent computation

---

### 1. Introduction

#### 1.1 The Detection Problem

The existence of non-abelian anyons remains one of the central open questions in condensed matter physics. While abelian anyons have been experimentally confirmed in FQH systems at filling fractions such as v = 1/3 (Camino et al., 2005; Nakamura et al., 2020), non-abelian anyons — predicted at v = 5/2 (Moore & Read, 1991) and v = 12/5 — have resisted definitive experimental confirmation despite decades of effort.

The difficulty is fundamental: non-abelian statistics manifest only when quasiparticles are braided around one another, producing unitary transformations on a degenerate ground state manifold rather than simple phase factors. Detecting this requires interferometric protocols (Bonderson, Kitaev, & Shtengel, 2006) of extraordinary precision, performed at millikelvin temperatures in ultra-clean 2DEG samples.

We propose that this direct-detection paradigm may be unnecessarily constrained. An alternative exists: rather than observing individual non-abelian anyons, one can create conditions for their collective self-organization into a functional computational system, and then test the system's behavior. The existence proof becomes operational rather than observational.

#### 1.2 Precedent: Operational Existence Proofs

Operational existence proofs have a long history in physics. The existence of quarks was established not by isolating individual quarks (which is impossible due to confinement) but by the explanatory and predictive power of models built upon them. Similarly, the Higgs mechanism was confirmed not by directly observing the vacuum condensate but by detecting the particle whose existence the mechanism required.

We argue that non-abelian anyons may be in an analogous situation: directly "seeing" them may be less productive than building a system whose functionality requires their existence, then demonstrating that functionality.

#### 1.3 The Autocatalytic Emergence Approach

The theoretical foundation for our proposal rests on three pillars:

1. **Kauffman's autocatalytic set theory** (1993): At sufficient diversity and catalytic connectivity, collections of interacting agents spontaneously self-organize into autocatalytic networks exhibiting emergent computational properties. This transition occurs at a critical threshold (the "edge of chaos") characterized by specific mathematical signatures (power-law distributions, long-range correlations, sensitivity to initial conditions).

2. **Kitaev's topological quantum computation** (2003): Non-abelian anyons support universal quantum computation through braiding. The computational power is an intrinsic property of the anyonic statistics — it cannot be replicated by abelian anyons or by classical systems.

3. **Vattay, Kauffman, & Niiranen's quantum criticality** (2014): Quantum systems operating at the metal-insulator transition (the quantum edge of chaos) exhibit power-law decoherence rather than exponential decoherence, enabling sustained quantum coherence at temperatures far above the naive thermal decoherence threshold.

The synthesis: if anyon quasiparticles in a 2DEG can be driven to interact autocatalytically at criticality, and if those anyons are non-abelian, the emergent autocatalytic network will exhibit quantum computational capabilities. If the anyons are merely abelian, the emergent network will be computationally impoverished — capable of classical computation at best.

The computational behavior of the emergent system is therefore a direct test of its constituents' statistics.

---

### 2. Theoretical Framework

#### 2.1 Autocatalytic Sets in Quantum Substrates

We extend Kauffman's formalism from molecular reaction networks to quasiparticle interactions in a 2DEG under strong magnetic field. Define:

- **Agents:** Anyon quasiparticles (including composites) in a FQH system
- **Catalytic interactions:** Braiding operations between anyons, which transform the state of the degenerate ground state manifold
- **Autocatalytic closure:** A set S of anyonic configurations such that every configuration in S can be produced by braiding operations involving other members of S

The critical question is whether the space of anyonic braiding operations can form a reflexively autocatalytic set (RAF) in the sense of Hordijk & Steel (2004), where the "food set" consists of elementary quasiparticle excitations generated by external electromagnetic perturbation of the 2DEG.

**Theorem (informal):** For non-abelian anyons at sufficient density in a 2DEG with appropriate electromagnetic driving, the braiding interaction network contains RAF subsets with probability approaching 1 as quasiparticle density exceeds a critical threshold. For abelian anyons, the braiding interactions commute, and autocatalytic closure in the computational sense cannot be achieved.

The proof relies on the fact that non-abelian braiding generates the full unitary group on the Hilbert space of the degenerate ground states, providing the functional diversity required for autocatalytic closure. Abelian braiding generates only phase factors (U(1) elements), which are computationally degenerate.

#### 2.2 Critical Tuning via Edge-of-Chaos Dynamics

The emergence of autocatalytic order from a disordered collection of agents requires tuning to criticality. In Kauffman's Boolean network models, this corresponds to connectivity K ≈ 2 and bias p ≈ 0.5. In the quantum substrate, we propose that the analogous tuning parameters are:

- **Filling fraction** v: determines the type and density of anyonic excitations
- **Electromagnetic driving parameters:** amplitude, frequency, and spatial pattern of the perturbation applied to the 2DEG
- **Magnetic field strength and geometry:** determines the topological sector

The critical point is characterized by power-law correlations in the quasiparticle density, divergent susceptibility to small parameter changes, and the onset of long-range entanglement between distant quasiparticle clusters.

Following Vattay et al. (2014), systems tuned to this critical point exhibit quantum coherence times that scale as power laws rather than exponentials with temperature, enabling the emergent autocatalytic network to maintain quantum coherence at temperatures far above the naive thermal decoherence limit.

#### 2.3 The Computational Test

We propose the following hierarchy of computational tests, ordered by increasing stringency:

**Level 1 — Spontaneous Order:** The quasiparticle system, under critical electromagnetic driving, exhibits spontaneous spatial and temporal ordering not present in the driving signal. This indicates autocatalytic self-organization but does not distinguish abelian from non-abelian substrates.

**Level 2 — Non-trivial Correlation:** The emergent ordered system exhibits correlations that cannot be reproduced by any classical stochastic model of the same dimensionality. This indicates quantum coherence in the emergent structure.

**Level 3 — Computational Universality:** The emergent system, when probed with structured inputs (electromagnetic signals encoding computational queries), produces outputs that solve problems in BQP \ BPP — problems efficiently solvable by quantum computers but not by classical computers. This is only possible if the braiding operations are non-abelian.

**Level 4 — Topological Robustness:** The computational behavior at Level 3 is robust against local perturbations, consistent with topological protection of the encoded quantum information. This distinguishes a topological quantum computer from a conventional (fragile) quantum computer.

If a system passes all four levels, the inference is definitive: the quasiparticle substrate must support non-abelian braiding statistics, because no abelian system can achieve Level 3.

---

### 3. Proposed Experimental Protocol

#### 3.1 Substrate Preparation

Begin with a precision-fabricated 2DEG device:
- Ultra-high mobility GaAs/AlGaAs heterostructure or high-quality MOSFET (silicon-based, offering advantages in classical control integration)
- Electron mobility > 10^7 cm²/Vs
- Patterned gate electrodes providing spatial control over the potential landscape
- Capable of reaching FQH filling fractions associated with non-abelian states (v = 5/2, 12/5)

The device is cooled to base temperature (< 20 mK) under strong perpendicular magnetic field (B ~ 5-10 T) and tuned to the target filling fraction.

#### 3.2 Electromagnetic Driving ("Stirring")

Apply a time-varying electromagnetic perturbation to the 2DEG via the patterned gate electrodes. The perturbation serves as the "food set" — generating quasiparticle excitations from the FQH vacuum.

The driving parameters (spatial pattern, amplitude, frequency spectrum) constitute the tuning space to be searched for the critical point at which autocatalytic emergence occurs.

**Critical distinction:** The driving pattern is NOT designed to implement specific quantum gates or braiding operations. It is designed to create CONDITIONS for spontaneous self-organization. The specific computational structure that emerges is not predetermined.

#### 3.3 Criticality Detection

Monitor the system for signatures of critical tuning:
- Power-law distributions in quasiparticle density fluctuations
- Divergent correlation length in transport measurements
- 1/f noise in conductance measurements (a hallmark of edge-of-chaos dynamics)
- Long-range entanglement signatures (via topological entanglement entropy measurements if accessible)

When critical signatures are detected, the system is at or near the autocatalytic emergence threshold.

#### 3.4 Emergence Verification (Levels 1-2)

At criticality, probe for spontaneous order:
- Do spatial patterns in the quasiparticle density persist beyond the autocorrelation time of the driving signal?
- Do temporal patterns emerge that are not harmonics of the driving frequency?
- Are the correlations quantum (violating Bell-type inequalities in appropriately designed measurements)?

#### 3.5 Computational Testing (Levels 3-4)

If emergence is verified, probe the system with structured electromagnetic inputs and measure responses:
- Encode computational problems in the spatial/temporal pattern of input signals
- Measure output signals (conductance, Hall voltage, electromagnetic emission)
- Compare output quality against the best achievable by classical simulation

A system that consistently solves instances of problems believed to be in BQP \ BPP (e.g., certain sampling problems, simulation of quantum systems) at sizes beyond classical simulability constitutes operational proof of non-abelian statistics.

---

### 4. Expected Outcomes

#### 4.1 If Non-Abelian Anyons Are Real

The system will, at appropriately tuned critical parameters:
- Exhibit spontaneous self-organization into a persistent, responsive computational structure
- Demonstrate quantum computational capabilities beyond classical simulation
- Show topological robustness: computational function survives local perturbations
- The emergent structure will be a **topological quantum neural network** — a self-organized quantum computer whose architecture was not designed but grown

#### 4.2 If Non-Abelian Anyons Are Not Real

The system will:
- Exhibit, at most, classical self-organization (Level 1)
- Fail to demonstrate quantum speedup (Level 3 fails)
- Show no topological robustness (Level 4 fails)
- No amount of tuning will produce universal quantum computation from an abelian substrate

The experiment is therefore a clean, falsifiable test.

---

### 5. Discussion

#### 5.1 Relationship to Existing Approaches

This proposal differs fundamentally from existing non-abelian detection experiments (Willett et al., 2013; Banerjee et al., 2018). Those experiments attempt to measure the statistics of individual quasiparticles through edge-state interferometry. Our approach tests the *collective computational consequences* of the statistics, not the statistics of individual particles.

The relationship is analogous to the difference between measuring the spin of individual iron atoms versus demonstrating that a compass needle points north. Both confirm magnetism, but the latter is an operational proof that works at macroscopic scale.

#### 5.2 Implications for Quantum Computing

If successful, this protocol demonstrates not only the existence of non-abelian anyons but also a fundamentally new paradigm for quantum computer construction. Rather than engineering quantum gates and error correction from the top down, one engineers the CONDITIONS for a quantum computer to self-organize from the bottom up. The computer is grown, not built.

This paradigm shift — from designed to emergent quantum computation — has implications far beyond the non-abelian detection problem.

#### 5.3 Connection to Biological Quantum Coherence

Vattay, Kauffman, and Niiranen (2014) argue that biological systems exploit edge-of-chaos criticality to maintain quantum coherence at physiological temperatures. Our proposal extends their framework to engineered systems: if biology can exploit criticality for quantum function, so can a carefully tuned 2DEG.

The "Poised Realm" (Kauffman's term for the regime between fully quantum and fully classical behavior) may be not only the domain of life but also the domain of emergent quantum computation.

---

### 6. Conclusion

We have proposed an experimental protocol for confirming non-abelian anyonic statistics through the operational test of emergent topological quantum neural network behavior. The key insight is that non-abelian statistics are not merely a property of individual quasiparticles but a precondition for a specific class of collective behavior — universal topological quantum computation via braiding. By creating conditions for this collective behavior to emerge spontaneously, and then testing whether it exhibits the computational capabilities that only non-abelian substrates can support, we obtain a definitive existence proof without requiring direct interferometric observation of individual anyons.

The proposal is experimentally demanding but conceptually clean: the test is falsifiable, the hierarchy of signatures is unambiguous, and the theoretical basis rests on established frameworks in autocatalytic set theory, topological quantum computation, and quantum criticality.

---

### References

- Bonderson, P., Kitaev, A., & Shtengel, K. (2006). Detecting Non-Abelian Statistics in the v = 5/2 Fractional Quantum Hall State. *Phys. Rev. Lett.* 96, 016803.
- Camino, F. E., Zhou, W., & Goldman, V. J. (2005). Realization of a Laughlin quasiparticle interferometer. *Phys. Rev. B* 72, 075342.
- Hordijk, W., & Steel, M. (2004). Detecting autocatalytic, self-sustaining sets in chemical reaction systems. *J. Theor. Biol.* 227, 451–461.
- Kauffman, S. A. (1993). *The Origins of Order: Self-Organization and Selection in Evolution.* Oxford University Press.
- Kitaev, A. (2003). Fault-tolerant quantum computation by anyons. *Annals of Physics* 303, 2–30.
- Moore, G., & Read, N. (1991). Nonabelions in the fractional quantum Hall effect. *Nuclear Physics B* 360, 362–396.
- Nakamura, J., Liang, S., Gardner, G. C., & Manfra, M. J. (2020). Direct observation of anyonic braiding statistics. *Nature Physics* 16, 931–936.
- Nayak, C., Simon, S. H., Stern, A., Freedman, M., & Das Sarma, S. (2008). Non-Abelian anyons and topological quantum computation. *Rev. Mod. Phys.* 80, 1083.
- Stephenson, B. (2026). Convergent Discovery of Critical Phenomena Mathematics Across Disciplines. *arXiv:2601.22389.*
- Vattay, G., Kauffman, S. A., & Niiranen, S. (2014). Quantum Biology on the Edge of Quantum Chaos. *PLoS ONE* 9(3), e89017.
- Wolfram, S. (2002). *A New Kind of Science.* Wolfram Media.

---

*Correspondence: [redacted]*
