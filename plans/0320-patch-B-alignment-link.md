---
Plan-UID: 0320-v6 Patch B
Status: READY FOR GENERATOR
---

# Patch B: Link Alignment Demo from White Paper

## What to modify

File: `~/software/persistent-ai-collaboration/index.html`

## Two insertion points

### 1. In the Honest Costs section, after the paragraph about the obvious question ("Partly, they are...")

Insert one paragraph (~50 words) after the paragraph that discusses how the hard parts resist productization. The point: the governance architecture described in this paper has a natural complement — a mathematical framework that can detect alignment drift in transformer internal states, operating below the output layer. Link to the demo. Tone: matter-of-fact, not salesy. This is "here's what exists" not "buy our thing."

Content direction: "The governance architecture described here operates at the application layer — system prompts, memory files, behavioral rules. A complementary approach monitors the model layer directly, using relational mathematics to detect internal structural drift that output metrics cannot see. A working demonstration exists: [ABRCE Alignment Drift Detection](https://github.com/Relational-Relativity-Corporation/abrce-alignment-demo). The mathematical formalism is published at [arXiv:2601.22389](https://arxiv.org/abs/2601.22389)."

### 2. In the References accordion (Technical Citations), add a bibliography entry

After the existing Anthropic entry, add:

Stephenson, B. & Macomber, R. (2026). *ABRCE Alignment Drift Detection: Cross-Domain Generalizability Demonstration*. Metatron Dynamics. [github.com/Relational-Relativity-Corporation/abrce-alignment-demo](https://github.com/Relational-Relativity-Corporation/abrce-alignment-demo). Mathematical formalism: [arXiv:2601.22389](https://arxiv.org/abs/2601.22389).

And add a Component Provenance bullet:

**Alignment drift detection:** ABRCE operators applied to transformer internal states detect structural deviation that output metrics are blind to. 31 of 43 escalation sequences triggered field alarms without output degradation. Working demonstration on Phi-3 Mini (model-agnostic). Published: arXiv:2601.22389.

## Voice

Match existing register. One factual paragraph, no hype. The demo speaks for itself — link it and move on.

## Constraints

- Do NOT modify any other content
- Keep insertion 1 to a single short paragraph
- Keep insertion 2 to one bibliography entry + one provenance bullet

## Report format

"Plan-UID: 0320-v6 Patch B complete. Two insertions at [line numbers]."
