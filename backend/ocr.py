"""
VidhiAI OCR Pipeline
====================
Hybrid text extraction pipeline:
  1. Primary:  PyMuPDF native text layer (fast, exact, zero loss)
  2. Fallback: pytesseract / Tesseract-OCR for scanned / image-only pages

This guarantees maximum text coverage even for government PDFs that are
purely scanned image documents (common in Assam government gazette archives).

Author: VidhiAI Engineering
"""

import io
import re
import logging
from typing import List, Dict, Any, Optional

import fitz  # PyMuPDF

logger = logging.getLogger(__name__)

# Minimum characters required for a page to be considered "text-extractable"
# by PyMuPDF before we fall back to OCR.
_MIN_TEXT_THRESHOLD = 50


def clean_extracted_text(raw_text: str) -> str:
    """
    Normalizes extracted PDF text for optimal statutory readability and indexing:
      1. Reconstructs hyphenated words split across lines (e.g., 'pen-\\nsion' -> 'pension').
      2. Normalizes multiple carriage returns and excessive whitespace.
      3. Strips stray null/control characters while keeping clean paragraph structure.
    """
    if not raw_text:
        return ""

    # Rejoin words broken across line wraps by hyphens: "adminis-\ntration" -> "administration"
    text = re.sub(r"([A-Za-z])-[\r\n]+([A-Za-z])", r"\1\2", raw_text)

    # Replace lone carriage returns with newlines
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Collapse multiple inline spaces/tabs (preserving newlines)
    lines = []
    for line in text.split("\n"):
        cleaned_line = re.sub(r"[ \t]+", " ", line).strip()
        lines.append(cleaned_line)

    text = "\n".join(lines)
    # Collapse 3+ newlines to double newlines (paragraphs)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _has_meaningful_text(text: str) -> bool:
    """Returns True if the page has sufficient selectable text."""
    stripped = text.strip()
    return len(stripped) >= _MIN_TEXT_THRESHOLD


def _ocr_page_with_tesseract(page: fitz.Page, dpi: int = 300) -> str:
    """
    Render a single PDF page to an image and run Tesseract OCR on it.
    Applies image preprocessing (contrast enhancement, sharpening) for
    maximum clarity on government gazette scans.
    Supports English + Assamese (asm) if the language pack is installed.
    """
    try:
        import pytesseract
        from PIL import Image, ImageEnhance, ImageFilter

        # Render at 300 DPI for crisp character contours
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=mat, colorspace=fitz.csGRAY)
        img_data = pix.tobytes("png")

        img = Image.open(io.BytesIO(img_data))

        # Image enhancement: enhance contrast and sharpen scanned text
        try:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(1.5)
            img = img.filter(ImageFilter.SHARPEN)
        except Exception as filter_err:
            logger.debug("Image filter enhancement skipped: %s", filter_err)

        # Try English + Assamese; fall back to English only
        try:
            text = pytesseract.image_to_string(img, lang="eng+asm")
        except Exception:
            text = pytesseract.image_to_string(img, lang="eng")

        return text
    except ImportError:
        logger.warning("pytesseract is not installed; skipping OCR fallback for page.")
        return ""
    except Exception as exc:
        logger.warning("Tesseract OCR failed for page: %s", exc)
        return ""


def extract_text_from_pdf(pdf_path: str) -> List[Dict[str, Any]]:
    """
    Extract text from every page of a PDF using the hybrid pipeline:
      1. Primary: PyMuPDF native text layer with reading-order sorting (sort=True).
      2. Quality Check: If native text is empty or sparse (< 60 chars) and page has images,
         run high-resolution Tesseract OCR.
      3. Clean & Normalize: Unwraps line hyphens and removes encoding artifacts.

    Returns a list of page dicts:
        {
            "page_number": int,
            "text": str,           # cleaned extracted text
            "raw_text": str,       # verbatim text
            "extraction_method": "native" | "ocr",
        }
    """
    doc = fitz.open(pdf_path)
    pages: List[Dict[str, Any]] = []

    for page_idx in range(len(doc)):
        page = doc[page_idx]
        page_num = page_idx + 1

        # Step 1: Extract native text with reading order sort
        native_text = page.get_text("text", sort=True)
        native_clean = clean_extracted_text(native_text)

        has_images = len(page.get_images()) > 0
        needs_ocr = not _has_meaningful_text(native_clean) or (len(native_clean) < 80 and has_images)

        if not needs_ocr:
            pages.append({
                "page_number": page_num,
                "text": native_clean,
                "raw_text": native_text,
                "extraction_method": "native",
            })
            logger.debug("Page %d: native text extracted (%d chars).", page_num, len(native_clean))
        else:
            # Step 2: Fallback to high-res Tesseract OCR
            logger.info("Page %d: running OCR fallback for scanned content.", page_num)
            ocr_text = _ocr_page_with_tesseract(page)
            ocr_clean = clean_extracted_text(ocr_text)

            # Choose the richer extract (or combine if native had partial header)
            if len(ocr_clean) > len(native_clean):
                final_text = ocr_clean
                final_raw = ocr_text
                method = "ocr"
            else:
                final_text = native_clean if native_clean else ocr_clean
                final_raw = native_text if native_text else ocr_text
                method = "native" if native_clean else "ocr"

            pages.append({
                "page_number": page_num,
                "text": final_text,
                "raw_text": final_raw,
                "extraction_method": method,
            })

    doc.close()
    return pages


def get_page_count(pdf_path: str) -> int:
    """Return total page count of a PDF without full extraction."""
    doc = fitz.open(pdf_path)
    count = len(doc)
    doc.close()
    return count
