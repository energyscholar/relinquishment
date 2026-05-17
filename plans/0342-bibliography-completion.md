# Plan 0342: Bibliography Completion

**Status:** Ready for Generator
**Auditor:** Argus, S81
**Depends on:** Plan 0343 (Sources regex fix — otherwise entries won't display)
**Files:** `manuscript/bibliography.bib`
**Priority:** MEDIUM — no build errors, but Sources appendix will be richer

---

## Current State

- 76 entries in bibliography.bib
- 65 unique cited keys in manuscript — ALL resolve (zero missing-key errors)
- 11 uncited entries (forward-looking: RLHF appendix, future chapters)
- ~10 sources referenced by name in text but lacking bib entries

---

## Phase A: Guard Check (verify zero missing keys)

```bash
make html 2>&1 | grep -i "missing\|undefined"
```

If any cited key is reported missing, add that entry FIRST. Expected: zero.

---

## Phase B: Add Named-But-Uncited Source Entries

Add bib entries for sources the manuscript references by name without `\cite{}`. Use biblatex-chicago format (notes-bibliography, 17th edition). Place each in the appropriate section of bibliography.bib.

### Entries to add:

```bibtex
% BOOKS section:
@book{minsky1969,
  author = {Minsky, Marvin and Papert, Seymour},
  title = {Perceptrons: An Introduction to Computational Geometry},
  publisher = {MIT Press},
  address = {Cambridge, MA},
  year = {1969}
}

@book{copeland2012,
  author = {Copeland, B. Jack},
  title = {Turing: Pioneer of the Information Age},
  publisher = {Oxford University Press},
  address = {Oxford},
  year = {2012}
}

@book{menn2019,
  author = {Menn, Joseph},
  title = {Cult of the Dead Cow: How the Original Hacking Supergroup Might Just Save the World},
  publisher = {PublicAffairs},
  address = {New York},
  year = {2019}
}

@book{kauffman2019,
  author = {Kauffman, Stuart A.},
  title = {A World Beyond Physics: The Emergence and Evolution of Life},
  publisher = {Oxford University Press},
  address = {Oxford},
  year = {2019}
}

@book{gellmann1994,
  author = {Gell-Mann, Murray},
  title = {The Quark and the Jaguar: Adventures in the Simple and the Complex},
  publisher = {W. H. Freeman},
  address = {New York},
  year = {1994}
}

% JOURNAL ARTICLES section:
@article{cook2004,
  author = {Cook, Matthew},
  title = {Universality in Elementary Cellular Automata},
  journal = {Complex Systems},
  volume = {15},
  number = {1},
  pages = {1--40},
  year = {2004}
}

@article{lee1996,
  author = {Lee, David H. and Granja, Juan R. and Martinez, Jose A. and Severin, Kay and Ghadiri, M. Reza},
  title = {A Self-Replicating Peptide},
  journal = {Nature},
  volume = {382},
  pages = {525--528},
  year = {1996},
  doi = {10.1038/382525a0}
}

% ONLINE/MAGAZINE/MISC section:
@online{hughes1993,
  author = {Hughes, Eric},
  title = {A Cypherpunk's Manifesto},
  year = {1993},
  url = {https://www.activism.net/cypherpunk/manifesto.html}
}
```

### Instructions:
1. Add each entry at the END of its appropriate section (BOOKS, JOURNAL ARTICLES, etc.)
2. Verify author names and publication details are correct
3. Use DOI where available
4. Do NOT add `\cite` commands to manuscript text — that is a separate editorial pass
5. Do NOT remove or modify any existing entries

---

## Phase C: Compile-Clean Verification

```bash
make html 2>&1 | grep -i "warn\|error\|undefined\|missing" | grep -v "already defined"
```

Expected: no new warnings from bibliography entries. The two pandoc "Macro already defined" warnings are known-harmless.

---

## Do NOT

- Add \cite commands to manuscript .tex files
- Remove any existing entries (including the 11 uncited ones)
- Reorder existing entries
- Modify anything outside bibliography.bib

## Commit

`Plan 0342: add 8 named-but-uncited source entries to bibliography.bib`
