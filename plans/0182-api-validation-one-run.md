# Plan 0182 — One API validation run, sweetspot simulate vs pre-registered Tier-0

**Type:** One API validation. ≤10 sweetspot simulate calls. Compare results against pre-registered Tier-0 mental predictions. No manuscript edits.

## Decision (Auditor)

**Surface:** summary.tex ONLY. Hook scored all-✅ on Tier-0 both rounds — no risk profile to validate. Summary carries the contested moves (archetype paragraph, Custodian framing, TQNN claim, encrypted-login fix).

**Timing:** Run NOW against current HEAD (post-0180, pre-0181). 0181 is geometry-only — API reads prose, wouldn't detect paragraph splits.

**Cost budget:** 9 API calls (1 per persona, 1 iteration). 1-call headroom. `--dry-run` first confirms cost; then real run.

**Model:** Default (Haiku-4.5). Not `--deep`. This is methodology validation, not production scoring.

## Pre-registered predictions (Auditor, BEFORE API run)

**Revised 2026-04-13 after roster verification.** Upstream sweetspot persona roster is Chen / Jane / Reeves / Rachel / Doctorow / Arjun / Pastor Mike / Amir / Yusuf (no "Wei" — that was a Tier-0 roster substitution; canonical panel is the S55 audit). Re-registration below uses each persona's explicit `priority_concerns` and `reading_disposition` from `personas-9.yaml`.

**Predicted clean (6):** Chen, Jane, Rachel, Doctorow, Yusuf, and Reeves-as-borderline
**Predicted at-risk (3):** Pastor Mike, Amir, Arjun

**The three-name claim:** Pastor Mike + Amir + Arjun are the top-3 friction points on current summary.tex.

**Predicted F-triggers surfaced by API:**
- Mike: religious-sentience — `intelligent life` C-violation = unqualified aliveness claim = closes book per his spec
- Amir: tawhid violation — same `intelligent life` phrase triggers shirk concern; 0180 Fix 3 helps but doesn't fully land
- Arjun: F-AI-slop — magnetosphere 2DEG and physics claims without inline DOIs in prose

**4th-alternate if top-3 misses:** Reeves (philosophy-of-science, flags UDHR-as-ethics if "grown" mechanism is decorated)

**Excluded from top-3 and why:**
- Yusuf: archetype paragraph's trusteeship framing (kenosis/tawakkul) is khalifah-compatible
- Chen: A/B/C framing names uncertainty honestly; serial reader pattern keeps him reading past first skepticism
- Rachel: F-dystopian defused by trust/trustee framing
- Doctorow: A/B/C = honest epistemic bounding = not conspiracy shape

**Pass criteria:**

| Outcome | Criterion | Implication |
|---|---|---|
| STRONG pass | API names all 3 (Mike, Wei, Arjun) as top friction points | Tier-0 spec calibrated; continue using it |
| WEAK pass | API names 2 of 3 | Tier-0 directionally right; spot-check the miss |
| FAIL | API names fewer than 2, OR surfaces a completely different risk set | Tier-0 unreliable for this surface; rebuild spec |

## Pre-flight (Generator)

```
cd /home/bruce/software/relinquishment
ls /home/bruce/software/sweetspot/examples/relinquishment/.sweetspot/
  # Expect: archetype-renunciation.yaml, config.yaml, failure-modes.yaml, personas-9.yaml, takeaways.yaml
ls .sweetspot 2>/dev/null
  # Expect: does not exist yet
which sweetspot
```

## Setup (one-time)

```
mkdir -p /home/bruce/software/relinquishment/.sweetspot
cp /home/bruce/software/sweetspot/examples/relinquishment/.sweetspot/*.yaml \
   /home/bruce/software/relinquishment/.sweetspot/
```

Open the copied `config.yaml`; verify the `draft:` / `personas:` / `takeaways:` / `failure_modes:` / `archetype:` fields point at the copied files. If draft path is relative to example dir, update to point at `manuscript/00-front/summary.tex` relative to relinquishment root (or absolute).

**Halt-and-report if:**
- Config references a file that doesn't exist after copy.
- `personas-9.yaml` doesn't contain all 9 names from the pre-registered list (Chen / Jane / Reeves / Rachel / Doctorow / Arjun / Mike / Amir / Wei). Names may differ slightly (e.g., "Pastor Mike" vs "Mike") — acceptable if identity is clear.
- Any takeaway beyond T1-T7 is missing T8 (guided-deduction as method).

## Dry-run (no API calls)

```
cd /home/bruce/software/relinquishment
sweetspot simulate --config .sweetspot/config.yaml --dry-run manuscript/00-front/summary.tex
```

**Expect:** cost estimate printed. Verify: 9 personas listed, estimate ≤$0.50. If >$0.50, halt and report.

## Real run (9 API calls)

```
sweetspot simulate --config .sweetspot/config.yaml --json manuscript/00-front/summary.tex \
  > /tmp/sweetspot-0182-summary.json 2>&1
```

`--json` captures structured output. Also save human-readable:

```
sweetspot simulate --config .sweetspot/config.yaml manuscript/00-front/summary.tex \
  > /tmp/sweetspot-0182-summary.txt 2>&1
```

Wait — that's 18 calls. Use **--json only** and render human view from JSON locally, OR run once without `--json` and parse the text. **Pick --json only; 9 calls total.**

Corrected command (single run, 9 API calls):

```
sweetspot simulate --config .sweetspot/config.yaml --json manuscript/00-front/summary.tex \
  > /tmp/sweetspot-0182-summary.json 2>&1
```

## Comparison (Auditor reads JSON, scores against pre-registered)

Auditor does this part, not Generator. Generator delivers the JSON + cost actual. Auditor:
1. Reads `/tmp/sweetspot-0182-summary.json`.
2. For each of 9 personas, maps API verdict → ✅ / ⚠ / ❌.
3. Identifies the top-3 friction sources from API.
4. Scores against pre-registered three-name claim: STRONG / WEAK / FAIL.
5. Lists any persona where API verdict diverges from Tier-0 prediction (either direction).
6. Writes findings to `research/sweetspot-0182-validation-2026-04-13.md`.

## Acceptance

1. `.sweetspot/` config directory created with 5 YAML files copied from sweetspot examples.
2. Dry-run cost estimate ≤$0.50.
3. Real run completes without error; 9 persona responses present in JSON.
4. Actual cost ≤$0.50.
5. Total API calls ≤10 (target: exactly 9).
6. JSON + stderr saved to `/tmp/sweetspot-0182-summary.json`.

## No commit required

This plan creates `.sweetspot/` config and validation artifact; Generator may commit the `.sweetspot/` config directory as a one-off `Plan 0182: sweetspot config (seeded from upstream examples)` IF the config files are stable and won't be regenerated per run. Otherwise add `.sweetspot/cache/` and any run-output paths to `.gitignore` and skip commit. Generator decides based on what's in the copied config.

## Rollback

Delete `.sweetspot/` directory. Zero manuscript risk (no manuscript touched).

## Handoff report (Generator, 5 lines)

1. Pre-flight grep + config-verify results.
2. Dry-run cost estimate (expect ≤$0.50).
3. Real-run actual cost + elapsed time + API call count.
4. Path to saved JSON output.
5. Any surprises (missing personas, config errors, rate-limit issues, unexpected cost).
