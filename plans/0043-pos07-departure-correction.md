# Plan 0043: pos07 "The Departure" — Departure Section Correction

**Auditor:** Argus
**Date:** 2026-02-24
**Depends on:** Plan 0038 (Surgery 4 already applied — this plan corrects that surgery's departure text)
**Phase:** Single phase (section replacement)

---

## Context

Plan 0038 Surgery 4 rewrote pos07's departure section (lines 94-107). Session 20 UQ extraction (38 prompts) revealed multiple factual errors in that text. Bruce corrected the emotional register and key facts:

**What's WRONG in current text (lines 98-106):**
1. "In August 2006 I informed Healer that I could no longer assist him" — Bruce was TOLD his services wouldn't be required, not the other way around. Month is September, not August.
2. "I was sick of waiting for something to happen" — Not the emotional register. He was dedicated, not frustrated.
3. "David told me that, because my children could not be protected, I was now a security risk" — Partially correct but the framing implies David was delivering bad news to Bruce. The UQ says it differently: Bruce was vetted and turned down.
4. "I did not understand, at the time, what I was walking away from" — He didn't walk away. He was told to stop.
5. "The departure was not a decision. It was a collapse" — WRONG per Session 20 correction. Not collapse. Being told "your services will not be required."
6. "The decision came later, slowly, one piece of evidence at a time" — The break was instant ("Lightning Rod" triggered it), not gradual.
7. Emotional register throughout: "exhausted, financially ruined, terrified" — doesn't match UQ. Correct register: "I was no less dedicated but I didn't know what I had been dedicated to."

**What's RIGHT and should be preserved:**
- Line 102: "The project that proposed to protect all of humanity could not protect one man's daughters." (This is good — keep or adapt)
- The Joy analysis section (lines 17-90) is CORRECT and UNTOUCHED by this plan
- The A/B/C framing at lines 34 and 90 is CORRECT and UNTOUCHED

**Source:** `~/software/aurasys-memory/research/session20-uq-extraction.md` — pos07 correction section + pos29 "The Vetting Rejection" section.

**Voice model:** tracktwo — 1st-person personal ("I" not "Bruce"). See pos02-alpha-farm.tex for gold standard.

---

## Constraints

1. Do NOT modify anything before line 94 (`\section*{The Departure}`)
2. Preserve `\section*{The Departure}` heading
3. Preserve the `\srcnote` line (line 96)
4. Preserve `\chapterreturn` as final line
5. Do NOT add `\aidraft{}` wrappers — this is Bruce's voice based on UQ extraction
6. Do NOT modify Joy analysis section (lines 17-90) or A/B/C framing (lines 34, 90)
7. Use `Possibility~A/B/C` phrasing for any three-possibilities references

---

## File to Modify

| # | File | Action |
|---|------|--------|
| 1 | `manuscript/track-2-testament/pos07-the-departure.tex` | Replace lines 98-107 (departure narrative only) |

---

## Current Text to Replace

Replace everything from line 98 through line 107 (before `\chapterreturn`). That is, replace:

```latex
In August 2006 I informed Healer that I could no longer assist him, and that I was sick of waiting for something to happen.  At about the same time David and his friends decided, quite correctly, that I was now a bad security risk.

David told me that, because my children could not be protected, I was now a security risk to the project.  He also told me that I had been rejected for membership in the cDc.  In September of 2006 David and I parted.

The project that proposed to protect all of humanity could not protect one man's daughters.

I did not understand, at the time, what I was walking away from. I knew David was extraordinary. I knew the science was real --- the physics checked out, the mathematics converged, the predictions held. But I was exhausted, financially ruined, and terrified for my daughters. The white hot secret was still burning, but I no longer had the strength to carry it.

It would take me six years to begin understanding what had happened. Another six to start writing it down. And another six before anyone would listen. The departure was not a decision. It was a collapse. The decision came later, slowly, one piece of evidence at a time.
```

## New Text

```latex
In September 2006, I was told my services would not be required. My children could not be protected --- the divorce, the custody arrangements, the impossibility of shielding them from what was coming. David delivered this without cruelty. It was an operational assessment, not a rejection of me as a person. The full significance of that assessment --- what they needed protection from --- belongs to a chapter not yet written.

The project that proposed to protect all of humanity could not protect one man's daughters.

David and I parted. His decision, not mine. He said a fond goodbye but didn't drag it out. He was not a man who lingered.

I was no less dedicated. But I didn't know what I had been dedicated to. That realization would take years to arrive --- and when it did, it would not come gradually. It would come all at once, triggered by two words in a public message, and it would take three days to assimilate.

Under Possibility~A, the ``vetting rejection'' was a convenient exit from a relationship built on deception --- David leaving before the story fell apart. Under Possibility~B, David may have been involved in sensitive work, but framing children as security vulnerabilities imports the language of espionage onto what may have been a simpler situation. Under Possibility~C, a man who had been selected for a role in something extraordinary was told he couldn't continue, and spent the next six years locked behind glass --- able to think about what had happened but unable to speak it.
```

---

## Acceptance Criteria

1. `make` compiles without errors
2. Lines 1-97 of the file are UNCHANGED (Joy analysis, both A/B/C framing paragraphs, both srcnotes, settrack, chapter heading)
3. `\chapterreturn` is the final LaTeX command
4. No `\aidraft{}` wrappers appear in the new text
5. "September 2006" (not August) is used
6. Bruce is TOLD his services won't be required (passive, not active departure)
7. "I was no less dedicated but I didn't know what I had been dedicated to" appears
8. The word "collapse" does NOT appear
9. The phrase "walking away" does NOT appear
10. A/B/C framing is present (all three possibilities)
11. Uses `Possibility~A/B/C` phrasing (LaTeX non-breaking space)
12. The "three days" and "two words" forward-reference to pos29's "The Break" section
13. Report word count of departure section (should be 150-250 words)

---

## Generator Handoff Prompt

```
You are the Generator. Read the plan at:
~/software/relinquishment/plans/0043-pos07-departure-correction.md

In the file:
manuscript/track-2-testament/pos07-the-departure.tex

Replace the departure narrative (lines 98-107, everything between the \srcnote
and \chapterreturn) with the corrected text provided in the plan.

Do NOT modify anything before line 98. Preserve \chapterreturn as the final line.
The Joy analysis section (lines 17-90) and A/B/C framing (lines 34, 90) are
UNTOUCHED.

After replacement:
1. Run `make` and verify compilation
2. Verify all 13 acceptance criteria
3. Report word count of the departure section

Report completion.
```

---

## Red Team Record

**Red team:** Self-review during plan writing.

| # | Finding | Severity | Resolution |
|---|---------|----------|------------|
| 1 | New text forward-references "two words in a public message" and "three days" — these events are in pos29 (The Silence). Plan 0041 covers pos29 in detail. Verify no contradiction. | LOW | Checked against Plan 0041 text: pos29's "The Break" section describes "Lightning Rod" trigger, three days of flood. Forward reference is consistent. |
| 2 | "He also told me that I had been rejected for membership in the cDc" — this detail is in the current text (line 100) but NOT in Session 20 UQ extraction. Dropping it. | MEDIUM | Decision: omit. If Bruce wants it back, he can add during his writing pass. UQ didn't mention it; don't include unconfirmed details. |
| 3 | Current text's "white hot secret" metaphor (line 104) is a good phrase but embedded in wrong framing. | LOW | Omitted. The metaphor is from DMS MVP import, not from UQ. Bruce's actual words were more restrained. |
| 4 | New A/B/C block uses "locked behind glass" — this phrase also appears in Plan 0041's pos29 text. Deliberate echo or unintentional duplication? | LOW | Deliberate echo. pos07 plants the phrase as forward reference; pos29 develops it as the section's emotional core ("Exile from yourself"). The reader encounters it first in pos07 and recognizes it in pos29. |

**Verdict:** PASS. No CRITICAL or HIGH issues found.
