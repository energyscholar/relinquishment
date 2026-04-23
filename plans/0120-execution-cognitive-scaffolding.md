# Plan 0120: Execution Plan — Cognitive Scaffolding (Plans 0117–0119)

**Status:** ANNEALED
**Implements:** Plans 0117 (physics), 0118 (hover tool), 0119 (non-physics)
**Sessions:** 6 generator handoffs via copy-paste
**Order:** Content first → Infrastructure → Markup last

---

## Architecture

**Content (Sessions 1–4):** All prose changes. Plain LaTeX. No \hovertip markers. Stabilize text.
**Infrastructure (Session 5):** Build hover mechanism. YAML + generate script + preprocess.py + CSS. No content.
**Markup (Session 6):** Install \hovertip{term} markers on stable text. One argument, definitions in YAML.

Content is fully stable before infrastructure or markup touches it.

---

## Session Map

| # | Layer | Scope | Files touched |
|---|-------|-------|---------------|
| 1 | Content | Rewrite "White Hot Secret" — concept ladder | summary.tex |
| 2 | Content | Major scaffolds (Spider-Man, non-bio life, room-temp) | summary.tex, possibly p3 chapters |
| 3 | Content | Light touches + "true under all three" markers | summary.tex |
| 4 | Content | p1 seeds | hook.tex |
| 5 | Infra | Build hover mechanism (YAML, generator, preprocess, CSS) | build/ files, Makefile |
| 6 | Markup | Install \hovertip{term} markers on stable text | summary.tex, hook.tex |

---

## Generator Prompts

### Session 1: Rewrite "White Hot Secret"

```
You are the Generator. Read Plan 0117 at ~/software/relinquishment/plans/0117-flat-cognitive-ladder.md

Execute Phase 2: Rewrite summary.tex "The White Hot Secret" section.

BEFORE WRITING: Read summary.tex lines 33-60. Read the Concept Ladder table in the plan (the "Tier 1" table). Each numbered step = one or two sentences in the rewrite.

p3 check: Grep manuscript/track-1-confession/ for "teleportation" and "Bennett". If quantum teleportation lacks a p3 paragraph with citation, add one in pos10-the-braid.tex or pos13-genesis.tex before proceeding.

Rewrite summary.tex from the line "What the sequence points to:" through the line ending "the Flat can support not just life but intelligent life." Follow the proposed structure in the plan exactly:

0. New opening: lead with the undebatable, not the life claim
1-7. Concept ladder steps, in order
8. Expert confirmation ("every claim above is published, peer-reviewed")
9. A/B/C at dividing line — no "barren." A = "fiction but potential is not"
10-11. Life claim AFTER A/B/C

Write plain prose. No \hovertip markup — that comes later.

ACs: Does not lead with life claim. Ladder in order. Teleportation has classical backchannel qualifier. Kauffman: "can form" not "do form". A/B/C: no "barren." Expert confirmation BEFORE A/B/C. Life claim AFTER. ≤12th grade. 370-690 words. No challengeable physics claims. make html succeeds.

Commit: "Plan 0117 phase 2: Flat concept ladder in p2"
```

### Session 2: Major Scaffolds

```
You are the Generator. Read Plan 0119 at ~/software/relinquishment/plans/0119-cognitive-scaffolding-non-physics.md

Session 1 is complete (summary.tex "White Hot Secret" rewritten). LINE NUMBERS HAVE SHIFTED. Locate insertion points by searching for quoted text and section headings, not line numbers.

Execute Phase 2a: Three major scaffolds in summary.tex.

p3 checks before writing:
- B1: Grep pos10-the-braid.tex for "topological protection" and "room temperature". If missing, add 1 paragraph.
- B3: Grep pos13-genesis.tex for "substrate" and "substrate-independent". If missing, add 1 paragraph.
- B6: Grep manuscript/ for "Spider-Man" or "can't use.*can't keep". If missing in p3, add it to the appropriate chapter.

Then install in summary.tex:

B6 (MOST IMPORTANT): Near the sentence "This act — voluntarily giving up the most powerful technology ever created...is called relinquishment." Insert the logic chain: can't use it (becomes tyrant) → can't keep it (secrets leak) → can't bear the responsibility (Spider-Man: "With great power comes great responsibility" — what if nobody is up to being Spider-Man?) → relinquishment is not sacrifice, it's the only sane option. 3-4 sentences.

B3: Near "origin of life in a new medium" in "The Breakthrough" section. Insert 1-2 sentences: life is self-sustaining organization, not specific chemistry. The substrate doesn't matter.

B1: Near "built one that worked at room temperature" in "The Breakthrough" section. Insert 1 sentence connecting to topological protection the reader already absorbed from the Flat section.

Plain prose. No \hovertip markup.

ACs: B6 has can't-use/can't-keep/can't-bear chain + Spider-Man. B3 has substrate-independence. B1 connects to topological order. All ≤12th grade. make html succeeds.

Commit: "Plan 0119 phase 2a: cognitive scaffolds (relinquishment, non-bio life, room-temp)"
```

### Session 3: Light Touches + "True Under All Three"

```
You are the Generator. Read Plan 0119 at ~/software/relinquishment/plans/0119-cognitive-scaffolding-non-physics.md

Sessions 1-2 are complete. LINE NUMBERS HAVE SHIFTED. Use section headings and surrounding text as anchors.

Execute Phase 2b: Light touches in summary.tex.

- B5: In "The Mentor" section, near "Lane never disclosed anything classified" — if the Snowden parallel isn't nearby, add 1 sentence echoing the criminal-penalty gravity.
- B4: In "The Walk-Out" section, near "walked the working technology out" — add 1 sentence: the technology is knowledge, not hardware.
- B2: In "The Breakthrough" section, near "grown, not built" — add a connecting clause linking to self-organization if not already clear.
- B8: Add 2 "true under all three" markers (1 already exists in the Flat section = 3 total):
  1. After the QC/encryption explanation (end of "The Secret Lab" section)
  2. In "The Mentor" section (after guided deduction explanation)
  Vary phrasing. Light touch. 1 sentence each.

Plain prose. No \hovertip markup.

ACs: All 4 light touches installed. 2 new "true under all three" markers. ≤12th grade. make html succeeds.

Commit: "Plan 0119 phase 2b: light scaffolds and true-under-all-three markers"
```

### Session 4: All p1 Seeds

```
You are the Generator. Read Plan 0117 at ~/software/relinquishment/plans/0117-flat-cognitive-ladder.md

All p2 work is complete. Execute Phase 3 (p1 seed) in hook.tex.

Expand the Flat reference near "It lives in flat worlds" so the reader's brain tags it as real, physical, with different rules. Not a full explanation (p2's job). Establish: the Flat is a real physical place, it has different rules, it is inside things the reader owns.

≤40 words added. ≤8th grade. No technical vocabulary (no "topological order", "nonlocal", "entanglement", "teleportation", "wormhole"). Preserve narrative momentum — don't feel like a physics lecture.

Plain prose. No \hovertip markup.

ACs: Flat conveyed as real physical environment. Different rules established. ≤40 words added. ≤8th grade. Narrative momentum preserved. make html succeeds.

Commit: "Plan 0117 phase 3: p1 Flat seed"
```

### --- CONTENT STABLE — INFRASTRUCTURE + MARKUP BELOW ---

### Session 5: Build Hover Mechanism

```
You are the Generator. Read Plan 0118 at ~/software/relinquishment/plans/0118-inline-hover-definitions.md

Execute Phase 1: Build the hover mechanism. Do NOT edit manuscript content.

Architecture: \hovertip{term} in .tex (one argument, marker only). Definitions in YAML. Build marries them.

1. Create build/hover-definitions.yaml — copy the full term set from Plan 0118.

2. Create build/generate-hover.py (~30 lines):
   - Read hover-definitions.yaml
   - Write build/hover-generated.tex containing:
     - \usepackage{etoolbox}
     - One \csdef{hover@TERM}{DEFINITION} per YAML entry
     - \newcommand{\hovertip}[1]{\textit{#1}\ifcsdef{hover@#1}{\footnote{\csuse{hover@#1}}\csundef{hover@#1}}{}}
   - The \csundef trick removes the definition after first use — automatic first-occurrence-only footnotes.

3. Add \input{build/hover-generated} to build/preamble.tex (after existing \newcommand definitions).

4. Add "python3 build/generate-hover.py" to Makefile: in dev: target before the latexmk line, and in dms: target before its latexmk line.

5. Add Fix 8 to build/preprocess.py patch() function (after Fix 7, before dst.write_text):
   - Load build/hover-definitions.yaml
   - Track first occurrences per file (set)
   - For each \hovertip{term}: look up in YAML
     - First occurrence: replace with <span class="hover-term" title="definition">term</span>
     - Subsequent: replace with <em>term</em>
     - Not in YAML: replace with <em>term</em>, print warning
   - Use brace-counting to extract the single argument

6. Add .hover-term CSS to collapse_css in collapse_chapters():
   .hover-term { font-style: italic; border-bottom: 1px dotted #888; cursor: help; }
   .hover-term:hover { border-bottom-color: #2471a3; }
   Dark mode: border-bottom-color: #666 / hover: #5dade2

7. TEST: Add \hovertip{encryption} to ONE line in summary.tex "The Lock on Every Door" section. Run make dev. Verify:
   - PDF: "encryption" appears italic with a footnote containing the YAML definition
   - HTML: "encryption" has dotted underline, hover shows tooltip
   Remove the test marker. Commit infrastructure only — no \hovertip markers in .tex files.

Commit: "Plan 0118 phase 1: hover mechanism (YAML + generate + preprocess + CSS)"
Report: confirm make dev succeeds, confirm PDF footnote + HTML tooltip both work.
```

### Session 6: Install Hover Markers on Stable Content

```
You are the Generator. Read Plan 0118 at ~/software/relinquishment/plans/0118-inline-hover-definitions.md

Session 5 is complete. The hover mechanism works. All content is stable.

Execute Phase 2: Install \hovertip{term} markers. Do NOT change any prose. Only wrap existing terms.

summary.tex — first occurrence only per term:
- two-dimensional electron gas
- topological order
- entanglement (or "entangled")
- quantum teleportation
- nonlocal
- autocatalytic
- classical backchannel
- magnetosphere
- guided deduction
- topological protection (if present)
- relinquishment (first defining occurrence)

hook.tex — ≤3 terms:
- flat worlds
- Special Air Service
- grew (near "grew a working quantum computer")

Rules:
- First occurrence only per term per file
- Do NOT change surrounding text
- Do NOT add or remove any words
- Only wrap: "topological order" → \hovertip{topological order}
- If a term doesn't appear in the text, skip it (don't force it in)

Verify: make dev succeeds. Open HTML — hover over 3 terms, confirm tooltips. Check PDF — confirm footnotes appear at first occurrence only.

Commit: "Plan 0118 phase 2: hover markers on stable content"
```

---

## Post-Execution

After all 6 sessions: `make dev`, Bruce reads p1 and p2 in HTML + PDF, Auditor reviews all ACs.

To update a definition later: edit `build/hover-definitions.yaml` and rebuild. No .tex changes needed.
To add a new hover term: add to YAML + add one `\hovertip{term}` marker in .tex.
