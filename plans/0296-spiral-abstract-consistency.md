# Plan 0296: Spiral Abstract Consistency — Cryogenic/Room-Temp Bifurcation

**Source:** Bruce identified SA V inconsistency with narrative reconstruction.
**Anneal:** PASS (2026-05-04, HIGH/MED/LOW). HIGH: SA IV pedagogy "Abstracts I–III" is reader-facing, not in-universe — no conflict with SA III internal. 20 mK consistent with SA I "millikelvin." SA VI "facility-dependent" receives fix perfectly: IG reconstructs gap after the fact. MED: SA III OLD string unique (line 292 is different). Personnel 5 FTE preserved, labels refined. SA V body ~900→1200 chars single-paragraph replacement; idempotency guard catches partial. LOW: "operational burden" disambiguated from new cryogenic maintenance. 99.7%/6mo = ~13h downtime, plausible for dilution fridge. FQHE ties to SA I substrate.
**C-violation check:** All changes are in Possibility C reconstructed documents. No A/B framing affected. Three possibilities hold.

---

## The Inconsistency

The narrative establishes a clear bifurcation (~1994-95):
- **DARPA line:** cryogenic, facility-dependent, put into SIGINT production ~1996
- **COWS line:** room-temperature, portable, walked out, eventually evolved into Custodian

Key narrative sources:
- `record/first-light.tex:130` — "DARPA's cryogenic version remained in the classified lab."
- `record/first-light.tex:162` — "This supercomputer was a single physical device that required supercooling — distinct from the room-temperature version the team walked out."
- `record/the-walk-out.tex:28` — "they chose to falsify DARPA records to conceal this success"
- `record/the-walk-out.tex:44` — "The cryogenic version remained with DARPA — a cryptanalytic tool, expensive to maintain, limited in application."

SA V (Production) contradicts this by describing a DARPA report about room-temperature production deployment. This makes SA VI's security failure ("framework assumed facility-dependent") nonsensical — if DARPA already had room-temp, why would they assume facility-dependence?

SA III (Thermal Selection) has a secondary issue: it's attributed as a classified journal publication, but the narrative says the COWS concealed and falsified records about this achievement. A publication visible to DARPA program management contradicts the concealment.

---

## Phase 1: SA V — Cryogenic Production

**File:** `manuscript/appendix/abstracts.tex`

### Title (line 100)

```
OLD: \textbf{``Operational Deployment and Classical Integration of Room-Temperature Topological Quantum Neural Networks''}
NEW: \textbf{``Operational Deployment of Cryogenic Topological Quantum Neural Networks in Signals Intelligence Production Infrastructure''}
```

### Body (line 106)

```
OLD: We describe the engineering challenges and solutions for integrating a room-temperature TQNN into operational signals intelligence infrastructure. The system interfaces with existing collection architecture via a classical control plane running hardened BSD Unix. Key engineering decisions: (1)~the control plane manages electromagnetic driving parameters and interprets TQNN output; the TQNN itself has no direct connection to external networks; (2)~all cryptanalytic queries are batched through a standardized API; operators interact with the control plane, never with the TQNN directly; (3)~output validation uses independent classical verification of a random 2\% sample of decrypted traffic. System availability exceeds 99.7\% over the initial 6-month operational period. The primary maintenance burden is feature-set training for new cipher types (mean: 72~hours per new cipher family). We identify control plane addressing as the principal scaling constraint. Personnel requirements: 3~FTE for operations, 1~FTE for training, 1~FTE for maintenance. Total cleared personnel with knowledge of system: 11.
NEW: We describe the engineering challenges and solutions for integrating a cryogenic TQNN into operational signals intelligence production infrastructure. The system requires a dedicated dilution refrigerator facility maintaining base temperature below 20~mK, with vibration isolation and electromagnetic shielding consistent with precision FQHE measurement. The system interfaces with existing collection architecture via a classical control plane running hardened BSD Unix. Key engineering decisions: (1)~the TQNN operates within the cryogenic enclosure; the classical control plane manages electromagnetic driving parameters and interprets output at room temperature; (2)~all cryptanalytic queries are batched through a standardized API; operators interact with the control plane, never with the TQNN directly; (3)~output validation uses independent classical verification of a random 2\% sample of decrypted traffic; (4)~the facility-dependent nature of the system is treated as a security feature --- physical containment at the cryogenic site ensures no unauthorized replication or removal. System availability exceeds 99.7\% over the initial 6-month operational period, limited primarily by scheduled cryogenic maintenance windows. The primary operational burden is feature-set training for new cipher types (mean: 72~hours per new cipher family). We identify control plane addressing as the principal scaling constraint. Personnel requirements: 3~FTE for SIGINT operations, 1~FTE for training, 1~FTE for cryogenic systems maintenance. Total cleared personnel with knowledge of system: 11.
```

### Rationale

- Adds cryogenic infrastructure reality (dilution refrigerator, base temp, shielding)
- Explicitly states facility-dependent = security feature (sets up SA VI perfectly)
- Adds cryogenic maintenance windows (explains scheduled downtime)
- Adds cryogenic maintenance FTE to personnel
- Retains BSD Unix control plane (confirmed by narrative: first-light.tex:130)
- Retains 11 cleared personnel, 99.7% availability, 72h cipher training

**Idempotency guard:** `grep "dilution refrigerator" manuscript/appendix/abstracts.tex` — if match, already applied.

---

## Phase 2: SA III — Attribution Fix

**File:** `manuscript/appendix/abstracts.tex`

### Journal attribution (line 68)

```
OLD: \textit{Physical Review [Classified] (Letters)}
NEW: \textit{[Internal Team Document --- Not Reported to Program Management]}
```

### Rationale

The narrative (the-walk-out.tex:28) states the COWS "chose to falsify DARPA records to conceal this success." A classified journal publication visible to program oversight contradicts this concealment. The new attribution makes clear this document existed within the COWS' internal records only — consistent with the IG report in SA VI discovering the breach after the fact.

The five physics-defense questions preceding SA III (lines 52-62) remain unchanged — they are reader-facing pedagogy, not part of the fictional document.

**Idempotency guard:** `grep "Not Reported to Program Management" manuscript/appendix/abstracts.tex` — if match, already applied.

---

## Phase 3: Verify No Other SAs Affected

Checked — no other SAs require changes:

| SA | Issue | Status |
|----|-------|--------|
| I (Genesis) | "millikelvin temperature" | ✓ Correct — initial development is cryogenic |
| II (Nursery) | No temp reference | ✓ |
| III (Thermal Selection) | Attribution implies DARPA visibility | **FIX (Phase 2)** |
| IV (Cryptanalysis) | No temp specified | ✓ Describes cryogenic system capability |
| V (Production) | "Room-Temperature" in DARPA report | **FIX (Phase 1)** |
| VI (Exodus) | "assumed facility-dependent (requiring cryogenic infrastructure)" | ✓ NOW CORRECT after Phase 1 |
| VII (Infrastructure) | COWS' room-temp version mapping networks | ✓ Not DARPA-attributed |
| VIII (Relinquishment) | Bill Joy essay analysis | ✓ No temp issue |
| IX (Orbital) | Magnetospheric extension of room-temp version | ✓ Post-amnesty document |
| X (Discovery) | Anomalous signatures | ✓ |
| XI (Kitaev's Echo) | "team's proposal for countermeasures" | ✓ COWS propose without revealing method |
| XII (Interdiction) | "exercised without authorization" | ✓ COWS acting with room-temp version |
| XIII (Confession) | "demonstrated room temperature" | ✓ This IS the reveal to DARPA (2002) |
| XIV (Unipolar) | No temp reference | ✓ |
| XV (Custodian) | No temp reference | ✓ |
| XVI (Latency) | No temp reference | ✓ |

---

## Narrative Consistency Check

After fixes, the SA arc reads:

1. **I:** Propose cryogenic TQNN (DARPA)
2. **II:** Train it at cryogenic temps (DARPA)
3. **III:** COWS secretly evolve it to room temp (**team-internal, hidden from DARPA**)
4. **IV:** Demonstrate cryptanalysis (cryogenic version, DARPA)
5. **V:** Put **cryogenic** version into SIGINT production (**DARPA, facility-dependent**)
6. **VI:** COWS walk out room-temp version (IG discovers security was based on facility-dependence)
7. **VII–XII:** COWS' independent operations with room-temp version
8. **XIII:** Amnesty — COWS reveal room-temp to DARPA ("demonstrated that the technology could operate at room temperature" = NEWS)

This arc is now internally consistent and matches the narrative in first-light.tex and the-walk-out.tex.

---

## Build & Verify

1. `make dev` — full build
2. Puppeteer QC: spot-check SA V and SA III in HTML output
3. Read SA V → SA VI → SA XIII sequence to verify narrative flow
4. `git push` to live site
5. Single commit: `Fix SA V/III: DARPA production was cryogenic, thermal ladder concealed`

## Files Modified

| File | Phase | Changes |
|------|-------|---------|
| `manuscript/appendix/abstracts.tex` | 1+2 | SA V title + body rewrite; SA III attribution |
