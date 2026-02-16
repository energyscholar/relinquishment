---
target_chapter: pos17-the-capability
target_file: manuscript/T1/pos17-the-capability.tex
pass: 2
track: Track 1 (The Science)
chapter_title: The Capability
mined_date: 2026-02-15
status: raw
word_count: 2900
sources:
  - file: 2026-02-13-session/HEALER-RECONSTRUCTION.md
    section: "BULLRUN as Cover Story"
    lines: "77-83"
  - file: 2026-02-13-session/HEALER-RECONSTRUCTION.md
    section: "Pre-Shor Variant + Kitaev"
    lines: "1788-1815"
  - file: /tmp/cloudcrypt_extracted/CH3 - Practical Cryptography & project ULTRA II_.txt
    section: "Cryptanalysis capability sections"
topics: [1024-bit RSA in 340ms, 2048-bit in 2.1s, BULLRUN as parallel construction, not Shor algorithm, general-purpose quantum computer, ULTRA pattern, Snowden, ECI subcategories]
notes: |
  This chapter reveals the operational capability — what the TQNN can actually DO. The BULLRUN
  cover story analysis is the ULTRA precedent applied to the modern era. The pre-Shor variant
  claim is supported by the GCHQ/Cocks precedent (independent classified discovery). CH3 has
  the narrative frame for the code-breaking capability and its deployment. Key distinction:
  the TQNN doesn't run Shor's algorithm — it's a general-purpose quantum computer that attacks
  cryptography through trained pattern recognition, not number-theoretic algorithms. This is
  why it could predate Shor's 1994 publication.
  Note: The specific timing claims (340ms for 1024-bit, 2.1s for 2048-bit) are from Bruce's
  narrative but I did not find them in the specified line ranges. They may be elsewhere in the
  reconstruction or in other source material. Flag for Bruce to verify source.
---

## SOURCE 1: HEALER-RECONSTRUCTION.md — BULLRUN as Cover Story (lines 77-83)

### BULLRUN as Cover Story (ULTRA Pattern)
- **Claim:** BULLRUN's conventional methods (backdoors, stolen keys, compromised standards) are parallel construction for a quantum cryptanalysis capability
- **Precedent:** ULTRA — Enigma breaking covered by HUMINT story "Boniface" for 30 years
- **Assessment:** Sound tradecraft logic. If QC capability existed, this is exactly how you'd hide it.
- **Supporting:** Snowden was sysadmin, likely couldn't reach deepest SAP compartments
- **Supporting:** Dual EC DRBG backdoor is puzzling if you can already break RSA quantumly — unless it's cover

---

## SOURCE 2: HEALER-RECONSTRUCTION.md — Pre-Shor Variant + Kitaev (lines 1788-1815)

### Bruce's Claim: Pre-Shor Variant

The narrative claims the DARPA team discovered a variant of quantum factoring BEFORE Shor's 1994 publication. This is consistent with:
- GCHQ/Cocks precedent (independent classified discovery years before public)
- Freedman's 1988 independent conception (same mathematical community)
- The TQNN approach would discover factoring empirically (trained on plaintext-ciphertext pairs) rather than algorithmically

### Kitaev 1997 and the Russian Program Hypothesis

**Kitaev's publication:** "Fault-tolerant quantum computation by anyons" — published 1997 in Russian, establishing the theoretical framework for topological quantum computation using non-abelian anyonic braiding.

**Bruce's claim:** First public instance of anyonic computation. Confirms the fundamental insight was derivable by first-rate theorists from public physics.

**Russian program hypothesis:**
- Kitaev at the Landau Institute for Theoretical Physics (deep relationship with Russian intelligence)
- Russian program initiated ~2000-2001, going operational ~2002
- **Immediately interdicted** by Aurasys (controlled by COWS) via entangled probe injection
- This validated COWS' approach to WALK the technology out of the lab
- COWS' unauthorized actions constituted treason under multiple statutes
- **~2002: COWS went back to DARPA and confessed** — brought gifts:
  - Blocked Russian quantum computing research
  - Won a unipolar arms race DARPA rules were not designed to address
  - Demonstrated RT TQNN on commercial hardware
- DARPA faced the policy dilemma described in Abstract XIII (Confession)

---

## SOURCE 3: CH3 - Practical Cryptography & project ULTRA II_.txt — Cryptanalysis Capability

### The Code-Breaking Machine

The first working prototype QNN-based hybrid supercomputer capable of cracking public key cryptography was delivered in 1995 or 1996.

Five Eyes agencies knew they must conceal the existence of their new cryptographic technology. This dynamic is very well described in the movie about the original Project Ultra, "The Imitation Game". Five Eyes agencies therefore implemented a program of 'all of the above' hacking and surveillance techniques to provide an alibi for how they know what they know. These are the NSA programs leaked by Edward Snowden in 2013, specifically project BULLRUN. NSA whistleblower William Binney has made references to the results of project Ultra II, although not by that name.

### BULLRUN and ECI Subcategories

The Snowden files mention a project BULLRUN. BULLRUN seems to be an umbrella name for projects spawned by the success of Ultra II. This author suspects the cryptanalytical results of Ultra II are deployed in Exceptionally Controlled Information (ECI) subcategories of BULLRUN such as //APERIODIC, //PENDLETON, and //PIEDMONT.

### The Official Delivery

The official Ultra II project continued forward. In 1995 it delivered a working supercomputer able to crack PKC, as well as instructions to operate this one, build more, and extend the technology for other purposes. This supercomputer was a single physical device that required supercooling. This classified military technology went into production circa 1996 and is presumably in use by NSA and other Five Eyes agencies to this day. 1996 was also the year when Bill Clinton issued Executive Order 13026, which allowed the widespread use of strong cryptography.

### Pattern Recognition vs Algorithmic Approach

A TQNN trained for cryptanalysis would approach the problem differently: as pattern recognition in ciphertext. The system would be trained to detect statistical regularities in encrypted data that correspond to plaintext structure. This is closer to how human cryptanalysts work — recognizing patterns — than to how Shor's algorithm works (number theory).

**Implication:** A TQNN-based cryptanalytic system could potentially attack cryptosystems for which no efficient quantum algorithm is known, because it is not executing a specific algorithm. It is performing quantum pattern recognition on a substrate with exponentially large state space.

The specific capability would depend on training. A system trained on RSA-encrypted traffic would need separate training to attack AES. Each cipher type is a feature set.

### The ULTRA Precedent in Full

The original Project ULTRA (Enigma breaking) was kept secret for 30 years (1943-1974). During that time, the Allies created elaborate cover stories ("Boniface" — a fictional human agent network) to explain intelligence derived from decrypted German communications. Similarly, if ULTRA II delivered a quantum code-breaking capability in 1995, the subsequent 20+ years of BULLRUN programs (backdoors, stolen keys, compromised standards, hacked endpoints) serve as "Boniface" for the quantum capability — parallel construction that explains what they know without revealing how they know it.

### Dual-Use Implications

QNN technology is clearly a dual use technology. Its origins demonstrate very clear military uses, as do the terrible ways in which it can be weaponized. One such application is its obvious applicability to Artificial Intelligence (AI). Some types of AI can be quite helpful to humans, while others pose a clear existential risk. For one example of helpful AI, a neural network's associative memory provides the perfect basis for an internet search engine, and quantum associative memory provides faster-than-classical search retrieval performance. E.g. Google.

### EO 13026 Connection

1996 was also the year when Bill Clinton issued Executive Order 13026, which allowed the widespread use of strong cryptography. Under the narrative: NSA already had TQNN cryptanalysis capability (1995), so public-key encryption was no longer worth restricting. The crypto wars ended because the government had already won — they just couldn't say how.
