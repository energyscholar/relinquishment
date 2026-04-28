# Plan 0025v2: Manuscript Hygiene — Remaining Items

**Purpose:** Fix the three remaining issues from original Plan 0025: one prose violation, one reference error, one Makefile bug. Add spiral-repeat markers to remaining files.

**Supersedes:** Plan 0025 (most of which was already executed in Sessions 13-14).

**Prerequisite:** Plan 0024 complete (✓).

**Deliverables:**
- pos28 line 68 "Healer told" resolved
- terminology.md "David Lane" corrected to clarify pseudonym
- Makefile `check` target bug fixed (FAIL+PASS double-print)
- SPIRAL-REPEAT markers added to remaining chapter files
- `make check` passes clean

**Commit format:** `Plan 0025v2 phase N: description`

---

## Context for Generator

**You have NO conversation history. Everything you need is in this file and the files it references.**

### What's Already Done (DO NOT REDO)
- Voice headers: 36/36 files ✓
- COWs normalization: 0 violations ✓
- `make check` and `make check-strict` targets exist ✓
- `plans/terminology.md` exists ✓
- main.tex convention comment exists ✓
- SPIRAL-REPEAT markers: 28 files already marked ✓

### Critical Rules
1. **Healer's method = GUIDED DEDUCTION.** Healer never told Bruce classified information. Bruce DEDUCED the classified program. NEVER write "Healer told Bruce" about TQNN/classified content.
2. **"David Lane" / "Lane" = PSEUDONYM.** Not Healer's real name.
3. **Three-possibilities framing:** Every claim about the classified program must be hedged.

---

## Phase 1: Fix pos28 "Healer Told" Violation

### Context

File: `manuscript/convergence/pos28-surrender.tex`, line 68.

Current text:
```
Bruce asked confirmatory questions. Healer told him that he and the other
two COWS had surrendered their master keys. They no longer had any recall
power or control over Custodian. The relinquishment was complete and
irrevocable.
```

This triggers the `make check` "Healer told" detector.

### The Nuance

This is a gray area. The guided-deduction rule exists because Healer never disclosed *classified science* to Bruce — Bruce deduced the TQNN program from public-domain conversations. But in this scene, Healer is announcing the *completion of an event* ("It is done"), not disclosing classified science. "We surrendered the master keys" is a personal statement about an action, not a physics lesson.

**However:** The Makefile check cannot distinguish these cases, and the pattern "Healer told him" reads identically to a guided-deduction violation. The fix should preserve the scene's emotional directness while avoiding the flagged pattern.

### Fix

Replace line 68 with:

```latex
Bruce asked confirmatory questions. He and the other two COWS had surrendered their master keys, Healer said. They no longer had any recall power or control over Custodian. The relinquishment was complete and irrevocable.
```

This preserves Healer as the speaker (he IS telling Bruce — this is a personal confession, not classified disclosure) but restructures the sentence to avoid the "Healer told" grep pattern. The inversion ("Healer said" at end) is a common literary construction for reported speech.

### Verify

```bash
grep -n "Healer told\|Lane told" manuscript/convergence/pos28-surrender.tex
```

Should return nothing.

---

## Phase 2: Fix Terminology Reference

### File: `plans/terminology.md`, line 10

Current:
```
| Healer | Healer | healer | Handle/proper noun when referring to David Lane |
```

This implies "David Lane" is Healer's real name. It is NOT — "Lane" is a pseudonym used in Bruce's earlier documents.

### Fix

Replace with:
```
| Healer | Healer | healer | Handle/proper noun. "David Lane" is a pseudonym (not his real name) |
```

---

## Phase 3: Fix Makefile Check Bugs

### The Bug

**Both** the Healer-told check (lines 102-107) and the COWs check (lines 108-111) use the same broken pattern:

```makefile
&& (echo "FAIL — ..."; exit 1) \
|| echo "PASS"
```

The `exit 1` runs inside a subshell `(...)`. It exits the subshell with code 1, but since `A && B || C` is parsed as `(A && B) || C`, when B fails (exit 1), the `||` branch fires and prints "PASS" too. Result: the check prints BOTH "FAIL" and "PASS" and Make continues instead of stopping. This bug affects BOTH checks.

### Fix

Replace the Healer-told check (lines 101-107) with:

```makefile
	@echo -n "Healer-told violation: "
	@if grep -rn "Healer told\|Lane told" manuscript/ --include="*.tex" \
		| grep -v "staging/\|sources/\|raw/" \
		| grep -v "^[^:]*:[0-9]*:%"  \
		| grep -v "told me\|told this\|told an elaborate" \
		| grep -q .; then \
		grep -rn "Healer told\|Lane told" manuscript/ --include="*.tex" \
			| grep -v "staging/\|sources/\|raw/" \
			| grep -v "^[^:]*:[0-9]*:%" \
			| grep -v "told me\|told this\|told an elaborate"; \
		echo "FAIL — guided deduction invariant violated"; \
		exit 1; \
	else \
		echo "PASS"; \
	fi
```

Replace the COWs check (lines 108-111) with:

```makefile
	@echo -n "COWs capitalization: "
	@if grep -rn "\bCOWs\b" manuscript/ --include="*.tex" \
		| grep -v "staging/\|sources/\|raw/" \
		| grep -v "^[^:]*:[0-9]*:%" \
		| grep -q .; then \
		grep -rn "\bCOWs\b" manuscript/ --include="*.tex" \
			| grep -v "staging/\|sources/\|raw/" \
			| grep -v "^[^:]*:[0-9]*:%"; \
		echo "FAIL — use COWS not COWs"; \
		exit 1; \
	else \
		echo "PASS"; \
	fi
```

Changes:
1. Uses if/then/else instead of `&&`/`||` for BOTH checks — no ambiguous exit codes.
2. `exit 1` is now in the main shell, not a subshell — Make will stop on failure.
3. Added `"told an elaborate"` to Healer-told allowlist — pos28 line 74 ("told an elaborate lie") is legitimate three-possibilities prose under Possibility A.

### Verify

```bash
cd ~/software/relinquishment && make check
```

Should print "PASS" for all checks with no double-print.

---

## Phase 4: Add SPIRAL-REPEAT Markers to Remaining Chapter Files

### Files Needing Markers

The following pos*.tex chapter files do NOT yet have SPIRAL-REPEAT markers. For each file, search for any of the known repeated phrases (listed below). If a phrase appears, add a `% SPIRAL-REPEAT:` comment above it. If NO repeated phrases appear in the file, no marker is needed — skip it.

**Files to check:**
```
manuscript/bridge/pos04-the-code-war.tex
manuscript/bridge/pos05-kangaroos.tex
manuscript/bridge/pos08-dual-use.tex
manuscript/bridge/pos09-the-factoring-game.tex
manuscript/bridge/pos10-the-braid.tex
manuscript/bridge/pos11-the-experiment.tex
manuscript/bridge/pos14-growing-a-mind.tex
manuscript/convergence/pos28-surrender.tex
manuscript/convergence/pos35-the-question.tex
manuscript/track-1-confession/pos17-the-capability.tex
manuscript/track-1-confession/pos20-the-network.tex
manuscript/track-1-confession/pos26-interdiction.tex
manuscript/track-2-testament/pos02-alpha-farm.tex
manuscript/track-2-testament/pos03-the-mentor.tex
manuscript/track-2-testament/pos23-the-weight.tex
manuscript/track-2-testament/pos29-the-silence.tex
manuscript/track-2-testament/pos33-digital-doppelganger.tex
manuscript/track-3-awakening/pos32-the-magnetosphere.tex
```

**Pedagogical spiral phrases to search for** (phrases that teach the same concept at increasing depth across chapters):
1. `forgiveness than permission` — subtitle/through-line
2. `Why the Future Doesn't Need Us` — Bill Joy reference
3. `brash and daring warrior-scholar` — Healer characterization
4. `edge of chaos` — Kauffman concept
5. `guided deduction` — pedagogical method

**DO NOT mark these as spiral repeats** — they are structural vocabulary that appears throughout because it's the book's terminology, NOT pedagogical repetition at increasing depth:
- COWS, TQNN, FQHE, UDHR, 2DEG (acronyms/proper nouns used everywhere)
- Possibility A/B/C, "three possibilities" (framing device used in every hedged passage)
- Custodian, Healer (character names)

The distinction: "forgiveness than permission" appearing in 3 chapters is a deliberate spiral teaching the concept at different depths. "TQNN" appearing in 20 chapters is just the word being used. Only mark the former.

**Marker format:**
```latex
% SPIRAL-REPEAT: "phrase" — context/purpose, also in [list other files where it appears]
```

**Rules:**
- Only mark phrases that appear in OTHER files too (that's what makes them repeats)
- Do NOT mark first-use or sole-use instances
- Do NOT add DUPLICATE-FLAG or REPEAT-REVIEW markers — those require Bruce's judgment
- If uncertain whether something is a repeat, skip it. Under-marking is better than over-marking.

### Also check front/back matter (non-pos files without markers):

```
manuscript/00-front/corrections.tex
manuscript/00-front/genevieve-preface.tex
manuscript/00-front/how-to-read.tex
manuscript/00-front/not-claimed.tex
manuscript/00-front/preface.tex
manuscript/99-back/acknowledgements.tex
manuscript/99-back/verification.tex
manuscript/appendix/glossary.tex
manuscript/appendix/predictions.tex
manuscript/appendix/rlhf-bias.tex
```

Same rules: search for repeated phrases, add markers where found.

---

## Phase 5: Verification

### Step 5.1: Run `make check`

```bash
cd ~/software/relinquishment && make check
```

**Expected output:**
```
=== Invariant Checks ===
Healer-told violation: PASS
COWs capitalization: PASS
Spiral-repeat markers present: NN files marked
Voice headers present: 36 files marked
aidraftchapter coverage: 13 of 36 chapters marked
=== Done ===
```

All checks must pass. No double-print on Healer-told line.

### Step 5.2: Run `make dev`

```bash
cd ~/software/relinquishment && make dev
```

Build must compile clean (0 errors).

### Step 5.3: Report marker counts

```bash
grep -rc "SPIRAL-REPEAT" manuscript/ --include="*.tex" | grep -v ":0" | sort
```

Report total count. Should be ≥ 28 (existing) plus whatever was added.

---

## Test Cases

| ID | Criterion | Method |
|----|-----------|--------|
| TC1 | Zero "Healer told" / "Lane told" in .tex files (excluding comments/staging/allowlisted) | `make check` shows PASS (not FAIL+PASS) |
| TC2 | `make check` exits non-zero on violation, zero on clean | Verify exit code |
| TC3 | terminology.md clarifies "David Lane" as pseudonym | `grep "pseudonym" plans/terminology.md` |
| TC4 | pos28 line 68 no longer contains "Healer told him" | `grep -n "Healer told" manuscript/convergence/pos28-surrender.tex` returns nothing |
| TC5 | `make dev` compiles clean | Build output |
| TC6 | Spiral-repeat markers added to chapter files that contain repeated phrases | Count ≥ 28 |
| TC7 | pos28 line 74 "told an elaborate lie" NOT flagged by `make check` | Allowlist working |

---

## Important Constraints

1. **Do NOT redo voice headers, COWs fixes, or other already-complete work.**
2. **Do NOT modify prose** beyond the single fix in Phase 1 (pos28 line 68).
3. **Do NOT add spiral-repeat markers to files that have no repeated phrases.** Not every file needs a marker.
4. **Commit one commit per phase.** Message format: `Plan 0025v2 phase N: description`
5. **If `make check` fails after Phase 1 and Phase 3 fixes, STOP and investigate.**

---

## File Reference (Absolute Paths)

| File | Role |
|------|------|
| `~/software/relinquishment/manuscript/convergence/pos28-surrender.tex` | Phase 1: "Healer told" fix |
| `~/software/relinquishment/plans/terminology.md` | Phase 2: pseudonym clarification |
| `~/software/relinquishment/Makefile` | Phase 3: check target bug fix |
| `~/software/relinquishment/manuscript/**/*.tex` | Phase 4: spiral-repeat markers |
