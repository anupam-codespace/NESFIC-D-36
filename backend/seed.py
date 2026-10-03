import os
import json
from .db import engine, Base, SessionLocal
from .models import Document, Chunk
from .chunker import extract_chunks_from_pdf
from .ocr import get_page_count

def seed_database():
    """
    Creates tables and ingests all verified Assam Government PDFs into SQLite.
    """
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    base_dir = os.path.dirname(os.path.dirname(__file__))
    corpus_dir = os.path.join(base_dir, "corpus")
    manifest_path = os.path.join(corpus_dir, "manifest.json")

    if not os.path.exists(manifest_path):
        print(f"Error: manifest.json not found at {manifest_path}")
        return

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest_docs = json.load(f)

    print(f"Ingesting {len(manifest_docs)} documents into VidhiAI SQLite database...")
    total_chunks = 0

    for doc_data in manifest_docs:
        doc_id = doc_data["id"]
        pdf_path = os.path.join(corpus_dir, doc_data["filename"])

        page_count = 0
        if os.path.exists(pdf_path):
            page_count = get_page_count(pdf_path)

        # Check existing
        existing_doc = session.query(Document).filter(Document.id == doc_id).first()
        if existing_doc:
            session.delete(existing_doc)
            session.query(Chunk).filter(Chunk.document_id == doc_id).delete()
            session.commit()

        db_doc = Document(
            id=doc_id,
            filename=doc_data["filename"],
            title=doc_data["title"],
            department=doc_data["department"],
            doc_type=doc_data["doc_type"],
            authority=doc_data["authority"],
            issue_date=doc_data["issue_date"],
            effective_date=doc_data["effective_date"],
            version=doc_data["version"],
            language=doc_data.get("language", "English"),
            source_url=doc_data.get("source_url"),
            review_status=doc_data.get("review_status", "approved"),
            validity=doc_data.get("validity", "active"),
            supersedes=doc_data.get("supersedes"),
            superseded_by=doc_data.get("superseded_by"),
            sha256=doc_data["sha256"],
            page_count=page_count,
        )
        session.add(db_doc)

        # Extract and insert chunks
        if os.path.exists(pdf_path):
            chunks = extract_chunks_from_pdf(pdf_path, doc_id)
            for c in chunks:
                db_chunk = Chunk(
                    id=c["id"],
                    document_id=c["document_id"],
                    rule_or_section=c["rule_or_section"],
                    page_number=c["page_number"],
                    char_start=c["char_start"],
                    char_end=c["char_end"],
                    text=c["text"],
                    clean_text=c["clean_text"],
                )
                session.add(db_chunk)
            total_chunks += len(chunks)
            print(f"  [+] Ingested: {doc_data['title']} ({page_count} pages, {len(chunks)} chunks)")

    session.commit()
    session.close()
    print(f"\nSuccessfully seeded VidhiAI database with {len(manifest_docs)} documents and {total_chunks} chunks.")

if __name__ == "__main__":
    seed_database()
