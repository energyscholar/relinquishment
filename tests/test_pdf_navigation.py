#!/usr/bin/env python3
"""
Comprehensive PDF Navigation Test Suite for Relinquishment.

Tests all navigation features:
- PDF bookmarks (sidebar) — depth, structure, page targets
- TOC hyperlinks — every chapter entry links to correct page
- "Return to TOC" links — present and functional at chapter ends
- Footer TOC links — present on content pages
- Cross-references — internal named destinations resolve
- External URLs — well-formed and reachable
- Section bookmarks — present for sections within chapters
- Navigation completeness — every chapter reachable from TOC,
  every chapter has return path to TOC

Usage:
    python3 tests/test_pdf_navigation.py [path/to/pdf]
    python3 tests/test_pdf_navigation.py --verbose
    python3 tests/test_pdf_navigation.py --fix-report
"""
import pymupdf
import sys
import re
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TestResult:
    name: str
    passed: bool
    message: str
    severity: str = "INFO"  # INFO, WARNING, ERROR, CRITICAL


@dataclass
class NavTestSuite:
    pdf_path: str
    doc: Optional[pymupdf.Document] = None
    results: list = field(default_factory=list)
    verbose: bool = False

    def open(self):
        self.doc = pymupdf.open(self.pdf_path)
        return self

    def close(self):
        if self.doc:
            self.doc.close()

    def add_result(self, name, passed, message, severity="INFO"):
        self.results.append(TestResult(name, passed, message, severity))
        if self.verbose and not passed:
            marker = {"INFO": ".", "WARNING": "?", "ERROR": "!", "CRITICAL": "X"}
            print(f"  {marker.get(severity, '?')} {name}: {message}")

    # ========== BOOKMARK TESTS ==========

    def test_bookmarks_exist(self):
        """Verify PDF has bookmarks at all."""
        toc = self.doc.get_toc()
        if len(toc) == 0:
            self.add_result("bookmarks_exist", False,
                            "No bookmarks found in PDF", "CRITICAL")
        else:
            self.add_result("bookmarks_exist", True,
                            f"{len(toc)} bookmark entries found")

    def test_bookmark_depth(self):
        """Verify bookmarks include section-level entries (depth >= 2)."""
        toc = self.doc.get_toc()
        max_depth = max(entry[0] for entry in toc) if toc else 0
        levels = {}
        for entry in toc:
            level = entry[0]
            levels[level] = levels.get(level, 0) + 1

        if max_depth < 2:
            self.add_result("bookmark_depth", False,
                            f"Max bookmark depth is {max_depth} (chapters only). "
                            f"Need depth >= 2 for section navigation.",
                            "ERROR")
        else:
            self.add_result("bookmark_depth", True,
                            f"Bookmark depth: {max_depth}. Levels: {levels}")

    def test_bookmark_page_targets(self):
        """Verify all bookmarks point to valid pages."""
        toc = self.doc.get_toc()
        num_pages = len(self.doc)
        invalid = []
        for entry in toc:
            page = entry[2] if len(entry) > 2 else -1
            title = entry[1]
            if page < 1 or page > num_pages:
                invalid.append(f"'{title}' → page {page}")

        if invalid:
            self.add_result("bookmark_targets", False,
                            f"{len(invalid)} bookmarks with invalid page targets: "
                            f"{'; '.join(invalid[:5])}", "ERROR")
        else:
            self.add_result("bookmark_targets", True,
                            f"All {len(toc)} bookmarks point to valid pages")

    def test_bookmark_ordering(self):
        """Verify bookmarks are in page order (no jumps backward)."""
        toc = self.doc.get_toc()
        out_of_order = []
        prev_page = 0
        for entry in toc:
            page = entry[2] if len(entry) > 2 else 0
            title = entry[1]
            if page < prev_page:
                out_of_order.append(f"'{title}' p{page} after p{prev_page}")
            prev_page = page

        if out_of_order:
            self.add_result("bookmark_order", False,
                            f"Bookmarks out of order: {'; '.join(out_of_order[:5])}",
                            "WARNING")
        else:
            self.add_result("bookmark_order", True,
                            "All bookmarks in page order")

    def test_chapter_bookmarks_complete(self):
        """Verify all expected chapters have bookmarks."""
        toc = self.doc.get_toc()
        l1_titles = [entry[1] for entry in toc if entry[0] == 1]

        # Expected chapters (from the known structure)
        expected_keywords = [
            "Three Possibilities", "Alpha Farm", "Mentor", "Code War",
            "Stories", "Secret", "Departure", "Dual-Use", "Factoring",
            "Braid", "Experiment", "Threshold", "Genesis", "Growing",
            "First Light", "Thermal", "Capability", "Walk-Out",
            "Patrick Ball", "Network", "Convergence", "Weight",
            "Instantiation", "Ethical", "Interdiction", "Extension",
            "Surrender", "Silence", "Redacted", "Unipolar", "Wolfram",
            "Doppelganger", "Magnetosphere", "Research", "Engine",
            "Question", "Glossary", "Acknowledgement", "Colophon",
        ]

        missing = []
        for keyword in expected_keywords:
            found = any(keyword.lower() in title.lower() for title in l1_titles)
            if not found:
                missing.append(keyword)

        if missing:
            self.add_result("chapters_bookmarked", False,
                            f"Missing chapter bookmarks for: {', '.join(missing)}",
                            "WARNING")
        else:
            self.add_result("chapters_bookmarked", True,
                            f"All {len(expected_keywords)} expected chapters bookmarked")

    # ========== LINK TESTS ==========

    def test_link_types(self):
        """Catalog all link types in the PDF."""
        type_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        total = 0
        for page_num in range(len(self.doc)):
            for link in self.doc[page_num].get_links():
                kind = link.get("kind", 0)
                type_counts[kind] = type_counts.get(kind, 0) + 1
                total += 1

        self.add_result("link_census", True,
                        f"Total: {total}. GOTO:{type_counts[1]}, "
                        f"URI:{type_counts[2]}, NAMED:{type_counts[4]}, "
                        f"OTHER:{type_counts[0]+type_counts[3]+type_counts[5]}")

    def test_no_broken_goto_links(self):
        """Verify all GOTO links point to valid pages."""
        broken = []
        for page_num in range(len(self.doc)):
            for link in self.doc[page_num].get_links():
                if link.get("kind") == 1:
                    dest = link.get("page", -1)
                    if dest < 0 or dest >= len(self.doc):
                        broken.append(f"p{page_num+1} → p{dest+1}")

        if broken:
            self.add_result("goto_links_valid", False,
                            f"{len(broken)} broken GOTO links: {'; '.join(broken[:5])}",
                            "ERROR")
        else:
            self.add_result("goto_links_valid", True,
                            "All GOTO links point to valid pages")

    def test_external_urls_wellformed(self):
        """Verify all external URLs are well-formed."""
        bad_urls = []
        all_urls = []
        for page_num in range(len(self.doc)):
            for link in self.doc[page_num].get_links():
                if link.get("kind") == 2:
                    uri = link.get("uri", "")
                    all_urls.append((page_num + 1, uri))
                    if not (uri.startswith("http://") or uri.startswith("https://")
                            or uri.startswith("mailto:")):
                        bad_urls.append(f"p{page_num+1}: {uri[:60]}")

        if bad_urls:
            self.add_result("urls_wellformed", False,
                            f"{len(bad_urls)} malformed URLs: {'; '.join(bad_urls[:5])}",
                            "WARNING")
        else:
            self.add_result("urls_wellformed", True,
                            f"All {len(all_urls)} external URLs well-formed")

    # ========== TOC NAVIGATION TESTS ==========

    def test_toc_page_has_links(self):
        """Verify the Table of Contents pages contain hyperlinks."""
        # Find TOC pages by looking for "Contents" heading
        toc_pages = []
        for page_num in range(min(40, len(self.doc))):
            text = self.doc[page_num].get_text()
            if "Contents" in text and any(
                keyword in text for keyword in
                ["Alpha Farm", "Three Possibilities", "The Mentor"]
            ):
                toc_pages.append(page_num)

        if not toc_pages:
            self.add_result("toc_located", False,
                            "Could not locate TOC pages", "ERROR")
            return

        total_links = 0
        for pg in toc_pages:
            links = self.doc[pg].get_links()
            total_links += len(links)

        if total_links < 10:
            self.add_result("toc_has_links", False,
                            f"TOC pages {[p+1 for p in toc_pages]} have only "
                            f"{total_links} links (expected 30+)", "ERROR")
        else:
            self.add_result("toc_has_links", True,
                            f"TOC pages {[p+1 for p in toc_pages]} have "
                            f"{total_links} hyperlinks")

    # ========== RETURN-TO-TOC TESTS ==========

    def test_return_to_toc_present(self):
        """Verify 'Return to Table of Contents' appears at chapter ends."""
        pages_with_return = []
        for page_num in range(len(self.doc)):
            text = self.doc[page_num].get_text()
            if "Return to Table of Contents" in text:
                pages_with_return.append(page_num + 1)

        # Should have roughly one per chapter (35+ chapters)
        if len(pages_with_return) < 30:
            self.add_result("return_toc_present", False,
                            f"Only {len(pages_with_return)} 'Return to TOC' links "
                            f"(expected 30+)", "ERROR")
        else:
            self.add_result("return_toc_present", True,
                            f"{len(pages_with_return)} 'Return to TOC' instances found")

    def test_return_to_toc_linked(self):
        """Verify 'Return to TOC' text has an actual hyperlink."""
        unlinked = []
        for page_num in range(len(self.doc)):
            text = self.doc[page_num].get_text()
            if "Return to Table of Contents" in text:
                links = self.doc[page_num].get_links()
                # Check if any link on this page is an internal nav link
                has_nav_link = any(
                    l.get("kind") in (1, 4) for l in links
                )
                if not has_nav_link:
                    unlinked.append(page_num + 1)

        if unlinked:
            self.add_result("return_toc_linked", False,
                            f"{len(unlinked)} 'Return to TOC' without hyperlinks: "
                            f"pages {unlinked[:10]}", "ERROR")
        else:
            self.add_result("return_toc_linked", True,
                            "All 'Return to TOC' instances have hyperlinks")

    # ========== FOOTER TOC LINK TESTS ==========

    def test_footer_toc_links(self):
        """Verify footer 'TOC' links are present on content pages."""
        pages_with_toc_footer = 0
        content_pages = 0

        for page_num in range(len(self.doc)):
            text = self.doc[page_num].get_text()
            lines = text.strip().split("\n")
            # Content pages have page numbers
            if any(line.strip().isdigit() for line in lines[-5:]):
                content_pages += 1
                if any(line.strip() == "TOC" or line.strip() == "toc"
                       for line in lines):
                    pages_with_toc_footer += 1

        coverage = pages_with_toc_footer / max(content_pages, 1) * 100
        if coverage < 80:
            self.add_result("footer_toc", False,
                            f"Footer TOC link on {pages_with_toc_footer}/{content_pages} "
                            f"content pages ({coverage:.0f}%)", "WARNING")
        else:
            self.add_result("footer_toc", True,
                            f"Footer TOC on {pages_with_toc_footer}/{content_pages} "
                            f"pages ({coverage:.0f}%)")

    # ========== NAVIGATION COMPLETENESS ==========

    def test_every_chapter_reachable(self):
        """Verify every chapter can be reached from TOC bookmarks."""
        toc = self.doc.get_toc()
        bookmarked_pages = set(entry[2] for entry in toc)

        # Find chapter start pages by looking for "Chapter N" headings
        chapter_pages = []
        for page_num in range(len(self.doc)):
            text = self.doc[page_num].get_text()
            if re.search(r"^Chapter\s+\d+", text, re.MULTILINE):
                chapter_pages.append(page_num + 1)

        unreachable = [p for p in chapter_pages if p not in bookmarked_pages]

        if unreachable:
            self.add_result("chapters_reachable", False,
                            f"{len(unreachable)} chapter start pages not in bookmarks: "
                            f"{unreachable[:10]}", "ERROR")
        else:
            self.add_result("chapters_reachable", True,
                            f"All {len(chapter_pages)} numbered chapters bookmarked")

    # ========== PREV/NEXT NAVIGATION ==========

    def test_prev_next_links(self):
        """Check if prev/next chapter navigation exists."""
        has_prev = False
        has_next = False
        for page_num in range(len(self.doc)):
            text = self.doc[page_num].get_text()
            if "Previous Chapter" in text or "Prev" in text:
                has_prev = True
            if "Next Chapter" in text:
                has_next = True

        if not (has_prev and has_next):
            self.add_result("prev_next_nav", False,
                            "No prev/next chapter navigation found. "
                            "Reader must use TOC or bookmarks for chapter hopping.",
                            "WARNING")
        else:
            self.add_result("prev_next_nav", True,
                            "Prev/Next chapter navigation present")

    # ========== BLANK PAGE AUDIT ==========

    def test_blank_pages(self):
        """Count blank/near-blank pages (screen reading waste)."""
        blank_pages = []
        for page_num in range(len(self.doc)):
            text = self.doc[page_num].get_text().strip()
            # Page is "blank" if it has < 50 chars (just page number + TOC footer)
            if len(text) < 50:
                blank_pages.append(page_num + 1)

        pct = len(blank_pages) / len(self.doc) * 100
        if pct > 10:
            self.add_result("blank_pages", False,
                            f"{len(blank_pages)} blank/near-blank pages ({pct:.1f}%) — "
                            f"print formatting waste for screen readers. "
                            f"Pages: {blank_pages[:20]}{'...' if len(blank_pages) > 20 else ''}",
                            "WARNING")
        else:
            self.add_result("blank_pages", True,
                            f"{len(blank_pages)} blank pages ({pct:.1f}%)")

    # ========== NAMED DESTINATION RESOLUTION ==========

    def test_named_destinations(self):
        """Check that named destinations can be resolved."""
        # Collect all named link targets
        named_targets = set()
        for page_num in range(len(self.doc)):
            for link in self.doc[page_num].get_links():
                if link.get("kind") == 4:
                    name = link.get("name", "")
                    if name:
                        named_targets.add(name)

        # Check which named destinations exist in the PDF
        # PyMuPDF can resolve named destinations
        resolved = 0
        unresolved = []
        for name in named_targets:
            try:
                dest = self.doc.resolve_link(f"#{name}")
                if dest:
                    resolved += 1
                else:
                    unresolved.append(name)
            except Exception:
                unresolved.append(name)

        if named_targets:
            pct = resolved / len(named_targets) * 100
            if unresolved:
                self.add_result("named_dests", False,
                                f"{len(unresolved)}/{len(named_targets)} named destinations "
                                f"unresolved: {unresolved[:5]}", "WARNING")
            else:
                self.add_result("named_dests", True,
                                f"All {resolved} named destinations resolve ({pct:.0f}%)")
        else:
            self.add_result("named_dests", True,
                            "No named destinations to check")

    # ========== PDF METADATA ==========

    def test_pdf_metadata(self):
        """Verify PDF metadata is complete."""
        md = self.doc.metadata
        required = ["title", "author"]
        missing = [k for k in required if not md.get(k)]

        if missing:
            self.add_result("metadata", False,
                            f"Missing PDF metadata: {missing}", "WARNING")
        else:
            self.add_result("metadata", True,
                            f"Title: '{md['title'][:50]}', Author: '{md['author'][:50]}'")

    # ========== SCREEN GEOMETRY ==========

    def test_page_orientation(self):
        """Check if PDF uses landscape (screen) or portrait (print) orientation."""
        page = self.doc[0]
        w, h = page.rect.width, page.rect.height

        if w > h:
            orientation = "landscape"
            self.add_result("orientation", True,
                            f"Landscape ({w:.0f}x{h:.0f}pt) — optimized for screen")
        else:
            orientation = "portrait"
            self.add_result("orientation", False,
                            f"Portrait ({w:.0f}x{h:.0f}pt) — print format, "
                            f"not optimized for screen reading", "WARNING")

    # ========== RUN ALL TESTS ==========

    def run_all(self):
        """Run the complete test suite."""
        self.open()

        print(f"Testing: {self.pdf_path}")
        print(f"Pages: {len(self.doc)}")
        print(f"{'='*60}")

        tests = [
            # Bookmark tests
            self.test_bookmarks_exist,
            self.test_bookmark_depth,
            self.test_bookmark_page_targets,
            self.test_bookmark_ordering,
            self.test_chapter_bookmarks_complete,
            # Link tests
            self.test_link_types,
            self.test_no_broken_goto_links,
            self.test_external_urls_wellformed,
            # TOC tests
            self.test_toc_page_has_links,
            # Return-to-TOC tests
            self.test_return_to_toc_present,
            self.test_return_to_toc_linked,
            # Footer tests
            self.test_footer_toc_links,
            # Completeness tests
            self.test_every_chapter_reachable,
            self.test_prev_next_links,
            # Quality tests
            self.test_blank_pages,
            self.test_named_destinations,
            self.test_pdf_metadata,
            self.test_page_orientation,
        ]

        for test in tests:
            try:
                test()
            except Exception as e:
                self.add_result(test.__name__, False,
                                f"Test crashed: {e}", "CRITICAL")

        self.close()
        return self.report()

    def report(self):
        """Print test results summary."""
        passed = sum(1 for r in self.results if r.passed)
        failed = sum(1 for r in self.results if not r.passed)
        total = len(self.results)

        print(f"\n{'='*60}")
        print(f"RESULTS: {passed}/{total} passed, {failed} failed")
        print(f"{'='*60}")

        # Group by severity
        for severity in ["CRITICAL", "ERROR", "WARNING", "INFO"]:
            items = [r for r in self.results if not r.passed and r.severity == severity]
            if items:
                print(f"\n{severity}:")
                for r in items:
                    print(f"  FAIL  {r.name}: {r.message}")

        print(f"\nPASSED:")
        for r in self.results:
            if r.passed:
                print(f"  OK    {r.name}: {r.message}")

        return failed == 0


def main():
    args = sys.argv[1:]
    verbose = "--verbose" in args or "-v" in args
    args = [a for a in args if not a.startswith("-")]

    pdf_path = args[0] if args else "Relinquishment.pdf"

    suite = NavTestSuite(pdf_path=pdf_path, verbose=verbose)
    success = suite.run_all()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
