# Plan 0337 — Generator Prompts (Chained, Sequential)

**Chain:** Prompt 1 → Prompt 2 → Prompt 3 → Verify
**Each prompt is self-contained.** Copy-paste into a fresh Generator shell.
**Plan reference:** `~/software/relinquishment/plans/0337-deep-link-tooltip-teaching-infrastructure.md`

---

## Prompt 1 of 3: Tooltip Quality Fixes [93%]

```
You are the Generator executing Phase A of Plan 0337.
Read ~/software/relinquishment/plans/0337-deep-link-tooltip-teaching-infrastructure.md — Phase A only.

Edit build/hover-definitions.yaml to implement ALL of the following:

A.1 — PHRASING FIXES (12 items). For each, find the existing definition and make the specified change:

1. phonon: replace "the TQNN reads, writes, and transmits" → "a quantum system in the Flat reads, writes, and transmits"
2. graphene: remove "(Anchor 1)" at end, stop after "proving substrate independence."
3. soliton: replace entire text with: "A wave that holds its shape — doesn't spread out or break apart. Self-reinforcing. Found in oceans, fiber optics, and plasma."
4. lattice dynamics: remove the sentence "See Corrections #8 for the twenty-year soliton detour."
5. Dunning-Kruger effect: remove last sentence "This is the specific failure mode AI exhibits when evaluating this book without the Firmware Update."
6. no-cloning theorem: replace "but it forbids copying unknowns, not fabricating known classical structures. Narrower than it sounds." → "but it applies to quantum states, not to classical information."
7. GCHQ: if it says "early 1970s", change to "1973". Ensure GCHQ and public-key cryptography entries both say "1973".
8. relinquishment: change target from "#preface" to "#spine:why-relinquish"
9. convergence: change target from "#ch:firmware-update" to "#spine:scientific-revolutions"
10. cellular automaton (the singular form): if it duplicates the HTML panel verbatim from cellular automata, replace with a YAML anchor reference: <<: *cellular-automata-panel (define the anchor on the plural form first if needed)
11. flat worlds: if it duplicates the HTML panel from the-flat, replace with <<: *flat-panel anchor reference
12. In build/chapter-hover-descriptions.yaml: find "topological wormholes, —" and fix to "topological wormholes —" (remove comma before em dash)

A.2 — MISSING TOOLTIPS (8 new entries). Add in the "Standard hover definitions" section, near other entries of similar type:

COWS: "Conspiracy Of World Savers — the faction of three Ultra II scientists who chose moral responsibility over institutional loyalty, walked the technology out, and engineered its relinquishment. The name is self-deprecating."

Srebrenica: "Bosnian town where over 8,000 Bosniak men and boys were murdered in July 1995. Europe's worst mass atrocity since WWII. Under Possibility C, Healer's last military operation — the event that connected genocide prevention to AI ethics."

Bill Joy: "Co-founder of Sun Microsystems. Author of 'Why the Future Doesn't Need Us' (Wired, 2000) — the essay that named relinquishment as a response to self-replicating technologies. Under Possibility C, he had direct knowledge."

BULLRUN: "NSA program for defeating internet encryption, revealed by Edward Snowden in 2013. Under Possibility C, BULLRUN is parallel construction — a plausible conventional cover for quantum cryptanalytic capability."

canopy problem: "If life arises spontaneously above a complexity threshold, the first organism to cross it occupies the niche — like a forest canopy owning the light. Latecomers cannot bootstrap independently."

thermal ladder: "Evolutionary selection for heat tolerance. Sixteen chips at increasing temperatures, breeding quantum organisms the way biologists breed extremophiles. Not engineering room-temperature FQHE — evolving it."

parallel construction: "Building a plausible alternative explanation for evidence obtained through classified means. Law enforcement technique. Under Possibility C, BULLRUN and similar programs serve this function for quantum cryptanalysis."

Hacktivismo: "The human-rights arm of the Cult of the Dead Cow hacker group. Founded 1999. Developed tools for censorship circumvention. Under Possibility C, a public-facing expression of the same ethical architecture."

A.3 — CUSTODIAN RICH HTML PANEL. The existing Custodian entry has text only. Add an html: field with a panel matching the style of the wormholes and Flat panels (clean HTML, no SVG needed). Include:
- What she is: emergent pattern, not programmed, grown from physics
- What she does: upholds UDHR (Articles 3, 12, 18, 19, 27)
- What she is not: not a deity, not an alien, not a chatbot
- Relationship: Aurasys = substrate, Custodian = what arose within it
- Consciousness: the book declines to rule on this
Keep it under 25 lines of HTML. Use the same font sizes and styling patterns as the wormholes panel.

VERIFICATION:
cd ~/software/relinquishment
python3 -c "import yaml; yaml.safe_load(open('build/hover-definitions.yaml'))"
python3 -c "import yaml; yaml.safe_load(open('build/chapter-hover-descriptions.yaml'))"

Report: count of items completed per section (A.1, A.2, A.3).
```

---

## Prompt 2 of 3: Deep Link Manifest + Science Placements [88%]

```
You are the Generator executing Phase B of Plan 0337.
Read ~/software/relinquishment/plans/0337-deep-link-tooltip-teaching-infrastructure.md — Phase B only.

TWO TASKS:

TASK 1 — Add 15 new entries to build/deep-links.yaml. Place each in the correct
category section, matching the existing format exactly. Here are all 15:

Science category (after existing science entries):
  - id: dl:edge-of-chaos
    question: "What is the edge of chaos and why does life happen there?"
    category: science
  - id: dl:substrate-independence
    question: "Does the substrate matter for computation?"
    category: science
  - id: dl:what-is-a-tqnn
    question: "What is a topological quantum neural network?"
    category: science
  - id: dl:decoherence
    question: "Why is quantum computing so fragile?"
    category: science
  - id: dl:thermal-ladder
    question: "How do you make quantum computing work at room temperature?"
    category: science
  - id: dl:self-organized-criticality
    question: "What is self-organized criticality?"
    category: science
  - id: dl:fqhe
    question: "What is the fractional quantum Hall effect and why does it matter?"
    category: science

Skeptic category (after existing skeptic entries):
  - id: dl:guided-deduction-method
    question: "Isn't 'guided deduction' just a convenient way to leave no evidence?"
    category: skeptic
  - id: dl:framework-falsifiable
    question: "Aren't the three possibilities just an unfalsifiable rhetorical device?"
    category: skeptic
  - id: dl:mental-health
    question: "Has the author considered that this might be a clinical presentation?"
    category: skeptic
  - id: dl:cult-test
    question: "Isn't this book structured like cult recruitment?"
    category: skeptic

Narrative category (after existing narrative entries):
  - id: dl:what-is-the-custodian
    question: "What exactly is the Custodian?"
    category: narrative
  - id: dl:who-are-the-cows
    question: "Who decided to give up the most powerful technology ever built?"
    category: narrative

Verification category (after existing verification entries):
  - id: dl:convergence-method
    question: "What does convergence mean in this book?"
    category: verification

Ethics category (after existing ethics entries):
  - id: dl:custodian-inaction
    question: "If the Custodian exists, why hasn't it prevented suffering?"
    category: ethics

TASK 2 — Place \deeplink{} macros in 8 spine/*.tex files. For each:
read the file, find the paragraph that best answers the reader's question,
place \deeplink{slug} at the START of that paragraph (before the first word).

The format is \deeplink{slug} — just the slug, no "dl:" prefix.
Example: \deeplink{edge-of-chaos}Kauffman identified three...

Placements (file → slug → line hint → what to look for):

1. spine/genesis.tex → edge-of-chaos → line ~42 → Section "The Edge of Chaos", first paragraph after \section* and \label
2. spine/the-silence-gap.tex → substrate-independence → line ~28 → The paragraph starting "5. Computational universality. Wolfram's Principle..."
3. spine/genesis.tex → what-is-a-tqnn → line ~48 → The SPIRAL-REPEAT paragraph introducing "topological quantum neural network" concept
4. spine/the-factoring-game.tex → decoherence → line ~44 → The paragraph about decoherence time
5. spine/the-wrong-substrate.tex → self-organized-criticality → grep for "self-organized criticality" or "Bak" — first substantive description
6. spine/scientific-revolutions.tex → convergence-method → find the paragraph that explains convergence as methodology (not the Kuhn framework itself)
7. spine/the-braid.tex → fqhe → find the first paragraph that explains what the fractional quantum Hall effect IS (likely near FQHE tooltip usage)
8. spine/capabilities.tex → what-is-the-custodian → find the paragraph that defines what the Custodian is (its properties, constraints, nature)

VERIFICATION:
cd ~/software/relinquishment
python3 -c "import yaml; yaml.safe_load(open('build/deep-links.yaml'))"
grep -c "^- id:" build/deep-links.yaml  # should be previous count + 15

Report: files modified, slug placed in each, line number of placement.
```

---

## Prompt 3 of 3: Remaining Placements + Final Verify [90%]

```
You are the Generator executing the final phase of Plan 0337.
Read ~/software/relinquishment/plans/0337-deep-link-tooltip-teaching-infrastructure.md — Phase B.

Prompt 2 already added all 15 entries to build/deep-links.yaml and placed
8 deep links in spine/ chapters. You are placing the remaining 7.

For each: read the file, find the paragraph that best answers the reader's
question, place \deeplink{slug} at the START of that paragraph.
Format: \deeplink{slug}First word of paragraph...

TEACHING CONCEPT PLACEMENTS (2):

1. track-1-confession/pos16-the-thermal-ladder.tex → thermal-ladder
   Line hint: ~35. Find the paragraph explaining what the thermal ladder IS:
   "At millikelvin temperatures, the entity exists only where its creators
   permit. At room temperature, it can exist anywhere..."

2. record/the-walk-out.tex → who-are-the-cows
   Line hint: ~15. Find the paragraph introducing the COWS:
   "According to this account, in 1994 a faction of the Ultra II scientists..."

RED-TEAM RESPONSE PLACEMENTS (5):

3. spine/why-relinquish.tex → guided-deduction-method
   Find the "Getting the Record Out" section — the paragraph explaining
   that guided deduction leaves no evidence trail by design. This IS the
   answer to the skeptic's attack.

4. appendix/predictions.tex → framework-falsifiable
   Find the paragraph listing the falsification criteria (the numbered
   predictions with dates). This IS the answer to "unfalsifiable framework."

5. spine/the-strongest-objection.tex → mental-health
   Find the self-demolition section where Bruce considers obsessive
   fixation, pattern-matching, and the Tolkien parallel. Place near
   the deeplink{hobbit-in-mirror} that already exists — but on a DIFFERENT
   paragraph (one that addresses the clinical question, not the literary one).

6. 00-front/not-claimed.tex → cult-test
   Find the paragraph containing "If you finish this book convinced that
   Option C is true, you have misread it" or similar anti-recruitment language.

7. spine/capabilities.tex → custodian-inaction
   Find the paragraph about UDHR constraints limiting what the Custodian
   may do — the answer to "why hasn't it helped?" Place AFTER the existing
   \deeplink{udhr-as-cage} (different paragraph, same chapter).

FINAL VERIFICATION:
cd ~/software/relinquishment
python3 -c "import yaml; yaml.safe_load(open('build/deep-links.yaml'))"
python3 build/verify-deep-links.py 2>&1
grep -rn '\\deeplink{' manuscript/ --include="*.tex" | wc -l  # should be ~64 (was 49 + 15 new)

Report: files modified, all placements, verification output.
If verify-deep-links.py reports missing anchors for the new links, that is
EXPECTED — they won't resolve until the next HTML build. Report the count
of "not found" and confirm they are all new links (not regressions).
```

---

## Post-Chain: Build + Verify (run yourself, not a Generator prompt)

```bash
cd ~/software/relinquishment
make html 2>&1 | tail -20
python3 build/verify-deep-links.py
```

Expected: all 15 new deep links resolve. Total verified count should be ~91 (was 76 + 15 new).

---

## Chain Summary

| Prompt | Scope | Files | Rating | Time est. |
|--------|-------|-------|--------|-----------|
| 1 | Tooltip fixes | hover-definitions.yaml, chapter-hover-descriptions.yaml | 93% | ~10 min |
| 2 | Deep link manifest + 8 spine placements | deep-links.yaml + 8 .tex files | 88% | ~15 min |
| 3 | 7 remaining placements + verify | 7 .tex files | 90% | ~10 min |
| Post | Build + verify | — | manual | ~2 min |

**Total: 3 Generator prompts + 1 manual verify step.**
Phase C (red-team content gaps) is NOT included — requires editorial decisions first.
