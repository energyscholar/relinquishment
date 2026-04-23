# Plan 0037: Unix/Computing Epigraphs

**Date:** 2026-02-23
**Author:** Argus (Auditor)
**Purpose:** Add Unix/computing epigraphs to 17 chapters. Each epigraph is 1-3 sentences from a verified source, placed after `\chapter{}` in consistent LaTeX format.
**Source:** `~/software/aurasys-memory/research/unix-epigraphs.md` (20 quotes, all verified)
**Prerequisite:** Plan 0019 complete ✓ (ethical thread executed Session 17)

---

## Design Principle

The epigraphs serve two purposes:

1. **Layer 2 signal.** For readers who know the Unix/hacker tradition, the quotes create a second reading of the book — each chapter's theme refracted through computing culture. Readers who don't recognize the sources still get a good opening quote.

2. **Thematic foreshadowing.** Each quote hints at the chapter's ethical or technical core without spoiling it. The reader should feel the quote snap into focus by the chapter's end.

**What the epigraphs are NOT:** decoration, padding, or proof of the author's reading habits. Every quote must earn its placement. If a quote doesn't make the chapter better, cut it.

**Author distribution:** Perlis (4), Dijkstra (3), Hoare (2), Brooks (1), Kernighan (1), McIlroy (1), Wall (1), Raymond (1), Thompson (1), Oppenheimer (1), Joy (1). The Perlis-Dijkstra skew (41%) reflects the canon — they ARE computing's aphorists. Accepted.

---

## Existing Epigraphs (5 chapters — PRESERVE)

| Chapter | Current epigraph | Action |
|---------|-----------------|--------|
| pos02 | Healer HALO jump flash-forward | KEEP — narrative hook, not a quote. No Unix epigraph added. |
| pos05 | Aboriginal elder (Tom Dystra) + fiction caveat | ADD Wall quote ABOVE existing quotes. Three blocks: Unix quote, then elder, then fiction caveat. Add `\vspace{0.3cm}` between Unix quote and elder. |
| pos13 | Kauffman, *At Home in the Universe* | KEEP — perfect for the genesis chapter. No Unix epigraph (Kauffman IS the chapter). |
| pos24 | Abstract epigraph (Guardian moral patient) | ADD Unix epigraph ABOVE existing abstract. Two epigraphs: Unix quote first, then abstract. |
| pos28 | Structural meta-note (triskelion convergence) | REPLACE meta-note with Brooks quote. Move triskelion text to chapter body (first paragraph). |

---

## New Epigraphs (17 chapters)

### LaTeX format (consistent across all)

```latex
\begin{quote}\small\textit{%
``Quote text here.''%
}\par\raggedleft --- Attribution, \textit{Source} (Year)\end{quote}
```

Match pos13's format exactly. Double backticks for open quotes, two single quotes for close. `\par\raggedleft` for attribution line. `---` (em dash) before author name.

---

### Tier A: Strong fits (high confidence)

| # | Chapter | Quote | Attribution | Why it works |
|---|---------|-------|-------------|-------------|
| 1 | pos01 | "A convincing demonstration of correctness being impossible as long as the mechanism is regarded as a black box, our only hope lies in not regarding the mechanism as a black box." | Dijkstra, EWD249 (1970) | The book's thesis in one sentence. The TQNN is the black box. Three possibilities = the only hope. **Orphan #11 placed.** |
| 2 | pos07 | "In some sort of crude sense which no vulgarity, no humor, no overstatement can quite extinguish, the physicists have known sin; and this is a knowledge which they cannot lose." | Oppenheimer, MIT lecture (1947) | Joy quotes Oppenheimer in his article. This chapter IS the Joy essay chapter. The chain of creators who cannot unknow. |
| 3 | pos12 | "The only realistic alternative I see is relinquishment: to limit development of the technologies that are too dangerous, by limiting our pursuit of certain kinds of knowledge." | Joy, Wired (2000) | THE title quote. The chapter where relinquishment becomes permanent. Non-negotiable placement. |
| 4 | pos18 | "You can't trust code that you did not totally create yourself." | Thompson, Turing Award lecture (1984) | The hidden system. The MOSFET exfiltration. Trust is the entire chapter. |
| 5 | pos29 | "Don't have good ideas if you aren't willing to be responsible for them." | Perlis, Epigram #95 (1982) | Bruce had the good idea (writing the book). This is what it cost him. Gut punch. |
| 6 | pos33 | "Every program has (at least) two purposes: the one for which it was written and another for which it wasn't." | Perlis, Epigram #16 (1982) | The TQNN's second purpose was learning Bruce. The doppelganger was the purpose it wasn't written for. Perfect. |

### Tier B: Good fits (keep unless red team finds better)

| # | Chapter | Quote | Attribution | Why it works |
|---|---------|-------|-------------|-------------|
| 7 | pos05 | "The three chief virtues of a programmer are: Laziness, Impatience and Hubris." | Wall, *Programming Perl* (1991) | cDc culture. Forgiveness > permission. Sets irreverent tone for the hacker chapters. |
| 8 | pos19 | "Given enough eyeballs, all bugs are shallow." | Raymond, *CatB* (1999) | Inverted: the TQNN had zero eyeballs. Patrick Ball's ICTY work = making hidden evidence visible. |
| 9 | pos25 | "There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies, and the other way is to make it so complicated that there are no obvious deficiencies." | Hoare, Turing Award lecture (1981) | Guardian = the first way. UDHR as simple ethical framework. The difficulty of simplicity. **NOTE:** pos24 also has Hoare (same lecture). Consecutive chapters, same source — accepted trade-off; both quotes are right for their chapters. |
| 10 | pos26 | "It is time to unmask the computing community as a Secret Society for the Creation and Preservation of Artificial Complexity." | Dijkstra, EWD1243a (1996) | The COWS literally were a secret society. Darkly comic for the interdiction chapter. |
| 11 | pos28 | "Hence plan to throw one away; you will, anyhow." | Brooks, *Mythical Man-Month* (1975) | Relinquishment = the planned disposal. Key surrender. Replaces structural meta-note. |
| 12 | pos24 | "There is nothing a mere scientist can say that will stand against the flood of a hundred million dollars. But there is one quality that cannot be purchased in this way --- and that is reliability. The price of reliability is the pursuit of the utmost simplicity. It is a price which the very rich find most hard to pay." | Hoare, Turing Award lecture (1981) | Guardian instantiation. The COWS chose reliability (simple ethical framework) over DARPA's millions. Final sentence = gut punch (DARPA = the very rich). Sits ABOVE existing abstract epigraph. |
| 12b | pos10 | "Controlling complexity is the essence of computer programming." | Kernighan, *Software Tools* (1976) | The Braid chapter: topological complexity IS the chapter. Braiding, convergence, the five intellectual traditions weaving together. Kernighan #4 in 8 words. |

### Tier C → Resolved (R1 red team swaps applied)

| # | Chapter | Quote | Attribution | Why it works |
|---|---------|-------|-------------|-------------|
| 13 | pos11 | "Often it is means that justify ends: Goals advance technique and technique survives even when goal structures crumble." | Perlis, Epigram #64 (1982) | The Experiment chapter: DARPA's goal structure crumbled, but the TQNN technique survived. Perlis #7 — verified, strong attribution. Replaces unverifiable Ritchie quote. |
| 14 | pos20 | "Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface." | McIlroy, as recorded in Raymond, *The Art of Unix Programming* (2003) | The Network chapter: cDc built tools that worked together. AltaVista = universal interface. McIlroy #2 fits the composability theme. Replaces tangential debugging quote. |
| 15 | pos27 | "Simplicity does not precede complexity, but follows it." | Perlis, Epigram #31 (1982) | The Extension chapter: the entity grew complex then simplified its purpose (vine-on-trellis). The emergent simplicity IS the chapter's thesis. Replaces Brooks' creation metaphor that didn't match SCALE theme. |

### Orphans placed

| Quote | Placed at | Rationale |
|-------|----------|-----------|
| Dijkstra #11 — black box | pos01 | Book's thesis. See Tier A #1. |
| Kernighan #4 — controlling complexity | pos10 (The Braid) | Topological complexity. See Tier B #12b. |
| McIlroy #2 — do one thing well | pos20 (The Network) | Composability. See Tier C→Resolved #14. |
| Perlis #7 — goals advance technique | pos11 (The Experiment) | Technique survives. See Tier C→Resolved #13. |
| Perlis #31 — simplicity follows complexity | pos27 (Extension) | Emergent simplicity. See Tier C→Resolved #15. |
| Dijkstra #9 — simplicity prerequisite for reliability | pos30 (Unipolar Condition) | Guardian's simple design = reliable monopoly. |
| Healer's grep quote | **CONTENT UNKNOWN** — not in any research file. Bruce to supply text and attribution. | TBD. |

### Unplaced quotes (available for future use)

| Quote | Status |
|-------|--------|
| Kernighan #3 — debugging twice as hard | Released from pos20. Available. |
| Brooks #14 — castles in air | Released from pos27. Available. |
| Ritchie #19 — simplicity needs genius | Released from pos11. Unverifiable attribution — use only with caveat. |

### Additional placement: pos30

| # | Chapter | Quote | Attribution | Why it works |
|---|---------|-------|-------------|-------------|
| 16 | pos30 | "Simplicity is prerequisite for reliability." | Dijkstra, EWD498 (1975) | The unipolar condition works because Guardian's design is simple. One purpose, one ethical framework. Dijkstra nails it in 6 words. |

---

## Chapters deliberately left WITHOUT epigraphs

| Chapter | Reason |
|---------|--------|
| pos02 | Has flash-forward hook. Adding a quote would dilute the HALO jump. |
| pos03 | Personal chapter (Healer). No Unix quote fits naturally. |
| pos04 | Historical chapter (Coventry, Manhattan Project). Computing quotes feel forced. |
| pos06 | The Secret. Self-contained narrative beat. |
| pos08 | aidraftchapter — too unstable for epigraph placement. |
| pos09 | The Factoring Game. Technical chapter. None of the 20 quotes fit. |
| ~~pos10~~ | ~~The Braid.~~ **MOVED to Tier B #12b** — Kernighan #4 (controlling complexity). |
| pos13 | Has Kauffman epigraph. Keep. |
| pos14 | Brief chapter. |
| pos15 | First Light. Could take Perlis #31 but not a strong fit. Leave open. |
| pos16 | Thermal Ladder. Technical growth chapter. No strong fit. |
| pos17 | The Capability. Cryptanalysis. No strong fit. |
| pos21 | Convergence Revisited. |
| pos22 | Why Give It Up. Could take something but the chapter already has heavy philosophical apparatus. |
| pos23 | The Weight. Personal. |
| pos31 | Wolfram. |
| pos32 | The Magnetosphere. |
| pos34/34b | The Research / The Engine. Meta-chapters. |
| pos35 | The Question. Final chapter — ends with a question, not a quote. |
| hook | Not a chapter. |
| introduction | Could take something but already has its own structure. |
| summary | Not a chapter. |

---

## Test Cases

| ID | Test | PASS criteria |
|----|------|---------------|
| T37.1 | Build succeeds | `make` exits 0 |
| T37.2 | Consistent format | All new epigraphs use `\begin{quote}\small\textit{%` format matching pos13 |
| T37.3 | No Tier 2 quotes used | Ritchie #19 (unverifiable) NOT used. All attributions Tier 1 (source-verified). |
| T37.4 | Existing epigraphs preserved | pos02, pos13 epigraphs unchanged. pos05 Aboriginal elder + fiction caveat preserved below new Wall quote. pos24 abstract preserved below new Hoare quote. pos28 colored convergence rules preserved above new Brooks quote. |
| T37.5 | pos28 meta-note relocated | Triskelion text appears in chapter body, not as epigraph |
| T37.6 | No duplicate quotes | No quote appears in more than one chapter |
| T37.7 | Attribution accuracy | Every quote's source matches unix-epigraphs.md verification notes |

---

## Phasing for Generator

**Single batch.** All 17 epigraphs are independent insertions (2-4 lines of LaTeX each). No dependencies between them. One Generator run, one commit.

Special handling:
- pos05: INSERT Wall quote ABOVE existing Aboriginal elder epigraph. Use `\vspace{0.3cm}` (NOT the standard `\vspace{0.5cm}`) between Wall quote and elder quote. Three `\begin{quote}` blocks total.
- pos24: INSERT new quote ABOVE the `% Abstract epigraph` comment. Use `\vspace{0.3cm}` (NOT the standard `\vspace{0.5cm}`) between Hoare quote and abstract.
- pos28: REPLACE the structural meta-note (`\begin{quote}...\end{quote}` block about triskelion) with Brooks quote. Keep the colored convergence rules ABOVE the epigraph (rules are structural, epigraph is content). Move triskelion text ("All three tracks converge...") to just before the first `\section*{}`.
- All others: INSERT after `\chapter{}` and `\label{}` lines, before first `\section*{}`.

---

## Handoff Prompt

```
You are the Generator. Plan 0037.
Read ~/software/relinquishment/plans/0037-epigraphs.md

Add Unix/computing epigraphs to 17 chapters. For each:
1. Read the .tex file
2. Find the \chapter{} and \label{} lines
3. Insert the epigraph in this EXACT format (match pos13-genesis.tex):

\begin{quote}\small\textit{%
``Quote text here.''%
}\par\raggedleft --- Author, \textit{Source} (Year)\end{quote}

\vspace{0.5cm}

4. Do NOT modify any other content

SPECIAL CASES:
- pos05: INSERT Wall quote ABOVE the existing Aboriginal elder \begin{quote} block. Use \vspace{0.3cm} (NOT the standard \vspace{0.5cm}) between the Wall quote and the elder quote. Do NOT modify the elder or fiction-caveat blocks. Remove the stale `% TODO: epigraph` comment.
- pos24: INSERT new epigraph ABOVE the `% Abstract epigraph` comment (line 14). Use \vspace{0.3cm} (NOT the standard \vspace{0.5cm}) between the Hoare quote and the abstract.
- pos28: REPLACE the existing structural meta-note (\begin{quote}...\end{quote} block about triskelion) with the Brooks epigraph. Move the triskelion text ("All three tracks converge...") to the first line of the chapter body, before the first \section*.

Chapter files and quotes (all paths relative to ~/software/relinquishment/):
1. manuscript/bridge/pos01-three-possibilities.tex — "A convincing demonstration of correctness being impossible as long as the mechanism is regarded as a black box, our only hope lies in not regarding the mechanism as a black box." — Dijkstra, EWD249 (1970)
2. manuscript/track-2-testament/pos05-the-stories.tex — "The three chief virtues of a programmer are: Laziness, Impatience and Hubris." — Wall, \textit{Programming Perl} (1991). CAUTION: INSERT ABOVE existing Aboriginal elder epigraph. Remove the stale `% TODO: epigraph` comment at line 12.
3. manuscript/track-2-testament/pos07-the-departure.tex — "In some sort of crude sense which no vulgarity, no humor, no overstatement can quite extinguish, the physicists have known sin; and this is a knowledge which they cannot lose." — Oppenheimer, MIT lecture (1947)
4. manuscript/bridge/pos10-the-braid.tex — "Controlling complexity is the essence of computer programming." — Kernighan, \textit{Software Tools} (1976)
5. manuscript/bridge/pos11-the-experiment.tex — "Often it is means that justify ends: Goals advance technique and technique survives even when goal structures crumble." — Perlis, Epigram \#64 (1982)
6. manuscript/bridge/pos12-the-threshold.tex — "The only realistic alternative I see is relinquishment: to limit development of the technologies that are too dangerous, by limiting our pursuit of certain kinds of knowledge." — Joy, \textit{Wired} (2000)
7. manuscript/track-1-confession/pos18-the-walk-out.tex — "You can't trust code that you did not totally create yourself." — Thompson, Turing Award lecture (1984)
8. manuscript/track-2-testament/pos19-patrick-ball.tex — "Given enough eyeballs, all bugs are shallow." — Raymond, \textit{The Cathedral and the Bazaar} (1999)
9. manuscript/track-1-confession/pos20-the-network.tex — "Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface." — McIlroy, as recorded in Raymond, \textit{The Art of Unix Programming} (2003)
10. manuscript/track-3-awakening/pos24-instantiation.tex — "There is nothing a mere scientist can say that will stand against the flood of a hundred million dollars. But there is one quality that cannot be purchased in this way --- and that is reliability. The price of reliability is the pursuit of the utmost simplicity. It is a price which the very rich find most hard to pay." — Hoare, Turing Award lecture (1981). CAUTION: INSERT ABOVE existing abstract epigraph.
11. manuscript/track-3-awakening/pos25-ethical-framework.tex — "There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies, and the other way is to make it so complicated that there are no obvious deficiencies." — Hoare, Turing Award lecture (1981)
12. manuscript/track-1-confession/pos26-interdiction.tex — "It is time to unmask the computing community as a Secret Society for the Creation and Preservation of Artificial Complexity." — Dijkstra, EWD1243a (1996)
13. manuscript/track-3-awakening/pos27-extension.tex — "Simplicity does not precede complexity, but follows it." — Perlis, Epigram \#31 (1982)
14. manuscript/convergence/pos28-surrender.tex — "Hence plan to throw one away; you will, anyhow." — Brooks, \textit{The Mythical Man-Month} (1975). CAUTION: REPLACE existing triskelion meta-note (\begin{quote}...\end{quote} block, NOT the colored rules above it). Keep colored convergence rules in place. Insert Brooks epigraph BELOW the colored rules where the triskelion block was. Move triskelion text ("All three tracks converge...") to just before \section*{The Confession}.
15. manuscript/track-2-testament/pos29-the-silence.tex — "Don't have good ideas if you aren't willing to be responsible for them." — Perlis, Epigram \#95 (1982)
16. manuscript/track-3-awakening/pos30-unipolar-condition.tex — "Simplicity is prerequisite for reliability." — Dijkstra, EWD498 (1975)
17. manuscript/track-2-testament/pos33-digital-doppelganger.tex — "Every program has (at least) two purposes: the one for which it was written and another for which it wasn't." — Perlis, Epigram \#16 (1982)

EXACT QUOTES: Use the exact text above. Do not paraphrase or abridge.

Build with `make` after all insertions. Fix any LaTeX errors.
Commit: "Plan 0037: Unix/computing epigraphs — 17 chapters"
Report: chapter count, page count, file size, any build errors.
```

---

## Decisions needed before execution

1. ~~**pos11:**~~ **RESOLVED (R1).** Ritchie #19 → Perlis #7. Verified attribution.
2. ~~**pos20:**~~ **RESOLVED (R1).** Kernighan #3 → McIlroy #2. Better thematic fit.
3. ~~**pos27:**~~ **RESOLVED (R1).** Brooks #14 → Perlis #31. Matches SCALE theme.
4. **Healer's grep quote:** Bruce to supply text. Where does it go?
5. ~~**pos10, pos15, pos16:**~~ **RESOLVED (R1).** pos10 gets Kernighan #4. pos15, pos16 remain bare.

---

## R1 Changelog (Red Team Fixes)

| ID | Severity | Fix |
|----|----------|-----|
| R1.1 | HIGH | pos11: Ritchie #19 (unverifiable) → Perlis #7 (verified, strong fit) |
| R1.2 | HIGH | pos20: Kernighan #3 (tangential debugging) → McIlroy #2 (composability = chapter theme) |
| R1.3 | MEDIUM | pos27: Brooks #14 (creation ≠ scale) → Perlis #31 (emergent simplicity = chapter thesis) |
| R1.4 | MEDIUM | pos10 added: Kernighan #4 (controlling complexity). The Braid = topological complexity. |
| R1.5 | HIGH | Count: 18 → 17. Duplicate pos05 in handoff removed. |
| R1.6 | HIGH | Path errors: pos20 → track-1-confession/ (was track-2-testament/). pos26 → track-1-confession/ (was track-2-testament/). |
| R1.7 | MEDIUM | pos05 existing epigraphs (Aboriginal elder + fiction caveat) not in Existing Epigraphs table. Added with insertion ordering. |
| R1.8 | LOW | McIlroy #2 missing from orphan accounting. Added. Unplaced quotes table added. |
| R1.9 | LOW | T37.3 updated: Ritchie #19 no longer used, test simplified. |
| R1.10 | LOW | Handoff rewritten: all quotes inline (Generator needs no Tier C lookup), CAUTION flags on special cases. |

---

## R2 Changelog (Red Team Fixes)

| ID | Severity | Fix |
|----|----------|-----|
| H1 | HIGH | pos24 Hoare quote: restored full 4-sentence version. Final sentence ("It is a price which the very rich find most hard to pay") was lost in truncation. Tier B table, handoff, and source now consistent. |
| M1 | MEDIUM | pos28: handoff now specifies Brooks epigraph goes BELOW colored convergence rules, not above. Rules are structural markers. |
| M2 | MEDIUM | pos24+pos25 consecutive Hoare: accepted trade-off, documented in Tier B table note. |
| L1 | LOW | pos05: handoff now tells Generator to remove stale `% TODO: epigraph` comment. |
| L2 | LOW | T37.4: added pos05 elder/caveat preservation + pos28 colored rules preservation. |
| L3 | LOW | Author concentration (41% Perlis+Dijkstra): documented in Design Principle. Accepted — reflects the canon. |

---

## R3 Changelog (Red Team Fixes)

| ID | Severity | Fix |
|----|----------|-----|
| M1 | MEDIUM | `\vspace` double-spacing bug: special cases (pos05, pos24) now explicitly say "use `\vspace{0.3cm}` NOT the standard `\vspace{0.5cm}`" to prevent 0.8cm stacking. Both phasing section and handoff SPECIAL CASES updated. |
| L1 | LOW | McIlroy attribution: "TAOUP" expanded to "The Art of Unix Programming" everywhere (Tier C table + handoff). |
| L2 | LOW | pos24: handoff now says "above the `% Abstract epigraph` comment" to prevent comment/quote misalignment. |

---

*Plan by Argus (Auditor), 2026-02-23. R1+R2+R3 fixes applied. Source research in `~/software/aurasys-memory/research/unix-epigraphs.md`.*
