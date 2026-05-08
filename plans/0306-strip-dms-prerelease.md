# Plan 0306: Strip DMS Artifacts + Pre-Release Notice

**Status:** READY FOR GENERATOR
**Priority:** HIGH — must be done before release (~May 19)
**Source:** Bruce, S68. "Strip off the Dead Man Switch and Early Version wording."

## Context

The book was originally distributed as a DMS (dead man's switch) manuscript. The public `make dev` build guards some DMS content behind `\ifdefined\dmsbuild`, but a thorough sweep of both HTML and PDF output found **6 reader-visible DMS/pre-release items** across 4 files:

### Full Sweep Results (HTML + PDF, verified identical)

| # | File | Content | Action |
|---|------|---------|--------|
| 1 | `copyright.tex:78-82` | "Pre-Release Draft — [timestamp]" + "working copy" notice | REMOVE |
| 2 | `timeline.tex:285` | "DMS letters sent to Schneier, Doctorow, Gilmore" | REWORD |
| 3 | `acknowledgements.tex:24` | "under a deadman's switch arrangement" | REWORD |
| 4 | `verification.tex:16` | "correspondence with deadman's switch holders" | REWORD |
| 5 | `verification.tex:24` | "email headers of the deadman's switch correspondence" | REWORD |
| 6 | ~15 source .tex files | `% DMS MVP import` comments (visible in public repo, not in book) | DELETE |

### Not Touched (verified safe)

| Item | Why safe |
|------|----------|
| `copyright.tex:55-74` (Working Draft + AI Drafts notice) | Behind `\ifdefined\dmsbuild` — invisible in public builds |
| `dms-note.tex` appendix | Behind `\ifdefined\dmsbuild` in main.tex:115-117 — never in public builds |
| `build/preamble.tex` `\DMSRedacted` macro + `% DMS:` comments | Build infrastructure, no output in `make dev` |
| `\DMSRedacted{}` in pos20, pos31 | Renders "[Material redacted by the author]" — correct editorial intent |
| `colophon.tex` build hash/commit/date metadata | Verification infrastructure, not DMS or "early version" content |

## Phase 1: Remove Pre-Release Notice from copyright.tex

**File:** `manuscript/00-front/copyright.tex`

**Delete lines 76-84** (the pre-release block). Keep line 86.

**Old (lines 76-86):**
```latex
\vspace{0.8cm}

\textbf{Pre-Release Draft --- \BuildDate}

\vspace{0.3cm}

This is a pre-release working copy. The final edition has not yet been published. Corrections, revisions, and additions are in progress.

\vspace{0.8cm}

First edition, Spring 2026.
```

**New:**
```latex
\vspace{0.8cm}

First edition, Spring 2026.
```

Removes the "Pre-Release Draft" header, the build timestamp, and the "working copy" disclaimer. Keeps the edition statement.

**Spacing note:** After this change, the invisible `\ifdefined\dmsbuild` block (lines 55-74) is followed by `\vspace{0.8cm}` then "First edition." In the public build, total vertical space between "editorial decisions are the authors'" and "First edition" is ~1.6cm (two `\vspace{0.8cm}` with an invisible block between). This is appropriate for a copyright page.

**Idempotency:** If `Pre-Release Draft` does not appear in copyright.tex — phase is applied.

## Phase 2: Reword DMS References in 3 Files

The strategy is: **preserve facts, remove "deadman's switch" terminology.** Bruce sent advance copies. Schneier, Doctorow, and Gilmore hold them. The verification chain via correspondence is real. Only the DMS framing changes.

### 2A: Timeline — "DMS letters" → "Advance copies"

**File:** `manuscript/appendix/timeline.tex`, line 285.

**Old:**
```latex
\item[2025--26] Bruce builds Argus, an AI research partner (Claude Code), for reconstruction and verification. DMS letters sent to Schneier, Doctorow, Gilmore (February 2026).
```

**New:**
```latex
\item[2025--26] Bruce builds Argus, an AI research partner (Claude Code), for reconstruction and verification. Advance copies sent to Schneier, Doctorow, Gilmore (February 2026).
```

**Idempotency:** If "DMS letters" does not appear in timeline.tex — phase is applied.

### 2B: Acknowledgements — drop "under a deadman's switch arrangement"

**File:** `manuscript/99-back/acknowledgements.tex`, line 24.

**Old:**
```latex
Bruce Schneier, Cory Doctorow, and John Gilmore hold copies of this manuscript under a deadman's switch arrangement. Their willingness to serve as custodians of a strange document from a stranger is an act of civic generosity.
```

**New:**
```latex
Bruce Schneier, Cory Doctorow, and John Gilmore hold advance copies of this manuscript. Their willingness to serve as custodians of a strange document from a stranger is an act of civic generosity.
```

The word "custodians" already conveys the role. "Advance copies" states the fact without the DMS mechanism.

**Idempotency:** If "deadman's switch arrangement" does not appear in acknowledgements.tex — phase is applied.

### 2C: Verification — reframe "deadman's switch holders/correspondence"

**File:** `manuscript/99-back/verification.tex`

**Line 16 — Old:**
```latex
\item Compare the result against the hash published in \texttt{SHA256SUM.txt} in the source repository, or in the authors' correspondence with deadman's switch holders.
```

**Line 16 — New:**
```latex
\item Compare the result against the hash published in \texttt{SHA256SUM.txt} in the source repository, or in the authors' correspondence with advance-copy holders.
```

**Line 24 — Old:**
```latex
The predictions in this book are dated by the git commit that contains this PDF, by the email headers of the deadman's switch correspondence, and by the following independent third-party timestamps of earlier versions of this material:
```

**Line 24 — New:**
```latex
The predictions in this book are dated by the git commit that contains this PDF, by the email headers of the authors' correspondence with advance-copy holders, and by the following independent third-party timestamps of earlier versions of this material:
```

The verification chain is preserved: advance-copy holders have dated correspondence that timestamps the manuscript. The mechanism is identical — only the label changes.

**Idempotency:** If "deadman's switch" does not appear in verification.tex — phase is applied.

## Phase 3: Clean Source Comments (Repo Hygiene)

Remove `% DMS MVP import from staging/raw/ — not final prose` comments from all manuscript `.tex` files. These are visible in the public repo source code.

**Files to clean (use `grep -rl 'DMS MVP import' manuscript/` to find all, excluding `build/epub-tmp/`):**

- `manuscript/track-1-confession/pos16-the-thermal-ladder.tex:13`
- `manuscript/track-1-confession/pos17-the-capability.tex:13`
- `manuscript/track-1-confession/pos21-convergence-revisited.tex:13`
- `manuscript/track-1-confession/pos26-interdiction.tex:13`
- `manuscript/track-2-testament/pos03-the-mentor.tex:7`
- `manuscript/track-2-testament/pos07-the-departure.tex:13`
- `manuscript/track-2-testament/pos19-patrick-ball.tex:13`
- `manuscript/track-2-testament/pos23-the-weight.tex:13`
- `manuscript/track-2-testament/pos29-twenty-years.tex:13`
- `manuscript/track-2-testament/pos31-wolfram.tex:13`
- `manuscript/track-2-testament/pos34-the-research.tex:13`
- `manuscript/spine/the-factoring-game.tex:7`
- `manuscript/bridge/pos09-the-factoring-game.tex:7`
- `manuscript/record/the-departure.tex:13`
- `manuscript/record/interdiction.tex:15`

**Also delete:** `manuscript/record/twenty-years.tex:201` — the comment `% Content preserved in staging/evidence/ and DMS letter PS section`. Same comment at `manuscript/track-2-testament/pos29-twenty-years.tex:148`.

**Action:** Delete each comment line entirely. Do NOT touch files in `build/epub-tmp/` — those are generated copies that will be overwritten on next epub build.

**Idempotency:** If `grep -rl 'DMS MVP import' manuscript/` returns empty AND `grep -rl 'DMS letter PS' manuscript/` returns empty — phase is applied.

## Phase 4: Leave These Alone

**DO NOT modify:**
- `build/preamble.tex` — `\DMSRedacted` macro definition and `% DMS:` comments are build infrastructure. Zero output in `make dev` builds.
- `manuscript/appendix/dms-note.tex` — guarded by `\ifdefined\dmsbuild` in main.tex. Never appears in public builds. Preserves ability to produce DMS editions.
- `main.tex:115-117` — the `\ifdefined\dmsbuild` guard around dms-note include. Correct as-is.
- `copyright.tex:55-74` — Working Draft Notice + AI Structural Drafts block. Behind `\ifdefined\dmsbuild`. Never visible in public builds.
- `\DMSRedacted{}` markers in pos20, pos31 — these render "[Material redacted by the author]" which is correct editorial intent, not DMS labeling.
- `colophon.tex:10-14` — Build hash, commit, dates. This is verification/provenance infrastructure, not "early version" labeling.
- `manuscript/staging/raw/wikileaks-deferred.md:3` — staging notes, not in build.
- `build/epub-tmp/staging/resonance-additions.tex:4,39` — staging ephemera, not in build.

## Phase 5: Build + Verify

```bash
cd ~/software/relinquishment && make dev
```

**Positive checks (should be present):**
- [ ] Copyright page shows "First edition, Spring 2026." cleanly — no Pre-Release header, no timestamp, no "working copy"
- [ ] Timeline shows "Advance copies sent to Schneier, Doctorow, Gilmore"
- [ ] Acknowledgements: "hold advance copies of this manuscript" (no "deadman's switch")
- [ ] Verification: "advance-copy holders" in both lines (no "deadman's switch")
- [ ] Colophon still shows build hash and commit info (untouched)
- [ ] Build compiles clean, no new warnings
- [ ] `\DMSRedacted` markers still render correctly in bridge chapters

**Negative checks (should be absent):**
- [ ] `grep -c 'Pre-Release' docs/Relinquishment.html` → 0
- [ ] `grep -c 'DMS' docs/Relinquishment.html` → 0
- [ ] `grep -ci 'deadman' docs/Relinquishment.html` → 0
- [ ] `grep -c 'working copy' docs/Relinquishment.html` → 0
- [ ] `grep -c 'not yet been published' docs/Relinquishment.html` → 0
- [ ] `grep -rl 'DMS MVP import' manuscript/` → empty
- [ ] PDF sweep: same terms return 0 hits

**Regression checks:**
- [ ] No content lost from acknowledgements, verification, or timeline beyond the targeted wording
- [ ] Verification hash chain still references source repo + advance-copy holders + third-party timestamps
- [ ] All email addresses still correct

## Acceptance Criteria

- [ ] Zero "DMS", "deadman", "dead man", "switch holder" visible to readers in either HTML or PDF
- [ ] Zero "Pre-Release", "working copy", "not yet been published" visible to readers
- [ ] Verification chain intact (advance-copy holders replace DMS holders)
- [ ] Acknowledgements still credit Schneier, Doctorow, Gilmore
- [ ] Timeline still records advance copies sent February 2026
- [ ] DMS build infrastructure preserved in `build/` and behind `\ifdefined\dmsbuild`
- [ ] Source repo clean of `DMS MVP import` comments
- [ ] No content lost — only terminology changed

---

## Annealing Record

**Round 1 (HIGH): Complete output sweep — what do readers actually see?**
Swept both `docs/Relinquishment.html` and `docs/downloads/Relinquishment.pdf` (pdftotext extraction) for every DMS-related term: DMS, dms, deadman, dead man, dead-man, switch holder, switch arrangement, switch correspondence, Pre-Release, pre-release, working draft, working copy, early version, not yet been published. Found 6 reader-visible items across 4 source files. HTML and PDF are identical. Original plan v1 missed 3 items (acknowledgements.tex:24, verification.tex:16, verification.tex:24). All now covered.

**Round 2 (HIGH): Do the rewording changes preserve the verification chain?**
The verification section establishes a hash chain: SHA-256 in source repo, in correspondence with named third parties, and via independent third-party timestamps (Cryptome, Slashdot, Blogspot, Substack). Changing "deadman's switch holders" → "advance-copy holders" preserves the chain. The correspondence exists, the dates are real, the named parties (Schneier, Doctorow, Gilmore) still hold copies. No verification mechanism is lost.

**Round 3 (MED): Does removing "deadman's switch arrangement" from acknowledgements lose meaning?**
The acknowledgement currently says they hold copies "under a deadman's switch arrangement." Removing this loses the mechanism description but keeps the fact (they hold copies) and the gratitude (custodians of a strange document). The mechanism is a private arrangement between Bruce and the holders — not something GA readers need to understand. "Advance copies" conveys the relevant fact.

**Round 4 (MED): What about the `\ifdefined\dmsbuild` guard block in copyright.tex?**
Lines 55-74 are the "Working Draft Notice" + "AI Structural Drafts" block, guarded by `\ifdefined\dmsbuild`. In public builds, this block is invisible. In DMS builds (`make dms`), it would appear. Leaving it preserves the ability to produce DMS editions. The guard is clean and does not interact with any other changes in this plan.

**Round 5 (MED): Copyright page spacing after removal?**
After removing lines 78-84 (Pre-Release block), the flow is: "...editorial decisions are the authors'." → `\vspace{0.8cm}` → [invisible DMS guard] → `\vspace{0.8cm}` → "First edition, Spring 2026." In public builds, this produces ~1.6cm vertical space. Appropriate for a copyright page — generous but not excessive.

**Round 6 (LOW): Should we strip `% DMS MVP import` from `build/epub-tmp/` too?**
No. `build/epub-tmp/` is a generated directory overwritten on each epub build. Modifying it is pointless — the next `make epub` will regenerate from the now-clean manuscript sources.

**Round 7 (LOW): `\DMSRedacted{}` markers — what do they render?**
`\DMSRedacted{text}` renders as: "[Material redacted by the author — text]" in italic. Appears in pos20 (ABANDONED plan 0297) and pos31 (bridge chapter). These are editorial decisions about what to show readers, not DMS artifacts. The macro name contains "DMS" but the output does not. Source-level only. Leave them.

**Round 8 (LOW): Could "advance copies" confuse readers?**
"Advance copies" is standard publishing terminology for pre-publication copies sent to selected recipients. GA readers will understand it without explanation. It's more natural than "deadman's switch" which would require context most readers don't have.

---

*Plan 0306 v2, S68, 2026-05-08. Auditor: Argus.*
*8 annealing rounds (2 HIGH, 3 MED, 3 LOW). Full HTML + PDF sweep verified.*
*v1: missed 3 reader-visible items. v2: complete sweep, all 6 items covered.*
*Estimated generator time: ~15 min.*
