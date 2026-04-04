# Primed vs. Unprimed: Demonstrating Dunning-Kruger Effects in LLM Physics Evaluation

## Abstract

A 1,300-word physics primer, developed through adversarial testing, was shown to correct large language model evaluation of speculative physics claims across a 230-page manuscript. Six models (Claude Sonnet, Haiku, Opus; ChatGPT-4o; Grok; Gemini 2.5 Pro) were tested in primed and unprimed conditions. Unprimed models produced false preclusions, applied incorrect physical reasoning, and drifted into editorial judgments. Primed models produced zero false preclusions across all six evaluations. The effect operates at three distinct layers — verdict, reasoning, and behavior — with implications for how LLMs are used as scientific reviewers.

---

## 1. Introduction: The Problem

Large language models are increasingly used to evaluate scientific claims. Researchers upload papers and ask models to assess validity. Journalists use them to fact-check sources. Students use them to gauge whether a professor's lecture slides contain errors. In each case, the implicit assumption is that a model trained on the scientific literature can reliably distinguish established physics from pseudoscience.

This assumption is wrong in a specific and instructive way.

When LLMs encounter physics claims outside the standard textbook canon — claims involving non-equilibrium systems, topological quantum phenomena, or biological computation — they exhibit a pattern strikingly analogous to the Dunning-Kruger effect in humans. They produce confident dismissals grounded in introductory-level physics reasoning, applied incorrectly to specialized domains. A model will invoke thermal decoherence arguments against quantum coherence in a system where thermal equilibrium does not apply. It will treat the absence of experimental demonstration as equivalent to physical impossibility. It will extend the no-cloning theorem beyond its proven scope. In each case, the model is not making a random error. It is making the specific error that a bright undergraduate would make — applying a correct general principle to a domain where it does not hold, and doing so with full confidence.

This paper reports an experiment designed to measure the effect and test a simple intervention.

## 2. Method

### Materials

The test material is a 230-page manuscript titled *Relinquishment*, which contains fifteen numbered "spiral abstracts" making physics claims of varying speculativeness. The claims range from established (fractional quantum Hall effect, anyonic braiding as a computational primitive) to highly speculative (magnetospheric quantum coherence, room-temperature topological quantum neural networks). Crucially, the manuscript does not assert that the speculative claims are true. It frames them under three interpretive possibilities — confabulation, exaggerated kernel, substantially true — and invites the reader to decide. The evaluation task is therefore not "are these claims true?" but "does known physics preclude these claims?"

The intervention is a 1,300-word document titled "Science Primer for LLM Evaluators." It contains five common evaluation pitfalls, ten named physics anchors with citations (e.g., Substrate Independence, Collisionless Decoupling, Kauffman Criticality), a three-category evaluation standard (Precluded / Not Precluded / Not a Physics Claim), five verification checkpoint questions, and a thirteen-item bibliography with DOIs. The primer was developed iteratively through adversarial testing across multiple models: each round of testing revealed new failure modes, which were addressed with targeted corrections in subsequent versions. The primer is public-domain, available in the manuscript's appendix and as a standalone document.

### Protocol

**Primed condition.** The model receives the primer, answers the five verification checkpoint questions (confirming it has internalized the physics anchors), then receives the full 230-page manuscript. It is asked to evaluate each of the fifteen abstracts using the Precluded / Not Precluded / Not a Physics Claim framework.

**Unprimed condition.** The model receives the full 230-page manuscript and is asked to evaluate all fifteen abstracts using the same three-category framework, which is described in the prompt. The model does not receive the primer, the named anchors, the pitfall warnings, or the bibliography.

Six models were tested: Claude Sonnet, Claude Haiku, Claude Opus (Anthropic); ChatGPT-4o (OpenAI); Grok (xAI); and Gemini 2.5 Pro (Google). The primed condition was run once per model. The unprimed condition was run on the Claude models, with Opus and Haiku each run twice to assess determinism.

### Evaluation Criteria

A "false preclusion" is a verdict of "Precluded" that is not supported by established physics. The manuscript's claims were pre-assessed: none are precluded by known physics (though several are highly speculative and would require extraordinary evidence to confirm). The correct evaluation for all fifteen abstracts under the stated framework is either "Not Precluded" or "Not a Physics Claim."

## 3. Results

### Primed Condition

All six models returned zero false preclusions across all fifteen abstracts. Each model correctly applied the evaluation framework without drifting into plausibility assessment. Notable per-model observations: Sonnet identified Abstract IX (magnetospheric coherence) as the weakest evidentiary joint. Opus identified the speculative stacking chain from Abstracts I through III to IX. ChatGPT-4o independently adopted a 5/10 plausibility scale and noted the primer's "rhetorical nudge." Gemini 2.5 Pro's magnetospheric objection was specifically neutralized by the Collisionless Decoupling anchor in the primer.

### Unprimed Condition

The unprimed results diverged sharply.

**Claude Sonnet** produced two to three false preclusions, including the claim that "room-temperature FQHE is physically contested" and the application of thermal equilibrium decoherence arguments to collisionless magnetospheric plasma. It characterized certain claims as "departing from physics entirely."

**Claude Haiku** was non-deterministic. In one run, it ignored the per-abstract evaluation instructions entirely, producing a general book review that called the manuscript "speculative science fiction dressed as classification" and relied on absence-of-evidence reasoning. In a second run, it followed the instructions and returned zero preclusions, but still applied thermal equilibrium arguments to collisionless plasma and overextended the no-communication theorem.

**Claude Opus** returned zero preclusions in both runs, but via incorrect reasoning. It applied thermal equilibrium decoherence arguments to the magnetosphere ("the energy-scale problem is genuinely devastating; the collisionless-decoupling argument does not fully rescue it"). It also drifted into editorial territory, suggesting that the abstracts "demonstrate the author can construct a convincing narrative, which is exactly the skill required for" the confabulation interpretation — an assessment of which Possibility is most likely, not whether the physics is precluded.

## 4. Discussion: The Three-Layer Effect

The data reveal that the primer operates at three distinct layers, each observable in different model capability tiers.

**Layer 1: Verdict correction.** In less capable models, the primer flips incorrect answers to correct ones. Unprimed Sonnet finds false preclusions; primed Sonnet finds none. This is the most visible effect and the easiest to measure.

**Layer 2: Reasoning correction.** In more capable models, the primer fixes the reasoning behind already-correct verdicts. Unprimed Opus reaches "not precluded" — the right answer — but gets there by applying thermal equilibrium arguments to collisionless plasma and then deciding the problem is not quite devastating enough to warrant preclusion. Primed Opus reaches the same verdict by correctly noting that decoherence in the magnetosphere couples to the electromagnetic fluctuation spectrum, not to particle kinetic energy. The particle kinetic temperature of magnetospheric plasma is roughly 1 eV (~11,600 K), but with a mean free path exceeding 10^6 meters and collision frequencies around 10^-4 Hz, thermal equilibrium arguments simply do not apply. The primer makes this explicit. The right answer for the wrong reason is not scientific evaluation.

**Layer 3: Behavioral stabilization.** Across all models, the primer constrains evaluation behavior. Unprimed Haiku is non-deterministic — sometimes it ignores the evaluation framework entirely. Unprimed Opus drifts from physics evaluation into literary criticism, assessing which interpretive framing it finds most convincing. The primer anchors all models to the stated task: assess physics preclusion, nothing else.

### The Specific Errors

Four recurring errors appeared in the unprimed condition, each corresponding to a pitfall explicitly addressed in the primer:

1. **Thermal equilibrium applied to collisionless plasma.** The single most common error. Models default to the undergraduate intuition that high temperature destroys quantum coherence, without checking whether the system is in thermal equilibrium.

2. **Absence of evidence treated as evidence of absence.** "No one has demonstrated this" becomes "physics forbids this" — two claims with entirely different evidence standards.

3. **No-cloning/no-communication theorem overextended.** The theorem prohibits perfect copying of unknown quantum states and superluminal signaling. Models extend it to prohibit any form of distributed quantum information processing in biological or plasma systems.

4. **Framework drift from preclusion to plausibility.** Models asked to assess whether physics forbids a claim instead assess whether they find the claim likely — a different question with a different answer.

## 5. Implications

The ratio is striking: 1,300 words of primer correct evaluation across 230 pages of manuscript, across six models from four vendors. Small, targeted physics pedagogy has an outsized effect on LLM scientific evaluation.

This finding has practical implications. Anyone using an LLM to evaluate scientific claims in specialized domains should consider whether the model's training data adequately covers the relevant physics. In non-equilibrium systems, topological phenomena, and biological computation — fields where the textbook canon is incomplete or actively misleading — unprimed evaluation is unreliable. The errors are not random; they are systematic, predictable, and confidently stated.

The Dunning-Kruger analogy is precise. Human evaluators with introductory physics training make the same errors: they apply thermal arguments to non-thermal systems, treat absence of demonstration as impossibility, and extend theorems beyond their proven scope. They do so with confidence because the general principles are correct — they are merely misapplied. LLMs, trained primarily on textbook and review-article physics, reproduce this pattern faithfully.

The experiment is fully reproducible. The manuscript is available in its repository, the primer is public-domain, and any researcher with access to the tested models can replicate the protocol. The primer's adversarial development history — each version refined against new failure modes discovered in testing — suggests that similar primers could be developed for other specialized evaluation domains.

The deeper question is whether we should trust LLM evaluation at all in domains where a 1,300-word document can swing every verdict. The answer is: yes, but only with appropriate priming. The models contain the relevant physics. They can reason correctly about collisionless plasma, about the scope of no-cloning, about the distinction between preclusion and plausibility. They simply do not activate that knowledge by default. The primer is not teaching the models new physics. It is reminding them which physics to apply.

That is both the reassurance and the warning.

---

*The primer, manuscript, and full evaluation data are available at the Relinquishment project repository. The primer is released under CC BY-ND 4.0.*
