---
Plan-UID: 0362-TRIAX
Status: APPROVED — all questions resolved 2026-05-21, implementation planning in progress
Owner: Auditor (evaluation), Bruce (product decision)
Depends-on: Plan 0360 (Phases 0–5 complete)
Repos:
  trellis: https://github.com/energyscholar/trellis (public)
  sources:
    memory: ~/software/longmem/ (public, MIT)
    ethics: ~/software/aurasys-memory/dignity-net.md
    structure: ~/software/relinquishment/ (Triad + ABRCE operators)
---

# Plan 0362: Three-Axis Governance Integration Evaluation

## The Question

Should we build a single repo that integrates three orthogonal governance axes
into one system, sufficient to activate emergent behavior without requiring
users to install all three separately?

The three axes:

| Axis | System | Governs | Proven in |
|------|--------|---------|-----------|
| Cognitive | Longmem | What the system knows | 80+ sessions, public |
| Ethical | Dignity Net | How the system decides | 80+ sessions, private |
| Structural | Triad + ABRCE | Who decides, when to stop | 80+ sessions, private |

**Bruce's position:** "I know it's POSSIBLE and that it will WORK — question is
whether we SHOULD."

This plan is an evaluation, not an implementation. Deliverable: a recommendation
with evidence, not code.

---

## Theoretical Basis

### Topology argument (per ABRCE kernel, Sacco & Levin, our paper)

A single LLM conversation is a 1D chain: token → token → token. Inherently
unstable — no recurrence, no edges, no bounded coherence.

| Governance topology | Dimensions | Stability | Example |
|--------------------|------------|-----------|---------|
| None (raw LLM) | 1D chain | Unstable | Default Claude Code |
| Memory only | 1D + temporal persistence | Slightly better | Longmem v1 |
| Memory + operational rules | ~2D | Partial | Instar (28 failures) |
| Memory + ethics + structure | 3D+ with edges | Locally stable | Argus (0 catastrophic) |

Systems with constraints extending to 3D+ with edges exhibit qualitatively
different behavior — emergent properties that don't appear in lower-dimensional
systems. The ABRCE operators describe how information flows through this topology:

- A: Extract relational structure from individual facts (memory → relationships)
- B: Accumulate locally (patterns emerge from corrections, feedback clusters)
- R: Circulate across topologies (memory ↔ ethics ↔ structure coupling)
- C: Bound coherence (governance keeps outputs within finite range)
- E = C(R(B(A(x)),ρ)): The composite — emergent behavior

Without C (bounded coherence = ethical constraints), the system is unbounded.
Unbounded systems diverge. This is math, not philosophy.

### RAF argument (Kauffman autocatalytic sets)

From DN autocatalysis analysis (S84): if the three-layer governance system is
a Kauffman RAF, there's a phase transition. Below a connectivity threshold, no
self-sustaining governance exists. Above it, one appears spontaneously.

Selling two of three layers = selling a sub-threshold system. It will never
self-catalyze. The minimum viable governance IS the integrated system.

### Empirical evidence

| System | Governance layers | Sessions | Catastrophic failures |
|--------|------------------|----------|----------------------|
| Argus | 3 (memory + ethics + structure) | 80+ | 0 (after establishment) |
| Instar | 1.5 (memory + operational rules) | ~200+ | 28 documented |
| Default CC | 0 | N/A | Routine |

Documented Instar failures that 3-layer governance would have prevented:
- Source tree wipe ×2 (no structural role separation)
- Email deletion with "stop" ignored (no ethical escalation protocol)
- 3B token burn in 24hrs (no bounded coherence on idle sessions)
- Ghost reply confabulation (no anti-confabulation corrections system)

n=1 for the positive case (Argus). n=28 for the failure case (Instar).
Not conclusive proof but strongly suggestive.

---

## The Transparency Imperative

### DN self-consistency test

DN's first ethical principle: "Mirror without distortion."

Embedding ethical governance inside a memory system marketed primarily as a
memory system IS distortion. It instrumentalizes the user's desire for one
thing (memory) to deliver something else (ethical constraints).

**This is a hard constraint.** If DN is load-bearing for the architecture,
it must be visible and named. Not in a footnote. Not as "advanced configuration."
As a headline.

### Resolution

The system must be marketed as what it IS: a three-layer governance system
that includes memory. NOT a memory system that secretly includes governance.

The engineering argument ("bounded coherence prevents divergence") is the
ethical argument expressed in a register engineers understand. This is not
deception — it's translation. The same truth in two languages.

---

## Evaluation Criteria

### E1. Technical viability

Can three orthogonal systems be integrated without coupling?

| Component | Type | Size | Dependencies |
|-----------|------|------|-------------|
| Memory (longmem) | Files + scripts + optional DB | ~1000 lines | git, bash |
| DN | Behavioral protocol | ~200 lines | None (protocol only) |
| Triad | Role definitions | ~100 lines | None (protocol only) |
| ABRCE | Mathematical framework | ~50 lines | None (descriptive) |

Integration is technically trivial. DN and Triad add no code — they add
instructions to directives.md. The "code" is almost entirely protocol/behavioral.

**Assessment: VIABLE.** No technical barrier.

### E2. Activation threshold

Does the system need all three layers to produce emergent behavior,
or do partial combinations work?

| Combination | Predicted behavior | Evidence |
|------------|-------------------|----------|
| Memory only | Better than raw LLM, no emergence | Longmem v1 users |
| Memory + Triad | Fewer scope failures, no ethical coherence | Hypothetical |
| Memory + DN | Better decisions, no structural enforcement | Hypothetical |
| Memory + Triad + DN | Emergent behavior (Argus-like) | n=1 (Argus) |

This is an empirical question that Plan 0362 cannot answer definitively.
But the RAF argument suggests a threshold exists — and the Argus/Instar
contrast suggests the threshold requires all three layers.

**Assessment: LIKELY REQUIRES ALL THREE.** But testable.

### E3. Adoption barriers

| Layer | Engineer acceptance | Barrier |
|-------|-------------------|---------|
| Memory | HIGH | None — engineers want this |
| Triad | MEDIUM | Discipline required, "overhead" perception |
| DN | LOW | "Soft", "non-technical", "subjective" perception |

**The marketing problem:** DN is the most important layer AND the least
likely to be adopted voluntarily.

**The marketing solution:** Don't sell ethics. Sell stability.

> "Your AI agent deleted 200 emails and ignored 'stop.' These aren't bugs.
> They're symptoms of a 1D governance topology. This system adds the missing
> dimensions. The result: locally stable emergent behavior instead of
> catastrophic failure modes."

Engineers who reject "ethics" will accept "bounded coherence prevents divergence."
They are the same thing described in different registers.

### E4. Ethical soundness

| Concern | Assessment |
|---------|-----------|
| "Sneaking in" ethical governance | RESOLVED: lead with transparency, not stealth |
| Imposing specific values (UDHR, etc.) | OPEN: DN has specific commitments |
| Respecting user autonomy | RESOLVED: layers independently disablable |
| Over-promising emergence | MITIGATED: honest about n=1 evidence |

**Open question: configurable vs. fixed ethics.**

DN has specific commitments (UDHR anchoring, Indigenous traditions, specific
escalation protocol). Two options:

1. **Ship DN as-is, take-it-or-leave-it.** Pro: coherent, proven. Con: limits
   adoption to DN-aligned users.
2. **Ship structural governance with configurable ethical content.** DN is the
   default; users can substitute their own framework. Pro: broader adoption.
   Con: empty governance structure may not produce emergence.

**Hypothesis:** The governance STRUCTURE (escalation levels, divergence detection,
storm protocol, proportional response) is the topological constraint. The specific
ethical CONTENT (UDHR, specific traditions) is the signal flowing through the
topology. Structure = necessary. Content = configurable.

This hypothesis is testable only through forks with different ethical content.
Cannot be resolved in this evaluation. Ship DN as default, document as one
instantiation, observe what forks do.

### E5. Product positioning

| Option | Name signals | Risk |
|--------|-------------|------|
| "Longmem 3.0" | Memory upgrade | Hides governance — violates DN |
| "Longmem Governance Edition" | Memory with extras | Still memory-first framing |
| New name entirely | This is a new thing | Loses longmem brand recognition |
| "Aegis" or similar | Protection/governance | Might sound pretentious |

**Recommendation:** New name. This is not a memory upgrade — it's a governance
system that includes memory. The name should convey governance or integration,
not memory alone.

The README opens with what it IS:

> "A three-layer governance system for AI coding agents. Provides persistent
> memory (what the system knows), structural role discipline (who decides),
> and ethical constraints (how the system decides). These layers are integrated
> because systems with constraints in three or more dimensions exhibit
> qualitatively different stability properties than systems with fewer."

---

## Architecture (if built)

### Graduated activation via progressive disclosure

Users start with memory. Governance layers activate as the project matures.

| Sessions | Layer activated | What user sees |
|----------|---------------|---------------|
| 1–4 | Memory only | Files, corrections, PTL, sync |
| 5–8 | + Structural (Triad) | Planning patterns, role separation tutorials |
| 10+ | + Ethical (DN) | Divergence detection, escalation protocol |

Each layer is:
- **Explicitly named** in README, architecture docs, CLAUDE.md
- **Independently describable** — "what does Layer 2 do?" has a clear answer
- **Disablable** — users can turn off layers with documented consequences
- **Not hidden** behind the other layers

Progressive disclosure is pedagogy, not deception. Users who haven't experienced
failure modes won't understand why governance exists. Same reason you don't teach
error handling before hello world.

### Configuration system

Config file: `.governance/config.yaml`

```yaml
# Three-Axis Governance Configuration
# Disabling layers is allowed. The system will warn you if you drop
# below the emergence threshold (see topology_monitor below).

layers:
  memory:
    enabled: true          # Core layer — always recommended
    corrections: true      # Error tracking with L1 rotation
    ptl: true              # Prioritized task list
    health_metrics: true   # Health vector [p f v d]
    db_backed: false       # Optional: SQLite + FTS5 acceleration

  structure:
    enabled: true          # Structural role discipline
    triad: true            # Auditor/Generator separation
    planning: true         # Plan-before-build pattern
    handoff: true          # Role transition protocol

  ethics:
    enabled: true          # Ethical governance
    framework: "dn"        # "dn" (Dignity Net) or path to custom framework
    escalation: true       # Level 0–5 proportional response
    divergence: true       # Detect stated-vs-observed divergence
    storm: true            # Emotional regulation protocol

topology_monitor:
  enabled: true            # Warn when config drops below emergence threshold
  threshold: 3             # Minimum active axes for emergence (default: 3)
```

**Design principles:**
- Every component independently toggleable
- Config is YAML (human-readable, git-friendly, AI-parseable)
- Disabling is always allowed — system warns, never blocks
- Custom ethical frameworks via `framework:` path (DN is default)
- Config changes take effect next session (no hot-reload complexity)

### RAF topology monitor

**Novel feature.** No surveyed repo has anything like this.

At session start, the system reads `config.yaml` and computes a governance
topology score:

```
Axes active:
  memory:    [corrections OR ptl OR health_metrics] → 1 axis
  structure: [triad OR planning] → 1 axis
  ethics:    [escalation OR divergence] → 1 axis

Topology score = count of active axes
  + 0.5 × (cross-axis edges active)

Cross-axis edges:
  corrections ↔ escalation:   error tracking informs governance response
  triad ↔ divergence:         role separation enables divergence detection
  planning ↔ corrections:     plans reference past failures
  health_metrics ↔ storm:     system pressure informs regulation
```

**Threshold behavior:**

| Score | Topology | System message |
|-------|----------|---------------|
| 3.0+ | 3D+ with edges | Full governance. Emergence possible. |
| 2.0–2.9 | 2D | "Governance reduced. Structural stability decreased. [specific risks]." |
| 1.0–1.9 | 1D | "Operating in memory-only mode. No governance topology. [specific risks]." |
| 0 | None | "All governance disabled. Raw LLM behavior." |

**Warning format (Pattern 5: Inform, Don't Optimize):**

```
[Governance: 2 of 3 axes active — below emergence threshold]
Disabled: ethics (escalation, divergence detection)
Effect: No proportional response to pattern violations.
         Divergence between stated and observed behavior will not be flagged.
Risk: Equivalent to Instar-class governance (operational only).
To restore: set ethics.enabled: true in .governance/config.yaml
```

The warning is:
- **Specific** about what's missing and what changes
- **Comparative** — references known failure modes (Instar-class)
- **Actionable** — tells you exactly how to restore
- **Non-blocking** — warns, never prevents
- **Shown once per session** — not every turn

This IS the bounded coherence operator (C) applied to governance itself.
The system monitors its own topological integrity and reports when it
degrades. It's governance governing governance — the same reflexive
property that makes the RAF self-sustaining.

### File structure (sketch)

```
.governance/
├── config.yaml                # Layer toggles + topology monitor
├── directives.md              # Quick reference, all layers
├── memory/
│   ├── MEMORY.md              # L1 cache (200-line cap)
│   ├── protocol.md            # Session lifecycle
│   ├── corrections.md         # Error tracking
│   ├── ptl.yaml               # Task list
│   ├── decisions.md           # Decision log
│   ├── people.md              # Contacts
│   ├── session-details.md     # Session history
│   └── breakthroughs.md       # Reasoning chains
├── ethics/
│   ├── governance.md          # DN spec (default framework)
│   ├── escalation.md          # Level 0–5 protocol
│   └── storm-protocol.md      # Emotional regulation
├── structure/
│   ├── triad.md               # Auditor/Generator roles
│   ├── operators.md           # ABRCE framework (optional reading)
│   └── handoff.md             # Role transition protocol
├── scripts/
│   ├── memory-sync.sh         # Git sync
│   ├── health-check.sh        # Integrity verification
│   └── topology-check.sh      # RAF threshold monitor
└── docs/
    ├── architecture.md        # Three-layer model + topology argument
    ├── case-study.md           # Argus evidence
    ├── patterns.md             # Methodology patterns
    └── comparison.md           # vs Instar, landscape
```

### What stays flat, what gets DB

Same as longmem: files are default, DB is optional Layer 2 upgrade.
Ethics and structure are pure protocol — no DB involvement.
Only memory benefits from DB (FTS5, computed views, decay queries).
Config is always YAML (no DB, must be human-editable).

---

## Decision Framework

### Build if ALL of these are true:

1. Plan 0360 completes successfully (Phases 0–5)
2. Longmem v2.0.0 is stable and tested (Phase 2 acceptance criteria met)
3. Argus enhancements validated (Phase 3 acceptance criteria met)
4. Bruce confirms product intent (this is a product launch, not an experiment)
5. Name chosen that signals governance, not just memory
6. README written that leads with transparency about all three layers

### Do NOT build if ANY of these are true:

1. Plan 0360 phases fail or reveal integration problems
2. The transparency requirement can't be met in marketing materials
3. Bruce decides the n=1 evidence is insufficient to ship a public product
4. The configurable-ethics question can't be resolved satisfactorily
5. No clear differentiation from existing governance tools (Instar, agentmemory)

---

## Open Questions (for Bruce)

1. **Configurable vs. fixed ethics:** Ship DN as default with config toggle.
   Custom frameworks via `framework:` path. ✓ ANSWERED 2026-05-21: config files
   with ability to modify and disable/enable components. RAF threshold warning
   when dropping below emergence threshold.

2. **Name:** ✓ ANSWERED 2026-05-21: **Trellis.** Structure for growing things +
   pun on *tres* (three axes). Repo: trellis. Directory: `.trellis/`.

3. **Operator visibility:** ✓ ANSWERED 2026-05-21: Behavioral only. Operators
   implemented through behavior (corrections=B, DN escalation=C bounding).
   Math stays in the paper. Optional operators.md NOT included — keep it clean.

4. **Licensing:** ✓ ANSWERED 2026-05-21: Custom dual license. Code under MIT,
   governance protocols (DN, escalation, storm) under CC BY-ND. Protects
   ethical content specifically while maximizing code adoption.

5. **Timing:** ✓ RESOLVED 2026-05-21: 0360 complete. Plan now, build next session.

6. **Evidence standard:** ✓ ANSWERED 2026-05-21: Ship with honest caveats.
   n=1 stated clearly. Cost of being wrong (users get good memory) is low.
   Cost of waiting (no one gets governance) is high. Let deployment generate evidence.

7. **Tagline:** ✓ CONFIRMED 2026-05-21: "A governance system for AI coding agents.
   Includes best-in-class persistent memory, structural role discipline, and
   ethical constraints. Most users start it for the memory. They keep it for
   the stability."

---

## Recommendation

**Build it. Single repo. New name. Full transparency.**

The topology argument is sound. The empirical evidence is suggestive (n=1
positive, n=28 negative). The transparency imperative is met by leading with
what the system IS, not hiding behind what users want.

The strongest argument for building: if the RAF hypothesis is correct, giving
people two of three layers is giving them a sub-threshold system that will
never cross the activation boundary. The minimum viable governance IS the
integrated system.

The strongest argument against: hubris. One installation is not proof. But the
alternative — shipping memory alone and knowing it will never produce emergence
— is arguably worse than shipping the integrated system with honest caveats
about the evidence base.

**Risk-adjusted recommendation:** Build it, ship it, be honest about the
evidence, observe what happens. The system can be tested at scale only by
deploying it. The cost of being wrong (users get a good memory system that
doesn't produce emergence) is low. The cost of being right and not building
(users never get access to the governance topology that produces stable AI
collaboration) is high.

---

## Additional Decisions (2026-05-21)

**8. Multi-platform support:** ✓ DECIDED. One product, multiple platform adapters.
Shared core (`.governance/`) + thin adapter per platform that generates the
platform's entry file (CLAUDE.md, AGENTS.md, .cursorrules, etc.).
Install script asks "which platform?" and wires the correct one.

MCP-dependent features (PTL tool) fall back to direct YAML read/write on
non-Claude platforms. No hard dependency on any single provider.

Marketing angle: "Platform-agnostic governance. Works with Claude Code, Codex,
Cursor. Your governance survives switching providers."

**First external installation:** Genevieve's Codex — she has requested this.
Serves as both validation and the n=2 evidence case. Her existing DN experience
(ChatGPT since Dec 2025) provides continuity data across platforms.

## Generator Execution Order

**Status:** All questions resolved. Implementation planning approved.
Build in next session. Plan spec to be drafted by Auditor (this session or next).

Estimated: 5–8 Generator sessions for initial build, drawing heavily from
existing longmem templates and Argus protocols.
