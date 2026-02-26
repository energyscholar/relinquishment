# Relinquishment — Build System
# All targets run from repo root.

SHELL := /bin/bash
SOURCE_DATE_EPOCH := $(shell git log -1 --pretty=%ct 2>/dev/null || date +%s)
export SOURCE_DATE_EPOCH

JOBNAME := Relinquishment

TIKZ_SRCS := $(filter-out build/images/standalone-header.tex, $(wildcard build/images/*.tex))
TIKZ_PDFS := $(TIKZ_SRCS:.tex=.pdf)

.PHONY: dev final screen print images validate clean clean-cache manifest size-report gitinfo check check-strict epub html markdown

# --- Dev build (host, no tagging) ---
dev: gitinfo images
	@echo "" > build/flags.tex
	@mkdir -p build/tikz-cache
	latexmk -r build/.latexmkrc -jobname=$(JOBNAME) main.tex

# --- Final build (Docker required) ---
final:
	@command -v docker >/dev/null 2>&1 || { echo "ERROR: Docker required for final builds. Not installed on this host."; exit 1; }
	@echo "\\def\\FINAL{1}" > build/flags.tex
	docker run --rm -v "$(CURDIR)":/src -w /src relinquishment-build latexmk -r build/.latexmkrc -jobname=$(JOBNAME) main.tex

# --- Screen layout (landscape, Docker required) ---
screen:
	@command -v docker >/dev/null 2>&1 || { echo "ERROR: Docker required for screen builds. Not installed on this host."; exit 1; }
	@echo "\\def\\FINAL{1}" > build/flags.tex
	docker run --rm -v "$(CURDIR)":/src -w /src relinquishment-build latexmk -r build/.latexmkrc -jobname=$(JOBNAME) main.tex

# --- Print layout (portrait, Docker required) ---
print:
	@command -v docker >/dev/null 2>&1 || { echo "ERROR: Docker required for print builds. Not installed on this host."; exit 1; }
	@echo "\\def\\FINAL{1}\\def\\PRINT{1}" > build/flags.tex
	docker run --rm -v "$(CURDIR)":/src -w /src relinquishment-build latexmk -r build/.latexmkrc -jobname=$(JOBNAME) main.tex

# --- EPUB (primary distribution) ---
epub: gitinfo
	python3 build/preprocess.py
	cd build/epub-tmp && pandoc main.tex \
		-f latex -t epub3 \
		--top-level-division=chapter \
		--toc --toc-depth=1 \
		--epub-cover-image=build/images/cover-triskellion.png \
		--css=../../build/epub.css \
		--metadata-file=../../build/metadata.yaml \
		-o ../../$(JOBNAME).epub

# --- Single HTML (universal fallback) ---
html: gitinfo
	python3 build/preprocess.py
	cd build/epub-tmp && pandoc main.tex \
		-f latex -t html5 \
		--standalone --self-contained \
		--top-level-division=chapter \
		--toc --toc-depth=1 \
		--mathml \
		--css=../../build/epub.css --css=../../build/html.css \
		--metadata-file=../../build/metadata.yaml \
		-o ../../$(JOBNAME).html

# --- Markdown (archival) ---
markdown: gitinfo
	python3 build/preprocess.py
	cd build/epub-tmp && pandoc main.tex \
		-f latex -t gfm \
		--top-level-division=chapter \
		--toc --toc-depth=2 \
		-o ../../$(JOBNAME).md

# --- Compile standalone TikZ images ---
images: $(TIKZ_PDFS)

build/images/%.pdf: build/images/%.tex build/images/standalone-header.tex build/palette.tex
	lualatex --shell-escape --output-directory=build/images $<

# --- Validation pipeline ---
validate:
	bash build/validate.sh

# --- Clean all generated files ---
clean:
	latexmk -r build/.latexmkrc -jobname=$(JOBNAME) -C main.tex 2>/dev/null || true
	rm -f $(JOBNAME).pdf $(JOBNAME).aux $(JOBNAME).log $(JOBNAME).toc $(JOBNAME).out $(JOBNAME).fls $(JOBNAME).fdb_latexmk
	rm -f $(JOBNAME).glo $(JOBNAME).gls $(JOBNAME).glg $(JOBNAME).ist $(JOBNAME).synctex.gz $(JOBNAME).bbl $(JOBNAME).blg
	rm -f main.pdf main.aux main.log main.toc main.out main.fls main.fdb_latexmk
	rm -f main.glo main.gls main.glg main.ist main.synctex.gz main.bbl main.blg
	rm -rf build/tikz-cache/*
	rm -f build/images/*.pdf
	rm -f build/validation.json
	@echo "" > build/flags.tex
	@echo "Clean complete."

# --- Clean TikZ cache only ---
clean-cache:
	rm -rf build/tikz-cache/*
	@echo "TikZ cache cleared."

# --- Generate manifest ---
manifest:
	@echo '{' > build/manifest.json
	@echo '  "generated": "'$$(date -u +%Y-%m-%dT%H:%M:%SZ)'",' >> build/manifest.json
	@echo '  "files": [' >> build/manifest.json
	@find manuscript/ build/ -type f \( -name '*.tex' -o -name '*.sty' -o -name '*.cls' \) | sort | while read f; do \
		echo "    \"$$f\"," ; \
	done | sed '$$ s/,$$//' >> build/manifest.json
	@echo '  ]' >> build/manifest.json
	@echo '}' >> build/manifest.json
	@echo "Manifest written to build/manifest.json"

# --- Size report ---
size-report:
	@echo "=== Size Report ==="
	@if [ -f $(JOBNAME).pdf ]; then \
		echo "PDF: $$(ls -lh $(JOBNAME).pdf | awk '{print $$5}')"; \
		pdfinfo $(JOBNAME).pdf 2>/dev/null | grep -E "^(Pages|File size)" || true; \
	else \
		echo "No $(JOBNAME).pdf found. Run 'make dev' first."; \
	fi
	@echo ""
	@echo "--- TeX source files ---"
	@find manuscript/ -name '*.tex' -exec ls -lh {} \; 2>/dev/null | awk '{printf "  %-50s %s\n", $$NF, $$5}'
	@echo ""
	@echo "--- Build files ---"
	@find build/ -name '*.tex' -exec ls -lh {} \; 2>/dev/null | awk '{printf "  %-50s %s\n", $$NF, $$5}'
	@echo ""
	@echo "--- TikZ cache ---"
	@du -sh build/tikz-cache/ 2>/dev/null || echo "  (no cache)"

# --- Manuscript invariant checks ---
check:
	@echo "=== Invariant Checks ==="
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
	@echo -n "Spiral-repeat markers present: "
	@grep -rl "SPIRAL-REPEAT" manuscript/ --include="*.tex" | wc -l | xargs -I{} echo "{} files marked"
	@echo -n "Voice headers present: "
	@grep -rl "% VOICE:" manuscript/ --include="*.tex" | wc -l | xargs -I{} echo "{} files marked"
	@echo -n "aidraftchapter coverage: "
	@echo "$$(grep -rl 'aidraftchapter' manuscript/ --include='*.tex' | grep -v staging | wc -l) of $$(find manuscript -name 'pos*.tex' ! -path '*/staging/*' | wc -l) chapters marked"
	@echo "=== Done ==="

# --- Strict checks (three-possibilities discipline) ---
check-strict: check
	@echo "=== Strict Checks ==="
	@echo -n "Unhedged C-assertions: "
	@grep -rn "The COWS \|COWS built\|COWS created\|COWS began\|COWS released\|COWS surrendered\|COWS would\|Guardian is \|Guardian was \|Guardian carefully\|The TQNN \|TQNN grew\|TQNN colonized\|She would \|She called \|They trained\|They walked\|They increased\|They built\|He enlightened" manuscript/ --include="*.tex" \
		| grep -v "^%\|staging/\|sources/\|raw/" \
		| grep -v "^[^:]*:[0-9]*:%" \
		| grep -v "Possibility\|proposition\|surmise\|deduce\|if.*true\|under.*C\|According\|account\|reportedly\|reconstruction\|if this\|If the COWS" \
		| grep -v "srcnote\|VOICE:\|SPIRAL-REPEAT" \
		&& echo "WARNING — possible unhedged C-assertions (review needed)" \
		|| echo "PASS"
	@echo -n "Three-poss coverage in aidraft chapters: "
	@for f in $$(grep -rl 'aidraftchapter' manuscript/ --include='*.tex' | grep -v staging); do \
		count=$$(grep -c -E 'Possibility|proposition|According to this|if this account|If this is true|reconstruction' "$$f" 2>/dev/null); \
		count=$${count:-0}; \
		if [ "$$count" -lt 2 ]; then \
			echo ""; echo "  LOW HEDGING ($$count): $$f"; \
		fi; \
	done
	@echo ""
	@echo "=== Done ==="

# --- Generate git info ---
gitinfo:
	@echo "\\newcommand{\\GitHash}{$$(git log -1 --pretty=%H 2>/dev/null || echo unknown)}" > build/gitinfo.tex
	@echo "\\newcommand{\\GitShortHash}{$$(git log -1 --pretty=%h 2>/dev/null || echo unknown)}" >> build/gitinfo.tex
	@echo "\\newcommand{\\GitDate}{$$(git log -1 --pretty=%ci 2>/dev/null || echo unknown)}" >> build/gitinfo.tex
	@echo "\\newcommand{\\BuildDate}{$$(date -u +%Y-%m-%dT%H:%M:%SZ)}" >> build/gitinfo.tex
