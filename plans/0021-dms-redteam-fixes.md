# Plan 0021: DMS Red Team Fixes

**Purpose:** Fix all issues found in DMS artifact red team before shipping.
**Prerequisite:** Plans 0001-0020 executed. PDF builds clean (203pp, 672KB).
**Deliverable:** Rebuilt `Relinquishment.pdf` + DMS copy, all red team findings resolved.

---

## Decisions (finalized by Bruce)

### FIX 1: Coventry in Ch 26 (CRITICAL)
**Decision: DELETE the Coventry sentence.**
File: `manuscript/track-1-confession/pos26-interdiction.tex` line 16.
Delete the sentence beginning "Prime Minister Winston Churchill considered..." and ending "...learn of the Ultra Secret."
Keep the surrounding text. The paragraph should read:
> "The Sponsors of the original QC project wanted an Ultra Secret Magic Decoder Box... This is utterly useless once your rivals know it exists. The closest historical parallel, the Ultra Secret of World War Two, which read encrypted military communiques by the Third Reich, remained a secret until 1975, 35 years after its origin."
(Next paragraph about Official Secrets Act follows immediately.)

### FIX 2: Placeholder images (CRITICAL)
**Decision: REMOVE ALL placeholder image calls.**
Delete these lines entirely (the `\graphicsonly{...}` blocks containing `\placeholderimage`):
1. `manuscript/track-2-testament/pos02-alpha-farm.tex` lines 20-23
2. `manuscript/track-3-awakening/pos24-instantiation.tex` line 19 (and surrounding `\graphicsonly{}` wrapper)
3. `manuscript/convergence/pos28-surrender.tex` line 26 (and surrounding wrapper)
4. `manuscript/track-1-confession/pos13-genesis.tex` line 19 (and surrounding wrapper)

### FIX 3: Alpha Farm stub (CRITICAL)
**Decision: DEFERRED.** Bruce is reviewing. Do NOT change pos02-alpha-farm.tex stub text.

### FIX 4: Sources appendix (CRITICAL)
**Decision: BETTER PLACEHOLDER.**
File: `manuscript/appendix/sources.tex`
Replace entire content after `\chapter{Sources}` and `\label{app:sources}` with:
```latex
A comprehensive bibliography is in preparation. Key sources are cited within individual
chapters. The Verification page provides cryptographic timestamps and third-party references.
```
Remove the `\begin{itemize}...\end{itemize}` list and "Sources will include:" text.

### FIX 5: Ken/Kevin (HIGH)
**Decision: ACKNOWLEDGE UNCERTAINTY.**
File: `manuscript/track-2-testament/pos05-the-stories.tex` line 57.
Change: `we'll call him Officer Kevin`
To: `we'll call him Officer Kevin (or Ken --- the name is uncertain after decades)`
Do NOT change pos03-the-mentor.tex (Bruce's original, uses "Ken" — provenance preserved).

### FIX 6: Kangaroo year (HIGH)
**Decision: DO NOT CHANGE ORIGINALS.**
Both Ch 3 (1977) and Ch 5 (1978) are Bruce's own tellings — provenance must be preserved.

**PLACEMENT (red team corrected):** The note goes ONLY before the kangaroo story. It must NOT cover the Srebrenica testimony that follows in the same chapter.

File: `manuscript/track-2-testament/pos05-the-stories.tex`
Insert AFTER the epigraph `\end{quote}` block (line 15) and BEFORE `\vspace{0.5cm}` (line 17), so it appears between the Aboriginal Elder quote and "The year is 1978":
```latex

\begin{quote}\small\textit{%
The following is the author's fictionalized retelling of a story he heard once, decades ago.
Details including dates may differ from other accounts in this book.
}\end{quote}
```
The Srebrenica section (starting at `\section*{Srebrenica, July 1995}`) is NOT fictionalized and must NOT be covered by this note. The `\vspace` and horizontal rule between the two sections provide visual separation.

### FIX 7: Verbatim duplicates (HIGH)
**Decision: KEEP ALL.** Spiral repetition is intentional. No changes needed.
(Reference: Illuminatus! trilogy — repetition as structural feature.)

### FIX 8: Unhedged Option-C assertions (HIGH)
**Decision: DEFERRED.** Bruce wants interactive discussion before deciding. Do NOT hedge any passages.

### FIX 9: REDACTED blocks (HIGH)
**Decision: CHANGE FORMAT to "[Material redacted by the author]" with proportional length.**

**Step 1: Update macro** in `build/preamble.tex`. Replace existing `\DMSRedacted` definition (lines 171-175) with:
```latex
\newcommand{\DMSRedacted}[1]{%
  \begin{quote}
  \textit{[Material redacted by the author --- #1]}
  \end{quote}
}
```

**Step 2: Convert raw REDACTED blocks to use macro.** Two files use raw `\texttt{[REDACTED]###...}` instead of the macro:
- `manuscript/track-2-testament/pos31-wolfram.tex` line 57: Replace the raw `\texttt{[REDACTED]\#\#\#...}` line with `\DMSRedacted{approximately 150 words}`
- `manuscript/track-2-testament/wikileaks.tex` line 10: Replace the raw `{[REDACTED]\#\#\#...}` line with `\DMSRedacted{chapter contents deferred}`

**Step 3: Update existing macro calls** with scope descriptions. The 4 existing calls pass WikiLeaks deferral text that the old macro silently discarded. The new macro displays the argument, so shorten them:
- `manuscript/track-1-confession/pos20-the-network.tex` line 60: `\DMSRedacted{subsequent transparency initiatives --- see WikiLeaks chapter}`
- `manuscript/track-1-confession/pos20-the-network.tex` line 92: `\DMSRedacted{subsequent transparency initiatives --- see WikiLeaks chapter}`
- `manuscript/track-2-testament/pos29-the-silence.tex` line 14: `\DMSRedacted{subsequent transparency initiatives --- see WikiLeaks chapter}`
- `manuscript/track-2-testament/pos29-the-silence.tex` line 22: `\DMSRedacted{subsequent transparency initiatives --- see WikiLeaks chapter}`

**No front matter addition.** Bruce authorized the format change only. No copyright.tex changes for FIX 9.

### FIX 10: Verification page filename (CRITICAL — from provenance audit)
**Decision: FIX FILENAME AND ADD URLs.**
File: `manuscript/99-back/verification.tex`
1. Line 14: Change `Relinquishment\_by\_Bruce\_Stephenson.pdf` to `Relinquishment.pdf`
2. Lines 25-28: Add URLs to each timestamp entry:
```latex
\item Cryptome (2012 --- 42 Wayback Machine captures, identical content hash across 12 years)\\
  \url{http://cryptome.org/2012/03/qc-footprint.htm}
\item Slashdot (UID 801915 --- account creation date establishes presence)\\
  \url{http://slashdot.org/comments.pl?sid=2926019&cid=40375589}
\item Blogspot (2012--2025 --- 30+ Wayback Machine captures)\\
  \url{https://postquantumhistoricalretrospective.blogspot.com/}
\item Substack, \texttt{postquantum.substack.com} (2024--2025 --- 10+ Wayback Machine captures)\\
  \url{https://postquantum.substack.com}
```

### FIX 11: Coventry header and callback in Ch 4 (HIGH — from provenance audit)
The Coventry *body text* in pos04-the-code-war.tex is correctly disputed. But:
- Line 42 section header: "Churchill Let Coventry Burn" — states myth as fact
- Line 132 callback: "having watched Churchill let Coventry burn" — states myth as fact

Fix header (line 42): Change `Churchill Let Coventry Burn` to `The Coventry Question`
Fix callback (line 132): Change `having watched Churchill let Coventry burn` to `having heard that Churchill may have let Coventry burn`

**Note (red team):** The callback is in a rhetorical climax. This fix trades some rhetorical punch for factual integrity. The chapter already correctly disputes the myth in the body (lines 44-100+), so the callback should be consistent with the chapter's own conclusion. Worth the tradeoff.

### FIX 12: Clean repo root crust
Delete old JOBNAME build artifacts from repo root:
```bash
rm -f Relinquishment_by_Bruce_Stephenson.aux Relinquishment_by_Bruce_Stephenson.auxlock \
  Relinquishment_by_Bruce_Stephenson.fdb_latexmk Relinquishment_by_Bruce_Stephenson.fls \
  Relinquishment_by_Bruce_Stephenson.glg Relinquishment_by_Bruce_Stephenson.glo \
  Relinquishment_by_Bruce_Stephenson.gls Relinquishment_by_Bruce_Stephenson.ist \
  Relinquishment_by_Bruce_Stephenson.log Relinquishment_by_Bruce_Stephenson.toc \
  Relinquishment_by_Bruce_Stephenson.upa main.auxlock
```
Delete orphan image (clearly unrelated to any chapter):
```bash
rm -f images/600_ton_subsidized_liner_astral_dawn.jpeg
```
**KEEP `images/alpha-farm-1.jpg`** — FIX 3 (Alpha Farm) is deferred; Bruce may want this image when he revises that chapter.

---

## Red Team Corrections Applied

1. **FIX 6 placement precision** — Note now explicitly placed BEFORE kangaroo story, NOT covering Srebrenica testimony. Visual separation already exists.
2. **FIX 9 scope reduction** — Removed unauthorized copyright.tex addition. Bruce authorized format change only.
3. **FIX 9 call site audit** — Discovered pos31-wolfram.tex and wikileaks.tex use RAW `\texttt{[REDACTED]###}` instead of the macro. Added Step 2 to convert these. Shortened existing call arguments for new display format.
4. **FIX 12 image preservation** — Kept `alpha-farm-1.jpg` since FIX 3 (Alpha Farm) is deferred and Bruce may want it.
5. **FIX 11 tradeoff noted** — Documented rhetorical punch vs factual integrity tradeoff.
6. **TC8 count specified** — 6 total DMSRedacted instances (was "matches expected count").
7. **TC11-13 added** — Srebrenica negative test, old REDACTED format gone, image preserved.

---

## Execution Phases

### Phase 1: Apply fixes
Apply FIXes 1, 2, 4, 5, 6, 9, 10, 11, 12 as specified above. Skip FIX 3 (deferred) and FIX 8 (deferred).

### Phase 2: Rebuild and verify
1. `make clean && make` — must build clean with 0 errors
2. Extract text with `pdftotext Relinquishment.pdf -`, verify:
   - `grep -i "placeholder"` → 0 results
   - `grep -i "under development"` → 0 results
   - `grep "tens of thousands"` → 0 results
   - `grep "Relinquishment_by_Bruce_Stephenson"` → 0 results
   - `grep "Material redacted"` → confirms new redaction format
   - `grep "cryptome.org"` → confirms URL on verification page
3. `sha256sum Relinquishment.pdf` → record new hash
4. `qpdf --check Relinquishment.pdf` → no structural errors

### Phase 3: Package DMS
1. `cp Relinquishment.pdf dms/Relinquishment_imperfect_beats_nonexistent.pdf`
2. Update `SHA256SUM.txt` with new hash, page count, file size
3. Report: page count, file size, hash

---

## Test Cases
- TC1: `pdftotext ... | grep -i "placeholder"` → 0 results
- TC2: `pdftotext ... | grep -i "under development"` → 0 results
- TC3: `pdftotext ... | grep "tens of thousands"` → 0 results
- TC4: `pdftotext ... | grep "Relinquishment_by_Bruce_Stephenson"` → 0 results
- TC5: Build completes with 0 LaTeX errors
- TC6: `qpdf --check Relinquishment.pdf` → no structural errors
- TC7: File size < 750KB (Gmail safe)
- TC8: `pdftotext ... | grep "Material redacted"` → 6 results (pos20 x2, pos29 x2, pos31 x1, wikileaks x1)
- TC9: `pdftotext ... | grep "cryptome.org"` → 1 result (verification page)
- TC10: `pdftotext ... | grep "Coventry Question"` → 1 result (fixed header)
- TC11: `pdftotext ... | grep "fictionalized retelling"` → 1 result (kangaroo section only, NOT Srebrenica)
- TC12: `pdftotext ... | grep "\[REDACTED\]"` → 0 results (all converted to new format)
- TC13: `ls images/alpha-farm-1.jpg` → file still exists (not deleted)
