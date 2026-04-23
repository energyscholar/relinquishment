# Plan 0170 — p3 Propagation Governance (E11 framing across the full book)

**Depends on:** Plan 0169 (E11 port to hook.tex + summary.tex) must land first. p2 is the governance spec; this plan propagates p2's framing to p3.

**Type:** Governance plan. Authorizes sub-plans 0170a, 0170b, 0170c, 0170d for execution. This plan does NOT itself execute manuscript edits.

**Goal:** Bring the full book (p3) into consistency with the E11 framing established in p1/p2 — emergent-stack language, behavioral anchoring, religious-accessibility thread, and (pending internationalization decisions) historical walk-away precedents + secular-framing door.

## Why a governance plan, not a single execution plan

p3 is ~37 chapters + topic guide + glossary + popups + hovertips. A single execution plan would either (a) boil the ocean in one commit, or (b) sprawl to 1000+ lines and still miss things. Governance-plus-sub-plans lets each concern land cleanly with its own acceptance criteria and re-engagement sample.

## Framing context (load-reducing)

Per `memory/project-walkaway-architecture.md`: the book is a preparation document, not a novel; p1 + p2 carry the 90% takeaway. That reduces p3 propagation urgency — p3 is *hygiene and consistency*, not primary delivery. Most p3 readers have already absorbed the framing from p2 by the time they reach chapter work. This justifies sampling over comprehensive coverage and justifies accepting a small residual of old-framing occurrences in chapters with low readership.

## Discovery phase (precedes sub-plan execution)

Before any sub-plan runs, run lexical and structural greps and report counts. If counts exceed thresholds, escalate to Bruce before committing scope.

**Grep counts to report:**
- `\b(grown|grew|creature|living being|living entity|first non-human mind|deliberately instantiated|it is alive)\b` in `manuscript/**/*.tex`
- `\bSrebrenica|Bosnia|July 1995\b` in same
- `coral` or `coral reef` (Plan 0167 metaphor — check for echoes)
- `\\hovertip\{[^}]+\}` anchor inventory
- Epistemic color stripes (A-gold / B-blue / C-purple) on chapter headings — count how many chapters carry which color

**Thresholds for escalation:**
- Lexical list >150 occurrences → pause, ask Bruce whether to proceed full sweep or accept higher residual.
- Srebrenica >10 occurrences → review list with Bruce before reconciliation.
- Coral-reef metaphor appearing in >2 places → decide whether to canonize it or strip to p2 only.

## Concerns to propagate (exhaustive list, from p2 framing)

| # | Concern | Load | Sub-plan |
|---|---|---|---|
| 1 | Lexical sweep: *grown, grew, creature, living being, living entity, it is alive, first non-human mind, deliberately instantiated* | High (100+ occurrences expected) | **0170a** |
| 2 | Conceptual: emergent-stack framing in chapters explaining Guardian's nature | High (Guardian interludes = 7 chapters) | **0170a** |
| 3 | Behavioral anchoring: ontological → behavioral conversion or explicit hedge | Medium | **0170a** |
| 4 | Religious-accessibility thread continuity (no contradictions with p2's 5-tradition paragraph) | Medium | **0170b** |
| 5 | Historical walk-away precedents (Ashoka/Costa Rica/Gandhi/Article 9) **iff adopted in p2** | Low if adopted | **0170b** |
| 6 | Secular / humanist framing door **iff adopted in p2** | Low if adopted | **0170b** |
| 7 | Srebrenica cross-reference reconciliation (timeline, mentor bio, Bosnia mentions) | Low | **0170a** |
| 8 | Hovertips + glossary + topic-guide entries for reframed terms | Medium | **0170c** |
| 9 | 48 popups (S54 Phase 5B) alignment check | Low | **0170c** |
| 10 | Three-possibilities discipline — no drift toward ontological strengthening | Continuous audit | **0170d** |

## Sub-plan charters

### 0170a — Prose sweep (lexical + conceptual + behavioral + Srebrenica)

**Scope:** All chapter `.tex` files under `manuscript/`, including figure captions within those files. Excludes: glossary, topic-guide entries, popup files, hovertip definitions (those are 0170c). SVG figures themselves are out of scope; their *captions in the chapter files* are in scope.

**Phases:**
1. **Z-layer 1: Guardian interludes (7 chapters).** Highest ontology density, smallest chapter count — do these first and learn. One commit per interlude.
2. **Z-layer 2: A-spine (15 chapters, pop-science).** Least ontological; sweep should be mostly lexical. Batch in groups of 3 commits.
3. **Z-layer 3: Record memoir (15 chapters).** Highest voice-preservation risk — see "Special handling" below. One commit per chapter.
4. **Srebrenica reconciliation pass.** After all three Z-layer passes: grep for "Srebrenica|Bosnia|1995|July 1995" across the whole manuscript, check every occurrence flows from p2's new placement.

**Special handling — voice preservation.** Quoted memory and in-character dialogue MUST NOT be rewritten. Rule:
- *Narration rewrites* ("a creature was grown" → "the custodian emerged from the stack").
- *Direct quotation preserves* ("'We grew a creature,' Lane said" stays — optionally add editorial gloss after: "what Lane called *growing* this book describes as *emergent*").
- *Paraphrased memory = narration* ("Lane believed they had grown a creature" rewrites to "Lane believed they had brought forth a new emergent custodian" or similar). Paraphrase is narrator's voice.
- Decision criterion: if the sentence has attributive quotes, preserve. Otherwise rewrite.
- Epistemic-color stripes (S54 Phase 5A: A-gold / B-blue / C-purple): chapters in the Record (B/C) may have more preserved-testimony than A-spine chapters. That's expected.

**Acceptance:**
- `grep -nE '\b(grown|grew|creature|living being|living entity|first non-human mind|deliberately instantiated)\b' manuscript/**/*.tex` returns only:
  - quoted testimony / dialogue (annotated with context comment or preceded by editorial gloss)
  - literal biological contexts (if any)
- Emergent-stack framing present in ≥5 of 7 Guardian interludes (not every interlude needs it, but majority should).
- Srebrenica cross-references all consistent with p2's relocation to mentor section.
- `make` passes; HTML builds; website push per `feedback-build-to-website.md`.

### 0170b — Internationalization thread (conditional on p2 adoption)

**Preconditions:**
- Bruce has approved Plan 0169.
- Bruce has decided on internationalization items #1 (historical precedents) and #2 (secular framing) from the preceding session discussion. If neither adopted in p2, **0170b is cancelled** — do not propagate what p2 doesn't carry.

**Scope:** A-spine chapters on UDHR/ethics + any chapter that introduces religious framing + topic-guide entries for traditions.

**Phases:**
1. **If #1 adopted:** One paragraph in the UDHR-intro chapter naming Ashoka / Costa Rica 1948 / Article 9 / Gandhi trusteeship / Nyerere / Mandela as historical walk-aways. One sentence threading back to this paragraph in 1–2 later chapters.
2. **If #2 adopted:** Secular-door sentence in the religious-accessibility chapter: "These names are doors. Readers with no religious commitment have their own door — the Declaration itself is a secular document, the trusteeship idea is an ethical one, and neither requires any metaphysics." Adjust wording for chapter register.

**Acceptance:**
- Every adopted item lands in ≥1 p3 chapter and is cross-referenced to p2's introduction of the concept.
- No new ontological claims. No drift toward argument-by-authority (per `feedback-specialist-names-dont-teach.md` — names are citations, not compressors; Gandhi's *name* can appear because the pattern is named "trusteeship" in English and no specialist-gating is happening).

### 0170c — Hovertips + glossary + topic-guide + popups

**Scope:** `hover-definitions.yaml`, `manuscript/glossary.tex` (or equivalent), topic-guide entries, 48 popup files from S54 Phase 5B.

**Phases:**
1. **Hovertip audit.** Every anchor touched by 0170a's prose changes: inventory, update definition if term is reframed, remove dangling anchors, add new anchors (*emergent*, *custodian*, *trustee*) with definitions.
2. **Glossary sweep.** Entries for *creature, living being, grown* → rename/redirect/remove. Add entries for *emergent property, custodian, trustee* if absent.
3. **Topic-guide reconciliation.** ~50 broken refs noted in S54 handoff — fix in conjunction with glossary sweep.
4. **Popup alignment check.** Spot-read 10 of 48 popups; if ≥2 carry the old framing, full sweep. Else sample-only.

**Acceptance:**
- No dangling `\hovertip{}` anchors anywhere in manuscript.
- Glossary has no entries that contradict p2's framing.
- Topic-guide broken-refs count = 0.
- Popups sampled or swept; all aligned.

### 0170d — Continuous discipline audit (no commit, just a check)

**Scope:** Post-sweep verification that three-possibilities discipline (A/B/C never privileged in prose) survived the rewrite.

**Method:** Random sample of 8 chapters (2 per Z-layer + 2 Guardian interludes). For each, score: "does this chapter remain compatible with A (fantasy), B (exaggerated kernel), and C (substantially true)?"

**Acceptance:** 8/8 compatible. Any chapter that drifted into ontological commitment during the sweep gets a targeted edit (recorded as a 0170a follow-up commit).

## Re-engagement test (whole-book sample)

After 0170a + 0170b + 0170c land:

**Sample four chapters for 10-persona Tier-0 scoring (stratified, Generator picks from eligible lists):**
1. One A-spine chapter (pop-science register) — Generator picks from A-spine chapter list; Bruce may override.
2. One Guardian interlude — Generator picks from the 7 interludes.
3. One Record memoir chapter — Generator picks; prefer one with preserved testimony to stress-test the voice rule.
4. One topic-guide entry — Generator picks; prefer an entry on a reframed term (e.g., *emergent*, *custodian*, *trustee*).

Generator states its picks in the report so Bruce can veto and request re-sampling.

Use the same 10-persona panel inlined in Plan 0169 Part E.

**Pass criterion:** 0 bounces across 4 × 10 = 40 cells. Yellow zones ≤ 5 total. If any regresses, targeted fix + re-sample.

**Why 4 chapters not all 37:** cost. Sampling gives strong signal; full coverage is not worth the token/time budget at this stage. If sampling passes, the framing is consistent; if it fails, the failures will point to which sub-plan has a gap.

## Dependencies and ordering

```
0169 (p1/p2 port) ──▶ Discovery phase (grep + report + escalation if over threshold)
                              │
                              ▼
                     0170a (prose sweep, Z-layer 1/2/3)
                              │
                              ├──▶ 0170b (internationalization, conditional) — must follow 0170a Phase 1
                              │                                                (Guardian interludes) so int'l thread
                              │                                                lands on reframed prose
                              │
                              └──▶ 0170c (hovertips/glossary/popups) — must follow 0170a
                                                                       Phases 1-3 to know which
                                                                       anchors were renamed
                                   │
                                   ▼
                          0170d (discipline audit) ──▶ re-engagement sample
```

0170a runs first. 0170b and 0170c can run in parallel *after* 0170a completes the relevant Z-layer (0170b after Phase 1, 0170c after all three). 0170d and re-engagement wait for all three.

## Rollback

Each sub-plan commits per-chapter or per-group. Rollback is per-commit via `git revert`. No global rollback needed — sub-plans are designed to be revertable in pieces.

Baseline tag for 0170 as a whole: tag `post-0169-pre-0170` at the commit where 0169 Phase 3 lands. Push to origin.

## Out of scope

- Adding new chapters.
- Rewriting chapters for reasons unrelated to p2 framing propagation.
- Reading-level changes (p3 remains unconstrained).
- SVG / figure asset edits (separate concern; figure *captions* are in scope under 0170a).
- Translation / localization work (separate plan if pursued).
- Sweetspot Phase 2 real-API runs (separate: recovery plan Step 2).

## Handoff note

This plan is a spec. Execution happens via 0170a/b/c/d. Each sub-plan is Generator-shell work with its own handoff prompt, written when 0169 lands and Bruce has made the internationalization call.

## Open questions (for Bruce, before sub-plans are written)

1. **Internationalization scope.** Do #1 (historical precedents) and #2 (secular framing) land in p2 during 0169, or get deferred to 0170b? Answer determines whether 0170b runs.
2. **Voice-preservation rule.** Agree with "narration rewrites; testimony preserves with optional gloss"? Or stricter/looser?
3. **Re-engagement sample size.** 4 chapters enough, or sample 8? 4 is my 30%-thread recommendation; 8 is the conservative call.
4. **Sub-plan ordering.** Parallel (my default) or serial? Parallel is cheaper; serial is safer if sub-plans might step on each other.
