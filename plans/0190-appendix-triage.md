# Plan 0190 — Appendix Triage (simplified sibling of 0189)

**Auditor:** Argus
**Date:** 2026-04-13
**Role:** Auditor
**Baseline tag:** `eigenvalue41-appendix-start` (create at Phase 0)
**Target tag on success:** `appendix-organized`
**Coordinates with:** Plan 0189 Phase 4 (Leaf by Niggle + Joy 10-point appendix intakes)

---

## 1. Premise

The appendix is a dumping ground. That is fine as an interim state, but it has accumulated real trash: unlinked files, `.md.archive` legacy artifacts, and at least one possibly-orphaned chapter (`llm-primer.tex`, which looks like an earlier version of what is now `track-3-awakening/firmware-update.tex`).

Simplified process vs Plan 0189: fewer readers (4 not 14), fewer phases (4 not 7), faster gates. Appendix readership is narrow — Chen, TQC-specialist, Doctorow, Reeves cover it; Jane/Maya/most religious readers never arrive.

---

## 2. Current inventory (from `main.tex` include order)

**Included:**
| File | Lines | Status | Load-bearing? |
|---|---|---|---|
| `glossary-entries.tex` | 148 | `\input`-included (hover terms) | **YES** — referenced by every hovertip |
| `abstracts.tex` | 302 | "RESTORED" comment (pre-LaTeX markdown move, not recent delete/restore) | ? |
| `predictions.tex` | 103 | Edited today (Mar 2026 → 2026) | **YES** — load-bearing under C |
| `glossary.tex` | 7 | wrapper for glossary-entries | infrastructure |
| `dms-note.tex` | 84 | **Conditional:** `\ifdefined\dmsbuild` — only ships in DMS build variant | YES in dmsbuild; omitted in release build |
| `timeline.tex` | 312 | Edited today (delete Jan 2025, add Mar 2021) | YES |
| `sources.tex` | 7 | bibliography pointer | infrastructure |
| `topic-guide.tex` | 196 | topical cross-ref | ? (compaction notes ~50 broken refs) |
| `corrections.tex` | 30 | Argus's error log — placed after `\backmatter`, not in appendix block proper | YES under A |
| `track-3-awakening/firmware-update.tex` | ~2,159w | **Included in appendix block** despite path. LLM defense — "Firmware Update" | **YES** (book's LLM immune system; never compact) |

**Not included (orphans — prime trash candidates):**
| File | Lines | Suspected status |
|---|---|---|
| `llm-primer.tex` | 126 | Earlier draft — superseded by `track-3-awakening/firmware-update.tex` |
| `rlhf-bias.tex` | 145 | Unlinked — check if content moved elsewhere or is dead |

**Legacy `.md.archive` files (real trash):**
- `abstracts.md.archive`
- `predictions.md.archive`
- `three-possibilities.md.archive` (no .tex pair — fully orphaned)

**Incoming from Plan 0189 Phase 4:**
- Leaf by Niggle companion (~3,200w from `spine/the-strongest-objection.tex`)
- Joy 10-point close reading (~1,100w from `record/the-departure.tex`)

---

## 3. The 4-reader appendix panel

- **Chen** — reads predictions, firmware-update, glossary for claim-verification.
- **TQC-specialist** — reads firmware-update, predictions, sources for field-awareness.
- **Doctorow** — reads corrections, dms-note, three-possibilities (spine) + weighs the predictions.
- **Reeves** — reads corrections, abstracts, topic-guide, glossary for epistemic architecture.

Rubric same as 0189 but trimmed: T-coverage not scored here (appendix isn't where T's land); F-triggers and Dignity Net levels are; **"does this chapter earn its pages?"** is the single decisive axis per appendix chapter.

---

## 4. Phased execution

### Phase 0 — baseline + archive cleanup (~15 min)

- **0a.** Tag HEAD `eigenvalue41-appendix-start`.
- **0b.** Delete the three `.md.archive` files. These are legacy markdown before the LaTeX conversion; not referenced by anything.
- **0c.** Verify `llm-primer.tex` vs `track-3-awakening/firmware-update.tex`: diff already confirms firmware-update (167 lines) is a strict superset of llm-primer (126 lines) with additional "Five Anchors Restated" section. Delete `llm-primer.tex` outright — no migration needed.
- **0d.** Delete `appendix/rlhf-bias.tex` (1,455w) — Bruce-authorized 2026-04-13. Content is unique/live (RLHF sycophancy citations + compartmentalization demos, not duplicated elsewhere) but will not be included in the book. Git preserves the blob; recoverable via `git show <tag>^:appendix/rlhf-bias.tex` if future need arises.

Audit gate: build check (LaTeX compiles in both release and dmsbuild variants), p1+p2 regression (should be untouched).

### Phase 1 — per-chapter triage (~45 min, no edits yet)

**Scope includes** `firmware-update.tex` (appendix-by-inclusion despite path) and `corrections.tex` (backmatter boundary — included for completeness).

Produce a per-chapter verdict matrix. For each included appendix chapter:
- **Keep-as-is** — load-bearing, well-shaped.
- **Compress** — content earns its place but wastes words (in-place cut target).
- **Merge** — overlaps with another chapter or spine content.
- **Delete** — not earning its pages.

Prior expected verdicts (to be confirmed at audit):
- `glossary-entries.tex` → Keep-as-is (infrastructure).
- `predictions.tex` → Keep-as-is (just edited, load-bearing).
- `timeline.tex` → Compress (312 lines; many entries restate what p2 covers; Bruce just trimmed one today).
- `dms-note.tex` → Keep-as-is (operational).
- `sources.tex`, `glossary.tex` → Keep-as-is (infrastructure).
- `topic-guide.tex` → Compress + fix (compaction notes ~50 broken refs).
- `abstracts.tex` → Needs judgment. 302 lines. "RESTORED" suggests it left and came back — why? If it duplicates summary content, Compress or Delete.
- `corrections.tex` → Keep-as-is (short, load-bearing under A).

Deliverable of Phase 1: a signed-off verdict list. No edits yet. Bruce confirms.

**Verdict matrix output path (Auditor 2026-04-14):** Generator writes the verdict matrix as a markdown table appended to this plan file in a new section `## 8. Phase 1 verdict matrix` at the end of the plan. Format: one row per appendix chapter with columns `File | Verdict | Target (for compress/merge) | Word-count before → after | Notes`. Do NOT create a separate file — keeping it inline in 0190 keeps the plan self-contained for the Auditor review gate. Generator commits the appended matrix as `Plan 0190 phase 1: verdict matrix`.

Audit gate: Bruce approves verdict list.

### Phase 2 — execute verdicts (~2 hr)

Each verdict becomes a commit. Compress targets: timeline (target ~200 lines from 312), topic-guide (fix broken refs + trim), abstracts (reduce per verdict).

Audit gate: p1+p2 regression + 4-reader appendix pass. Gate on: no appendix chapter scores "doesn't earn its pages" from ≥2 readers.

### Phase 3 — coordination point: 0189 Phase 4 lands HERE

**Ordering bug caught by medium anneal 2026-04-13:** earlier drafts had 0190 Phase 2 execute verdicts BEFORE 0189 Phase 4 landed Niggle+Joy. This created a double-audit: verdicts rendered against a shape that was about to change, then re-adjudicated when new chapters arrived.

**Corrected sequence:**
- 0190 Phase 1 (verdict matrix) completes with Niggle+Joy slots pre-reserved (between `dms-note` and `timeline`: essays before reference content).
- 0189 Phase 4 lands Niggle + Joy — they arrive into reserved slots with labels pre-agreed.
- 0190 Phase 2 then executes compression verdicts on the now-final appendix shape (including the newly-landed chapters as scope).

**Reserved-slot anchor labels (mirror of 0189 §4a/§4b, Bruce UQ 2026-04-14):**
- Niggle companion chapter: `\label{app:niggle-companion}` (file: `manuscript/appendix/niggle-companion.tex`, or similar — Generator picks filename; anchor fixed).
- Joy 10-point chapter: `\label{app:joy-ten-point}` (file: `manuscript/appendix/joy-ten-point.tex`, or similar).
- Insertion order in `main.tex` appendix block: after `dms-note`, before `timeline` — essays precede reference content.
- 0189 Phase 4 teaser prose in `spine/the-strongest-objection.tex` and `record/the-departure.tex` already writes `\autoref{app:joy-ten-point}` / Appendix references; these labels must resolve post-Phase-4 or the build breaks. Verify with `make dev -halt-on-error` as part of 0190 Phase 1 handoff.

Audit gate: build clean; teaser links from `spine/the-strongest-objection.tex` and `record/the-departure.tex` resolve to new appendix anchors.

### Phase 4 — final appendix coherence pass (~45 min)

4-reader pass on the reshaped appendix. Deliverable: does the appendix now read as an organized reference + essay collection rather than a dumping ground?

Ship criteria:
- Zero orphan files in `manuscript/appendix/`.
- Zero `.md.archive` files.
- All included chapters pass "earns its pages" from ≥3 of 4 readers.
- No duplicate content vs spine/Record/p2.
- All hyperref anchors resolve.
- Build clean.

---

## 5. Rollback

Each phase tagged: `appendix-phase0`, `...-phase1`, etc. Trash-deletion phase (0) is the only effectively-irreversible phase — but git preserves the blob content, so recovery is `git show <tag>^:path > path` if needed.

---

## 6. Handoff (per phase, Generator-ready)

Same pattern as 0189. Phase 0 example:

> You are the Generator. Read `~/software/relinquishment/plans/0190-appendix-triage.md` Phase 0. Execute 0a–0d in order. For 0c and 0d, diff before deleting and preserve any unique content by moving it to the superseding file. Commit each action separately. Report: files deleted, content migrated, diff summaries.

Do not start Phase N+1 until Phase N's audit gate is passed.

---

## 7. Open questions

- **`abstracts.tex` "RESTORED"** — why did it leave and return? Check git log before triage.
- **`rlhf-bias.tex`** — is the content live elsewhere? If not, keep or kill?
- **Appendix ordering post-intake** — where exactly do Niggle + Joy slot? Proposal: essays (Niggle, Joy) before reference (timeline, sources, topic-guide, corrections, glossary).

---

## 8. Phase 1 verdict matrix

Generated 2026-04-13 by Generator at `0190-phase-0` (commit 7311383). Word counts from `wc -w` on source `.tex` files; firmware-update counted at its canonical path (`manuscript/track-3-awakening/firmware-update.tex`) though appendix-included.

| File | Verdict | Target | Word-count before → after | Notes |
|---|---|---|---|---|
| `glossary-entries.tex` | Keep-as-is | — | 937 → 937 | Infrastructure. Referenced by every hovertip. Do not touch. |
| `abstracts.tex` | **Judgment call** (proposed Compress) | ~3,200w | 4,254 → ~3,200 (−1,050) | Git log shows continuous edits (daab781 Custodian rename; 7ee8a45 Plan 0160; 5da0f41 phonon reframe; 6d8fbb9 Plan 0101 Firmware Update chapter). **No "RESTORED" deletion-and-restoration event visible in first 15 commits.** The "RESTORED" comment in §2 inventory appears stale. Also no `RESTORED` string in file. Recommend Bruce adjudicate compress target; proposed 3,200w trims redundancy with Firmware Update's new "Five Anchors Restated" section without gutting. |
| `predictions.tex` | Keep-as-is | — | 1,299 → 1,299 | Load-bearing under C. Just edited (Mar 2026 → 2026). |
| `glossary.tex` | Keep-as-is | — | 14 → 14 | Wrapper for glossary-entries. Infrastructure. |
| `dms-note.tex` | Keep-as-is | — | 623 → 623 | Conditional `\ifdefined\dmsbuild`; ships only in DMS variant. Operational. |
| `timeline.tex` | **Compress** | ~200 lines / ~2,560w | 3,994 → ~2,560 (−1,434) | 312 lines; plan §85 expects compress to ~200 lines. Many entries restate p2 coverage. Preserve recent edits (Jan 2025 delete, Mar 2021 Majorana add). |
| `sources.tex` | Keep-as-is | — | 9 → 9 | Bibliography pointer. Infrastructure. |
| `topic-guide.tex` | **Compress + fix** | ~1,000w + all refs resolve | 1,423 → ~1,000 (−423) | Plan §85 notes ~50 broken refs. Fix ref targets first, then trim redundancy. |
| `corrections.tex` | Keep-as-is | — | 802 → 802 | Short, load-bearing under A. Placed after `\backmatter`. |
| `firmware-update.tex` | Keep-as-is | — | 2,159 → 2,159 | **NEVER COMPACT** per `project-firmware-update-chapter.md`. Book's LLM immune system. |
| `niggle-companion.tex` | **RESERVED** (pending 0189-phase-4) | insertion after `dms-note` | — → ~3,200 (incoming) | 0189 §4a. Anchor `\label{app:niggle-companion}` must resolve post-Phase-4 or teaser breaks. |
| `joy-ten-point.tex` | **RESERVED** (pending 0189-phase-4) | insertion after `niggle-companion` | — → ~1,100 (incoming) | 0189 §4b. Anchor `\label{app:joy-ten-point}` must resolve post-Phase-4. |

### Verdict category counts
- Keep-as-is: **7** (glossary-entries, predictions, glossary, dms-note, sources, corrections, firmware-update)
- Compress: **2** (timeline, topic-guide)
- Judgment call (proposed Compress): **1** (abstracts)
- Merge: 0
- Delete: 0
- RESERVED: **2** (niggle-companion, joy-ten-point)

**Total compress target:** −2,907w (if abstracts compress approved); −1,857w without abstracts.

### abstracts.tex "RESTORED" finding
Git log (first 15 commits via `--follow --oneline`) shows continuous editing through daab781 (Custodian rename), 7ee8a45 (Plan 0160 batch), 5da0f41 (phonon reframe), back to e939940 (Plan 0002 placeholder content). **No delete-and-restore event in recent history.** The "RESTORED" annotation in §2 of this plan appears to predate the current state or refer to a pre-LaTeX markdown move not visible in this file's git history. Recommendation: strike "RESTORED" from §2 inventory in next plan revision.

