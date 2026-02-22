# Plan 0025: Manuscript Hygiene (Spiral Markers + Invariant Checks + Confirmed Failures)

**Purpose:** Mark intentional spiral repetitions so they're distinguishable from accidental duplicates. Add automated invariant checks to the Makefile. Fix confirmed critical violations found during audit.

**Prerequisite:** Plan 0024 complete.

**Deliverables:**
- `% SPIRAL-REPEAT:` markers on all intentional repetitions
- `make check` target catching critical invariant violations
- Fix "Healer told" violation in pos26
- COWS/COWs capitalization normalized
- Voice convention comments in all chapter headers
- Terminology reference file

**Commit format:** `Plan 0025 phase N: description`

---

## Context for Generator

**You have NO conversation history. Everything you need is in this file and the files it references.**

### Book Structure
- 35 chapters across 5 directories: `bridge/`, `track-1-confession/`, `track-2-testament/`, `track-3-awakening/`, `convergence/`
- Plus front/back matter in `manuscript/` root
- Pedagogical spiral: same concepts taught at increasing depth across chapters
- Three tracks with different voices (see Phase 2)

### Critical Rules
1. **Healer's method = GUIDED DEDUCTION.** Healer never told Bruce anything classified. Bruce DEDUCED the classified program from conversations about public-domain topics. NEVER write "Healer told Bruce" or "Lane told Bruce."
2. **Three-possibilities framing:** Every claim about the classified program must be hedged.
3. **COWS** = all caps, always. It's an acronym (Conspiracy Of World Saving). Never "COWs" or "cows" when referring to the faction.

---

## Phase 1: Spiral-Repeat Markers

### Step 1.1: Identify All Repeated Phrases

Search the entire `manuscript/` directory (excluding `staging/`, `sources/`, `raw/`) for these known repeated phrases:

```bash
grep -rn "forgiveness than permission" manuscript/ --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
grep -rn "Why the Future Doesn't Need Us" manuscript/ --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
grep -rn "Universal Declaration of Human Rights" manuscript/ --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
grep -rn "Conspiracy Of World Sav" manuscript/ --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
grep -rn "brash and daring warrior-scholar" manuscript/ --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
grep -rn "edge of chaos" manuscript/ --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
grep -rn "it is easier to get" manuscript/ --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
grep -rn "topological quantum neural network" manuscript/ --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
```

Also search for any OTHER phrases that appear in 3+ .tex files — these are candidate unintentional duplicates.

### Step 1.2: Classify and Mark

For each repeated phrase, determine:
- **INTENTIONAL** — spiral pedagogy, thematic through-line, or subtitle echo
- **ACCIDENTAL** — same passage imported twice from different sources
- **UNCERTAIN** — flag for Bruce's review

Add a LaTeX comment ABOVE the line containing the repeat:

```latex
% SPIRAL-REPEAT: "forgiveness than permission" — subtitle/through-line, also in pos03, pos18, pos26, pos27, title, cover, colophon, summary, timeline, abstracts, copyright
It is easier to get forgiveness than permission.
```

For accidental duplicates, add:
```latex
% DUPLICATE-FLAG: "passage description" — also in posNN. Review needed: keep here, remove, or differentiate.
```

For uncertain cases:
```latex
% REPEAT-REVIEW: "phrase" — appears in N files. Bruce: intentional spiral or accidental?
```

### Step 1.3: Add Convention Comment to main.tex

At the top of `main.tex`, after the existing comments, add:

```latex
% === REPETITION TRACKING CONVENTION ===
% SPIRAL-REPEAT: Intentional pedagogical repetition (same concept at increasing depth)
% DUPLICATE-FLAG: Suspected accidental duplication (review needed)
% REPEAT-REVIEW: Classification uncertain (Bruce decides)
% Search: grep -rn "SPIRAL-REPEAT\|DUPLICATE-FLAG\|REPEAT-REVIEW" manuscript/
```

---

## Phase 2: Voice Convention Headers

### Step 2.1: Add Voice Comment to Every Chapter

Add a voice convention comment after the `\settrack{}` line in every chapter .tex file:

**Bridge chapters** (`bridge/`):
```latex
\settrack{trackbridge}
% VOICE: expository/pedagogical — teaches concepts, no narrative events, no "the COWS did X"
```

**Track 1 chapters** (`track-1-confession/`):
```latex
\settrack{trackone}
% VOICE: 3rd-person scientific/reconstructive — "According to this account..." / "The proposition holds..."
```

**Track 2 chapters** (`track-2-testament/`):
```latex
\settrack{tracktwo}
% VOICE: 1st-person personal (Bruce) — "I" not "Bruce". Personal/investigative voice.
```

**Track 3 chapters** (`track-3-awakening/`):
```latex
\settrack{trackthree}
% VOICE: mixed speculative/philosophical — can use both 1st and 3rd person, speculative tone
```

**Convergence** (`convergence/`):
```latex
\settrack{trackconv}
% VOICE: convergence — all three voices present, all three themes engaged
```

### Step 2.2: Flag Voice Violations (Report Only)

Search for voice contamination but DO NOT FIX — report for Bruce's review:

```bash
# 1st-person in Track 1 (should be 3rd-person)
grep -rn "\bI \b\|I've\|I'm\|\bmy \b" manuscript/track-1-confession/*.tex | grep -v "^%\|srcnote\|aidraft\|quote\|textit"

# 3rd-person "Bruce" in Track 2 (should be 1st-person "I")
grep -rn "\bBruce\b" manuscript/track-2-testament/*.tex | grep -v "^%\|srcnote\|aidraft"
```

Report findings with file and line number. DO NOT modify prose — voice fixes require Bruce's editorial judgment.

---

## Phase 3: Critical Fixes

### Step 3.1: Fix "Healer Told" Violation

**File:** `manuscript/track-3-awakening/pos26-interdiction.tex`

Search for any instance of "Healer told" or "told Bruce" in this file. Replace with guided-deduction framing:
- "Healer told Bruce about X" → "Bruce's reconstruction suggests X" or "According to this account, X"
- Verify no other files contain "Healer told" or "Lane told" (excluding staging/sources/raw and LaTeX comments)

### Step 3.2: Normalize COWS Capitalization

Search for "COWs" (mixed case) across all .tex files. Replace with "COWS" (all caps).

```bash
grep -rn "\bCOWs\b" manuscript/ --include="*.tex" | grep -v staging | grep -v sources | grep -v raw
```

Replace every instance. Do NOT replace "cows" (lowercase) if it refers to actual animals. Check context.

### Step 3.3: Walk-Out Date Consistency

Search for walk-out date references. The canonical range is "1994 or 1995" (honest uncertainty). Any timeline entry showing just "1994" without the range should be updated to "1994--1995".

```bash
grep -rn "1994\|1995" manuscript/ --include="*.tex" | grep -i "walk\|pocket\|mosfet\|enlighten"
```

---

## Phase 4: Makefile Invariant Checks

### Step 4.1: Add `check` Target

Add to `~/software/relinquishment/Makefile`:

```makefile
# Manuscript invariant checks
check:
	@echo "=== Invariant Checks ==="
	@echo -n "Healer-told violation: "
	@grep -rn "Healer told\|Lane told" manuscript/ --include="*.tex" \
		| grep -v "^%\|staging/\|sources/\|raw/" \
		&& (echo "FAIL — guided deduction invariant violated"; exit 1) \
		|| echo "PASS"
	@echo -n "COWs capitalization: "
	@grep -rn "\bCOWs\b" manuscript/ --include="*.tex" \
		| grep -v "^%\|staging/\|sources/\|raw/" \
		&& (echo "FAIL — use COWS not COWs"; exit 1) \
		|| echo "PASS"
	@echo -n "Spiral-repeat markers present: "
	@grep -rl "SPIRAL-REPEAT" manuscript/ --include="*.tex" | wc -l | xargs -I{} echo "{} files marked"
	@echo -n "Voice headers present: "
	@grep -rl "% VOICE:" manuscript/ --include="*.tex" | wc -l | xargs -I{} echo "{} files marked"
	@echo -n "aidraftchapter coverage: "
	@echo "$$(grep -rl 'aidraftchapter' manuscript/ --include='*.tex' | grep -v staging | wc -l) of $$(find manuscript -name 'pos*.tex' ! -path '*/staging/*' | wc -l) chapters marked"
	@echo "=== Done ==="
```

### Step 4.2: Add `check-strict` Target (Future Use)

```makefile
# Strict checks — add more as conventions stabilize
check-strict: check
	@echo "=== Strict Checks ==="
	@echo -n "Unhedged assertions: "
	@grep -rn "COWS built\|COWS created\|Guardian is\|Guardian was" manuscript/ --include="*.tex" \
		| grep -v "^%\|staging/\|sources/\|raw/\|Possibility\|proposition\|surmise\|deduce\|if.*true\|under.*C\|According" \
		&& echo "WARNING — possible unhedged assertions (review needed)" \
		|| echo "PASS"
	@echo "=== Done ==="
```

---

## Phase 5: Terminology Reference

### Step 5.1: Create Terminology File

Create `~/software/relinquishment/plans/terminology.md`:

```markdown
# Terminology Conventions

Generators: use these exact forms. Automated checks enforce some of these.

| Term | Correct | Wrong | Notes |
|------|---------|-------|-------|
| COWS | COWS | COWs, cows | All-caps acronym: Conspiracy Of World Saving |
| Guardian | Guardian (capital G) | guardian | Proper noun — the entity's name |
| TQNN | TQNN | tqnn, Tqnn | All-caps acronym |
| Healer | Healer | healer | Handle/proper noun when referring to David Lane |
| UDHR | UDHR or "Universal Declaration of Human Rights" | udhr | Full name on first use per chapter |
| FQHE | FQHE | fqhe | Acronym, define on first use in bridge chapters |
| 2DEG | 2DEG | 2deg, 2-DEG | Standard physics notation |
| Walk-out date | "1994 or 1995" or "1994--1995" | "1994" alone | Honest uncertainty — always show range |
| Bill Joy article | "Why the Future Doesn't Need Us" (2000) | Various shortened forms | Italicize title |
| Guided deduction | "Bruce deduced" / "Bruce's reconstruction" | "Healer told Bruce" | CRITICAL — see MEMORY.md #12 |
```

---

## Phase 6: Verification

### Step 6.1: Run `make check`

```bash
cd ~/software/relinquishment && make check
```

All invariant checks must pass.

### Step 6.2: Run `make dev`

Build must compile clean (0 errors).

### Step 6.3: Verify Marker Counts

```bash
grep -rc "SPIRAL-REPEAT" manuscript/ --include="*.tex" | grep -v ":0" | sort
grep -rc "DUPLICATE-FLAG" manuscript/ --include="*.tex" | grep -v ":0" | sort
grep -rc "REPEAT-REVIEW" manuscript/ --include="*.tex" | grep -v ":0" | sort
grep -rc "% VOICE:" manuscript/ --include="*.tex" | grep -v ":0" | sort
```

Report counts.

---

## Test Cases

| ID | Criterion | Method |
|----|-----------|--------|
| TC1 | Zero "Healer told" / "Lane told" in .tex files (excluding comments/staging) | `make check` |
| TC2 | Zero "COWs" in .tex files (excluding comments/staging) | `make check` |
| TC3 | All 35+ chapter .tex files have `% VOICE:` header | `grep -rc` count |
| TC4 | All known intentional repeats marked with `% SPIRAL-REPEAT:` | Manual count vs known list |
| TC5 | Convention comment present in `main.tex` | `grep "REPETITION TRACKING"` |
| TC6 | `make check` passes all checks | Build output |
| TC7 | `make dev` compiles clean | Build output |
| TC8 | `plans/terminology.md` exists and contains all terms | `test -s` |
| TC9 | Voice violation report generated (findings listed, NOT fixed) | Report in commit message or stdout |

---

## Important Constraints

1. **Do NOT fix voice violations.** Report them only. Voice fixes require Bruce's editorial judgment.
2. **Do NOT modify prose content** beyond the specific fixes in Phase 3 (Healer-told, COWs, date range).
3. **Do NOT add `\aidraftchapter`** to chapters that don't already have it — that's a separate audit decision.
4. **Do NOT remove any intentional repetitions.** Only MARK them.
5. **Commit one commit per phase.** Message format: `Plan 0025 phase N: description`
6. **If `make check` fails after Phase 3 fixes, STOP and investigate.** The fix may have introduced a new problem.

---

## File Reference (Absolute Paths)

| File | Role |
|------|------|
| `~/software/relinquishment/manuscript/**/*.tex` | All chapter files — markers added |
| `~/software/relinquishment/manuscript/main.tex` | Convention comment added |
| `~/software/relinquishment/manuscript/track-3-awakening/pos26-interdiction.tex` | Critical fix: "Healer told" |
| `~/software/relinquishment/Makefile` | `check` and `check-strict` targets added |
| `~/software/relinquishment/plans/terminology.md` | NEW — terminology reference |
