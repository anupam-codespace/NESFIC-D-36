import pytest
from backend.verifier import normalize_text, verify_grounding, verify_rule_citation

def test_nfkc_normalization():
    raw_str = "Rule  41(2) \t\n Net  Qualifying\u00A0Service "
    normalized = normalize_text(raw_str)
    assert normalized == "Rule 41(2) Net Qualifying Service"

def test_exact_substring_grounding_success():
    source = "Under the Assam Services (Pension) Rules 1969, where AE = Average Emoluments, QS = Qualifying Service Maximum upto 33 Years."
    claim = "where AE = Average Emoluments, QS = Qualifying Service Maximum upto 33 Years."
    is_grounded, offset = verify_grounding(claim, source)
    assert is_grounded is True
    assert offset is not None
    assert offset >= 0

def test_whitespace_invariant_grounding():
    source = "Section 8(1) mandates that an appeal may be preferred within 30 days."
    claim = "Section  8(1)  mandates   that an appeal may be preferred within 30 days."
    is_grounded, offset = verify_grounding(claim, source)
    assert is_grounded is True

def test_hallucination_rejection():
    source = "Under the Assam Services (Pension) Rules 1969, where AE = Average Emoluments, QS = Qualifying Service Maximum upto 33 Years."
    hallucinated_claim = "Under Central Civil Services rules, maximum qualifying service is 40 years."
    is_grounded, offset = verify_grounding(hallucinated_claim, source)
    assert is_grounded is False
    assert offset is None

def test_empty_string_rejection():
    is_grounded, offset = verify_grounding("", "Some source text")
    assert is_grounded is False
    assert offset is None

def test_superseded_rule_detection():
    # Active rule
    is_valid, notice = verify_rule_citation("Rule 41(2)", "active")
    assert is_valid is True
    assert notice is None

    # Superseded rule
    is_valid, notice = verify_rule_citation("Circular 1989", "superseded")
    assert is_valid is False
    assert "superseded" in notice.lower()

    # Rule with superseding notice
    is_valid, notice = verify_rule_citation("Rule 41(2)", "active", supersedes_info="Finance Dept Notification 2018")
    assert is_valid is True
    assert "Amendment Notice" in notice
