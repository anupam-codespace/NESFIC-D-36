# Project Proposal & Technical Report
## Trusted Government Knowledge, Rules & Document Assistant
### A Sovereign Administrative Intelligence Platform Delivering Verbatim Statutory Grounding, Multi-Department Rule Synthesis, and Decision-Support for the Government of Assam

**Problem Statement No.:** PS No. 46 · NESFIC-D-36  
**Submitted to:** Administrative Reforms, Assam Administrative Staff College (AASC), Department of Science & Technology, Pension & Public Grievances Department, and Assam State Space Application Centre (ASSAC), Government of Assam  
**Submission type:** Deep-Tech Prototype · Production-Ready  
**Applicant:** Globizhub India Private Limited  
**Date:** October 2026  

---

> **Notice & Disclaimer:** This document represents an independent technical proposal and functional prototype submitted in response to challenge problem statement PS No. 46 / NESFIC-D-36 issued under the North East Seva First Innovation Challenge 2026 (NESFIC 2026) under the *Seva Sankalp Abhiyan*. It is designed to demonstrate technical feasibility, deterministic statutory grounding, and administrative decision-support workflows. It is not an officially commissioned, endorsed, or operational system of the Government of Assam or any department thereof.

---

## 1. Company Overview & Corporate Identity

* **Company Name:** Globizhub India Private Limited
* **Industry Sector:** Information Technology (IT) Services, Software Solutions & Deep-Tech GovTech AI
* **Website:** https://globizhub.com/

---

## 2. Registration & Accreditation Details

* **Corporate Identification Number (CIN):** U74999KA2019PTC120377
* **DPIIT Recognition Number:** DIPP250200
* **MASI Registration Number:** MASI2025/1029

---

## 3. Office Locations & Addresses

* **Registered Address (Karnataka):** No. 594/4/2, First Floor, Opposite to BDS Nagar, RK Nagar 2, Kothanur Main Road, Bangalore, Karnataka — 560077
* **Branch Office (Assam):** No. 59, First Floor, Nayanpur Road, Ganeshguri, Guwahati, Kamrup Metropolitan, Assam — 781006

---

## 4. Leadership & Key Contacts

* **Key Contact Person:** Ethesham Hussain Hashmi (Director, M.Sc., Ph.D.) | Email: admin@globizhub.com | Phone: +91 9401317482 / +91 9585123786
* **Executive Leadership:** Mashuda Manjur (Director, M.Sc.) | Email: mashuda.manjur@globizhub.com | Phone: +91 9940131230
* **Corporate Email:** admin@globizhub.com

---

## 5. Problem Statement

Administrative governance in Assam is operationalised through a large portfolio of gazettes, notifications, service rules, executive guidelines, and office memoranda across multiple nodal line departments — Administrative Reforms & Training, Assam Administrative Staff College (AASC), Department of Science & Technology (DST), Pension & Public Grievances Department, and Assam State Space Application Centre (ASSAC). Each department manages critical statutory mandates, qualifying service determinations, and citizen-facing services. Yet an operational gap exists between legislative intent and administrative disposal:

1. **For Department Desk Officers & Secretariat Branches:** Official rules, amendments, and executive circulars reside scattered across scanned historical PDF archives, legacy paper records, and disparate departmental desks. Desk officers spend hours manually searching for prevailing clauses and verifying whether an earlier rule has been superseded by a subsequent circular, leading to file pendency and procedural delays.
2. **For State Administrators & Civil Service Training (AASC):** When inducting and training Assam Civil Services (ACS) and departmental personnel, curricula rely on static digests that quickly fall out of sync with real-time statutory amendments. Supervisory authorities lack a centralized, searchable intelligence platform to monitor knowledge utilization and ensure uniformity across departments.
3. **For Technical & Spatial Governance (DST & ASSAC):** Complex technical guidelines for remote sensing, geospatial land demarcation, and digital infrastructure require strict adherence to statutory specifications. Non-technical officers frequently struggle to locate and interpret specialized norms without inter-departmental referrals.
4. **For Retiring Employees & Public Pensioners:** Retiring government servants and citizens face significant bureaucratic friction understanding pension eligibility, qualifying service calculations, and requisite forms (e.g., Form 7, No Demand Certificates) under the *Assam Services (Pension) Rules 1969*, often resulting in avoidable grievances.

---

## 6. Solution Overview

We present **Trusted Government Knowledge, Rules & Document Assistant** — a sovereign, deep-tech administrative intelligence platform that transitions knowledge management from periodic manual search to continuous operational intelligence. The platform comprises five interconnected operational layers:

1. **Multimodal Document Intelligence & Ingestion Pipeline:** High-throughput document processor featuring adaptive contrast enhancement, layout-aware segmentation, and dual-layer analysis. Extracts structured text from both digital gazettes and legacy archives, with bilingual support for Assamese and English administrative fonts.
2. **Structural Chunking & Statutory Rule Parsing Layer:** Custom algorithmic chunker that detects statutory section boundaries (e.g., *Rule 41(2)*, *Section 9(1)*) and consolidates structured lists, preventing broken clauses and preserving legal context.
3. **Deterministic Hybrid RAG Engine & Operative Quote Extractor:** High-performance retrieval engine pairing BM25 sparse keyword matching with dense semantic embeddings and reciprocal rank fusion. A substantive sentence extractor isolates operative legal provisions to eliminate administrative boilerplate.
4. **Strict Character-Level Verifier Guardrail:** Mathematical character-level NFKC string grounding validator. Every statement synthesized by the system is cross-referenced against the verbatim text layer of the cited gazette. If a claim lacks exact substring grounding, the response is safely withheld.
5. **Secretariat Green-Sheet Noting & Cryptographic Audit Layer:** Formats verified statutory answers directly into standard Assam Secretariat Manual notings. Every ingested document chunk and generated noting is timestamped and cryptographically hashed (SHA-256), establishing a continuous audit trail.

---

## 7. Core Architectural Capabilities

The platform introduces the following architectural innovations tailored to Assam's administrative framework:

1. **Character-Level NFKC String Grounding (Verbatim Accuracy Guarantee):** The verifier normalizes unicode characters and verifies that every statutory citation is an exact, byte-level substring of the official gazette. Extrapolations and ungrounded statements are strictly prohibited.
2. **Role-Based Access Control with Server-Side Enforcement:** Dedicated workspaces for STATE_ADMIN (full statewide visibility), DEPT_OFFICER (department-scoped with instant noting generation), and CITIZEN (plain-language eligibility summaries with transparent document page viewers).
3. **Safe Refusal & Administrative Escalation Protocol:** When queried on matters outside the active statutory index, the platform refuses to synthesize ungrounded speculation, instead logging the query for departmental nodal officer review.
4. **Bilingual Script Ingestion Readiness:** Foundational tokenization pipeline architected for seamless processing of Assamese script (Asomiya) alongside English administrative gazettes.
5. **Sovereign On-Premise Deployability:** Designed for deployment within the Assam State Data Centre (SDC) or MeitY-empanelled sovereign cloud infrastructure, ensuring confidential government files remain within state-controlled perimeters.

---

## 8. Technology Stack & Implementation Status

### Implemented Prototype Features

| Layer | Implemented Prototype Technologies |
| :--- | :--- |
| **Frontend Framework** | Next.js 16 (App Router, Turbopack), React 19, TypeScript 5, Tailwind CSS 4, shadcn/ui, Lucide React icons, Framer Motion |
| **Accessibility & UI** | GIGW 3.0 compliant, Screen Reader ARIA landmarks, `A-`/`A+` font resizer, SpeechSynthesis audio narrator (`Hear`), Bilingual selector (`EN`/`AS`) |
| **Backend & Database** | FastAPI / Python 3.9+ asynchronous REST API, SQLite3 relational metadata index, PyMuPDF (fitz) dual-layer document extraction engine |
| **Grounding & RAG Engine** | Hybrid BM25 + dense vector indexing, deterministic substantive quote extractor, character-level NFKC verifier engine |
| **Access Control** | Role-scoped session handling (Super Admin, Desk Officer, Citizen), scoped document filtering via `dept_scope` |
| **Audit Ledger** | SHA-256 cryptographic document chunk hashing, immutable noting timestamps, CSV telemetry export |

### Proposed Production Architecture

| Component | Production Architecture Plan |
| :--- | :--- |
| **Direct Gazette Ingestion** | Automated sync connector with the Assam Government e-Gazette repository and departmental MIS portals |
| **Enterprise IAM** | Integration with official State SSO (*Jan Parichay* / *e-Pramaan*) with Multi-Factor Authentication (MFA) |
| **Sovereign Deep Tech SLM** | Fine-tuned 7B/14B parameter Indian Legal Small Language Model deployed on dedicated SDC GPU nodes (vLLM / TensorRT-LLM) |
| **Bilingual Vision-Language Pipeline** | Custom vision-language model fine-tuned on historical Assam Government font ligatures and official seal marks |
| **Security & Compliance** | Full CERT-In empanelled VAPT auditing, STQC GIGW 3.0 compliance certification, and DPDP Act 2023 adherence |
| **Workflow Automation** | Integration with e-Office (NIC) for direct insertion of AI-generated verified green-sheet notings into official files |

---

## 9. Current Stage & Production Deployment

**Functional Deep-Tech Prototype · Production-Ready.** A working full-stack platform is deployed using official Assam gazettes across Pension Rules 1969, ARTPS Act 2012, Mission Basundhara guidelines, and DST circulars. The system includes multi-route navigation, role-based desk isolation, dual-layer document extraction, character-level verification, automated green-sheet noting generation, and a continuous audit trail.

* **Production Link:** [https://nesfic-d-36.vercel.app](https://nesfic-d-36.vercel.app)
* **Source Code Repository:** [https://github.com/anupam-codespace/NESFIC-D-36.git](https://github.com/anupam-codespace/NESFIC-D-36.git)

| Feature | Status | Production Scope |
| :--- | :--- | :--- |
| **Multi-Route Navigation** | Implemented | Integration with State portal master navigation |
| **Accessibility Suite (TTS & Font Resizer)** | Implemented | STQC certified WCAG 2.1 AAA compliance |
| **Multi-Department Gazette Ingestion** | Implemented | Automated e-Gazette webhook listener |
| **Dual-Layer Document Extraction** | Implemented | Distributed GPU-accelerated ingestion workers |
| **Character-Level Verifier Guardrail** | Implemented | Formally verified mathematical proof engine |
| **Secretariat Green-Sheet Noting Generator** | Implemented | Direct integration with NIC e-Office file dispatch |
| **Role-Based Desk Isolation (Admin/Officer/Citizen)**| Implemented | Jan Parichay enterprise SSO integration |
| **Live Telemetry & Performance Benchmarks** | Implemented | Real-time Prometheus/Grafana monitoring |
| **SHA-256 Cryptographic Audit Ledger** | Implemented | Hyperledger / State Blockchain notarization |
| **Public Transparency & Citizen Inquiry** | Implemented | Sewa Setu / RTPS citizen service integration |

---

## 10. Stakeholder & Context Analysis

### Target Stakeholders

1. **Primary Regulatory & Administrative Bodies (B2G):** Administrative Reforms Department (statutory compliance), Assam Administrative Staff College (ACS civil service training), Department of Science & Technology & ASSAC (geospatial/technical guidelines), and Pension & Public Grievances Department.
2. **Internal Administrative Cadre:** Joint Secretaries, Deputy Secretaries, Under Secretaries, Section Officers, and Senior Assistants across line departments responsible for file drafting and statutory approvals.
3. **Public Beneficiaries:** Retiring government employees, pensioners, and citizens who benefit from transparent entitlement interpretations and verified eligibility calculations.

### Contextual Differentiation

Existing administrative workflows rely on manual circular physical files and static digests. Generic AI and ticketing platforms lack awareness of Assam's statutory workflows, secretariat green-sheet noting hierarchies, and departmental jurisdictions. VidhiAI is purpose-built for the Assam context — it models the exact statutory relationships between principal acts and amending notifications, ensures 100% evidence-grounded answers, and formats results directly into the green-sheet notings officers already know.

---

## 11. Intellectual Property & Licensing

* **IP Status:** Proprietary software architecture developed for the challenge; the source code for the platform is provided for evaluation purposes.
* **Patent Strategy:** Provisional domestic patent planned covering the method and architecture for real-time statutory verification, automated green-sheet noting generation, and cryptographic provenance tracking in administrative governance.
* **Deployment Model:** Proposed as an indigenous SaaS / GovTech model deployable on the State Data Centre (SDC) or MeitY-empanelled cloud infrastructure, with the option of an on-premise deployment for air-gapped secretariats.

---

## 12. Funding & Staged Milestones

<b>Requested Grant:</b> ₹40,00,000 (Rupees Forty Lakhs) — Deep Tech Grant / Assam Startup Scheme.

| # | Milestone | Budget | Share | Prerequisites | Deliverables |
| :-: | :--- | :-: | :-: | :--- | :--- |
| **1** | **Multi-Department Data & Gazette Corpus Engineering** | ₹6,40,000 | 16% | Gazette archives from AASC, Pension, ARTPS, DST, ASSAC | Comprehensive Assam statutory ontology; structured JSON schema; multimodal ingestion pipeline |
| **2** | **Bilingual Assamese Document Intelligence & Ingestion Engine** | ₹10,40,000 | 26% | Historical gazettes corpuses; State Data Centre sandbox | Custom vision-language model fine-tuned on Assamese ligatures (98%+ benchmark); dual-layer connector with retry logic |
| **3** | **Sovereign Legal SLM & Zero-Hallucination Grounding Engine** | ₹10,80,000 | 27% | Secretariat Manual precedents; annotated green-sheet notings | Domain-adapted 7B/14B parameter Legal SLM; character-level NFKC verifier engine; automated statutory conflict graph |
| **4** | **Multi-Department Secretariat Pilot & Security Hardening** | ₹7,60,000 | 19% | Pilot clearance (Administrative Reforms, AASC, Pension); MeitY staging cloud | 60-day live pilot across 3 nodal departments (100+ officers); CERT-In VAPT audit report; GIGW 3.0 accessibility verification |
| **5** | **Legal & Scale Readiness, Provenance Ledger & SDC Deployment** | ₹4,80,000 | 12% | Pilot telemetry data; SDC production container clearance | Evaluation report; statewide rollout blueprint; SHA-256 cryptographic provenance ledger; SDC bare-metal deployment |
| | **Total** | **₹40,00,000** | **100%** | | |

---

## 13. Projected Impact & Evaluation

*Targeted estimates based on pilot benchmarks.*

### Administrative Impacts

1. **Accelerated Evidence Retrieval:** Reduces evidence-assembly and rule cross-referencing time for file reviews from hours to minutes, dramatically accelerating Secretariat decision-making.
2. **Proactive Operational Triage:** Surfaces operative clauses, qualifying service rules, and entitlement ceilings within seconds of query submission — eliminating the lag between file intake and supervisory disposal.
3. **Objective Merit Recognition:** Continuous per-scheme progress and audit-logged noting records establish an objective basis for recognizing high-performing officers and departments.
4. **Citizen-Centric Transparency:** Plain-language entitlement summaries and transparent source document inspections restore citizen trust in government pension and public service delivery.

### Employment & Capacity Targets

* **Direct Technical Roles:** 6–10 engineering, AI/ML research, legal ontology, and GIS data roles based in Assam (Guwahati branch office).
* **Ecosystem Support Roles:** 25–40 indirect technical and training support positions across districts (nodal officers, digitization operators, field trainers).

---

## 14. Alignment with Assam Startup Policy 2025–2030

**Primary Category:** Category B — IT, ITeS & Artificial Intelligence (Deep Tech Specialization)

The proposal aligns with the "Innovate Assam 2030" key strategic focus areas:

1. **Domestic GovTech Innovation:** Indigenous technology built for Government of Assam needs, addressing the specific statutory workflows of Administrative Reforms, AASC, DST, Pension & PG, and ASSAC.
2. **Data Governance:** High-performance web tools, deterministic verification algorithms, RBAC, and audit trails engineered by regional talent based at the Guwahati branch office.
3. **Citizen-Centric Governance:** Supports the statutory objectives of transparent pension processing, entitlement verification, and grievance redressal under the Assam Right to Public Services Act (ARTPS).
4. **Employment Generation:** Direct and indirect technical roles based in Assam, with specialized AI training programs for secretariat staff and departmental nodal officers.
