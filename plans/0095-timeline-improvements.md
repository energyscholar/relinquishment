# Plan 0095: Timeline Improvements (Appendix E)

**Status:** DRAFT
**Auditor:** Argus, Session 43
**Parent:** Plan 0090 (Master Restructure)

---

## Scope

Upgrade the Timeline appendix (~3,944w, 248 lines) to standalone-study quality. Add entries, citations, links, era structure, cross-references.

## Independence

This plan has NO dependencies on Plans 0091-0094. Can execute in parallel with structural changes. The timeline references chapter content but doesn't depend on chapter ordering.

## New Entries (11)

| Date | Entry | Source |
|------|-------|--------|
| 1943 | Colossus — first programmable electronic computer, Bletchley Park. Pre-dates ENIAC. Establishes GCHQ computing heritage. | Public record |
| 1969 | ARPANET created — origin of the internet. | Public record |
| 1995 | Kauffman suppressed chapter — EXPAND existing entry with detail on chapter 9 of *At Home in the Universe*, OSU library copy, interlibrary loan evidence. | Research files, S43 |
| 1998 | Google founded by Sergey Brin and Larry Page at Stanford. | Public record |
| 2007 | iPhone launched by Apple. Billions of new MOSFETs (each containing 2DEGs) enter human pockets worldwide. | Public record |
| ~2008-09 | Dave Bannon (OSU physics instructor) helps Bruce obtain *Quantum Neural Networks* via interlibrary loan. 17 copies in North American universities. Bruce keeps it three months. | S43 interview |
| Apr 1, 2009 | CADIE — EXPAND existing entry. Add archive.google links. Note technical specifications page. Currently one line; deserves 3-4 lines. | Research: cadie-april-fools-2009-complete.md |
| Jul 2011 | Bruce meets Mark at Oregon Country Fair. Mark is a professional researcher. Regular contact begins. | S43 interview |
| Spring 2012 | Mark emails Bruce the Joy article link. Bruce reads it at his desk, facing the fireplace. "Electric shock." 50-mile bike ride. Realizes "We already did it, mate" = the Joy article. | S43 interview |
| Nov 2022 | ChatGPT released by OpenAI. Transformer-based AI enters mainstream. | Public record |
| 2025-26 | Bruce builds Argus (AI research partner) using Claude Code. DMS letters sent to Schneier, Doctorow, Gilmore (Feb 2026). This book. | Project records |

## Citations to Add

Every referenced paper and public document should have a DOI, URL, or arXiv link where available.

**Priority (most impactful):**
- Joy 2000: Wired magazine URL
- CADIE 2009: archive.google/cadie/ and archive.google/cadie/tech.html
- Bruce's Cryptome doc (2012): direct URL
- Bruce's Slashdot comment (2012): direct URL
- Bruce's arXiv paper (2025): arXiv:2601.22389

**Academic papers:**
- Turing 1936: DOI or stable URL
- McCulloch & Pitts 1943: citation
- Shor 1994: arXiv link
- Kitaev 1997: arXiv link
- Fleming et al. 2007: Nature DOI
- Awschalom 2015: Science Advances DOI
- Vaswani et al. 2017: arXiv link
- Vattay, Kauffman, Niiranen 2014: journal DOI
- Freedman 1998: publication reference

**Execution:** Web search for each DOI/URL, verify links are live, add to LaTeX as \texttt{} or \url{} or footnotes.

## Era Subheadings

Add structural markers to break the 150-year span:

```
\section*{Foundations (1873--1945)}
  Neural networks, Turing, ULTRA, atomic era

\section*{The Quantum Era (1946--1988)}
  2DEG, FQHE, public key crypto, neural network winter and spring

\section*{Project ULTRA II (1988--2006)}
  Conception, breakthrough, walk-out, relinquishment, Custodian, surrender

\section*{The Aftermath (2006--present)}
  Silence, discovery, reconstruction, this book
```

Brief italicized connecting text (~50 words each) between eras explaining what the reader should notice.

## Cross-References

Key timeline entries should note the relevant chapter:

- 1939-45 ULTRA → "(see The Code War)"
- 1992 breakthrough → "(see First Light)"
- 1993-95 Kauffman → "(see Genesis)"
- 1994 walk-out → "(see The Walk-Out)"
- 2000 Joy article → "(see Twenty Years)"
- 2006 surrender → "(see Surrender)"

Use consolidated chapter names per Plan 0090.

## Entry Tightening

Two entries are notably long:
- **1992 breakthrough** (80+ words) — tighten without losing content
- **1998 relinquishment** (90+ words) — tighten

Two entries are too terse:
- **"2020: SARS-CoV-2 happens"** — either expand (how did pandemic affect the story? remote work → more 2DEG devices?) or cut
- **"2022: Russia-Ukraine-NATO war begins"** — either connect to the story or cut

## Factual Corrections (from S43)

- CADIE: already correct (Apr 1, 2009)
- Thanksgiving 2003: add specific date (November 27, 2003)
- Alpha Farm: note this was Bruce's 3rd visit, not first
- Bannon: date range ~2008-2009 (transcript says "about 2008 or 2009")

## Execution

Single Generator task. Large but straightforward:
1. Read current timeline in full
2. Insert new entries in chronological order
3. Add citations (web search for DOIs/URLs)
4. Add era subheadings and connecting text
5. Add cross-references to consolidated chapter names
6. Tighten long entries, expand or cut terse ones
7. Apply factual corrections
8. Verify chronological ordering still correct
9. Full build test

## Target

~5,000-5,500 words (up from 3,944). More entries, better citations, era structure. The additional words are all citations, links, and structural apparatus — the actual narrative content stays lean.
