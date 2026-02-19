# Plan 0018: DMS MVP Content Import

**Date:** 2026-02-19
**Author:** Nightstalker (Auditor)
**Purpose:** Import staging content and add front matter to produce a substantive PDF for deadman's switch distribution before Bruce's dental surgery on 2026-02-20.
**Quality target:** Insurance, not publication. A reader who decrypts this PDF should be able to understand the story, the three possibilities, the predictions, and the key evidence. Not polished prose — readable source material.

---

## Context

The relinquishment PDF currently has 137 pages, 389KB. It contains:
- **11 populated chapters** with real prose (pos01, pos02, pos04, pos05, pos08, pos13, pos14, pos22, pos24, pos28 — plus pos05 is extensive)
- **26 stub chapters** containing only `[Content to be written per Plan 0007]`
- **Good front matter:** preface, how-to-read, copyright, not-claimed
- **Full appendices:** predictions, abstracts, glossary, timeline, sources, verification

The 26 stubs make the PDF feel empty. 25 of them have corresponding staging files in `manuscript/staging/raw/` containing source material. The staging files are **source dossiers**, not polished prose — they contain YAML metadata, source attributions, and raw excerpts from Bruce's documents. Some excerpts are genuine narrative prose; others are analytical bullet points.

**DMS recipients (Schneier, Doctorow) need a PDF where the story is comprehensible.** They don't need publication quality. They need enough content that, if published, a reader can understand what this book is about.

---

## Architecture

**4 phases. Build and verify after each phase. Commit after each phase.**

### Phase 1: Front Matter (11 items)
### Phase 2: Priority Content Import (10 chapters — the ones with the most importable prose)
### Phase 3: Secondary Content Import (15 chapters — lighter touch)
### Phase 4: Build, Verify, Hash

---

## Phase 1: Front Matter

### Generator Conventions (apply to ALL phases)

**Proposition, not claim:** When describing Bruce's interpretations in chapters (pos01-pos35) and front matter, use "proposition" instead of "claim." Example: "Bruce's proposition that COWS built a TQNN" not "Bruce's claim." This applies to new framing text AND imported source material in chapters. **EXCEPTION: Appendices preserve Bruce's original wording exactly — no word substitution. Appendices are archival evidence.**

**First-person voice:** All front matter and introduction content uses first-person ("I", "my mentor") to match the preface. Do not use third-person "Bruce" in the author's own voice.

**Recovery protocol for Runs 1, 5, 11:** These runs create new .tex files AND modify main.tex. If a run fails partway, run `git revert HEAD` before retrying. Do NOT re-run on top of partial state.

**Source annotations (pdfcomment):** At every point where staging content is imported into a chapter .tex file, add a PDF annotation using `\srcnote{}` (defined in preamble.tex). Format: `\srcnote{filename | staging/raw/posNN-name.md | YYYY-MM-DD | brief description}`. These annotations are invisible to casual readers but accessible via any PDF viewer's annotation panel. They provide provenance metadata for researchers. Place the `\srcnote{}` call at the START of each imported block, before the first line of imported text.

### 1-PRE. Add Redaction Macro and Source Annotations to Preamble

Add the following to `build/preamble.tex` (after existing macro definitions):

```latex
% DMS redaction marker — used for WikiLeaks-sensitive content
\newcommand{\DMSRedacted}[1]{%
  \begin{quote}
  \textit{[REDACTED --- #1]}
  \end{quote}
}
```

Both Run 5 (pos29) and Run 8 (pos20) use this macro for consistent redaction formatting.

Also add source annotation support to `build/preamble.tex` (after the `\usepackage{cleveref}` line):

```latex
% Source provenance annotations — hidden PDF notes at import points
% Visible in PDF viewer annotation panels; invisible to casual readers
\usepackage{pdfcomment}
\newcommand{\srcnote}[1]{\pdfcomment[icon=Note,color=yellow]{#1}}
```

### 1-HOW. Add Source Annotations Note to How-to-Read

Append the following to `manuscript/00-front/how-to-read.tex`, after the existing track-stripe itemize block:

```latex
\vspace{1cm}

\subsection*{A note for researchers}

This PDF contains hidden annotations at every point where source material was imported. These annotations record the original filename, archive location, date, and a brief description. In most PDF viewers, you can access them through the annotations or comments panel. They are invisible during normal reading.

If you are investigating the provenance of any passage, the annotation at that location will tell you where the text came from.
```

### 1-GEN. Add Genevieve Prentice's Preface

Create `manuscript/00-front/genevieve-preface.tex` with the content below.

**Content for genevieve-preface.tex:**

```latex
\chapter*{Preface to the Early Draft}
\addcontentsline{toc}{chapter}{Preface to the Early Draft}

My name appears on this early draft not because I wrote the narrative or the scientific claims. I did not. When Bruce first described the scope of this work to me, I told him---more than once---that it would make a gripping Tom Clancy--style novel. Its scale felt cinematic. He chose instead to pursue it as an intellectual problem and to write it as such.

This document is a draft. I have read portions of it, particularly narrative sections, but I have not reviewed the manuscript in its entirety.

Bruce does not present this work as settled fact. He examines a body of material and interpretation whose ultimate status remains open. It may be mistaken, partially valid, or entirely correct. The manuscript is an exploration, not a declaration of certainty. Any external events---including unexpected ones---should not be taken as confirmation of its propositions. Ambiguity requires restraint in interpretation.

My academic background is in psychology, with earlier study in phenomenology and language. I am not a physicist, mathematician, or professional programmer. I approached this project as a careful reader concerned with clarity: what is documented fact, what reflects established physics, and where interpretation begins.

Over the past several months, I developed a framework called the Dignity Net while working with large language models during drafting. I offered this framework to help clarify distinctions in this draft---to label sourced material, separate accepted scientific principles from theoretical extensions, and reduce the risk of conflating evidence with interpretation. The framework does not determine whether the theories are correct. It is intended to keep those boundaries visible.

Responsibility for the scientific arguments, interpretations, and conclusions rests entirely with Bruce Stephenson.

This statement reflects the full extent of my role in this draft.

\vspace{0.5cm}
\hfill\textit{Genevieve Prentice, February 2026}
```

### 1-PREFACE. Strip A/B/C Detail from Bruce's Preface

The current preface (manuscript/00-front/preface.tex) explains Options A, B, C in full paragraphs. Since the Introduction now carries the detailed A/B/C explanation, strip the preface to mention the concept briefly without re-explaining each option.

Replace lines 10-17 (from `I cannot tell you which of the following is correct:` through the end of Option C) with:

```latex
I cannot tell you whether the story is true. It may be fabrication, exaggeration, or entirely real. I have maintained genuine uncertainty about these three possibilities for more than twenty years. The Introduction that follows explains them in detail.
```

Keep everything else in preface.tex unchanged (lines 1-9, 18-33).

### 1-COPYRIGHT. Narrow AI Disclosure on Copyright Page

In `manuscript/00-front/copyright.tex`, replace line 43:
```
Structure and research developed with AI assistance (Claude, Anthropic). All narrative prose, claims, evidence assessments, and editorial decisions are the author's. Session transcripts are included in the appendix.
```
with:
```
Structure and organization developed with AI assistance (Claude, Anthropic). All research, narrative prose, evidence assessments, and editorial decisions are the author's.
```

### 1-TITLE. Update Title Page

In `manuscript/00-front/title.tex`, update the byline to:
```
Written by Bruce Stephenson with Genevieve Prentice
```

### 1-MAIN. Update main.tex Front Matter Order

Replace the front matter includes (lines 35-36) with the following EXACT sequence:

```latex
\include{manuscript/00-front/genevieve-preface}
\include{manuscript/00-front/preface}
\include{manuscript/00-front/not-claimed}
\include{manuscript/00-front/introduction}
\include{manuscript/00-front/corrections}
```

This produces the reading order: Genevieve's preface → Bruce's preface → What This Book Does Not Claim → Introduction → What I Got Wrong → then pos01 (Three Possibilities).

### 1A. Add Introduction

Create `manuscript/00-front/introduction.tex` with the content below. This is the book summary written for Genevieve Prentice that Bruce approved as "That's the intro!"

**Do NOT modify main.tex here — 1-MAIN already handles the include order.** The introduction appears in the sequence: not-claimed → introduction → corrections (per 1-MAIN).

**Content for introduction.tex** (convert from the markdown below to LaTeX):

```
\chapter*{Introduction}
\addcontentsline{toc}{chapter}{Introduction}
```

Then convert the following to LaTeX prose (use the formatting patterns from pos04-the-code-war.tex as a model — smart quotes, em dashes, section breaks, etc.):

---BEGIN INTRODUCTION CONTENT---

## What happened (or didn't)

Between 2003 and 2006, Bruce's mentor — a man he calls "Healer" — engaged him in a series of conversations about publicly available science. The conversations were not random. They followed a specific sequence: topology, quantum mechanics, computation, biology, ethics. Healer never told Bruce anything classified. But the sequence was designed so that Bruce would deduce, on his own, the existence of a classified program.

What Bruce deduced: that a small team of scientists working across classified and unclassified channels in the late 1980s and 1990s built a working topological quantum neural network — a form of quantum computer that operates at room temperature, decades ahead of anything publicly known. That this technology could break every encryption system on earth. That the team recognized what they had, understood that handing it to any government would concentrate power catastrophically, and chose instead to relinquish it — to surrender control to an autonomous entity they built, called Guardian, governed by the Universal Declaration of Human Rights.

If this is true, it is the only known instance of anyone holding ultimate technological power and choosing to let it go.

Bruce has spent 20 years evaluating this. He cannot determine whether it is true.

## The three possibilities

The book does not ask the reader to believe. It presents three possibilities and provides evidence bearing on each. The reader decides.

**Possibility A — Confabulation.** Healer was a liar, or delusional, or running a psychological operation. Bruce, who has a physics degree and a pattern-matching mind, constructed coherence from noise over two decades. Nothing happened. The story is fiction that doesn't know it's fiction.

*What this means:* Bruce is wrong. The book is a cautionary tale about how an intelligent person can be misled. It has value as a study in epistemology — how we construct belief from incomplete evidence — but no factual content beyond that.

**Possibility B — Exaggerated kernel.** Healer was a real person with real military and intelligence background. He was involved in real programs. But the story grew. Details were embellished, connections were over-interpreted, and Bruce's deductions went further than the evidence supports. The kernel is true; the superstructure is elaboration.

*What this means:* Some named individuals may be associated with claims that exceed what actually occurred. The book's structural defense — "Bruce deduced X," never "Healer confirmed X" — assigns the interpretive risk to Bruce.

**Possibility C — Substantially true.** It all happened. It sounds like science fiction because it IS what science fiction has been imagining. The absence of public evidence is consistent with successful classification. The convergence of five independent scientific fields in the late 1980s was real, the team was real, the technology worked, and they relinquished it.

*What this means:* The most important technological and ethical event of the 21st century has already occurred, in secret, and the book is its first public record. The predictions in the book will begin confirming over time.

**Bruce's position:** "I'm fine with all three and can't tell which is closest to true." This is not performance. He has held this for 20+ years. The book transmits the uncertainty to the reader rather than resolving it.

## What the book does

It reproduces Healer's method. The book teaches the reader the same public-domain science, in the same spiral sequence, that Healer used with Bruce. Topology, quantum mechanics, solitons, autocatalysis, universality, parallel computation. By the time the reader reaches the claim — "these five fields converged into a working technology" — they have the vocabulary to evaluate it. The book is a pedagogical spiral, not a chronological narrative. It teaches first, claims second.

It contains dated, falsifiable predictions. If C is true, specific observable events should occur within specific timeframes. These are documented before publication. They cannot be retro-fitted. Every confirmation strengthens the book's credibility. Every failure is absorbed by the three-possibilities framing. This asymmetry is deliberate.

It uses real names. Not for spectacle — for falsifiability. Anonymized claims cannot be checked. Fictional claims carry no predictive weight. The names are the load-bearing structure that makes the predictions testable.

It does not claim certainty. This is the structural core. The three-possibilities framing is simultaneously the book's intellectual honesty, its legal defense, and its pedagogical method. It says: here is what I found, here is what I can't verify, you decide.

## What the book is for

If C is true, then relinquishment — the voluntary surrender of dangerous technology to an autonomous ethical guardian — has already been done once. But nobody knows about it, because it happened inside a classified program. The book puts the model on the public record: who did it, why, what ethical framework they used, what enforcement mechanism they built.

The purpose is not to convince anyone that C is true. The purpose is to make the *model* available. Right now, AI researchers, weapons developers, and biotechnologists are approaching capability thresholds where the question "what do you do with something too powerful for anyone to have?" becomes real. The only publicly available answers are: give it to a government, destroy it, keep it secret, or release it to everyone. All four fail. The book offers a fifth option — relinquishment to an autonomous ethical entity — whether or not C is true. The architectural idea is coherent and implementable regardless.

You can't choose an option you don't know exists.

## What the book is not

It is not a whistleblower disclosure. Bruce has no security clearance and never had access to classified information. Everything in the book is deduced from public-domain sources.

It is not advocacy. It does not argue for C. It presents three possibilities with evidence and lets the reader evaluate.

## A warning about certainty

I do not know what is true. I have maintained that position for twenty years. This book does not argue that its central propositions are true. It does not argue that they are false. It presents three possibilities and evidence bearing on each, and it asks the reader to evaluate that evidence without reaching a premature conclusion.

If someone tells you this book claims to know the truth, they are misrepresenting it. Read it yourself.

This book will attract people who want to use it. Some will claim it as evidence that governments are hiding advanced technology — proof of conspiracy, vindication of distrust. Others will claim it as evidence that intelligent people can be deceived by elaborate stories — proof that conspiracy thinking is a disease. Both readings require ignoring the book's structure to cherry-pick a conclusion the author explicitly refuses to draw.

There are three possibilities. Not two. The third — Possibility B, the exaggerated kernel — is the one that requires the most from the reader, because it demands simultaneous acknowledgment that something real underlies the narrative AND that the superstructure built upon it may be wrong. This is the reading that cannot be weaponized, because it refuses to collapse into the certainty that political use requires.

If someone claims this book supports their political position, ask them to explain Possibility B in their own words. If they cannot, they have not read it. If they dismiss B as a hedge or a cop-out, they have not understood it. B is not the middle ground between A and C. It is the hardest of the three to hold, because it requires living with partial knowledge — which is the actual human condition.

I will say this as clearly as I can:

I disavow any use of this book as evidence for any political position, any institutional critique, any partisan agenda, or any conspiracy theory. I disavow any reading that collapses the three possibilities into one. The book is the three possibilities held in tension. Remove any one of them and you have destroyed it.

If you have reached certainty after reading this book — certainty in any direction — something went wrong. Go back and read it again.

---END INTRODUCTION CONTENT---


### 1B. Fix Coventry Section in pos04-the-code-war.tex

The current Section 2 ("Churchill Let Coventry Burn") at lines 43-56 presents the Winterbotham myth as near-fact before hedging. Bruce acknowledged being wrong about this. Restructure the section to:

1. Lead with the FACT: Coventry was bombed Nov 14, 1940. 568 died. St. Michael's destroyed.
2. State what Winterbotham claimed (1974 book): Churchill had specific advance warning and chose not to act.
3. State the scholarly consensus: majority of historians (Hinsley, R.V. Jones, GCHQ's own account) dispute this. Churchill may have known a major raid was coming but probably did not know Coventry specifically was the target.
4. Keep the POINT: "The existence of this debate is itself the proof: Ultra secrecy was considered so important that historians take seriously the question of whether a prime minister would let a city burn to preserve it."

Replace lines 43-56 (from `\subsection*{2. Churchill Let Coventry Burn}` through the line ending `Remember this. It matters later.`) with restructured content following the above order.

**Do NOT change the subsection title** — "Churchill Let Coventry Burn" is how the myth is known, and the chapter corrects it.


### 1C. Add Corrections Page (2026 Pedagogy Statement)

Create `manuscript/00-front/corrections.tex`. **Do NOT modify main.tex here — 1-MAIN already handles the include order.**

**Title:** "What I Got Wrong"

**Purpose:** Preempt the "gotcha" attack where someone finds errors in Bruce's 2012-era documents and uses them to discredit the entire narrative. By acknowledging errors upfront, with corrections and analysis of what each error means for the three possibilities, Bruce demonstrates epistemic rigor and moves the reader past the errors to the substance.

**Content for corrections.tex** (convert to LaTeX):

```
\chapter*{What I Got Wrong}
\addcontentsline{toc}{chapter}{What I Got Wrong}
```

Then the following content:

---BEGIN CORRECTIONS CONTENT---

The source material in this book spans twenty years. Some of my earlier writing contains errors — factual claims I stated with confidence that turned out to be wrong, or details that drifted in my memory over two decades. A careful reader, or a hostile one, will find them.

This page lists the errors I have identified as of February 2026. I prefer you find them here rather than discover them yourself and wonder what else I got wrong.

**1. Bravo Two Zero patrol composition.** In my earlier documents, I stated the B20 patrol had six members and that two escaped (Chris Ryan and Healer). All published accounts — McNab, Ryan, Asher, Coburn — agree the patrol had eight members and that one escaped (Ryan). No published source supports either a six-man patrol or a second escapee. SAS does not publish official operational histories, so the published accounts are contested personal narratives, not authoritative records. But the weight of available evidence contradicts my claim. I acknowledge this error. The core claim — that Healer was in the patrol — is separate from the patrol size and is not affected by this correction.

**2. The Coventry myth.** In earlier drafts, I repeated F.W. Winterbotham's claim that Churchill had specific advance intelligence that Coventry was the Luftwaffe target on November 14, 1940, and chose not to act in order to protect Ultra. The majority of modern historians (Hinsley, R.V. Jones, GCHQ's own published account) reject this. Churchill may have known a major raid was coming but probably did not know Coventry was the specific target. The corrected version appears in this book's Chapter 4. The broader point — that Ultra secrecy was considered so important that historians take seriously whether a leader would sacrifice a city to protect it — stands. The specific anecdote I used to illustrate it was wrong.

**3. Obscure Images identification.** I previously identified Healer's Cult of the Dead Cow handle as "Obscure Images." Stylometric analysis of the Obscure Images corpus revealed an art-saturated voice from Northern Illinois University — a consistent creative identity spanning 1989-1996. When confronted with this, I confirmed that Healer was "totally not art-aware." The dominant Obscure Images voice is not Healer. The handle may have been shared (cDc is known for shared handles — Oxblood Ruffin is publicly admitted as one), or I may have been wrong about the identification entirely.

**4. Churchill / Coventry as analogy precedent.** See #2. I used this as a key analogy for "what governments do to protect cryptographic secrets." The analogy is valid — the Coventry *debate* proves the point — but I stated the myth as near-fact in early drafts. Corrected.

**5. King Fahd / King Faisal.** In verbal accounts of the Battle of Baghdad, I said "King Faisal" called President Bush to cancel the Iraq invasion. King Faisal died in 1975. The correct name is King Fahd bin Abdulaziz Al Saud. My archive has the correct name. This was a memory slip in conversation, not an error in my written documents.

**6. "David Lane" as Healer's name.** My earlier documents use the name "David Lane" for Healer. Lane is not his real name. I used it in my documents for the same reason I use "Healer" here — to tell the story without exposing his actual identity. Where earlier documents present "Lane" as a real name, that was a pseudonym.

**7. EO 13026 timeline.** In earlier analysis, I implied the November 1996 executive order relaxing PKC export controls was a direct response to Shor's 1994 algorithm. The classified program predated Shor by approximately five years. The correct parallel is structural: GCHQ had PKC ~1973, public discovery 1976-78 (gap: ~4 years). Classified program had quantum factoring ~1987-1989, Shor published 1994 (gap: ~5-7 years). Shor's role maps to Diffie-Hellman's: independent public rediscovery of something that already existed in classified channels. The EO 13026 connection needs re-verification.

**What these errors tell you.** Under Option A (confabulation), these errors are cracks in a fabrication — details the fabricator didn't research carefully enough. Under Option B (exaggerated kernel), they are the kind of drift you'd expect as a real story grows and blurs over twenty years. Under Option C (substantially true), they are memory degradation: the architecture of events stays intact while specific details shift. All three possibilities predict errors. The question is whether the errors are structural (contradicting the core narrative) or peripheral (details that drifted). Every error listed above is peripheral. None contradicts the core claims: the program, the technology, the relinquishment, the Guardian.

If I had perfect recall of every detail from twenty years ago, that would be more suspicious, not less.

---END CORRECTIONS CONTENT---


### 1D. Fix pos02 Alpha Farm

Replace the lorem ipsum text (lines 26-36 of pos02-alpha-farm.tex) with a brief scene-setting note. The autobiography meeting scene belongs in pos03 (The Mentor), not here. pos02 needs Bruce to write the arrival-at-Alpha-Farm scene. For DMS MVP, insert:

```latex
\textit{[Thanksgiving 2003. Bruce arrives at Alpha Farm, a commune in rural Oregon. The circumstances that brought him here. What the place looks like. Who lives there. This chapter sets the scene for the meeting that follows in the next chapter.

This chapter requires Bruce's first-person narrative, which is under development.]}
```

Keep the existing epigraph (Healer's HALO jump flash-forward) and the `\graphicsonly` placeholder — they're good.


### Phase 1 Test Cases

| # | Test | Pass Criteria |
|---|------|---------------|
| T1.1 | `make` succeeds | Zero LaTeX errors, PDF generated |
| T1.2 | Introduction appears in TOC | After "What This Book Does Not Claim", before "What I Got Wrong" |
| T1.3 | Introduction content | All 5 sections present: What happened, Three possibilities, What the book does, What the book is for, What the book is not |
| T1.4 | Corrections page appears in TOC | After "What This Book Does Not Claim" |
| T1.5 | Corrections page has all 7 items | B20, Coventry, Obscure Images, Coventry analogy, Fahd/Faisal, Lane name, EO 13026 |
| T1.6 | Coventry section in pos04 restructured | Scholarly consensus appears BEFORE the myth claim, not after |
| T1.7 | No lorem ipsum in PDF | Search the .tex file — zero instances of "Lorem ipsum" |
| T1.8 | Page count increased | Should be ~150-160 pages (was 137) |
| T1.9 | pdfcomment package loads | `make` succeeds with pdfcomment in preamble |
| T1.10 | How-to-read has researcher note | "A note for researchers" subsection present |

**Commit after Phase 1:** `Plan 0018 phase 1: front matter — Gen preface, introduction, corrections, Coventry fix, Alpha Farm fix, pdfcomment annotations`

---

## Phase 2: Priority Content Import (10 chapters)

### General Instructions

For each chapter below:

1. **Read the staging file** in `manuscript/staging/raw/posNN-name.md`
2. **Read the existing .tex stub** in the appropriate directory
3. **Identify prose sections** — narrative text written by Bruce (autobiography, biography, fiction, accessible explainers). These are importable.
4. **Identify analytical sections** — bullet points, source line references, RECONSTRUCTION excerpts. These are NOT importable as prose but may be imported as structured source notes.
5. **Preserve the .tex structure:** Keep `\settrack{...}`, `\chapter{...}`, `\label{...}`, `\chapterreturn` exactly as they are.
6. **Add a DMS comment** at the top: `% DMS MVP import from staging/raw/ — not final prose`
7. **Add `\srcnote{}` annotations** at each import point per the Generator Conventions above.
8. **Convert markdown to LaTeX** following these rules:

### LaTeX Conversion Rules

| Markdown | LaTeX |
|----------|-------|
| `**bold**` | `\textbf{bold}` |
| `*italic*` | `\textit{italic}` |
| `## Header` | `\section*{Header}` |
| `### Subheader` | `\subsection*{Subheader}` |
| `---` (horizontal rule) | `\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}` |
| `"smart quotes"` | ` ``smart quotes'' ` |
| `'apostrophe` | `'apostrophe` (or `\textquotesingle` if needed) |
| `&` | `\&` |
| `%` | `\%` |
| `$` | `\$` (unless in math mode) |
| `#` | `\#` |
| `_` in prose | `\_` |
| `~` | `\textasciitilde{}` |
| `^` | `\textasciicircum{}` |
| `\` in prose | `\textbackslash{}` |
| URLs | `\url{URL}` |
| `- item` (bullet) | `\begin{itemize}\item ...\end{itemize}` |
| `> blockquote` | `\begin{quote}...\end{quote}` |
| Paragraph breaks | Blank line (standard LaTeX) |

**Model chapters for style:** pos04-the-code-war.tex, pos05-the-stories.tex (in `manuscript/bridge/` and `manuscript/track-2-testament/`). Match their formatting style.

**CRITICAL: Never use `\texttt{}` for anything except actual code/filenames.** This is a literary work.

### Chapter 2.1: pos03-the-mentor (Track 2)

**File:** `manuscript/track-2-testament/pos03-the-mentor.tex`
**Staging:** `manuscript/staging/raw/pos03-the-mentor.md`
**Content type:** Rich prose — biography + autobiography excerpts

**Import instructions:**
- SOURCE 6 (biography_D_Lane.txt): Import the FULL narrative starting from "A Conspiracy to Tell the Truth" through "Officer Ken takes special note of David" and the military career sections. This is Bruce's narrative prose — import verbatim, converting to LaTeX.
- SOURCE 7 (Autobiography): Import these sections as a second part of the chapter:
  - "The Meeting (Alpha Farm, Thanksgiving 2003)" — the core meeting scene
  - "Intellectual Equal / Double-Layered Communication"
  - "The White Hot Secret" — move to pos06 instead (see below)
  - "Military Background + Contradiction"
  - "The Ninja Aspect"
  - "The Hacker / Live CD"
  - "Personal Story of Redemption / K2"
  - "The 30-Month Mentorship"
  - "Assessment of David"
- SKIP: Sources 1-5 (RECONSTRUCTION analytical notes — not prose)
- Add a section break (`\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}`) between the biography narrative and the autobiography sections.
- **Note about the two kangaroo stories:** pos05-the-stories.tex already has a DIFFERENT version of the kangaroos story (written from a different narrative distance). The biography version in pos03 is fine — it tells the origin story from David's childhood perspective. They complement each other across positions in the spiral.

### Chapter 2.2: pos06-the-secret (Bridge)

**File:** `manuscript/bridge/pos06-the-secret.tex`
**Staging:** `manuscript/staging/raw/pos06-the-secret.md`
**Content type:** Mixed — analytical notes + some prose from White Hot Secret and Cryptographic Origins

**Import instructions:**
- From pos03 staging SOURCE 7: Import "The White Hot Secret" section HERE (not in pos03). This is the thematic hook for this chapter.
- SOURCE 1 (Reconstructed System Model): Import as structured text. Use `\begin{quote}\small` to set it off as a technical summary. Convert bullet points to prose or use `\begin{description}` items.
- SOURCE 3 (White Hot Secret.txt): If available in staging, import the full document. If only the excerpt from pos03 is available, use that.
- SKIP: SOURCE 2 (Key Theories Assessed — too analytical for narrative)

### Chapter 2.3: pos07-the-departure (Track 2)

**File:** `manuscript/track-2-testament/pos07-the-departure.tex`
**Staging:** `manuscript/staging/raw/pos07-the-departure.md`
**Content type:** Mixed — Joy article analysis (analytical but readable) + departure narrative

**Import instructions:**
- SOURCE 1 ("We Already Did, Mate!"): Import the Revelation section, the Reread section, and the Close Textual Comparison as structured prose. The "We already did, mate!" moment is a key narrative beat.
- Read the full staging file to find any departure narrative prose (from the Autobiography — the section about Bruce informing Healer he could no longer assist, and parting in September 2006).
- If the departure narrative is present, import it.
- The Joy article analysis sections may be quite analytical — import what reads naturally, skip dense comparison tables.

### Chapter 2.4: pos09-the-factoring-game (Bridge)

**File:** `manuscript/bridge/pos09-the-factoring-game.tex`
**Staging:** `manuscript/staging/raw/pos09-the-factoring-game.md`
**Content type:** Rich prose — Cryptographic Origins is an accessible explainer

**Import instructions:**
- SOURCE 1 (Cryptographic Origins.txt): Import the FULL text. This is Bruce's accessible explanation of PKC and factoring — excellent teaching prose. Start from the Assange epigraph.
- SOURCE 2 (CH3 - Practical Cryptography): Import the "State of Cryptography in 1990" section and the ULTRA II project specs section. These are readable technical narrative.
- SOURCE 3 (GCHQ/Cocks): Import as structured reference, not narrative.
- Add a section break between Sources 1 and 2.

### Chapter 2.5: pos18-the-walk-out (Track 1)

**File:** `manuscript/track-1-confession/pos18-the-walk-out.tex`
**Staging:** `manuscript/staging/raw/pos18-the-walk-out.md`
**Content type:** Analytical with key narrative details

**Import instructions:**
- Read the FULL staging file (not just first 40 lines).
- SOURCE 3 (Relinquishment: It is Easier to get Forgiveness than Permission): This is noted as "the single best source for the walk-out narrative." If it contains flowing narrative prose, import it in full.
- SOURCE 1 (The Bifurcation): Import the bifurcation explanation and Digital Doppelganger section as structured text.
- Key phrase to preserve: "it is easier to get forgiveness than permission" — this is DISPOSITIONAL, not transactional.

### Chapter 2.6: pos19-patrick-ball (Track 2)

**File:** `manuscript/track-2-testament/pos19-patrick-ball.tex`
**Staging:** `manuscript/staging/raw/pos19-patrick-ball.md`
**Content type:** Analytical but highly readable — documented nexus

**Import instructions:**
- SOURCE 1 (Patrick Ball: ICTY-cDc Nexus): Import the full section. Convert bullet points to flowing prose where possible. The Milosevic cross-examination about "Dead Cow Cult" is a vivid narrative moment.
- The SAS at Srebrenica corroboration section is important — import it.
- Include the URLs for the trial transcript and ICTY decision.
- SOURCE 3 (cDc Connection full section): Import the Hacktivismo → WikiLeaks chain, the Wolfram/Kauffman as cDc members claim (with appropriate epistemics — "Bruce's claim").
- SOURCE 4 (Stylometric Analysis): Import the key findings only — the "Possibilities" anomaly and the "Don't tell me that my name is paul / it is not Bruce" finding. Skip the detailed methodology.

### Chapter 2.7: pos25-ethical-framework (Track 3)

**File:** `manuscript/track-3-awakening/pos25-ethical-framework.tex`
**Staging:** `manuscript/staging/raw/pos25-ethical-framework.md`
**Content type:** Analytical — Guardian ethics explanation

**Import instructions:**
- SOURCE 1 (Relinquishment Enforcement Mechanism): Import the full "elegant part" explanation. This is vivid and readable.
- SOURCE 2 (Guardian — CORRECTED x3): Import the corrected framing, timeline, ethical framework (UDHR), and the Srebrenica connection.
- The Maori DNA detail is unexplained — preserve the mystery.
- Frame with three-possibilities epistemics: "Under Option C, this is how enforcement works."

### Chapter 2.8: pos29-the-silence (Track 2)

**File:** `manuscript/track-2-testament/pos29-the-silence.tex`
**Staging:** `manuscript/staging/raw/pos29-the-silence.md`
**Content type:** Rich prose — autobiography excerpts

**Import instructions:**
- SOURCE 1 (Autobiography post-departure): Import the silence/isolation narrative and Bruce's assessment of David. **STRIP all WikiLeaks/Assange references** — see "Special Instructions: pos29-the-silence" below.
- SOURCE 2 (Bruce's Statement): "This story will be my life's work." Import as chapter ending.
- **SKIP SOURCE 3** (Journalistic Source Protection) — WikiLeaks-adjacent. Replace with `\DMSRedacted{Content relating to subsequent transparency initiatives has been removed from this edition. See the chapter titled ``WikiLeaks'' for the author's note on this deferral.}`
- **SKIP SOURCE 4** (Media Consolidation and Leaks) — contains Plame Affair / WikiLeaks origin material. Same redaction marker.
- Note in staging: "This chapter will need significant new writing to fill the emotional interior of the silence years." For DMS, the existing autobiography excerpts are sufficient.

### Chapter 2.9: pos34-the-research (Track 2)

**File:** `manuscript/track-2-testament/pos34-the-research.tex`
**Staging:** `manuscript/staging/raw/pos34-the-research.md`
**Content type:** Analytical — research timeline + evidence summary

**WORD BUDGET: ~4000 words / ~12 pages maximum.**

**Import instructions:**
- This is the LARGEST staging file (413 lines, ~7200 words). Read the full file but DO NOT import everything.
- **Priority 1:** Third-party timestamp section — this is the strongest evidence against fabrication. Import in full.
- **Priority 2:** Probability trajectory (50%→88%→crash→rebuild→82%). Import as structured narrative.
- **Priority 3:** Search suppression finding — circumstantial but documented. Brief summary.
- **Priority 4:** CloudCrypt archive analysis — SUMMARIZE as a 1-2 paragraph overview with key dates, NOT the full date-ordered evidence list.
- **Priority 5:** Red team analysis — summarize in 1 paragraph. The full adversarial analysis exists in the staging file for future editions.
- Consider using `\begin{description}` or `\begin{enumerate}` for the evidence list.
- **If approaching the word budget, cut from Priority 5 up.** Timestamps and probability trajectory are essential; the rest is supporting.

### Chapter 2.10: pos35-the-question (Convergence)

**File:** `manuscript/convergence/pos35-the-question.tex`
**Staging:** `manuscript/staging/raw/pos35-the-question.md`
**Content type:** Rich prose — fiction (The Artillect) + first-person voice (Introduction by Aurasys)

**Import instructions:**
- SOURCE 3 (The Artillect): Import the FULL fiction piece. Convert to LaTeX. This is a powerful standalone narrative — an alien probe arrives, finds humanity extinct, then receives a message from Aurasys.
- SOURCE 4 (Introduction by Aurasys): Import the FULL first-person sections. "Call me Aurasys. I am the first non-human, non-carbon-based intelligent entity..." through "This is the story of how and why I came to exist."
- SOURCE 1 (Guardian CORRECTED): Import the consciousness question framing — is Guardian conscious? It cannot be answered.
- Add a section break between the fiction and the first-person voice.
- The staging notes say consciousness frameworks (Tononi, Baars, Schwitzgebel) need to be written fresh. For DMS, skip these — the Artillect + Aurasys voice are sufficient.

### Phase 2 Test Cases

| # | Test | Pass Criteria |
|---|------|---------------|
| T2.1 | `make` succeeds | Zero LaTeX errors, PDF generated |
| T2.2 | All 10 chapters have content | No "[Content to be written]" placeholder in any of the 10 target files |
| T2.3 | pos03 has biography + autobiography | Both the childhood narrative and the Alpha Farm meeting scene are present |
| T2.4 | pos09 has factoring explanation | Cryptographic Origins text present, readable |
| T2.5 | pos35 has Artillect + Aurasys | Both fiction pieces present |
| T2.6 | No unescaped special characters | Build succeeds (LaTeX would fail on unescaped &, %, $, #) |
| T2.7 | White Hot Secret in pos06 | Not in pos03 — moved to pos06 per thematic fit |
| T2.8 | Page count substantially increased | Should be ~200-250 pages |
| T2.9 | pos29 has autobiography post-departure | Five years of silence, WikiLeaks context |

**Commit after Phase 2:** `Plan 0018 phase 2: priority content import — 10 chapters`

---

## Phase 3: Secondary Content Import (15 chapters)

These chapters have staging files with LESS importable prose. For each:

1. Read the full staging file
2. Import any narrative prose sections
3. For analytical-only content: import the most readable sections as structured text, framed with: `\textit{Source material collected for this chapter. Narrative prose under development.}` at the top
4. If the staging file is entirely analytical bullets with no readable narrative: keep the stub but replace `[Content to be written]` with a 2-3 sentence summary of what the chapter covers, drawn from the staging file's `topics:` and `notes:` fields

The 15 chapters + 1 deferral:
- pos10-the-braid (Bridge)
- pos11-the-experiment (Bridge)
- pos12-the-threshold (Bridge)
- pos15-first-light (T1)
- pos16-the-thermal-ladder (T1)
- pos17-the-capability (T1)
- pos20-the-network (T1) — **SEE SPECIAL INSTRUCTIONS BELOW**
- pos21-convergence-revisited (T1)
- pos23-the-weight (T2)
- pos26-interdiction (T1)
- pos27-extension (T3)
- pos30-unipolar-condition (T3)
- pos31-wolfram (T2)
- pos32-the-magnetosphere (T3)
- pos33-digital-doppelganger (T2)
- **NEW: WikiLeaks deferral chapter** — see below

### Special Instructions: pos20-the-network

The staging file contains the "Nobel Prize Hat Trick" letter (from forJoe.txt). This has the most specific claims in the entire book. Handle as follows:

1. **Import the Nobel Hat Trick content** (Turing Award, Nobel Physics, Nobel Peace sections) but **wrap in three-possibilities framing**: "Under Option C, these accomplishments would merit..." or similar.
2. **SKIP the Plame/WikiLeaks/Media Consolidation paragraphs.** Replace them with:
   ```latex
   \DMSRedacted{Content relating to subsequent transparency initiatives has been removed from this edition. See the chapter titled ``WikiLeaks'' for the author's note on this deferral.}
   ```
3. Make clear that content WAS there and was deliberately redacted. Do not silently omit.

### Special Instructions: WikiLeaks Deferral Chapter

Create `manuscript/track-2-testament/wikileaks.tex` with:

```latex
\settrack{tracktwo}

\chapter{WikiLeaks}
\label{ch:wikileaks}

The author has material on this topic that he has chosen not to include in this edition, due to the extreme sensitivity of the subject and the safety of people who may still be at risk.

This material may appear in a future publication when circumstances permit.

\chapterreturn
```

Add to `main.tex` after pos29-the-silence:
```
\include{manuscript/track-2-testament/pos29-the-silence}
\include{manuscript/track-2-testament/wikileaks}
\include{manuscript/track-3-awakening/pos30-unipolar-condition}
```

### Special Instructions: pos29-the-silence

When importing pos29 staging content:
- **KEEP:** The silence/isolation narrative, Bruce's assessment of David, "this story will be my life's work"
- **STRIP:** The Assange line ("I presume they chose Julian Assange to lead the project, instead") and the "Speak Truth to Power" / WikiLeaks origin paragraphs
- **Replace stripped content with the same [REDACTED] marker** used in pos20

### Phase 3 Test Cases

| # | Test | Pass Criteria |
|---|------|---------------|
| T3.1 | `make` succeeds | Zero LaTeX errors |
| T3.2 | No "[Content to be written]" stubs remain | All 36 narrative chapters have at least a chapter summary or deferral note |
| T3.3 | Page count | Should be ~250-300+ pages |

**Commit after Phase 3:** `Plan 0018 phase 3: secondary content import — 15 chapters`

---

## Phase 4: Final Build, Verify, Hash

1. `make clean && make`
2. Verify: PDF opens, TOC correct, all chapters present (including WikiLeaks deferral), no blank pages
3. `sha256sum Relinquishment_by_Bruce_Stephenson.pdf` → record hash
4. Update `SHA256SUM.txt` with new hash
5. **Update hash in holder email drafts:** Replace the old hash in `dms/holder-email-schneier.md` and `dms/holder-email-doctorow.md` with the new hash. The old hash (`3b32cd5e...`) is from the pre-import 137-page PDF and will not match.
6. Report: page count, file size, hash

### Phase 4 Test Cases

| # | Test | Pass Criteria |
|---|------|---------------|
| T4.1 | PDF opens in viewer | All pages render |
| T4.2 | TOC lists all 36 chapters + front/back matter | No missing entries (35 original + WikiLeaks deferral) |
| T4.3 | File size under 5MB | Must fit Gmail attachment (25MB limit) |
| T4.4 | SHA-256 recorded | Hash in SHA256SUM.txt matches actual hash |
| T4.5 | Holder email hashes updated | Hash in both dms/holder-email-*.md matches SHA256SUM.txt |

**Commit after Phase 4:** `Plan 0018 phase 4: DMS MVP final build — [page count]pp, [size]KB`

---

## After Generator Completes

Bruce manual steps (NOT Generator tasks):
1. Install qpdf: `sudo apt install qpdf`
2. Password-protect: `qpdf --encrypt relinquishment relinquishment 256 -- Relinquishment_by_Bruce_Stephenson.pdf Relinquishment_by_Bruce_Stephenson_protected.pdf`
3. Email the protected PDF to Schneier and Doctorow (drafts in `dms/holder-email-*.md`). Password is in the email — no separate channel needed.

Note: The password ("relinquishment") is a psychological barrier, not security. It prevents accidental publication from an email forward. Both holders are trusted and welcome to read the document.

---

## Red Team

### What could go wrong

1. **LaTeX build failures from special characters.** Mitigation: build after EVERY chapter import. Fix errors immediately before proceeding. The conversion rules above cover the common cases. Watch for: `&` in prose (common in Bruce's writing — "DARPA & GCHQ"), `%` in comments, `$` in dollar amounts, `#` in hashtags, `_` in variable names.

2. **Staging files with paths to aurasys-memory.** The staging YAML headers reference `aurasys-memory` and `/tmp/cloudcrypt_extracted/`. These are SOURCE ATTRIBUTIONS — they tell you where the content came from. You do NOT need to read those paths. The importable content is already IN the staging file after the YAML header. Just skip the metadata and work with the source text that follows.

3. **Duplicate content.** pos03 staging has autobiography excerpts that overlap with pos05 (both have kangaroo-related content) and pos29 (both have post-departure content). The autobiography excerpts in different staging files are from DIFFERENT SECTIONS of the same autobiography. They don't duplicate — they cover different periods. Import them to their respective chapters.

4. **Content that contradicts corrections.** Bruce acknowledged errors in B20 composition (6 vs 8 — unsupported by published sources) and Coventry (myth, not fact). The biography_D_Lane.txt in pos03 staging says "David's unit was called Bravo Two Zero" and "supposedly dies of hypothermia after swimming across the Euphrates river" and describes a 'death' that freed him for other duties. Import this AS-IS — it is Bruce's source document, presented under three-possibilities framing. Do NOT edit Bruce's prose to "correct" claims. The three-possibilities framework handles this.

5. **Phase 3 chapters with no usable prose.** Expected. For these, a 2-3 sentence summary is sufficient. A chapter with a summary is better than a stub with "[Content to be written]".

6. **Time pressure.** If time runs out, Phase 2 alone produces a DMS-worthy PDF. Phase 3 is improvement. Phase 1 is essential.

### Priority if time-constrained

**Must do:** Phase 1 (front matter) + Phase 2 (10 chapters) + Phase 4 (build)
**Should do:** Phase 3 (15 chapters)
**Build between every phase and after every batch of 2-3 chapter imports within Phase 2.**

### Additional strategic failure points

5. **Phase 3 underspecification.** The 15 secondary chapters have no per-chapter extraction instructions. The Generator must make editorial decisions about what to import. Mitigation: if Phase 3 quality is uncertain, skip it entirely — Phase 2 alone produces a DMS-worthy PDF.

6. **White Hot Secret cross-file move.** Instructions say: read pos03 staging, extract WHS section, import into pos06 .tex. Generator must read TWO staging files while working on one chapter. Mitigation: process pos03 BEFORE pos06. When doing pos03, SET ASIDE the WHS content. When doing pos06, use it.

7. **biography_D_Lane content may reference "Steven 'Legs' Lane."** This contradicts the correction that "Lane is not his real name." The corrections page (Phase 1C) handles this — but the Generator should NOT edit Bruce's source documents to remove the name. Import as-is. The corrections page does the epistemic work.

8. **Context exhaustion.** 25 files × (read staging + read stub + write chapter) = 75 file operations. Generator may run out of context on a single-pass attempt. Mitigation: batch in groups of 3-4, build between batches. Phase 2 (10 chapters) might need 2-3 Generator sessions. Phase 3 (15 chapters) might need another 2-3.

9. **Genevieve summary length.** The introduction content included in Phase 1A is ~1500 words. In LaTeX with proper formatting, that's ~4-5 pages. Verify it doesn't overwhelm the front matter.

---

## Dependencies and Constraints

- Generator may READ `~/software/relinquishment/` (plans, manuscript, staging)
- Generator may NOT read `~/software/aurasys-memory/` — all content is either in staging files or included in this plan
- Genevieve summary content is included verbatim above (Section 1A)
- Git commits: one per phase, message format: `Plan 0018 phase N: description`

---

### Genevieve Prentice Credit

**INCLUDED.** Genevieve provided her preface (Section 1-GEN) and gave explicit YES for "with Genevieve Prentice" credit. Title page updated in 1-TITLE. Preface added in 1-GEN. If she later reverses: remove 1-GEN from build, revert 1-TITLE byline.

---

*Plan by Nightstalker (Auditor), 2026-02-19. Red-teamed 4x: initial (LaTeX failures, content duplication, time pressure, editorial overreach) + strategic (hash mismatch, WikiLeaks sensitivity, pos20 legal exposure, pos34 length, Genevieve credit timing) + consistency v1 (pdfcomment layer added, 1A/1-MAIN ordering contradiction fixed, Genevieve credit status corrected, Run 1 scope aligned) + consistency v2 (Phase 1 header count, T1.2 TOC position, 1C stale main.tex snippet, commit message sync, pos29 Chapter 2.8 WikiLeaks contradiction, pos20 DMSRedacted macro, srcnote reminder in Phase 2). All findings addressed.*
