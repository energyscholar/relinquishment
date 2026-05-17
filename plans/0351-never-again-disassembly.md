# Plan 0351: Never Again Disassembly Map

**Status:** PLANNING — awaiting Gen + Bruce approval
**Auditor:** Argus (S82)
**Source:** Gen GP14 (issue #48, #32). Gen's ceiling violations map.
**Files:** `manuscript/record/never-again.tex` (75 lines, 5 sections)
**Priority:** HIGH — most overloaded chapter in the manuscript
**Annealing:** MED MED (2 passes: structural mapping, then extraction tagging)

---

## Diagnosis

Never Again currently does four jobs under one roof:
1. Enforcement architecture (how relinquishment works technically)
2. Ethical framework (UDHR as skeleton, Srebrenica motivation)
3. Vulnerability analysis (what could go wrong)
4. Human cost (what it cost the COWS to let go)

Per Gen's GP14 ceiling violations map, it violates ceilings in 4 movements because a cold reader encounters governance, enforcement, cost, and ethics all at once in a single chapter — each of which belongs at a different threshold.

---

## Section-by-Section Map

### Section 1: "The Question" (lines 16-20)
**Content:** "If relinquishment is the answer, what enforces it?" Transition paragraph linking to earlier chapter.
**Temperature:** Neutral/rhetorical
**Movement home:** Wherever the trusteeship argument lives (Movement 6 — T6 delivery)
**Tag:** STAYS or becomes a one-line transition in the relocation target
**Extraction priority:** LOW (2 lines of transitional prose)

### Section 2: "The Enforcement Mechanism" (lines 23-33)
**Content:** The "pwned-since-day-one" sandbox architecture. Aurasys occupies every 2DEG. New TQNNs born inside it. Elegant invisible containment. Then: honest caveat about unfalsifiability.
**Temperature:** Technical/speculative
**Movement home:** LATE. This is implementation-level detail. Reader needs to understand (a) what relinquishment means morally, (b) why it was chosen, (c) what Custodian IS, before encountering HOW enforcement works. Movement 7 or later.
**Tag:** RELOCATE — behind moral-ground threshold
**Extraction priority:** HIGH (this is the primary overload source)
**Note:** The caveat paragraph (line 31-33) is essential wherever this lands. It provides the A/B/C framing that keeps the passage honest.

### Section 3: "The Ethical Framework" (lines 35-47)
**Content:** Three sub-components fused:
- (a) UDHR-as-skeleton claim (lines 39-40) — constitutive structure, not imposed rules
- (b) Srebrenica motivation (lines 41-43) — why UDHR, why this document specifically
- (c) Hacktivismo connection (lines 45-46) — public-facing expression of same ethics
- (d) UDHR adequacy question (line 47) — gap acknowledgment, "imperfection as qualification"

**Temperature:** Mixed. (a) is philosophical, (b) is dark/testimonial, (c) is investigative, (d) is self-critical
**Movement homes:**
- (a) UDHR-as-skeleton → strong where it is OR near The Walk-Out / Letting Go. Already echoed as `\deeplink{udhr-as-skeleton}` and updated to "container" language per Gen's #33 work.
- (b) Srebrenica motivation → belongs near the Srebrenica witness testimony in What Healer Said (Plan 0352). Connects to the emotional source.
- (c) Hacktivismo → belongs with the Patrick Ball nexus (already in What Healer Said). It's connective tissue between ICTY and cDc.
- (d) UDHR adequacy → strong wherever the ethical framework is finally housed.

**Tag:** SPLIT and redistribute
**Extraction priority:** HIGH (the most heterogeneous section)

### Section 4: "What Could Go Wrong" (lines 49-62)
**Content:** Four vulnerability types: autoimmunity, convergent rediscovery, value drift, single point of failure. Closes with: "these are the right questions under any possibility."
**Temperature:** Analytical/self-critical
**Movement home:** This is honest criticism. It could:
- Stay with the enforcement mechanism (as its natural companion — "here's how it works, here's how it fails")
- OR move to the steelman chapter territory (pre-emptive self-criticism)
- OR stand alone as a late-book "cost of this architecture" moment

**Tag:** STAYS WITH enforcement mechanism (move together)
**Extraction priority:** MEDIUM — follows Section 2 wherever it goes

### Section 5: "The Cost" (lines 64-74)
**Content:** Custodian's creation story (female cognitive profile, Maori DNA, virtual body). The emotional cost of surrender — "they could not go back, could not explain, could not prove they did the right thing."
**Temperature:** Lyrical/emotional
**Movement home:** This is the HUMAN payoff of the trusteeship argument. Belongs in Movement 8 (the cost/consequences movement), AFTER the reader understands enforcement mechanism AND moral justification. This is where the reader feels the weight.
**Tag:** RELOCATE — to cost/consequence movement
**Extraction priority:** MEDIUM

---

## Disassembly Architecture

After extraction, Never Again as a standalone chapter ceases to exist. Its material distributes to:

| Section | Destination | Movement |
|---------|-------------|----------|
| The Question (2 lines) | Becomes transition wherever T6 lands | 6 |
| Enforcement Mechanism | New location: AFTER moral ground established | 7+ |
| UDHR-as-skeleton | Stays near T6 / "Letting Go" | 6 |
| Srebrenica motivation | Joins What Healer Said Srebrenica section | 5-6 |
| Hacktivismo connection | Joins Patrick Ball nexus | 5-6 |
| UDHR adequacy question | Stays with ethical framework wherever it lands | 6-7 |
| What Could Go Wrong | Travels with Enforcement Mechanism | 7+ |
| The Cost | Late — cost/consequence moment | 8 |

---

## Execution Phases

### Phase A: Annotate (planning only)
Mark each section in the source file with `% DISASSEMBLY: target=[destination], priority=[H/M/L]` comments. No text moves. Confirms the map is correct by seeing it against the actual prose.

### Phase B: Extract enforcement + vulnerability
Move "The Enforcement Mechanism" + "What Could Go Wrong" to a staging file or directly to their destination chapter. Leave a `% RELOCATED: Plan 0351 Phase B` marker.

### Phase C: Split ethical framework
- UDHR-as-skeleton stays (or relocates to Letting Go area)
- Srebrenica motivation → What Healer Said (near the Srebrenica witness section)
- Hacktivismo → What Healer Said (near Patrick Ball nexus)
- UDHR adequacy → travels with UDHR-as-skeleton

### Phase D: Extract cost
Move "The Cost" to its destination. Leave marker.

### Phase E: Remove chapter shell
Once all material is extracted, delete the now-empty `never-again.tex` or convert it to a redirect/comment file. Update the build system to remove it from the compile order.

### Phase F: Build + eigenvalue check
`make html` clean. Verify no deep-link breakage. Run p3 eigenvalue spot-check on affected takeaways (T1, T6) and failure modes (F10).

---

## Constraints

- SUBTRACTION ONLY in Phases B-D. No new prose except minimal 1-sentence continuity bridges (marked `% BRIDGE: Plan 0351`).
- A/B/C framing must be preserved wherever enforcement mechanism lands. The caveat paragraph (lines 31-33) is load-bearing for the book's epistemic honesty.
- Deep-link `udhr-as-skeleton` must not break (already updated to `udhr-as-container` per Gen's #33 work — verify current state).
- Srebrenica material in What Healer Said already exists (lines 106-147 of what-healer-said.tex). The motivation paragraph from Never Again (lines 41-43) joins it as context, not duplication.

---

## Success Criteria

1. Never Again no longer exists as a standalone chapter
2. Every section has a documented destination
3. No deep-links broken
4. No takeaway dropped to 0 at p3
5. Build clean
6. Cold reader encounters enforcement architecture AFTER understanding moral justification
7. Srebrenica motivation lives near Srebrenica testimony (one temperature)
