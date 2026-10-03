"""
Corpus Gate Inspection Script (Phase 0)
Inspects PDFs in /corpus:
- Page count
- Text layer presence (extracts pages 1-3 and prints 300 chars)
- Detects whether PDF is scanned (image-only) or digital text
- Scans for structural legal headings (Rule, Section, Chapter, Order, Notification)
"""

import sys
import os
import re
from pathlib import Path

def inspect_corpus(corpus_dir: str = "corpus"):
    corpus_path = Path(corpus_dir)
    if not corpus_path.exists():
        print(f"[!] Directory '{corpus_dir}' does not exist.")
        return False, []

    pdf_files = list(corpus_path.glob("*.pdf")) + list(corpus_path.glob("*.PDF"))
    if not pdf_files:
        print(f"[!] No PDF files found in '{corpus_dir}'.")
        print(f"    Please place 3 to 6 curated Assam Government PDFs in '{corpus_dir}/'.")
        return False, []

    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("[!] PyMuPDF (fitz) is not installed in the active environment.")
        return False, []

    print(f"=== PHASE 0: CORPUS GATE INSPECTION ===")
    print(f"Found {len(pdf_files)} PDF file(s) in '{corpus_dir}/'\n")

    results = []
    scanned_files = []

    heading_regex = re.compile(
        r'^\s*(CHAPTER\s+[IVXLCDM\d]+|SECTION\s+\d+|RULE\s+\d+|PART\s+[IVXLCDM\d]+|NOTIFICATION|GOVERNMENT OF ASSAM|ORDER|CLAUSE\s+\d+|\d+\.\s+[A-Z])',
        re.IGNORECASE | re.MULTILINE
    )

    for pdf_file in sorted(pdf_files):
        print(f"--------------------------------------------------")
        print(f"File: {pdf_file.name}")
        print(f"Path: {pdf_file}")
        
        try:
            doc = fitz.open(pdf_file)
            page_count = len(doc)
            print(f"Total Pages: {page_count}")

            extracted_text = ""
            sample_pages = min(3, page_count)
            text_per_page = []

            for p_idx in range(sample_pages):
                page = doc[p_idx]
                text = page.get_text("text").strip()
                text_per_page.append(text)
                extracted_text += f"\n--- Page {p_idx + 1} ---\n" + text

            total_sample_chars = sum(len(t) for t in text_per_page)
            has_text_layer = total_sample_chars > 50

            if not has_text_layer:
                print("  STATUS: [!] SCANNED / NON-TEXT PDF DETECTED")
                print("  Sample character count across first 3 pages is near 0.")
                scanned_files.append(pdf_file.name)
            else:
                print("  STATUS: [✓] DIGITAL TEXT LAYER PRESENT")
                print(f"  First 300 extracted characters:")
                preview = extracted_text.replace('\n', ' ')[:300]
                print(f"  \"{preview}...\"\n")

                # Heading detection
                headings = heading_regex.findall(extracted_text)
                if headings:
                    print(f"  Headings found in first {sample_pages} pages: {len(headings)}")
                    for h in headings[:5]:
                        print(f"    - {h.strip()}")
                else:
                    print("  Headings: Standard paragraph layout (no explicit structural headings in pages 1-3)")

            results.append({
                "file": pdf_file.name,
                "pages": page_count,
                "has_text_layer": has_text_layer,
                "sample_chars": total_sample_chars,
            })
            doc.close()

        except Exception as e:
            print(f"  [ERROR] Failed to read PDF {pdf_file.name}: {e}")
            results.append({
                "file": pdf_file.name,
                "error": str(e)
            })

    print(f"\n================ SUMMARY ================")
    print(f"Total PDFs examined: {len(pdf_files)}")
    print(f"Text-layer PDFs: {len([r for r in results if r.get('has_text_layer')])}")
    print(f"Scanned/Image-only PDFs: {len(scanned_files)}")

    if scanned_files:
        print(f"\n[ALERT] Gate Condition Triggered:")
        print(f"Scanned document(s) detected: {', '.join(scanned_files)}")
        print("Per Phase 0 instructions: STOP and notify user before building OCR pipeline.")
        return False, results
    else:
        print(f"\n[SUCCESS] Phase 0 Corpus Gate Passed: All documents have accessible digital text layers.")
        return True, results

if __name__ == "__main__":
    dir_to_check = sys.argv[1] if len(sys.argv) > 1 else "corpus"
    inspect_corpus(dir_to_check)
