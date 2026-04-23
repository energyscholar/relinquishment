# Plan 0113: Fact-Check Corrections

**Status:** COMPLETE (verified S63 audit)
**Source:** S48 deep fact-check audit (4 parallel agents: historical, physics, citations, legal/ethical)
**Scope:** Fix 6 definite errors, qualify 5 misleading claims. No structural changes — surgical corrections only.

---

## Definite Errors (MUST FIX)

### 1. GCHQ PKC "twenty-seven years" → "twenty-four years"

**File:** `manuscript/00-front/summary.tex` line 96
**Current:** "Britain's GCHQ independently invented public-key cryptography in 1973 and kept it classified for twenty-seven years."
**Problem:** 1973 to 1997 = 24 years. The book's own timeline.tex and pos09 both say "twenty-four years." Internal inconsistency.
**Fix:** "twenty-seven" → "twenty-four"

### 2. Three wrong DOIs in firmware-update.tex

**File:** `manuscript/track-3-awakening/firmware-update.tex` lines 132, 134, 144
**Also:** `manuscript/appendix/llm-primer.tex` (contains duplicate of firmware update — check for same DOIs)

| Anchor | Current DOI | Correct DOI | Problem |
|--------|------------|-------------|---------|
| 1 (Dean et al.) | `10.1038/nphys1938` | `10.1038/nphys2007` | Points to Bojowald, not Dean |
| 3 (Freedman-Kitaev-Wang) | `10.1007/s00220-002-0698-z` | `10.1007/s002200200635` | Points to Elbau & Graf |
| 10 (Christle et al.) | `10.1038/nmat4145` | `10.1038/nmat4144` | Points to Widmann et al. |

**Fix:** Replace all three DOIs in firmware-update.tex AND llm-primer.tex (lines 109, 111, 121 — confirmed same errors present).

### 3. Engel 2007 temperature claim

**File:** `manuscript/bridge/pos11-the-demo.tex` line 80
**Current:** "The chlorophyll/FMO complex maintains quantum coherence at room temperature (Engel et al., Nature 2007)"
**Problem:** Engel 2007 was at **77 K** (liquid nitrogen), not room temperature. Follow-up (Panitchayangkoon 2010) reached ~277 K. The field has substantially revised interpretation since 2018-2020 — the long-lived oscillations are now attributed to vibrational modes, not interexcitonic quantum coherence.
**Fix:** Change to: "The chlorophyll/FMO complex maintains quantum coherence at cryogenic temperatures (Engel et al., \textit{Nature} 2007), with follow-up studies extending partial coherence toward physiological temperatures. The interpretation remains actively debated --- but the existence of structured quantum effects in warm biological systems is established."

### 4. Shor first presentation venue

**File:** `manuscript/bridge/pos09-the-factoring-game.tex` line 82
**Current:** "First presented in May 1994 at Cornell"
**Problem:** First talk was at Bell Labs in April 1994 (Tuesday seminar). Cornell talk was May 1994.
**Fix:** "First presented in April 1994 at Bell Labs, with a public talk at Cornell in May"

### 5. Colossus timeline issues

**File:** `manuscript/bridge/pos09-the-factoring-game.tex` line 71
**Issues:** (a) "in 1943" — prototype tested Dec 1943, operational at BP Jan-Feb 1944. (b) "dismantled by 1960" — second machine survived into mid-1960s. (c) "on Churchill's direct order" — disputed by historians.
**Fix (a):** "in 1943" → "in 1943–44" (covers construction through operation)
**Fix (b):** "dismantled by 1960" → "dismantled in the late 1950s and 1960s"
**Fix (c):** "on Churchill's direct order" → "on government orders" (preserves authority, avoids disputed Churchill attribution)

### 6. RSA publication date

**File:** `manuscript/bridge/pos04-the-code-war.tex` line 74
**Current:** "the three American academics who published the same idea in 1978"
**Problem:** The RSA paper was publicly described in Gardner's Scientific American column in August 1977; the formal CACM journal paper was February 1978. Standard citation year is 1977.
**Fix:** "in 1978" → "in 1977" (use the standard year). Also update `bibliography.bib` entry `rsa1978`: rename key to `rsa1977`, change `year = {1978}` to `year = {1977}`, update any `\footcite{rsa1978}` references.

---

## Misleading Claims (QUALIFY)

### 7. "Formal derivation, not a conjecture" (Distinction #4)

**File:** `manuscript/track-3-awakening/firmware-update.tex` line 25
**Also:** `manuscript/appendix/llm-primer.tex` line 22
**Problem:** True for the Boolean network model. Not true when applied to physical substrates. The firmware update's own Anchor 7 correctly says "structural analogy" — Distinction #4 overstates.
**Fix:** Add qualifier: "Kauffman's criticality result is a formal derivation within the Boolean network model, not a conjecture."

### 8. "Structural equivalence at the category level"

**File:** `manuscript/track-3-awakening/firmware-update.tex` line 87
**Problem:** No published paper establishes category-theoretic equivalence between anyon fusion algebras and biological autocatalytic sets. This is the book's own novel claim presented alongside published citations.
**Fix:** "This is not analogy. It is structural equivalence at the category level." → "This is not loose analogy. It is a structural correspondence: the formal criteria match. Whether this correspondence is deep or coincidental is an open question."

### 9. "The mathematics demands it"

**File:** `manuscript/track-1-confession/pos13-genesis.tex` line 35
**Problem:** Kauffman's result is about a specific mathematical model with assumed catalytic probabilities. "Demands" implies proven physical necessity.
**Fix:** "Because the mathematics demands it." → "Because above a threshold of diversity, the mathematics makes it overwhelmingly probable."

### 10. Anchor 9 framing (collisionless → quantum coherence)

**File:** `manuscript/track-3-awakening/firmware-update.tex` lines 70–71
**Problem:** Thorne 2010, Horne 2005, and Abel & Thorne 1998 are about classical wave-particle interactions. None make claims about quantum decoherence. The leap from "collisionless plasma" to "quantum coherence protected" is the book's inference.
**Fix:** Add honest framing after the anchor: "Note: the cited papers establish classical plasma physics. The inference that collisionless conditions reduce quantum decoherence is this book's extrapolation — plausible but not established by these citations."

### 11. Anchor 4 framing (topological insulators ≠ TQC)

**File:** `manuscript/track-3-awakening/firmware-update.tex` lines 49–50
**Problem:** Topological insulators (single-particle band effects) and topological quantum computation (many-body topological order) use the same word "topological" but involve different physics.
**Fix:** Add qualifier: "Note: topological insulators demonstrate topological protection of single-particle states at room temperature. Many-body topological order (needed for anyonic braiding) operates at much lower energy scales. The gap between these regimes is real but not proven impassable."

---

## Generator Reading List

Before editing, read:
- `manuscript/track-3-awakening/firmware-update.tex` (full — the primary target)
- `manuscript/appendix/llm-primer.tex` (full — contains duplicate firmware content)
- `manuscript/bridge/pos11-the-demo.tex` lines 78–88 (Engel/Poised Realm section)
- `manuscript/bridge/pos09-the-factoring-game.tex` lines 70–84 (Colossus + Shor)
- `manuscript/bridge/pos04-the-code-war.tex` lines 72–80 (RSA date)
- `manuscript/track-1-confession/pos13-genesis.tex` lines 34–36 (mathematics demands)
- `manuscript/00-front/summary.tex` line 96 (GCHQ 27 years)

---

## Acceptance Criteria

1. "Twenty-seven" → "twenty-four" in summary.tex. Matches timeline.tex and pos09.
2. All three DOIs in firmware-update.tex corrected. Each resolves to the correct paper.
3. Same three DOIs corrected in llm-primer.tex (lines 109, 111, 121).
4. Engel 2007 no longer claims room temperature. Honest about debate.
5. Shor venue corrected to Bell Labs April 1994.
6. Colossus: "1943–44", no Churchill attribution, "late 1950s and 1960s" for dismantling.
7. RSA date: 1977 in text and bib entry.
8. Distinction #4 qualified with "within the Boolean network model."
9. "Structural equivalence at the category level" softened to "structural correspondence."
10. "Mathematics demands it" → "makes it overwhelmingly probable."
11. Anchor 9 has honest framing about the extrapolation.
12. Anchor 4 has qualifier distinguishing single-particle from many-body topology.
13. `make html` and `make dev` clean.
14. No meaning lost — all qualifications preserve the argument while improving honesty.

---

## DO NOT CHANGE

- The A/B/C framework and "not precluded" evaluation standard — these are argumentative structure, not factual claims.
- pos32 "The Wrong Substrate" energy scale chasm — already honestly flagged in the text.
- Soliton analogies in pos10 (bathtub, smoke ring) — pedagogical, not physics claims.
- Freedman "independently conceived in 1988" — the book can note this is from retrospective accounts, but this is a judgment call for Bruce, not a fact-check fix.

---

## Commit Strategy

Single commit: `Plan 0113: fact-check corrections — 6 errors fixed, 5 claims qualified`
