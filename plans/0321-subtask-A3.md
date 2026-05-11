# Subtask A3: Revolutions 2-4 (Oxygen, Evolution, Germ Theory)

**Output:** Modify `build/images/scientific-revolutions-draft.html` (extend, don't overwrite)
**Commit:** `Plan 0321 A3: Revolutions 2-4 (Oxygen, Evolution, Germ Theory)`
**Read first:** The existing HTML file. Preserve everything. Add segments 2, 3, 4 following the same pattern established in segment 1 (Heliocentrism).

## Pattern (same as revised Heliocentrism)

Each revolution follows this structure:
1. **Normal Science** (~5s): What people believed/experienced. Name the key thinker + date.
2. **Anomaly Accumulation** (~15-20s): Multiple anomaly-dismissal PAIRS. Each pair:
   - Anomaly text appears center (36px, amber)
   - Reader absorbs (2s)
   - Dismissal bubble appears below (20px, muted)
   - Reader absorbs (1.5s)
   - Both shrink to ~10px and fly to park in a cluster near the Anomaly position
   - They STAY (creating visual clutter)
3. **Pause** (1s): Reader sees accumulated mess.
4. **Crisis** (~4s): 1-2 hostile quotes. Park near Crisis position. Maximum clutter.
5. **Revolution** (~4s): Golden flash (opacity 0.3). Clutter clears. Dramatic moment.
6. **New Paradigm** (~4s): What it gave us. Title bar resolves.

Total per revolution: ~35-40s. THAT'S FINE. Slower is better.

Activate scrubber dots 2, 3, 4 (gold, clickable). Show start year below each dot.

## Revolution 2: Oxygen (Segment 2)

**Scrubber year:** "1770" below dot 2.

**Title bar:**
- "The Chemical Revolution (1770–1789)"
- *"When things burn, they release phlogiston — an invisible fire element."*
- Resolve: *"Combustion consumes oxygen. Mass is conserved."*

**Years:** Normal: "~1700" | Anomalies: "1772"–"1777" | Crisis: "1780" | Revolution: "1783" | New Paradigm: "1789"

**Normal Science (blue):**
"Things burn. The flame rises. Something escapes into the air."
Below: "Georg Stahl's phlogiston theory. (~1703)"

**Anomaly-dismissal pairs (amber, 4 pairs):**

| # | Anomaly | Dismissal |
|---|---------|-----------|
| 1 | "Burn a piece of metal. Weigh the ash. It got HEAVIER." | "Phlogiston has negative weight." |
| 2 | "Seal a flask. Burn something inside. Total weight unchanged." | "The phlogiston is still in the flask." |
| 3 | "Some metals gain weight. Others lose it. No consistency." | "Different substances contain different amounts of phlogiston." |
| 4 | "Priestley isolates a gas that makes things burn MORE vigorously." | "He calls it 'dephlogisticated air.' Problem solved." |

**Crisis:**
- *"The theory explains everything — and therefore nothing."*
- *"Every anomaly gets a special exception."*

**Revolution:**
"Lavoisier seals a flask. Burns metal. Weighs everything."
"Mass conserved. A new element: oxygen. Combustion is combination, not release."
Name: "Lavoisier, 1783"

**New Paradigm:**
"The periodic table. Conservation of mass. Modern chemistry."

## Revolution 3: Evolution (Segment 3)

**Scrubber year:** "1859" below dot 3.

**Title bar:**
- "The Darwinian Revolution (1831–1953)"
- *"Each species was created in its present form. Species do not change."*
- Resolve: *"Species descend from common ancestors through natural selection."*

**Years:** Normal: "~1800" | Anomalies: "1811"–"1844" | Crisis: "1844–1858" | Revolution: "1859" | New Paradigm: "1953"

**Normal Science (blue):**
"Every living thing in its place. The Great Chain of Being."
Below: "Linnaeus's fixed classification. (~1735)"

**Anomaly-dismissal pairs (amber, 5 pairs):**

| # | Anomaly | Dismissal |
|---|---------|-----------|
| 1 | "Fossils of creatures that no longer exist." | "God created them and then un-created them." |
| 2 | "A whale's flipper has the same bones as a human hand." | "The Creator reused a good design." |
| 3 | "Same fossils found in South America AND Africa." | "They were placed there independently." |
| 4 | "Selective breeding changes animals dramatically in generations." | "That's artificial, not natural. Different thing entirely." |
| 5 | "Galápagos finches: different beaks on different islands." | "Each island received its own creation." |

**Crisis:**
- *"To suggest we descend from apes is an insult to our Creator."*
- *"Darwin delays publication for twenty years, dreading the response."*

**Revolution:**
"On the Origin of Species. Descent with modification. Natural selection."
Small icon: branching tree.
Name: "Darwin, 1859"

**New Paradigm:**
"DNA. Genetics. Gene therapy. CRISPR."

## Revolution 4: Germ Theory (Segment 4)

**Scrubber year:** "1847" below dot 4.

**Title bar:**
- "The Germ Theory Revolution (1847–1885)"
- *"Disease arises from miasma — foul vapors from rotting matter."*
- Resolve: *"Disease is caused by microorganisms. Hygiene saves lives."*

**Years:** Normal: "~1840" | Anomalies: "1847"–"1858" | Crisis: "1850–1861" | Revolution: "1861" | New Paradigm: "1885"

**Normal Science (blue):**
"The air smells bad near the sick. Open the windows."
Below: "Miasma theory, ancient tradition. Galen, ~200 AD."

**Anomaly-dismissal pairs (amber, 4 pairs):**

| # | Anomaly | Dismissal |
|---|---------|-----------|
| 1 | "Semmelweis: wash hands between patients. Deaths drop 18% → 1%." | "A gentleman's hands are always clean." |
| 2 | "Cholera follows water supply lines, not wind patterns." | "Coincidence. Bad air follows bad water." |
| 3 | "Wounds fester less when kept clean, even in fresh air." | "The miasma was already present in the wound." |
| 4 | "Semmelweis committed to an asylum. Dies there, age 47." | "He was clearly unstable. His ideas were offensive." |

**Crisis:**
- *"Are you suggesting that WE are killing our own patients?"*
- *"Preposterous. Invisible creatures causing disease?"*

**Revolution:**
"Pasteur's swan-neck flask. Broth stays clear for years."
"No spontaneous generation. Germs are real. They can be killed."
Name: "Semmelweis / Pasteur"

**New Paradigm:**
"Antibiotics. Vaccines. Sterile surgery. Modern medicine."

## Technical Notes

- Each segment follows the identical anomaly-accumulation engine pattern from segment 1
- Anomaly cluster parking: offset each shrunken pair slightly from the last (spiral or scatter) to create visible mess, not a neat stack
- The Kuhn cycle loop stays persistent at 0.25 opacity throughout — never cleared, never redrawn
- Between segments: brief pause (2s) + clear revolution-specific content (not the loop) before next segment
- If a user clicks a specific dot, jump directly to that segment
- Golden flash: max opacity 0.3 (toned down from previous)

## Report

State: file size, per-segment duration, anomaly pair counts, total cumulative duration, what works.
