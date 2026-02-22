# Relinquishment — Build System
# All targets run from repo root.

SHELL := /bin/bash
SOURCE_DATE_EPOCH := $(shell git log -1 --pretty=%ct 2>/dev/null || date +%s)
export SOURCE_DATE_EPOCH

JOBNAME := Relinquishment

TIKZ_SRCS := $(filter-out build/images/standalone-header.tex, $(wildcard build/images/*.tex))
TIKZ_PDFS := $(TIKZ_SRCS:.tex=.pdf)

.PHONY: dev final screen print images validate clean clean-cache manifest size-report gitinfo

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

# --- Generate git info ---
gitinfo:
	@echo "\\newcommand{\\GitHash}{$$(git log -1 --pretty=%H 2>/dev/null || echo unknown)}" > build/gitinfo.tex
	@echo "\\newcommand{\\GitShortHash}{$$(git log -1 --pretty=%h 2>/dev/null || echo unknown)}" >> build/gitinfo.tex
	@echo "\\newcommand{\\GitDate}{$$(git log -1 --pretty=%ci 2>/dev/null || echo unknown)}" >> build/gitinfo.tex
	@echo "\\newcommand{\\BuildDate}{$$(date -u +%Y-%m-%dT%H:%M:%SZ)}" >> build/gitinfo.tex
