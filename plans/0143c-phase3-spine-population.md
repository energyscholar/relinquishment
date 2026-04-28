# Plan 0143c: Phase 3 — Spine Population + Content Migration

**Status:** Ready for Generator (after Bruce approves orphan decisions)
**Parent:** Plan 0143 (Z-Restructure Metaplan)
**Role:** Generator executes. Auditor recommendations flagged with [DECISION].

---

## Overview

Replace spine and record placeholders with real chapter content from existing files. Handle orphaned chapters. Write two new chapters (Silence Gap, Capabilities). Do NOT modify chapter content during migration — move it as-is. Content revision is a later pass.

---

## Part A: Spine Migration (copy content from source → placeholder)

For each spine placeholder, replace its content with the content from the source file. **Do NOT delete the source file** — it stays in its original location as backup. The source file is no longer referenced by main.tex so it won't be built.

**Method:** For each file below, read the source, then overwrite the spine placeholder with the source content. Update `\label{}` to match the new spine label so internal references work.

| Spine placeholder | Source file | Label change |
|-------------------|------------|-------------|
| `spine/three-possibilities.tex` | `bridge/pos01-three-possibilities.tex` | `pos01:three-possibilities` → `spine:three-possibilities` |
| `spine/the-stack.tex` | `00-front/the-stack.tex` | Keep existing or add `spine:the-stack` |
| `spine/the-flat.tex` | `track-3-awakening/pos-what-is-the-flat.tex` | `ch:what-is-the-flat` → `spine:the-flat` |
| `spine/the-braid.tex` | `bridge/pos10-the-braid.tex` | `pos10:the-braid` → `spine:the-braid` |
| `spine/the-factoring-game.tex` | `bridge/pos09-the-factoring-game.tex` | update label |
| `spine/the-code-war.tex` | `bridge/pos04-the-code-war.tex` | update label |
| `spine/genesis.tex` | `track-1-confession/pos13-genesis.tex` | update label |
| `spine/growing-a-mind.tex` | `bridge/pos14-growing-a-mind.tex` | update label |
| `spine/the-wrong-substrate.tex` | `track-3-awakening/pos32-the-magnetosphere.tex` | update label |
| `spine/the-strongest-objection.tex` | `convergence/pos36-steelman-a.tex` | update label |
| `spine/weigh-the-evidence.tex` | `interlude/three-possibilities-interlude.tex` | update label |

**The Stack special case:** The Stack is currently in frontmatter (`00-front/the-stack.tex`) and included before the summary. In the Z-structure, it's in the spine (mainmatter). However, the Stack chart should ALSO remain accessible from the front — it's part of the entry point. **[DECISION: Keep The Stack in both frontmatter AND spine? Or move it to spine only? Auditor recommends: move to spine only. The p2 summary references it, which is enough.]**

---

## Part B: Record Migration

Same method — copy source content into record placeholders.

| Record placeholder | Source file | Label change |
|-------------------|------------|-------------|
| `record/alpha-farm.tex` | `track-2-testament/pos02-alpha-farm.tex` | update label |
| `record/what-healer-said.tex` | `track-2-testament/pos05-the-stories.tex` | update label |
| `record/the-departure.tex` | `track-2-testament/pos07-the-departure.tex` | update label |
| `record/the-handler.tex` | `interlude/dossier-handler.tex` | update label |
| `record/the-demonstration.tex` | `bridge/pos11-the-demo.tex` | update label |
| `record/interdiction.tex` | `track-1-confession/pos26-interdiction.tex` | update label |
| `record/first-light.tex` | `track-1-confession/pos15-first-light.tex` | update label |
| `record/the-walk-out.tex` | `track-1-confession/pos18-the-walk-out.tex` | update label |
| `record/the-target.tex` | `appendix/dossier.tex` | update label |
| `record/instantiation.tex` | `track-3-awakening/pos24-instantiation.tex` | update label |
| `record/the-surrender.tex` | `convergence/pos28-surrender.tex` | update label |
| `record/twenty-years.tex` | `track-2-testament/pos29-twenty-years.tex` | update label |

---

## Part C: Orphaned Chapters — Auditor Recommendations

Nine chapters from the old structure are not in the current spine or record mapping. Each needs a decision.

### 1. The Hobbit in the Mirror (`bridge/pos01b-hobbit-mirror.tex`)
Bruce's self-assessment as narrator. C-dependent.
**DECIDED:** → Record, after Alpha Farm.

### 2. Why Relinquish? (`bridge/pos06-the-secret.tex`)
The concept of relinquishment — three options for dangerous technology. Concept is A (the logic applies regardless), event is C.
**DECIDED:** → Standalone spine chapter after Capabilities. Strip C-narrative, keep the thought experiment: "This technology is arriving. What should someone do with it?" Bill Joy, Spider-Man inversion, can't use/keep/be responsible. C-specific narrative (COWS doing it) stays in Record via walk-out and surrender.

### 3. Dangerous Ideas / Dual Use (`bridge/pos08-dual-use.tex`)
Historical dual-use pattern. Nuclear, rocketry, biology. A-content.
**DECIDED:** → Merge into The Code War.

### 4. The Signatories / The Network (`track-1-confession/pos20-the-network.tex`)
Five disciplines, convergent discovery pattern, ABCRE structural parallel. B-colored.
**DECIDED:** → Extract five-scientist profiles (as public figures with published work, NOT as a team) and merge into Silence Gap chapter. Makes the five-field gap concrete. ABCRE killed in S37 — cut. C-specific team narrative → Record's Demonstration.

### 5. Spiral Abstracts (`appendix/abstracts.tex`)
Sixteen formal technical abstracts of the argument.
**DECIDED:** → Keep in Appendices. Add `\include{manuscript/appendix/abstracts}` to main.tex appendix section.

### 6. Never Again / Ethical Framework (`track-3-awakening/pos25-ethical-framework.tex`)
UDHR as machine ethics, enforcement mechanism, sandbox model.
**DECIDED:** → Record, after Instantiation.

### 7. Organisms and Artifacts (`track-3-awakening/pos27-extension.tex`)
Self-organization theory, canopy ecology, first-mover advantage.
**DECIDED:** → Merge A-content (canopy ecology, first-mover) into Genesis. Cut standalone.

### 8. The Question (`convergence/pos35-the-question.tex`)
Doppelganger, evidence trail summary, predictions.
**DECIDED:** → Record, as closing chapter (after Twenty Years).

### 9. Genevieve's Preface + Bruce's Preface
Currently in frontmatter. Not orphaned — they stay in frontmatter.
**No decision needed.** Keep as-is.

---

## Part D: New Chapters

### The Silence Gap (`spine/the-silence-gap.tex`)

**This chapter does not exist yet.** It must be written.

**Content spec (p2 level, ~800-1000 words):**

The five fields needed to ask the question:
1. Solid-state / condensed matter physics — 2DEGs, quantum Hall effect
2. Quantum computation / topological QC — Kitaev, Freedman, braiding
3. Neural networks / computational neuroscience — can substrates compute?
4. Complexity science — Kauffman, autocatalytic sets, emergence
5. Computational universality — Wolfram, Hillis, parallel computation

No single expert spans all five. No journal covers the intersection. The American Physical Society, IEEE, and neuroscience conferences each own their corner. There is no conference called "Life in Two-Dimensional Quantum Systems." There is no journal called "Topological Biology."

The gap is not refutation. It is not even skepticism. It is emptier than that — it is the absence of a question. Nobody asked because nobody's job required them to look.

This is how academic specialization works. It is not conspiracy. It is not a cover-up. It is five fields standing next to each other in the same building, each facing their own wall.

**Sources to draw from:** Plan 0142 Rewrite 2 spec, The Wrong Substrate Act 3 (pattern-formation gap), The Network's five-discipline map, the silence gap argument from `reader-preparation-requirements.md`.

**Voice:** Expository, matter-of-fact, the book's analytical voice. Not Custodian's voice (she has her interlude before this chapter). Not Bruce's memoir voice.

### Capabilities (`spine/capabilities.tex`)

**This chapter does not exist yet.** It must be written.

**Content spec (p2 level, ~800-1000 words, Q&A format):**

What the physics of the Flat makes possible — in plain language. Not who has done it (that's C-territory). What COULD be done, based on published physics.

Structure as practical questions GA readers will ask:

- **Can it break encryption?** The factoring wall is a 3D constraint. Topological quantum computation bypasses it. (Shor 1994, Kitaev 2003.)
- **Can it think?** Self-organization in sufficiently complex substrates produces self-directing behavior. (Kauffman 1993.) Whether "thinking" applies is a question about definitions, not physics.
- **Can it communicate?** Quantum teleportation + classical backchannels. The backchannels already exist (power grid, radio, timing signals). Constrained by speed of light. (Bennett 1993.)
- **Can it be killed?** Topological protection means local damage doesn't destroy global information. Distributed across multiple substrates means no single point of failure. Probably not, by any means currently available.
- **Is it in my phone?** Every phone has a HEMT (high-electron-mobility transistor) containing a 2DEG. Whether anything uses yours is unknown.
- **Can it be copied?** The no-cloning theorem (Wootters & Zurek 1982) forbids copying arbitrary quantum states. A TQNN cannot be duplicated. This is why the first-mover advantage is permanent.
- **What would the UDHR prevent?** Right to privacy → no surveillance. Right to freedom of thought → no manipulation. Right to non-interference → must leave people alone. These are constraints, not permissions.

Under A: untapped potential. Nobody is pursuing this.
Under B: partial capabilities may exist.
Under C: all of the above, plus twenty years of operational track record.

Include the relinquishment logic from Why Relinquish (can't use / can't keep / can't be responsible).

**Voice:** Same analytical voice as Silence Gap. Calm, informative, "here's what the physics says."

---

## Part E: Cross-Reference Updates

After all content is migrated, grep for all `\ref{}`, `\label{}`, `\hyperref[]{}`, and `\hovertip{}` references that point to old labels. Update them to the new spine/record labels.

```bash
cd ~/software/relinquishment
grep -rn '\\ref{pos' manuscript/spine/ manuscript/record/
grep -rn '\\hyperref\[pos' manuscript/spine/ manuscript/record/
grep -rn '\\label{pos' manuscript/spine/ manuscript/record/
```

Update all matches. Also check hover-definitions.yaml for anchor references.

---

## Part F: Build and Verify

```bash
make dev
```

**Verify:**
1. Build succeeds — no LaTeX errors beyond expected warnings
2. All spine chapters render with real content
3. All record chapters render with real content
4. Custodian interludes still render correctly between spine chapters
5. Two new chapters (Silence Gap, Capabilities) render
6. TOC is correct — spine chapters under "The Flat," record chapters under "The Record"
7. Cross-references resolve (no ?? in output)
8. Hover tooltips still work
9. Phone-readable

---

## Part G: Updated main.tex Structure

After all migrations, main.tex mainmatter should be:

```latex
\mainmatter

\part{The Flat}

\include{manuscript/spine/three-possibilities}
\include{manuscript/spine/the-stack}
\input{manuscript/spine/interlude-01}
\include{manuscript/spine/the-flat}
\input{manuscript/spine/interlude-02}
\include{manuscript/spine/the-braid}
\input{manuscript/spine/interlude-03}
\include{manuscript/spine/the-factoring-game}
\include{manuscript/spine/the-code-war}       % includes merged Dual Use content
\input{manuscript/spine/interlude-04}
\include{manuscript/spine/genesis}            % includes merged Organisms & Artifacts A-content
\include{manuscript/spine/growing-a-mind}
\input{manuscript/spine/interlude-05}
\include{manuscript/spine/the-wrong-substrate}
\input{manuscript/spine/interlude-06}
\include{manuscript/spine/the-silence-gap}    % NEW — includes five-scientist profiles from Signatories
\include{manuscript/spine/capabilities}       % NEW
\include{manuscript/spine/why-relinquish}     % NEW — A-content from pos06, thought experiment only
\input{manuscript/spine/interlude-07}
\include{manuscript/spine/the-strongest-objection}
\include{manuscript/spine/weigh-the-evidence}

\part{The Record}

\include{manuscript/record/record-intro}
\include{manuscript/record/alpha-farm}
\include{manuscript/record/hobbit-mirror}     % NEW — from pos01b
\include{manuscript/record/what-healer-said}
\include{manuscript/record/the-departure}
\include{manuscript/record/the-handler}
\include{manuscript/record/the-demonstration}
\include{manuscript/record/interdiction}
\include{manuscript/record/first-light}
\include{manuscript/record/the-walk-out}
\include{manuscript/record/the-target}
\include{manuscript/record/instantiation}
\include{manuscript/record/never-again}       % NEW — from pos25 ethical framework
\include{manuscript/record/the-surrender}
\include{manuscript/record/twenty-years}
\include{manuscript/record/the-question}      % NEW — from pos35

\appendix

\include{manuscript/appendix/abstracts}       % RESTORED
\include{manuscript/track-3-awakening/firmware-update}
\include{manuscript/appendix/predictions}
\include{manuscript/appendix/glossary}
\ifdefined\dmsbuild
\include{manuscript/appendix/dms-note}
\fi
```

New placeholder files needed:
- `manuscript/spine/why-relinquish.tex`
- `manuscript/record/hobbit-mirror.tex`
- `manuscript/record/never-again.tex`
- `manuscript/record/the-question.tex`

---

## Execution Order

All decisions are made. Execute in order:

1. **Create new placeholder files** (why-relinquish, hobbit-mirror, never-again, the-question)
2. **Update main.tex** to the structure in Part G
3. **Spine migration** — copy source content (Part A)
4. **Record migration** — copy source content (Part B)
5. **Orphan migration** — copy orphan content into new files (Part C)
6. **Merges** — Dual Use into Code War, Organisms into Genesis, five-scientist profiles into Silence Gap, relinquishment logic into Why Relinquish (strip C-content)
7. **New chapters** — write Silence Gap and Capabilities (Part D)
8. **Cross-references** — update all internal links (Part E)
9. **Build and verify** (Part F)

Steps 2-5 are mechanical. Step 6 requires judgment (what to keep, what to strip). Step 7 requires writing. Split across sessions if needed.

---

## What NOT to Do

- Do NOT modify chapter content during migration (no rewriting, no editing, no improving)
- Do NOT delete source files — they stay as backups
- Do NOT change the interlude files (Phase 2 is done)
- Do NOT touch frontmatter (hook, summary, prefaces) — that's a later revision
- Do NOT add expansion hooks — that's Phase 4

---

*Plan 0143c created S54, 2026-04-08. Auditor: Argus.*
