# Plan 0047: Fix Quote Attributions + Add "Know Thyself" + Shorten Ack

## Context

Bruce requested: fix the two quotes in the Jay Hanson acknowledgment entry with correct original wording and proper attributions. Add "Know Thyself" as a third quote. Shorten the overall acknowledgments.

## Target File

`manuscript/99-back/acknowledgements.tex`

## Task 1: Fix Hanson Entry (line 30)

### Current text (line 30):
```latex
Jay Hanson built dieoff.org --- the first serious attempt to connect energy depletion, evolutionary biology, and human social behavior into a single framework. We corresponded regularly for more than fifteen years. His work on the parable of the tribes and the impossibility of voluntary relinquishment shaped my thinking as no one had before. He taught me two quotes I have never forgotten: ``If a path to the better there be, it begins first with a look at the worst,'' and ``Treason doth never prosper. What's the reason? An' if it prosper, none dare call it treason.'' He died in a diving accident in 2019. I wish he could have read this too.
```

### Replacement text:
```latex
Jay Hanson built dieoff.org --- the first serious attempt to connect energy depletion, evolutionary biology, and human social behavior into a single framework. We corresponded for more than fifteen years. His work on the parable of the tribes shaped my thinking as no one had before. He taught me three quotes I have never forgotten: ``If way to the Better there be, it exacts a full look at the Worst'' (Thomas Hardy), ``Treason doth never prosper: what's the reason? Why, if it prosper, none dare call it treason'' (Sir John Harington), and ``Know Thyself'' (Delphi). He died in a diving accident in 2019.
```

### Changes:
1. **Hardy quote fixed:** "If a path to the better there be, it begins first with a look at the worst" → "If way to the Better there be, it exacts a full look at the Worst" — Thomas Hardy, "In Tenebris II" (1895-96)
2. **Harington quote fixed:** "An' if it prosper" → "Why, if it prosper" — Sir John Harington, *Epigrams* (c. 1618)
3. **"Know Thyself" added:** Ancient Greek maxim inscribed at the Temple of Apollo at Delphi. Attributed to Thales, Chilon, or Socrates. "(Delphi)" is the cleanest attribution.
4. **"two quotes" → "three quotes"**
5. **Trimmed:** Removed "regularly" from "corresponded regularly", removed "and the impossibility of voluntary relinquishment" (the parable of the tribes IS about the impossibility of voluntary relinquishment — redundant), removed "I wish he could have read this too" (already said for Crandall — repetition weakens both).
6. **Net reduction:** ~20 words shorter despite adding a quote.

## Task 2: Shorten Acknowledgments

The current ack is 58 lines. Bruce asked to shorten. Recommendations (Generator should confirm with Bruce if unsure):

### Keep as-is (essential):
- Healer (line 4) — origin
- Genevieve (line 6) — co-author credit
- Daughters (line 8) — family
- Karen (line 10) — family
- Angerman (line 12) — evidence
- Bannon (line 14) — evidence
- Metzger (line 16) — origin
- Crandall (line 20) — physics education
- Bury (line 22) — academic
- Mysak (line 24) — academic
- DMS holders (line 26) — custodians
- Hanson (line 30) — intellectual foundation
- Hagens (line 32) — intellectual foundation
- Claude/AI (line 58) — disclosure

### Candidates for trimming or removal (Bruce decides):
- **Brian Kahn (line 18):** One sentence. Could merge with Metzger as "early mentors."
- **Margaret Anderson (line 34):** One sentence. Generic.
- **John Sechrest (line 36):** One sentence. Entrepreneurship, tangential.
- **Nancy Calichio / Chris Osgood (line 40):** Two people, one sentence. School teachers.
- **Robin Macomber (line 42):** One sentence. "Contributions ongoing" is vague.
- **Mark Swanson (line 44):** Three sentences. Could trim to one.
- **Jeff Bradford (line 46):** One sentence. Chess.
- **Kim (line 48):** Two sentences. Emotionally significant but readers don't know who she is.
- **Teri Turner (line 50):** One sentence. Cryptic.
- **Tanja (line 52):** One sentence. Dog.
- **Magdalena (line 54):** Two sentences. Current life.

### Recommendation:
Don't cut anyone. Bruce included these people for a reason. But consider consolidating the shorter entries into a grouped paragraph: "Early mentors shaped the path: Brian Kahn in security, Nancy Calichio and Chris Osgood at the Grammar School in Putney, Margaret Anderson in literature, John Sechrest in entrepreneurship." This preserves names while reducing word count by ~40%.

## Verification

1. [ ] Hardy quote matches original: "If way to the Better there be, it exacts a full look at the Worst"
2. [ ] Harington quote matches original: "Treason doth never prosper: what's the reason? For if it prosper, none dare call it treason"
3. [ ] "Know Thyself" present with "(Delphi)" attribution
4. [ ] "three quotes" not "two quotes"
5. [ ] No gratuitous cuts to people Bruce chose to include
6. [ ] LaTeX compiles

## Generator Handoff

You are the Generator. Read plan `plans/0047-ack-quotes-fix.md`.

Task: Execute Task 1 (Hanson entry fix) in `manuscript/99-back/acknowledgements.tex` line 30. For Task 2 (shortening), only execute if Bruce has indicated what to cut. Otherwise, leave for Bruce's writing pass.
