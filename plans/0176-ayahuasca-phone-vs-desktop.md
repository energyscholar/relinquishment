# Plan 0176 — Ayahuasca: Phone vs Desktop Persona Matrix

**Status:** QUEUED. Do not execute until BOTH:
1. Plan 0175 (phone-paragraph pass) has shipped and been pushed.
2. User says keyword `ayahuasca` to authorize the run.

**Type:** Tier-0 mental scoring, two-device matrix. No real-API sweetspot calls (per `feedback-no-sweetspot-until-budget.md`).

## Goal

Measure the device-delta for each persona. Same text, two reading surfaces (phone + desktop), two-axis scoring per persona. Surface where phone vs desktop actually changes the read — and where it doesn't.

## Why this is worth doing

- Bruce reads on phone; many target readers do too. Prior persona audits implicitly assumed one reading mode.
- Plan 0175 is a phone-specific intervention; this run measures whether it delivered (phone reads should now match or approach desktop reads for density-sensitive personas like Jane).
- Desktop reads surface dense-prose signals that phone reads mask (long grafs read fine on desktop; a phone reader bounces on them without registering "density" as the cause).
- Two-device scoring gives us a cleaner decomposition: **content signal** (what both devices agree on) vs **format signal** (where they disagree).

## The 10-persona panel

Use the established panel. Bruce referenced "9" — flag on invocation and confirm whether to drop one (likely Mike, who doesn't advance to p3 under current reads) or keep all 10. Default: all 10.

Chen, Jane, Reeves, Rachel, Doctorow, Arjun, Pastor Mike, Amir, Yusuf, Wei.

## Surfaces under test

Three rounds, same as prior audits:

- **Round 1:** p1 (hook.tex at HEAD after 0175)
- **Round 2:** p1 + p2 (hook + summary.tex at HEAD after 0175)
- **Round 3:** p3 sampler — `spine/the-flat.tex`, `spine/interlude-01.tex`, `record/the-handler.tex` — for personas who advance.

## Two-device simulation method

For each persona, Auditor simulates two distinct reading sessions:

**Desktop read:**
- Single-column 70ch-wide render, full screen.
- User can skim ahead, backtrack, see paragraph structure at a glance.
- Long paragraphs read as "dense but navigable."
- Hovertips: reader may hover freely, see rich panels.

**Phone read:**
- Thumb-scroll, ~1 paragraph visible per screen.
- No skim-ahead affordance — reading is linear and committed.
- Long paragraphs read as "where does this end?"
- Hovertips: tap-based, more friction than hover, often skipped.
- Reader patience is a function of next-paragraph-preview, not content alone.

**Scoring per persona per device per round:** GREEN+ / GREEN / YELLOW / BOUNCE, with one-line rationale.

## Output format

Three tables (one per round), each 10 rows × 3 columns:

| Persona | Desktop | Phone | Δ-note |
|---|---|---|---|
| Chen | GREEN+ | GREEN | hovertip friction cost |
| Jane | GREEN | GREEN | (was YELLOW pre-0175) |
| ... | | | |

Plus summary commentary section:

1. **Where device disagrees:** which personas have Δ ≥ 1 level between devices, and why.
2. **Where device agrees:** content-locked reads — agreement means the signal is content, not format.
3. **0175 delta:** compare this run's phone-column to the pre-0175 phone reads from the prior audit. Did Jane finish p2? Did any other persona improve on phone?
4. **Format-driven findings:** specific grafs/sections that read differently on phone vs desktop, with one-line recommendation per finding (may seed future plan).

## Out of scope

- Real-API sweetspot runs (blocked per `feedback-no-sweetspot-until-budget.md`).
- Any content changes. This is pure measurement.
- Tablet, e-reader, audio, or other reading modes — phone + desktop only.
- Internationalization / translation variants.

## Acceptance

- Three matrix tables produced (R1/R2/R3).
- Δ-note column populated for every persona on every round where devices disagree.
- Summary commentary covers the four sections listed above.
- 0175 delta explicitly called out (with before/after on Jane specifically).

## Re-engagement trigger

User message containing keyword `ayahuasca` after Plan 0175 has shipped. At that point Auditor runs the matrix inline (no Generator handoff needed — this is scoring, not code).

## Dependencies

- **Blocked by:** Plan 0175 ship + push + website deploy.
- **Blocks:** nothing — this is measurement, results may inform future plans but no downstream plan is queued against this one.
