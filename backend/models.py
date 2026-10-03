from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from .db import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(String(100), primary_key=True, index=True)
    filename = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    department = Column(String(255), nullable=False)
    doc_type = Column(String(100), nullable=False)
    authority = Column(String(255), nullable=False)
    issue_date = Column(String(50), nullable=False)
    effective_date = Column(String(50), nullable=False)
    version = Column(String(50), nullable=False)
    language = Column(String(50), nullable=False, default="English")
    source_url = Column(String(500), nullable=True)
    review_status = Column(String(50), nullable=False, default="approved")
    validity = Column(String(50), nullable=False, default="active")
    supersedes = Column(String(100), nullable=True)
    superseded_by = Column(String(100), nullable=True)
    sha256 = Column(String(64), nullable=False, unique=True)
    page_count = Column(Integer, default=0)

class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(String(120), primary_key=True, index=True)
    document_id = Column(String(100), ForeignKey("documents.id"), nullable=False, index=True)
    rule_or_section = Column(String(100), nullable=True)
    page_number = Column(Integer, nullable=False)
    char_start = Column(Integer, default=0)
    char_end = Column(Integer, default=0)
    text = Column(Text, nullable=False)
    clean_text = Column(Text, nullable=False)

class AuditLedger(Base):
    __tablename__ = "audit_ledger"

    id = Column(String(100), primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    role = Column(String(50), nullable=False)
    query = Column(Text, nullable=False)
    outcome = Column(String(50), nullable=False)
    rule_cited = Column(String(100), nullable=True)
    document_title = Column(String(255), nullable=True)
    page_cited = Column(Integer, nullable=True)
    sha256 = Column(String(64), nullable=True)
    verifier_status = Column(String(50), nullable=False)
    latency_ms = Column(Integer, default=0)
