# Subtask A: The Handler → The Teacher

**Parent:** Plan 0331 rev 1
**Output:** Rewrite `manuscript/record/the-handler.tex` — strip C cosmetics, honest sourcing, rename
**Commit:** `Plan 0331A: The Handler → The Teacher — strip C cosmetics, honest sourcing`
**Read first:** This spec, then `plans/0331-teacher-student-revision.md`, then `manuscript/record/the-handler.tex`

## Design Principle

Reward investigation, not demand belief. Present threads a curious reader can pull. Honest uncertainty beats theatrical classification. Works under all three possibilities (A/B/C).

## Voice

Bruce Stephenson: direct, spare, slightly wry. No over-hedging. No legal-disclaimer tone. State what you know, tag the source, admit what you don't know, move on.

## Sourcing Tags (replace throughout)

| Old | New | Rule |
|-----|-----|------|
| [observed] | [observed] | Keep when Bruce directly witnessed it |
| [observed] | [Healer's account] | Change when it's something Healer *told* Bruce |
| [REDACTED] | honest unknown | "He didn't explain." / "I don't know." / remove |
| [clancy] | [Clancy] | Keep — verifiable |

## Changes

### 1. Title (lines 7-9)
```latex
\chapter*{The Teacher}
\addcontentsline{toc}{chapter}{The Teacher}
\label{record:handler}  % KEEP — stable deep link
```

### 2. Opening (replace line 11 entirely)
```latex
I spent 2.7 years in close contact with the person I call Healer. What follows is assembled from two sources: Tom Clancy's character Timothy Hanley in \textit{Rainbow Six} (1998), which Healer told me was modeled on him; and my own observations during 2003--2006. I knew \textit{Rainbow Six} only as a video game. I did not know there was a novel, or that the novel contained detailed character biographies, until 2026 --- twenty years after our last contact.

I present this as a portrait, not a verified biography. A curious reader will find the Clancy character and the Bravo Two Zero patrol roster in the public record. What you make of the connections is yours to decide.
```

### 3. Epigraph (lines 13-15)
Keep. It provides sourcing context. Remove the `\vspace{1cm}` after it.

### 4. Header block (lines 19-32) — REMOVE AND REPLACE
Delete the entire Five Eyes header: `\textsc{Five Eyes...}`, Classification, File No, Subject, Nationality, DOB, Cover Legend, Prepared for, Source classification paragraph.

Replace with:
```latex
\noindent I never learned his real name. He was Australian, of mixed European/M\={a}ori ancestry. If the Clancy character's birthday is his, he was born 14 April 1965.\footnote{From the novel character. Not independently confirmed.}

He presented himself as a walkabout veteran and humanitarian worker. Both appeared to be true. Whether they were also cover, I cannot say.
```

### 5. Section I: Biographical Summary (lines 36-54)
Keep section heading. Retitle: `\subsection*{I. What Clancy Wrote}`

Keep all [Clancy] items. They're verifiable.

Remove line 41 (`[observed] Subject is of mixed European/Māori ancestry`) — already stated in new header block.

### 6. Section I: Bravo Two Zero (line 51) — REPLACE
Remove the current text (lines 51-53). Replace with:
```latex
\textsc{[Healer's account]} Healer told me he had served on the compromised \hovertip{Bravo Two Zero} patrol. His ``death'' during the operation freed him for classified work. I do not name the patrol member he identified as, out of respect for the families involved --- though a reader familiar with the published accounts may be able to narrow it. He told me his parents were informed before the public announcement, and that he visited them discreetly afterward. There was something about a medal --- possibly a Saint Christopher medal, possibly from Iraq --- awarded posthumously to a man who was not dead. His parents had to maintain the fiction. I don't remember the details precisely. This is twenty-year-old memory of what I was told, not what I witnessed.\footnote{The Bravo Two Zero patrol roster and casualty records are public. Three men are recorded as killed. I leave the investigation to the reader.}
```

### 7. Section I: K2 (line 53)
Keep. Retag: already [observed] which is correct (Bruce was told this, but it's a biographical claim Healer made → [Healer's account]).

```latex
\textsc{[Healer's account]} In 1996, he stood on the summit of K2 and resolved to use his abilities for something other than ``killing bad guys.'' He anchored this vow to the Universal Declaration of Human Rights. This is the origin point of the Relinquishment.
```

### 8. Section II: What Clancy Left Out (lines 57-75)
Keep section heading. Replace triple [REDACTED] (lines 60-64) with:
```latex
There are aspects of his background he never explained and I never learned. The mathematics and physics fluency, in particular, had no source I could identify.
```

Line 66 (math/physics fluency): keep [observed] — Bruce witnessed this directly.

Line 68 ("new form of mathematics"): retag to [Healer's account].

Line 70 ([REDACTED]): remove.

Line 72 (eidetic memory testing): keep [observed].

Line 74 ([REDACTED]): remove.

### 9. Section III: The Safe House (lines 78-86) — DELETE SECTION
Fold one sentence into Section IV:
```latex
\textsc{[observed]} A property in rural Australia was offered as relocation for my wife and daughters. The offer was not casual.
```
Delete the Clancy cross-reference ("As one does") and the section heading/rules.

### 10. Section IV: Operational Characteristics (lines 89-101)
Keep section heading. Keep all [observed] items — these are direct observations.

Replace line 92: remove "SAS + Intelligence Corps training evident in every interaction." Replace with:
```latex
\textsc{[observed]} OPSEC: \textbf{Exceptional.} He left no paper trail, no digital footprint, no photographs. Whatever his background, his operational discipline was extraordinary.
```

Line 98 (cover legend): already handled by new header block. Remove or simplify to avoid repetition.

Line 100 ([REDACTED]): remove.

### 11. Section V: Skills Assessment table (lines 104-127)
Keep table structure. Changes:
- Mathematics / Physics / Computational theory / Languages: change `[REDACTED]` source to "unknown" or "[Healer's account] — claimed"
- Mathematics / Physics / Computational theory: change level from `[REDACTED]` to "deep (observed)" 
- Languages: remove row (no information)

### 12. Section VI: Assessment (lines 131-141)
Keep entire section — strongest paragraph. One change at line 140:

Replace: `Unless \textbf{[REDACTED]}.`
With: `What fills that gap is the question this book asks.`

### 13. Section VII: Current Status (lines 144-148)
Replace `[REDACTED]` with:
```latex
I have had no contact with Healer since 2006. I do not know where he is or whether he is alive.
```

### 14. Footer (lines 151-156)
Replace "Filed by / FVEY EYES ONLY" with:
```latex
\begin{flushright}\small\textit{%
Assembled by Bruce Stephenson, 2026.\\
Sources: Clancy, T.\ (1998). Rainbow Six. G.P.\ Putnam's Sons.\\
Direct observation, 2003--2006.%
}\end{flushright}
```

### 15. Cross-references
- `manuscript/record/alpha-farm.tex` lines 15-16: `\textit{The Handler}` → `\textit{The Teacher}` (two occurrences in footnote)
- `manuscript/record/alpha-farm.tex` line 97: `\textit{The Handler}` → `\textit{The Teacher}`
- `manuscript/track-2-testament/pos02-alpha-farm.tex` lines 15-16 and 98: same changes
- `manuscript/appendix/topic-guide.tex` lines 116-117: update chapter title references
- Check Makefile and any `\input`/`\include` for `the-handler` — update if found
- Rename file: `the-handler.tex` → `the-teacher.tex`

## Verify

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
python3 build/verify-deep-links.py
```

Chapter appears with new title. No orphan deep links. No build errors.

## Do NOT

- Change any other manuscript file beyond those listed
- Change `\label` values (`record:handler`, `record:hd-*`)
- Add new C-level claims
- Over-hedge — no "perhaps" "possibly" "it could be" chains
- Add comments about what was removed or why
- Modify the tutorial source or build/preprocess.py
