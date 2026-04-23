# Plan 0159 — Compress "The Reread" Section

**Role:** Generator (fresh shell)
**Source:** Auditor (Argus), 2026-04-11
**Authorization:** Bruce directly approved this compression 2026-04-11 after re-reading the section on phone.
**Repo:** `/home/bruce/software/relinquishment/`
**Scope:** One file, one section. Surgical edit.

---

## 0. Context (required for a shell with no history)

The section titled "The Reread" appears in `manuscript/record/the-departure.tex` at lines 45–81 (verify before editing). It currently contains:

- Opening setup (3 short paragraphs)
- "Close Textual Comparison: Joy (2000) vs. My Reconstruction (2022)" — a 10-point numbered list comparing Bill Joy's 2000 Wired essay "Why the Future Doesn't Need Us" to the author's own 2022 reconstruction, each point interpreted under all three Possibilities (A confabulation / B exaggerated kernel / C substantially true)
- A closing paragraph restating A/B/C interpretations of the whole pattern
- A one-line "I leave the reader to determine what this correspondence means."

Total ~1500 words. The problem: the section over-argues, and over-argument reads as the exact shape of apophenia the author is admitting could be happening. Brevity is more credible than thoroughness here. The per-point A/B/C triple-reading is redundant — A/B/C is established globally in the book.

Bruce's instruction verbatim: "yes, perform the chop. We won't miss it." and (earlier) "we say way less about this." Target: ~150–200 words from ~1500.

**Do NOT under any circumstances:** add a "go ask Bill Joy" invitation, a reader-outreach prompt, a contact route, or any deputization of readers toward a named living person. This was explicitly rejected. No links, no bio pointers, no "Joy is alive."

---

## 1. The Compression

### Keep (lines 45–52, verbatim)

```
\section*{The Reread}
\label{record:dep-the-reread}

Under one reading --- the one most people give it --- ``Why the Future Doesn't Need Us'' is a brilliant technologist's warning about the future. Under another reading, it is something else entirely. The second reading occurred to me in 2012. It has not left me since.

\vspace{0.5cm}

What follows is either the most revealing close reading in this book or the most damning exhibit of pattern-matching. I cannot tell you which.
```

### Replace (lines 54–81 — the "Close Textual Comparison" header, all 10 numbered points, and the closing A/B/C summary paragraph) with the block below

**Three hooks, plain prose, no per-bullet A/B/C, no section header.** Write it as a single ~120-word passage. The three hooks, in order:

1. **The exact phrase.** Joy calls the threat "a surprising and terrible empowerment of extreme individuals." Under my reconstruction, that phrase is not speculation — it is a description.
2. **The named circle.** Joy names Wolfram, Hasslacher, Hillis, Kauffman, Gell-Mann as the people who shaped his thinking. I identify the same people as the project team.
3. **The word itself.** "The only realistic alternative I see is relinquishment," Joy writes. I titled this book \textit{Relinquishment}.

Then a single closing sentence acknowledging apophenia without ten paragraphs of it:

> Any of this can be read as pattern-matching. I am telling you what I saw and what I could not unsee.

**Constraints on the prose:**
- ≤200 words total for the replacement block (hooks + closing sentence)
- No "Under Possibility A/B/C" per hook — state the correspondence plainly
- No invitation to third-party verification
- No footnotes, no citations beyond what's already inline
- LaTeX-compatible (use `\textit{}` for titles, `---` for em-dash, straight-single-quotes as `'`, double-quotes as ``` `` '' ```)
- Preserve the `\vspace{0.5cm}` rhythm where natural

### Keep (lines 83+ verbatim)

The `\vspace{1cm}\noindent\rule{0.5\textwidth}{0.5pt}\vspace{0.5cm}` divider and everything after it (the "The Departure" section starts at the current line 85 and continues unchanged).

---

## 2. File not to touch

There is also a pre-Z-restructure copy at `manuscript/track-2-testament/pos07-the-departure.tex`. **Leave it alone.** It is archived, included only from `main-pre-z.tex`, not from the current `main.tex`. Do not edit it.

---

## 3. Verify before editing

1. `grep -n 'The Reread' manuscript/record/the-departure.tex` — confirm line 45 (or current equivalent)
2. `grep -n 'I leave the reader' manuscript/record/the-departure.tex` — confirm the closing line (current 81) of the section to replace
3. Confirm lines 83+ contain the `\vspace{1cm}...\rule` divider and "The Departure" section unchanged

If line numbers differ from expected, work from the content markers (section heading + closing line), not the numbers.

---

## 4. Build and verify

After the edit:

1. Run the Makefile target that builds HTML (check `Makefile` for the correct target — likely `make html` or `make all`). If the build system is unfamiliar, read `Makefile` first.
2. Confirm the compressed section renders (open the built HTML for the-departure, search for "Reread")
3. Confirm no LaTeX errors in the build log
4. Confirm the "The Departure" section immediately after still starts correctly

If build fails, read the error, fix the LaTeX, and rebuild. Do NOT commit a broken build.

---

## 5. Commit

One commit, message format:

```
Plan 0159: compress "The Reread" from 10-point A/B/C comparison to 3-hook passage

~1500 words → ~200 words. Three hooks (phrase match, named circle, the word
"relinquishment") stated plainly without per-bullet A/B/C triple-reading.
Apophenia acknowledged in one closing line.

manuscript/record/the-departure.tex only; archived pre-z copy untouched.
```

Do not push. Bruce controls pushes.

---

## 6. Acceptance Criteria

1. `manuscript/record/the-departure.tex` "The Reread" section is ≤250 words total (opening + hooks + closing)
2. Opening 3 paragraphs preserved verbatim
3. Exactly 3 hooks, in the order specified, stated plainly (no per-bullet A/B/C)
4. One-line apophenia acknowledgment at close (no multi-paragraph triple-reading)
5. No Joy invitation / contact route / reader outreach prompt anywhere
6. `manuscript/track-2-testament/pos07-the-departure.tex` untouched
7. Build succeeds; HTML renders; no LaTeX errors
8. One commit made, not pushed

---

## 7. Completion Report (to Bruce)

1–5 lines. Include: word count before / after, commit hash, confirmation that archived pre-z file was not touched.

---

## 8. Handoff Prompt (for Bruce to paste into fresh Generator shell)

```
You are the Generator. Read /home/bruce/software/relinquishment/plans/0159-reread-compression.md from section 0 onward and execute it. The plan is self-contained; do not load aurasys-memory. Edit only manuscript/record/the-departure.tex — the archived track-2-testament copy stays untouched. Rebuild HTML, verify, commit (do not push). Report completion in 1-5 lines with word count before/after and commit hash.
```
