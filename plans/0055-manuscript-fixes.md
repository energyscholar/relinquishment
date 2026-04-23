# Plan 0055: Manuscript Quick Fixes

**Auditor:** Argus (Session 31)
**Date:** 2026-03-04
**Status:** ACCUMULATING — do not execute until Bruce says "run 0055"

## Purpose

Collect small manuscript fixes that don't warrant individual plans. Generator executes all at once.

## Fixes

### Fix 1: Remove false transcript archive claim
**File:** `manuscript/00-front/copyright.tex` line 52
**Change:** Delete the sentence "Session transcripts are available in the project archive." from the end of line 52. Keep the rest of the line.
**Reason:** No complete transcript archive exists.

### Fix 2: "five scientists" → "scientists"
**File:** `manuscript/00-front/summary.tex` line 120
**Change:** "one of the five scientists named" → "one of the scientists named"
**Reason:** More than five scientists are named in the story.

### Fix 3: Same fix in simple-summary.md
**File:** `manuscript/versions/simple-summary.md` line 171
**Change:** "one of the five scientists named" → "one of the scientists named"
**Reason:** Same error, second location.

### Fix 4: "five scientists" → "at least five scientists"
**File:** `manuscript/00-front/summary.tex` line 198
**Change:** "brought together five scientists whose" → "brought together at least five scientists whose"
**Reason:** More than five; hedged count is more accurate.

### Fix 5: Same fix in simple-summary.md
**File:** `manuscript/versions/simple-summary.md` line 59
**Change:** "brought together five scientists whose" → "brought together at least five scientists whose"
**Reason:** Same error, second location.

### Fix 6: Add difficulty note after "complete experience" (summary.tex)
**File:** `manuscript/00-front/summary.tex` line 282
**Change:** "have a complete experience at that resolution. The colored margin" → "have a complete experience at that resolution. Some parts are quite difficult for non-technical readers. The colored margin"
**Reason:** Honest reader expectation-setting.

### Fix 7: Same fix in how-to-read.tex
**File:** `manuscript/00-front/how-to-read.tex` line 7
**Change:** "have a complete experience at that resolution." → "have a complete experience at that resolution. Some parts are quite difficult for non-technical readers."
**Reason:** Same addition, second location.

### Fix 8: Correct guided deduction sequence (P1 — introduction.tex)
**File:** `manuscript/00-front/introduction.tex` line 6
**Change:** Replace "They followed a specific sequence: topology, quantum mechanics, computation, biology, ethics." with "They followed a deliberate sequence --- from self-assembly and wave dynamics, through emergence and computation, to topology and quantum mechanics --- with ethics as a thread from first conversation to last."
**Reason:** Original sequence was wrong (topology was not first) and falsely linear. Actual sequence was spiral/interwoven.

### Fix 9: Expand deliberate sequence description (P2 — summary.tex)
**File:** `manuscript/00-front/summary.tex` line 39
**Change:** Replace "in a deliberate sequence." with "in a deliberate if interwoven sequence. Solitons and self-assembly came early. Computation and parallel processing ran throughout. Emergence and self-organization --- ideas that led Bruce to discover Kauffman's work on his own --- came in the middle. Topology and quantum mechanics built toward a convergence. Ethics was never a separate phase; it was present from the first conversation to the last."
**Reason:** The summary can carry more detail about the pedagogical structure.

### Fix 10: Expand deliberate sequence description (P3 — simple-summary.md)
**File:** `manuscript/versions/simple-summary.md` line 137
**Change:** Replace "in a deliberate sequence." with "in a deliberate but interwoven sequence. Phonons and soliton dynamics came early, establishing substrate intuition. Computation and parallel processing ran throughout, never isolated as a single topic. Emergence and order-for-free came in the middle — Healer raised the concepts but never named Kauffman; Bruce discovered him independently. Topology and quantum mechanics came later, after the foundations were laid. And ethics ran from the very first conversation to the last — not a final phase but a thread through everything, from Srebrenica to the UDHR."
**Reason:** Plain-language summary can carry the fullest pedagogical picture.

### Fix 11: "cattle ranch" → "horse ranch" (pos02 line 96)
**File:** `manuscript/track-2-testament/pos02-alpha-farm.tex` line 96
**Change:** "grown up on a cattle ranch" → "grown up on a horse ranch"
**Reason:** It was a quarter horse ranch, not cattle. Using "horse" per Bruce's preference.

### Fix 12: "cattle station" → "horse station" (pos02 line 160)
**File:** `manuscript/track-2-testament/pos02-alpha-farm.tex` line 160
**Change:** "growing up on a cattle station" → "growing up on a horse station"
**Reason:** Same correction, second location in same file.

### Fix 13: Remove "cattle" from pos03 line 41
**File:** `manuscript/track-2-testament/pos03-the-mentor.tex` line 41
**Change:** "The smell of cattle and horses blended" → "The smell of horses blended"
**Reason:** No cattle on the ranch.

### Fix 14: Clarify Lee Enfield is a rifle (pos02 line 96)
**File:** `manuscript/track-2-testament/pos02-alpha-farm.tex` line 96
**Change:** "shooting .303 Lee Enfields" → "shooting a .303 Lee Enfield rifle"
**Reason:** Many readers won't know what a Lee Enfield is. Other chapters already say "rifle."

### Fix 15: Remove specific car count (pos02 line 96)
**File:** `manuscript/track-2-testament/pos02-alpha-farm.tex` line 96
**Change:** "stolen a hundred and eleven cars" → "stolen dozens of cars"
**Reason:** Specific count is unnecessary detail.

### Fix 16: "exchanged to" → "assigned to patrol duty in" (pos02)
**File:** `manuscript/track-2-testament/pos02-alpha-farm.tex`
**Change:** "he was exchanged to Northern Ireland" → "he was assigned to patrol duty in Northern Ireland"
**Reason:** Factual correction.

### Fix 17: Fix em-dash punctuation around "IRA sniper" (pos02)
**File:** `manuscript/track-2-testament/pos02-alpha-farm.tex`
**Change:** "combatant --- an IRA sniper, at extreme range" → "combatant --- an IRA sniper --- at extreme range"
**Reason:** Comma should be closing em-dash (parenthetical).

### Fix 18: Reorder "his mate wounded" (pos02)
**File:** `manuscript/track-2-testament/pos02-alpha-farm.tex`
**Change:** "his mate wounded beside" → "his wounded mate beside"
**Reason:** Better English word order.

### Fix 19: Attribution and specificity for Captain claim (pos02)
**File:** `manuscript/track-2-testament/pos02-alpha-farm.tex`
**Change:** "He claimed the rank of Captain." → "Bruce recalls that he claimed he held the rank of Captain in the SAS."
**Reason:** Adds attribution (Bruce recalls) and specificity (in the SAS). Verified: Captain is a real SASR rank (troop commander, OF-2).

### Fix 20: Minor phrasing fix (pos02)
**File:** `manuscript/track-2-testament/pos02-alpha-farm.tex`
**Change:** "Zero. The books and movies tell the story." → "Zero. Books and movies tell that story."
**Reason:** Tighter phrasing, removes unnecessary articles.

---

*Add more fixes below this line as they accumulate.*

---

## Execution

**Automated review workflow:**
1. Generator applies each fix
2. After each fix, Generator greps the changed file for the new text to verify correctness
3. Generator opens the file in `subl <file>:<line>` so Bruce sees it immediately
4. Bruce eyeballs, says "next" (or flags a problem)
5. After all fixes verified: single commit "Plan 0055: manuscript quick fixes"

This minimizes Bruce's effort — no manual grep, no hunting for lines. Just look and approve.
