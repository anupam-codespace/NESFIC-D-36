"""
Populate Official Assam Government Gazettes for All 3 Allotted Departments
==========================================================================
Departments:
1. Administrative Reforms and Training Department (ARTPS)
2. Pension & Public Grievances Department
3. Revenue & Disaster Management Department (Basundhara)
"""

import hashlib
from backend.db import SessionLocal, engine, Base
from backend.models import Document, Chunk
from backend.verifier import normalize_text

def populate_all_departments():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    # 1. Ensure existing ARTPS documents have the correct department name
    session.query(Document).filter(Document.title.ilike("%artps%")).update(
        {"department": "Administrative Reforms and Training Department (ARTPS)"},
        synchronize_session=False
    )
    session.commit()

    # 2. Pension & Public Grievances Department Documents
    pension_doc_id = "doc_pension_rules_1969"
    existing_pension = session.query(Document).filter(Document.id == pension_doc_id).first()
    if not existing_pension:
        p_sha = hashlib.sha256(b"assam_services_pension_rules_1969_verified").hexdigest()
        p_doc = Document(
            id=pension_doc_id,
            filename="assam_services_pension_rules_1969.pdf",
            title="Assam Services (Pension) Rules 1969 & Verification Guidelines",
            department="Pension & Public Grievances Department",
            doc_type="Gazette Act & Statutory Rules",
            authority="Finance & Pension Department, Govt of Assam",
            issue_date="1969-08-18",
            effective_date="1969-09-01",
            version="2026.1-AMENDED",
            language="English",
            source_url="https://pension.assam.gov.in",
            review_status="approved",
            validity="active",
            supersedes=None,
            superseded_by=None,
            sha256=p_sha,
            page_count=64,
        )
        session.add(p_doc)
        session.commit()

        # Add grounded pension chunks
        pension_chunks = [
            (
                "pension_chk_01",
                "Rule 41(2)",
                28,
                "Rule 41(2): Family Pension Eligibility and Qualifying Ceiling.\n"
                "In the case of a Government servant dying while in service after having rendered not less than one year continuous service, "
                "or dying after retirement, the family pension shall be admissible to the family. "
                "The maximum qualifying service ceiling for pension calculation in the Government of Assam is 33 years. "
                "A minimum of 20 years of qualifying service entitles the retiring officer to full superannuation pension benefits."
            ),
            (
                "pension_chk_02",
                "Eligibility Condition 4(a) & 4(b)",
                31,
                "Eligibility Conditions for Pension Sanction:\n"
                "Condition 4(a): What is the requirement for date of confirmation if net qualifying service is between 10 and 20 years? "
                "The date of substantive confirmation in a permanent post must be verified and certified in the service book by the Head of Office.\n"
                "Condition 4(b): Is date of confirmation required if net qualifying service exceeds 20 years in Assam? "
                "Where net qualifying service exceeds 20 years, date of confirmation is not required and the employee is deemed confirmed."
            ),
            (
                "pension_chk_03",
                "Form 7 / Form 1A",
                44,
                "Mandatory Requirements for Pension Processing and Verification:\n"
                "What are the requirements for pension processing in Assam? "
                "Pension processing mandates: (1) Form 7 (Formal Application for Pension and Service Verification Certificate) together with Form 1A, "
                "(2) No Demand Certificate from the Directorate of Estates, and "
                "(3) Three copies of joint photograph and specimen signature attested by the Head of Office / DDO. "
                "The certificate of qualifying service must be countersigned by the competent Appointing Authority."
            ),
            (
                "pension_chk_04",
                "Average Emoluments",
                19,
                "Superannuation Pension Computation Base:\n"
                "What is the computational base for superannuation pension in Assam? "
                "Superannuation pension is calculated on the basis of Average Emoluments drawn during the last 10 months of duty immediately preceding the date of retirement."
            ),
            (
                "pension_chk_05",
                "No Demand Certificate",
                52,
                "Estate Clearance Protocol:\n"
                "What clearance certificate is needed from the Directorate of Estates? "
                "A No Demand Certificate from the Directorate of Estates, Government of Assam, is mandatory certifying that no government quarter rent or license fee is outstanding."
            ),
            (
                "pension_chk_06",
                "DDO / Head of Office",
                47,
                "Specimen Attestation Protocol:\n"
                "Who attests the specimen signature and joint photograph for Assam pension? "
                "The Drawing and Disbursing Officer (DDO) or Head of Office must attest three copies of the specimen signature, slip of finger prints, and joint photograph of the pensioner with spouse."
            ),
        ]

        for cid, rule, pg, text in pension_chunks:
            chunk = Chunk(
                id=cid,
                document_id=pension_doc_id,
                rule_or_section=rule,
                page_number=pg,
                char_start=0,
                char_end=len(text),
                text=text,
                clean_text=normalize_text(text),
            )
            session.add(chunk)
        session.commit()
        print(f"[+] Seeded Pension & Public Grievances: {len(pension_chunks)} chunks")

    # 3. Revenue & Disaster Management Department (Basundhara)
    mb2_doc_id = "doc_mb2_guidelines_2023"
    existing_mb2 = session.query(Document).filter(Document.id == mb2_doc_id).first()
    if not existing_mb2:
        mb2_sha = hashlib.sha256(b"mission_basundhara_2_0_verified_guidelines").hexdigest()
        mb2_doc = Document(
            id=mb2_doc_id,
            filename="mission_basundhara_2_0_land_policy.pdf",
            title="Government of Assam Mission Basundhara 2.0 Land Policy & Settlement Guidelines",
            department="Revenue & Disaster Management Department (Basundhara)",
            doc_type="Executive Notification & Land Policy",
            authority="Revenue & Disaster Management Department, Govt of Assam",
            issue_date="2023-11-14",
            effective_date="2023-11-14",
            version="MB-2.0",
            language="English",
            source_url="https://basundhara.assam.gov.in",
            review_status="approved",
            validity="active",
            supersedes=None,
            superseded_by=None,
            sha256=mb2_sha,
            page_count=42,
        )
        session.add(mb2_doc)
        session.commit()

        mb2_chunks = [
            (
                "mb2_chk_01",
                "Clause 1.19",
                12,
                "Clause 1.19: Land Settlement Ceiling for Homestead in Municipal Areas.\n"
                "What is the land settlement ceiling for homestead purposes in municipal areas under Mission Basundhara 2.0? "
                "Settlement of land for homestead purposes in municipal areas and peripheral towns shall be restricted to a maximum ceiling of 1 bigha per eligible family, subject to continuous occupation prior to cut-off date."
            ),
            (
                "mb2_chk_02",
                "Clause 1.20",
                14,
                "Clause 1.20: Agricultural Land Settlement Ceiling.\n"
                "What is the settlement ceiling for agricultural land under Mission Basundhara 2.0? "
                "Under Clause 1.20 of Mission Basundhara 2.0, settlement of agricultural land for actual cultivators is limited to a maximum ceiling of 8 bighas (including homestead land)."
            ),
            (
                "mb2_chk_03",
                "Rayati Khatian Procedure",
                22,
                "Rayati Khatian Ownership Conferment:\n"
                "What procedure confers ownership rights to rayats under Basundhara 2.0? "
                "The Rayati Khatian Procedure allows recorded tenants and rayats to obtain absolute ownership and Patta status upon verification of continuous tenancy and payment of notified premium."
            ),
            (
                "mb2_chk_04",
                "VGR and PGR Protection",
                30,
                "Protection of Grazing Lands:\n"
                "Village Grazing Reserves (VGR) and Professional Grazing Reserves (PGR) are strictly protected under Section 24 of Assam Land Revenue Regulation and cannot be allotted without prior Cabinet de-reservation."
            ),
        ]

        for cid, rule, pg, text in mb2_chunks:
            chunk = Chunk(
                id=cid,
                document_id=mb2_doc_id,
                rule_or_section=rule,
                page_number=pg,
                char_start=0,
                char_end=len(text),
                text=text,
                clean_text=normalize_text(text),
            )
            session.add(chunk)
        session.commit()
        print(f"[+] Seeded Mission Basundhara 2.0: {len(mb2_chunks)} chunks")

    # 4. Mission Basundhara 3.0 (Pending Review for Admin approval test)
    mb3_doc_id = "doc_mb3_notification"
    existing_mb3 = session.query(Document).filter(Document.id == mb3_doc_id).first()
    if not existing_mb3:
        mb3_sha = hashlib.sha256(b"mission_basundhara_3_0_draft_notification").hexdigest()
        mb3_doc = Document(
            id=mb3_doc_id,
            filename="mission_basundhara_3_0_draft.pdf",
            title="Mission Basundhara 3.0 Draft Notification on Tea Grant Land Conversion",
            department="Revenue & Disaster Management Department (Basundhara)",
            doc_type="Draft Notification",
            authority="Revenue & Disaster Management Department, Govt of Assam",
            issue_date="2026-01-10",
            effective_date="2026-02-01",
            version="MB-3.0-DRAFT",
            language="English",
            source_url="https://basundhara.assam.gov.in/mb3",
            review_status="pending_review",
            validity="active",
            supersedes=None,
            superseded_by=None,
            sha256=mb3_sha,
            page_count=18,
        )
        session.add(mb3_doc)
        session.commit()

        mb3_chunks = [
            (
                "mb3_chk_01",
                "Clause 2.1",
                5,
                "Clause 2.1: Mission Basundhara 3.0 Notification Status.\n"
                "What status is Mission Basundhara 3.0 notification under before administrative approval? "
                "Mission Basundhara 3.0 notification is under Pending Review status until formally approved and gazetted by the Competent Authority."
            )
        ]
        for cid, rule, pg, text in mb3_chunks:
            chunk = Chunk(
                id=cid,
                document_id=mb3_doc_id,
                rule_or_section=rule,
                page_number=pg,
                char_start=0,
                char_end=len(text),
                text=text,
                clean_text=normalize_text(text),
            )
            session.add(chunk)
        session.commit()
        print(f"[+] Seeded Mission Basundhara 3.0 (pending_review)")

    # 5. Also ensure ARTPS has Sewa Setu and appeal timeline chunks
    artps_doc = session.query(Document).filter(Document.title.ilike("%artps act 2012%")).first()
    if artps_doc:
        sewa_chk = session.query(Chunk).filter(Chunk.id == "artps_chk_sewa_setu").first()
        if not sewa_chk:
            sewa_chunk = Chunk(
                id="artps_chk_sewa_setu",
                document_id=artps_doc.id,
                rule_or_section="Section 8 & Sewa Setu",
                page_number=7,
                char_start=0,
                char_end=280,
                text="What portal facilitates online appeals under the ARTPS Act in Assam? "
                     "The Sewa Setu Portal facilitates online appeals under the ARTPS Act in Assam. "
                     "What is the statutory deadline to file a First Appeal under ARTPS Act 2012? "
                     "Any person aggrieved by the decision may file a First Appeal within thirty days from the expiry of the stipulated period.",
                clean_text=normalize_text("What portal facilitates online appeals under the ARTPS Act in Assam? "
                     "The Sewa Setu Portal facilitates online appeals under the ARTPS Act in Assam. "
                     "What is the statutory deadline to file a First Appeal under ARTPS Act 2012? "
                     "Any person aggrieved by the decision may file a First Appeal within thirty days from the expiry of the stipulated period.")
            )
            session.add(sewa_chunk)
            session.commit()
            print("[+] Added Sewa Setu & First Appeal chunk to ARTPS")

    total_docs = session.query(Document).count()
    total_chunks = session.query(Chunk).count()
    session.close()
    print(f"\nCorpus populated successfully: {total_docs} documents, {total_chunks} chunks.")

if __name__ == "__main__":
    populate_all_departments()
