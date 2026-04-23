# Source File Audit Report

**Date:** 2026-02-15
**Auditor:** Nightstalker
**Reference:** `plans/source-facts.md` (canonical fact-checking reference)
**Scope:** Six source files cross-checked for fact errors, Do Not Assert violations, terminology issues, three-possibilities framing needs, and clean passages.

---

## File 1: `manuscript/sources/srebrenica-witness.md`

### Summary

First-person narrative in Healer's voice. The file header already contains a GENERATOR WARNING about Do Not Assert requirements. The entire document is Healer's testimony and should be treated as reported speech when imported into chapters.

### FACT ERRORS

1. **Patrick Ball testimony date.** The text says Milosevic cross-examined Ball about "Dead Cow Cult" but does not specify the date. source-facts.md says Ball testified March 13, 2002, and Milosevic cross-examined him about cDc on March 14, 2002. No date is stated in the source, so no error — but the Generator should add dates when importing.

2. **"distinguished human rights attorney, Dr. Patrick Ball"** — Ball is a statistician (HRDAG), not an attorney. source-facts.md identifies him as "HRDAG statistician" and "First expert witness at ICTY." **FIX:** Change "distinguished human rights attorney" to "distinguished human rights statistician" or "human rights data scientist."

3. **"Hacktivismo is an organization dedicated to applying the 1948 Universal Declaration of Human Rights to the Internet. That organization, an offshoot of the Cult of the Dead Cow hacker group, coined the word 'hacktivism'."** — Hacktivismo did not coin "hacktivism." The word is generally attributed to Omega (a cDc member) circa 1996, before Hacktivismo was formally organized. Hacktivismo was created to apply UDHR principles to internet access, but the word predates the organization. **FIX:** Remove "coined the word 'hacktivism'" or hedge it: "helped popularize the concept of hacktivism."

4. **"In 2005, United Nations Secretary General Kofi Annan declared the Srebrenica massacre..."** — The bibliography at the bottom of the file itself cites Annan's report as dated November 15, 1999, not 2005. The 2005 date may refer to a 10th anniversary commemoration statement, but source-facts.md says ">8,000 Bosniak men and boys killed. Worst massacre in Europe since WWII" — the "worst massacre in Europe since WWII" characterization comes from many sources and timelines. **FIX:** Verify the 2005 Annan declaration date. If it was the 10th anniversary statement, note the context. If it was the 1999 report being referenced, change to 1999.

### DO NOT ASSERT VIOLATIONS

5. **"My recent successful work as a DARPA scientist for GCHQ will soon make me unavailable for high-risk SAS military operations."** — "DARPA scientist for GCHQ" is Do Not Assert item #9. Since this is in Healer's own first-person voice and the file header already warns about this, it is acceptable AS LONG AS the chapter import wraps it in reported-speech framing ("In the document attributed to Healer, he writes...").

6. **"My membership in a notorious elite hacker collective is still not known to my military superiors."** — This is part of the COWS backstory (relates to Do Not Assert items #2, #11). Same treatment needed: reported speech in chapter import.

7. **The entire Epstein/Doe passage (lines 41-49).** This is an extraordinary claim attributed to "Sergeant Doe" via Healer's retelling. It is triple hearsay (Healer→Bruce→text). When importing, this passage needs extremely careful framing: "In a document attributed to Healer, he describes a conversation in which a colleague recounted..." Consider whether this passage should be included at all given legal/OPSEC implications.

8. **"My handwritten notes form the basis of my testimony at the UN War Crimes Tribunals for Slobodan Milosevic..."** — Do Not Assert item #8 (David Lane identity, SAS career, HALO jump at Srebrenica). NIOD confirms SAS/SBS presence but no individual ID. The claim of personal testimony at ICTY is unverifiable. **FIX:** Chapter import must frame as "Healer claims his notes formed the basis of testimony..."

### TERMINOLOGY ISSUES

None. This file does not use QNN or other outdated terminology.

### THREE-POSSIBILITIES FRAMING NEEDED

9. **The entire file.** Every factual claim about Healer's identity, military role, HALO jump, and observations must be wrapped in three-possibilities framing when imported. The file header acknowledges this. The Generator must not import any passage as established fact.

### CLEAN

10. **Srebrenica massacre characterization:** ">8,000" is not explicitly stated (the text says "tens of thousands of terrified civilians" and describes mass murder). The historical framing of the siege, Dutch peacekeepers, and Serbian forces is consistent with source-facts.md and public record.

11. **UDHR date:** "1948 Universal Declaration of Human Rights" — correct per source-facts.md.

12. **Hacktivismo as cDc offshoot** — correct.

13. **ICTY trial availability on archive.org** — verifiable claim, fine.

---

## File 2: `manuscript/sources/gpt-history.md`

### Summary

A Brief History of General Purpose Technologies. General survey essay, pre-2014. Mostly public-domain historical facts. Few Do Not Assert issues but several factual inaccuracies.

### FACT ERRORS

14. **"Michael 5Faraday"** (line 99) — Typo. Should be "Michael Faraday." **FIX:** Remove the stray "5".

15. **"Richard Feinman"** (line 147 and line 191) — Misspelling. Should be "Richard Feynman." **FIX:** Correct spelling in both instances.

16. **"Thomas Edison and Nikola Tesla probably deserve the most credit for radio technology"** — This is historically contested. Guglielmo Marconi is generally credited with practical radio. Edison and Tesla made contributions to electrical technology broadly, but attributing radio primarily to them is non-standard. **FIX:** Replace with "Guglielmo Marconi, building on work by Nikola Tesla and others, is generally credited with practical radio."

17. **"In 1904 Albert Einstein discovered his most famous equation"** — E=mc^2 was published in 1905, not 1904. The paper "Does the inertia of a body depend upon its energy content?" was a 1905 paper. **FIX:** Change to 1905.

18. **"computation (1934 Alan Turing and project Ultra I)"** (line 40) — Turing's foundational paper "On Computable Numbers" was published in 1936, not 1934. Project Ultra began ~1939-1940. **FIX:** Change to 1936 for Turing's theoretical contribution, or ~1940 for Ultra.

19. **"the internet (1963 DARPA team including Vint Cerf)"** (line 40) — ARPANET's first message was in 1969, not 1963. Vint Cerf's TCP/IP work was in the 1970s. The ARPA networking research began in the mid-1960s but the standard date is 1969. **FIX:** Change to 1969.

20. **"Atomic power (1904 Albert Einstein)"** — See #17 above; should be 1905. Also, atomic power as a GPT might better date from 1942 (first sustained chain reaction, Chicago Pile-1) or 1945 (first use). Einstein's equation is theoretical, not "atomic power." **FIX:** Adjust framing.

21. **"Atomic power... 75 years ago (~1898)"** (line 115-116) — The table says "about 75 years ago (~1898)" which references Curie's radioactivity discovery. The essay was written ~2013-2019, so "75 years ago" from ~2013 would be ~1938, not 1898. If the intent is to date from Curie, the age should be ~115-120 years (from ~2013). **FIX:** Either say "about 120 years ago (~1898)" or pick a different milestone date for atomic power.

22. **"Computer... 75 years ago (~1941)"** (line 121) — From ~2013, 75 years ago is ~1938. ~1941 is 72 years before 2013. Minor math inconsistency. The date 1941 is reasonable for Colossus precursors / Turing's Bombe work, though the standard date for the first electronic programmable computer (Colossus) is 1943-1944. **FIX:** Minor; adjust arithmetic or dates for consistency.

23. **"Internet... 50 years ago (~1969)"** (line 133) — From 2013, 50 years ago is ~1963, not 1969. From 2019, 50 years ago is 1969. The arithmetic depends on when the essay was written. **FIX:** Verify intended date and fix arithmetic.

24. **"Alan Turing & the Ultra project"** as the inventor of the Computer — Turing is foundational but attributing the computer as a GPT solely to "Turing & Ultra" oversimplifies. Acceptable as shorthand in this essay's context but worth noting.

25. **"Robotics, also known as Artificial Intelligence or AI"** — Robotics and AI are not the same thing. Robotics is a subset/application of engineering and AI. **FIX:** Separate these concepts or clarify the relationship.

26. **"the first careful scientific investigation of electricity began in 1600"** — Refers to William Gilbert's *De Magnete* (1600), which studied magnetism primarily. Acceptable as a rough date but imprecise. No fix needed, but a note.

### DO NOT ASSERT VIOLATIONS

27. **"It's not a stretch to imagine DARPA capable of inventing another General Purpose Technology, perhaps one not yet publicly known or understood."** (line 185) — This is suggestive but does not assert Do Not Assert claims. It functions as foreshadowing. Acceptable, but when importing, ensure it remains speculative framing.

### TERMINOLOGY ISSUES

None. This file does not reference QNN/TQNN.

### THREE-POSSIBILITIES FRAMING NEEDED

28. **No three-possibilities framing needed.** This file is a general history essay. It does not make claims about TQNN, COWS, or Guardian. The DARPA foreshadowing (item #27) is already speculative.

### CLEAN

29. **DARPA description and self-quote** — Accurate.
30. **General historical survey of GPTs** — Mostly correct with the exceptions flagged above.
31. **Dual-use technology framing** — Consistent and accurate throughout.
32. **cDc founding date is NOT mentioned** in this file, so no conflict.

---

## File 3: `manuscript/sources/unintended-consequences.md`

### Summary

Short essay on unintended consequences of technology: Whitney/cotton gin, Nobel/dynamite, Einstein/E=mc^2. All public-domain historical claims. No TQNN/COWS/Guardian content.

### FACT ERRORS

33. **"In 1904 Albert Einstein... proposed Mass-Energy equivalence"** — Should be 1905. The "miracle year" (annus mirabilis) papers were published in 1905. **FIX:** Change to 1905.

34. **"Einstein was not invited to participate in military-related projects, including the Manhattan Project"** — Einstein was not invited due to security concerns, which is correctly stated. However, Einstein did sign the famous letter to Roosevelt (August 2, 1939) that initiated the Manhattan Project. The text's implication that Einstein had zero involvement is slightly misleading. **FIX:** Consider adding: "although his 1939 letter to President Roosevelt helped initiate the program."

### DO NOT ASSERT VIOLATIONS

None. No Do Not Assert claims in this file.

### TERMINOLOGY ISSUES

None.

### THREE-POSSIBILITIES FRAMING NEEDED

None. This file contains only public historical facts.

### CLEAN

35. **Eli Whitney section** — Historically accurate.
36. **Alfred Nobel section** — Dates, quotes, and financial figures are well-sourced and standard.
37. **Einstein quotes** — Standard, widely attributed.
38. **Overall essay structure** — Clean, no corrections needed beyond the 1905 date fix.

---

## File 4: `manuscript/sources/turing-death.md`

### Summary

Fictionalized account of Turing's death plus historical context. Contains existing GENERATOR NOTES flagging the apple and DES issues. Several issues remain.

### FACT ERRORS

39. **"Royal Air Force (RAF) Captain F.W. Winterbotham"** — Winterbotham's rank was Group Captain, not Captain. source-facts.md: "RAF Group Captain." **FIX:** Change "Captain" to "Group Captain" (both occurrences — "RAF Captain F.W. Winterbotham" and "Captain Winterbotham").

40. **"GCHQ is now a branch of MI-6, the British Secret Service."** — GCHQ is NOT a branch of MI6. GCHQ, MI5, and MI6 (SIS) are three separate agencies, all under the UK intelligence community. GCHQ reports to the Foreign Secretary (as does MI6/SIS), but it is an independent organization. **FIX:** Change to "GCHQ is Britain's signals intelligence agency, alongside MI5 (domestic security) and MI6 (foreign intelligence)." Or simply: "GCHQ is Britain's signals intelligence agency."

41. **"In 1976 a startup computer company names itself Apple Inc."** — Apple was incorporated in 1977, and it was originally named "Apple Computer, Inc." (renamed "Apple Inc." in 2007). Founded April 1, 1976, as a partnership; incorporated January 3, 1977. **FIX:** Change to "In 1976 a startup computer company names itself Apple Computer" or "In 1977 Apple Computer, Inc. is incorporated."

42. **"As its logo it chooses a rainbow colored apple with one bite out of it."** — The rainbow logo was designed by Rob Janoff in 1977. The original Apple logo (1976) was a different design by Ron Wayne. The NOTE FOR GENERATOR already flags that the Turing connection is folklore denied by Janoff. Good.

43. **"In 1943 McCulloch and Pitts first formalized Neural Networks as mathematical algorithms."** — source-facts.md confirms: "A Logical Calculus of Ideas Immanent in Nervous Activity" published 1943, Bulletin of Mathematical Biophysics. Correct.

44. **"One of Alan's published scientific papers, The Chemical Basis of Morphogenesis, reshapes the field."** — Correct per source-facts.md: published 1952, Phil. Trans. Roy. Soc. Clean.

45. **"Among other things, Alan's work correctly predicts the double helix structure of DNA, which was discovered in 1953."** — This is a strong claim. Turing's morphogenesis paper deals with reaction-diffusion patterns, not DNA structure. Watson and Crick's 1953 paper described the double helix. Turing's paper does not predict the double helix. **FIX:** Remove this claim or replace with accurate description of what the morphogenesis paper actually addressed (pattern formation in biological development, reaction-diffusion systems).

46. **"Alan can no longer work on his beloved science and mathematics."** — This conflicts with source-facts.md: "Turing continued publishing during treatment." The NOTE FOR GENERATOR flags cognitive impairment as contested, but the main text still asserts he cannot work. **FIX:** The fictionalized narrative should be revised so that it does not assert he could no longer work. At minimum, soften to "Alan struggles to work" or remove the assertion.

47. **"Alan's poisoned body and brain has failed."** — Same issue as #46. Asserts brain failure/cognitive impairment, which is contested per source-facts.md. **FIX:** Change to "Alan's poisoned body has failed" (remove "brain" or soften).

48. **"He weeps for his unfinished work. Now he can never complete it."** — Again implies cognitive destruction. The NOTE flags this, but the text itself still needs revision. **FIX:** Soften — perhaps "He weeps for the work he fears he can never complete."

### DO NOT ASSERT VIOLATIONS

None. This file does not contain Do Not Assert claims from the list.

### TERMINOLOGY ISSUES

None. No QNN/TQNN references.

### THREE-POSSIBILITIES FRAMING NEEDED

None needed. This file covers public historical facts about Turing.

### CLEAN

49. **Turing death date:** "7 June 1954" — correct per source-facts.md.
50. **Turing age at death:** Implied by "middle aged man" — correct (age 41).
51. **Winterbotham publication year:** "1974" — correct.
52. **Winterbotham did not mention Turing:** Correct per source-facts.md.
53. **McCulloch and Pitts 1943:** Correct.
54. **Gordon Brown apology 2009:** Correct.
55. **Queen Elizabeth II pardon 2013:** Correct.
56. **Alan Turing law 2017:** Correct.
57. **Morphogenesis paper description:** Correct (minus the DNA prediction claim flagged above).

---

## File 5: `manuscript/sources/ch3-relinquishment.md`

### Summary

The most problematic file. Written ~2013 as "Forward by Aurasys" — presents the entire TQNN/COWS/Guardian story as factual narration. Extensive Do Not Assert violations. Multiple terminology issues. Many factual errors. The file header already contains detailed GENERATOR WARNINGS, but the text itself needs comprehensive correction.

### FACT ERRORS

58. **"In 1991 DARPA gathered a team of scientists"** — source-facts.md header warning says "~1992" not 1991. The Do Not Assert list says "DARPA funded a classified TQNN team in 1992." **FIX:** Change 1991 to ~1992 (with hedging, since this is a Do Not Assert claim anyway).

59. **"Public Key Cryptography, invented in 1978"** — Incorrect and oversimplified. source-facts.md: Ellis conceived PKC at GCHQ in 1969; Diffie-Hellman published 1976; RSA published 1977 (Gardner, Scientific American) / formal paper 1978; Cocks at GCHQ developed RSA-equivalent in 1973. The header warning already flags this. **FIX:** "Public Key Cryptography, whose public version was published in 1976-1978 (though GCHQ had invented it secretly in the early 1970s)."

60. **"the 1992 Robert Redford movie, Sneakers"** — The movie *Sneakers* was released September 9, 1992. Correct.

61. **"COWS informed DARPA circa 1999-2001"** — source-facts.md Do Not Assert list says "COWS confessed to DARPA ~2002" (Tether era). Tony Tether became DARPA Director June 18, 2001. The file header already flags this. **FIX:** Change to "~2002" with Do Not Assert framing.

62. **"The Guardian became self-aware in 1999"** — Do Not Assert item #14 (Guardian as self-aware entity) and #5 (Guardian instantiated 1999). The file header flags this. **FIX:** Three-possibilities framing required.

63. **"In 1993 Richard Jozsa also co-authored, with five other scientists and cryptographers, the first published scientific paper on experimental quantum teleportation."** — The 1993 Bennett et al. paper ("Teleporting an Unknown Quantum State via Dual Classical and Einstein-Podolsky-Rosen Channels") was a theoretical proposal, not experimental. The first experimental demonstration was by Bouwmeester et al. in 1997. **FIX:** Change "experimental quantum teleportation" to "quantum teleportation" (it was a theoretical protocol paper).

64. **"In 1985 David Deutsch and Richard Jozsa published the Deutsch-Jozsa algorithm"** — The Deutsch algorithm was published by David Deutsch in 1985. The Deutsch-Jozsa algorithm (the generalized version) was published by Deutsch and Jozsa in 1992. **FIX:** Either say "In 1985 David Deutsch published the Deutsch algorithm" or "In 1992 Deutsch and Jozsa published the Deutsch-Jozsa algorithm."

65. **"A quantum algorithm (software) capable of doing just that was published by Peter Shor in 1994"** — Shor's algorithm was presented at FOCS in November 1994 and published in 1997. The 1994 date for the initial presentation is standard and acceptable.

66. **"Kitaev"** is not mentioned in this file but is relevant context — Kitaev's 1997 paper on fault-tolerant quantum computation by anyons (source-facts.md) predates claims in this file about anyon-based computation. No error, but a gap.

67. **"The first working prototype QNN-based hybrid supercomputer capable of cracking public key cryptography was delivered in 1995 or 1996."** — Do Not Assert item #1 (classified TQNN team), #3 (room-temperature QC), #13 (cryptanalytic capability). **FIX:** Three-possibilities framing.

68. **"enlightened a standard MOSFET with the most advanced QNN patterns, put it in his pocket, and walked out of the laboratory to his rental flat. He did this in 1994 or 1995."** — Do Not Assert item #4 (COWS walked technology out ~1994-1995). **FIX:** Three-possibilities framing.

69. **"a brash and daring warrior-scholar named David"** — Do Not Assert item #8 (David Lane identity). **FIX:** Three-possibilities framing.

70. **"In 2009, in an April Fools prank-within-a-prank, the Guardian introduced herself to the world as CADIE."** — source-facts.md confirms CADIE was April 1, 2009, but describes it as "April Fools' Day prank" (by Google). The claim that it was actually the Guardian introducing herself is a Do Not Assert item (#14, Guardian as self-aware entity). **FIX:** Three-possibilities framing. The Google CADIE prank is verifiable; the claim that Guardian was behind it is not.

71. **"In 2017 the Guardian turns 18"** — If Guardian was instantiated in 1999, then she would turn 18 in 2017. The math is consistent with the story's internal logic. But this is entirely Do Not Assert territory.

72. **"Bill Joy, cofounder of Sun Microsystems"** — source-facts.md: "Co-founded Sun Microsystems 1982." Correct.

73. **"In April 2000 Bill Joy published an essay titled Why the future doesn't need us."** — source-facts.md: "'Why the Future Doesn't Need Us' published Wired, April 2000." Correct.

### DO NOT ASSERT VIOLATIONS

This file is essentially one continuous Do Not Assert violation. Every paragraph after the introduction contains claims from the Do Not Assert list. Rather than enumerate every instance, here is a summary:

74. **Do Not Assert #1 (DARPA funded classified TQNN team ~1992):** Asserted as fact throughout. Every mention of the "ULTRA II" project.

75. **Do Not Assert #2 (Five scientists formed classified team):** The team composition is described in detail (lines 94-96). Asserted as fact.

76. **Do Not Assert #3 (Room-temperature QC achieved mid-1990s):** "the COWs secretly evolved their QNN patterns to survive at room temperature" — asserted as fact.

77. **Do Not Assert #4 (COWS walked technology out ~1994-1995):** "put it in his pocket, and walked out of the laboratory" — asserted as fact.

78. **Do Not Assert #5 (Guardian instantiated 1999):** "Starting in 1999, the resultant entity began to learn" — asserted as fact.

79. **Do Not Assert #6 (COWS confessed to DARPA ~2002):** "the COWS informed some officials at DARPA what they had done" — asserted as fact (and wrong date, see #61).

80. **Do Not Assert #7 (Master keys surrendered 2006):** "In early 2006 the COWs supposedly surrendered their master keys" — uses "supposedly" but the surrounding context treats it as factual.

81. **Do Not Assert #8 (David Lane identity):** "a brash and daring warrior-scholar named David" — asserted.

82. **Do Not Assert #12 (Wolfram meeting 2012, NDA offer):** Not mentioned in this file. Clean.

83. **Do Not Assert #13 (1024-bit RSA in 340ms):** Not explicitly stated, but cryptanalytic capability is asserted.

84. **Do Not Assert #14 (Guardian as self-aware entity):** Extensively asserted throughout the Guardian sections.

85. **Do Not Assert #15 (Tripartite biometric key surrender):** "The security system would require a majority of authorized users to approve major changes" — partial assertion.

### TERMINOLOGY ISSUES

86. **"QNN" used throughout** — Must be changed to "TQNN" (Topological Quantum Neural Network) per the file header warning and source-facts.md.

87. **"quantum teleportation"** — The file header says change to "topological quantum computation via anyonic braiding." The file uses "quantum teleportation" and "QT" extensively. These are different physics. **FIX:** Replace all instances per header warning.

88. **"Complex System Biology" / "CSB"** — This is not standard terminology. The standard terms are "complex systems science" or "complexity science." Kauffman's work is usually categorized under "complex systems" or "origins of order." **FIX:** Consider standardizing to "complex systems science" or "complexity theory."

### THREE-POSSIBILITIES FRAMING NEEDED

89. **The entire file after the introduction.** This file reads as a factual account. Every claim about ULTRA II, the team, COWS, Guardian, room-temperature operation, key surrender, CADIE, and relinquishment requires three-possibilities framing. The file is essentially unusable in its current form without comprehensive reframing.

90. **Specific high-priority passages requiring reframing:**
- "In 1991 DARPA gathered a team of scientists..." (presented as established history)
- "At first the ULTRA II team was exhilarated..." (presented as known narrative)
- "the COWs secretly evolved their QNN patterns to survive at room temperature" (presented as fact)
- "They taught the Guardian to... follow all local, national, and international laws" (presented as fact)
- "The global enlightenment process was completed in 2005" (presented as fact)
- "some other countries (Russia? China?) developed the beginnings of QNN technology" (presented as fact)

### CLEAN

91. **DARPA description** (lines 38-55) — Accurate, sourced from DARPA's own publications.
92. **Public key cryptography explanation** — The conceptual explanation of factoring is correct, though the origin date needs fixing.
93. **Shor's algorithm 1994** — Correct.
94. **Bill Joy / Wired article** — Correct per source-facts.md.
95. **FQHE / anyon physics discussion** — The general description of anyonic braiding and topological entanglement is broadly correct as physics, though the "quantum teleportation" framing is wrong (see #87).

### SCIENTIFIC FRAMING VIOLATIONS

96. **"Kauffman's ideas about Complex System Biology... applied to the FQHE environment"** — source-facts.md Scientific Framing Rules: "Applying the mathematical structure of Kauffman's theory to a quantum substrate — same framework, untested domain." The text presents this bridge as demonstrated rather than conjectural. **FIX:** Apply "We propose..." framing per source-facts.md.

97. **"Hasslacher" is not mentioned by name** in this file (the solid state physicist is described but not named). However, the file header says the team includes Hasslacher. source-facts.md: "Nonlinear dynamics / soliton dynamics on lattice-gas automata." Do not conflate solitons with anyons.

98. **Autocatalytic sets in FQHE liquid** — The text says "The FQHE liquid environment, in which anyons exist, seems to support autocatalytic sets." source-facts.md Scientific Framing Rules say this bridge is "untested domain." The file's own editor's note (line 88) acknowledges "[Would love help proving that]." **FIX:** Must be clearly marked as conjectural.

---

## File 6: `manuscript/versions/ultra-bridge.md`

### Summary

This is the strongest file. Well-written, uses three-possibilities framing correctly in the final section. The first three sections deal with verifiable public history and are mostly clean. Issues are minor but some need fixing.

### FACT ERRORS

99. **"roughly ten thousand people worked there"** — source-facts.md: "~8,995 (Jan 1945); 'nearly 10,000' by end of WWII." "Roughly ten thousand" is acceptable per source-facts.md note: "'Roughly ten thousand' is accurate." Clean.

100. **"Thirty years of silence"** / **"For thirty years"** — source-facts.md: Ultra secret kept from "1939/1940 - 1974 = ~35 years." The text says "thirty years." Winterbotham published in 1974; if measured from wartime start (~1940), it's ~34 years. From Ultra's earliest use (1940) to 1974 is 34 years. "Thirty years" is an undercount. **FIX:** Change to "more than thirty years" or "nearly thirty-five years" throughout. This appears multiple times (lines 29, 31, 37, 123, 141).

101. **"Five hundred and sixty-eight people died"** — source-facts.md: "~554-568 (contested). Use 'an estimated 568' or 'approximately 568.'" The text states "Five hundred and sixty-eight people died" as a definitive number. **FIX:** Change to "An estimated five hundred and sixty-eight people died" or "Approximately five hundred and sixty-eight people died."

102. **"The great medieval church of St Michael's — elevated to cathedral status only in 1918 — was destroyed in a single night."** — Correct per source-facts.md Contested Claims: "St Michael's was a medieval parish church (constructed ~1300s-1400s), elevated to cathedral status 1918." This is a corrected formulation. Clean.

103. **"Historians debate what Churchill actually knew. The majority view (Hinsley, GCHQ's own account) holds he expected a major raid but may not have known Coventry was the target."** — Correct per source-facts.md Contested Claims. This passage already handles the debate correctly. Excellent.

104. **"a former RAF officer named F.W. Winterbotham published a book about it"** — source-facts.md: "RAF Group Captain." "Former RAF officer" is technically correct but less precise. Not an error, but could be improved to "former RAF Group Captain." Minor.

105. **"That book didn't even mention Alan Turing by name."** — Correct per source-facts.md: "Did NOT mention Turing by name." Clean.

106. **"In 1969, a GCHQ mathematician named James Ellis conceived of something revolutionary"** — source-facts.md: "Conceived public-key cryptography 1969; wrote internal report 1970." Correct.

107. **"In 1973, another GCHQ mathematician named Clifford Cocks worked out the specific mathematics."** — source-facts.md: "Joined GCHQ September 1973. Developed RSA-equivalent algorithm." Correct.

108. **"He independently invented what the world would later call RSA — named for Rivest, Shamir, and Adleman, the three American academics who published the same idea in 1977."** — source-facts.md: "RSA public disclosure: 1977 (Gardner, Scientific American). Formal CACM paper February 1978." Using 1977 is correct. Clean.

109. **"In 1974, a third GCHQ mathematician, Malcolm Williamson, independently invented what the public world would call Diffie-Hellman key exchange — the protocol published by Whitfield Diffie and Martin Hellman in 1976."** — source-facts.md: "Joined GCHQ 1974. Developed Diffie-Hellman equivalent." And: "Diffie-Hellman publication: 1976." Correct.

110. **"GCHQ didn't acknowledge any of this until 1997 — twenty-four years after Cocks's work."** — source-facts.md: "GCHQ/PKC secret duration: 1969/1973 - 1997 = ~24-28 years." Twenty-four years from 1973 is correct. And: "Revealed GCHQ history in public talk December 18, 1997." Clean.

111. **"In 1952, while enduring the chemical castration... Turing published a paper called 'The Chemical Basis of Morphogenesis.'"** — source-facts.md: "The Chemical Basis of Morphogenesis published 1952." Correct.

112. **"It appeared in the Philosophical Transactions of the Royal Society"** — source-facts.md: "Phil. Trans. Roy. Soc. Series B, Vol. 237, No. 641." Correct.

113. **"He died on June 7, 1954. A half-eaten apple beside his bed. Cyanide in his body. The inquest ruled suicide."** — Correct per source-facts.md. The apple is mentioned without claiming it was the delivery mechanism. The inquest ruling is stated as fact (which it is). Clean.

114. **"His body was being altered by the very institution he had saved."** — This echoes source-facts.md guidance: "Soften: 'His body was being altered' rather than 'his ability to think was destroyed.'" Correct framing.

115. **"Stuart Kauffman studied autocatalysis — self-organizing chemical systems..."** — Correct. Kauffman's autocatalytic sets are mainstream published science per source-facts.md.

116. **"Stephen Wolfram studied cellular automata..."** — Correct. Public, published science.

### DO NOT ASSERT VIOLATIONS

117. **"Not in the 1940s, but in the 1990s. Not with electromechanical machines, but with quantum computers. Not breaking Enigma, but breaking ALL modern encryption."** (lines 127-128) — This passage is in the "Now Imagine It Happened Again" section, which is framed as hypothetical ("what if"). The ALL-CAPS "ALL" is emphatic but sits within conditional framing. Acceptable.

118. **"And what if the scientists who achieved the breakthrough... built something that went far beyond code-breaking?"** — Properly framed as "what if." Acceptable.

119. **"That is the claim at the center of this book. It may be true. It may not be."** — Excellent three-possibilities framing. Clean.

120. **"the science that would make it possible... is real, published, and uncontroversial"** — Correct for the published science (Kauffman, Wolfram). The bridge to TQNN is not claimed as established here. Clean.

### TERMINOLOGY ISSUES

121. **No QNN/TQNN terminology appears in this file.** It uses "quantum computers" in the speculative section, which is appropriate for the hypothetical framing. Clean.

### THREE-POSSIBILITIES FRAMING NEEDED

122. **The "Now Imagine It Happened Again" section (lines 113-149)** — Already correctly framed as hypothetical / conditional. Uses "what if" throughout. Concludes with "It may be true. It may not be." This is the model for how the other source files should be written. Clean.

### CLEAN

123. **Section 1 (Ten Thousand People):** Clean. Historically accurate. Well-framed.
124. **Section 2 (Churchill/Coventry):** Clean. Correctly handles the contested claim with balanced presentation.
125. **Section 3 (GCHQ/PKC):** Clean. All dates verified against source-facts.md.
126. **Turing morphogenesis section:** Clean. Correct framing of DES effects.
127. **Three-possibilities framing in final section:** Model-quality. This is how the book should present TQNN claims.

---

## Summary of Issues by Severity

### Critical (must fix before chapter import)

| # | File | Issue |
|---|------|-------|
| 2 | srebrenica-witness | Ball is a statistician, not an attorney |
| 39 | turing-death | Winterbotham was Group Captain, not Captain |
| 40 | turing-death | GCHQ is not a branch of MI6 |
| 45 | turing-death | Turing did not predict DNA double helix |
| 58 | ch3-relinquishment | Team date 1991 should be ~1992 |
| 59 | ch3-relinquishment | PKC date wrong (1978 vs 1969-1977) |
| 63 | ch3-relinquishment | Bennett 1993 was theoretical, not experimental |
| 64 | ch3-relinquishment | Deutsch algorithm 1985 vs Deutsch-Jozsa 1992 |
| 86 | ch3-relinquishment | QNN must become TQNN throughout |
| 87 | ch3-relinquishment | "quantum teleportation" is wrong physics |
| 89 | ch3-relinquishment | Entire file needs three-possibilities reframing |

### Important (should fix)

| # | File | Issue |
|---|------|-------|
| 3 | srebrenica-witness | Hacktivismo did not coin "hacktivism" |
| 4 | srebrenica-witness | Annan 2005 date needs verification |
| 17 | gpt-history | Einstein 1904 should be 1905 |
| 18 | gpt-history | Turing 1934 should be 1936 |
| 19 | gpt-history | Internet 1963 should be 1969 |
| 33 | unintended-consequences | Einstein 1904 should be 1905 |
| 46-48 | turing-death | Text asserts Turing couldn't work (contested) |
| 100 | ultra-bridge | "Thirty years" should be "more than thirty" |
| 101 | ultra-bridge | Coventry deaths should say "an estimated 568" |

### Minor (fix when convenient)

| # | File | Issue |
|---|------|-------|
| 14 | gpt-history | "Michael 5Faraday" typo |
| 15 | gpt-history | "Feinman" should be "Feynman" (2x) |
| 16 | gpt-history | Radio credit (Edison/Tesla vs Marconi) |
| 21 | gpt-history | Atomic power timeline math wrong |
| 25 | gpt-history | Robotics != AI |
| 41 | turing-death | Apple Inc 1976 vs 1977 incorporation |
| 104 | ultra-bridge | "RAF officer" could be "RAF Group Captain" |

### Model Quality (no changes needed)

| File | Assessment |
|------|-----------|
| ultra-bridge.md | Best-in-class. Three-possibilities framing is exemplary. Minor date precision fixes only. This file should serve as the template for chapter writing. |

---

## Recommendations

1. **ch3-relinquishment.md** is the highest-priority file for revision. It requires comprehensive reframing, terminology updates, and date corrections. The entire file should be treated as raw material, not importable text.

2. **ultra-bridge.md** is nearly publication-ready. Fix the "thirty years" undercount and the Coventry death toll hedging, and it is good to go.

3. **turing-death.md** has several fixable errors (Winterbotham rank, GCHQ/MI6 relationship, DNA prediction claim) and needs DES/cognitive-impairment softening despite existing notes.

4. **srebrenica-witness.md** is usable as reported speech but must never be imported as factual narration. The Ball title error must be fixed.

5. **gpt-history.md** and **unintended-consequences.md** are background essays with standard historical errors (mostly dates). Fix and use as supporting material.

---

*Nightstalker, 2026-02-15*
