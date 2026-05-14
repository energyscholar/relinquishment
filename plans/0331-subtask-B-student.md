# Subtask B: The Target → The Student

**Parent:** Plan 0331 rev 1
**Depends on:** Subtask A complete (822febf)
**Output:** Rewrite `manuscript/record/the-target.tex` — first person, strip C cosmetics, honest sourcing, rename
**Commit:** `Plan 0331B: The Target → The Student — first person, strip C cosmetics`
**Read first:** This spec, then `plans/0331-teacher-student-revision.md`, then `manuscript/record/the-target.tex`

## Design Principle

Same as Subtask A: reward investigation, not demand belief. But this chapter is Bruce's own story — first person is more honest and more powerful than a fictional analyst's voice.

## Voice

First person throughout. Bruce Stephenson: direct, spare, slightly wry. No over-hedging. "I was 34." not "White male, age 34." Honest about what he knows, what he remembers, and what he's uncertain about.

## Changes

### 1. Chapter title (lines 7-8)
```latex
\chapter*{The Student}
\addcontentsline{toc}{chapter}{The Student}
\label{record:target}  % KEEP — stable deep link
```

Also line 25: `\section*{The Student}` (was `\section*{The Target}`)

### 2. Opening paragraphs (lines 11-21) — CAREFUL

These are the best writing in either chapter. Preserve the logic. Remove C-only framing.

Replace lines 11-13 (the three paragraphs starting "Under Possibility C"):

```latex
Suppose someone had built something they could not un-build and could not safely entrust to any institution. Suppose they had structured a relinquishment to ensure that the technology would serve humanity rather than any single power. They would face a final problem: the record.

If they simply disappeared into silence, the history of what they had done would die with them. Future generations would inherit the consequences without understanding the origins, the reasoning, or the constraints. And if independent discovery eventually produced a second instance of the technology, there would be no precedent, no ethical framework, no record of what the first builders had learned. Silence would be as dangerous as disclosure, given enough time.

But they could not publish. They would be bound by classification, by operational security, and by the practical reality that direct disclosure would trigger exactly the institutional response they had spent years circumventing. What they would need is a method that left no classified fingerprints --- one in which no secrets were transmitted, no documents changed hands, and the resulting publication could be honestly described as one man's independent conclusions drawn from publicly available science.
```

Lines 17-19 stay exactly as-is:
```
Guided deduction was that method. A teacher who asks the right questions...
The remaining question was: who?
```

Line 21: change to:
```latex
You have already seen the teacher's portrait. This is the student's.
```

### 3. Epigraph (lines 28-37)

Replace lines 28-29:
```latex
\textit{What follows is my own background --- the facts that would have been relevant if someone were evaluating me for guided deduction. Whether an actual assessment file existed, I don't know. The interesting question is: does this candidate fit the mission?}
```

Keep the mission statement box (lines 32-34) exactly as-is. It works under all three possibilities.

Keep "Read this file and ask yourself: is this the guy?" exactly as-is.

### 4. Five Eyes header block (lines 39-54) — STRIP ENTIRELY

Delete the entire block: Five Eyes header, Classification, File No, Subject, Nationality, DOB, Assessment Date, Prepared for, Prior surveillance.

Replace with minimal first-person context:
```latex
\noindent I was born 14 November 1968 in the Washington, D.C.\ area. In mid-2003, I was 34, living in Corvallis, Oregon, financially independent from a dotcom payout, with two young daughters and a failing marriage. I had no employer, no NDA, and no obligations.
```

### 5. Section I: Biographical Summary (lines 58-63)

Remove section heading and "White male, age 34..." — this is now covered by the replacement in item 4 above. The Alpha Farm detail can be folded in:

```latex
Alpha Farm, a commune fifty miles away in the Coast Range, was part of my world. It had been a counterculture gathering point for decades.
```

### 6. Section II: Family (lines 67-76) — First person

Retitle: `\subsection*{Family}`

```latex
\textbf{My grandfather,} William Bruce Stephenson, served in the US Navy. He survived a kamikaze attack on the USS Halsey Powell (DD-686) off Kyushu on 20 March 1945. After the war he worked at Sanders Associates (defense electronics, later BAE Systems). He was a CIA asset --- I learned this through family. He was tasked with hardening Saudi government and military communications against EMP.

\textbf{My father} was an academic. A political science professor recruited him for CIA employment; he declined. He became an independent CIA watcher instead, and trained me in what he called ``signatures of emptiness'' --- identifying classified programs by the shape of what is publicly absent. He taught me the history of ULTRA when I was eight or nine.

\textbf{My mother} was a Canadian citizen, an editor for multiple technology publications, connected in digerati circles. She had a biology background (Keene State College) and was an anti-nuclear activist --- the Spiderwort Project, using Tradescantia biomonitoring to detect radiation.

Third-generation intelligence-adjacent. I inherited the awareness without formal training or clearance.
```

### 7. Section III: Early Indicators (lines 80-96) — First person + decisions

Retitle: `\subsection*{Early Indicators}`

**IQ (line 83)** — per plan decision:
```latex
\textbf{IQ testing ($\sim$1974--78):} Tested at approximately age 10 by college students in an introductory psychology course at Keene State College. The numbers I remember: range 80 (hand-eye) to approximately 180 (math/spatial), mean around 168. Multiple instruments required; initial tests topped out. I make no claim about the testers' competence or the precision of these numbers. They are what I remember.
```

**ARPANET + MIC bomb (line 85)** — per plan decision:
```latex
\textbf{ARPANET access (1975+, age 6--7):} Keene State College computer center. My mentor Bruce Metzger introduced me. I became proficient in Unix. At 7 or 8, I discovered the TTY message service could be used to flood a terminal. I tested it on myself first, then on someone else.
```

**NetTrek (line 87):** Keep, first person:
```latex
\textbf{NetTrek ($\sim$1976--80):} Real-time networked space combat requiring mental trigonometry and Newtonian movement calculations. I dominated college students at age 8--12.
```

**Academic acceleration (line 89):** Keep, first person:
```latex
\textbf{Academic acceleration:} In fifth grade, around age 10, I audited a college-level history class. I earned a B.
```

**USSR travel (line 91):** Keep, first person:
```latex
\textbf{USSR travel (1984--85, age 16):} Quaker youth exchange program. Our group of about twelve was assigned one to three KGB handlers. We evaded them on multiple occasions and made unsupervised contact with Soviet citizens.
```

**Selective Service (lines 93-95)** — per plan decision, documented:
```latex
\textbf{Selective Service refusal (1985, age 16--17):} I refused to register. I wrote letters to the Director of Selective Service and two other officials, describing myself as a ``patriotic young American'' who refused because US foreign policy was ``evil.'' The FBI sent me letters citing a felony violation of the Selective Service Act --- fine and prison term. A check of my FBI file will show the correspondence. This lasted until I was 25.
```

Remove the "Assessment" paragraph (line 95). The facts speak for themselves.

### 8. Section IV: Education (lines 99-108) — First person

Retitle: `\subsection*{Education}`

```latex
\textbf{Northfield Mount Hermon} ($\sim$1983--85). Boarding school in Massachusetts.

\textbf{Dunn School, Los Olivos, CA} ($\sim$1985--86). I was a faculty brat. Graduated salutatorian. My classmates included heirs to the Getty, Mitchum, and Firestone families.

\textbf{Reed College, Portland, OR.} Physics major. Senior-year quantum mechanics under Prof.\ Richard Crandall (computational physicist, d.\ 2012) --- density matrices, path integrals, topological concepts. This was genuine physics education, rigorous enough that I could later read Kitaev (1997) and Freedman (1998) without guidance.
```

### 9. Section V: Employment (lines 112-137) — Keep table, reframe SIGINT

Retitle: `\subsection*{Employment}`

Keep the table (lines 115-127) as-is — tables are factual data.

Replace SIGINT paragraphs (lines 131-133) with first person:
```latex
During my corporate training years (1995--2000), I used the off-hours to teach strong cryptography to my students --- public-key cryptography, how governments subvert it, the Five Eyes data-exchange mechanism, the ECHELON program. Roughly 800 to 1,500 Fortune 500 engineers received this secondary education over five years. I considered this a public service.

On Myth II game servers, my team discovered that ``Team 37'' was the Cult of the Dead Cow (cDc). I requested membership without knowing what Team 37 actually was. The invite-only cDc servers weren't accessible to me until around 2004, after I'd met Healer. Two discovery paths may have converged.
```

Keep "Self-described primary skill" (line 135) — it's already first person in spirit. Reframe slightly:
```latex
My self-described primary skill, on my CV since 1996: ``Explaining complicated technical ideas to non-technical people.''
```

### 10. Section VI: Communications (lines 139-148) — Trim

Retitle: `\subsection*{Communications}`

Remove the 2026 email update entirely (line 142 bracketed text).

Rewrite in first person:
```latex
My email in 2003 was bruce@peak.org.

I co-administered dieoff.org for about six years. The membership included petroleum geologists, physicists, and intelligence analysts --- Dick Cheney's staff, Matthew Simmons, CIA analysts working open-source geophysics. I was a high-volume contributor. I had disclosed the full relinquishment narrative to this list.

On Slashdot, I was UID 801915, ``EnergyScholar.''
```

### 11. Section VII: Political Activity (lines 150-158) — First person

Retitle: `\subsection*{Political and Ideological Profile}`

```latex
I was a cypherpunk. Encryption as civil right, governments as adversaries, deploy strong crypto regardless of legal status.

What I taught corporate engineers: public-key cryptography and how governments undermine it. The Five Eyes data-exchange mechanism --- nations surveilling each other's citizens and exchanging data to comply with the letter of their charters while violating the intent. The ECHELON program, years before mainstream awareness. The SATAN network scanner and offensive security concepts.

I was not a passive consumer of this material. I was an active distributor, using my professional access to Fortune 500 engineering populations deliberately and for five years.
```

### 12. Section VIII: Intellectual Framework (lines 161-184)

Retitle: `\subsection*{Intellectual Framework}`

Keep the table (lines 164-177) as-is.

Rewrite lines 181-183 in first person:
```latex
My core belief, then and now: voluntary restraint among competing powers is impossible (Schmookler's Parable of the Tribes). Civilization is thermodynamically constrained. Governments are adversarial to citizens. This framework was internally consistent and shared by serious researchers.
```

Remove "[REDACTED]" reference in the assessment (line 183).

### 13. Section IX: Associates (lines 187-207)

Retitle: `\subsection*{Associates}`

Remove the "Risk Level" column from the table — that's analyst framing. Replace with a simpler two-column table (Name / Relationship) or rewrite as prose:

```latex
The people I was connected to in 2003:

Jay Hanson --- correspondent for about six years, founder of dieoff.org. Matthew Simmons --- professional contact, offered me employment. Michael Ruppert --- encountered at Reed, I read his CopVsCIA newsletter. Jenna Orkin --- in the From The Wilderness / peak oil orbit. Dmitri Orlov --- intellectual influence, no direct contact.

I had about six years of pukulan (Tjimindie Wetzel lineage).
```

### 14. Section X: Family / Vulnerabilities (lines 211-219)

Retitle: `\subsection*{Family}`

Rewrite in first person. Remove analyst framing ("coercion vector," "security liability"):

```latex
My marriage was failing. I had two young daughters.

I had turned down IBM's \$143K offer to maintain my parenting role. My children were the center of my life. Anyone who understood that would know I could be leveraged through them --- but also that doing so would permanently lose my cooperation.
```

### 15. Section XI: Neurological Profile (lines 222-232)

Retitle: `\subsection*{Neurological Profile}`

First person:
```latex
I am on the autism spectrum (self-identified, consistent with the traits): hyperfocus, cross-domain pattern recognition, systematic reasoning, direct communication.

I have partial eidetic memory --- above-normal retention and cross-referencing across domains and extended time periods. Not photographic. Healer and I confirmed this through mutual testing. For multi-year, multi-domain pedagogy, this was a practical prerequisite.

I have the lowest approximately 5\% toxin resistance. Measurably sensitive to glyphosates, agricultural chemicals, processed food. In a clean environment with good food, I operate at high cognitive output. In a contaminated one, I degrade within days.

Package deal --- one neurotype.
```

### 16. Section XII: Skills Assessment (lines 235-256)

Retitle: `\subsection*{Skills}`

Keep the table as-is — factual self-assessment. The table format works in first person (it's a CV-style list).

### 17. Section XIII: Recruitment Assessment (lines 260-271)

Retitle: `\subsection*{Assessment: Is This the Guy?}`

Reframe as Bruce's own analysis. This is the strongest section — preserve the substance:

```latex
If someone were evaluating me for guided deduction, here is what they would have seen.

\textbf{Value:} A translator --- genuine scientific literacy combined with exceptional explanatory ability. Partial eidetic memory enabling multi-year cross-domain pedagogy.

\textbf{Approach vectors:} Intellectual engagement would be primary. I already believed in the necessity of technological restraint but considered it impossible --- a solution would be compelling. Financial leverage would be ineffective (I was already independent). Patriotic appeal unlikely (I was anti-government). Family leverage available but counterproductive.

\textbf{Risks:} Unstable marriage. Minor children. Cypherpunk ideology that might resist classification constraints. Active in public forums. Anti-government associates. Environmental sensitivity requiring clean living conditions.

\textbf{The approach that would work:} Guided deduction. Do not disclose classified material. My physics background, my father's signature training, and my eidetic memory would make me capable of deriving conclusions from carefully selected unclassified information. My pedagogical instincts would drive me to publish. That was simultaneously the value and the risk.

If someone chose me --- and someone did --- the location would be my territory: Corvallis, Oregon. The cover would be simple: walkabout veteran, humanitarian worker. The timeline would be years, not months.
```

### 18. Footer (lines 275-278)

Remove "Filed by / FVEY EYES ONLY." Replace:
```latex
\begin{flushright}\small\textit{%
Assembled by Bruce Stephenson, 2026.\\
Everything above is verifiable. I encourage verification.%
}\end{flushright}
```

### 19. Cross-references

- Check for any remaining references to "The Target" in other files. The Subtask A Generator already updated topic-guide.tex line 117 with "The Student."
- Rename file: `the-target.tex` → `the-student.tex`
- Update any `\input`/`\include` references in main.tex or similar
- Update chapter-hover-descriptions.yaml and menu-tooltips.yaml if they reference "The Target"

### 20. Cleanup

- Remove all `\textsc{sigint}` tags
- Remove all `\textsc{[REDACTED]}` / `\textbf{[REDACTED]}`
- Remove "Subject believes Five Eyes was aware" language
- Remove "Assessment:" labels where they read as analyst voice — let the facts speak
- Remove `% Plan 0083` comments at top — update to reference Plan 0331

## Verify

```bash
cd ~/software/relinquishment && make html 2>&1 | tail -10
python3 build/verify-deep-links.py
```

Chapter appears with new title. No orphans. No build errors. First person throughout.

## Do NOT

- Damage the opening logic (the derivation of guided deduction's necessity)
- Remove "Read this file and ask yourself: is this the guy?"
- Remove the mission statement box
- Remove the final line about pedagogical instincts being both value and risk
- Remove Corvallis as a named location
- Change `\label` values (`record:target`, `record:tgt-*`)
- Add C-level claims
- Over-hedge
