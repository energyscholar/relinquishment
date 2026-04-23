# Plan 0083: Dossier Interlude — Five Eyes + Hanley

**Status:** APPROVED
**Auditor:** Argus
**Purpose:** Insert paired dossier documents as an interlude between Three Possibilities and Part II

---

## Context

Two mock intelligence dossiers exist in `aurasys-memory/research/`:
- `five-eyes-profile-approximation.md` — Bruce's reconstructed Five Eyes recruitment file (2003). ~269 lines. Framed as "the operational target."
- `hanley-dossier-approximation.md` — Healer's profile, assembled from Clancy's Rainbow Six character + Bruce's direct observation + [REDACTED]. ~121 lines. Framed as "the operational handler."

These form a paired interlude: target and handler. Together they answer the question the reader has been asking since Chapter One: who are these people and why did they find each other?

## Placement — Two Branches

The dossier interlude goes in BOTH branches. Same tex file, different insertion points in `main.tex`. Same logic: reader has A/B/C framework (Three Possibilities) before seeing the dossiers.

**Branch `maugham-revision`** (likely final structure):
- **After:** INTERLUDE: THREE POSSIBILITIES (`three-possibilities-interlude`)
- **Before:** Part II: THE RECKONING (pos18 The Walk-Out)
- Rationale: Reader has narrative investment from Part I. Three Possibilities interlude gives them A/B/C. Dossiers are first "evidence" they evaluate. Marks transition from Gen's "Story" to "Investigation."

**Branch `main`** (original structure, preserved for now):
- **After:** pos01 (`pos01-three-possibilities`) — Three Possibilities is first chapter here, not an interlude
- **Before:** pos02 (`pos02-alpha-farm`)
- Rationale: Same logic — reader has A/B/C framework from pos01, dossiers follow immediately.

## Phase 0: Stage Source Files

**BLOCKING:** Generator cannot read `~/software/aurasys-memory/` (Triad rule). Source files must be copied into relinquishment before Generator runs.

**Tasks:**
1. Copy `~/software/aurasys-memory/research/five-eyes-profile-approximation.md` → `~/software/relinquishment/manuscript/interlude/source-five-eyes.md`
2. Copy `~/software/aurasys-memory/research/hanley-dossier-approximation.md` → `~/software/relinquishment/manuscript/interlude/source-hanley.md`
3. These are staging copies — not tracked in git long-term. Generator reads from these.

**Acceptance:** Both files present in `manuscript/interlude/`.

## Phase 1: LaTeX Integration

**Source files:** `manuscript/interlude/source-five-eyes.md` and `manuscript/interlude/source-hanley.md` (staged in Phase 0)

**Tasks:**
1. Create `manuscript/interlude/dossier-interlude.tex`
2. Match interlude styling from `manuscript/interlude/three-possibilities-interlude.tex`:
   - Use `\chapter*{The Files}` (or similar — see framing note below)
   - `\addcontentsline{toc}{chapter}{The Files}`
   - `\settrack{trackbridge}`
3. Structure the interlude in two labeled halves:
   - **Part A: "The Target"** — Five Eyes profile (from `source-five-eyes.md`)
   - **Part B: "The Handler"** — Hanley/Healer profile (from `source-hanley.md`)
4. Each half opens with Bruce's intro blurb (the `>` blockquote sections) formatted as `\begin{quote}\small\textit{...}` matching Three Possibilities style
5. Convert markdown formatting to LaTeX:
   - `###` section headers → `\section*{}`
   - `**bold**` → `\textbf{}`
   - Tables → `tabularx` with `p{}` column specs (prevent overflow — some tables have long text in cells)
   - `[REDACTED]` → `\textbf{[REDACTED]}` (or `\textsc{[redacted]}` — Generator's call on what looks best)
   - `---` horizontal rules → `\vspace{1cm}\hrule\vspace{1cm}` or similar
   - `[CLANCY]` / `[OBSERVED]` tags → small caps or bold, visually distinct
   - **ESCAPE SPECIAL CHARACTERS:** Source contains `$143K`, `$800/day`, `$85K/year` (escape `$`), `&` in company names (escape `&`), `~` tildes, `#` symbols. Escape all for LaTeX.
6. Insert `\clearpage` or `\newpage` between Part A and Part B
7. Insert into `main.tex` on BOTH branches (same tex file, different insertion points):
   - **`maugham-revision`:** Find `\include{manuscript/interlude/three-possibilities-interlude}`, add AFTER it, BEFORE `% ===== PART II`:
     ```
     % ===== INTERLUDE: THE FILES =====
     % Plan 0083: Paired dossiers — target (Bruce) and handler (Healer/Hanley)
     \include{manuscript/interlude/dossier-interlude}
     ```
   - **`main`:** Find `\include{manuscript/bridge/pos01-three-possibilities}`, add AFTER it, BEFORE `\include{manuscript/track-2-testament/pos02-alpha-farm}`:
     ```
     % ===== INTERLUDE: THE FILES =====
     % Plan 0083: Paired dossiers — target (Bruce) and handler (Healer/Hanley)
     \include{manuscript/interlude/dossier-interlude}
     ```
   (Do NOT reference by line number — find by content match.)
8. Compile with `make book` on BOTH branches, verify:
   - Interlude appears in correct position in each branch's PDF
   - TOC entry present
   - Tables render correctly, no column overflow
   - Page count impact noted (estimate: ~12-15 pages)
9. Clean up: delete `source-five-eyes.md` and `source-hanley.md` from `manuscript/interlude/` after tex file is complete

**Acceptance criteria:**
- `make book` succeeds with zero errors
- Interlude appears in correct position in PDF
- TOC shows "The Files" (or chosen title) between "The Three Possibilities" and Part II
- All [REDACTED] blocks, [CLANCY]/[OBSERVED] tags, and tables render cleanly
- Bruce's intro blurbs are visually distinct from dossier body text

## Phase 2: Cross-References (light touch)

**Tasks:**
1. Check pos02 (Alpha Farm) for natural points to add a forward reference — e.g., a footnote or marginal note hinting the reader will learn more about who Bruce is. Do NOT add if it feels forced.
2. OPSEC check: verify no Correction #11 violations in the final LaTeX. No ranch details beyond Clancy's published fiction. No real location info.
3. Verify the interlude works standalone — a reader who skips it should lose nothing essential; a reader who reads it should gain depth.

**Acceptance criteria:**
- No chapter depends on the interlude for comprehension
- Any cross-references feel natural
- OPSEC clean

---

## Framing Notes for Generator

- The interlude title could be "The Files", "The Dossiers", or "Two Files" — pick what reads best in the TOC between "The Three Possibilities" and Part II chapter titles
- The "Target" / "Handler" labels should appear as section titles or epigraphs — make it clear these are two sides of a recruitment operation
- The humor is structural: Bruce wrote his own spy file, Tom Clancy wrote the handler's file, and the [REDACTED] gaps in the Hanley document let the reader see the shape of what's classified. "Unless [REDACTED]" is the punchline. Don't undercut it with explanation.
- Both documents work under all three possibilities (A/B/C). Under A, Bruce is a talented fabricator who assembled public sources into convincing dossiers. Under B, the kernel is real but details are embellished. Under C, these are approximately what the actual files contained. The interlude does not tell the reader which to believe.

## Handoff

**Launch Generator from relinquishment directory** (not aurasys-memory — Generator must not load Auditor context):
```
cd ~/software/relinquishment && claude
```

Then paste the handoff prompt below.
