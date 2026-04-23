# Plan 0015: Signing Pipeline + Deadman's Switch

**Author:** Auditor (Session 9)
**Status:** OBSOLETE (superseded by Z-restructure, verified S63 audit)
**Priority:** P0 — MUST complete before Bruce flies
**Depends:** 0001
**TODO ref:** B01, B02, S04, D01

---

## Context

If Option C is substantially true, Bruce is a single point of failure. A deadman's switch converts the calculus from "convenient to eliminate" to "counterproductive to eliminate." This must be operational before he boards an airplane.

The switch does NOT require a finished book. It requires a SIGNED artifact — even a rough draft — deposited such that Bruce's incapacitation triggers release.

---

## Part A: PGP Key

### Step 1: Generate Key

```bash
gpg --full-generate-key
# Type: RSA and RSA
# Keysize: 4096
# Expiration: 0 (does not expire)
# Name: Bruce Stephenson
# Email: energyscholar@gmail.com
# Passphrase: [strong, memorized, NOT stored digitally]
```

### Step 2: Export Public Key

```bash
gpg --armor --export energyscholar@gmail.com > relinquishment-signing-key.asc
```

### Step 3: Distribute Public Key

Publish the public key on multiple independent platforms BEFORE the book:
- Upload to keys.openpgp.org
- Publish on postquantum.substack.com (new post: "Signing Key for Upcoming Publication")
- Include in the book's appendix (hardcoded, not generated)
- Post fingerprint on Blogspot blog
- Email fingerprint to Schneier and 2-3 other trusted contacts

**Why pre-distribute:** If the key only appears inside the book, there's no independent proof the key existed before the book. Pre-distribution on multiple timestamped platforms establishes the key's provenance.

### Step 4: Backup Private Key

```bash
gpg --armor --export-secret-keys energyscholar@gmail.com > PRIVATE-KEY-BACKUP.asc
```

Store on:
- Encrypted USB drive in a physical safe or with a trusted person
- NOT on any cloud service
- NOT on the same machine as the book repo

If the private key is lost, Bruce cannot sign errata or new editions.

---

## Part B: Signing Pipeline

### The Chicken-and-Egg Problem

The SHA-256 hash covers the entire PDF. But the PDF contains the hash on the verification page. Circular dependency.

### Solution: Two-Pass Build

```
Pass 1: Build PDF with hash placeholder → compute SHA-256 of everything EXCEPT
        the verification page → insert hash into verification page
Pass 2: Rebuild PDF with real hash → compute FINAL SHA-256 of complete document
        → this is the "document hash"
PGP:    Sign the FINAL PDF as a detached signature
```

The verification page contains:
- The Pass 1 hash (covers all content except the verification page itself)
- A note: "This hash covers all pages except this verification page. The detached PGP signature covers the complete document including this page."

This is standard practice for self-referential signed documents.

### Makefile Target

```makefile
sign: final
	@echo "Computing content hash (excludes verification page)..."
	# Extract all pages except verification, compute hash
	pdftk $(PDF) cat 1-$(VERIFY_PAGE_MINUS_1) $(VERIFY_PAGE_PLUS_1)-end output /tmp/content-only.pdf
	sha256sum /tmp/content-only.pdf | cut -d' ' -f1 > build/content-hash.txt
	# Inject hash into verification page and rebuild
	# [sed or LaTeX variable injection]
	$(MAKE) final
	@echo "Computing document hash..."
	sha256sum $(PDF) | cut -d' ' -f1 > build/document-hash.txt
	@echo "Signing..."
	gpg --detach-sign --armor $(PDF)
	@echo "Done. Signature: $(PDF).asc"
	@echo "Content hash: $$(cat build/content-hash.txt)"
	@echo "Document hash: $$(cat build/document-hash.txt)"
```

### Simpler Alternative: External Hash Only

Skip the in-document hash entirely. The verification page says:

```
This document's integrity can be verified using the detached PGP signature
published alongside it. The signature covers the complete document.

Signing key fingerprint: [FINGERPRINT]
Key available at: keys.openpgp.org, postquantum.substack.com

To verify:
  gpg --verify Relinquishment_by_Bruce_Stephenson.pdf.asc \
               Relinquishment_by_Bruce_Stephenson.pdf
```

**Recommendation:** Use the simpler alternative. The detached PGP signature is stronger than an in-document hash anyway. The hash-in-document is a nice touch but adds build complexity that could delay the deadline.

---

## Part C: Deadman's Switch

### Requirements

1. If Bruce is alive, nothing happens
2. If Bruce is incapacitated/dead, the signed PDF is released automatically
3. The trigger must be simple (not easily faked or accidentally triggered)
4. Multiple independent mechanisms (no single point of failure)
5. Must be operational within days, not weeks

### Mechanism 1: Timed Email Service

Services like FutureMe.org, LetterMeLater, or similar allow scheduling emails for future delivery. However, these are unreliable for critical use.

**Better: Gmail scheduled send + dead-man check-in.**

Set up a recurring system:
- Bruce schedules an email to himself every 7 days: "I am alive, postpone release"
- A trusted person (Genevieve?) holds the signed PDF + instructions
- If Bruce misses two consecutive check-ins (14 days), the trusted person releases

### Mechanism 2: Trusted Third Party

Give the signed PDF + public key + distribution instructions to 2-3 trusted people:
- Genevieve (primary)
- One other trusted friend
- Schneier? (as both recipient and backup distributor)

Instructions: "If I am dead or incapacitated, publish this PDF to: archive.org, IPFS, email it to [list of 10-20 recipients], post the PGP signature."

**This is the simplest and most reliable mechanism.** Human judgment about whether Bruce is alive or dead is more robust than any automated system.

### Mechanism 3: Encrypted Cloud Deposit + Key Escrow

1. Encrypt the signed PDF with a symmetric key
2. Upload the encrypted file to multiple public locations (archive.org, IPFS, personal website) — this can be done NOW, openly, because the file is encrypted
3. Give the decryption key to 2-3 trusted people with instructions

Advantage: the encrypted file is already distributed. No one needs to upload anything after Bruce's death. They just publish the decryption key.

**This is the strongest mechanism.** The encrypted artifact is already everywhere. The trusted parties hold only a short string (the key). The information is pre-positioned.

### Recommended Combination

**Primary:** Mechanism 3 (encrypted deposit + key escrow)
**Backup:** Mechanism 2 (trusted third party holds unencrypted copy)

Steps:
1. Sign the PDF (Part B)
2. Encrypt: `gpg --symmetric --cipher-algo AES256 Relinquishment_signed.pdf`
3. Upload encrypted file to: archive.org, IPFS, personal website, Blogspot
4. Give decryption passphrase to Genevieve + 1-2 others
5. Give unencrypted signed PDF to Genevieve as backup
6. Write clear instructions: "If I am dead, publish the passphrase and unencrypted PDF to [locations]"
7. Set up weekly check-in with Genevieve

### Timeline for Setup

- Day 1: Generate PGP key, sign current draft (even if incomplete)
- Day 1: Encrypt + upload to archive.org and IPFS
- Day 1: Give Genevieve the passphrase + instructions
- Day 1: Distribute public key to keyserver + Substack + Blogspot
- Ongoing: Re-sign and re-encrypt as the book improves
- Before flight: Final sign of best available version

---

## Part D: Version Strategy

The deadman's switch doesn't need the FINAL book. It needs the BEST AVAILABLE version at any point. Strategy:

- Sign and deposit a new version every day during the sprint
- Each version supersedes the previous
- The switch always holds the most recent signed version
- If the worst happens on Day 3, the Day 3 version releases — incomplete but containing the core thesis, predictions, and evidence

The incomplete version is better than no version. The predictions, abstracts, and appendices are already complete. The front matter is done. What's missing is chapter prose — but the staging files contain the raw content.

---

## Acceptance Criteria

1. PGP key generated and backed up
2. Public key published on 3+ independent platforms
3. Current PDF signed with detached signature
4. Encrypted PDF uploaded to 2+ public locations
5. Decryption passphrase given to 2+ trusted people with written instructions
6. Weekly check-in protocol established
7. Verification page updated with signing key fingerprint and verification instructions
8. `make sign` target works (or manual process documented)

---

## Red Team

### 1. What if the trusted parties are compromised?
Use 2-3 independent people who don't know each other. Genevieve is primary. One person outside Bruce's immediate circle. The encrypted-deposit mechanism means even if a trusted party is pressured, the encrypted file is already public — they can't un-distribute it.

### 2. What if the encrypted file is intercepted and cracked?
AES-256 symmetric encryption with a strong passphrase is effectively unbreakable. The passphrase should be 6+ random words (Diceware method), not a memorable phrase that could be guessed.

### 3. What if archive.org removes the encrypted file?
Upload to multiple platforms: archive.org, IPFS (content-addressed, censorship-resistant), personal website, Blogspot (Google infrastructure). If one removes it, others persist. IPFS is the strongest — once pinned, it's permanent and content-addressed.

### 4. What if Bruce accidentally misses a check-in?
Use a generous window (14 days, not 7). Genevieve can use judgment — a missed check-in while Bruce is on a camping trip is different from a missed check-in after a plane crash. Human judgment > automated triggers.

### 5. What if the PGP key is compromised?
The key proves authorship, but the CONTENT is what matters. Even without PGP verification, the predictions are timestamped, the Cryptome/Slashdot/Blogspot evidence is independently verifiable. The PGP signature is belt-and-suspenders, not the sole proof.

### 6. What if someone creates a fake "updated" version after Bruce's death?
The PGP signature prevents this. Only Bruce's private key can sign. If someone publishes an unsigned PDF claiming to be an update, it fails verification. The original signed version is canonical.

### 7. What about the session transcripts?
For the deadman's switch version, include a note: "Session transcripts will be included in the final edition. In the event of my death, the full unredacted transcripts are in [location]." The transcripts add credibility but aren't essential for the switch.

### 8. Legal: can the encrypted file be ordered taken down?
The encrypted file is legally meaningless gibberish. No court can order removal of random bytes. Only after decryption does it become a document — and by then it's been distributed. Pre-positioning the encrypted artifact is legally clean.

---

## Handoff Prompt

```
You are the Generator. Read plans/0015-signing-and-deadman.md.

Phase 1: Verification page update
- Update manuscript/99-back/verification.tex to replace the placeholder
  hash/signature blocks with the simpler PGP-only verification instructions
  per Part B "Simpler Alternative."
- Leave [FINGERPRINT] as a placeholder — Bruce will fill after key generation.
- make dev succeeds with 0 errors.

Phase 2: Makefile target (optional)
- Add a `sign` target to Makefile that:
  1. Runs `make final` (or `make dev` if Docker unavailable)
  2. Runs gpg --detach-sign --armor on the output PDF
  3. Prints the SHA-256 hash and signature file path
- This is convenience only. Bruce can sign manually.

Report: completion status, any issues.
NOTE: Key generation, encryption, upload, and distribution are BRUCE'S
tasks — not Generator tasks. They involve secrets and cannot be automated.
```
