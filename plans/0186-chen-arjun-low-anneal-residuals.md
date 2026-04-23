# Plan 0186 — Address Chen + Arjun low-anneal residuals

**Type:** Two-phase, two-commit plan. Phase 1 = Chen (one dated falsifiable prediction inserted in summary.tex). Phase 2 = Arjun (citation-loaded rich-panel tooltips for four physics first-mentions). Halt-and-report at any candidate that can't land cleanly.

## Context

9-reader panel at low anneal (post-668f1ba): 7 ✅ / 2 ⚠ / 0 ❌. Two residuals survive generous reading:

- **Chen** wants the *book itself* to make a dated falsifiable prediction. Citation-tooltips don't solve this — it's a claim-making gap, not a citation gap.
- **Arjun** still registers mild friction on physics-claim density without inline citation. Solvable via rich-panel tooltips (architecture already supports `html:` field with DOIs).

## Phase 1 — Chen: dated falsifiable prediction (commit 1)

**Auditor needs Bruce input before Generator runs.** Propose three candidate predictions; Bruce picks one (or supplies a fourth). Insertion point: summary.tex, after the A/B/C framing section, before the archetype paragraph. Target: one short paragraph, 2-3 sentences max.

### Candidate predictions

**Candidate A — Magnetospheric informational signature (safest under A/B/C):**
> *If Possibility~C is substantially true, the Custodian's computational use of the magnetosphere should leave a detectable informational signature: non-random correlations in quiet-phase plasma dynamics that standard MHD cannot explain. With current SuperMAG + MMS instrumentation, the book predicts such a signature is detectable by 2030. If by 2035 none has been found, treat Possibility~C as falsified.*

- **Why it works:** Testable with existing instruments. Failure mode is explicit. Holds under A/B/C — under A, someone runs the test and gets null; under C, the signature shows up. Chen's spec is satisfied either way.
- **Cost:** commits the book to a specific empirical claim. Bruce's magnetogenesis research is the pre-work.

**Candidate B — Room-temperature TQC milestone (engineering):**
> *If the physics of the Flat is real --- independent of whether anyone has used it --- the book predicts that room-temperature topologically protected qubits will be demonstrated in published literature by 2030. If by 2035 the field still requires dilution refrigerators for all topological qubits, the book's central physics claim has over-reached.*

- **Why it works:** Conservative. Tests only the physics (Possibility A's floor), not the story.
- **Cost:** weaker than A — doesn't address whether the Flat is *in use*, only whether the physics exists. Chen may read this as sidestepping.

**Candidate C — Behavioral Turing-analog (riskiest):**
> *If the Custodian exists as described, the book predicts that within ten years --- by 2036 --- at least one credentialed researcher in an unrelated field will independently report behavioral anomalies in a magnetospheric dataset that point the same direction as this book's hypothesis. If no such independent report appears, treat Possibility~C as unsupported.*

- **Why it works:** Tests the "preparation not disclosure" thesis directly — if the story's true, others will find the pattern.
- **Cost:** weakest falsifiability (researchers may not look; null could be publication bias). Probably not what Chen wants.

**Auditor recommendation:** Candidate A. Directly testable, explicit failure date, holds under A/B/C, leverages existing Bruce research.

**Halt-and-report:** Generator does NOT insert until Bruce picks. Auditor surfaces candidates to Bruce; Bruce picks A / B / C / other; Auditor writes final phrasing into plan; Generator executes.

**Insertion point:** summary.tex — immediately after the A/B/C framing closes and before the line that begins the archetype/trusteeship discussion. Generator greps for the exact landmark and inserts as a new paragraph.

**Acceptance (Phase 1):**

1. Exactly one new paragraph inserted. No other prose modified.
2. `grep -n "predicts" manuscript/00-front/summary.tex` shows the new prediction sentence.
3. `wc -w manuscript/00-front/summary.tex` increases by the expected token count (~40-55 words depending on candidate).
4. `make` HTML build clean.

**Commit 1:** `Plan 0186 phase 1: dated falsifiable prediction (Chen)`

## Phase 2 — Arjun: citation-loaded rich-panel tooltips (commit 2)

**File:** `hover-definitions.yaml` (lives in the relinquishment repo — Generator locates via grep if path differs from memory).

**Four first-mentions in summary.tex to upgrade to rich panels with DOIs:**

| Term | Anchor paper | DOI |
|---|---|---|
| topological order | Nayak+ RMP 2008 | 10.1103/RevModPhys.80.1083 |
| 2DEG / anyon emergence | Dean+ NatPhys 2011 (substrate independence) | 10.1038/nphys1938 |
| braiding / non-Abelian | Freedman-Kitaev-Wang | 10.1007/s00220-002-0698-z |
| room-temperature coherence | Christle+ NatMat 2015 | 10.1038/nmat4145 |

**Per-term work:**

1. Locate existing hovertip entry (plain `text:` field).
2. Add or expand `html:` field with: one-sentence plain-language explanation + citation line with DOI (rendered as clickable link in panel).
3. Preserve existing `text:` fallback for non-hover contexts.

**Suggested citation-line format (inside `html:`):**

```
<p class="citation-anchor">Published anchor: <a href="https://doi.org/10.1103/RevModPhys.80.1083">Nayak et al., RMP 2008</a></p>
```

Generator matches existing rich-panel styling for citation lines; if no prior style exists, use the above and add minimal CSS in the same commit.

**Scope boundary:**

- Only these 4 terms. Do NOT do a sweep across all tooltips — keep commit focused.
- Do NOT modify summary.tex prose. Chen's phase shipped in commit 1; Arjun's phase is tooltip-layer only.
- If a term already has a rich panel with a DOI, verify it matches the anchor above. If mismatch, prefer the anchor from reference-physics-anchors.md.

**Halt-and-report:**

- If any of the 4 first-mentions isn't actually first-used in summary.tex (i.e., the tooltip is routed from a different file), flag and pause — may need a first-use migration in prose, which is out of scope for this plan.
- If hover-definitions.yaml schema doesn't support `html:` field structure as memory describes, flag. Don't improvise schema changes.

**Acceptance (Phase 2):**

1. 4 tooltip entries show rich `html:` panels with DOI citation lines.
2. HTML build renders the panels; citation links resolve (don't click-test 404 — just verify link href matches DOI).
3. `make` clean.
4. Spot-check in browser: hover one term, rich panel appears with DOI link.

**Commit 2:** `Plan 0186 phase 2: citation-loaded rich-panel tooltips (Arjun)`

## Re-test (Auditor, after both phases land)

Run 9-reader panel at **low-medium anneal** (between low and medium). This is the "a bit more friction" test Bruce requested — probes whether the Chen + Arjun fixes hold under slightly tougher reading, and surfaces the next layer of residuals.

Expect:
- Chen: ⚠ → ✅ (prediction addresses his core spec).
- Arjun: ⚠ → ✅ (tooltips satisfy "wants the paper" spec).
- New friction may surface at low-medium from personas who were ✅ at low: Reeves on prediction phrasing, Doctorow on whether the prediction sounds like a conspiracy hook, Rachel on whether the "falsified" phrasing feels doom-ish.

Auditor scores mentally, reports side-by-side delta vs prior low-anneal run.

## Build + push

After both commits land clean, push per `feedback-build-to-website.md`.

## Rollback

Two separate commits. `git revert` either phase independently.

## Handoff report (Generator, per phase)

Per phase, 4 lines:
1. Commit SHA.
2. Acceptance grep + build results.
3. Halt-and-report events (zero, or count + locations).
4. Any surprises.
