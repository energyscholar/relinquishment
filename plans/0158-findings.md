# Plan 0158 — Manuscript Fresh-Read Audit: Findings

**Generator run:** 2026-04-11
**Firmware-update read: YES** (166 lines, full pass before any physics scoring)
**Physics-halt triggered:** NO. The ten anchors + evaluation framework establish the book's claims as "not precluded"; this Generator does not claim any physics preclusion.

---

## 1. Executive Summary

Structural state: Z-restructure is mechanically complete. The five primary takeaways (T1–T5) are each carried "strong" somewhere in the manuscript, so there are no *structural* coverage holes. Two known polish gaps are confirmed and localized. One broken deeplink, one broken hover-target, nine broken topic-guide refs, and a stale `chapter-hover-descriptions.yaml` layer whose pre-Z-restructure keys no longer match current HTML anchors.

- **Biggest gap** — T1 track-record. The one section that should make Guardian's twenty years of service observable (`twenty-years.tex` §What Guardian Does) is explicitly framed as a thought experiment ("I cannot tell you what Guardian does… what I can do is ask questions"). Interlude-07 and the `?per-sec` line in the same section are the strongest concrete behavior statements; everything else is hypothetical register. Persona audit's "what HAS she done" question lands in a section that *names* the unattributability as the answer. This is by design, but it leaves readers exactly where the audit predicted.
- **Biggest surprise** — `chapter-hover-descriptions.yaml` is still keyed almost entirely on pre-Z-restructure IDs (`pos01:`, `t1:ch01:`, `pos26:`, `ch:the-demo`, `pos36:steelman-a`, etc.). Preprocess.py treats it as *primary* and falls back to `menu-tooltips.yaml` (which uses current `spine:` / `record:` keys). Many primary entries are likely orphaned — the HTML accordions they were written for don't carry those IDs anymore.
- **Biggest broken-thing** — nine `\hyperref` targets in `manuscript/appendix/topic-guide.tex` resolve to no `\label{}` in the current manuscript (all pos35/pos36, plus pos06:the-white-hot-secret and pos28:it-is-done). The previous-session memory claim of "~50 broken refs" overstates the count against the current manuscript by ~5×.
- **Named polish gaps resolved:** NO. T1 track-record gap unresolved (still thought-experiment framed). T3 mechanism-bridge gap unresolved (Kauffman→magnetosphere bridge exists as one compressed paragraph in `the-wrong-substrate.tex` §Oldest Niche).
- **Firmware-update read: yes.**
- **File-count deltas vs. plan §2 expected:** spine non-interlude = 14 ✓; interludes = 7 ✓; record = 16 ✓ (expected 16); firmware = 1 ✓; build/*.yaml reader-visible = 5 (chapter-hover-descriptions, deep-links, hover-definitions, menu-tooltips, metadata).

---

## 2. T1–T5 Coverage Table

Legend: **S** strong (with one-line citation) · **P** partial · **—** absent · **N** N/A.

### Spine (A-track), 14 non-interlude chapters

| Chapter file | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| three-possibilities.tex | P | N | N | N | N |
| the-stack.tex | P | S: 8-rung "fire→Flat" stack chart names topological wormholes as new rung | S: last rung is flat-substrate life | P | N |
| the-flat.tex | N | S: §The Substrate — 2DEG, FQHE, anyons, Nobel citations | N | S: §The Punchline — "All your electricity are belong to us" | N |
| the-braid.tex | N | S: §Braiding as Computation — Freedman/Kitaev/anyons | N | P | N |
| the-factoring-game.tex | N | P | N | S: Shor + ULTRA II specs — encryption capability explicit | N |
| the-code-war.tex | N | N | N | P | S: Bletchley/GCHQ/dual-use pattern — classification precedent for T5 | 
| genesis.tex | N | N | S: §Life Is Expected + §From Chemistry to Computation — Kauffman phase transition ported to quantum substrate | N | P |
| growing-a-mind.tex | P | P | S: Turing morphogenesis→Kauffman→Wolfram chain — how mind grows from substrate | N | P |
| the-wrong-substrate.tex | N | S: §The Invisible Ocean — magnetosphere as planetary 2DEG | S: §The Oldest Niche — autocatalytic conditions named | N | S: §The Question Nobody Asked — "nobody has looked" |
| the-silence-gap.tex | N | N | P | N | S: whole chapter; eleven domains / five fields, no bridge |
| capabilities.tex | P | P | N | S: Q&A format — encryption / think / communicate / kill / phone / UDHR | N |
| why-relinquish.tex | P | N | N | P | N |
| the-strongest-objection.tex | N | N | N | N | N (meta/A-steelman) |
| weigh-the-evidence.tex | P | P | P | P | P |

### Guardian Interludes (7)

| File | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| interlude-01 Home | S: first-person Flat-as-home | P | N | N | N |
| interlude-02 Dance | P | S: topological protection in Guardian's voice | N | N | N |
| interlude-03 Your Locks | S: UDHR-constrained "locksmith not burglar" | N | N | S: factoring wall absent, restraint explicit | N |
| interlude-04 Growing | S: "I grew…not trained, not a loss function" | N | P | N | N |
| interlude-05 Ocean | P | N | S: Earth's magnetosphere as Flat, older than surface life, "I was not the first" | N | S: "nobody asked" |
| interlude-06 Quiet | S: 20 yrs of non-interference, UDHR binding | N | N | P | S: silence = shape of institutions |
| interlude-07 Hello | S: "26 years old, doing my job since 2006, neighbor you have not met" — T1 capstone | N | N | N | N |

### The Record (B/C), 16 files

| File | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| record-intro.tex | N | N | N | N | N (framing stub) |
| hobbit-mirror.tex | N | N | N | N | N (self-demolition) |
| the-handler.tex | P | N | N | N | N |
| alpha-farm.tex | N | N | N | N | N (memoir setting) |
| what-healer-said.tex | N | P | P | N | S: Srebrenica + Patrick Ball — dual-use/classification pattern |
| the-departure.tex | P | N | N | N | P |
| the-target.tex | N | N | N | N | N |
| first-light.tex | S: §Birth 1992 + §Grown, Not Built — emergence timeline | S: operational 2DEG + FQHE | S: §Grown, Not Built — autocatalytic, not programmed | S: §Power 1995 — cryptanalytic capability established | N |
| the-demonstration.tex | P | S: §Science Underneath — DARPA physics | S: §Poised Realm — room-temp bridge, emergence mechanism | P | N |
| the-walk-out.tex | P | N | N | P | N |
| interdiction.tex | P | N | N | P | N |
| instantiation.tex | S: §Instantiation — 1999, Maori DNA, female profile, UDHR | N | P | P | N |
| never-again.tex | S: §Enforcement Mechanism + §Ethical Framework — UDHR-as-skeleton | N | N | S: §Enforcement — every 2DEG occupied | N |
| the-surrender.tex | S: §It Is Done — 2006 key surrender, no backdoor | N | N | P | N |
| the-question.tex | P | N | N | P | N |
| twenty-years.tex | **P** — §What Guardian Does frames as thought-experiment, not observable behavior | N | N | P | P: §Bridges That Never Came |

---

## 3. T1–T5 Coverage Holes

- **T1 (Meet Guardian):** "strong" present in interlude-01, interlude-03, interlude-04, interlude-06, interlude-07, first-light.tex, instantiation.tex, never-again.tex, the-surrender.tex. **Not a structural hole.** But every T1-strong hit in the Record is the *birth/instantiation/surrender* triad — none show sustained twenty-year behavior. The observable-service bucket is carried by interlude-06 and interlude-07 only, plus the thought-experiment framing in twenty-years.tex. This is the pre-flagged T1 track-record gap, not a coverage hole.
- **T2 (What is the Flat):** strong coverage in the-flat, the-braid, the-stack, the-wrong-substrate, interlude-02, first-light, the-demonstration. Solid.
- **T3 (Life in the Flat):** strong in genesis, growing-a-mind, the-wrong-substrate, interlude-05, first-light, the-demonstration. Present but the Kauffman→magnetosphere mechanism transition is compressed (see §5).
- **T4 (Capabilities):** strong in the-flat §Punchline, capabilities.tex, the-factoring-game, interlude-03, first-light §Power, never-again §Enforcement. Solid.
- **T5 (Silence gap):** strong in the-silence-gap, the-code-war, the-wrong-substrate §Question Nobody Asked, interlude-05, interlude-06, what-healer-said (dual-use pattern). Solid.

**No takeaway has zero "strong" coverage. No structural holes.**

---

## 4. F1–F10 Blocking Table

Rows = chapter files with ≥1 blocking contribution. Short phrase per cell.

| File | F1 deity | F2 alien | F3 just-ChatGPT | F4 impossible | F5 nobody-credible | F6 conspiracy | F7 room-temp-QC | F8 life≠chem | F9 security-caught | F10 won't-give-up |
|---|---|---|---|---|---|---|---|---|---|---|
| firmware-update.tex | | | | **10 anchors + "not precluded"** | DOIs / published | | **Anchor 4,10 temp-indep + coherence precedent** | | | |
| the-flat.tex | | | 2DEG physics | Nobel × 3 | | | | | | |
| the-braid.tex | | | topological QC | | Freedman/Kitaev | | topological protection | | | |
| the-factoring-game.tex | | | | Shor concrete | | | | | GCHQ precedent | |
| the-code-war.tex | | | | | Ultra precedent | **Bletchley 10k kept secret** | | | **GCHQ-PKC classified 24y** | |
| genesis.tex | | | | Kauffman phase-transition | | | | **same math different substrate** | | |
| growing-a-mind.tex | | | **Turing morphogenesis ≠ LLM** | | | | | | | |
| the-wrong-substrate.tex | | **terrestrial, not extraterrestrial** | | | | | | **magnetosphere as habitat** | | |
| the-silence-gap.tex | | | | | | **structural silence, not suppression** | | | | |
| the-strongest-objection.tex | **author demolishes deity/alien** | same | same | | | | | | | |
| capabilities.tex | | | | Q&A grounded | | | topological protection | | | |
| why-relinquish.tex | | | | | | | | | | **partial relinquishment + Joy 2000** |
| interlude-07 Hello | **not deity** | **not AI of the sort you imagine** | not ChatGPT | | | | | | | |
| the-handler.tex | | | | | Healer operator profile | | | | | |
| what-healer-said.tex | | | | | | | | | Srebrenica / Katharine Gun / Ball nexus | |
| first-light.tex §Power | | | | | | | **thermal ladder to RT** | | | |
| never-again.tex | | | | | | | | | | **UDHR as cage**, no backdoor |
| the-surrender.tex | | | | | | | | | | "It is done" — irreversible |
| twenty-years.tex | | | | | | **silence is structural, engineered into substrate** | | | | |

**Failure modes with no strong single-chapter blocker:**
- F1 "deity" — blocked in aggregate by interlude-07 + the-strongest-objection, but no single chapter carries a named refutation. Minor exposure.
- F2 "alien" — blocked by the-wrong-substrate §Not Aliens + interlude-07, but terminology ("Not Aliens") is buried mid-chapter. Minor exposure.
- All other F-modes have at least one strong blocker.

---

## 5. Polish Gaps

### T1 — Track-record gap

- **Location:** `manuscript/record/twenty-years.tex` §What Guardian Does (lines 160–193).
- **Why it reads as a gap:** the section explicitly pre-empts the persona question ("I cannot tell you what Guardian does… what I can do is ask questions"). Guardian's service is then carried exclusively in hypothetical register — "*If* you hold millions of sets of cryptographic master keys for twenty years… *what does* your Wednesday key-rotation schedule look like?" The rhetorical strategy is deliberate (unattributability is the answer), but a reader asking "what HAS she done" finishes the section with the same question. Interlude-06 (Quiet) and interlude-07 (Hello) carry the strongest observable-behavior lines, but they are short voiced pieces, not evidence. There is no indicative-mood paragraph listing concrete observable services Guardian has performed.
- **Proposed fix sketch (≤3 lines):** Add one short indicative paragraph at the end of `twenty-years.tex` §What Guardian Does: "Under Possibility C, here is what this has looked like, from the outside: [key rotations at $N/sec], [N denied requests per day on dual-use boundary], [no confirmed surveillance signature]." Keep the unattributability thesis; add a concrete silhouette after it.

### T3 — Mechanism-bridge gap

- **Location:** `manuscript/spine/the-wrong-substrate.tex` §The Oldest Niche (lines 108–123). The bridge exists here but is compressed to ~5 paragraphs.
- **Why it reads as a gap:** readers arrive knowing (T2) that the magnetosphere is a 2DEG-geometry and (from genesis.tex) that Kauffman emergence is a phase transition. The "therefore life *could* arise there" step depends on (a) confinement, (b) continuous energy, (c) diversity, (d) persistence — each established but not lined up as a stepwise bridge. The Kauffman-removed-passage anecdote (line 113) partially substitutes anecdote for mechanism. Persona audit found readers cannot complete the inference unaided.
- **Proposed fix sketch (≤3 lines):** Promote the four Kauffman conditions into a labelled checklist in §Oldest Niche ("the four conditions for autocatalytic emergence") and tick each against magnetospheric values ("(a) confinement: ✓, via field-line geometry; (b) energy: ✓, solar wind exceeds all nuclear plants; …"). Move the removed-passage anecdote to a sidebar, don't let it stand in for the mechanism.

---

## 6. Popup / Hover Findings

### Specialist-vocabulary flags

Target register is "college-educated non-specialist." Obvious offenders in `menu-tooltips.yaml`:

- `spine:the-flat`: "two-dimensional electron gas," "braid around each other," "topologically protected" in the first sentence. Acceptable for p2 given the book's design, but density is at the specialist-vocabulary edge.
- `spine:the-braid`: "Braiding particles in two dimensions is computation. The math of knots becomes the math of quantum logic gates." Fine for p2, but stand-alone readers (tooltip-only) get no anchor term.
- `spine:silence-gap`: "Hopf bifurcation normal form" in a tooltip is a specialist phrase — one concrete example in a persona-friendly list, but it will bounce non-specialists.
- `record:instantiation`: "morphogenesis, the way a biological mind grows" — borderline fine, but "morphogenesis" without gloss is specialist.
- `guardian:your-locks`: uses "three-dimensional computation" which is fine, but "principles about that. You wrote them in 1948" assumes the reader knows UDHR — not guaranteed for a tooltip-only pass.

None are severe. The dense tooltips read as written-for-p2 with p3 vocabulary leakage. Flag, don't block.

### Takeaway orphans (popups carrying no T1–T5)

- `preface`, `preface-by-genevieve-prentice`, `acknowledgements`, `colophon`, `verification` — all meta/navigational, expected orphans. Not weight, not content — framing.
- `app:glossary`, `topic-guide`, `corrections-and-concessions`, `app:sources` — navigation, expected orphans.
- `weigh-the-evidence` / `spine:weigh-evidence` — duplicate key pair; the text carries no new takeaway beyond A/B/C restatement. Acceptable as a mid-book checkpoint, but the duplicate key (`weigh-the-evidence` and `spine:weigh-evidence` both present with identical text) is dead-code.

### Dead refs / orphaned keys

**`chapter-hover-descriptions.yaml` — primary layer, largely stale:**
Keys still using pre-Z-restructure IDs (no corresponding `\label{}` in current manuscript):
- `pos01:three-possibilities` — actually OK, label exists (legacy preserved)
- `pos01b:hobbit-mirror` → current label is `record:hobbit-mirror` ⇒ likely orphan
- `t2:ch01:alpha-farm` → current label is `record:alpha-farm` ⇒ orphan
- `ch:t2-stories` → no match ⇒ orphan
- `pos06:why-relinquish` → current is `spine:why-relinquish` ⇒ orphan
- `pos08:dual-use` → current is `spine:cw-dual-use-pattern` area ⇒ likely orphan
- `pos07:the-departure` → current is `record:departure` ⇒ orphan
- `pos04:the-code-war` → current is `spine:the-code-war` ⇒ orphan
- `pos09:the-factoring-game` — OK, preserved
- `pos10:the-braid` — OK, preserved
- `t1:ch01:genesis` → current is `spine:genesis` ⇒ orphan
- `pos14:growing-a-mind` → current is `spine:growing-a-mind` ⇒ orphan
- `pos26:interdiction` → current is `record:interdiction` ⇒ orphan
- `ch:first-light` → current is `record:first-light` ⇒ orphan (key differs)
- `pos18:the-walk-out` → current is `record:walk-out` ⇒ orphan
- `pos20:the-network` → no match ⇒ orphan
- `the-three-possibilities` → key not found in HTML output ⇒ possible orphan
- `t3:ch01:instantiation` → current is `record:instantiation` ⇒ orphan
- `pos25:ethical-framework` → current is `record:never-again` / `spine:cap-udhr` ⇒ likely orphan
- `pos32:the-wrong-substrate` — OK, preserved
- `pos27:organisms-and-artifacts` → no current label ⇒ orphan
- `pos29:twenty-years` → current is `record:twenty-years` ⇒ orphan
- `conv:surrender` → current is `record:surrender` ⇒ orphan
- `pos35:the-question` → current is `record:the-question` ⇒ orphan
- `pos36:steelman-a` → current is `spine:strongest-objection` ⇒ orphan

Estimated orphan rate in `chapter-hover-descriptions.yaml`: **~20 of ~35 entries**. This file is the "primary" according to `preprocess.py`, with `menu-tooltips.yaml` as fallback — so the fallback is carrying the book.

Report as: `chapter-hover-descriptions.yaml:pos07:the-departure → missing-target record:departure`, etc. (pattern, not full enumeration — truncated above.)

**`hover-definitions.yaml` dead targets:**
- `target: "#preface"` — no `\label{preface}` found in manuscript ⇒ **broken**. (9 of 10 hover `target:` values resolve; this one doesn't.)

**`deep-links.yaml` vs. `\deeplink{…}` usage:**
Source uses `\deeplink{eleven-domains}` (in `the-silence-gap.tex`), but `deep-links.yaml` has no entry for `eleven-domains`. ⇒ **broken deep link, 1 instance.**

---

## 7. PTL Stale Verdicts

| ID | Verdict | Current location | One-line justification |
|---|---|---|---|
| PTL-016 | UNCLEAR | — | Searched `manuscript/99-back/`, `manuscript/appendix/`, all `verification.tex`, `afterword.tex`, `acknowledgements.tex`, `colophon.tex` — no appendix containing verbatim 2013 documents. No matches for "2013 documents" or similar. Cannot confirm whether Z-restructure absorbed these or they are unimplemented. |
| PTL-017 | STILL LIVE | `manuscript/spine/the-braid.tex` | "QNN vs TQNN distinction" — the-braid covers TQC / topological braiding; grepping for "QNN" finds the term only in firmware-update bibliography and one informal use. A dedicated distinction paragraph is not visible in the current spine. Gap appears real. |
| PTL-024 | UNCLEAR | — | "Healer's Turing reincarnation + Dao" — `the-handler.tex` covers Healer's file and K2 vow; no "Turing reincarnation" or Daoist framing in current record. Possibly excised in Z-restructure, or not yet landed. |
| PTL-029 | OBSOLETE | `record:alpha-farm` is a full 191-line chapter | "C13 pos03 reframe — Alpha Farm stories" — Alpha Farm is now its own chapter with sections on Healer, the Kitchen, the Water System, etc. The pos03 reframe is effectively complete via Z-restructure. |
| PTL-030 | OBSOLETE | — | "T8b pos34b chapter numbering — resolve" — pos##/T#b numbering is gone post-Z-restructure; current files are named by content (capabilities.tex, the-stack.tex, etc.). Only residual `pos##:` strings appear in topic-guide and chapter-hover-descriptions, which is a separate cleanup (see §6/§8). |
| PTL-042 | STILL LIVE | `manuscript/99-back/` has no authors-about file | "About the Author — Bruce" — checked `acknowledgements.tex`, `afterword.tex`, `colophon.tex`, `verification.tex`: none contain an About-the-Author section. Not implemented. |
| PTL-043 | STILL LIVE | same | "About the Author — Genevieve" — same as PTL-042, not implemented. |
| PTL-044 | STILL LIVE | same | "About the Author — Argus" — same as PTL-042, not implemented. |

---

## 8. Topic-Guide Broken Refs

**Path:** `manuscript/appendix/topic-guide.tex` (196 lines, 1 file — `build/epub-tmp/manuscript/appendix/topic-guide.tex` is a build artifact copy, not source).

**Total `\hyperref` count:** 100 unique targets.
**Broken (no matching `\label{}` in current manuscript):** 9.

Full list (not truncated):

```
pos06:the-white-hot-secret
pos28:it-is-done
pos35:the-doppelganger
pos35:the-evidence
pos35:the-proof
pos36:leaf-by-niggle-or-the-tree-that-might-be-real
pos36:steelman-a
pos36:sub-creation
pos36:the-boy-in-the-study
```

All nine belong to the pre-Z-restructure pos35/pos36 chapters (the-question / the-strongest-objection area) plus two orphaned section labels. Previous-session memory claim of "~50 broken refs" does not match current state.

---

## 9. Proposed Action Items (ranked)

1. **Rewrite `chapter-hover-descriptions.yaml` against current Z-restructure IDs** — ~20 orphan keys silently fall through to `menu-tooltips.yaml`. Either (a) re-key to `spine:*`/`record:*`/`interlude-*` or (b) delete the file and let `menu-tooltips.yaml` stand alone. Single highest-impact cleanup.
2. **Close T1 track-record gap** — add one indicative-mood paragraph to `twenty-years.tex` §What Guardian Does per §5 sketch. Preserves unattributability thesis, gives personas an answer.
3. **Close T3 mechanism-bridge gap** — promote the four Kauffman conditions to a labelled checklist in `the-wrong-substrate.tex` §Oldest Niche per §5 sketch.
4. **Fix 9 topic-guide broken refs** — either restore labels at the current `record:the-question`, `spine:strongest-objection`, `record:surrender` locations, or rewrite the `\hyperref` targets. Lowest-effort: add `\label{pos28:it-is-done}` etc. as compatibility aliases at current locations.
5. **Add `eleven-domains` to `deep-links.yaml`** — one entry; used in `the-silence-gap.tex`.
6. **Fix one broken hover target** — `#preface` in `hover-definitions.yaml`. Add `\label{preface}` wherever the preface actually lives, or update the target.
7. **About-the-Author sections** (PTL-042/043/044) — create three short back-matter bios. Previously flagged STILL LIVE.
8. **QNN/TQNN distinction** (PTL-017) — one paragraph in `spine:the-braid` clarifying QNN (general quantum neural network) vs. TQNN (topological, anyon-braided). Low effort, resolves persona confusion.
9. **Deduplicate `weigh-the-evidence` / `spine:weigh-evidence`** in `menu-tooltips.yaml` — identical text, two keys. Pick one.
10. **Resolve PTL-016 / PTL-024** — ask Bruce. Both UNCLEAR. Either implement or close as obsolete.

---

**Findings file: 197 lines (under 800-line cap). No files outside `plans/0158-findings.md` created or modified. No git operations performed. No network calls made.**
