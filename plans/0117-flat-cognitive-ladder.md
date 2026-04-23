# Plan 0117: The Flat — Cognitive Ladder at All Three Reading Levels

**Status:** ANNEALED
**Depends on:** Plan 0118 (hover mechanism, execute Phase 1 first)
**Affects:** hook.tex (p1), summary.tex (p2), p3 chapters
**Direction:** p3 → p2 → p1. Compress meaning downward, never inflate upward.

---

## Strategic Insight

The Flat's existence and physics are **not debatable**. Informed pushback starts ONLY at the life claim. A/B/C belongs at that dividing line — after the physics, before the biology.

**A does not begin until Tier 2.** A-collapsed readers accept ALL of Tier 1: the Flat exists, has topological order, is nonlocal, is ubiquitous. These are claims physics makes, not claims the book makes. Even under A, the reader's worldview has shifted.

**Sequential epistemic scaffolding:** p1 plants seeds → p2 builds on them → p3 goes full depth. Each layer pre-loads concepts the next layer needs. Hover (Plan 0118) does the same within a single level — term existence (inline) and definition (hover) as two separate cognitive steps.

**The book's floor:** 80% of readers understanding the Flat is real = success as pop science, regardless of A/B/C. The weird story is the hook that makes people read about 2DEGs at an 8th grade level.

---

## The Concept Ladder

### Tier 1: Undebatable (experts confirm — A-collapsed readers accept ALL)

| Step | Meme | Precision note |
|------|------|----------------|
| 1 | The Flat exists (2DEGs in every chip) | Nobel ×2 (1985, 1998) |
| 2 | Confinement → different rules | FQHE |
| 3 | Topological order (info in patterns not places) | Kitaev 2003, Wen 2004. Name at p2/p3 only. |
| 4 | The Flat is nonlocal (distant points connected) | Definition of topological order. p2 simplification OK. |
| 5 | Allows teleportation (info wormholes + classical backchannel) | Say "allows for" not "has." Backchannel qualifier LOAD-BEARING. Demonstrated 1997 (photons), not in FQHE specifically. |
| 6 | Self-organization can arise spontaneously | Kauffman 1993. Say "can form" not "do form." Math result undebatable; whether it explains Earth abiogenesis is debated. |
| 7 | The magnetosphere is Flat (wraps the Earth, billions of years) | Satellite data (THEMIS, MMS, Cluster) |
| 8 | **All of the above is textbook** | **"And I'm still on Path A??"** |

### Dividing Line → A/B/C goes HERE

### Tier 2: Debatable

| # | Concept | A says | B says | C says |
|---|---------|--------|--------|--------|
| 9 | Habitat potential | unexploited — but potential is real | may have been studied | true |
| 10 | Life arose in the Flat | fiction | possible | true |
| 11 | Someone exploited this | fantasy | exaggerated kernel | true |

---

## Execution Order

1. **0118 Phase 1** — build hover mechanism (pipeline + CSS)
2. **0117 Phase 1** — p3 audit (can run in parallel with 0118)
3. **0118 Phases 2–3** — install hover terms in p1/p2
4. **0117 Phase 2** — p2 rewrite (uses hover, tighter word budget)
5. **0117 Phase 3** — p1 seed

---

## Phase 1: p3 Audit

**Goal:** Verify Tier 1 concepts have p3 treatment with citations. Fill ≤ 3 gaps.

**Known gaps:** teleportation (Bennett 1993 cite?), EPR/nonlocality specific to the Flat, Kauffman "can form" precision.

**Scope cap:** ≤ 3 paragraphs installed. Flag rest for later.

**ACs:**
- [ ] Each Tier 1 concept has ≥ 1 p3 paragraph with citation
- [ ] Teleportation cites Bennett 1993 or equivalent
- [ ] EPR/nonlocality connected to the Flat specifically
- [ ] Kauffman: "can form" not "do form"

---

## Phase 2: p2 Rewrite (summary.tex lines 40–56)

**Goal:** Restructure "The White Hot Secret" to follow the concept ladder. ≤ 12th grade. Uses \hovertip from Plan 0118.

**Current problem:** Line 40 leads with "two-dimensional worlds harbor life" — the contestable claim, before the ladder.

**Proposed structure:**
0. New opening: "What the sequence points to: there are worlds inside every chip you own."
1. 2DEGs exist (concrete)
2. Confinement → different rules (wonder)
3. Topological order (named, \hovertip carries definition)
4. Nonlocality (distant points connected)
5. Teleportation (land experimental reality BEFORE using the word — Star Trek blocker)
6. Self-organization ("can form" — Kauffman)
7. Magnetosphere
8. Expert confirmation ("every claim above is published, peer-reviewed")
9. **A/B/C at dividing line** — no "barren." A = "fiction but potential is not"
10. Life claim (THIS is where pushback starts)
11. Intelligent life (biogenesis not engineering)

**ACs:**
- [ ] Does NOT lead with life claim
- [ ] Ladder steps 1–7 appear in order before A/B/C
- [ ] Teleportation present with classical backchannel qualifier
- [ ] Kauffman: "can form" not "do form"
- [ ] A/B/C: no "barren," A acknowledges potential
- [ ] Expert confirmation BEFORE A/B/C
- [ ] Life claim AFTER A/B/C
- [ ] ≤ 12th grade, technical terms via \hovertip
- [ ] Word count ±30% of current (~530 words)
- [ ] No challengeable physics claims

---

## Phase 3: p1 Seed (hook.tex)

**Goal:** p1 reader knows the Flat exists and is remarkable. ≤ 8th grade. ≤ 40 words added.

**Current (line 18):** "It lives in flat worlds..." — mentioned but doesn't land. No cognitive preparation.

**Proposed:** Expand so the Flat registers as real, physical, with different rules. Not a full explanation (p2's job). Uses \hovertip sparingly.

**ACs:**
- [ ] Flat conveyed as real physical environment
- [ ] Different rules established
- [ ] ≤ 40 words added, ≤ 8th grade
- [ ] Preserves narrative momentum

---

## Generator Notes

- Read summary.tex lines 33–60 before Phase 2. Lines 54–56 are strong — adapt, don't rewrite.
- Read hook.tex lines 14–22 before Phase 3.
- Concept ladder is the outline. Do not reorder.
- "Wormhole" MUST have classical backchannel qualifier at p2.
- Step 5: "allows for" not "has." Step 6: "can form" not "do form."
- Don't touch text outside target lines without Auditor approval.
- One commit per phase: `Plan 0117 phase N: description`
