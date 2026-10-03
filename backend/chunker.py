"""
VidhiAI Chunker
===============
Converts raw per-page text (from the hybrid OCR pipeline) into structured,
citation-ready chunks stored in SQLite.

Each chunk carries:
  - Exact page number
  - Detected Rule / Section / Clause citation
  - Character offset range
  - Normalized clean_text for deterministic substring verification
"""

import re
from typing import List, Dict, Any

from .verifier import normalize_text
from .ocr import extract_text_from_pdf

RULE_PATTERNS = [
    re.compile(r"(Rule\s+\d+[\w\(\)\-\.]*)", re.IGNORECASE),
    re.compile(r"(Section\s+\d+[\w\(\)\-\.]*)", re.IGNORECASE),
    re.compile(r"(Clause\s+\d+(\.\d+)?)", re.IGNORECASE),
    re.compile(r"(Chapter\s+[IVXLCDM\d]+(?:\s*[-:]\s*[A-Za-z\s]+)?)", re.IGNORECASE),
    re.compile(r"(Article\s+\d+(\([a-zA-Z0-9]+\))?)", re.IGNORECASE),
    re.compile(r"((?:Office\s+Memorandum|O\.?M\.?)\s*(?:No\.?)?\s*[\w\d/.-]+)", re.IGNORECASE),
    re.compile(r"(Notification\s+(?:No\.?)?\s*[\w\d/.-]+)", re.IGNORECASE),
    re.compile(r"(Order\s+(?:No\.?)?\s*[\w\d/.-]+)", re.IGNORECASE),
    re.compile(r"(Paragraph\s+\d+)", re.IGNORECASE),
    re.compile(r"(Schedule\s+[A-Z0-9]+)", re.IGNORECASE),
    re.compile(r"(Form\s+[A-Z0-9]+(?:\([a-zA-Z0-9]+\))?)", re.IGNORECASE),
    re.compile(r"(Appendix\s+[A-Z0-9]+)", re.IGNORECASE),
    re.compile(r"(Guideline\s+\d+(\.\d+)?)", re.IGNORECASE),
    re.compile(r"(Eligibility\s+(?:Condition|Criteria)\s*\d*(?:\([a-zA-Z0-9]+\))?)", re.IGNORECASE),
    re.compile(r"(Preamble)", re.IGNORECASE),
    re.compile(r"(দফা\s+\d+(\.\d+)?)"),
    re.compile(r"(নিয়ম\s+\d+(\([a-zA-Z0-9]+\))?)"),
    re.compile(r"(ধাৰা\s+\d+(\([a-zA-Z0-9]+\))?)"),
    re.compile(r"(অনুচ্ছেদ\s+\d+)"),
    re.compile(r"(প্ৰপত্ৰ\s+[\w\d]+)"),
]


def _detect_rule(text: str, page_num: int = 1) -> str:
    """Return the first Rule/Section/Clause reference found in the text, or meaningful section label."""
    for pat in RULE_PATTERNS:
        match = pat.search(text)
        if match:
            return match.group(1).strip()

    # Check if this is the statutory preamble or title page
    lower_snippet = text[:250].lower()
    if page_num <= 2 and any(w in lower_snippet for w in ["preamble", "whereas", "an act to", "notification", "gazette", "memorandum"]):
        return "Statutory Preamble & Enactment"

    # Check for numbered clauses at the beginning (e.g., "1. Short Title and Commencement")
    numbered_lead = re.match(r"^\s*(\d+\.[\d.]*)\s+([A-Z][A-Za-z\s]{3,40})", text)
    if numbered_lead:
        return f"Clause {numbered_lead.group(1).strip()} ({numbered_lead.group(2).strip()})"

    return "General Statutory Provision"


def _split_long_paragraph(text: str, max_chars: int = 900) -> List[str]:
    """Splits oversized text blocks into natural sentence-level sub-chunks."""
    if len(text) <= max_chars:
        return [text]

    sentences = re.split(r"(?<=[.!?\n])\s+", text)
    sub_chunks: List[str] = []
    current_buf: List[str] = []
    current_len = 0

    for sent in sentences:
        s_clean = sent.strip()
        if not s_clean:
            continue
        if current_len + len(s_clean) > max_chars and current_buf:
            sub_chunks.append(" ".join(current_buf))
            current_buf = [s_clean]
            current_len = len(s_clean)
        else:
            current_buf.append(s_clean)
            current_len += len(s_clean) + 1

    if current_buf:
        sub_chunks.append(" ".join(current_buf))

    return sub_chunks if sub_chunks else [text]


def extract_chunks_from_pdf(pdf_path: str, doc_id: str) -> List[Dict[str, Any]]:
    """
    Full extraction pipeline:
      1. Extracts text per page via hybrid OCR (native PyMuPDF -> Tesseract fallback).
      2. Groups short bullet lists and segments paragraphs into clean chunks (100 to 900 chars).
      3. Tags each chunk with page number, detected rule citation, and char offsets.
    """
    pages = extract_text_from_pdf(pdf_path)
    chunks: List[Dict[str, Any]] = []
    chunk_counter = 1

    for page_data in pages:
        page_num = page_data["page_number"]
        page_text = page_data["text"]

        if not page_text or not page_text.strip():
            continue

        # Split into paragraphs on blank lines or double-newlines
        raw_paragraphs = re.split(r"\n{2,}", page_text)

        # If page had no double newlines, try splitting on single newlines followed by numbers or capital letters
        if len(raw_paragraphs) == 1 and len(raw_paragraphs[0]) > 600:
            raw_paragraphs = re.split(r"\n(?=[A-Z0-9\(\[])", raw_paragraphs[0])

        # Consolidate short consecutive fragments (like bullet lists or checklists)
        consolidated_paras: List[str] = []
        buf: List[str] = []
        buf_len = 0

        for raw_p in raw_paragraphs:
            p_strip = raw_p.strip()
            if not p_strip:
                continue
            # Accumulate short lines (e.g. form fields, bullets) unless it starts with Rule or Section
            if len(p_strip) < 40 and not (p_strip.startswith("Rule") or p_strip.startswith("Section")):
                buf.append(p_strip)
                buf_len += len(p_strip)
                if buf_len >= 120:
                    consolidated_paras.append("\n".join(buf))
                    buf = []
                    buf_len = 0
            else:
                if buf:
                    consolidated_paras.append("\n".join(buf))
                    buf = []
                    buf_len = 0
                consolidated_paras.append(p_strip)
        if buf:
            consolidated_paras.append("\n".join(buf))

        if not consolidated_paras and page_text.strip():
            consolidated_paras = [page_text.strip()]

        current_offset = 0

        for para_str in consolidated_paras:
            # Skip trivial 1-2 char noise (e.g. standalone footnote marks)
            if len(para_str) < 15:
                current_offset += len(para_str) + 2
                continue

            # Split paragraphs that are excessively large
            sub_segments = _split_long_paragraph(para_str, max_chars=900)

            for segment in sub_segments:
                seg_clean = segment.strip()
                if len(seg_clean) < 15:
                    continue

                detected_rule = _detect_rule(seg_clean, page_num=page_num)
                clean = normalize_text(seg_clean).lower()
                char_len = len(seg_clean)

                chunks.append({
                    "id": f"{doc_id}_p{page_num}_c{chunk_counter}",
                    "document_id": doc_id,
                    "rule_or_section": detected_rule,
                    "page_number": page_num,
                    "char_start": current_offset,
                    "char_end": current_offset + char_len,
                    "text": seg_clean,
                    "clean_text": clean,
                })
                current_offset += char_len + 2
                chunk_counter += 1

    return chunks
