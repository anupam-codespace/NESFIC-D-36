import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_api_health():
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"
    assert data["corpus_documents"] >= 5
    assert data["indexed_chunks"] >= 20

def test_api_list_documents():
    res = client.get("/api/documents")
    assert res.status_code == 200
    docs = res.json()
    assert len(docs) >= 5
    titles = [d["title"] for d in docs]
    assert any("Pension" in t for t in titles)
    assert any("artps" in t.lower() or "public service" in t.lower() for t in titles)

def test_api_ask_pension_officer():
    payload = {
        "query": "How many years of service are required for family pension in Assam?",
        "role": "employee",
        "persona": "officer",
        "language": "en"
    }
    res = client.post("/api/ask", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["outcome"] == "answered"
    assert len(data["claims"]) > 0
    assert data["claims"][0]["page"] >= 1
    assert data["claims"][0]["isVerified"] is True
    assert data["officerNoting"] is not None
    assert "GOA/" in data["officerNoting"]["fileNo"]
    assert data["verifierStatus"].startswith("PASSED")

def test_api_ask_citizen_persona():
    payload = {
        "query": "What are the requirements for pension processing?",
        "role": "employee",
        "persona": "citizen",
        "language": "en"
    }
    res = client.post("/api/ask", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["outcome"] == "answered"
    assert data["citizenGuide"] is not None
    assert len(data["citizenGuide"]["checklist"]) > 0

def test_api_safe_failure_refusal():
    payload = {
        "query": "What is the subsidy percentage for residential solar installation in Assam?",
        "role": "employee",
        "persona": "officer",
        "language": "en"
    }
    res = client.post("/api/ask", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["outcome"] == "insufficient_evidence"
    assert len(data["claims"]) == 0
    assert "REFUSED" in data["verifierStatus"]

def test_api_approve_document():
    res = client.post("/api/documents/doc_mb3_notification/approve")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "approved"
