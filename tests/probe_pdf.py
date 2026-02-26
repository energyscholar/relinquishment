#!/usr/bin/env python3
"""Quick probe of PDF structure for navigation analysis."""
import pymupdf
import sys

pdf_path = sys.argv[1] if len(sys.argv) > 1 else "Relinquishment.pdf"
doc = pymupdf.open(pdf_path)

print(f"Pages: {len(doc)}")
print(f"PDF version: {doc.metadata.get('format', 'unknown')}")
print(f"Title: {doc.metadata.get('title', 'none')}")
print()

# TOC / Bookmarks
toc = doc.get_toc()
print(f"=== TOC/Bookmark entries: {len(toc)} ===")
for entry in toc:
    level, title, page = entry[0], entry[1], entry[2]
    indent = "  " * (level - 1)
    print(f"  {indent}[L{level}] p{page}: {title}")
print()

# Count links per page
total_links = 0
pages_with_links = 0
link_types = {}
broken_links = []

for page_num in range(len(doc)):
    page = doc[page_num]
    links = page.get_links()
    if links:
        pages_with_links += 1
    for link in links:
        total_links += 1
        kind = link.get("kind", -1)
        link_types[kind] = link_types.get(kind, 0) + 1

        # Check internal links
        if kind == 1:  # LINK_GOTO (internal)
            dest_page = link.get("page", -1)
            if dest_page < 0 or dest_page >= len(doc):
                broken_links.append((page_num + 1, link))

print(f"=== Link Statistics ===")
print(f"Total links: {total_links}")
print(f"Pages with links: {pages_with_links}/{len(doc)}")
print(f"Link types: {link_types}")
print(f"  0=NONE, 1=GOTO(internal), 2=URI(external), 3=LAUNCH, 4=NAMED, 5=GOTOR(other doc)")
if broken_links:
    print(f"\n!!! BROKEN LINKS: {len(broken_links)} !!!")
    for pg, link in broken_links[:10]:
        print(f"  Page {pg}: {link}")
print()

# Sample links from first few content pages
print("=== Sample links (first 10 pages with links) ===")
count = 0
for page_num in range(len(doc)):
    page = doc[page_num]
    links = page.get_links()
    if links:
        print(f"\n  Page {page_num + 1} ({len(links)} links):")
        for link in links[:3]:
            kind = link.get("kind", -1)
            if kind == 1:
                print(f"    GOTO → page {link.get('page', '?') + 1}")
            elif kind == 2:
                print(f"    URI → {link.get('uri', '?')[:80]}")
            elif kind == 4:
                print(f"    NAMED → {link.get('name', '?')}")
            else:
                print(f"    kind={kind}: {link}")
        if len(links) > 3:
            print(f"    ... +{len(links) - 3} more")
        count += 1
        if count >= 10:
            break

# Check for "Return to Table of Contents" links
print("\n=== 'Return to TOC' link check ===")
toc_links_found = 0
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    if "Return to Table of Contents" in text:
        toc_links_found += 1
        links = page.get_links()
        has_goto = any(l.get("kind") == 1 for l in links)
        status = "LINKED" if has_goto else "TEXT ONLY (no hyperlink!)"
        # Only print first few
        if toc_links_found <= 5:
            print(f"  Page {page_num + 1}: {status}")

print(f"Total 'Return to TOC' instances: {toc_links_found}")

# Check for TOC page footer links
toc_footer_count = 0
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    # Look for standalone "TOC" text (footer link)
    lines = text.split("\n")
    for line in lines:
        if line.strip() == "TOC":
            toc_footer_count += 1
            break

print(f"Pages with 'TOC' footer: {toc_footer_count}")

doc.close()
