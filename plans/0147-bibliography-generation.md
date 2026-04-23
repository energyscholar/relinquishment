# Plan 0147: Bibliography/Sources — Complete Audit and Fix

**Status:** COMPLETE (verified S63 audit)
**Created:** 2026-04-09
**Annealed:** 2026-04-09 (medium + low + low + low)
**Auditor:** Argus

---

## Current State

### LaTeX/PDF Pipeline (working)
- `manuscript/bibliography.bib`: **61 entries** (books 17, articles 27, online/misc 11, preprints 1, tech reports 1, legal/archival 4).
- `build/preamble.tex`: biblatex-chicago (Chicago Notes-Bibliography 17th ed.), biber backend.
- `manuscript/appendix/sources.tex`: `\printbibliography[heading=none]` — correct for LaTeX/biber.
- PDF citations render correctly via `make dev` (biber runs).

### HTML Pipeline (PRIMARY DISTRIBUTION — BROKEN)
- Build order: `preprocess.py patch()` → pandoc → `preprocess.py --fix-html`
- Pandoc does **not** run biber. All `\footcite{}` / `\cite{}` become empty `<span class="citation" data-cites="key1 key2"></span>` (space-separated keys in the attribute).
- **87 empty citation spans** in the HTML. Every footnote referencing a .bib entry is blank.
- The Sources appendix (`#app:sources`) is an empty `<details>` element — `\printbibliography` produces nothing.
- EPUB has the same bug (same pandoc path).

---

## Gap Analysis

### G1. Missing .bib Entry
| Key | Cited in | Likely reference |
|-----|----------|-----------------|
| `sharma2005` | `spine/the-wrong-substrate.tex:102`, `track-3-awakening/pos32-the-magnetosphere.tex:116` | Sharma, A.S. et al. (2005) magnetospheric complexity paper. **Bruce to confirm.** |

### G2. Citation Syntax Bug
`\footcite{kitaev2003, nayak2008}` (comma-separated) in 4 files total. Pandoc converts this to `data-cites="kitaev2003 nayak2008"` which actually works for the HTML fix (space-separated keys). Still worth fixing in LaTeX for biber correctness.

Files: `spine/three-possibilities.tex:66`, `spine/why-relinquish.tex:24`, `bridge/pos01-three-possibilities.tex:66`, `bridge/pos06-the-secret.tex:23`. Only the 2 spine/ files are in the build path; bridge/ files are not (except `firmware-update`).

### G3. Uncited .bib Entries
| Key | Status | Action |
|-----|--------|--------|
| `helliwell1983` | Magnetosphere/VLF — future content | KEEP |
| `mccullochpitts1943` | Hardcoded in timeline footnote | Convert to \footcite (G4) |
| `parrot2002` | DEMETER satellite — future content | KEEP |
| `schumann1952` | Schumann resonances — future content | KEEP |

All four should appear in the generated Sources bibliography regardless of citation status.

### G4. Hardcoded Inline References

**In the build path (fix these):**

*Convert to \footcite (entry exists in .bib):*
1. `timeline.tex:29` — Turing 1936 → `\footcite{turing1936}`
2. `timeline.tex:247` — Engel 2007 → `\footcite{engel2007}`
3. `timeline.tex:277` — Vattay 2014 → `\footcite{vattay2014}`
4. `timeline.tex:279` — Klimov 2015 → `\footcite{klimov2015}`
5. `timeline.tex:35` — McCulloch & Pitts 1943 → `\footcite{mccullochpitts1943}`
6. `timeline.tex:155` — Shor 1994 → `\footcite{shor1994}`
7. `timeline.tex:175` — Kitaev 1997 → `\footcite{kitaev2003}` (arXiv 1997, published 2003; key reflects publication year)
8. `timeline.tex:192` — Joy 2000 → `\footcite{joy2000}`
9. `predictions.tex:49` — Stephenson arXiv → `\footcite{stephenson2025}`
10. `spine/the-braid.tex:85` — Bouwmeester 1997 → `\footcite{bouwmeester1997}` (after adding to .bib)

*Add to .bib first, then convert (step 10 above depends on step 11):*
11. `timeline.tex:85` — Bouwmeester et al. 1997, Nature 390:575-579 → ADD `bouwmeester1997`
12. `timeline.tex:283` — Vaswani et al. 2017, "Attention Is All You Need" → ADD `vaswani2017`

*Keep inline (verification URLs, not academic citations):*
13. `timeline.tex:253` — Google CADIE 2009 (archival URLs)
14. `timeline.tex:267` — Cryptome.org 2012
15. `timeline.tex:271` — Slashdot 2012

**NOT in build path (skip):**
- `bridge/pos01-three-possibilities.tex`, `bridge/pos06-the-secret.tex`, `bridge/pos10-the-braid.tex`, `track-3-awakening/pos32-the-magnetosphere.tex` — these are pre-Z-restructure files not included via main.tex (only `track-3-awakening/firmware-update.tex` is included).

### G5. Missing DOIs

**High priority (9 foundational papers):**
- `bennett1993` — PRL 70(13):1895
- `turing1952` — Phil Trans R Soc B 237(641):37
- `diffiehellman1976` — IEEE Trans Info Theory 22(6):644
- `feynman1982` — Int J Theor Phys 21(6-7):467
- `freedman1998` — PNAS 95(1):98
- `kitaev2003` — Ann Phys 303(1):2
- `witten1989` — Commun Math Phys 121(3):351
- `frisch1986` — PRL 56(14):1505
- `shor1994` — FOCS 1994

**Medium priority:** `turing1936`, `rsa1977`, `deutschjozsa1992`, `langton1990`, `merton1961`, `bardeen1948`, `mccullochpitts1943`, `schumann1952`

**Low/no DOI:** `joy2000` (Wired magazine), `casper2023`, `durmus2025`, `sharma2024`, `foreignpolicy2012`

### G6. HTML Citation Rendering Architecture

Pandoc produces `<span class="citation" data-cites="key1 key2"></span>` — empty spans with the .bib keys in the attribute. The fix operates in `preprocess.py --fix-html` (post-pandoc HTML processing).

**Approach (Option B — expand in preprocess.py):**
1. Parse `bibliography.bib` into a Python dict (regex parser — `bibtexparser` not installed, not worth adding a dependency for 64 entries)
2. Find all `<span class="citation" data-cites="..."></span>` in HTML
3. For each span, look up keys (space-separated), format as short Chicago note: `Author, <em>Title</em> (Year)`
4. Fill the span with formatted citation text
5. Find the empty Sources chapter (`#app:sources`), inject a generated full bibliography grouped by type

This runs in the existing `fix_html_toc()` function alongside all other HTML post-processing. No new pipeline step needed. No new dependencies.

**Why not Option A (pandoc --citeproc):** Requires .csl file, converting all `\footcite` to `[@key]` syntax in the pre-pandoc step, and changes the pandoc command line in the Makefile. More moving parts, less control over formatting.

**Why not Option C (parse .bbl):** Couples HTML build to LaTeX build state. Fragile.

---

## Phased Implementation

### Phase 1: Fix .bib Data (~15 min Generator)
1. Add `sharma2005` (Bruce confirms reference first)
2. Add `bouwmeester1997`: Bouwmeester et al., "Experimental quantum teleportation," Nature 390:575-579, 1997
3. Add `vaswani2017`: Vaswani et al., "Attention Is All You Need," NeurIPS 2017, arXiv:1706.03762
4. Fix `\footcite{kitaev2003, nayak2008}` → `\footcites{kitaev2003}{nayak2008}` in the 2 spine/ files in the build path
5. Add DOIs to the 9 high-priority articles (G5)

**Acceptance:**
- `grep -roh '\\footcite{[^}]*,[^}]*}' manuscript/spine/ manuscript/appendix/` returns no results
- All cited keys resolve to .bib entries
- `bibliography.bib` has 63–64 entries (61 existing + 2 required new: `bouwmeester1997`, `vaswani2017` + 1 pending Bruce confirmation: `sharma2005`)

### Phase 2: Normalize Inline References (~15 min Generator)
1. Convert the 10 hardcoded timeline/spine footnotes to `\footcite` (G4 items 1-10)
2. Leave 3 URL-only references as inline footnotes (G4 items 13-15)
3. Only touch files in the build path (spine/, appendix/, 00-front/)

**Acceptance:**
- `make dev` builds without biber "undefined citation" warnings
- Timeline footnotes that cite papers in .bib use `\footcite{key}`
- No information lost (DOIs/contextual notes preserved in .bib entries)

### Phase 3: HTML Citation Rendering (~60 min Generator)

This is the largest phase. Break into sub-steps:

**3a. BibTeX parser** (~15 min)
- Add function `parse_bib(path)` to preprocess.py
- Returns dict: `{key: {type, author, title, year, journal, doi, url, ...}}`
- Regex-based: `@type{key,` blocks, `field = {value}` or `field = "value"` pairs
- Handle multiline values (braces nesting)
- Test: parse all 64 entries, print count

**3b. Citation formatter** (~10 min)
- `format_short_cite(entry)` → `Author, <em>Title</em> (Year)` with DOI link if available
- `format_full_entry(entry)` → full Chicago-style bibliography entry with all fields
- Handle multiple authors (truncate to "First et al." for short form)

**3c. Fill empty citation spans** (~15 min)
- In `fix_html_toc()`, after existing processing:
- Find all `<span class="citation" data-cites="..."></span>`
- Split `data-cites` on spaces → list of keys
- Look up each key, format short cite, join with "; "
- Replace empty span content with formatted text
- Log count of filled vs unfilled citations

**3d. Generate Sources bibliography** (~20 min)
- Find `<details>` containing `id="app:sources"`
- Generate HTML bibliography from all .bib entries (not just cited ones)
- Group by type: Books, Journal Articles, Conference Proceedings, Preprints, Online Resources, Legal/Archival, Technical Reports
- Each entry: Author. *Title*. Journal/Publisher, Year. DOI/URL link.
- Inject after `</summary>` of the Sources chapter

**Acceptance:**
- `make html` succeeds
- `grep -c 'data-cites="[^"]*"></span>' docs/downloads/Relinquishment.html` returns 0 (no empty citations)
- Sources chapter contains 64+ formatted entries with clickable DOI/URL links
- Visual spot-check: footnotes show real text on phone

### Phase 4: Verification (~10 min Auditor)
1. Compare PDF bibliography entry count against HTML Sources entry count
2. Click-test 5 random DOI links
3. Spot-check 5 random footnotes in HTML
4. `make html` clean (no warnings)
5. Verify uncited entries (helliwell1983, parrot2002, schumann1952, mccullochpitts1943) appear in Sources

---

## Resource Discipline
- No new pip packages. Regex parser only.
- No network access needed during build.
- bibliography.bib is ~8KB — fits in memory trivially.
- Phase 3 adds ~150-200 lines to preprocess.py.

## Risk Notes
- Phase 3 is the largest single change to preprocess.py since the Z-restructure. Build and visually verify before committing.
- The regex BibTeX parser only needs to handle the 64 entries in this specific .bib file. It does not need to be a general-purpose parser.
- Multi-key citations (`data-cites="kitaev2003 nayak2008"`) produce compound footnotes: "Kitaev, *Fault-tolerant quantum computation* (2003); Nayak et al., *Non-Abelian anyons* (2008)."

## Decision Required from Bruce
1. **Before Phase 1:** Confirm `sharma2005` reference (magnetospheric complexity paper).
2. **Before Phase 3:** Option B (expand in preprocess.py) is the recommended default. No action needed unless Bruce prefers an alternative.
