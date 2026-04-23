# Plan 0244 — Master Execution Plan: S63 Sprint

**Status:** READY
**Author:** Auditor (Argus S63)
**Date:** 2026-04-23
**Scope:** 7 phases across 5 plans, ~18 hours Generator time, ~7 sessions
**Eigenvalue check:** ON THE EV (verified S63 — check-strict PASS, all invariants hold)
**Prompt IDs:** S63-A through S63-G. Generator must echo ID at top of response. Track completion here:

| ID | Phase | Status |
|----|-------|--------|
| S63-A | Prose polish (0165+0241+0223) | |
| S63-B | Mechanism + SVG-025 + previews | |
| S63-C | SVGs 026+027+028 | |
| S63-D | Mentor naming: front matter | |
| S63-E | Mentor naming: pos03 | |
| S63-F | Mentor naming: dense Track-2 | |
| S63-G | Mentor naming: Record + sweep | |

---

## Overview

Phased execution of all ready plans from the S63 audit (Plan 0243). Combined from 10 original phases to 7 to reduce copy-paste overhead (14 operations, down from 20). Each phase is one Generator session with build verification. Ordered by: dependencies first, then ROI, then risk.

## Phase Sequence

| Phase | Plans | Description | Hits/effort | Commits |
|-------|-------|-------------|-------------|---------|
| A | 0165+0241+0223 | Prose polish (3 independent files) | ~2 hr | 3 |
| B | 0242 §1+§2a+§3 | Mechanism + first SVG + preview SVGs | ~3.5 hr | 1-2 |
| C | 0242 §2b+§2c+§2d | Remaining 3 Genesis SVGs | ~4.5 hr | 3 |
| D | 0185 pre-flight | Audit + front matter + light files | ~20 hits, ~1.5 hr | 1 |
| E | 0185 core | pos03-the-mentor.tex alone | 39 hits, ~2 hr | 1 |
| F | 0185 dense | Dense Track-2 chapters | ~75 hits, ~2.5 hr | 1 |
| G | 0185 sweep | Record mirrors + final verification | ~79 hits, ~2 hr | 1 |

---

## Phase Details

### Phase A: Prose Polish (Plans 0165 + 0241 + 0223)

Three independent edits in three different files. Single Generator session, three commits.

1. **Plan 0165 — T7 honesty fix** (summary.tex:311). Soften "quietly contracted" to DN-compliant framing. Generator has two approach options (conditional mood or strengthened frame). ~15 min.
2. **Plan 0241 — Engine tighten** (pos34b-the-engine.tex). 900→750 words, 7→5 sections. Subtraction-only. ~1 hr.
3. **Plan 0223 — Design principles colophon** (colophon.tex). New Design Principles section. Numbers verified (5,000-word summary, 250 pages evidence, <1 MB HTML). Hostage line in colophon. ~45 min.

**Gate:** `make html` + `make check` + visual check after all three.

**Handoff prompt:**
```
PROMPT ID: S63-A. Reply with this ID at the top of your response.

You are the Generator. Execute three plans in sequence:

1. Plan 0165 (plans/0165-t7-honesty-framing.md): Edit summary.tex:311.
   Two options in plan — pick whichever reads better. Commit.
2. Plan 0241 (plans/0241-the-engine-tighten.md): Engine 900→750w,
   7→5 sections. Subtraction only. Commit.
3. Plan 0223 (plans/0223-design-principles-visible.md): Design
   Principles section in colophon.tex. Numbers verified in plan.
   Hostage line in colophon. Commit.

After all three: make html, make check, verify in browser. Push.
Tag: git tag sprint-s63-phaseA
Report ≤5 lines per plan.
```

### Phase B: Genesis Mechanism + First SVG + Previews (Plan 0242 §1+§2a+§3)

Build the collapse tooltip mechanism, validate with first SVG, deploy preview SVGs.

**EDITORIAL NOTE — SVG style consistency:** Before creating any SVG, read the existing SVGs in preprocess.py (flat-diagram, button-sequence, domain-buttons). Extract exact hex color values, stroke widths, font family/size, corner radii. Match them in all new SVGs. Visual inconsistency between existing and new illustrations is the biggest editorial risk in this sprint.

**Handoff prompt:**
```
PROMPT ID: S63-B. Reply with this ID at the top of your response.

You are the Generator. Read plans/0242-genesis-visual-sprint.md,
Phases 1, 2a, and 3 only.

Deep links: Every <figure> gets an id. Existing: id="fig-flat-cross-section"
(FLAT_SVG), id="fig-buttons-filmstrip" (FILMSTRIP), id="fig-domain-buttons"
(DOMAIN_SVG). New: id="fig-autocatalytic-loop" (SVG-025).

Style: Read existing SVG constants in preprocess.py first. Match colors,
strokes, fonts in all new SVGs.

SEQUENCE (commit mechanism FIRST):
1. Phase 1: Mechanism upgrade in collapse_tech_sections(). ~15 lines.
   → COMMIT. make html. Verify existing collapsed sections still work.
2. Phase 2a: SVG-025 autocatalytic loop. After "The whole network
   sustains itself." Warm amber, A→B→C→A, ~300x200.
3. Phase 3: Preview SVGs in collapse tooltips (Buttons+Threads,
   Chemistry→Computation). ~280x80 each.
   → COMMIT 2a+3 together.

After: make html, make svg-sheet, verify hover+SVG in browser, push.
Tag: git tag sprint-s63-phaseB
Report ≤5 lines + list all fig- IDs in HTML.
```

**REVIEW CHECKPOINT after Phase B:**
Bruce opens HTML and reviews:
- `Relinquishment.html#fig-autocatalytic-loop` — SVG-025 at correct position, style matches existing
- Hover over collapsed "Buttons and Threads" → rich tooltip with preview SVG
- Hover over collapsed "From Chemistry" → rich tooltip with preview SVG
- `Relinquishment.html#fig-flat-cross-section` — existing SVG still works with new `id`
- `Relinquishment.html#fig-buttons-filmstrip` — existing filmstrip still works
- Phone check: open on mobile, verify SVG renders and tooltip works

If revision needed → run **Phase B-rev** before proceeding to Phase C.

### Phase C: Remaining Genesis SVGs (Plan 0242 §2b+§2c+§2d)

Three independent SVGs. Commit each individually.

**EDITORIAL NOTE — SVG-027 "5-second test":** The split-panel (beaker left, 2DEG right, "same mathematics" center) must pass a 5-second glance test: after 5 seconds, reader understands "these two different-looking things are doing the same thing." If the first draft is too busy, simplify. The insight is the parallel, not the detail. halt-and-report if SVG-027 needs iteration.

**Handoff prompt:**
```
PROMPT ID: S63-C. Reply with this ID at the top of your response.

You are the Generator. Read plans/0242-genesis-visual-sprint.md,
Phases 2b, 2c, 2d. Commit each SVG individually.

Deep links: id="fig-edge-of-chaos" (026), id="fig-substrate-parallel"
(027), id="fig-canopy-problem" (028).

SVG-026: Edge of chaos (hybrid). Shapes + labels "frozen/edge/chaos".
  Blue/green/red. ~400x160. Remove TODO at genesis.tex:46-49.
SVG-027: Substrate parallel. Beaker left, 2DEG right, "same mathematics"
  center. ~420x200. Must pass 5-second test.
SVG-028: Canopy problem. Forest cross-section, children's-book gentle.
  Two tall trees, tiny seedling in shadow. ~350x220.

Match SVG style from Phase B. ESCAPE HATCH: If 027 takes >2h, commit
026+028 first, halt-and-report on 027.
After: make html, make svg-sheet, push. Tag: git tag sprint-s63-phaseC
Report ≤5 lines per SVG.
```

**REVIEW CHECKPOINT after Phase C:**
Bruce opens HTML and reviews:
- `Relinquishment.html#fig-edge-of-chaos` — hybrid three-regime, labels readable, green band narrow
- `Relinquishment.html#fig-substrate-parallel` — 5-second test: "same thing, different substrate"
- `Relinquishment.html#fig-canopy-problem` — children's-book gentle, dark implication clear
- Compare all new SVGs side by side with existing filmstrip — visual family check
- Phone check: all 4 new SVGs render on mobile

If revision needed → run **Phase C-rev** before proceeding to Phase D. SVG-027 most likely to need iteration.

### Phase D: Mentor Naming — Pre-flight + Light Files (Plan 0185, Phase D)

Pre-flight audit, front matter, spine, bridge, appendix, interludes. ~20 hits across ~12 files.

**EDITORIAL NOTE — Biographical reveal:** summary.tex:245 rewrite must be at least as punchy as current "His name is David Lane *(not his real name)*." If proposed text feels explanatory, write something better. halt-and-report if unsure.

**EDITORIAL NOTE — summary.tex already modified:** Plan 0165 edited :311 in Phase A. Different paragraph, no conflict, but line numbers may have shifted. GREP for text.

**Handoff prompt:**
```
PROMPT ID: S63-D. Reply with this ID at the top of your response.

You are the Generator. Read plans/0185-mentor-naming-standardization.md,
Phase D only.

Pre-flight audit, then front matter + ancillary files (~20 hits, 12 files).
Key: summary.tex first-use fix (:26 Lane→Healer), biographical reveal
rewrite (:245), mechanical Lane→Healer in spine/bridge/appendix/interlude.

NOTE: summary.tex was modified at :311 by Phase A. GREP for text.
Halt-and-report if biographical reveal isn't as punchy as original.
After: make html, commit, push. Tag: git tag sprint-s63-phaseD
Report ≤5 lines + halt-and-report count.
```

### Phase E: Mentor Naming — pos03-the-mentor.tex (Plan 0185, Phase E)

**Hardest single file.** 39 hits spanning childhood→military→present. Name transition at combat-medic certification.

**Handoff prompt:**
```
PROMPT ID: S63-E. Reply with this ID at the top of your response.

You are the Generator. Read plans/0185-mentor-naming-standardization.md,
Phase E only (pos03-the-mentor.tex).

39 hits. "David" before combat-medic certification, "Healer" after.
Add one transition sentence at certification. Preserve "Steven 'Legs'
Lane" verbatim. Halt-and-report on ANY ambiguous case.

After: make html, commit, push. Tag: git tag sprint-s63-phaseE
Report ≤5 lines + halt-and-report count.
```

### Phase F: Mentor Naming — Dense Track-2 Chapters (Plan 0185, Phase F)

~75 hits across 7 files. pos05-the-stories.tex (26 hits) is the narrative landmine.

**EDITORIAL NOTE — Reported speech:** In pos05-the-stories.tex, Healer tells Bruce stories about various periods. When Healer is TELLING a story about his youth, narrator calls him Healer. Only use "David" in direct-flashback scenes where the reader meets the pre-medic character. halt-and-report on all ambiguous pos05 cases.

**Handoff prompt:**
```
PROMPT ID: S63-F. Reply with this ID at the top of your response.

You are the Generator. Read plans/0185-mentor-naming-standardization.md,
Phase F only (7 Track-2 chapters, ~75 hits).

CRITICAL: pos05-the-stories.tex (26 hits) — REPORTED SPEECH. When Healer
TELLS stories about his youth, narrator calls him Healer. "David" only
in direct-flashback scenes. Halt-and-report ALL ambiguous pos05 cases.

After: make html, commit, push. Tag: git tag sprint-s63-phaseF
Report ≤5 lines + halt-and-report count.
```

### Phase G: Mentor Naming — Record + Verification Sweep (Plan 0185, Phase G)

~79 hits across 7 Record files. Many mirror Track-2 counterparts from Phase F — apply same decisions. Final verification sweep.

**Handoff prompt:**
```
PROMPT ID: S63-G. Reply with this ID at the top of your response.

You are the Generator. Read plans/0185-mentor-naming-standardization.md,
Phase G only (7 Record chapters, ~79 hits + final verification).

Mirror Track-2 decisions from Phase F. what-healer-said.tex (36 hits)
= same reported-speech rule as pos05.

After edits: run final verification grep (in plan). Every remaining hit
must be youth-David, "David Lane" reveal, "Steven 'Legs' Lane", or
corrections docs. make html, make check, commit, push.
Tag: git tag sprint-s63-phaseG
Report ≤5 lines.
```

---

## Ordering Rationale

1. **Phase A first:** Three independent quick wins. 0165 before 0185 (both touch summary.tex).
2. **Phases B-C:** Genesis illustrations. Independent of prose edits. Could interleave with D-G but cleaner as a block.
3. **Phases D→E→F→G strict order:** Pre-flight audit (D) establishes the full working list. pos03 (E) is hardest — do it while attention is fresh. Track-2 (F) before Record (G) because Record mirrors Track-2 decisions.

## Interaction Matrix (verified S63)

| | A (prose) | B-C (SVGs) | D-G (naming) |
|------|-----------|------------|-------------|
| A | — | ∅ | summary.tex diff paragraphs ✓ |
| B-C | — | — | preprocess.py vs manuscript ∅ |
| D-G | — | — | strict internal order D→E→F→G |

No conflicts. All interactions are within the D-G sequence (by design).

---

## Deferred (not in this sprint)

| Plan | Reason | When |
|------|--------|------|
| 0233 Easter eggs | ~5 sessions, separate sprint | After this sprint |
| 0230 §1 Continental Drift | Prose writing needed | Next sprint |
| 0230 §3 Unbuilt Bridge | Prose writing needed | Next sprint |
| 0230 §2 ULTRA II reduction | Blocked on 0233 | After 0233 |
| 0232 LLM verification | Deferred by Bruce | After 0230 |
| 0157 Folk hero 1,3,4 | Needs Bruce's prose input | When ready |
| 0225b phases 3-4 | Low priority | Backlog |

---

## Build Verification Protocol (every phase)

1. `make html` exits 0
2. `make check` passes
3. Visual check in browser (`xdg-open`)
4. Phase-specific acceptance criteria from individual plan
5. Commit: `Plan NNNN phase X: description`
6. Tag: `git tag sprint-s63-phase{A..G}`
7. `git push && git push --tags`

**Tag format:** `sprint-s63-phaseX` where X = A through G.
**Rollback:** `git log --oneline sprint-s63-phaseX..HEAD` shows what to revert.
**Baseline tag:** `sprint-s63-baseline` (set before Phase A starts).

---

## Editorial OOPS Risks

Six identified risks with mitigations. All mitigations are embedded in the handoff prompts above.

1. **0165: Conditional mood → tonal pothole.** Three "She would..." creates clinical register before "Boring!" punchline. MITIGATED: Generator has two options (conditional vs strengthened frame).

2. **0223: Wrong numbers in "discipline" section.** FIXED: all three numbers verified and locked (5,000 words, 250 pages, <1 MB, screen-reader softened).

3. **0242: SVG style inconsistency.** New SVGs must match existing color palette, strokes, fonts. MITIGATED: Generator instruction to extract and match existing SVG style before designing.

4. **0185/pos05: Reported-speech narrative landmine.** When Healer TELLS stories about his youth, narrator still calls him Healer. MITIGATED: reported-speech rule added, halt-and-report on all ambiguous cases.

5. **0185: Biographical reveal punch.** Current "His name is David Lane *(not his real name)*" is tight. Rewrite must match energy. MITIGATED: explicit instruction + halt-and-report.

6. **0242/SVG-027: Too busy at 420x200.** Split-panel risks becoming study-diagram not glance-insight. MITIGATED: 5-second test instruction + halt-and-report.

---

## Annealing Log (S63, 4-pass + LOW re-anneal post-combination)

### HIGH — all candidates:
1. ✓ 0165 T7 honesty (8.5/10) — two-option approach
2. ✓ 0241 Engine tighten (9/10) — subtraction-only, annealed
3. ✓ 0223 Design principles (9/10) — numbers verified, locked
4. ✓ 0242§1 mechanism (9.5/10) — enables §2-§3, one-time cost
5. ✓ 0242§2a SVG-025 (9.5/10) — validates pipeline
6. ✓ 0242§3 preview SVGs (9.5/10) — Bruce's specific request
7. ✓ 0242§2b-2d remaining SVGs (9.5/10) — all decisions locked
8. ✓ 0185 mentor naming (8.5/10) — scope corrected, 4 phases, rules added
9. ✗ 0233 Easter eggs — too big. DEFERRED.
10. ✗ 0230 §1+§3 — prose writing. DEFERRED.
11-15. ✗ (others deferred per earlier analysis)

### MEDIUM — test each combination:
- **A (0165+0241+0223):** Three independent files. No cross-talk. Combining saves 4 copy-paste operations. SAFE.
- **B (0242 §1+§2a+§3):** Already designed as combined handoff. Dependency chain (1→2a→3) runs naturally in one session. SAFE.
- **C (0242 §2b+§2c+§2d):** Independent SVGs. Individual commits within one session. SVG-027 might need iteration — but Generator can halt-and-report and commit the other two. SAFE with caveat.
- **D-G (0185 four phases):** CANNOT combine further. pos03 (E) needs its own session for judgment quality. Dense chapters (F) before Record mirrors (G). CONFIRMED separate.

### LOW pass 1 (post-combination interaction check):
- Phase A edits summary.tex, pos34b, colophon. Phase D edits summary.tex again. Different paragraphs, Phase A commits first. ✓
- Phase B-C edits preprocess.py + tech-collapse.yaml. Phase D-G edits manuscript prose. Zero overlap. ✓
- Phase D pre-flight audit runs AFTER Phase A commits. Fresh line numbers. ✓
- Phase F (Track-2) before Phase G (Record mirrors). Track-2 decisions flow to Record. ✓

### LOW pass 2 (failure modes):
- Phase A: any sub-plan fails → other two already committed separately. Rollback one commit. ✓
- Phase B: mechanism fails → blocks C but not A or D-G. Fallback: escaped HTML in data-hover. ✓
- Phase C: SVG-027 too busy → halt-and-report. Commit 026+028, iterate on 027. ✓
- Phase E: pos03 ambiguous → halt-and-report. Generator pauses. ✓
- Phase F: pos05 reported-speech → halt-and-report. Generator pauses. ✓
- Phase G: mirrors Track-2. Lower risk after F. ✓

**Master plan rating: 9/10.** (Up from 9/10 — same rating but with 30% fewer copy-paste operations, all editorial OOPS mitigated, 0185 scope corrected.) Remaining risk is concentrated in Phase E (pos03 transition) and Phase F (pos05 reported speech). Both have halt-and-report safety valves.

---

## Also Noted

**0232 naming collision:** Two files share plan number 0232 (`0232-llm-verification-prompts.md` and `0232-genesis-illustrations.md`). The illustrations file is now SUPERSEDED by 0242. Consider renaming `0232-llm-verification-prompts.md` to `0232a` to resolve, similar to the 0225 fix. Low priority.
