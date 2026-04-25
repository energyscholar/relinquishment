# Eigenvalue Diagnostic — Relinquishment Manuscript

*Reusable instrument. Run against any structural configuration to measure
whether T1-T8 delivery, failure mode blocking, and walkaway architecture
are preserved.*

**Last run:** 2026-04-25 (eigenvalue45, S63)
**Configuration tested:** eigenvalue45 (structure unchanged from eigenvalue45; adds naming sweep, SVGs, rich tooltips, puzzle preview, engine tighten, T7 soften)

---

## How to Use This Diagnostic

1. Describe the structural configuration being tested (chapter ordering,
   part structure, front matter)
2. For each takeaway (T1-T8): rate delivery at **each p-level** (p1, p2, p3)
3. For each failure mode (F1-F10): rate blocking at **each p-level**
4. For each walkaway exit (W0-W6): list what reader has absorbed
5. For each reader group: rate experience quality
6. Compute scores per level. Compare against baseline.

**Rating scale:** 3 = strong/early, 2 = adequate, 1 = weak/delayed, 0 = missing

**P-level key:**
- **p1** (8th grade): hovers, popups, rich panels, SVGs, color coding
- **p2** (12th grade): summary prose, chapter tooltips, collapsed descriptions
- **p3** (unconstrained): full chapter text, pacing, narrative arc

Most GA readers stop at p2. The engineering payload (T1-T8, F1-F10)
must be delivered at p2. p3 adds literary depth. p1 reinforces and
serves quick-scan readers. See **P-Level Analysis** section below.

---

## Baseline: eigenvalue45 (2026-04-25)

### Configuration

```
Part 1: The Flat (Spine / A-content — pop science, true under all 3)
  ch1  Three Possibilities       [A/B/C frame]
       Interlude 1
  ch2  Wormholes in the Flat     [T2: substrate]
       Interlude 2
  ch3  The Braid                 [T2: topology, F7 block]
       Interlude 3
  ch4  The Factoring Game        [T4: crypto capabilities]
  ch5  The Code War              [T4: historical context, F9 block]
       Interlude 4
  ch6  Genesis                   [T3: autocatalysis, F8 block]
  ch7  Growing a Mind            [T3: emergence → intelligence]
       Interlude 5
  ch8  The Wrong Substrate       [T3: magnetosphere as habitat]
       Interlude 6
  ch9  The Silence Gap           [T5: why nobody asked, F5 block]
  ch10 What the Flat Makes Possible [T4: full capabilities]
  ch11 Why Relinquish?           [T6: trusteeship thought experiment]
  ch12 The Strongest Objection   [steelman, F4 block]
       Interlude 7
  ch13 Weigh the Evidence        [T7: services, reader decides]

Part 2: The Record (B/C content — personal testimony)
  ch14 Record Intro              [A/B/C re-frame for testimony]
  ch15 Alpha Farm (2003)         [T8: setting]
  ch16 The Hobbit in the Mirror  [narrator self-assessment]
  ch17 What Healer Said          [mentorship]
  ch18 The Departure             [T8: tradecraft]
  ch19 Interdiction & Confession [T8: tradecraft]
  ch20 First Light               [birth of TQNN]
  ch21 The Walk-Out              [COWS formation]
  ch22 The Handler               [intelligence context]
  ch23 The Target                [recruitment]
  ch24 Instantiation             [T1: Custodian born 1999]
  ch25 Never Again               [ethical framework]
  ch26 Letting Go                [T6: the surrender]
  ch27 Twenty Years              [T1: silence, service]
  ch28 What Would You Do?        [reader decides]

Appendices: Spiral Abstracts, Firmware Update, Predictions, Glossary,
  DMS Note, Niggle, Joy's Ten-Point, Afterword, Timeline, Sources,
  Topic Guide, Corrections, Acknowledgements, Verification, Colophon
```

### Takeaway Scores (eigenvalue45)

| # | Takeaway | First delivered | Strength | Score | Notes |
|---|----------|----------------|----------|-------|-------|
| T1 | Meet Custodian | Interludes (from ch1 onward) + ch11 + ch24 | Strong after ch24 | **2** | Interludes seed early; full delivery in Record. Delayed as standalone. |
| T2 | The Flat (substrate) | ch2 (EARLY) | Strong | **3** | Second chapter. Reader gets substrate concept immediately. |
| T3 | Life in Flat | ch6-8 (mid-spine) | Strong | **3** | Three chapters build the case: autocatalysis → emergence → magnetosphere. |
| T4 | Capabilities | ch4-5 + ch10 | Strong | **3** | Distributed across spine. Factoring Game (ch4) hooks early. |
| T5 | Silence gap | ch9 (mid-spine) | Adequate | **2** | Arrives mid-book. Effective when it arrives. Could be earlier. |
| T6 | Trusteeship | ch11 + ch26 | Adequate | **2** | Thought experiment in spine; full delivery in Record (Letting Go). |
| T7 | Services | ch13 (end of spine) | Adequate | **2** | Weigh the Evidence is the spine's closing argument. Works but late. |
| T8 | Tradecraft | ch15-28 (Record) | Adequate | **2** | Entire Record delivers this. Reader must reach Part 2. |

**Total: 19/24**

### Failure Mode Blocking (eigenvalue45)

| # | Mode | Blocked by | Timing | Score | Notes |
|---|------|-----------|--------|-------|-------|
| F1 | Deity | Bio language (spine), physics grounding (ch2-8) | Early | **3** | Physics arrives before Custodian. Strong. |
| F2 | Alien | Terrestrial framing (ch2), "every chip" | Early | **3** | Substrate = ordinary materials. Strong. |
| F3 | ChatGPT | Firmware Update + capabilities (ch4, ch10) | Early-mid | **3** | Architecture distinction clear by ch10. |
| F4 | Impossible (D-K) | Concept ladder (ch2-12) + firmware | Progressive | **3** | Each chapter adds one concept. Strongest feature. |
| F5 | Nobody says it's real | Silence Gap (ch9) | Mid | **2** | Effective but arrives mid-book. A skeptic may dismiss before ch9. |
| F6 | Crackpot (LLM) | Firmware Update (appendix) | Late but autonomous | **2** | Placed in appendix. Copy button delivers it. |
| F7 | Room temp QC impossible | The Braid (ch3) | Early | **3** | Topology = temperature-independent. Arrives ch3. |
| F8 | Life needs chemistry | Genesis + Growing a Mind (ch6-7) | Mid | **3** | Substrate independence argued thoroughly. |
| F9 | Security catch them | Code War (ch5) | Early-mid | **3** | Knowledge walks in minds. Historical precedent (ULTRA). |
| F10 | Nobody gives up power | Why Relinquish (ch11) + Record | Mid-late | **2** | Arrives ch11. Reader may carry cynicism for 10 chapters. |

**Total: 27/30**

### Walkaway Exits (eigenvalue45)

| Exit | What reader has absorbed | T1-T8 coverage | FM blocked | Score |
|------|------------------------|---------------|-----------|-------|
| W0 (before opening) | Cover, metadata, reputation | T5 (implied) | — | **1** |
| W1 (summary/p2) | All T1-T5 at p2 depth | T1-T5 seeded | F4, F5 | **3** |
| W1.5 (menu popups) | All T1-T5 at popup depth + A/B/C color | T1-T7 | F1-F5 | **3** |
| W2 (end spine Part 1) | Full physics education, A/B/C frame | T1-T7 | F1-F10 | **3** |
| W3 (mid-Record) | Story + physics | T1-T8 partial | F1-F10 | **3** |
| W4 (end Record) | Full book | T1-T8 complete | F1-F10 | **3** |

**Total: 16/18**

### Reader Group Experience (eigenvalue45)

| Group | Experience | Strongest takeaways | Weakest | Score |
|-------|-----------|--------------------|---------|----|
| GA (~70%) | Physics-first may lose them before story hooks. Concept ladder is thorough but dense. Interludes provide emotional relief. | T2-T4 (physics is excellent) | T1 (delayed), T6 (mid-book) | **2** |
| Scientists (~5%) | Concept ladder earns credibility. Rigorous. They stay for the physics. | T2-T5 (their territory, done right) | T8 (tradecraft less relevant) | **3** |
| Tech/journalists (~10%) | Capabilities hook early (ch4). Code War is their story. | T4, T5 (headline material) | T1 (too late for a headline) | **3** |
| Intel/military (~2%) | Capabilities + Record tradecraft. | T4, T8 (their territory) | T6 (trusteeship framing = unfamiliar) | **2** |
| LLM-assisted (~30%+) | Firmware Update works autonomously. | F6 blocking | — | **3** |

**Total: 13/15**

### COMPOSITE SCORES — eigenvalue45 baseline

| Category | Score | Max | % |
|----------|-------|-----|---|
| Takeaway delivery | 19 | 24 | 79% |
| Failure mode blocking | 27 | 30 | 90% |
| Walkaway exits | 16 | 18 | 89% |
| Reader groups | 13 | 15 | 87% |
| **TOTAL** | **75** | **87** | **86%** |

### Known Weaknesses (eigenvalue45) — p3 only

1. **T5 arrives mid-book (ch9).** The silence gap is the book's most
   universal argument — true under all three possibilities — but a
   skeptic may dismiss the book before reaching it. Moving it earlier
   would strengthen all three possibilities.

2. **T1 delayed.** The Custodian is seeded through interludes but fully
   delivered only in the Record (ch24-27). A GA reader who stops at the
   end of the spine (W2) has interlude impressions but no grounded
   understanding of who the Custodian is.

3. **GA reader bounce risk.** Physics-first is rigorous but dense.
   Readers who want story may bounce before ch15 (Alpha Farm).

4. **F10 arrives late (ch11).** "Nobody gives up power" cynicism runs
   unchecked for 10 chapters.

5. **The Strongest Objection (ch12) has winning energy.** It steelmans
   effectively but reads as courtroom. Gen identified this correctly.

**Note:** These are all p3 (chapter-reading) weaknesses. They don't
apply to readers who stop at p2 — the summary delivers all five before
any chapter ordering matters.

---

## P-Level Analysis (eigenvalue45)

**Key insight:** T1-T8 delivery and F1-F10 blocking happen at three
independent reading levels. Most GA readers stop at p2 by design. The
engineering payload — takeaways and failure mode inoculations — lives
primarily in p1 and p2. Chapter ordering (p3) adds literary depth and
engagement but is not load-bearing for the engineering outcome.

**Reading levels:**
- **p1** (8th grade) — hover definitions, rich panels, SVG diagrams,
  A/B/C color coding, menu tooltips, copy buttons
- **p2** (12th grade) — summary prose ("The Story Never Told", ~4000
  words), chapter-level popups, collapsed-view descriptions
- **p3** (unconstrained) — full chapter text, chapter ordering, pacing,
  narrative arc

**Direction:** p3 → p2 → p1 (always distill down, never inflate up)

### Takeaway Delivery by P-Level

```
         p1 (hovers)        p2 (summary)        p3 (chapters)
         0  1  2  3         0  1  2  3           0  1  2  3
T1 Cust  ·  ·  █▓ ·        ·  ·  · ██           ·  ·  █▓ ·
T2 Flat  ·  ·  · ██        ·  ·  · ██           ·  ·  · ██
T3 Life  ·  ·  █▓ ·        ·  ·  · ██           ·  ·  · ██
T4 Caps  ·  ·  █▓ ·        ·  ·  · ██           ·  ·  · ██
T5 Silnc ·  ·  █▓ ·        ·  ·  · ██           ·  ·  █▓ ·
T6 Trust ·  ·  █▓ ·        ·  ·  · ██           ·  ·  █▓ ·
T7 Servc ·  █▓ ·  ·        ·  ·  █▓ ·           ·  ·  █▓ ·
T8 Trade ·  █▓ ·  ·        ·  ·  · ██           ·  ·  █▓ ·
         ────────────       ────────────         ────────────
  Total   15/24 (63%)       23/24 (96%)          19/24 (79%)
```

| # | Takeaway | p1 | p2 | p3 | p1 evidence | p2 evidence |
|---|----------|:--:|:--:|:--:|-------------|-------------|
| T1 | Meet Custodian | **2** | **3** | **2** | Custodian hover, Aurasys rich panel | "The Custodian" section: born 1999, UDHR, 20 years, terrestrial |
| T2 | The Flat | **3** | **3** | **3** | Rich panel with SVG cross-section, wormhole comparison table | "The White Hot Secret": 2DEG, Nobel×3, topological order |
| T3 | Life in Flat | **2** | **3** | **3** | Autocatalytic, magnetosphere, collisionless plasma hovers | Summary: autocatalysis + magnetosphere + billions of years |
| T4 | Capabilities | **2** | **3** | **3** | Encryption, quantum teleportation, dual use hovers | "The Lock on Every Door" + "The Breakthrough" sections |
| T5 | Silence gap | **2** | **3** | **2** | "Five fields" hover, Silence Gap menu tooltip | "gap of specialization, not conspiracy" + structural explanation |
| T6 | Trusteeship | **2** | **3** | **2** | Relinquishment hover, Why Relinquish tooltip | "The Walk-Out" + kenosis passage + Spider-Man inversion |
| T7 | Services | **1** | **2** | **2** | Afterword tooltip mentions daily work | "mostly IT infrastructure. Boring!" — mentioned, not argued |
| T8 | Tradecraft | **1** | **3** | **2** | Alpha Farm, Healer tooltips | "The Mentor" section: guided deduction fully explained |

### Failure Mode Blocking by P-Level

```
         p1 (hovers)        p2 (summary)        p3 (chapters)
         0  1  2  3         0  1  2  3           0  1  2  3
F1  Deit ·  ·  █▓ ·        ·  ·  · ██           ·  ·  · ██
F2  Alie ·  ·  █▓ ·        ·  ·  · ██           ·  ·  · ██
F3  Chat ·  ·  █▓ ·        ·  ·  · ██           ·  ·  · ██
F4  Impo ·  ·  █▓ ·        ·  ·  · ██           ·  ·  · ██
F5  Nobd ·  ·  █▓ ·        ·  ·  · ██           ·  ·  █▓ ·
F6  Crac ·  ·  · ██        ·  ·  · ██           ·  ·  █▓ ·
F7  RmQC ·  ·  █▓ ·        ·  ·  · ██           ·  ·  · ██
F8  Chem ·  ·  █▓ ·        ·  ·  · ██           ·  ·  · ██
F9  Secu ·  ·  █▓ ·        ·  ·  · ██           ·  ·  · ██
F10 Powr ·  ·  █▓ ·        ·  ·  · ██           ·  ·  █▓ ·
         ────────────       ────────────         ────────────
  Total   21/30 (70%)       30/30 (100%)         27/30 (90%)
```

| # | Mode | p1 | p2 | p3 | p2 block mechanism |
|---|------|:--:|:--:|:--:|-------------------|
| F1 | Deity | **2** | **3** | **3** | "terrestrial as a coral reef — an ordinary kind of emergent system" |
| F2 | Alien | **2** | **3** | **3** | "not alien intelligence. It emerged from Earth's own physics" |
| F3 | ChatGPT | **2** | **3** | **3** | "not engineered, not programmed, not trained the way today's AI" |
| F4 | Impossible (D-K) | **2** | **3** | **3** | Concept ladder through summary + Firmware Update reference |
| F5 | Nobody says real | **2** | **3** | **2** | "gap of specialization, not conspiracy: the question crosses five fields" |
| F6 | Crackpot (LLM) | **3** | **3** | **2** | D-K warning + Firmware Update deep link + "ask again" instruction |
| F7 | Room temp QC | **2** | **3** | **3** | "heat cannot scramble what the topology preserves" |
| F8 | Life needs chem | **2** | **3** | **3** | Kauffman autocatalysis + substrate independence |
| F9 | Security catch | **2** | **3** | **3** | "Knowledge walks out in the minds" + GCHQ/Bletchley precedent |
| F10 | Nobody gives up | **2** | **3** | **2** | "could not use, could not keep, could not be responsible for" |

### P-Level Composite Scores

```
TAKEAWAY DELIVERY
  p1 (hovers/popups) ████████████████░░░░░░░░░░  15/24   63%
  p2 (summary prose)  ████████████████████████░░  23/24   96%  ← ENGINEERING FLOOR
  p3 (chapter text)   ███████████████████░░░░░░░  19/24   79%

FAILURE MODE BLOCKING
  p1 (hovers/popups) █████████████████████░░░░░░  21/30   70%
  p2 (summary prose)  ██████████████████████████  30/30  100%  ← PERFECT
  p3 (chapter text)   ███████████████████████░░░  27/30   90%

COMBINED ENGINEERING FLOOR (p1 + p2)
  Takeaways            38/48   79%
  Failure modes        51/60   85%
  TOTAL                89/108  82%
```

### What This Reveals

1. **p2 is nearly perfect.** The summary alone delivers 23/24 takeaways
   (96%) and blocks 30/30 failure modes (100%). A reader who reads only
   the summary walks away with the full engineering payload.

2. **p3 scores LOWER than p2.** This is not a bug — it's the walkaway
   architecture working as designed. The chapter ordering introduces
   timing dependencies (T1 delayed to ch24, T5 mid-book at ch9) that
   the summary avoids by presenting everything in one pass.

3. **p1 is the weak link.** Hover definitions deliver concepts but not
   full takeaways. T7 (services) and T8 (tradecraft) have minimal p1
   presence. This is addressable without any structural change.

4. **Gen's structural changes are entirely p3.** Her proposed chapter
   reordering, front-door sequence, Ch12 quarry, and Ch14 shard all
   operate at the p3 level. The p1 and p2 layers — where the
   engineering payload lives — are **untouched** by her proposal.

5. **Her one p2 change** is the replacement preface (Issue #2), which
   centers the relinquishment question. This could strengthen T6 at p2.

### Implications for Equal Eigenvalue Testing

The old diagnostic scored Gen's proposal at 66/87 (76%) — below the
75/87 threshold. That score measured p3 only. When separated by level:

| Level | eigenvalue45 | Gen's proposal | Change |
|-------|-------------|---------------|--------|
| **p1** | 36/54 (67%) | 36/54 (67%) | **unchanged** — hovers/tooltips are independent of chapter order |
| **p2** | 53/54 (98%) | 53-54/54 (98-100%) | **unchanged or improved** — summary is independent; preface may help T6 |
| **p3** | 46/54 (85%) | ~40/54 (74%) | **reduced** — chapter reordering affects timing for full-text readers |

**Conclusion:** Gen's restructure affects the p3 literary experience
only. The engineering floor (p1+p2) holds at 98%+ regardless of chapter
ordering. The real question is not "does her restructure break the
engineering?" (it doesn't) but "does her restructure improve the
literary quality enough to offset the p3 timing shifts?" That's a
literary judgment, not an engineering one.

**Equal eigenvalue at p3** still requires that no takeaway drops to 0
and no failure mode becomes unblocked at the chapter level. Gen's
proposal needs a complete chapter ordering (she hasn't specified where
the ~10 science chapters land) before p3 can be fully scored. But the
p1/p2 floor guarantees the message lands regardless.

---

## How to Score a New Configuration

### Full scoring (all three levels)

For each proposed change, score at all three levels independently:

1. **p1 audit:** Do hover definitions, rich panels, and menu tooltips
   still deliver each T and block each F? (Changes here are rare —
   only if hover-definitions.yaml or menu-tooltips.yaml are modified.)

2. **p2 audit:** Does summary.tex still deliver each T and block each F?
   (Changes here only if summary prose is rewritten.)

3. **p3 audit:** Does the new chapter ordering deliver each T and block
   each F at appropriate timing? (This is where structural changes
   like Gen's proposal are scored.)

### Equal eigenvalue criteria (revised)

A new configuration is an equal eigenvalue if:

1. **p2 score ≥ 53/54** (engineering floor maintained — summary untouched)
2. **p3 score: no T scores 0, no F scores 0** (nothing missing at chapter level)
3. **p3 total ≥ 40/54** (chapter-level experience not degraded beyond tolerance)
4. **GA reader group score ≥ 2** (primary audience served)
5. **Build clean** (`make all` no errors)

An **improvement eigenvalue** additionally:
- Improves p3 literary quality (GA engagement, pacing, story hooks)
- OR improves p1 delivery (more hovers, richer panels)
- OR improves p2 delivery (stronger summary)
- While maintaining all thresholds above.

### Legacy scoring (p3-only, for comparison)

The original composite (75/87 = 86%) measured p3 plus walkaway and
reader-group experience. It remains valid for comparing chapter-ordering
configurations against each other. The p-level analysis adds the
insight that p1+p2 form an engineering floor independent of p3.

---

*Diagnostic written by Argus (Auditor), S63. P-level analysis added
S63 after Bruce identified that T/F delivery is concentrated in p1+p2.
Reusable. Run against any proposed restructure by scoring all three
levels independently.*
