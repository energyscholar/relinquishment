# Plan 0119: Cognitive Scaffolding — Non-Physics Barriers

**Status:** COMPLETE (verified S63 audit)
**Depends on:** Plan 0118 (hover mechanism)
**Companion to:** Plan 0117 (physics barriers — the Flat)
**Affects:** summary.tex (p2), hook.tex (p1), selected p3 chapters
**Direction:** p3 → p2 → p1.

---

## Purpose

Plan 0117 scaffolds the physics (the Flat, topological order, teleportation). This plan scaffolds everything else a GA reader needs to absorb before reaching the end of p2. Goal: reader finishes p2 having understood every new concept, without bouncing.

**Key framing device:** For much of this journey, A/B/C doesn't matter. The physics is true, the historical precedents are true, the logic is true — under all three possibilities. Say this explicitly at strategic points. It removes "but is this real?" anxiety and lets the reader absorb freely.

---

## Barrier Inventory

### B1: Room-Temperature Quantum Computing (p2:129)

**Why readers bounce:** Public QC needs millikelvin cooling. The book claims room temp in the 1990s.

**Scaffold:** Topological protection doesn't need cooling — information is protected by the *pattern*, not the temperature. That's Kitaev's entire point and the reason Microsoft has spent billions on topological QC. The physics reason it could work is Tier 1 (undebatable). Whether anyone achieved it is where A/B/C diverge.

**Treatment:**
- p3: Ensure topological protection → room temp argument is explicit with citations (Kitaev 2003, Freedman/Nayak). Check pos10-the-braid.tex, pos13-genesis.tex.
- p2: One sentence near line 129. Reader already absorbed topological order from Plan 0117's Flat section — this connects: "Topological protection is why — information stored in patterns, not places, doesn't need shielding from heat." Piggybacks on 0117, not standalone.
- p1: No treatment (p1 doesn't mention temperature)
- \hovertip on "topological protection" if named

### B2: "Grown, Not Built" (p2:123, 168)

**Why readers bounce:** Computers are engineered. "Growing" one is alien.

**Scaffold:** Reader already absorbed self-organization from Plan 0117 (Kauffman, autocatalysis). This concept BUILDS ON that: if self-sustaining patterns form spontaneously given sufficient complexity, then "growing" a computational system means providing the substrate and letting physics do what physics does. Turing's morphogenesis (1952) — the same Turing who invented the computer also proved that patterns self-organize in chemical systems. Real science.

**Treatment:**
- p3: Verify morphogenesis/self-assembly treatment exists with Turing 1952 cite
- p2: The current text at 123 is already good ("grown, not built — the same way a living system grows"). Reinforce by connecting to self-organization concept from the Flat section. Reader should feel: "oh, this is the same thing I just learned about."
- p1: "grew a working quantum computer" (hook:13) — \hovertip explaining "grew" as self-organization
- \hovertip on "grown" linking to self-organization concept

### B3: Life in Non-Biological Substrate (p2:127)

**Why readers bounce:** "Life" = carbon + water + DNA. The Flat is physics, not biology.

**Scaffold:** Life is self-sustaining organization, not specific chemistry. Kauffman's autocatalytic sets are substrate-independent — the math works regardless of whether the reactions are chemical or quantum. This is mainstream origin-of-life thinking. If you accept that life is organization (which the reader already absorbed), then the substrate doesn't matter — carbon, silicon, anyons in a 2DEG. The question is whether the organizational complexity is sufficient.

**Treatment:**
- p3: Verify substrate-independence argument exists. Likely in pos13-genesis.tex.
- p2: Brief insertion near line 127. The current text jumps from "the system organized itself" to "origin of life in a new medium" without scaffolding WHY a non-biological substrate can host life. 1–2 sentences: "Life is organization, not chemistry. The same self-sustaining patterns that arose in Earth's oceans can arise in any substrate complex enough to support them."
- p1: Not needed at this level
- \hovertip on "substrate" or "new medium"

### B4: Walking Technology Out (p2:148)

**Why readers bounce:** "Security would catch them."

**Scaffold:** The technology is knowledge + physics, not hardware. You can't smuggle a nuclear reactor, but you can carry knowledge in your head. Every espionage case in history involves knowledge transfer. The precedent is already in the text (Bletchley Park, GCHQ PKC) — people kept secrets, but people also eventually talked. The walk-out is the inverse: people who were INSIDE choosing to take knowledge OUT.

**Treatment:**
- p3: Verify this is addressed in pos18-the-walk-out.tex
- p2: Brief reinforcement near line 148. Current text focuses on the moral weight ("breaks every rule of classified research"). Add: WHY it's physically possible. "The technology was not a machine in a vault. It was knowledge — physics, mathematics, methods. Knowledge walks out in the minds of the people who hold it."
- p1: Already implied ("They gave it up. Not to another country...")
- \hovertip on "walked the working technology out" — explaining knowledge vs hardware

### B5: Guided Deduction (p2:200)

**Why readers bounce:** "Just TELL him!" Why spend 3 years teaching?

**Scaffold:** Three-layer answer:
1. **Legal:** Classification oaths carry criminal penalties. Edward Snowden is in exile. Teaching published science is legal; disclosing classified information is prison. The distinction is load-bearing.
2. **Structural:** The physics was always public. The SEQUENCE was not. Lane didn't need to reveal anything classified — he just needed to point Bruce at the right papers in the right order. That's teaching, not disclosure.
3. **Historical:** This is how mentorship works. Socratic method. The PhD system. An advisor doesn't hand you the answer — they guide you to discover it. Lane used the oldest teaching method in the world.

**Treatment:**
- p3: Check The Handler chapter and pos05-the-stories.tex for explicit treatment
- p2: The scaffold is ALREADY IN THE TEXT at lines 198-201 ("Lane never disclosed anything classified. That distinction matters."). Light touch: add 1 sentence with the Snowden/criminal-penalty frame to land the gravity. Something like: "Edward Snowden is living in exile for revealing far less." — wait, that's already at line 153. Cross-reference or echo it near line 200. The reader may not connect the two passages.
- p1: Not needed (hook mentions "never revealing anything secret, only guiding him through published science")
- \hovertip on "guided deduction" — "Teaching someone to discover the answer from public information, rather than disclosing it directly. Legally distinct from disclosure. The method is as old as Socrates."

### B6: Relinquishment (p2:146-157, 183)

**Why readers bounce:** "Nobody gives up power."

**Scaffold — the Spider-Man inversion:**
1. You can't properly USE it. (What do you DO with the ability to read everyone's mail? You can't use it without becoming a tyrant.)
2. You can't reliably KEEP it. (Secrets leak. People die. Governments change. The Bletchley precedent: secrets held for decades eventually come out.)
3. With great power comes great responsibility — and no human can bear that responsibility indefinitely. (Everyone knows the Spider-Man line. The twist: what if you're NOT up to being Spider-Man? What if nobody is?)
4. So you're holding something you can't use, can't keep, and can't be responsible for. What do you do?
5. You relinquish it. Not heroic sacrifice — **the only sane option.**

This reframe flips the reader's instinct from "nobody gives up power" to "what ELSE could you do?"

**Treatment:**
- p3: Verify the logic chain exists. May need explicit development.
- p2: **Best placement: near line 183** ("This act... is called relinquishment") — right where the word is defined and the reader needs the WHY. The current walk-out section (146-157) covers the moral weight; the Guardian section (166-186) has the UDHR framing. What's missing is the CAN'T-USE / CAN'T-KEEP / CAN'T-BE-RESPONSIBLE logic chain. Build to the Spider-Man moment, don't start with it. 3–4 sentences: the logic chain first, then: "With great power comes great responsibility — but what if the responsibility is more than any person, any government, any institution can reliably bear? Relinquishment is not sacrifice. It is the only option left."
- p1: The hook already has "They gave it up." Sufficient at p1 level.
- \hovertip on "relinquishment" — "Voluntarily surrendering power — not to another owner, but permanently. Not because you're forced to, but because holding it is more dangerous than letting go."

### B7: The 12-Year-Old Marksman (p3 only)

**Why readers bounce:** Urban readers find this incredible.

**Scaffold:** Australian and NZ rural culture. Farm kids learn to shoot as a practical skill — pest control, livestock protection, putting down injured animals. .303 Lee-Enfield is the standard farm rifle. Regular practice from age 8 is normal. 400m is long range but not exceptional with a scoped rifle and years of practice.

**Treatment:**
- p3: \hovertip where this appears. "In rural Australia and New Zealand, children learn to shoot as a practical farm skill. A .303 Lee-Enfield is a standard farm rifle. Regular practice from age eight is common."
- p2/p1: Not mentioned at these levels. No treatment needed.

### B8: "True Under All Three" Markers (NEW DEVICE — throughout p2)

**Purpose:** At strategic points in p2, explicitly tell the reader that everything they've absorbed so far is true regardless of which possibility is correct. This removes "but is this real?" anxiety and lets them absorb freely.

**Placement:** Plan 0117 already places the main A/B/C marker at the Flat dividing line. Add only 2 more — enough to reassure, not enough to lecture:
1. After the encryption/QC explanation (~line 82): "Quantum computing is real. The race to build one is real. This is true under all three possibilities."
2. After the guided deduction explanation (~line 201): "Published science is public. The papers Lane pointed to are verifiable. None of this depends on the story being true."

**Treatment:**
- 1-sentence insertions. Light touch. Varied phrasing. The reader should feel reassured, not lectured.
- Do NOT add one after every section — that's heavy-handed. Two is enough to establish the pattern; the reader generalizes.

---

## Execution

### Phase 1: p3 Audit
Grep for each barrier's treatment in p3 chapters. Verify scaffolds exist. Fill ≤ 3 gaps.

### Phase 2a: p2 Major Scaffolds
Install B6 (Spider-Man relinquishment near line 183), B3 (non-bio life near line 127), B1 (room-temp QC near line 129). These are the biggest cognitive barriers that need new text.

### Phase 2b: p2 Light Touches
Install B5 (guided deduction echo — 1 sentence), B4 (walk-out knowledge vs hardware — 1 sentence), B2 (connect "grown" to self-organization — \hovertip + connecting clause), B8 ("true under all three" — 2 markers). These are refinements to existing text, not new arguments.

### Phase 3: p1 Seeds
Install \hovertips in hook.tex: "grew" (B2), "flat worlds" (0117), "relinquishment" if present.

---

## Acceptance Criteria

- [ ] AC1: Room-temp QC has physics scaffold (topological protection) BEFORE the claim
- [ ] AC2: "Grown not built" connects to self-organization concept the reader already absorbed
- [ ] AC3: Non-bio life scaffold present: life = organization, not chemistry
- [ ] AC4: Walk-out scaffold: knowledge vs hardware distinction
- [ ] AC5: Guided deduction: legal + structural WHY explicit
- [ ] AC6: Relinquishment: can't-use / can't-keep / can't-bear-responsibility logic chain + Spider-Man
- [ ] AC7: ≥ 3 "true under all three" markers in p2
- [ ] AC8: All new text ≤ 12th grade (p2) or ≤ 8th grade (p1)
- [ ] AC9: \hovertips on key terms per Plan 0118
- [ ] AC10: Total word count increase in summary.tex ≤ 250 words (scaffolds must be tight — \hovertips carry definitions, not inline text)

## Generator Notes

- Read full summary.tex before writing. Understand the flow.
- These are INSERTIONS, not rewrites. Existing text is strong. Add scaffolding around it.
- The Spider-Man line is pop culture gold at p2 level. Use it. Don't over-explain it.
- "True under all three" markers should feel natural, not formulaic. Vary the phrasing.
- The relinquishment logic chain (can't use, can't keep, can't be responsible) should build to the Spider-Man moment, not start with it.
- One commit per sub-phase: `Plan 0119 phase 2a/2b/3: description`
