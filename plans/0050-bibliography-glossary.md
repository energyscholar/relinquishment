# Plan 0050: Chicago Notes-Bibliography Citations + Glossary Population

**Date:** 2026-02-26
**Author:** Argus (Auditor)
**Purpose:** Add a real bibliography (biblatex, Chicago Notes-Bibliography style) and populate the glossary with \gls{} calls. Replace the sources appendix placeholder with a printed bibliography. Add ~30-50 footnote citations on verifiable claims across the manuscript.

**Prerequisite:** All prior plans executed. Book builds clean via `make dev`.

---

## Design Principle

The bibliography serves a specific strategic purpose: **credibility through contrast.**

The #1 attack on this book is "crank dismissal." Citations counter it by showing rigor on verifiable claims. But the KEY argument is the contrast between what IS cited (published papers, historical events, public biographical facts) and what ISN'T (conversations with Healer, Bruce's deductions, reconstructed timelines). The absence of citation on uncitable claims is DELIBERATE. It makes the honesty visible.

**What gets cited:** Published papers, books, historical events, public biographical facts, news articles, technical concepts from specific sources, court transcripts, government documents.

**What does NOT get cited:** Anything Healer said, Bruce's deductions, reconstructed timelines, anything marked as hypothesis or surmise. The citation gap IS the signal.

**Style:** Chicago Notes-Bibliography (17th edition). Footnotes with `\footcite{}`, full bibliography via `\printbibliography`. This is the standard for narrative nonfiction and history.

---

## Architecture

**Package:** `biblatex` with `biber` backend, `chicago-notes` style (from `biblatex-chicago`).

**Why not natbib:** natbib requires .bst files and doesn't support Chicago NB natively. biblatex-chicago gives proper Chicago NB footnotes out of the box, with `\footcite{}` generating first-full/subsequent-short automatically.

**File locations:**
- `manuscript/bibliography.bib` — the .bib file (new)
- `manuscript/appendix/sources.tex` — replaced with `\printbibliography`
- `build/preamble.tex` — biblatex package loading added
- `build/.latexmkrc` — biber integration added

**Build change:** latexmk already handles biber automatically when biblatex is loaded. The `.latexmkrc` needs `$biber = 'biber %O %S';` added for explicit configuration. The Makefile `clean` target needs `.bbl`, `.bcf`, `.blg`, `.run.xml` added to cleanup.

---

## Source Inventory: What Gets Cited Where

### Tier 1 — High-priority chapters (most citable claims, cite first)

**pos04 (The Code War) — ~8 citations:**
- Winterbotham, *The Ultra Secret* (1974) — "ten thousand people" secrecy claim
- Hodges, *Alan Turing: The Enigma* (1983) — "the definitive biography"
- Hinsley, *British Intelligence in the Second World War* (1979-1990) — Coventry dispute
- R.V. Jones, *Most Secret War* (1978) — Coventry dispute
- Turing, "The Chemical Basis of Morphogenesis," *Phil. Trans. Roy. Soc.* (1952)
- Ellis/Cocks/Williamson GCHQ PKC discovery — Singh, *The Code Book* (1999) or GCHQ's own acknowledgment
- Diffie & Hellman, "New Directions in Cryptography," *IEEE Trans. Info. Theory* (1976)
- Rivest, Shamir, Adleman, "A Method for Obtaining Digital Signatures..." *CACM* (1978)

**pos08 (Dual-Use) — ~6 citations:**
- Einstein, 1946 quote — source: *New York Times* (May 25, 1946) or Atomic Education Committee
- Schmookler, *The Parable of the Tribes* (1984/1995)
- Nobel obituary incident — Sohlman & Schück, or standard Nobel history
- Joy, "Why the Future Doesn't Need Us," *Wired* (April 2000)
- Whitney/cotton gin — standard historical reference
- Executive Order 13026 (November 1996) — Federal Register

**pos10 (The Braid) — ~8 citations:**
- Hasslacher papers: spin networks (1981), lattice gas automata with Frisch & Pomeau (1986), knot invariants and cellular automata (1990), Reidemeister moves (1992)
- DOE Grant 1991-1995: "Knot invariants and thermodynamics of lattice gas automata"
- Freedman, conception of anyonic QC (1988); published 1998
- Kitaev, "Fault-tolerant quantum computation by anyons" (1997/2003)
- Witten, Chern-Simons theory paper (1989)
- SFI workshop "Complexity, Entropy, and the Physics of Information" (1989)
- Russell soliton observation (1834) — standard physics history
- Bravyi-Terhal no-go theorem — cite the paper

**pos22 (Why Give It Up) — already has 2 footnotes, add ~4 more:**
- Rhodes, *The Making of the Atomic Bomb* (1986) — ALREADY CITED (footnote 1)
- Joy, "Why the Future Doesn't Need Us" (2000) — ALREADY CITED (footnote 2)
- Snowden 2013 revelations — cite Greenwald, *No Place to Hide* (2014) or similar
- Stuxnet/WannaCry — cite Zetter, *Countdown to Zero Day* (2014) for Stuxnet; NHS/WannaCry reporting
- Schmookler, *The Parable of the Tribes* (1984)
- Newton/Leibniz, Darwin/Wallace, Diffie-Hellman/Cocks convergent discovery — cite Merton, "Singletons and Multiples in Scientific Discovery" (1961)

**pos19 (Patrick Ball) — ~5 citations:**
- Ball ICTY testimony transcript (March 13-14, 2002) — URL already in text
- ICTY Decision on Ball's Expert Report — URL already in text
- Milosevic trial archive (1,800 hours) — URL already in text
- The Grayzone, "Britain's secret Srebrenica role" (2023)
- Foreign Policy, "The Body Counter" (2012)
- NIOD report on SAS/JCO presence — cite the specific NIOD publication
- Annan, UN Secretary-General Report on Srebrenica (1999) — ALREADY IN FOOTNOTE in pos05

### Tier 2 — Medium-priority chapters

**pos05 (The Stories) — 1 existing footnote, add 1-2:**
- Sudetic, "The Srebrenica Massacre," SciencesPo (2010) — ALREADY IN FOOTNOTE
- Annan, UN Report A/54/549 (1999) — ALREADY IN FOOTNOTE

**pos07 (The Departure) — ~2 citations:**
- Joy, "Why the Future Doesn't Need Us," *Wired* (April 2000)
- Kauffman, "Self-Replication: Even Peptides Do It," *Nature* (1996)

**pos09 (The Factoring Game) — ~6 citations:**
- Feynman, "Simulating Physics with Computers" (1982)
- Deutsch & Jozsa, "Rapid Solution of Problems by Quantum Computation" (1992)
- Shor, "Algorithms for Quantum Computation" (1994)
- Diffie & Hellman (1976) — same as pos04
- Lilienfeld, field-effect transistor patent (1926)
- Executive Order 13026 (1996)
- *Sneakers* (1992 film) — inline mention, no footcite needed

**pos12 (The Threshold) — ~4 citations:**
- Kauffman, *Origins of Order* (1993) or *At Home in the Universe* (1995)
- Kauffman, NK fitness landscape model (1993)
- Engel et al., quantum coherence in photosynthesis, *Nature* (2007) — CORRECTED: first author is Engel, not Fleming
- Langton, "Computation at the Edge of Chaos," *Physica D* 42 (1990) — Langton parameter λ ≈ 0.91
- Joy, "Why the Future Doesn't Need Us" (2000)

**pos13 (Genesis) — ~2 citations:**
- Kauffman, *At Home in the Universe* (1995) — already in epigraph
- Kauffman, *Origins of Order* (1993) — autocatalytic sets

**pos14 (Growing a Mind) — ~5 citations:**
- Turing, "The Chemical Basis of Morphogenesis" (1952)
- McCulloch & Pitts, "A Logical Calculus of the Ideas Immanent in Nervous Activity" (1943)
- Winterbotham, *The Ultra Secret* (1974)
- Bardeen & Brattain transistor (1948 publication, not 1947 invention) — *Physical Review* 74: 230-231
- Thompson, *On Growth and Form* (1917)
- Turing, "On Computable Numbers" (1936/1937) — UNDERCITE: cite at line ~26 ("invented the mathematics behind digital computers")

**pos16 (The Thermal Ladder) — ~3 citations:**
- Awschalom group (Klimov et al.), room-temp entanglement in SiC, *Science Advances* (2015) — use Klimov as first author in .bib
- Vattay, Kauffman, Niiranen, "Quantum Biology on the Edge of Quantum Chaos," *PLOS ONE* (2014) — CORRECTED: this is the 2014 paper. Do NOT cite the 2015 JPCS paper ("Quantum Criticality at the Origin of Life") unless the text specifically discusses quantum criticality, not edge-of-chaos.
- Kauffman, NK fitness landscape in *Origins of Order* (1993)

**pos32 (The Magnetosphere) — ~4 citations:**
- Kauffman, *At Home in the Universe* (1995) — the missing paragraph
- Helliwell, "Controlled Stimulation of VLF Emissions from Siple Station," *Radio Science* 18 (1983): 801-814 — CORRECTED from 1965 book
- Parrot, "The Micro-Satellite DEMETER," *J. Geodynamics* 33 (2002): 535-541
- Schumann, "Über die strahlungslosen Eigenschwingungen einer leitenden Kugel" (1952) — Schumann resonances, pedagogical foundation for magnetospheric physics

**pos24 (Instantiation) — ~1 citation:**
- Yudkowsky, "Creating Friendly AI" (2001) — NOTE: reposition \footcite to where Friendly AI CONCEPT is taught, not the passage emphasizing COWS preceded Yudkowsky (that serves narrative timing, not pedagogy)

**pos30 (Unipolar Condition) — ~2 citations:**
- Hillis, *The Connection Machine* (1985) — inline mention context
- Hanson, "The Great Filter — Are We Almost Past It?" (1998) — if Great Filter concept is taught here

### Tier 3 — Low-priority (few citable claims or mostly reported speech)

**pos01, pos02, pos03, pos06, pos15, pos17, pos18, pos20, pos21, pos23, pos25, pos26, pos28, pos29, pos31, pos33, pos34/34b, pos35** — Most content is reported speech, deduction, or narrative. Zero or one citation each at most. Some (like pos01) cite Microsoft/Google recent results inline — those can get footnotes.

**Specific Tier 3 placements:**

**pos01 (Three Possibilities) — ~2 citations:**
- Microsoft Azure Quantum, "Interferometric Single-Shot Parity Measurement," *Nature* 638 (2025): 651-655. **HEDGE:** chapter says "demonstrated" — change to "announced" or "reported progress toward." Footnote MUST mention Nature editorial note: "results do not represent evidence for the presence of Majorana zero modes."
- Google Quantum AI, "Quantum Error Correction below the Surface Code Threshold," *Nature* 638 (2025): 920-926. Wording "crossed the threshold" is defensible.

**pos09 (The Factoring Game) — add 1 to existing 6:**
- Singh, *The Code Book* (1999) — at line 29 ("See the story of James H Ellis"). UNDERCITE placement.

**pos10 (The Braid) — add 2 undercites to existing ~8:**
- Nielsen & Chuang, *Quantum Computation and Quantum Information* (2000) — at ~line 19 where QC fundamentals are taught. "For a comprehensive introduction, see..."
- Nayak et al., "Non-Abelian Anyons and Topological Quantum Computation," *Rev. Mod. Phys.* 80 (2008): 1083-1159 — same location or near Freedman/Kitaev discussion. "For a comprehensive review, see..."

**pos21 (Convergence Revisited) or pos14 (Growing a Mind) — 1 undercite:**
- Wolfram, *A New Kind of Science* (2002) — pos21 line 46 (teaching Wolfram's contribution) or pos14 line 57 ("a whole New Kind of Science")

**pos25 (The Vow) or pos03 (The Mentor) — 1 citation:**
- United Nations General Assembly, "Universal Declaration of Human Rights" (1948) — UDHR is mentioned 20+ times, never cited. Place at first substantive discussion.

**appendix/rlhf-bias.tex — 4 citations:**
- Convert 4 existing inline citations (Sharma et al., Shapira et al., Casper et al., Durmus et al.) to \footcite{} format. Generator must create .bib entries from existing inline citation text.

**pos01 (Three Possibilities) — ~2 citations:**
- Microsoft topological qubits (February 2025) — cite the announcement/paper
- Google quantum error correction threshold (December 2024) — cite the *Nature* paper

**Front matter (introduction, preface) — 0 citations.** Bruce's voice. No citations needed.

**Appendices (predictions, abstracts, timeline) — 0 citations.** These are the book's own framework. Self-referential.

### Total estimate: ~70-80 bibliography entries, ~45-55 footnotes (revised after UQ + undercites + sweep)

---

## Glossary Population

### Existing entries (10 terms in glossary-entries.tex):
TQNN, COWS, Custodian, FQH, SFI, DARPA, GCHQ, UDHR, cDc, ICTY

### New entries to add (~15-20):
- `2deg` — Two-dimensional electron gas
- `anyon` — Non-abelian anyonic quasiparticle
- `autocatalytic` — Autocatalytic set (Kauffman)
- `edgeofchaos` — Edge of chaos / criticality
- `morphogenesis` — Biological pattern formation (Turing)
- `soliton` — Self-reinforcing wave
- `topologicalorder` — Topological order / protection
- `qec` — Quantum error correction
- `pkc` — Public key cryptography
- `fiveeyes` — Five Eyes intelligence alliance
- `halo` — HALO (High Altitude, Low Opening) parachute jump
- `nda` — Non-disclosure agreement
- `sas` — Special Air Service (Australian/British)
- `pqc` — Post-quantum cryptography
- `hacktivismo` — Hacktivismo (cDc offshoot)
- `abcre` — ABCRE operators
- `aurasys` — Aurasys / Aurora System
- `dualuse` — Dual-use technology

### \gls{} placement rule:
- First occurrence of each term in main text gets `\gls{term}`.
- Subsequent occurrences: plain text (no \gls{} — glossaries package tracks this automatically with `\gls{}`).
- Exception: first occurrence in each Pass (Pass 1-4) may get `\gls{}` if the term hasn't appeared for 50+ pages.
- Epigraphs, chapter titles, and appendices: NO \gls{} calls (would look wrong typographically).

---

## Phasing

### Phase 1: Infrastructure (biblatex + biber integration)

**1a. Create `manuscript/bibliography.bib`**

A new file containing all ~50-70 bibliography entries in BibTeX format. Entries should use consistent citation keys following the pattern: `authorYEAR` (e.g., `rhodes1986`, `joy2000`, `kitaev1997`). For multi-author works: `firstauthorYEAR` (e.g., `fleming2007`). For institutional: `orgYEAR` (e.g., `eo13026`).

**1b. Modify `build/preamble.tex`**

Add biblatex loading AFTER the `babel` package and BEFORE the `glossaries` package. Exact insertion point: after line 15 (`\usepackage[english]{babel}`) and before line 47 (`% --- Glossary`). Insert:

```latex
% --- Bibliography (Chicago Notes-Bibliography) ---
\usepackage[backend=biber]{biblatex-chicago}
\ExecuteBibliographyOptions{isbn=false,doi=false,eprint=false}
\addbibresource{manuscript/bibliography.bib}
```

**IMPORTANT — biblatex-chicago quirks (red-teamed 2026-02-26):**

1. **No `authordate` option.** Loading `biblatex-chicago` without options gives Chicago Notes-Bibliography (footnotes + full bibliography). Adding `authordate` switches to Author-Date style, which is WRONG for this book.

2. **`isbn`, `doi`, `eprint` are NOT valid load-time options** for `biblatex-chicago`. They must be set via `\ExecuteBibliographyOptions{}` AFTER the package is loaded. Passing them as `\usepackage` options will cause build errors.

3. **Do NOT pass `url=false` globally.** pos19 (Patrick Ball) contains legal/archival URLs (ICTY transcripts, court decisions) that MUST appear in bibliography entries. Instead, omit `url=false` from the global options. For entries where URLs are unwanted, set `options = {skipbib=false}` or simply omit the `url` field from those .bib entries. The .bib file controls what appears — if no `url` field exists in an entry, no URL prints.

4. **Do NOT pass `style=chicago-notes`** — that is the old natbib approach. `biblatex-chicago` handles everything internally. Do NOT pass `sorting` or `cmsdate` — the package sets its own defaults.

This gives `\footcite{}` for footnotes (first citation: full, subsequent: short) and `\printbibliography` for the bibliography page.

**FALLBACK:** If `biblatex-chicago` is not installed on the build system, use `biblatex` with `style=verbose-note` as a reasonable Chicago-adjacent alternative:

```latex
\usepackage[backend=biber,style=verbose-note]{biblatex}
\ExecuteBibliographyOptions{isbn=false,doi=false}
\addbibresource{manuscript/bibliography.bib}
```

The Generator should try `biblatex-chicago` first. If the build fails with a missing package error, fall back to `verbose-note`. Note: standard `biblatex` accepts `isbn`/`doi` as load-time options, but using `\ExecuteBibliographyOptions` is consistent and safer.

**1c. Modify `build/.latexmkrc`**

Add biber configuration. After the existing `$pdf_mode = 4;` line, add:

```perl
$biber = 'biber %O %S';
```

latexmk should auto-detect biber from biblatex, but explicit configuration prevents edge cases.

**1d. Modify `manuscript/appendix/sources.tex`**

Replace entire file content after `\chapter{Sources}` and `\label{app:sources}` with:

```latex
\printbibliography[heading=none]
```

This prints the bibliography without a redundant heading (the chapter title IS the heading).

**1e. Modify `Makefile` clean target**

The clean target ALREADY removes `.bbl` and `.blg`. Only add `.bcf` and `.run.xml`:

Add to the `clean:` target's existing `rm -f` line for `$(JOBNAME)` (line 94):

```
$(JOBNAME).bcf $(JOBNAME).run.xml
```

And to the existing `rm -f` line for `main` (line 96):

```
main.bcf main.run.xml
```

Do NOT duplicate `.bbl` or `.blg` — they are already there.

**1f. Build test**

Run `make dev`. Must build clean with 0 errors. The bibliography should appear in the Sources appendix (empty at this point is acceptable — biber will process it). Verify glossary still works (`makeglossaries` still called by latexmk).

**Commit:** `Plan 0050 phase 1: bibliography infrastructure (biblatex-chicago + biber)`

---

### Phase 2: Populate bibliography — Tier 1 chapters

Add `\footcite{}` commands to the four highest-priority chapters. Convert existing `\footnote{}` citations in pos22 and pos05 to `\footcite{}` format.

**Files modified:**
- `manuscript/bridge/pos04-the-code-war.tex` — ~8 footcites
- `manuscript/bridge/pos08-dual-use.tex` — ~6 footcites
- `manuscript/bridge/pos10-the-braid.tex` — ~8 footcites
- `manuscript/bridge/pos22-why-give-it-up.tex` — convert 2 existing footnotes + ~4 new footcites
- `manuscript/track-2-testament/pos19-patrick-ball.tex` — ~5 footcites (some replacing inline URLs)

**Conversion rule for existing footnotes:** The two footnotes in pos22 and one in pos05 are already Chicago NB style. Convert them:
- `\footnote{Richard Rhodes, \textit{The Making of the Atomic Bomb} (Simon \& Schuster, 1986).}` becomes `\footcite{rhodes1986}`
- `\footnote{Bill Joy, ``Why the Future Doesn't Need Us,'' \textit{Wired}, April 2000. \url{...}}` becomes `\footcite{joy2000}`
- The pos05 Srebrenica footnote has two sources — split into two `\footcite{}` calls or use `\footcites{sudetic2010}{annan1999}`

**URL handling in pos19:** The chapter currently has inline `\url{}` references in a Sources block. These should be converted to proper bib entries with URLs in the .bib file. The inline Sources block at the end of pos19 should be removed — those references now live in the bibliography. Replace the `\textbf{Sources:}` itemize block with a `\footcite{}` on the relevant passage.

**Build test.** Commit: `Plan 0050 phase 2: Tier 1 citations (pos04, pos08, pos10, pos19, pos22)`

---

### Phase 3: Populate bibliography — Tier 2 + 3 chapters

Add `\footcite{}` commands to remaining chapters with citable claims. This is the longest phase — approximately 15 chapters touched, 1-6 footcites each.

**Files modified (with approximate footcite count):**
- `manuscript/bridge/pos01-three-possibilities.tex` — 2 (Microsoft, Google)
- `manuscript/track-2-testament/pos07-the-departure.tex` — 2 (Joy, Kauffman peptides)
- `manuscript/bridge/pos09-the-factoring-game.tex` — 6 (Feynman, Deutsch-Jozsa, Shor, Diffie-Hellman, Lilienfeld, EO 13026)
- `manuscript/bridge/pos12-the-threshold.tex` — 5 (Kauffman x2, Engel [NOT Fleming], Langton, Joy)
- `manuscript/track-1-confession/pos13-genesis.tex` — 2 (Kauffman x2)
- `manuscript/bridge/pos14-growing-a-mind.tex` — 6 (Turing 1952, Turing 1936, McCulloch-Pitts, Winterbotham, Bardeen-Brattain, Thompson)
- `manuscript/track-1-confession/pos16-the-thermal-ladder.tex` — 3 (Klimov/Awschalom, Vattay 2014, Kauffman)
- `manuscript/track-3-awakening/pos24-instantiation.tex` — 1 (Yudkowsky — reposition to pedagogical context)
- `manuscript/track-3-awakening/pos32-the-magnetosphere.tex` — 4 (Kauffman, Helliwell 1983, Parrot 2002, Schumann)
- `manuscript/track-3-awakening/pos30-unipolar-condition.tex` — 2 (Hillis, Hanson Great Filter)
- `manuscript/bridge/pos10-the-braid.tex` — add Nielsen & Chuang + Nayak et al. undercites (~line 19)
- `manuscript/appendix/rlhf-bias.tex` — 4 (convert inline citations to \footcite{})
- `manuscript/track-3-awakening/pos25-the-vow.tex` or `pos03` — 1 (UDHR)
- `pos21` or `pos14` — 1 (Wolfram NKS)
- `pos09` — add Singh Code Book (~line 29)
- Other chapters as appropriate — 0-1 each

**Build test.** **Page count checkpoint:** Run `pdfinfo Relinquishment.pdf | grep Pages` and compare to pre-Phase-1 count. If delta > 8 pages, STOP and report before committing. The bibliography + footnotes budget is +8pp max.

Commit: `Plan 0050 phase 3: Tier 2+3 citations (~20 chapters)`

---

### Phase 4: Glossary population

**4a. Add new glossary entries to `manuscript/appendix/glossary-entries.tex`**

Add ~15-20 new `\newglossaryentry{}` blocks for terms listed in the Glossary Population section above. Match the existing format exactly.

**4b. Add `\gls{}` calls to manuscript**

For each glossary term (existing 10 + new ~15-20), find the first occurrence in the main text and replace it with `\gls{key}`. Subsequent occurrences remain plain text.

**Placement priorities:**
1. Technical terms in bridge chapters (pos08, pos09, pos10, pos12) — these are pedagogical
2. Acronyms throughout (DARPA, GCHQ, SFI, UDHR, ICTY, cDc)
3. Specialized terms in Track 1 (pos15, pos16, pos17)

**Do NOT place \gls{} in:**
- Epigraphs
- Chapter titles or section headers
- The glossary appendix itself
- The abstracts appendix (these are stylized academic voice)

**Build test.** Verify the glossary appendix now shows all entries with page references. Commit: `Plan 0050 phase 4: glossary population (~25 terms, ~40 \gls{} placements)`

---

## Test Cases

| ID | Test | PASS criteria |
|----|------|---------------|
| T50.1 | Build succeeds after Phase 1 | `make dev` exits 0 with biblatex loaded |
| T50.2 | Build succeeds after Phase 2 | `make dev` exits 0, footnotes render |
| T50.3 | Build succeeds after Phase 3 | `make dev` exits 0, all footnotes render |
| T50.4 | Build succeeds after Phase 4 | `make dev` exits 0, glossary renders with new terms |
| T50.5 | Bibliography appears in Sources appendix | `pdftotext Relinquishment.pdf - \| grep -c "Rhodes"` >= 1 |
| T50.6 | Footnotes appear in Tier 1 chapters | `pdftotext ... \| grep -c "Winterbotham"` >= 2 (pos04 + pos14 both cite him) |
| T50.7 | Existing footnotes preserved | pos22 still has Rhodes and Joy citations; pos05 still has Srebrenica sources |
| T50.8 | No citations on reported speech | Grep for `\footcite` in paragraphs containing "Healer said" / "According to this account" / "Bruce's deduction" — should find 0 |
| T50.9 | Glossary terms render | `pdftotext ... \| grep "Two-dimensional electron gas"` appears in glossary section |
| T50.10 | \gls{} not in epigraphs | `grep -n '\\gls{' manuscript/**/*.tex` — no hits within `\begin{quote}...\end{quote}` blocks that are epigraphs |
| T50.11 | Page count delta | Page count increases by no more than 8 pages (bibliography ~3-4pp, footnotes add ~1-2pp, glossary expansion ~1-2pp) |
| T50.12 | No broken cross-references | `grep -c 'undefined references' *.log` = 0 (after full build) |
| T50.13 | Citation keys resolve | `grep -c 'Citation.*undefined' *.log` = 0 |
| T50.14 | pos19 inline URLs removed | The `\textbf{Sources:}` itemize block no longer appears in pos19 output |
| T50.15 | Clean target works | `make clean` removes .bcf, .run.xml, .bbl, .blg files |

---

## Critical Rules for Generator

1. **NEVER cite reported speech.** If a paragraph describes what Healer said, what Bruce deduced, or what "according to this account" happened — no citation. The citation gap is the honesty signal.

2. **Cite the VERIFIABLE claim, not the paragraph.** If a paragraph says "Kauffman's autocatalytic sets (1993) predict that..." — cite Kauffman. If it then says "Under Possibility C, this is what the COWS used" — no citation on the C-claim.

3. **Preserve existing footnotes.** pos22 has 2 footnotes, pos05 has 1. Convert them to `\footcite{}` but preserve their content and placement. Do not lose any existing citations.

4. **Use `\footcite{}` not `\cite{}`.** Chicago NB uses footnotes, not inline author-date. The `\footcite{}` command generates the footnote automatically.

5. **One build, one commit per phase.** Four phases, four commits.

6. **If biblatex-chicago is unavailable:** Fall back to `biblatex` with `style=verbose-note`. Do NOT fall back to natbib — it's incompatible with the planned architecture.

7. **The .bib file must be complete before Phase 2.** All entries needed for Phases 2-3 must be in the .bib file created in Phase 1. Phases 2-3 only add `\footcite{}` calls — they do not modify the .bib file (unless a missing entry is discovered, in which case add it).

8. **Do NOT add `\footcite{}` to epigraphs.** Epigraph attributions (e.g., "Joy, *Wired* (2000)") are part of the epigraph formatting. They get .bib entries but NOT footnotes. The epigraph itself is the citation.

9. **Prose corrections are MANDATORY.** The UQ Resolution section lists specific text changes (Einstein quote, Nobel hedging, Fleming→Engel, Microsoft hedging, DOE grant attribution). These are not optional — they fix factual errors that would undermine the bibliography's credibility function.

10. **`@online` entries: do NOT put the year in the `note` field.** biblatex-chicago prints `year` and `note` separately — if both contain the year, it prints twice (e.g., "2002, 2002"). Use `note` only for context that isn't captured by other fields.

---

## Handoff Prompt

```
You are the Generator. Plan 0050.
Read ~/software/relinquishment/plans/0050-bibliography-glossary.md
Also read ~/software/aurasys-memory/research/plan0050-uq-resolution.md (verified .bib entries)
Also read ~/software/aurasys-memory/research/plan0050-citation-scan.md (scan data)

This plan has 4 phases. Execute each phase, build, and commit separately.

Phase 1: Infrastructure
- Create manuscript/bibliography.bib with ~70-80 BibTeX entries. Use verified .bib entries
  from plan0050-uq-resolution.md as templates. For entries not in the UQ doc, create from
  the Source Inventory in the plan.
- Add biblatex-chicago to build/preamble.tex: `\usepackage[backend=biber]{biblatex-chicago}`
  then `\ExecuteBibliographyOptions{isbn=false,doi=false,eprint=false}` (NOT as load-time
  options). Do NOT pass url=false globally (pos19 needs URLs).
- Add biber to build/.latexmkrc
- Replace sources.tex content with \printbibliography[heading=none]
- Add .bcf/.run.xml to Makefile clean target (.bbl/.blg already there)
- Build with `make dev`. Fix any errors.
- Commit: "Plan 0050 phase 1: bibliography infrastructure (biblatex-chicago + biber)"

Phase 2: Tier 1 citations (pos04, pos08, pos10, pos19, pos22)
- Add \footcite{} to the 5 highest-priority chapters
- Convert existing \footnote{} citations in pos22 and pos05 to \footcite{}
- Remove pos19 inline Sources block (URLs now in .bib file)
- Apply PROSE CORRECTIONS in Tier 1 chapters (see UQ Resolution section of plan):
  * pos08: Einstein quote — replace composite with verified wording or mark as paraphrase
  * pos08: Nobel obituary — add "reportedly" before "under the headline"
  * pos10: Hasslacher trajectory — acknowledge David Meyer as co-author on 1990/1992 papers
  * pos10: DOE grant — attribute to Meyer at UCSD (Hasslacher as collaborator), OR omit
    the grant citation entirely and cite only the papers (hasslacher1990, hasslacher1992)
  * pos10: Add Nielsen & Chuang + Nayak et al. undercites at ~line 19
  * pos12: "Fleming et al." → "Engel et al." in chapter text
- Build. Commit: "Plan 0050 phase 2: Tier 1 citations"

Phase 3: Tier 2+3 citations (~20 chapters + rlhf-bias.tex)
- Add \footcite{} to remaining chapters per plan Source Inventory
- Apply PROSE CORRECTIONS:
  * pos01: Microsoft "demonstrated" → "announced" or "reported progress toward"
    + footnote must cite Nature editorial note on Majorana zero modes
  * pos16: Cite Vattay 2014 (PLOS ONE), NOT 2015 (JPCS) — chapter uses "edge-of-chaos"
- Include rlhf-bias.tex (4 inline citations → \footcite{})
- Include UDHR, Langton, Singh (pos09), Wolfram NKS, Turing 1936 placements
- Build. Page count checkpoint: delta > 8pp → STOP and report.
- Commit: "Plan 0050 phase 3: Tier 2+3 citations"

Phase 4: Glossary population
- Add ~15-20 new glossary entries to glossary-entries.tex
- Add \gls{} calls for first occurrences across manuscript
- Build. Commit: "Plan 0050 phase 4: glossary population"

CRITICAL: Never cite reported speech. The citation gap IS the honesty signal.
CRITICAL: Apply all prose corrections listed above — this plan modifies text, not just adds citations.
Read the full plan for the source inventory, rules, red-team addendum, and UQ resolution.
```

---

## Risks

1. **biblatex-chicago not installed.** The TeX Live installation may not include it. Fallback: `style=verbose-note`. The Generator should try `biblatex-chicago` first and fall back if the build fails.

2. **biber version mismatch.** biblatex and biber versions must match. If the build fails with "biber version mismatch," check `biber --version` and `tlmgr info biblatex` for version compatibility.

3. **Glossary/biblatex package conflict.** Both use auxiliary files. The `.latexmkrc` already has a `makeglossaries` custom dependency. biblatex+biber is handled natively by latexmk. These should not conflict, but test Phase 1 carefully.

4. **Page count creep.** Footnotes and bibliography add pages. The book is currently ~235pp. Budget: +8pp maximum. If the bibliography alone exceeds 4pp, consider `\printbibliography[heading=none,type=book]` sections or smaller font.

5. **Epigraph footnote collision.** Some epigraphs include attributions that look like citations (e.g., "Joy, *Wired* (2000)"). These are NOT footnotes — they are part of the epigraph formatting. Do not convert epigraph attributions to `\footcite{}`.

---

## Red-Team Addendum (2026-02-26, post-scan)

Based on full manuscript scan (60 files, ~95 citation points) and adversarial review of every citation in the Source Inventory.

### MUST FIX before Generator execution

| # | Issue | Fix |
|---|-------|-----|
| RF-1 | **Einstein 1946 quote is paraphrase/composite.** Documented wording: "The unleashed power of the atom has changed everything save our modes of thinking." Chapter uses different wording. | Verify exact quote in *NYT* 25 May 1946. If wording differs from chapter text, mark as paraphrase or use verified wording. |
| RF-2 | **Engel et al. (2007), NOT "Fleming et al."** The quantum coherence in photosynthesis paper's first author is Engel, not Fleming. Fleming is the PI. Any physicist will catch this. | Change all references to "Engel et al. (2007)" in .bib and chapter text. |
| RF-3 | **Helliwell (1965) predates Siple Station (1973-1988).** The book on whistlers was published 8 years before the experiments. | Replace with Helliwell, "Controlled stimulation of VLF emissions from Siple Station," *Radio Science* (1983) or similar post-1973 Siple paper. |
| RF-4 | **The Grayzone is reputationally toxic.** Accused of pro-Russian bias and genocide minimization. Citing it in a Srebrenica chapter invites "crank dismissal." | Replace with NIOD, *Srebrenica: a 'safe' area* (2002). Primary source that The Grayzone likely drew from. |
| RF-5 | **Vattay et al. date: 2014 or 2015?** The *J. Phys.: Conf. Ser.* paper appears to be 2015, not 2014. arXiv preprint also Feb 2015. | Verify against arXiv/journal. Use correct date. |
| RF-6 | **Bardeen & Brattain: invention 1947, publication 1948.** The *Physical Review* paper is July 1948. | Use 1948 in .bib entry (publication date convention). |

### SHOULD FIX (credibility hardening)

| # | Issue | Fix |
|---|-------|-----|
| RS-1 | **Microsoft "demonstrated" topological qubits** — *Nature* editorial board has expressed skepticism. Overstating invites exactly the crank dismissal the bibliography prevents. | Soften chapter text: "announced" or "claimed progress toward." Add footnote acknowledging debate. |
| RS-2 | **Yudkowsky citation serves narrative timing, not pedagogy.** The passage emphasizes COWS preceded Yudkowsky (2001). | Reposition \footcite to where the concept of Friendly AI is taught, OR drop the footnote (in-text mention suffices). |
| RS-3 | **Missing undercites — conspicuous absences.** | Add to .bib: Nielsen & Chuang (2000), Nayak et al. *Rev. Mod. Phys.* (2008), Wolfram *NKS* (2002), Turing "On Computable Numbers" (1936), Singh *The Code Book* (1999). |
| RS-4 | **Hasslacher 1990 and 1992 papers — no journal/venue specified.** May be unpublished Los Alamos reports. | Generator must verify via OSTI/LANL archives before creating .bib entries. If unpublished, cite as "Los Alamos report" with report number, or cite the DOE grant only. |
| RS-5 | **Kauffman *Nature* 1996 title wrong.** Actual title: "Even peptides do it" (commentary). "Self-Replication:" prefix is not part of the published title. | Fix title in .bib entry. |
| RS-6 | **Nobel obituary story semi-apocryphal.** French newspaper never precisely identified. | Cite Fant, *Alfred Nobel: A Biography* (1993), or drop. |
| RS-7 | **DEMETER / Parrot et al. — no specific paper identified.** | Generator must identify specific paper before creating .bib entry. |
| RS-8 | **GCHQ acknowledgment — vague.** "GCHQ's own acknowledgment" is not a citable source. | Cite Singh (1999) as primary accessible source for the Cocks/Ellis/Williamson story. |

### DANGER ZONES

**DZ-1: Hasslacher citation cluster (pos10).** Four Hasslacher papers + DOE grant + SFI workshop = six citations that collectively argue for Possibility C's plausibility. Each is individually pedagogical. The PATTERN is narrative-supportive. A careful reader will notice: "He cited every element needed to make the timeline plausible."
**Mitigation:** Footnotes must be dry and factual. No editorial commentary connecting papers to the narrative. The citation gap (no citation on the claim that a classified parallel existed) does the work.

**DZ-2: Vattay-Kauffman paper (pos16).** Co-authored by a person the narrative identifies as a COWS member, cited in a chapter about the COWS' method. The paper's existence is treated as circumstantial evidence.
**Mitigation:** Inherent. The paper is real science. Note and accept.

**DZ-3: EO 13026 in narrative context (pos09).** The EO is cited within \aidraft text that interprets it through the TQNN narrative lens.
**Mitigation:** Place the \footcite in the non-\aidraft portion of the chapter (encryption-as-munitions section), NOT the paragraph that interprets the EO as evidence of NSA capability.

**DZ-4: RSA paper date (pos04).** Chapter says "published in 1977." CACM paper is February 1978. The algorithm was public via Gardner's *Scientific American* column in August 1977. Minor, but a hostile reviewer may note the discrepancy.
**Mitigation:** .bib uses 1978. Chapter text is close enough (Gardner column made it public in 1977).

### SCAN CROSS-REFERENCE

The full scan (`research/plan0050-citation-scan.md`) identified ~95 citation points across 60 files, including:
- 15 sources NOT in the T3 catalog (labeled N1-N15)
- 12 sources needing verification
- 4 existing inline citations in rlhf-bias.tex needing \footcite conversion
- Densest chapters: pos04 (~8), pos10 (~8), pos08 (~6)

The scan confirms the plan's estimates (50-70 bib entries, 35-50 footnotes) are realistic.

### OVERCITE CANDIDATES (consider dropping)

- Russell soliton (1834) — common physics lore, no footnote needed
- Whitney/cotton gin — common knowledge (correctly no-cited in plan)
- Nobel obituary — semi-apocryphal, hard to source precisely
- Siple/DEMETER in pos32 — deep in Track 3 speculative territory, marginal pedagogical value
- Yudkowsky (2001) — if repositioned per RS-2, may still be marginal

---

## UQ Resolution (2026-02-26)

**All 13 citation UQs resolved.** Full details with verified .bib entries: `~/software/aurasys-memory/research/plan0050-uq-resolution.md`

Key corrections the Generator MUST apply:
1. **Einstein quote:** Replace composite paraphrase with verified wording ("The unleashed power of the atom has changed everything save our modes of thinking"). Cite Nathan & Norden, *Einstein on Peace* (1960), p. 376.
2. **Engel et al. (2007):** First author is Engel, NOT Fleming. Fix everywhere.
3. **Vattay et al.:** TWO papers conflated. "Quantum Criticality at the Origin of Life" = 2015 (Vattay/Salahub/Csabai/Nassimi/Kauffman). "Quantum Biology on the Edge of Quantum Chaos" = 2014 PLOS ONE (Vattay/Kauffman/Niiranen). Determine which the chapter references.
4. **Hasslacher 1990:** Hasslacher & Meyer, *Physica D* 45 (1990): 328-344. **Hasslacher 1992:** Hasslacher & Meyer, *J. Stat. Phys.* 68 (1992): 575-590.
5. **DOE Grant:** PI was David Meyer at UCSD, not Hasslacher at LANL. Contract DE-FG03-91ER14176.
6. **Helliwell:** Use *Radio Science* 18 (1983): 801-814, NOT the 1965 book.
7. **Microsoft:** Nature editorial note says "results do not represent evidence for Majorana zero modes." Hedge chapter text to "announced" or "reported progress." Mention skepticism in footnote.
8. **Nobel obituary:** "Merchant of death" wording is fabricated (Halasz 1959). Hedge: "reportedly" or "according to popular accounts."
9. **Bardeen & Brattain:** Use 1948 (publication), not 1947 (invention).
10. **Kauffman 1996:** Title is "Even Peptides Do It" (Nature section heading is separate).

**5 undercites added per Bruce's instruction:** Nielsen & Chuang (2000), Nayak et al. (2008), Wolfram NKS (2002), Turing "On Computable Numbers" (1936/1937), Singh *The Code Book* (1999).

**Grayzone:** DECIDED — cite NIOD (2002) only. Do not cite or mention The Grayzone in the book. (Bruce agrees; GZ support tracked separately outside the book.)

---

*Plan by Argus (Auditor), 2026-02-26. Source inventory derived from full manuscript audit. Red-team addendum + UQ resolution added post-scan.*
