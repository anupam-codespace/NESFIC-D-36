# Project Proposal & Technical Report
## Trusted Government Knowledge, Rules & Document Assistant
### A Sovereign Generative AI, Verbatim Statutory Grounding & Document Scrutiny Platform for the Government of Assam

**Challenge Problem Statement No.:** 46 · NESFIC-D-36  
**Submitted to:** Administrative Reforms, Assam Administrative Staff College (AASC), Department of Science & Technology, Pension & Public Grievances Department, and Assam State Space Application Centre (ASSAC), Government of Assam  
**Submission Type:** Functional Deep-Tech MVP Prototype · Demonstration-Ready  
**Applicant:** Globizhub India Private Limited  
**Date:** October 2026  

---

> **Notice & Disclaimer:** This document represents an independent technical proposal and functional prototype submitted in response to challenge problem statement **PS No. 46 / NESFIC-D-36** issued under the **North East Seva First Innovation Challenge 2026 (NESFIC 2026)** under the *Seva Sankalp Abhiyan*. It is designed to demonstrate technical feasibility, deterministic zero-hallucination statutory verification, and decision-support workflows. It is not an officially commissioned, endorsed, or operational system of the Government of Assam or any department thereof.

---

## 1. Company Overview & Corporate Identity

* **Company Name:** Globizhub India Private Limited
* **Industry Sector:** Information Technology (IT) Services, Software Solutions & Deep-Tech GovTech AI
* **Website:** [https://globizhub.com/](https://globizhub.com/)

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

* **Key Contact Person:** Ethesham Hussain Hashmi (Director, M.Sc., Ph.D.)  
  *Email:* admin@globizhub.com | *Phone:* +91 9401317482 / +91 9585123786
* **Executive Leadership:** Mashuda Manjur (Director, M.Sc.)  
  *Email:* mashuda.manjur@globizhub.com | *Phone:* +91 9940131230
* **Corporate Email:** admin@globizhub.com

---

## 5. Problem Statement

Administrative governance in the Government of Assam is governed by thousands of gazette notifications, service rules, executive guidelines, and office memoranda spread across multiple nodal departments:
* **Administrative Reforms & Training (ARTPS)**
* **Assam Administrative Staff College (AASC)**
* **Department of Science & Technology (DST)**
* **Pension & Public Grievances Department**
* **Assam State Space Application Centre (ASSAC)**

While these statutory rules form the backbone of legal administration, a severe operational gap exists between legislative intent, administrative file disposal, and citizen service delivery:

1. **For Department Desk Officers & Secretariat Branches:** Official rules, amendments, and executive circulars reside scattered across scanned historical PDF archives, legacy paper records, and disparate departmental desks. Desk officers spend hours manually searching for prevailing clauses, verifying whether an earlier rule has been superseded by a subsequent circular, leading to file pendency and procedural delays.
2. **For State Administrators & Civil Service Training (AASC):** When inducting and training Assam Civil Services (ACS) and departmental personnel, curricula rely on static digests that quickly fall out of sync with real-time statutory amendments. Supervisory authorities lack a centralized, searchable intelligence platform to monitor knowledge utilization and ensure uniformity across departments.
3. **For Technical & Spatial Governance (DST & ASSAC):** Complex technical guidelines for remote sensing, geospatial land demarcation, and digital infrastructure require strict adherence to statutory specifications. Non-technical officers frequently struggle to locate and interpret specialized norms without inter-departmental referrals.
4. **For Retiring Employees & Public Pensioners:** Retiring government servants and citizens face significant bureaucratic friction understanding pension eligibility, qualifying service calculations, and requisite forms (e.g., Form 7, No Demand Certificates) under the *Assam Services (Pension) Rules 1969*, often resulting in avoidable grievances.
5. **The Unacceptable Risk of Generic AI in Governance:** Standard commercial Large Language Models (LLMs) hallucinate plausible-sounding legal clauses, invent nonexistent government circulars, and cannot provide byte-accurate evidence citations. In public administration and statutory law, unverified synthetic text creates severe legal liability and compromises public trust.

---

## 6. Solution Overview

We present **Trusted Government Knowledge, Rules & Document Assistant (VidhiAI / NESFIC-D-36)** — a sovereign, deep-tech GovTech intelligence platform engineered specifically for the Government of Assam. The platform transitions administrative knowledge management from fragmented manual paper-search to continuous, verifiable, zero-hallucination operational intelligence.

The architecture comprises six interconnected operational layers:

1. **Dual-Layer 300 DPI OCR & Ingestion Pipeline:** High-throughput document processor featuring PIL/OpenCV-based adaptive contrast enhancement, skew correction, and dual-layer layout analysis. Extracts text layers from both clean digital gazettes and degraded historical scanned circulars, with dedicated support for English and Assamese statutory fonts.
2. **Structural Chunking & Statutory Rule Parsing Layer:** Custom algorithmic chunker that detects statutory section boundaries (e.g., `Rule 41(2)`, `Section 9(1)`, `Clause 1.19`) and consolidates structured lists, preventing broken clauses and preserving legal context.
3. **Deterministic Retrieval & Substantive Quote Extractor:** Hybrid search engine pairing BM25 keyword matching with dense semantic embeddings. A substantive sentence extractor isolates statutory operative sentences (containing verbs such as *mandates*, *shall*, *entitles*, *capped*) to eliminate decorative boilerplate.
4. **Zero-Hallucination Strict Verifier Guardrail:** Mathematical character-level NFKC string grounding validator. Every statement generated by the assistant is cross-referenced against the verbatim text layer of the cited gazette. If a claim lacks exact substring grounding, the response is rejected with a safe failure message.
5. **Audit-Ready Secretariat Green-Sheet Noting Generator:** Automatically formats statutory answers into standard Assam Secretariat Manual notings—complete with Reference File Number, Statutory Rule Citation, Verification Stamp, and Action Recommendation.
6. **SHA-256 Cryptographic Provenance Ledger:** Every ingested document chunk and every issued administrative noting is timestamped and cryptographically hashed, guaranteeing immutable traceability for vigilance audits and administrative inquiries.

---

## 7. Core Architectural Capabilities

The platform introduces the following deep-tech innovations tailored to Assam's administrative framework:

1. **Character-Level NFKC String Grounding (Zero Hallucination Guarantee):** The verifier normalizes unicode characters and verifies that every statutory citation is an exact, byte-level substring of the official gazette. Extrapolations are strictly prohibited.
2. **Departmental Context Boundary & Role-Based Access Control (RBAC):** Server-side enforcement provides dedicated workspaces for:
   * **State Admin / AASC:** Statewide visibility across all departmental gazettes and cryptographic audit logs.
   * **Desk Officer (Pension / ARTPS / DST / ASSAC):** Auto-scoped to departmental circulars with instant noting generation.
   * **Citizen / Public Persona:** Plain-language eligibility summaries with transparent document page viewers.
3. **Safe Refusal & Audit Escalation Protocol:** When queried on matters outside the active statutory index, the platform refuses to synthesize ungrounded speculation, instead logging the query for departmental nodal officer review.
4. **Bilingual Script Ingestion Readiness:** Foundational tokenization pipeline architected for seamless processing of Assamese script (*অসমীয়া লিপি*) alongside English administrative gazettes.
5. **Sovereign On-Premise Deployability:** Designed for deployment within the Assam State Data Centre (SDC) or MeitY-empanelled sovereign cloud infrastructure, ensuring all confidential government files remain within government-controlled perimeters.

---

## 8. Technology Stack & Implementation Status

### Implemented Prototype Features

| Layer | Implemented Prototype Technologies |
| :--- | :--- |
| **Frontend Framework** | Next.js 16 (App Router, Turbopack), React 19, TypeScript 5, Vanilla CSS Responsive Design System, Ant Design 6.x, Lucide React icons, Framer Motion |
| **Accessibility & UI** | GIGW 3.0 compliant, Screen Reader ARIA landmarks, `A-`/`A+` font resizer, SpeechSynthesis audio narrator (`Hear`), Bilingual language selector (`EN`/`AS`) |
| **Backend & API** | FastAPI / Python 3.9+ asynchronous REST API, SQLite3 relational metadata index, PyMuPDF (fitz) dual-layer OCR extraction engine |
| **Grounding & RAG Engine** | Hybrid BM25 + dense vector indexing, deterministic substantive quote extractor, character-level NFKC verifier engine |
| **Access Control & RBAC** | Role-scoped session handling (Super Admin, Desk Officer, Citizen), scoped document filtering via `dept_scope` |
| **Audit Ledger** | SHA-256 cryptographic document chunk hashing, immutable noting timestamps, CSV telemetry export |

### Proposed Production Architecture

| Component | Production Architecture Plan |
| :--- | :--- |
| **Direct Gazette Ingestion** | Automated sync connector with the Assam Government e-Gazette repository and departmental MIS portals |
| **Enterprise IAM** | Integration with official National/State Single Sign-On (*Jan Parichay* / *e-Pramaan*) with Multi-Factor Authentication (MFA) |
| **Sovereign Deep Tech SLM** | Fine-tuned 7B/14B parameter Indian Legal Small Language Model deployed on dedicated SDC GPU nodes (vLLM / TensorRT-LLM) |
| **Bilingual Assamese OCR** | Custom vision-language OCR pipeline fine-tuned on historical Assam Government font ligatures and stamp marks |
| **Security & Compliance** | Full CERT-In empanelled VAPT auditing, STQC GIGW 3.0 compliance certification, and DPDP Act 2023 adherence |
| **Workflow Automation** | Integration with e-Office (NIC) for direct insertion of AI-generated verified green-sheet notings into official files |

---

## 9. Current Stage & Demonstration

**Functional MVP Prototype · Demonstration-Ready.** A fully functional, responsive, and deployed prototype is live. The system indexes official Assam gazette collections across Pension Rules 1969, ARTPS Act 2012, Mission Basundhara guidelines, and DST circulars, delivering sub-second verbatim grounding with zero hallucination.

* **Live Web Demonstration URL:** [https://nesfic-d-36.vercel.app](https://nesfic-d-36.vercel.app)
* **Source Code Repository:** [https://github.com/anupam-codespace/NESFIC-D-36.git](https://github.com/anupam-codespace/NESFIC-D-36.git)

### Feature Implementation Status Matrix

| Feature | Status | Production Scope |
| :--- | :--- | :--- |
| **Bilingual Government Header & Banner** | Implemented | Integration with State portal master navigation |
| **Accessibility Suite (TTS Audio & Font Scaler)** | Implemented | STQC certified WCAG 2.1 AAA compliance |
| **Multi-Department Gazette Ingestion** | Implemented | Automated e-Gazette webhook listener |
| **Dual-Layer 300 DPI OCR Extraction** | Implemented | Distributed GPU-accelerated OCR workers |
| **Character-Level Verifier Guardrail** | Implemented | Formally verified mathematical proof engine |
| **Secretariat Green-Sheet Noting Generator** | Implemented | Direct integration with NIC e-Office file dispatch |
| **Role-Based Desk Isolation (Admin/Officer/Citizen)**| Implemented | Jan Parichay enterprise SSO integration |
| **Live Telemetry & Performance Benchmarks** | Implemented | Real-time Prometheus/Grafana monitoring |
| **SHA-256 Cryptographic Audit Ledger** | Implemented | Hyperledger / State Blockchain notarization |
| **Public Transparency & Citizen Inquiry** | Implemented | Sewa Setu / RTPS citizen service integration |

---

## 10. Stakeholder & Context Analysis

### Target Stakeholders

1. **Primary Regulatory & Secretariat Bodies (B2G):**
   * *Administrative Reforms Department:* Streamlining statutory compliance and departmental rules simplification.
   * *Assam Administrative Staff College (AASC):* Institutionalizing dynamic rules training for ACS officers and Secretariat staff.
   * *Department of Science & Technology (DST) & ASSAC:* Enforcing standard technical and geospatial guidelines.
   * *Pension & Public Grievances Department:* Eliminating pension settlement backlogs and grievance escalations.
2. **Internal Administrative Cadre:**
   * Joint Secretaries, Deputy Secretaries, Under Secretaries, Section Officers, and Senior Assistants across line departments responsible for file drafting and statutory approvals.
3. **Public Beneficiaries & Retiring Officers:**
   * Retiring government employees, pensioners, and citizens requiring clear, authoritative interpretations of Assam service laws and entitlement rules without intermediary exploitation.

### Contextual Differentiation

Generic AI bots fail catastrophically in public administration because they lack contextual awareness of the *Assam Secretariat Manual of Office Procedure*, statutory amendment hierarchies, and departmental jurisdictions. VidhiAI is purpose-built for Assam: it models the exact statutory relationships between principal acts and amending notifications, ensures 100% evidence-grounded answers, and formats results directly into the green-sheet notings officers utilize daily.

---

## 11. Intellectual Property & Licensing

* **IP Status:** Proprietary GovTech software and algorithmic architecture developed specifically for the challenge. Full demonstration source code provided for state evaluation.
* **Patent Strategy:** Provisional domestic patent planned covering:
  1. *Method and System for Deterministic Zero-Hallucination Retrieval and Character-Level NFKC String Grounding in Administrative Legal Documents.*
  2. *Automated Statutory Amendment Reconciliation and Cryptographic Provenance Tracking for Secretariat Decisions.*
* **Deployment Model:** Proposed as an indigenous SaaS / On-Premise GovTech model hosted on the Assam State Data Centre (SDC) or MeitY-empanelled sovereign cloud, with complete data isolation for air-gapped secretariats.

---

## 12. Funding & Staged Milestones

### Dual-Track Deep-Tech Funding Model: Total ₹40,00,000 (Rupees Forty Lakhs)

In alignment with the challenge grant guidelines:
* **Track A (Core MVP & Enterprise Deployment Grant — ₹20,00,000):** Establishes multi-department data connectors, production OCR ingestion, state SSO authentication, security compliance, and a live 60-day secretariat pilot.
* **Track B (Deep-Tech & Generative AI Research Grant — ₹20,00,000):** Funds research-intensive deep-tech development including bilingual Assamese script tokenizer and vision-LLM OCR training, sovereign legal SLM fine-tuning on Assam administrative precedents, and automated statutory conflict graph mapping.

### Comprehensive Milestone Budget Breakdown

| # | Milestone & Work Package | Track | Budget (₹) | Share | Prerequisites | Key Deliverables |
| :-: | :--- | :-: | :-: | :-: | :--- | :--- |
| **1** | **Multi-Department Data & Gazette Ontology Ingestion** | Track A | ₹3,60,000 | 9.0% | Gazette archives from AASC, Pension, ARTPS, DST | Comprehensive Assam statutory data dictionary; structured JSON schema; multi-department ingestion pipeline |
| **2** | **Production Ingestion Engine & SDC Connector** | Track A | ₹5,20,000 | 13.0% | State Data Centre sandbox; API permissions | Production-grade dual-layer OCR connector with automated retry logic, queue management, and reconciliation |
| **3** | **Security Hardening, VAPT & GIGW 3.0 Compliance** | Track A | ₹3,80,000 | 9.5% | MeitY-compliant staging cloud | CERT-In empanelled VAPT audit clearance; GIGW 3.0 accessibility verification; DPDP compliance dossier |
| **4** | **Multi-Department Secretariat Pilot Trial** | Track A | ₹5,00,000 | 12.5% | Pilot clearance (Administrative Reforms, AASC, Pension) | 60-day live pilot across 3 nodal departments; 100+ officers onboarded; end-to-end noting validation report |
| **5** | **Enterprise Scale Readiness & Rollout Blueprint** | Track A | ₹2,40,000 | 6.0% | Pilot telemetry data; legal review | Statewide rollout architectural blueprint; SDC bare-metal deployment scripts; officer training manual |
| **6** | **Bilingual Assamese OCR & Vision-Language Pretraining** | Track B (Deep Tech) | ₹5,50,000 | 13.75% | Historical Assamese printed gazettes & font corpuses | Custom OCR model fine-tuned on Assamese ligatures; 98%+ character recognition benchmark; bilingual chunker |
| **7** | **Sovereign Legal SLM Fine-Tuning for Secretariat Notings** | Track B (Deep Tech) | ₹6,00,000 | 15.0% | Secretariat Manual precedents & annotated notings | Domain-adapted 7B/14B parameter Small Language Model fine-tuned for formal Secretariat noting synthesis |
| **8** | **Automated Statutory Conflict & Amendment Graph** | Track B (Deep Tech) | ₹4,50,000 | 11.25% | Amendment history of Assam Service Rules | Directed Acyclic Graph (DAG) engine detecting repealed clauses, active circulars, and conflicting provisions |
| **9** | **Cryptographic Blockchain Provenance & Air-Gap Build** | Track B (Deep Tech) | ₹4,00,000 | 10.0% | Production container security clearance | SHA-256 tamper-evident provenance ledger; immutable audit trail export; air-gapped on-premise installer |
| | **Total Grant Request (Core MVP + Deep Tech)** | | **₹40,00,000** | **100%** | | **Demonstration-Ready, Scalable GovTech AI for Assam** |

---

## 13. Projected Impact & Evaluation

Targeted estimates based on prototype benchmarks:

### Administrative & Governance Impacts

1. **85% Reduction in File Disposal Time:** Reduces evidence retrieval and rule cross-referencing from an average of 4–6 hours per file to under 2 minutes, dramatically accelerating Secretariat decision-making.
2. **Zero Legal Liability from Hallucinations:** Guarantees that every citation provided in administrative notings is mathematically verifiable against authentic gazettes, protecting officers and the Government from flawed orders.
3. **Pensions and Entitlements Friction Elimination:** Eliminates delays in pension admissibility calculations by providing officers and citizens with immediate, verified formula applications under Rule 41(2) of Assam Pension Rules.
4. **Standardized AASC Training Infrastructure:** Provides Assam Administrative Staff College with an interactive, verified training repository, ensuring trainee officers learn prevailing statutory provisions with instantaneous source inspection.
5. **Full Audit Traceability:** Cryptographic hashing of every search and generated noting ensures transparent compliance with vigilance audits, RTI inquiries, and judicial scrutiny.

### Employment & Capacity Targets

* **Direct High-Tech Jobs:** 8–12 full-time engineering, AI/ML research, legal ontology, and GIS data roles based in Assam at the Globizhub Guwahati branch office.
* **Ecosystem Support Positions:** 30–50 indirect positions across districts for nodal officer training, digitization support, and bilingual Assamese data annotation.

---

## 14. Alignment with Assam Startup Policy 2025–2030

**Primary Category:** Category B — IT, ITeS & Artificial Intelligence (Deep Tech Specialization)

The proposal directly advances the strategic goals of the **Assam Startup Policy 2025–2030** and the **Innovate Assam 2030** roadmap:

1. **Indigenous Deep-Tech GovTech Innovation:** Develops sovereign, state-owned intellectual property in generative AI and legal intelligence, addressing the specific operational needs of the Government of Assam without reliance on foreign proprietary cloud models.
2. **Local Talent & Regional Capacity Building:** AI model fine-tuning, bilingual data engineering, and system development executed by regional technical talent based at Globizhub's Guwahati office.
3. **Citizen-Centric & Transparent Governance:** Directly supports the Assam Right to Public Services Act (ARTPS) and *Seva Sankalp Abhiyan* by ensuring citizens and government servants access accurate statutory entitlements swiftly and transparently.
4. **Exportable Governance IP:** Establishes Assam as a pioneering state in verifiable legal AI, creating a repeatable GovTech blueprint scalable to other North Eastern states and national departments.
