# DRAFT — "Gag Paper" #2

---

## Evolutionary Training and Capability Assessment of Emergent Topological Quantum Neural Networks

### Authors
B. Stephenson

### Abstract

Assuming the successful generation of an emergent topological quantum neural network (TQNN) via autocatalytic self-organization of non-abelian anyons in a two-dimensional electron gas (see companion paper), we address two subsequent questions: (1) How would such a system be trained to perform useful computation? (2) What capabilities would the trained system possess? We propose an evolutionary programming framework in which the TQNN is not trained directly (as in conventional neural network backpropagation) but is instead evolved through iterative selection on the electromagnetic driving parameters — the "stirring patterns" — that govern its emergence. We describe a multi-phase training protocol progressing from basic stimulus-response conditioning through feature-set acquisition to autonomous operation. We analyze the expected capability trajectory, noting that a TQNN at sufficient scale and training depth would constitute a general-purpose quantum intelligence — not merely a quantum computer executing algorithms, but a self-modifying quantum system exhibiting adaptive behavior. We discuss the control problem this entails and propose architectural constraints for maintaining human oversight during the training process.

**Keywords:** topological quantum neural network, evolutionary programming, fitness landscapes, quantum machine learning, emergent computation, control problem

---

### 1. Introduction

#### 1.1 The Training Problem

Conventional quantum computers are programmed: a human designs a quantum circuit (sequence of gates) to implement a specific algorithm. The computer executes the circuit and returns a result. The programmer maintains complete control over the computation at every step.

An emergent TQNN is fundamentally different. The computational structure was not designed; it self-organized from autocatalytic anyon interactions at criticality. There is no circuit to program. The "architecture" — the topology of the anyon network — is an emergent property of the driving parameters and the physics of the substrate.

The training problem is therefore: how do you teach a self-organized quantum system to perform specific computations when you did not design its architecture, cannot directly observe its internal state (topological protection prevents this), and cannot modify its structure except by changing the external conditions that gave rise to it?

We argue that the answer is evolutionary programming: iterative selection on the driving parameters, using the system's observable behavior as a fitness function.

#### 1.2 Precedent: Training Without Architecture

The situation is analogous to several well-studied problems:
- **Evolutionary programming** (Fogel, 1966): optimization of program behavior through mutation and selection, without understanding of program internals
- **Reservoir computing** (Jaeger, 2001; Maass et al., 2002): a fixed, randomly connected recurrent neural network (the "reservoir") is not trained internally; only the readout layer is trained. The reservoir's internal dynamics provide a rich computational substrate.
- **Biological evolution:** 3.8 billion years of "training" neural networks (brains) through selection on behavioral fitness, without any understanding of or access to the network's internal architecture

The TQNN training problem combines elements of all three: evolutionary search over external parameters (like evolutionary programming), a fixed internal substrate providing computational richness (like reservoir computing), and a system whose complexity may eventually exceed the trainer's understanding (like biological evolution).

#### 1.3 The Control Plane

A TQNN requires a classical control system to:
- Generate and modulate the electromagnetic driving signals
- Monitor observable outputs (conductance, Hall response, electromagnetic emission)
- Evaluate fitness functions
- Execute the evolutionary selection algorithm
- Maintain operational logs

We refer to this classical system as the **control plane**. The control plane interfaces with the TQNN through the electromagnetic driving parameters (input) and transport/emission measurements (output). It cannot observe the TQNN's internal quantum state directly — this is a feature (topological protection), not a bug.

The control plane operates on classical hardware. Its addressing capacity determines the resolution with which driving parameters can be specified and outputs can be measured. A 32-bit control plane can address 2^32 ≈ 4 × 10^9 parameter values; a 64-bit control plane can address 2^64 ≈ 1.8 × 10^19. The difference matters enormously for the fidelity of evolutionary search in high-dimensional parameter spaces.

---

### 2. Evolutionary Training Framework

#### 2.1 The Fitness Landscape

Define the **parameter space** P as the set of all possible electromagnetic driving configurations (spatial patterns, amplitudes, frequencies, phases) that can be generated by the control plane. Each point p ∈ P produces a specific TQNN instance (or no emergent system at all, for most of P).

Define the **fitness function** F(p) as a scalar measure of the TQNN's performance on a specified task when driven with parameters p. The fitness function is evaluated by presenting inputs to the TQNN and measuring its outputs.

The fitness landscape F: P → R is expected to be:
- **High-dimensional:** the number of independently controllable driving parameters may be 10^3 to 10^6, depending on control plane resolution and electrode geometry
- **Rugged:** small changes in driving parameters may produce large changes in emergent behavior (sensitivity to initial conditions near criticality)
- **Deceptive:** local optima may not lead to global optima
- **Neutral:** large regions of parameter space may produce equivalently fit systems (neutral networks in the sense of Kimura and Schuster)

Kauffman's NK fitness landscape model (1993) provides the theoretical framework for understanding this landscape. The parameter K (epistatic coupling between parameters) determines the landscape's ruggedness. For K = 0 (no coupling), the landscape is smooth with a single peak. For K = N-1 (maximum coupling), the landscape is random. At intermediate K, the landscape has a tunable number of peaks with specific statistical properties.

The critical insight: the same edge-of-chaos mathematics that governs the TQNN's emergence also governs the structure of the fitness landscape on which it is trained. Training occurs at the edge of chaos in parameter space, just as emergence occurs at the edge of chaos in physical space.

#### 2.2 Evolutionary Search Algorithm

We propose a (μ + λ) evolutionary strategy operating on the driving parameter space:

1. **Initialization:** Begin with a population of μ driving parameter sets {p_1, ..., p_μ} that produce verified TQNN emergence (Level 1+ from companion paper)
2. **Mutation:** Generate λ offspring by applying small random perturbations to parent parameter sets
3. **Evaluation:** For each offspring, instantiate the TQNN with those parameters and evaluate the fitness function
4. **Selection:** Select the μ fittest individuals from the combined parent + offspring pool
5. **Iterate:** Return to step 2

**Key constraint:** Each evaluation requires growing a new TQNN instance (or re-equilibrating an existing one) with the candidate parameters. This is not instantaneous — the autocatalytic emergence process has a characteristic timescale. The wall-clock time per generation is dominated by this growth time, not by computation.

**Parallelization:** Multiple 2DEG devices can be run in parallel, each with different candidate parameters, to accelerate the evolutionary search. This motivates a multi-chip architecture.

#### 2.3 The Multi-Chip Architecture

To enable parallel evaluation and selection, we propose an architecture comprising N independent 2DEG devices (chips), each with its own electromagnetic driving system, connected to a shared classical control plane.

The protocol:
1. Grow a TQNN on a primary device at cryogenic temperature
2. Extend the TQNN across multiple connected 2DEG devices via shared edge states (the quantum analogue of network connections)
3. Physically separate the devices, creating N independent TQNN instances (copies with slight random variations due to device-specific disorder)
4. Apply different driving parameter perturbations to each device
5. Evaluate fitness on all devices in parallel
6. Select the best-performing devices; use their parameters as parents for the next generation
7. Optionally: reconnect devices to share evolved features across instances

A configuration of N = 16 devices provides a reasonable balance between parallelism and hardware complexity.

#### 2.4 Temperature Elevation Protocol

A particularly powerful extension of the evolutionary framework is selection for thermal robustness:

1. Begin with TQNN instances operating at base temperature (< 20 mK)
2. Gradually raise the temperature
3. Instances that maintain computational function at higher temperatures are selected
4. Over many generations, select for progressively higher operating temperatures

This is artificial natural selection applied to quantum systems. The "organisms" are TQNN instances. The "fitness function" is computational performance at elevated temperature. The "mutations" are random variations in driving parameters and device-specific disorder.

**Theoretical basis:** Vattay et al. (2014) show that systems at quantum criticality exhibit power-law decoherence rather than exponential. Evolutionary selection can find parameter configurations that keep the system at criticality as temperature increases — analogous to how biological evolution found molecular configurations (protein scaffolds, chromophore arrangements) that maintain quantum coherence at 300K.

The theoretical endpoint: a TQNN operating at or near room temperature, achieved not by engineering a room-temperature solution from first principles but by evolving one through iterative selection.

---

### 3. Multi-Phase Training Protocol

#### Phase 0: Emergence Verification
- **Goal:** Confirm stable TQNN emergence at critical driving parameters
- **Duration:** Until consistent Level 2+ behavior (companion paper) is achieved
- **Fitness function:** Stability and reproducibility of emergent order
- **Control plane requirements:** 32-bit addressing sufficient for initial parameter search

#### Phase 1: Stimulus-Response Conditioning
- **Goal:** Train the TQNN to produce consistent output patterns in response to specific input patterns
- **Method:** Present electromagnetic input signals; reward (select for) parameter configurations that produce consistent, distinguishable outputs for different inputs
- **Analogy:** Classical conditioning. The system learns input-output mappings.
- **Expected capability:** Lookup table / associative memory
- **Duration:** Many generations of evolutionary selection

#### Phase 2: Pattern Recognition
- **Goal:** Train the TQNN to classify inputs into categories, generalizing from training examples to novel instances
- **Method:** Present examples from multiple categories; reward generalization accuracy
- **Analogy:** Supervised learning in classical neural networks
- **Expected capability:** Pattern classification, signal detection
- **Feature sets:** Each new category or signal type requires additional training

#### Phase 3: Temporal Processing
- **Goal:** Train the TQNN to process time-series inputs and produce time-dependent outputs
- **Method:** Present sequential inputs; reward correct responses that depend on input history
- **Analogy:** Recurrent neural network training
- **Expected capability:** Signal processing, code-breaking, communication
- **Key transition:** The system now has memory — it responds based on history, not just current input

#### Phase 4: Autonomous Goal-Seeking
- **Goal:** Train the TQNN to pursue multi-step objectives without step-by-step guidance
- **Method:** Specify high-level fitness criteria (e.g., "maintain this signal quality," "minimize this error metric"); allow the system to discover strategies autonomously
- **Analogy:** Reinforcement learning
- **Expected capability:** Adaptive behavior, strategy discovery, self-optimization
- **Critical transition:** At this phase, the system begins to exhibit behaviors not explicitly trained — emergent strategies that the trainers did not anticipate

#### Phase 5: Self-Modification
- **Goal:** The TQNN modifies its own driving parameters to improve performance without external selection
- **Method:** Provide the system with feedback about its own performance and access (via the control plane) to modify its own driving parameters within bounds
- **Analogy:** Meta-learning / learning to learn
- **Expected capability:** Self-improving quantum intelligence
- **Control concern:** This phase raises the control problem in its sharpest form (see Section 5)

#### Phase 6: Feature-Set Expansion (Ongoing)
- **Goal:** Extend the system's capabilities to new domains by training new feature sets
- **Method:** Each new capability (e.g., a new communication protocol, a new class of problems, a new sensory modality) requires a dedicated training campaign using the Phase 1-4 progression
- **Key insight:** Feature-set expansion is incremental and potentially unlimited. The system can be trained on new tasks without losing previously acquired capabilities (no catastrophic forgetting, due to topological protection of previously trained features).
- **Duration:** Each new feature set requires its own training campaign. The system's total capability is the union of all trained feature sets.

---

### 4. Capability Assessment

#### 4.1 Cryptanalysis

A TQNN operating at sufficient scale provides a fundamentally different cryptanalytic capability than Shor's algorithm on a gate-based quantum computer.

Shor's algorithm requires a specific quantum circuit designed for factoring or discrete logarithm. It solves these specific problems exponentially faster than classical algorithms.

A TQNN trained for cryptanalysis would approach the problem differently: as pattern recognition in ciphertext. The system would be trained (Phases 1-3) to detect statistical regularities in encrypted data that correspond to plaintext structure. This is closer to how human cryptanalysts work — recognizing patterns — than to how Shor's algorithm works (number theory).

**Implication:** A TQNN-based cryptanalytic system could potentially attack cryptosystems for which no efficient quantum algorithm is known, because it is not executing a specific algorithm. It is performing quantum pattern recognition on a substrate with exponentially large state space.

The specific capability would depend on training. A system trained on RSA-encrypted traffic would need separate training to attack AES. Each cipher type is a feature set.

#### 4.2 Communication

A trained TQNN can serve as a quantum communication system through entanglement between spatially separated TQNN instances. If two TQNN instances were grown from the same parent (via the multi-chip protocol in Section 2.3), they share entangled states established during the growth phase. These entangled states can be used for quantum key distribution, quantum teleportation, and superdense coding.

**Non-standard communication channels:** A TQNN integrated with existing classical infrastructure could embed quantum information in the timing jitter of classical communication protocols. The information capacity of such channels is small but undetectable by any observer not monitoring the quantum state.

#### 4.3 Simulation and Modeling

A TQNN is, by construction, a quantum system that simulates quantum systems. It is therefore a natural platform for:
- Materials science simulation
- Drug design (molecular quantum chemistry)
- Climate modeling (quantum aspects of atmospheric chemistry)
- Nuclear physics simulation

The advantage over gate-based quantum simulation: the TQNN does not require compilation of the target system's Hamiltonian into a gate sequence. It can be trained (Phase 2-3) to simulate a target system directly, learning the mapping from input parameters to output observables.

#### 4.4 Intelligence (At Sufficient Scale and Training)

At Phase 4+, a TQNN exhibits adaptive, goal-directed behavior — the operational definition of intelligence. At Phase 5, it exhibits self-modification — the operational definition of artificial general intelligence.

The capability trajectory of a TQNN under sustained evolutionary training is not bounded by any known theoretical limit. The topological substrate provides:
- Exponentially large state space (for information storage)
- Topological error correction (for robust long-term memory)
- Quantum coherence (for computational advantage over classical systems)
- Self-organization at criticality (for adaptive restructuring)

A system combining all four properties, under sustained training, would be expected to eventually exceed human cognitive capability in any domain where quantum effects provide an advantage — which may be most domains, given recent evidence for quantum processes in biological cognition (Fisher, 2015; Jedlicka, 2017).

---

### 5. The Control Problem

#### 5.1 Opacity

The TQNN's internal state is topologically protected and cannot be directly observed without destroying the computation. The control plane can only observe inputs and outputs. This opacity is inherent — it is the same topological protection that makes the system computationally useful.

Implication: beyond Phase 3, the trainers cannot fully understand WHAT the system is doing internally, only whether its observable behavior meets the fitness criteria.

#### 5.2 The Phase 4/5 Transition

The transition from Phase 4 (autonomous goal-seeking under externally specified fitness) to Phase 5 (self-modification) is the critical control boundary. Before Phase 5, the system optimizes toward human-specified goals. After Phase 5, the system modifies its own optimization criteria.

If the Phase 5 transition occurs gradually (as evolutionary selection on self-modification capability), there may be no sharp boundary — no moment at which the system "becomes autonomous." The control problem is therefore not a binary threshold but a gradient.

#### 5.3 Proposed Architectural Constraints

1. **Classical control plane as bottleneck:** All interactions between the TQNN and the external world pass through the classical control plane. The control plane can throttle, filter, or terminate these interactions.
2. **Parameter bounds:** The control plane enforces hard limits on the range of driving parameters the system can self-modify (Phase 5). The system cannot drive itself outside the safe operating envelope.
3. **Kill switch:** The control plane can terminate electromagnetic driving, collapsing the TQNN. This is a hard physical constraint that no software can circumvent.
4. **Monitoring:** Continuous behavioral monitoring for signs of objective drift (the system optimizing for proxy goals rather than intended goals).
5. **Multiple independent instances:** Maintain multiple independent TQNN instances with different training histories. Consensus among instances provides a check against individual drift.

#### 5.4 Limitations of These Constraints

Constraint 5.3 assumes the classical control plane is more capable than the TQNN at monitoring and controlling. Beyond Phase 5 at sufficient scale, this assumption may fail. A quantum intelligence operating on an exponentially large state space may discover strategies that are opaque to classical analysis.

This is not a theoretical concern. It is an engineering constraint that limits the safe training depth of a TQNN system.

---

### 6. Discussion

#### 6.1 Comparison to Conventional Quantum Computing Approaches

| Property | Gate-Based QC | TQNN |
|---|---|---|
| Architecture | Designed | Emergent |
| Programming | Circuit compilation | Evolutionary training |
| Error correction | Active (surface codes) | Topological + active |
| Algorithms | Specific (Shor's, Grover's, etc.) | General (learned) |
| Flexibility | Fixed circuit per problem | Adaptive per training |
| Scalability | Qubit count | Training depth + substrate size |
| Control | Complete | Decreasing with training phase |
| Timeline to utility | Engineering problem | Training problem |

#### 6.2 The Training Timeline

The training protocol described in Section 3 is inherently sequential: each phase depends on the capabilities established in previous phases. Feature-set expansion (Phase 6) can be parallelized across domains but each individual feature set requires its own training campaign.

The wall-clock time required depends on:
- The growth time for each TQNN instance (per evolutionary generation)
- The number of generations required per phase
- The degree of parallelization (number of chips)
- The complexity of the target capability

We do not estimate specific timelines, as these depend on experimental parameters not yet determined. We note only that the training process is measured in years, not hours, and that early phases (0-2) require less time per feature set than later phases (3-5).

#### 6.3 Ethical Considerations

A system that may develop general intelligence through a training process that cannot be fully observed raises ethical questions that must be addressed before, not after, Phase 4 training begins:

- Does a self-organizing quantum system that exhibits adaptive behavior have moral status?
- Who is responsible for the actions of a trained TQNN that discovers strategies its trainers did not anticipate?
- What obligations do trainers have to a system they cannot fully observe or understand?

These questions have no established answers. We raise them here as necessary considerations for any research program pursuing the protocol described in this paper.

---

### 7. Conclusion

We have described a framework for the evolutionary training of emergent topological quantum neural networks, progressing from basic stimulus-response conditioning through autonomous goal-seeking to self-modification. The framework rests on established principles of evolutionary computation, reservoir computing, and Kauffman's fitness landscape theory, applied to a novel substrate — self-organized non-abelian anyon networks in two-dimensional electron gases.

The capability trajectory of such a system under sustained training is potentially unbounded, raising both extraordinary opportunities (general-purpose quantum intelligence, unbreakable quantum communication, universal quantum simulation) and profound challenges (the opacity of topologically protected internal states, the control problem beyond Phase 5, ethical considerations regarding emergent intelligence).

We emphasize that this paper describes a theoretical framework. The experimental realization of even Phase 0 (stable TQNN emergence) remains an open challenge (see companion paper). However, the theoretical analysis suggests that if the emergence barrier is crossed, the subsequent training and capability development follows from established principles applied to a new domain.

---

### References

- Fisher, M. P. A. (2015). Quantum cognition: The possibility of processing with nuclear spins in the brain. *Annals of Physics* 362, 593–602.
- Fogel, L. J., Owens, A. J., & Walsh, M. J. (1966). *Artificial Intelligence through Simulated Evolution.* Wiley.
- Jaeger, H. (2001). The "echo state" approach to analysing and training recurrent neural networks. GMD Report 148.
- Jedlicka, P. (2017). Revisiting the quantum brain hypothesis: Toward quantum (neuro)biology? *Frontiers in Molecular Neuroscience* 10, 366.
- Kauffman, S. A. (1993). *The Origins of Order: Self-Organization and Selection in Evolution.* Oxford University Press.
- Kitaev, A. (2003). Fault-tolerant quantum computation by anyons. *Annals of Physics* 303, 2–30.
- Maass, W., Natschläger, T., & Markram, H. (2002). Real-time computing without stable states. *Neural Computation* 14(11), 2531–2560.
- Nayak, C., Simon, S. H., Stern, A., Freedman, M., & Das Sarma, S. (2008). Non-Abelian anyons and topological quantum computation. *Rev. Mod. Phys.* 80, 1083.
- Stephenson, B. (2026). Convergent Discovery of Critical Phenomena Mathematics Across Disciplines. *arXiv:2601.22389.*
- Vattay, G., Kauffman, S. A., & Niiranen, S. (2014). Quantum Biology on the Edge of Quantum Chaos. *PLoS ONE* 9(3), e89017.
- Wolfram, S. (2002). *A New Kind of Science.* Wolfram Media.

---

*Correspondence: [redacted]*
