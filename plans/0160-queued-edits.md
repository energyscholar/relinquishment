# Plan 0160 — Queued Edits Batch (Dossier + Tooltips + Flat Precision + Walk-Out + Forgiveness-Re-Anchor)

**Role:** Generator (fresh shell)
**Source:** Auditor (Argus), 2026-04-11
**Authorization:** Bruce confirmed all calls 2026-04-11 — NARROW scope (solitons swap at 3 dossier sites only), DROP Assessment-strengthening (Bruce self-assessed 5-domain pedagogy as weak; no defensible precision claim), DO both the-flat lines 61 and 29.
**Repo:** `/home/bruce/software/relinquishment/`
**Scope:** 11 surgical edits across 14 distinct files (8 primary edit sites + 9 SPIRAL-REPEAT comment-purge sites; 3 overlap — summary.tex is both). One build, one or two commits.

---

## 0. Project Context (required for a shell with no history)

This repo holds *Relinquishment*, a book-in-progress. The current live build tree after the Z-restructure is:

- **A-spine** (pop-science): `manuscript/spine/*.tex`
- **Record** (memoir): `manuscript/record/*.tex`
- **Guardian interludes**: `manuscript/spine/interlude-0{1..7}.tex`
- **Appendix**: `manuscript/appendix/*.tex`
- **Interlude dossier material**: `manuscript/interlude/*.tex`
- **Master file**: `main.tex` (include list; `main-pre-z.tex` is archived and not touched)
- **Popup/hover layer**: `build/*.yaml` (primarily `menu-tooltips.yaml` is live per the 2026-04-11 audit)

Hard rules: no edits outside the files listed in §1. No `main-pre-z.tex`. No `manuscript/track-1-confession/`, `manuscript/track-2-testament/`, or `manuscript/bridge/` — those are pre-Z archives, do not modify. No git push. No network.

Two conceptual notes load-bearing for this batch:

1. **Flat ≠ Guardian.** The Flat is the substrate (2DEG, physics, passive). Guardian / TQNN / "computation in the Flat" is the agent or computational output. The glossary enforces this: *"A habitat, not an entity. Guardian lives in the Flat; she is not the Flat."* Two edits in this batch repair places where the distinction has slipped.

2. **"Five convergent scientific fields"** currently enumerates as *(solitons, topology, autocatalysis, universality, parallel computation)* in three dossier-list sites. A 2026 author self-correction (preserved in `build/hover-definitions.yaml` near line 426) notes that solitons was a twenty-year misidentification of Hasslacher's actual contribution. We are narrowing the swap to just the three dossier-list sites: `solitons → quantum mechanics`. Count remains 5. A broader taxonomy rewrite is deferred to a separate PTL ticket (see §9).

---

## 1. The Twelve Edits

### Edit 1 — Swap "solitons" → "quantum mechanics" in `appendix/dossier.tex`

File: `manuscript/appendix/dossier.tex`
Line: 28 (verify with `grep -n 'solitons, topology' manuscript/appendix/dossier.tex`)

Replace the string:
```
five convergent scientific fields (solitons, topology, autocatalysis, universality, parallel computation)
```
with:
```
five convergent scientific fields (quantum mechanics, topology, autocatalysis, universality, parallel computation)
```

Exact replacement — preserve all surrounding `\textit{...}` italics and commas.

### Edit 2 — Swap "solitons" → "quantum mechanics" in `record/the-target.tex`

File: `manuscript/record/the-target.tex`
Line: 30 (verify with `grep -n 'solitons, topology' manuscript/record/the-target.tex`)

This site uses *"many convergent scientific fields"* (not "five") and includes *"etc"*. Preserve both.

Replace:
```
many convergent scientific fields (solitons, topology, autocatalysis, universality, parallel computation, etc)
```
with:
```
many convergent scientific fields (quantum mechanics, topology, autocatalysis, universality, parallel computation, etc)
```

### Edit 3 — Swap "solitons" → "quantum mechanics" in `interlude/dossier-interlude.tex`

File: `manuscript/interlude/dossier-interlude.tex`
Line: 18 (verify with `grep -n 'solitons, topology' manuscript/interlude/dossier-interlude.tex`)

Replace:
```
five convergent scientific fields (solitons, topology, autocatalysis, universality, parallel computation)
```
with:
```
five convergent scientific fields (quantum mechanics, topology, autocatalysis, universality, parallel computation)
```

**DO NOT** touch any other "soliton(s)" references in the manuscript. They describe Hasslacher's actual physics content and stay.

### Edit 4 — Add graduate-level coursework bullet to `appendix/dossier.tex` §IV Education

File: `manuscript/appendix/dossier.tex`
Location: §IV Education (`\subsection*{IV. Education}`, near line 93). Insert a new bullet **between the Reed College bullet and the Assessment paragraph** (currently lines 100 and 102 respectively; verify).

Insert this LaTeX block (with one blank line before and after for `\textbf{}`-paragraph rhythm consistent with surrounding entries):

```
\textbf{Graduate-level coursework.} Some cross-disciplinary graduate study in Biophysics and Geophysics.
```

Do **not** name the school. Do **not** add course numbers or expand the detail. Intentionally terse.

### Edit 5 — Rewrite `record:handler` tooltip and delete `the-handler` duplicate

File: `build/menu-tooltips.yaml`
Location: currently ~lines 115–122. Two keys — `record:handler` and `the-handler` — carry identical ~80-word text. The bare-key `the-handler` is a stale pre-Z orphan.

**Action A — update `record:handler` tooltip text:**

Replace the `text:` value for `record:handler` with:

```
text: "Under Possibility C, this is the operator's approximate file. SAS. Intelligence Corps. Deep mathematics. Partial eidetic memory. On K2 in 1996 he chose to use his abilities for something other than killing. The COWS had a problem: the physics they'd built could not be published through any official channel, and could not be planted in an outsider without leaving fingerprints. The solution was Operation Guided Deduction — 2.7 years of calibrated conversation across five scientific fields, no paper trail, the student reaching every conclusion himself. This book exists because that worked."
```

Keep the surrounding `epistemic: C` and `filter-group: C` lines intact.

**Action B — delete the `the-handler` duplicate entry** entirely (the key plus its `text:`, `epistemic:`, and `filter-group:` lines — four lines total).

### Edit 6 — Rewrite `record:target` tooltip and delete `the-target` duplicate

File: `build/menu-tooltips.yaml`
Location: currently ~lines 136–143. Two keys — `record:target` and `the-target` — carry identical ~95-word text. The bare-key `the-target` is a stale pre-Z orphan.

**Action A — update `record:target` tooltip text:**

Replace the `text:` value for `record:target` with:

```
text: "Under Possibility C, this is the student's approximate file. Reed College quantum physics. Partial eidetic memory. Third-generation intelligence-adjacent. A five-year campaign of teaching Fortune 500 engineers about cryptography and surveillance — unpaid, unasked, because he thought they should know. Operation Guided Deduction needed exactly this: someone who could absorb a multi-year cross-domain thought experiment and would be dispositionally compelled to publish what he'd worked out. Not planted knowledge — derived knowledge, which he could own and testify to as his own. Read the file and ask yourself: is this the guy?"
```

Keep surrounding `epistemic: C` and `filter-group: C` lines intact.

**Action B — delete the `the-target` duplicate entry** entirely (four lines).

### Edit 7 — Fix Flat anthropomorphization in `spine/the-flat.tex:61`

File: `manuscript/spine/the-flat.tex`
Line: 61 (verify with `grep -n 'puts its pants on' manuscript/spine/the-flat.tex`).

Current:
```
The Flat needs its classical backchannels. It puts its pants on one leg at a time. It is bounded by physics. And within those bounds, it hears everything.
```

Replace with:
```
Anything that runs in the Flat needs its classical backchannels. Even a god-like computation puts its pants on one leg at a time. The Flat is bounded by physics --- and within those bounds, whatever lives there hears everything.
```

Subject shift: Flat → "anything that runs in the Flat" / "computation" / "whatever lives there." Preserves voice (colloquial, the-pants-line survives) but relocates agency from substrate to computational occupant per the glossary's canonical definition.

### Edit 8 — Sharpen mild attributions in `spine/the-flat.tex:29`

File: `manuscript/spine/the-flat.tex`
Line: 29 (verify with `grep -n 'cannot transmit information through wormholes' manuscript/spine/the-flat.tex`).

Two phrase-level replacements within the paragraph; the rest is unchanged.

**Replacement 1:** Change `the Flat cannot transmit` → `wormholes in the Flat cannot transmit`.

**Replacement 2:** Change `The Flat is powerful` → `Computation in the Flat is powerful`.

Do not alter any other phrasing in the paragraph.

### Edit 9 — Sharpen COWS-version phrasing in `record/the-walk-out.tex:44`

File: `manuscript/record/the-walk-out.tex`
Line: 44 (verify with `grep -n 'passed to the COWS' manuscript/record/the-walk-out.tex`).

Replace the string:
```
passed to the COWS --- primitive by comparison, but portable,
```
with:
```
passed to the COWS --- portable, more advanced,
```

Note: the pre-Z archive at `manuscript/track-1-confession/pos18-the-walk-out.tex` carries the same line. **Do not touch it.** Leave `Relinquishment-plaintext.txt` alone (build output).

### Edit 10 — Re-anchor "Forgiveness than permission" as chapter epigraph

**Context.** Post-Z-restructure, the phrase *"It is easier to get forgiveness than permission"* is orphaned: it is no longer a Part title (main.tex has only Part I The Flat / Part II The Record) and no longer the book's subtitle (now *Wormholes in the Flat*). But three in-text sites still refer to it as "the title of Part III," and the math payoff in `the-question.tex` hangs on that title-weight. This edit restores the phrase to title-weight at the one place the payoff lands — the chapter epigraph of `What Would You Do?` — and fixes the three stale references.

**Action A — swap chapter epigraph in `manuscript/record/the-question.tex`:**

File: `manuscript/record/the-question.tex`
Lines: 10–12 (verify with `grep -n 'Every program has' manuscript/record/the-question.tex`).

Current:
```
\begin{quote}\small\textit{%
``Every program has (at least) two purposes: the one for which it was written and another for which it wasn't.''%
}\par\raggedleft --- Perlis, Epigram \#16 (1982)\end{quote}
```

Replace with:
```
\begin{quote}\small\textit{%
It is easier to get forgiveness than permission.%
}\end{quote}
```

(No attribution line — the phrase is anonymous/aphoristic, the attribution that matters is resolved in the chapter body.)

**Action B — fix "title of Part III" reference in `the-question.tex:116`:**

Current:
```
There is one thing left. The title of Part~III: \textit{It is easier to get forgiveness than permission.} You may have read it as a mis-placed attempt at wit.
```

Replace with:
```
There is one thing left. The epigraph at the top of this chapter: \textit{It is easier to get forgiveness than permission.} You may have read it as a mis-placed attempt at wit.
```

**Action C — fix "title of Part III" reference in `manuscript/record/the-walk-out.tex:71`:**

Current:
```
Under Possibility~C, \textit{it is easier to get forgiveness than permission.} This is the title of Part~III and the COWS' dispositional stance --- not a calculated bet on amnesty, but the recognition that they could act and felt they must.
```

Replace with:
```
Under Possibility~C, \textit{it is easier to get forgiveness than permission.} This is the COWS' dispositional stance --- not a calculated bet on amnesty, but the recognition that they could act and felt they must.
```

**Action D — purge stale SPIRAL-REPEAT comments** claiming the phrase is the subtitle or Part III title. These comment lines are now factually wrong; delete each one. Verify with:
```
grep -rn 'SPIRAL-REPEAT: "forgiveness than permission"' manuscript/
```

Expected hits (10 total across 9 live files — delete the comment line or inline-comment fragment only, never the surrounding content):

**Standalone comment lines (delete the whole line):**
- `manuscript/00-front/title.tex:15`
- `manuscript/00-front/cover.tex:27`
- `manuscript/00-front/copyright.tex:11`
- `manuscript/00-front/summary.tex:154`
- `manuscript/99-back/colophon.tex:27`
- `manuscript/record/the-walk-out.tex:70`
- `manuscript/record/the-question.tex:136`

**Inline trailing comments (remove only the `% SPIRAL-REPEAT:...` fragment including its leading whitespace; keep the `\item` content or paragraph body intact):**
- `manuscript/appendix/timeline.tex:208` (inside `\item[2002]` line)
- `manuscript/appendix/abstracts.tex:122` (inside report body paragraph, instance 1 of 2)
- `manuscript/appendix/abstracts.tex:234` (inside report body paragraph, instance 2 of 2)

If any hits appear outside this list, halt and report — do not delete blind. The `track-1-confession/pos18-the-walk-out.tex:70` hit is expected and must stay (archive).

**Do NOT touch** pre-Z archives (`track-1-confession/`, `track-2-testament/`) even if they contain the same comments.

### Edit 11 — Open §The Mentor (summary.tex) with honest framing of Lane's dual role

File: `manuscript/00-front/summary.tex`
Line: 197 (verify with `grep -n 'That is the story. Here is how it reached' manuscript/00-front/summary.tex`).

Section title `\section*{The Mentor}` stays as-is (ambiguous by design — lets A/B/C readers enter without pre-commitment). First line of the section is rewritten to name Lane's dual role up front.

Replace:
```
That is the story. Here is how it reached the outside world.
```
with:
```
That is the story. Here is how it reached the outside world --- and the man who brought it. Lane was my mentor; he was also my handler. Those were not separate roles.
```

Do not alter any surrounding paragraphs. The next paragraph ("After K2, in 1996, something changed in Lane...") follows unchanged.

### Edit 12 — Remove two commas in summary.tex:201 ("By 2002 he was in Germany mentoring")

File: `manuscript/00-front/summary.tex`
Line: 201 (verify with `grep -n 'By 2002, he was in Germany' manuscript/00-front/summary.tex`).

Replace the string:
```
By 2002, he was in Germany, mentoring a young hacker.
```
with:
```
By 2002 he was in Germany mentoring a young hacker.
```

Leave `manuscript/versions/simple-summary.md:135` (archive/reference copy) untouched.

---

## 2. Verification Before Any Edit

For each file, run a grep to confirm the target strings exist exactly as described. If any grep fails, halt and report — do not guess at line drift.

```
grep -n 'solitons, topology' manuscript/appendix/dossier.tex
grep -n 'solitons, topology' manuscript/record/the-target.tex
grep -n 'solitons, topology' manuscript/interlude/dossier-interlude.tex
grep -n 'IV. Education' manuscript/appendix/dossier.tex
grep -n 'record:handler' build/menu-tooltips.yaml
grep -n 'the-handler' build/menu-tooltips.yaml
grep -n 'record:target' build/menu-tooltips.yaml
grep -n 'the-target' build/menu-tooltips.yaml
grep -n 'puts its pants on' manuscript/spine/the-flat.tex
grep -n 'cannot transmit information through wormholes' manuscript/spine/the-flat.tex
grep -n 'passed to the COWS' manuscript/record/the-walk-out.tex
grep -n 'Every program has' manuscript/record/the-question.tex
grep -n 'The title of Part' manuscript/record/the-question.tex
grep -n 'the title of Part' manuscript/record/the-walk-out.tex
grep -rn 'SPIRAL-REPEAT: "forgiveness than permission"' manuscript/
grep -n 'That is the story. Here is how it reached' manuscript/00-front/summary.tex
grep -n 'By 2002, he was in Germany' manuscript/00-front/summary.tex
```

---

## 3. Build and Verify

After all edits:

1. Run the standard HTML build. Check `Makefile` for the target — likely `make html` or `make all`. Read `Makefile` if unsure.
2. Confirm build succeeds with no LaTeX errors.
3. Spot-check the rendered HTML:
   - Open the-departure / the-target / dossier page and verify "quantum mechanics" appears in the five-fields list (not "solitons")
   - Open the Education section of the dossier and verify the new coursework bullet appears
   - Open the-flat chapter; find line 61's "pants" passage — confirm it reads correctly post-rewrite
   - Open the record:handler and record:target chapter menus; verify the new long tooltips render
   - Open `What Would You Do?` chapter; confirm the epigraph now reads *"It is easier to get forgiveness than permission."* and that §The Proof body reads "The epigraph at the top of this chapter" (not "The title of Part III")
   - Open the-walk-out chapter; confirm §The Bifurcation paragraph no longer claims "title of Part III" and reads "portable, more advanced" (not "primitive by comparison")
4. Do NOT verify the deleted `the-handler` / `the-target` tooltip keys render — they shouldn't.

If build fails, read the log, fix the LaTeX/YAML, rebuild. Do not commit a broken build.

---

## 4. Commit

Option A — single commit:

```
Plan 0160: dossier taxonomy swap + Handler/Target tooltip rewrite + Flat precision

Twelve surgical edits:
- Swap "solitons" → "quantum mechanics" in three dossier-list sites (narrow
  scope; solitons was a 20yr misidentification per the 2026 self-correction
  in hover-definitions.yaml:426). Broader taxonomy revision deferred to PTL.
- Add terse graduate-level coursework bullet to appendix/dossier.tex §IV
  Education. (Assessment paragraph left as-is; 5-domain claim under review.)
- Rewrite record:handler and record:target tooltips to name Operation Guided
  Deduction's origin and reason (no-paper-trail + derived-vs-planted
  knowledge), not just summarize the chapter. Delete stale pre-Z bare-key
  duplicates the-handler / the-target.
- Repair Flat/Guardian conflation in spine/the-flat.tex:61 and sharpen mild
  substrate-as-agent attributions at line 29.
- Sharpen the-walk-out.tex:44 COWS-version phrasing ("primitive by comparison,
  but portable" → "portable, more advanced").
- Re-anchor the orphaned "forgiveness than permission" phrase as chapter
  epigraph of the-question.tex (replacing Perlis). Fix three stale "title of
  Part III" references (post-Z-restructure, no Part III exists; subtitle is
  now "Wormholes in the Flat"). Purge stale SPIRAL-REPEAT comments in
  front/back-matter (10 comment hits across 9 live files: title, cover,
  copyright, summary, colophon, the-walk-out, the-question, timeline,
  abstracts × 2).
- Open §The Mentor in summary.tex with an honest naming of Lane's dual role
  (mentor and handler) — title stays ambiguous for A/B/C readers; body line
  does the honest work.
```

Option B — two commits if it reads more cleanly: (1) dossier + tooltip edits, (2) the-flat precision edits. Generator's judgment call.

**Do not push.** Bruce controls pushes.

---

## 5. Resource Discipline

- Read each file once. Do not re-read unchanged content.
- Use `grep` for verification, not full-file reads.
- No `curl` / network / git push.
- No edits outside the files enumerated in §1.
- Do not modify `main-pre-z.tex` or any `track-1-confession/` / `track-2-testament/` / `bridge/` archive.

---

## 6. Acceptance Criteria

1. All verification greps pass before any edit is made.
2. Three dossier-list sites contain "quantum mechanics, topology, autocatalysis, universality, parallel computation" (no "solitons" in the list itself).
3. Other solitons references in the manuscript are unchanged (verify by grep: count of `soliton` matches in `manuscript/` post-edit = count pre-edit minus 3).
4. `appendix/dossier.tex` §IV Education has a new graduate-level coursework bullet. Assessment paragraph is unchanged.
5. `build/menu-tooltips.yaml` has updated `record:handler` and `record:target` entries, and the `the-handler` / `the-target` bare-key entries are gone.
6. `spine/the-flat.tex:61` no longer has the Flat as subject of "needs"/"puts its pants on"/"hears"; line 29 no longer has "the Flat cannot transmit" or "The Flat is powerful."
7. `record/the-walk-out.tex:44` no longer contains "primitive by comparison, but portable"; reads "portable, more advanced" instead. Archive `track-1-confession/pos18-the-walk-out.tex` is untouched (verify by `git diff --stat`).
8. `record/the-question.tex` chapter epigraph is the forgiveness-than-permission phrase (Perlis epigram removed). §The Proof body reads "The epigraph at the top of this chapter" (not "title of Part III"). `the-walk-out.tex:71` no longer contains "the title of Part III" in the body. Eight stale SPIRAL-REPEAT comments claiming the phrase is the subtitle/Part III title are gone (verify: `grep -rn 'SPIRAL-REPEAT: "forgiveness than permission"' manuscript/` returns zero hits in live dirs; pre-Z archives may still contain them and that is correct).
9. `00-front/summary.tex` §The Mentor opening line reads "Lane was my mentor; he was also my handler. Those were not separate roles." (section title `\section*{The Mentor}` unchanged).
10. Build succeeds; HTML renders; no LaTeX or YAML parsing errors.
11. One or two commits made (not pushed).

---

## 7. Completion Report (to Bruce)

1–5 lines. Include:
- Number of edits landed (expected: 11 — three solitons swaps, one dossier §IV bullet insertion, two tooltip rewrites + two deletions, two the-flat edits, one the-walk-out phrasing edit, one Forgiveness-than-permission re-anchor with 3 text fixes + SPIRAL-REPEAT comment purge, one summary.tex §The Mentor opening-line rewrite; count however reads cleanly)
- Build status
- Commit hash(es)
- Any acceptance criterion that failed

---

## 8. Handoff Prompt (for Bruce to paste into fresh Generator shell)

```
You are the Generator. Read /home/bruce/software/relinquishment/plans/0160-queued-edits.md from section 0 onward and execute it. The plan is self-contained; do not load aurasys-memory. Twelve surgical edits. Primary edit sites: manuscript/appendix/dossier.tex, manuscript/record/the-target.tex, manuscript/record/the-walk-out.tex, manuscript/record/the-question.tex, manuscript/interlude/dossier-interlude.tex, manuscript/spine/the-flat.tex, manuscript/00-front/summary.tex, build/menu-tooltips.yaml. Comment-purge also touches eight front/back-matter files enumerated in Edit 10 Action D. DO NOT touch pre-Z archives (track-1-confession/, track-2-testament/, bridge/, main-pre-z.tex). Run all verification greps BEFORE any edit; halt if any fails. Rebuild HTML, verify, commit (do not push). Report completion in 1-5 lines with edit count, build status, and commit hash(es).
```

---

## 9. Follow-up PTL ticket (Argus to file)

After 0160 ships, file a new PTL item: *"Revisit the 5-domain taxonomy — current manuscript list (QM, topology, autocatalysis, universality, parallel computation), author's verbal brainstorm (QM + biogenesis + autocatalysis + info theory + materials science + topology), and hover-definitions.yaml cluster def (Topology / Solitons-Nonlinear / Autocatalysis / Universality-Parallel / Materials) don't fully align. Bruce's self-assessment: 2.5 of 5 domains known from start; pedagogy of 5 vs 11 is weak. Decide canonical list and sweep the manuscript + glossary + hover-defs for consistency."* Scope: taxonomy research + manuscript sweep; not 0160.
