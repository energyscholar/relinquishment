# Plan 0008: Pre-Build Pedagogy Fixes (Revised)

**Serial:** 0008
**Date:** 2026-02-15 (revised after red team review)
**Status:** COMPLETE (verified S63 audit)
**Depends:** 0001, 0002
**Purpose:** Apply all identified scientific accuracy and pedagogical fixes to manuscript content before the major chapter-writing phase begins. Nine edits plus two guidance items across five files. Three fixes from the original plan were rejected by red team review; two narrative text edits (M2b) were dropped. Four additional fixes added from Session 9 factual red team (cathedral description, Churchill/Coventry reframe, Miller-Urey attribution, RSA footnote).

---

## Red Team Disposition

The original plan had 10 fixes. Red team review (2026-02-15) disposition:

| Verdict | Count | Fixes |
|---------|-------|-------|
| Approved as-is | 4 | C1, M1, M1b, M3 (guidance only), M4 (no edit) |
| Modified | 4 | C2, M2, m1, 5D-4 (timeline) |
| Rejected | 3 | P1, P2 (simple-summary hedges), five-disc in Plan 0007 |

**Rejected rationale:** P1/P2 micro-hedges in simple-summary.md damage the narrative voice. The three-possibilities framing at the structural level IS the hedge; injecting "according to this story" into narrative beats weakens the prose without improving epistemic honesty. The simple summary is written for Karen (general reader), not Priya (physicist). M2b narrative text ("Five minds, five disciplines") left as-is — it is placeholder prose in confident voice; "disciplines" is fine in English narrative. Plan 0007 internal language does not need terminological cleanup.

---

## Files Affected

1. `plans/0006-ultra-section.md`
2. `manuscript/versions/ultra-bridge.md`
3. `manuscript/appendix/abstracts.tex`
4. `manuscript/track-1-confession/ch01.tex`
5. `manuscript/appendix/timeline.tex`

All paths relative to `~/software/relinquishment/`.

---

## Fixes to Apply

### File 1: `plans/0006-ultra-section.md`

**Fix C1 — Coventry casualty figure (line ~41)**

Find:
```
Churchill had advance warning that the Luftwaffe would bomb Coventry. He let it happen — tens of thousands of civilian casualties — rather than reveal that Britain could read German codes.
```

Replace with:
```
Churchill had advance warning that the Luftwaffe planned a major raid. He let it happen — 568 people killed, the medieval cathedral destroyed — rather than reveal that Britain could read German codes.
```

Why: The actual death toll was 568. "Tens of thousands" is wrong by two orders of magnitude. If a future Generator re-runs this plan, it must not reintroduce the error.

---

### File 2: `manuscript/versions/ultra-bridge.md`

**Fix C2 — Coventry "exact target" asserted as known fact (lines 43-45)**

Find:
```
Winston Churchill had advance warning. British intelligence, using Ultra decrypts, knew the raid was coming. The exact target. The approximate timing. Churchill knew.

He did not evacuate the city. He did not visibly reinforce its defenses. He did not warn the people of Coventry that death was coming from the sky that night.
```

Replace with:
```
Winston Churchill had advance warning. British intelligence, using Ultra decrypts, knew a major raid was coming. Intelligence pointed to Coventry. Churchill knew enough.

He did not evacuate the city. He did not visibly reinforce its defenses. He did not warn the people of Coventry that death was coming from the sky that night.
```

Why: Modern historiography (Hinsley) holds Churchill knew a major raid was coming but may not have known the specific target with certainty. "The exact target" states the popular myth as fact. The replacement preserves the short-sentence rhythm, removes the contested claim, keeps the second paragraph intact (historically uncontested), and lets the existing hedge at line 51 do its job. "Churchill knew enough" preserves the moral weight without claiming omniscience.

**Fix m1 — Turing's apple (line 101)**

Find:
```
He died on June 7, 1954. A half-eaten apple laced with cyanide beside his bed.
```

Replace with:
```
He died on June 7, 1954. A half-eaten apple beside his bed. Cyanide in his body. The inquest ruled suicide.
```

Why: The apple was never tested for cyanide. The coroner ruled suicide by cyanide poisoning, but the delivery mechanism is debated (Copeland has argued accidental death via electroplating fumes). The replacement keeps the apple image, states cyanide as the established cause of death, separates the two facts (more accurate and more powerful than "laced with cyanide"), and adds "The inquest ruled suicide" — giving the historical record without endorsing it, signaling to Copeland-aware readers that the debate exists.

**Fix m2 — DES cognitive claim (line 99)**

Find:
```
His ability to think clearly was being destroyed by the very institution he had saved.
```

Replace with:
```
His body was being altered by the very institution he had saved.
```

Why: Source-facts.md flags "DES destroyed Turing's ability to think" as contested. Physical effects of DES are documented; cognitive impairment is less certain. Turing continued publishing during treatment. "Altered" captures the horror without asserting the contested cognitive claim.

---

### File 3: `manuscript/appendix/abstracts.tex`

**Fix M1 — Vattay citation in Abstract III (line ~47)**

Find:
```
The mechanism is analogous to biological extremophile evolution: the system exploits edge-of-chaos criticality (Vattay et al., 2014) to maintain quantum coherence through configurations where thermal noise assists rather than destroys coherent processes. We emphasize that no room-temperature TQNN was engineered from first principles; the solution was discovered by the evolutionary process and remains only partially understood by the research team.
```

Replace with:
```
The mechanism is analogous to biological extremophile evolution: the system exploits edge-of-chaos criticality to maintain quantum coherence through configurations where thermal noise assists rather than destroys coherent processes. The theoretical possibility of power-law (rather than exponential) decoherence at criticality has been explored for biological systems (Vattay et al., 2014), but its applicability to topological quantum substrates remains conjectural. We emphasize that no room-temperature TQNN was engineered from first principles; the solution was discovered by the evolutionary process and remains only partially understood by the research team.
```

Why: Vattay et al. (2014) studies the Anderson metal-insulator transition in biological molecules, not anyonic braiding in FQHE states. Citing it as the mechanism for room-temperature TQNN operation extrapolates the paper beyond its domain. The corrected version uses Vattay as theoretical precedent (power-law decoherence exists) while keeping evolutionary selection as the actual mechanism. This is the single most important scientific claim in the narrative and must be defensible.

**Fix M1b — Vattay citation in Abstract IX (line ~125)**

Find:
```
Edge-of-chaos criticality (Vattay et al., 2014) can, in principle, extend quantum coherence in such a system far beyond the naive thermal decoherence limit.
```

Replace with:
```
If the edge-of-chaos criticality mechanism explored for biological systems (Vattay et al., 2014) generalizes to plasma substrates --- an untested conjecture --- it could in principle extend quantum coherence far beyond the naive thermal decoherence limit.
```

Why: Same extrapolation problem, now applied to magnetospheric plasma. Adding "untested conjecture" makes the speculative chain explicit.

---

### File 4: `manuscript/track-1-confession/ch01.tex`

**Fix M2 — Disambiguation in placeholder image caption (line 18)**

Find:
```
\placeholderimage{0.8\textwidth}{4cm}{Diagram: Convergence of five disciplines --- topology, autocatalysis, universality, solitons, parallel computation}
```

Replace with:
```
\placeholderimage{0.8\textwidth}{4cm}{Diagram: Convergence of five fields --- topology (Freedman), autocatalysis (Kauffman), universality (Wolfram), soliton dynamics (Hasslacher), parallel computation (Hillis)}
```

Why: Adding scientist names is the real improvement — it disambiguates each contribution and prevents soliton-anyon conflation because the reader sees "soliton dynamics" attributed to Hasslacher's substrate work, not to anyonic excitations. Keep "soliton dynamics" (that IS what Hasslacher did on lattice-gas automata). Change "disciplines" to "fields" (shorter, natural, avoids the pedantic "intellectual traditions"). The narrative text at line 25 ("Five minds, five disciplines, one synthesis") is left as-is — it is placeholder prose in confident voice and will be rewritten when the chapter is fully drafted.

---

### File 5: `manuscript/appendix/timeline.tex`

**Fix 5D-4 — "five disciplines" in timeline (line 16)**

Find:
```
$\sim$1988 & Convergence of five disciplines begins & T1 & \ref{t1:ch01:genesis} \\
```

Replace with:
```
$\sim$1988 & Convergence of five fields begins & T1 & \ref{t1:ch01:genesis} \\
```

Why: The timeline is a reference document readers return to. "Five fields" is accurate, concise, and fits a table cell. "Intellectual traditions" is too long for a timeline entry.

---

## Additional Fixes (from Session 9 factual red team)

### File 2 (continued): `manuscript/versions/ultra-bridge.md`

**Fix C3 — Coventry cathedral description**

Find:
```
The medieval cathedral — built over centuries — was destroyed in a single night.
```

Replace with:
```
The great medieval church of St Michael's — elevated to cathedral status only in 1918 — was destroyed in a single night.
```

Why: The church destroyed in 1940 was a medieval PARISH CHURCH (constructed ~1300s-1400s), only elevated to cathedral status in 1918 — 22 years before its destruction. The actual medieval cathedral (St Mary's Priory) was a different building, destroyed during Henry VIII's dissolution of the monasteries. "Built over centuries" overstates the construction timeline. The correction is more historically precise and signals credibility to readers who know Coventry's ecclesiastical history.

---

### File 2 (continued): `manuscript/versions/ultra-bridge.md`

**Fix C4 — Coventry/Churchill reframe: present debate as evidence, not assert Churchill knew**

The C2 fix above addresses the "exact target" assertion in lines 43-45. This additional fix strengthens the existing hedge at line ~51 to make the debate itself serve the argument.

Find the passage near line 51 that reads:
```
Historians debate the exact details of his decision-making. Some argue he had less warning than the standard account suggests. But the core point stands and is well-established in the historical literature: the secrecy of Ultra was considered more important than civilian lives. When a code-breaking capability is real, protecting its secrecy justifies almost anything in the minds of those who hold it.
```

Replace with:
```
Historians debate what Churchill actually knew. The majority view (Hinsley, GCHQ's own account) holds he expected a major raid but may not have known Coventry was the target. The popular version — that he sacrificed a city to protect Ultra — may be legend. But the existence of this debate is itself the proof: Ultra secrecy was considered so important that historians take seriously the question of whether a prime minister would let a city burn to preserve it. When a code-breaking capability is real, protecting its secrecy justifies almost anything in the minds of those who hold it.
```

Why: The original hedge ("some argue he had less warning") is too vague. Naming Hinsley and GCHQ gives the counter-evidence authority. But then the reframe turns the debate into STRONGER evidence for the book's point: the mere plausibility of the legend proves how seriously Ultra secrecy was taken. This is more persuasive than the assertion it replaces, and it is bulletproof against the counter-evidence.

---

### Plans/0007 reference: Miller-Urey date and attribution

**Fix C5 — Miller experiment date and attribution (Plan 0007, Pos 11)**

The current Plan 0007 at Pos 11 refers to "Miller's 1952 experiment." This is borderline — the experiment was performed in fall 1952 but published in May 1953. The universally recognized citation is "Miller-Urey experiment, 1953" (Harold Urey supervised). When the Generator writes Pos 11 (The Experiment), it must use:

- "Miller-Urey experiment" (not "Miller's experiment") — Urey supervised and the experiment bears both names
- 1953 as the standard citation year (publication date), with optional mention that the experiment was performed in late 1952

This is guidance for the Generator, not an edit to Plan 0007 itself (plan language is internal and does not need terminological precision). The chapter text must use the standard citation.

---

### Optional: RSA date footnote

**Fix C6 — RSA 1977/1978 ambiguity (ultra-bridge.md)**

Current text: "RSA -- named for Rivest, Shamir, and Adleman, the three American academics who published the same idea in 1977"

This is defensible — RSA was first publicly described in Martin Gardner's "Mathematical Games" column in Scientific American in August 1977. The formal CACM paper appeared February 1978. Most academic citations use 1978. No change required to the main text, but if a footnote mechanism exists, add:

```
RSA was first publicly described by Martin Gardner in August 1977; the formal academic paper appeared in February 1978.
```

This is optional. If no footnote mechanism is in place, skip — the current text is defensible as-is.

---

## Guidance (no edits — for future Generator awareness)

**M3 — Kauffman-anyon bridge (Abstract I):** Already framed as "We propose..." — correct academic language. When the Kauffman-anyon bridge appears in future narrative prose, it must be flagged as a novel conjecture: "applying the mathematical structure of Kauffman's theory to a quantum substrate — the same framework in an untested domain." Never present it as established science.

**M4 — Freedman's Fields Medal:** The problematic framing exists only in aurasys-memory (not in relinquishment files). If any future Generator run references Freedman's Fields Medal, clarify that the Fields Medal (1986) was for the 4D Poincare conjecture, and Freedman's contribution to the TQNN story is his *subsequent* work on anyonic computation (1988+).

---

## Verification

After applying all fixes, run:

1. `make` — full build must succeed with no errors.
2. `grep -r "tens of thousands" manuscript/ plans/` — must return zero results in Coventry context.
3. `grep -r "exact target" manuscript/versions/ultra-bridge.md` — must return zero results.
4. `grep -r "laced with cyanide" manuscript/` — must return zero results.
5. `grep "five disciplines" manuscript/track-1-confession/ch01.tex` — must return zero results on line 18 (the caption). Note: line 25 ("Five minds, five disciplines") is intentionally unchanged.
6. `grep "five disciplines" manuscript/appendix/timeline.tex` — must return zero results.
7. `grep -r "built over centuries" manuscript/versions/ultra-bridge.md` — must return zero results.
8. `grep "Some argue he had less warning" manuscript/versions/ultra-bridge.md` — must return zero results (replaced by specific Hinsley/GCHQ reframe).
9. `grep "ability to think clearly" manuscript/versions/ultra-bridge.md` — must return zero results (replaced by "body was being altered").

---

## Constraints

- Do NOT change files in `~/software/aurasys-memory/` — only `~/software/relinquishment/`.
- Do NOT edit `manuscript/versions/simple-summary.md` — P1 and P2 were rejected by red team.
- Do NOT edit `manuscript/track-1-confession/00-outline.md` — M2b narrative text left as-is.
- Do NOT edit narrative text at ch01.tex line 25 — only the placeholder image caption at line 18.
- Preserve all existing formatting and structure.
- If a fix touches a `.tex` file, ensure LaTeX compiles after the change (verified by `make`).
- One git commit for all fixes: `Plan 0008 phase 1: Pre-build pedagogy fixes`

---

## Summary

| # | Severity | File | What |
|---|----------|------|------|
| C1 | Critical | plans/0006-ultra-section.md | Coventry: "tens of thousands" -> "568 killed" |
| C2 | Critical | manuscript/versions/ultra-bridge.md | Coventry: "exact target" -> "knew enough" |
| C3 | Moderate | manuscript/versions/ultra-bridge.md | Cathedral: "medieval cathedral built over centuries" -> correct description |
| C4 | High | manuscript/versions/ultra-bridge.md | Coventry/Churchill: vague hedge -> specific debate-as-evidence reframe |
| M1 | Moderate | manuscript/appendix/abstracts.tex (III) | Vattay: mechanism -> theoretical precedent |
| M1b | Moderate | manuscript/appendix/abstracts.tex (IX) | Vattay: add "untested conjecture" |
| M2 | Moderate | manuscript/track-1-confession/ch01.tex (line 18) | Caption: add scientist names, "disciplines" -> "fields" |
| m1 | Minor | manuscript/versions/ultra-bridge.md (line 101) | Turing apple: separate apple from cyanide, add inquest |
| m2 | Minor | manuscript/versions/ultra-bridge.md (line 99) | DES: "ability to think destroyed" -> "body altered" (contested claim) |
| 5D-4 | Consistency | manuscript/appendix/timeline.tex (line 16) | "five disciplines" -> "five fields" |
| C5 | Guidance | (Generator awareness) | Miller-Urey: use "1953" and name both scientists |
| C6 | Optional | manuscript/versions/ultra-bridge.md | RSA: optional footnote on 1977/1978 ambiguity |

Total: 10 edits + 2 guidance items across 5 files.

---

## Handoff Prompt

You are the Generator. Read the plan at `~/software/relinquishment/plans/0008-pedagogy-fixes.md`. Apply all 10 edits exactly as specified — find the exact strings, replace with the exact replacements. Skip C5 (guidance only) and C6 (optional footnote — skip unless footnote mechanism exists). Do NOT edit simple-summary.md, 00-outline.md, or ch01.tex line 25. Run all verification checks. One commit: `Plan 0008 phase 1: Pre-build pedagogy fixes`.

---

*Nightstalker, 2026-02-15 (revised after red team review)*
