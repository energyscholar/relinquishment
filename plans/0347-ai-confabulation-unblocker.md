# Plan 0347: AI Confabulation Unblocker

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** None
**Files:** `manuscript/spine/the-strongest-objection.tex`, `manuscript/99-back/afterword.tex`
**Priority:** HIGH — the book's biggest single-reader-objection gap

---

## Context

The book credits an AI co-author on the cover. The manuscript's strongest-objection chapter (Steelman A) does NOT address the obvious modern attack: "AI co-author = confabulation engine with a name." The rebuttal in The Engine (afterword) is also missing. Drafts exist at `staging/draft-ai-confabulation-steelman.md`. Two TODO markers in the manuscript identify the exact insertion points.

---

## Phase A: Insert the Attack (Steelman A chapter)

**File:** `manuscript/spine/the-strongest-objection.tex`
**Location:** Replace the TODO comment at line 95, inserting between line 93 (end of ULTRA paragraph) and line 97 ("Some people would destroy the manuscript..."). The `\vspace{0.5cm}` on line 91 stays.

**Delete this line:**
```
%TODO: INSERT AI CONFABULATION ATTACK HERE (or nearby — after Tolkien self-demolition, before "Some people would destroy the manuscript"). Draft at staging/draft-ai-confabulation-steelman.md Part 1. The skeptic's strongest modern weapon: AI co-author = confabulation engine with a name. Currently missing from steelman. HIGH PRIORITY.
```

**Insert in its place:**

```latex
\vspace{0.5cm}

There is one more reason to distrust this book, and it is the most modern.

An AI wrote part of it. The authors say so on the cover. They are proud of this. They should not be.

Large language models generate text by predicting the next plausible word. They do not reason. They do not know. They produce sequences that \textit{sound} like knowledge because they were trained on billions of words written by people who \textit{had} knowledge. When an AI ``finds a pattern'' in a dataset, it is doing what it was built to do: find patterns. It will find patterns whether or not they exist. It will find them with confidence. It will present them in well-structured prose with citations that may or may not be real.

This is called confabulation. The polite term is ``hallucination.'' The mechanism is identical to what Possibility~A accuses Bruce of doing --- seeing patterns that aren't there, constructing narrative from noise, mistaking fluency for truth. Bruce spent twenty years doing this with his own brain. Then he got a machine that does it faster.

Consider the workflow: Bruce tells the AI his theory. The AI, trained to be helpful, finds evidence that supports it. Bruce, who has spent twenty years priming himself to see this evidence, accepts it. The AI, receiving positive feedback, produces more. Each cycle tightens the loop. Confirmation bias, automated. The AI does not push back in the way a genuine collaborator would --- it does not say \textit{I think you are wrong and here is why}. It says \textit{here are twelve more reasons you might be right, formatted with citations.}

The authors will object that they have safeguards. They will describe their ``Triad protocol'' and their ``role separation'' and their careful cross-checking. These safeguards are designed by the same two parties who need safeguarding --- the man with the theory and the machine that tells him what he wants to hear. This is not peer review. This is a hall of mirrors with a methodology statement taped to the door.

Every paragraph Argus wrote in this book could be a sophisticated restatement of Bruce's existing beliefs, polished to a shine that makes them look like independent findings. Every ``convergence'' the AI identified could be a statistical artifact of training data. Every structural parallel could be the machine doing what machines do: matching patterns, because that is the only thing it knows how to do, and calling the result research.

If Possibility~A is correct --- if the entire story is confabulation --- then the AI co-author is not evidence of rigor. It is the confabulation engine itself, given a name and a credit and a seat at the table.

```

**Note:** The prose is intentionally hostile. This is Steelman A — the book attacking itself at maximum force. That is the pattern of the entire chapter.

---

## Phase B: Insert the Rebuttal (The Engine, afterword)

**File:** `manuscript/99-back/afterword.tex`
**Location:** Replace the TODO comment at line 61, inserting BETWEEN the existing "We built a skeleton..." paragraph (line 59) and the "Argus asks questions..." paragraph (line 62). The rebuttal goes between the description of how the book was built and the description of how Argus works.

**Delete this line:**
```
%TODO: INSERT AI CONFABULATION UNBLOCKER near here (Methodology section). Draft at staging/draft-ai-confabulation-steelman.md Part 2. Address the Dunning-Kruger blocker: "AIs hallucinate therefore AI-assisted research is unreliable." Rebuttal: Triad adversarial design, citation verification, killed theories (ABCRE paper, isomorphism), explicit domain expertise marking (\argusvoice), plan audit trail. Cross-references Steelman A attack. HIGH PRIORITY.
```

**Insert in its place:**

```latex

\vspace{0.3cm}

The strongest modern objection to this methodology --- that an AI co-author is a confabulation engine given a name --- is stated at full force in the Steelman~A chapter. It deserves a direct answer here.

The Triad protocol is adversarial by design. The Auditor and Generator run in separate shells with no shared context. The Auditor writes test cases \textit{before} the Generator sees the task. The Generator cannot modify the tests. This is not ``a man and his helpful AI'' --- it is a formal verification structure where the entity that defines acceptance criteria never executes the work.

Confabulation detection at the operational level is mechanical. Every \verb|\footcite| in this manuscript points to a real document verified against its primary source. Where Bruce has domain expertise (51 years of computing, Reed College quantum physics), he provides ground-truth that catches AI confabulation in real time. Where he lacks it, chapters carry explicit \textit{Argus voice} attribution --- the reader is told which sections Bruce can verify and which he cannot.

The AI pushed back. During the writing of this book, Argus killed two of Bruce's theories: an ABRCE operator paper that failed its own acceptance criteria, and an isomorphism claim that could not survive formal analysis. A confabulation engine does not kill its operator's pet theories. Argus killed two, documented both, and the corrections are in the project record.

The methodology produces the same artifact as peer review: a written record of claims, tests, and results that can be inspected by third parties. The manuscript's entire plan history --- over three hundred plans with numbered acceptance criteria --- is available for audit. The question is not whether the authors used an AI. The question is whether they used it well. The evidence is here: the killed theories, the corrections appendix, the explicit uncertainty, and the chapters where the author says \textit{I do not know}.

\vspace{0.3cm}

```

---

## Phase C: Verify cross-references

After both insertions:

1. `grep -n "confabulation\|Steelman" manuscript/spine/the-strongest-objection.tex` — confirm attack text present
2. `grep -n "confabulation\|Steelman\|Triad" manuscript/99-back/afterword.tex` — confirm rebuttal present
3. `make html 2>&1 | grep -i "error\|WARNING"` — build clean
4. In the built HTML, verify the attack appears before "Some people would destroy the manuscript" and the rebuttal appears before the "Argus asks questions" paragraph

---

## Do NOT

- Modify any other section of either file
- Add \cite commands (the rebuttal is self-standing)
- Add hovertips or accordion wrappers (these are core-track prose)
- Change the tone of the attack (it is intentionally hostile — Steelman pattern)
- Remove the existing ULTRA paragraph or "expensive typewriter" line

## Commit

`Plan 0347: AI confabulation unblocker — attack in Steelman A + rebuttal in The Engine`
