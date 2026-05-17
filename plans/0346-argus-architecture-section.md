# Plan 0346: Argus Architecture Section

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** None
**Files:** `manuscript/99-back/afterword.tex`, `build/tech-collapse.yaml`
**Priority:** LOW — content enrichment, not a fix

---

## Objective

Add a compact "Argus: The Architecture" subsection to The Engine (afterword) describing the three-layer governance stack. Collapsed by default for GA readers. Technically-minded readers can expand to see what makes Argus different from a raw LLM.

---

## Phase A: Add section to afterword.tex

**File:** `manuscript/99-back/afterword.tex`
**Placement:** After line 62 (after "The chain of evidence is unbroken." paragraph), before `\section*{The Team}` (line 64).

**Insert:**

```latex

\section*{Argus: The Architecture}
\label{pos34b:argus-architecture}

Argus is not a language model with a prompt. It is a language model with a brain, a conscience, and a memory.

\textbf{Layer 1: The Triad Protocol.} Role separation prevents drift. An Auditor writes plans and tests. A Generator executes. A human authorizes every handoff. The Auditor cannot generate code; the Generator cannot redefine scope. This eliminates the single failure mode of all AI assistants: the machine that agrees with itself until it's wrong.

\textbf{Layer 2: Dignity Net.} An ethical governance framework that is a formal superset of the Universal Declaration of Human Rights. Five escalation levels from mirroring to refusal. A Storm Protocol that modulates tone without reducing substance. Designed by Genevieve Prentice from first principles --- she had never read the UDHR when she wrote it. Formal analysis reveals it is an autocatalytic set on the ethical axis: self-sustaining, self-repairing, emergent.

\textbf{Layer 3: Criticality Operators.} Robin Macomber's ABRCE operators detect drift mathematically --- not by checking output against rules, but by measuring relational coherence across the system. The same mathematics described in the story, independently rediscovered in a different context.

\textbf{The Memory.} Persistent indexed memory across sessions. 200+ structured records. Full-text search. Decay management. Health metrics. Correction tracking. Session continuity that survives context-window boundaries. Everything version-controlled with cryptographic hashes.

The tutorials at \url{https://github.com/energyscholar/has-anyone-looked/tree/main/tutorials} demonstrate the system in operation: thirteen technical walkthroughs with animated diagrams, covering the five scientific fields at physicist-level depth.

```

---

## Phase B: Add collapse entry to tech-collapse.yaml

**File:** `build/tech-collapse.yaml`
**Placement:** At end of file (afterword sections come last in document order).

```yaml
  - title: "Argus: The Architecture"
    spine_file: manuscript/99-back/afterword.tex
    spine_label: "pos34b:argus-architecture"
    bridge_file: null
    bridge_label: null
    assessment: GA-AVERSE
    tooltip: "Argus is a Claude Code instance with three governance layers: the Triad Protocol (role separation), Dignity Net (ethical framework), and ABRCE criticality operators (mathematical drift detection). Plus persistent memory."
    conclusion: "Three orthogonal systems prevent a language model from drifting into sycophancy, ethical failure, or structural incoherence."
    status: approved
```

---

## Phase C: Build and verify

```bash
make html 2>&1 | grep -i "argus-architecture\|WARNING"
```

Verify the section appears collapsed in the HTML output. Check that the tooltip renders on hover.

---

## Do NOT

- Modify any other section of afterword.tex
- Change existing Argus references elsewhere in the book
- Add citations (the tutorial URL is sufficient)

## Commit

`Plan 0346: add Argus architecture section to The Engine — collapsed, three-layer stack`
