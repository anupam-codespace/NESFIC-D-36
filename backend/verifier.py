import unicodedata
import re
from typing import Tuple, Optional

def normalize_text(text: str) -> str:
    """
    Applies NFKC Unicode normalization and collapses redundant whitespace.
    Preserves all legal alphanumeric characters and clause numbering.
    """
    if not text:
        return ""
    # Unicode NFKC normalization
    normalized = unicodedata.normalize("NFKC", text)
    # Collapse multiple whitespace / tabs / newlines into a single space
    collapsed = re.sub(r"\s+", " ", normalized).strip()
    return collapsed

def verify_grounding(claim_text: str, source_text: str) -> Tuple[bool, Optional[int]]:
    """
    Deterministically verifies that the extracted claim exists as a verbatim substring
    inside the official gazette source text layer.
    
    Returns:
        (is_grounded, character_offset)
    """
    norm_claim = normalize_text(claim_text).lower()
    norm_source = normalize_text(source_text).lower()

    if not norm_claim or not norm_source:
        return False, None

    offset = norm_source.find(norm_claim)
    if offset != -1:
        return True, offset
    
    return False, None

def verify_rule_citation(rule_no: str, doc_validity: str, supersedes_info: Optional[str] = None) -> Tuple[bool, Optional[str]]:
    """
    Validates if a cited rule is prevailing or has been superseded by an amendment.
    """
    if doc_validity == "superseded":
        return False, f"Notice: This clause was superseded by subsequent Assam Government notification."
    if supersedes_info:
        return True, f"Amendment Notice: This rule incorporates provisions superseding {supersedes_info}."
    return True, None
