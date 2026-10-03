#!/usr/bin/env python3
"""
NESFIC 2026 - Problem Statement 46 (NESFIC-D-36)
Project Proposal & Technical Report PDF Generator
Produces a submission-ready, print-perfect 7-PAGE PDF matching the exact visual style,
typography, dark green header banner, structured tables, and page flow of teammate submissions.
"""

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm, mm
pt = 1
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Page dimensions for A4
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 40 * pt  # ~0.55 inch margins for crisp, professional density
USABLE_WIDTH = PAGE_WIDTH - 2 * MARGIN

# Register fonts
FONT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fonts')
INTER_FONT = os.path.join(FONT_DIR, 'Inter.ttf')

if os.path.exists(INTER_FONT):
    try:
        pdfmetrics.registerFont(TTFont('Inter', INTER_FONT))
        pdfmetrics.registerFont(TTFont('Inter-Bold', INTER_FONT))
        FONT_REGULAR = 'Inter'
        FONT_BOLD = 'Inter-Bold'
        FONT_ITALIC = 'Inter'
    except Exception as e:
        print(f"Warning loading Inter: {e}. Falling back to standard Helvetica.")
        FONT_REGULAR = 'Helvetica'
        FONT_BOLD = 'Helvetica-Bold'
        FONT_ITALIC = 'Helvetica-Oblique'
else:
    FONT_REGULAR = 'Helvetica'
    FONT_BOLD = 'Helvetica-Bold'
    FONT_ITALIC = 'Helvetica-Oblique'

# Corporate & Theme Colors
PRIMARY_GREEN = colors.HexColor('#084d38')    # Deep Government Assam Forest Green
DARK_TEXT = colors.HexColor('#0f172a')        # Slate 900
BODY_TEXT = colors.HexColor('#1e293b')        # Slate 800
MUTED_TEXT = colors.HexColor('#64748b')       # Slate 500
BORDER_COLOR = colors.HexColor('#cbd5e1')     # Slate 300
TABLE_BG_ALT = colors.HexColor('#f8fafc')     # Slate 50
TOTAL_YELLOW = colors.HexColor('#fef9c3')     # Soft Yellow highlight for Grant Total
ACCENT_GREEN = colors.HexColor('#059669')     # Emerald 600

class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to calculate total page count and draw running header/footer.
    """
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, total_pages):
        page_num = self._pageNumber
        self.saveState()
        
        # Draw running footer on ALL pages
        self.setFont(FONT_REGULAR, 7.5)
        self.setFillColor(MUTED_TEXT)
        
        # Left footer
        footer_text = "Project Proposal & Technical Report — Trusted Government Knowledge Assistant (NESFIC-D-36)"
        self.drawString(MARGIN, 20 * pt, footer_text)
        
        # Right footer
        page_str = f"Page {page_num}"
        self.drawRightString(PAGE_WIDTH - MARGIN, 20 * pt, page_str)
        
        # Thin divider line above footer
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.5)
        self.line(MARGIN, 30 * pt, PAGE_WIDTH - MARGIN, 30 * pt)
        
        # On Page 1, draw the top dark green header banner box!
        if page_num == 1:
            banner_y = PAGE_HEIGHT - MARGIN - 32 * pt
            banner_height = 32 * pt
            
            # Draw green rectangle
            self.setFillColor(PRIMARY_GREEN)
            self.rect(MARGIN, banner_y, USABLE_WIDTH, banner_height, stroke=0, fill=1)
            
            # Left banner text: "Government of Assam"
            self.setFillColor(colors.white)
            self.setFont(FONT_BOLD, 10.5)
            self.drawString(MARGIN + 12 * pt, banner_y + 10 * pt, "Government of Assam")
            
            # Right banner text
            dept_text = "Administrative Reforms · AASC · Science & Technology · Pension & PG · ASSAC"
            self.setFont(FONT_REGULAR, 7.5)
            self.drawRightString(PAGE_WIDTH - MARGIN - 12 * pt, banner_y + 11 * pt, dept_text)
            
        self.restoreState()


def build_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN + 36 * pt,  # Extra space for top banner on Page 1
        bottomMargin=38 * pt
    )

    # Custom typography styles
    style_label = ParagraphStyle(
        'DocLabel',
        fontName=FONT_REGULAR,
        fontSize=9.5,
        leading=13,
        textColor=MUTED_TEXT,
        spaceAfter=6
    )

    style_title = ParagraphStyle(
        'MainTitle',
        fontName=FONT_BOLD,
        fontSize=20,
        leading=24,
        textColor=DARK_TEXT,
        spaceAfter=6
    )

    style_subtitle = ParagraphStyle(
        'SubTitle',
        fontName=FONT_REGULAR,
        fontSize=10.5,
        leading=15,
        textColor=BODY_TEXT,
        spaceAfter=14
    )

    style_h1 = ParagraphStyle(
        'SectionH1',
        fontName=FONT_BOLD,
        fontSize=11,
        leading=15,
        textColor=DARK_TEXT,
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )

    style_h2 = ParagraphStyle(
        'SectionH2',
        fontName=FONT_BOLD,
        fontSize=9.5,
        leading=13,
        textColor=DARK_TEXT,
        spaceBefore=7,
        spaceAfter=4,
        keepWithNext=True
    )

    style_body = ParagraphStyle(
        'BodyTextCustom',
        fontName=FONT_REGULAR,
        fontSize=8.2,
        leading=11.5,
        textColor=BODY_TEXT,
        spaceAfter=5
    )

    style_body_bold = ParagraphStyle(
        'BodyBoldCustom',
        fontName=FONT_BOLD,
        fontSize=8.2,
        leading=11.5,
        textColor=DARK_TEXT,
        spaceAfter=5
    )

    style_disclaimer = ParagraphStyle(
        'DisclaimerText',
        fontName=FONT_ITALIC,
        fontSize=7.8,
        leading=11,
        textColor=colors.HexColor('#475569'),
        spaceBefore=4,
        spaceAfter=4
    )

    style_table_header = ParagraphStyle(
        'TableHeader',
        fontName=FONT_BOLD,
        fontSize=7.5,
        leading=10,
        textColor=DARK_TEXT
    )

    style_table_cell = ParagraphStyle(
        'TableCell',
        fontName=FONT_REGULAR,
        fontSize=7.5,
        leading=10,
        textColor=BODY_TEXT
    )

    style_table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName=FONT_BOLD,
        fontSize=7.5,
        leading=10,
        textColor=DARK_TEXT
    )

    style_grant_banner = ParagraphStyle(
        'GrantBanner',
        fontName=FONT_BOLD,
        fontSize=9,
        leading=12.5,
        textColor=PRIMARY_GREEN,
        spaceBefore=2,
        spaceAfter=2
    )

    elements = []

    # ==========================================
    # PAGE 1: COVER & EXECUTIVE METADATA
    # ==========================================
    elements.append(Spacer(1, 10 * pt))
    elements.append(Paragraph("Project Proposal & Technical Report", style_label))
    elements.append(Paragraph("Real-Time Monitoring & Trusted Government Knowledge Assistant", style_title))
    elements.append(Paragraph(
        "A Sovereign Generative AI, Verbatim Statutory Grounding & Document Scrutiny Platform for the Government of Assam",
        style_subtitle
    ))

    # Metadata Table
    meta_data = [
        [
            Paragraph("<b>Problem Statement No.</b>", style_table_cell_bold),
            Paragraph("PS No. 46 · NESFIC-D-36", style_table_cell)
        ],
        [
            Paragraph("<b>Submitted to</b>", style_table_cell_bold),
            Paragraph("Administrative Reforms, Assam Administrative Staff College (AASC), Department of Science & Technology, Pension & Public Grievances Department, and Assam State Space Application Centre (ASSAC), Government of Assam", style_table_cell)
        ],
        [
            Paragraph("<b>Submission type</b>", style_table_cell_bold),
            Paragraph("Functional Deep-Tech MVP Prototype · Demonstration-Ready", style_table_cell)
        ],
        [
            Paragraph("<b>Applicant</b>", style_table_cell_bold),
            Paragraph("Globizhub India Private Limited", style_table_cell)
        ],
        [
            Paragraph("<b>Date</b>", style_table_cell_bold),
            Paragraph("October 2026", style_table_cell)
        ]
    ]

    meta_table = Table(meta_data, colWidths=[130 * pt, USABLE_WIDTH - 130 * pt])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(meta_table)

    elements.append(Spacer(1, 18 * pt))

    # Notice & Disclaimer Box
    disclaimer_html = (
        "<b>Notice & Disclaimer:</b> <i>This document represents an independent technical proposal and "
        "functional prototype submitted in response to challenge problem statement PS No. 46 / NESFIC-D-36 "
        "issued under the North East Seva First Innovation Challenge 2026 (NESFIC 2026) under the Seva Sankalp Abhiyan. "
        "It is designed to demonstrate technical feasibility, deterministic zero-hallucination statutory verification, "
        "and decision-support workflows. It is not an officially commissioned, endorsed, or operational system of the "
        "Government of Assam or any department thereof.</i>"
    )
    disc_data = [[Paragraph(disclaimer_html, style_disclaimer)]]
    disc_table = Table(disc_data, colWidths=[USABLE_WIDTH])
    disc_table.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0, 0), (-1, -1), 7 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 6 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6 * pt),
    ]))
    elements.append(disc_table)

    elements.append(PageBreak())

    # ==========================================
    # PAGE 2: CORPORATE IDENTITY & PROBLEM STATEMENT (P1)
    # ==========================================
    elements.append(Paragraph("1. Company Overview & Corporate Identity", style_h1))
    c1_data = [
        [Paragraph("<b>Company Name</b>", style_table_cell_bold), Paragraph("Globizhub India Private Limited", style_table_cell)],
        [Paragraph("<b>Industry Sector</b>", style_table_cell_bold), Paragraph("Information Technology (IT) Services, Software Solutions & Deep-Tech GovTech AI", style_table_cell)],
        [Paragraph("<b>Website</b>", style_table_cell_bold), Paragraph("https://globizhub.com/", style_table_cell)]
    ]
    t_c1 = Table(c1_data, colWidths=[130 * pt, USABLE_WIDTH - 130 * pt])
    t_c1.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_c1)
    elements.append(Spacer(1, 6 * pt))

    elements.append(Paragraph("2. Registration & Accreditation Details", style_h1))
    c2_data = [
        [Paragraph("<b>Corporate Identification Number (CIN)</b>", style_table_cell_bold), Paragraph("U74999KA2019PTC120377", style_table_cell)],
        [Paragraph("<b>DPIIT Recognition Number</b>", style_table_cell_bold), Paragraph("DIPP250200", style_table_cell)],
        [Paragraph("<b>MASI Registration Number</b>", style_table_cell_bold), Paragraph("MASI2025/1029", style_table_cell)]
    ]
    t_c2 = Table(c2_data, colWidths=[160 * pt, USABLE_WIDTH - 160 * pt])
    t_c2.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_c2)
    elements.append(Spacer(1, 6 * pt))

    elements.append(Paragraph("3. Office Locations & Addresses", style_h1))
    c3_data = [
        [Paragraph("<b>Registered Address (Karnataka)</b>", style_table_cell_bold), Paragraph("No. 594/4/2, First Floor, Opposite to BDS Nagar, RK Nagar 2, Kothanur Main Road, Bangalore, Karnataka — 560077", style_table_cell)],
        [Paragraph("<b>Branch Office (Assam)</b>", style_table_cell_bold), Paragraph("No. 59, First Floor, Nayanpur Road, Ganeshguri, Guwahati, Kamrup Metropolitan, Assam — 781006", style_table_cell)]
    ]
    t_c3 = Table(c3_data, colWidths=[140 * pt, USABLE_WIDTH - 140 * pt])
    t_c3.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_c3)
    elements.append(Spacer(1, 6 * pt))

    elements.append(Paragraph("4. Leadership & Key Contacts", style_h1))
    c4_data = [
        [Paragraph("<b>Key Contact Person</b>", style_table_cell_bold), Paragraph("Ethesham Hussain Hashmi (Director, M.Sc., Ph.D.) | Email: admin@globizhub.com | Phone: +91 9401317482 / +91 9585123786", style_table_cell)],
        [Paragraph("<b>Executive Leadership</b>", style_table_cell_bold), Paragraph("Mashuda Manjur (Director, M.Sc.) | Email: mashuda.manjur@globizhub.com | Phone: +91 9940131230", style_table_cell)],
        [Paragraph("<b>Corporate Email</b>", style_table_cell_bold), Paragraph("admin@globizhub.com", style_table_cell)]
    ]
    t_c4 = Table(c4_data, colWidths=[130 * pt, USABLE_WIDTH - 130 * pt])
    t_c4.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_c4)
    elements.append(Spacer(1, 8 * pt))

    elements.append(Paragraph("5. Problem Statement", style_h1))
    elements.append(Paragraph(
        "Administrative governance in Assam is operationalised through thousands of gazette notifications, service rules, executive guidelines, and office memoranda across multiple nodal departments — <b>Administrative Reforms & Training (ARTPS)</b>, <b>Assam Administrative Staff College (AASC)</b>, <b>Department of Science & Technology (DST)</b>, <b>Pension & Public Grievances Department</b>, and <b>Assam State Space Application Centre (ASSAC)</b>. While these statutory rules form the backbone of legal administration, an acute operational gap exists between legislative intent, administrative disposal, and citizen service delivery:",
        style_body
    ))
    elements.append(Paragraph(
        "<b>1. For Department Desk Officers & Secretariat Branches:</b> Official rules, amendments, and executive circulars reside scattered across scanned historical PDF archives, legacy paper records, and disparate departmental desks. Desk officers spend hours manually searching for prevailing clauses and verifying whether an earlier rule has been superseded by a subsequent circular, leading to file pendency and procedural delays.",
        style_body
    ))

    elements.append(PageBreak())

    # ==========================================
    # PAGE 3: PROBLEM STATEMENT (P2), SOLUTION OVERVIEW & ARCH (P1)
    # ==========================================
    prob_p2 = [
        "<b>2. For State Administrators & Civil Service Training (AASC):</b> When inducting and training Assam Civil Services (ACS) and departmental personnel, curricula rely on static digests that quickly fall out of sync with real-time statutory amendments. Supervisory authorities lack a centralized, searchable intelligence platform to monitor knowledge utilization and ensure uniformity across departments.",
        "<b>3. For Technical & Spatial Governance (DST & ASSAC):</b> Complex technical guidelines for remote sensing, geospatial land demarcation, and digital infrastructure require strict adherence to statutory specifications. Non-technical officers frequently struggle to locate and interpret specialized norms without inter-departmental referrals.",
        "<b>4. For Retiring Employees & Public Pensioners:</b> Retiring government servants and citizens face significant bureaucratic friction understanding pension eligibility, qualifying service calculations, and requisite forms (e.g., Form 7, No Demand Certificates) under the <i>Assam Services (Pension) Rules 1969</i>, often resulting in avoidable grievances.",
        "<b>5. The Unacceptable Risk of Generic AI in Governance:</b> Standard commercial Large Language Models (LLMs) hallucinate plausible-sounding legal clauses, invent nonexistent government circulars, and cannot provide byte-accurate evidence citations. In public administration and statutory law, unverified synthetic text creates severe legal liability and compromises public trust."
    ]
    for p in prob_p2:
        elements.append(Paragraph(p, style_body))

    elements.append(Spacer(1, 6 * pt))
    elements.append(Paragraph("6. Solution Overview", style_h1))
    elements.append(Paragraph(
        "We present <b>Trusted Government Knowledge, Rules & Document Assistant (VidhiAI / NESFIC-D-36)</b> — a sovereign, deep-tech GovTech intelligence platform engineered specifically for the Government of Assam. The platform transitions administrative knowledge management from fragmented manual paper-search to continuous, verifiable, zero-hallucination operational intelligence. The platform comprises six interconnected operational layers:",
        style_body
    ))

    sol_layers = [
        "<b>1. Dual-Layer 300 DPI OCR & Ingestion Pipeline:</b> High-throughput document processor featuring PIL/OpenCV-based adaptive contrast enhancement, skew correction, and dual-layer layout analysis. Extracts text layers from both clean digital gazettes and degraded historical scanned circulars, with dedicated support for English and Assamese statutory fonts.",
        "<b>2. Structural Chunking & Statutory Rule Parsing Layer:</b> Custom algorithmic chunker that detects statutory section boundaries (e.g., <i>Rule 41(2)</i>, <i>Section 9(1)</i>, <i>Clause 1.19</i>) and consolidates structured lists, preventing broken clauses and preserving legal context.",
        "<b>3. Deterministic Retrieval & Substantive Quote Extractor:</b> Hybrid search engine pairing BM25 keyword matching with dense semantic embeddings. A substantive sentence extractor isolates statutory operative sentences (containing verbs such as <i>mandates</i>, <i>shall</i>, <i>entitles</i>, <i>capped</i>) to eliminate decorative boilerplate.",
        "<b>4. Zero-Hallucination Strict Verifier Guardrail:</b> Mathematical character-level NFKC string grounding validator. Every statement generated by the assistant is cross-referenced against the verbatim text layer of the cited gazette. If a claim lacks exact substring grounding, the response is rejected with a safe failure message.",
        "<b>5. Audit-Ready Secretariat Green-Sheet Noting Generator:</b> Automatically formats statutory answers into standard Assam Secretariat Manual notings—complete with Reference File Number, Statutory Rule Citation, Verification Stamp, and Action Recommendation.",
        "<b>6. SHA-256 Cryptographic Provenance Ledger:</b> Every ingested document chunk and every issued administrative noting is timestamped and cryptographically hashed, guaranteeing immutable traceability for vigilance audits and administrative inquiries."
    ]
    for s in sol_layers:
        elements.append(Paragraph(s, style_body))

    elements.append(Spacer(1, 6 * pt))
    elements.append(Paragraph("7. Core Architectural Capabilities", style_h1))
    elements.append(Paragraph(
        "The platform introduces the following deep-tech architectural innovations tailored to Assam's administrative framework:",
        style_body
    ))
    elements.append(Paragraph(
        "<b>1. Character-Level NFKC String Grounding (Zero Hallucination Guarantee):</b> The verifier normalizes unicode characters and verifies that every statutory citation is an exact, byte-level substring of the official gazette. Extrapolations are strictly prohibited.",
        style_body
    ))

    elements.append(PageBreak())

    # ==========================================
    # PAGE 4: ARCHITECTURE (P2) & TECHNOLOGY STACK
    # ==========================================
    arch_p2 = [
        "<b>2. Departmental Context Boundary & Role-Based Access Control (RBAC):</b> Server-side enforcement provides dedicated workspaces for STATE_ADMIN (full statewide visibility), DEPT_OFFICER (department-scoped with instant noting generation), and CITIZEN (plain-language eligibility summaries with transparent document page viewers).",
        "<b>3. Safe Refusal & Audit Escalation Protocol:</b> When queried on matters outside the active statutory index, the platform refuses to synthesize ungrounded speculation, instead logging the query for departmental nodal officer review.",
        "<b>4. Bilingual Script Ingestion Readiness:</b> Foundational tokenization pipeline architected for seamless processing of Assamese script (অসমীয়া লিপি) alongside English administrative gazettes.",
        "<b>5. Sovereign On-Premise Deployability:</b> Designed for deployment within the Assam State Data Centre (SDC) or MeitY-empanelled sovereign cloud infrastructure, ensuring confidential government files remain within state-controlled perimeters."
    ]
    for a in arch_p2:
        elements.append(Paragraph(a, style_body))

    elements.append(Spacer(1, 6 * pt))
    elements.append(Paragraph("8. Technology Stack & Implementation Status", style_h1))
    elements.append(Paragraph("<b>Implemented Prototype Features</b>", style_h2))

    tech_impl_data = [
        [
            Paragraph("<b>Frontend Framework</b>", style_table_cell_bold),
            Paragraph("Next.js 16 (App Router, Turbopack), React 19, TypeScript 5, Vanilla CSS Responsive Design System, Ant Design 6.x, Lucide React icons, Framer Motion", style_table_cell)
        ],
        [
            Paragraph("<b>Accessibility & UI</b>", style_table_cell_bold),
            Paragraph("GIGW 3.0 compliant, Screen Reader ARIA landmarks, A-/A+ font resizer, SpeechSynthesis audio narrator (Hear), Bilingual language selector (EN/AS)", style_table_cell)
        ],
        [
            Paragraph("<b>Backend & API</b>", style_table_cell_bold),
            Paragraph("FastAPI / Python 3.9+ asynchronous REST API, SQLite3 relational metadata index, PyMuPDF (fitz) dual-layer OCR extraction engine", style_table_cell)
        ],
        [
            Paragraph("<b>Grounding & RAG Engine</b>", style_table_cell_bold),
            Paragraph("Hybrid BM25 + dense vector indexing, deterministic substantive quote extractor, character-level NFKC verifier engine", style_table_cell)
        ],
        [
            Paragraph("<b>Access Control & RBAC</b>", style_table_cell_bold),
            Paragraph("Role-scoped session handling (Super Admin, Desk Officer, Citizen), scoped document filtering via dept_scope", style_table_cell)
        ],
        [
            Paragraph("<b>Audit Ledger & Export</b>", style_table_cell_bold),
            Paragraph("SHA-256 cryptographic document chunk hashing, immutable noting timestamps, CSV telemetry export", style_table_cell)
        ]
    ]

    t_tech_impl = Table(tech_impl_data, colWidths=[130 * pt, USABLE_WIDTH - 130 * pt])
    t_tech_impl.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_tech_impl)
    elements.append(Spacer(1, 8 * pt))

    elements.append(Paragraph("<b>Proposed Production Architecture</b>", style_h2))
    tech_prod_data = [
        [
            Paragraph("<b>Direct Gazette Ingestion</b>", style_table_cell_bold),
            Paragraph("Automated sync connector with the Assam Government e-Gazette repository and departmental MIS portals", style_table_cell)
        ],
        [
            Paragraph("<b>Enterprise IAM</b>", style_table_cell_bold),
            Paragraph("Integration with official National/State Single Sign-On (Jan Parichay / e-Pramaan) with Multi-Factor Authentication (MFA)", style_table_cell)
        ],
        [
            Paragraph("<b>Sovereign Deep Tech SLM</b>", style_table_cell_bold),
            Paragraph("Fine-tuned 7B/14B parameter Indian Legal Small Language Model deployed on dedicated SDC GPU nodes (vLLM / TensorRT-LLM)", style_table_cell)
        ],
        [
            Paragraph("<b>Bilingual Assamese OCR</b>", style_table_cell_bold),
            Paragraph("Custom vision-language OCR pipeline fine-tuned on historical Assam Government font ligatures and stamp marks", style_table_cell)
        ],
        [
            Paragraph("<b>Security & Compliance</b>", style_table_cell_bold),
            Paragraph("Full CERT-In empanelled VAPT auditing, STQC GIGW 3.0 compliance certification, and DPDP Act 2023 adherence", style_table_cell)
        ],
        [
            Paragraph("<b>Workflow Automation</b>", style_table_cell_bold),
            Paragraph("Integration with e-Office (NIC) for direct insertion of AI-generated verified green-sheet notings into official files", style_table_cell)
        ]
    ]

    t_tech_prod = Table(tech_prod_data, colWidths=[130 * pt, USABLE_WIDTH - 130 * pt])
    t_tech_prod.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_tech_prod)

    elements.append(PageBreak())

    # ==========================================
    # PAGE 5: CURRENT STAGE & DEMONSTRATION & STAKEHOLDERS
    # ==========================================
    elements.append(Paragraph("9. Current Stage & Demonstration", style_h1))
    elements.append(Paragraph(
        "<b>Functional MVP Prototype · Demonstration-Ready.</b> A working full-stack prototype is deployed and verified. "
        "The system indexes official Assam gazette collections across Pension Rules 1969, ARTPS Act 2012, Mission Basundhara guidelines, "
        "and DST circulars, delivering sub-second verbatim grounding with zero hallucination. The prototype includes bilingual UI navigation, "
        "desk-scoped filtering, dual-layer OCR text layer inspection, automated Secretariat green-sheet noting generation, "
        "speech synthesis accessibility, and continuous SHA-256 cryptographic audit logging.",
        style_body
    ))
    elements.append(Paragraph("<b>Demonstration URL:</b> https://nesfic-d-36.vercel.app <i>(Demonstration environment)</i>", style_body))
    elements.append(Paragraph("<b>Source Code Repository:</b> https://github.com/anupam-codespace/NESFIC-D-36.git", style_body))
    elements.append(Spacer(1, 4 * pt))

    feat_matrix_data = [
        [
            Paragraph("<b>Feature</b>", style_table_header),
            Paragraph("<b>Status</b>", style_table_header),
            Paragraph("<b>Production Scope</b>", style_table_header)
        ],
        [
            Paragraph("Bilingual Government Header & Banner", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Integration with State portal master navigation", style_table_cell)
        ],
        [
            Paragraph("Accessibility Suite (TTS Audio & Font Scaler)", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("STQC certified WCAG 2.1 AAA compliance", style_table_cell)
        ],
        [
            Paragraph("Multi-Department Gazette Ingestion", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Automated e-Gazette webhook listener", style_table_cell)
        ],
        [
            Paragraph("Dual-Layer 300 DPI OCR Extraction", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Distributed GPU-accelerated OCR workers", style_table_cell)
        ],
        [
            Paragraph("Character-Level Verifier Guardrail", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Formally verified mathematical proof engine", style_table_cell)
        ],
        [
            Paragraph("Secretariat Green-Sheet Noting Generator", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Direct integration with NIC e-Office file dispatch", style_table_cell)
        ],
        [
            Paragraph("Role-Based Desk Isolation (Admin/Officer/Citizen)", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Jan Parichay enterprise SSO integration", style_table_cell)
        ],
        [
            Paragraph("Live Telemetry & Performance Benchmarks", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Real-time Prometheus/Grafana monitoring", style_table_cell)
        ],
        [
            Paragraph("SHA-256 Cryptographic Audit Ledger", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Hyperledger / State Blockchain notarization", style_table_cell)
        ],
        [
            Paragraph("Public Transparency & Citizen Inquiry", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Sewa Setu / RTPS citizen service integration", style_table_cell)
        ]
    ]

    t_feat = Table(feat_matrix_data, colWidths=[145 * pt, 75 * pt, USABLE_WIDTH - 220 * pt])
    t_feat.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_BG_ALT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.8 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.8 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('LINEBELOW', (0, 0), (-1, 0), 1.0, PRIMARY_GREEN),
    ]))
    elements.append(t_feat)
    elements.append(Spacer(1, 8 * pt))

    elements.append(Paragraph("10. Stakeholder & Context Analysis", style_h1))
    elements.append(Paragraph("<b>Target Stakeholders</b>", style_h2))
    stk_points = [
        "<b>1. Primary Regulatory & Secretariat Bodies (B2G):</b> Administrative Reforms Department (statutory compliance), Assam Administrative Staff College (ACS civil service training), Department of Science & Technology & ASSAC (geospatial/technical guidelines), and Pension & Public Grievances Department (pension disposal).",
        "<b>2. Internal Administrative Cadre:</b> Joint Secretaries, Deputy Secretaries, Under Secretaries, Section Officers, and Senior Assistants across line departments responsible for file drafting and statutory approvals.",
        "<b>3. Public Beneficiaries & Retiring Officers:</b> Retiring government employees, pensioners, and citizens requiring clear, authoritative interpretations of Assam service laws and entitlement rules without intermediary exploitation."
    ]
    for sp in stk_points:
        elements.append(Paragraph(sp, style_body))

    elements.append(Paragraph("<b>Contextual Differentiation</b>", style_h2))
    elements.append(Paragraph(
        "Existing monitoring and review processes rely on static manual digests and unverified paper registries. Generic ticketing and commercial chat platforms lack awareness of Assam's statutory workflows, secretariat green-sheet noting hierarchies, and departmental jurisdictions. VidhiAI is purpose-built for Assam: it models the exact statutory relationships between principal acts and amending notifications, ensures 100% evidence-grounded answers, and formats results directly into the green-sheet notings officers utilize daily.",
        style_body
    ))

    elements.append(PageBreak())

    # ==========================================
    # PAGE 6: IP & FUNDING / STAGED MILESTONES (₹40 LAKHS)
    # ==========================================
    elements.append(Paragraph("11. Intellectual Property & Licensing", style_h1))
    ip_points = [
        "<b>• IP Status:</b> Proprietary GovTech software and algorithmic architecture developed specifically for the challenge. Full demonstration source code provided for state evaluation.",
        "<b>• Patent Strategy:</b> Provisional domestic patent planned covering (1) <i>Method and System for Deterministic Zero-Hallucination Retrieval and Character-Level NFKC String Grounding in Administrative Legal Documents</i>; and (2) <i>Automated Statutory Amendment Reconciliation and Cryptographic Provenance Tracking for Secretariat Decisions</i>.",
        "<b>• Deployment Model:</b> Proposed as an indigenous SaaS / On-Premise GovTech model hosted on the Assam State Data Centre (SDC) or MeitY-empanelled sovereign cloud, with complete data isolation for air-gapped secretariats."
    ]
    for ip in ip_points:
        elements.append(Paragraph(ip, style_body))

    elements.append(Spacer(1, 8 * pt))
    elements.append(Paragraph("12. Funding & Staged Milestones", style_h1))

    # Grant Directive callout matching manager's instruction
    grant_html = (
        "<b>Requested Grant: ₹40,00,000 (Rupees Forty Lakhs) — NESFIC 2026 Deep-Tech Grant</b><br/>"
        "<i>Allocation Model: Track A (Core MVP & Enterprise Deployment): ₹20,00,000 | "
        "Track B (Deep-Tech & Generative AI Research): ₹20,00,000</i>"
    )
    grant_banner_table = Table([[Paragraph(grant_html, style_grant_banner)]], colWidths=[USABLE_WIDTH])
    grant_banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#ecfdf5')),
        ('BOX', (0, 0), (-1, -1), 0.75, ACCENT_GREEN),
        ('TOPPADDING', (0, 0), (-1, -1), 4 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 8 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8 * pt),
    ]))
    elements.append(grant_banner_table)
    elements.append(Spacer(1, 6 * pt))

    # Milestones Table (9 Milestones matching ₹40 Lakhs exactly)
    ms_headers = [
        Paragraph("<b>#</b>", style_table_header),
        Paragraph("<b>Milestone & Work Package</b>", style_table_header),
        Paragraph("<b>Track</b>", style_table_header),
        Paragraph("<b>Budget</b>", style_table_header),
        Paragraph("<b>Share</b>", style_table_header),
        Paragraph("<b>Prerequisites</b>", style_table_header),
        Paragraph("<b>Key Deliverables</b>", style_table_header)
    ]

    ms_rows = [
        [
            Paragraph("1", style_table_cell_bold),
            Paragraph("Data & Gazette Ontology Ingestion", style_table_cell_bold),
            Paragraph("Track A", style_table_cell),
            Paragraph("₹3,60,000", style_table_cell_bold),
            Paragraph("9.0%", style_table_cell),
            Paragraph("Gazette archives from AASC, Pension, ARTPS, DST", style_table_cell),
            Paragraph("Assam statutory data dictionary; structured JSON schema; multi-dept pipeline", style_table_cell)
        ],
        [
            Paragraph("2", style_table_cell_bold),
            Paragraph("Production Ingestion & SDC Connector", style_table_cell_bold),
            Paragraph("Track A", style_table_cell),
            Paragraph("₹5,20,000", style_table_cell_bold),
            Paragraph("13.0%", style_table_cell),
            Paragraph("SDC sandbox access; API permissions", style_table_cell),
            Paragraph("Production OCR connector with automated retry logic, queue management & reconciliation", style_table_cell)
        ],
        [
            Paragraph("3", style_table_cell_bold),
            Paragraph("Security, VAPT & GIGW 3.0 Hardening", style_table_cell_bold),
            Paragraph("Track A", style_table_cell),
            Paragraph("₹3,80,000", style_table_cell_bold),
            Paragraph("9.5%", style_table_cell),
            Paragraph("MeitY-compliant staging cloud", style_table_cell),
            Paragraph("CERT-In empanelled VAPT audit clearance; GIGW 3.0 accessibility verification; DPDP dossier", style_table_cell)
        ],
        [
            Paragraph("4", style_table_cell_bold),
            Paragraph("Multi-Department Secretariat Pilot", style_table_cell_bold),
            Paragraph("Track A", style_table_cell),
            Paragraph("₹5,00,000", style_table_cell_bold),
            Paragraph("12.5%", style_table_cell),
            Paragraph("Pilot clearance (Admin Reforms, AASC, Pension)", style_table_cell),
            Paragraph("60-day live pilot across 3 nodal departments; 100+ officers onboarded; validation report", style_table_cell)
        ],
        [
            Paragraph("5", style_table_cell_bold),
            Paragraph("Scale Readiness & Rollout Blueprint", style_table_cell_bold),
            Paragraph("Track A", style_table_cell),
            Paragraph("₹2,40,000", style_table_cell_bold),
            Paragraph("6.0%", style_table_cell),
            Paragraph("Pilot telemetry data; legal review", style_table_cell),
            Paragraph("Statewide rollout architectural blueprint; SDC bare-metal scripts; officer manual", style_table_cell)
        ],
        [
            Paragraph("6", style_table_cell_bold),
            Paragraph("Bilingual Assamese OCR Pretraining", style_table_cell_bold),
            Paragraph("Track B<br/>(Deep Tech)", style_table_cell),
            Paragraph("₹5,50,000", style_table_cell_bold),
            Paragraph("13.75%", style_table_cell),
            Paragraph("Historical Assamese gazettes & font corpuses", style_table_cell),
            Paragraph("Custom OCR fine-tuned on Assamese ligatures; 98%+ character benchmark; bilingual chunker", style_table_cell)
        ],
        [
            Paragraph("7", style_table_cell_bold),
            Paragraph("Sovereign Legal SLM Fine-Tuning", style_table_cell_bold),
            Paragraph("Track B<br/>(Deep Tech)", style_table_cell),
            Paragraph("₹6,00,000", style_table_cell_bold),
            Paragraph("15.0%", style_table_cell),
            Paragraph("Secretariat Manual precedents & annotated notings", style_table_cell),
            Paragraph("Domain-adapted 7B/14B parameter SLM fine-tuned for formal Secretariat noting synthesis", style_table_cell)
        ],
        [
            Paragraph("8", style_table_cell_bold),
            Paragraph("Automated Statutory Conflict Graph", style_table_cell_bold),
            Paragraph("Track B<br/>(Deep Tech)", style_table_cell),
            Paragraph("₹4,50,000", style_table_cell_bold),
            Paragraph("11.25%", style_table_cell),
            Paragraph("Amendment history of Assam Service Rules", style_table_cell),
            Paragraph("Directed Acyclic Graph (DAG) detecting repealed clauses, active circulars & conflicts", style_table_cell)
        ],
        [
            Paragraph("9", style_table_cell_bold),
            Paragraph("Blockchain Provenance & Air-Gap Build", style_table_cell_bold),
            Paragraph("Track B<br/>(Deep Tech)", style_table_cell),
            Paragraph("₹4,00,000", style_table_cell_bold),
            Paragraph("10.0%", style_table_cell),
            Paragraph("Production container security clearance", style_table_cell),
            Paragraph("SHA-256 tamper-evident provenance ledger; immutable audit export; air-gapped installer", style_table_cell)
        ],
        [
            Paragraph("", style_table_cell_bold),
            Paragraph("<b>Total Grant Request (Track A + Track B)</b>", style_table_cell_bold),
            Paragraph("<b>Full Scope</b>", style_table_cell_bold),
            Paragraph("<b>₹40,00,000</b>", style_table_cell_bold),
            Paragraph("<b>100%</b>", style_table_cell_bold),
            Paragraph("<b>Complete 12-Month Roadmap</b>", style_table_cell_bold),
            Paragraph("<b>Demonstration-Ready, Scalable GovTech AI for Assam</b>", style_table_cell_bold)
        ]
    ]

    t_ms_data = [ms_headers] + ms_rows
    col_w = [16 * pt, 100 * pt, 48 * pt, 52 * pt, 34 * pt, 105 * pt, USABLE_WIDTH - (16+100+48+52+34+105) * pt]
    t_ms = Table(t_ms_data, colWidths=col_w)
    t_ms.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_BG_ALT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 2.5 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2.5 * pt),
        ('LINEBELOW', (0, 0), (-1, -2), 0.5, BORDER_COLOR),
        ('LINEBELOW', (0, 0), (-1, 0), 1.0, PRIMARY_GREEN),
        # Highlight total row in yellow
        ('BACKGROUND', (0, -1), (-1, -1), TOTAL_YELLOW),
        ('LINEABOVE', (0, -1), (-1, -1), 1.0, PRIMARY_GREEN),
        ('LINEBELOW', (0, -1), (-1, -1), 1.0, PRIMARY_GREEN),
        ('TOPPADDING', (0, -1), (-1, -1), 3.5 * pt),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 3.5 * pt),
    ]))
    elements.append(t_ms)

    elements.append(PageBreak())

    # ==========================================
    # PAGE 7: PROJECTED IMPACT & ASSAM STARTUP POLICY ALIGNMENT
    # ==========================================
    elements.append(Paragraph("13. Projected Impact & Evaluation", style_h1))
    elements.append(Paragraph("<i>Targeted estimates based on pilot benchmarks.</i>", style_body))
    elements.append(Paragraph("<b>Administrative Impacts</b>", style_h2))

    admin_impacts = [
        "<b>1. Accelerated Evidence Retrieval:</b> Reduces evidence retrieval and rule cross-referencing from an average of 4–6 hours per file to under 2 minutes, dramatically accelerating Secretariat decision-making.",
        "<b>2. Proactive Operational Triage:</b> Surfaces operative clauses, qualifying service rules, and entitlement ceilings within seconds of query submission — eliminating the lag between file intake and supervisory disposal.",
        "<b>3. Objective Merit Recognition:</b> Continuous audit-logged noting records establish an objective basis for recognizing high-performing desk officers, section officers, and departments.",
        "<b>4. Citizen-Centric Transparency:</b> Plain-language entitlement summaries and transparent source document inspections restore citizen trust in government pension and public service delivery.",
        "<b>5. Zero Legal Liability from Hallucinations:</b> Character-level string verifier guarantees that citations and rules cited in secretariat green notings are 100% true to official gazettes."
    ]
    for ai in admin_impacts:
        elements.append(Paragraph(ai, style_body))

    elements.append(Paragraph("<b>Employment & Capacity Targets</b>", style_h2))
    emp_points = [
        "<b>• Direct Technical Roles:</b> 8–12 engineering, AI/ML research, legal ontology, and GIS data roles based in Assam at the Globizhub Guwahati branch office.",
        "<b>• Ecosystem Support Roles:</b> 30–50 indirect technical and training support positions across districts (nodal officers, digitization operators, field trainers)."
    ]
    for ep in emp_points:
        elements.append(Paragraph(ep, style_body))

    elements.append(Spacer(1, 6 * pt))
    elements.append(Paragraph("14. Alignment with Assam Startup Policy 2025–2030", style_h1))
    elements.append(Paragraph("<b>Primary Category:</b> Category B — IT, ITeS & Artificial Intelligence (Deep Tech Specialization)", style_body_bold))
    elements.append(Paragraph("The proposal aligns with the \"Innovate Assam 2030\" key strategic focus areas:", style_body))

    align_points = [
        "<b>1. Domestic GovTech Innovation:</b> Indigenous technology built for Government of Assam needs, addressing the specific statutory workflows of Administrative Reforms, AASC, DST, Pension & PG, and ASSAC.",
        "<b>2. Data Governance:</b> High-performance web tools, zero-hallucination verification algorithms, RBAC, and audit trails engineered by regional talent based at the Guwahati branch office.",
        "<b>3. Citizen-Centric Governance:</b> Supports the statutory objectives of transparent pension processing, entitlement verification, and grievance redressal under the Assam Right to Public Services Act (ARTPS).",
        "<b>4. Employment Generation:</b> Direct and indirect technical roles based in Assam, with specialized AI training programs for secretariat staff and departmental nodal officers."
    ]
    for ap in align_points:
        elements.append(Paragraph(ap, style_body))

    elements.append(Spacer(1, 10 * pt))

    # Formal Submission / Sign-off block
    sign_data = [
        [
            Paragraph("<b>Submitted on behalf of:</b><br/>Globizhub India Private Limited<br/>Branch Office: No. 59, First Floor, Nayanpur Road,<br/>Ganeshguri, Guwahati, Kamrup Metro, Assam — 781006", style_table_cell),
            Paragraph("<b>Authorized Signatory & Seal:</b><br/><br/>____________________________________<br/>Ethesham Hussain Hashmi, Ph.D. / Mashuda Manjur<br/>Directors, Globizhub India Private Limited", style_table_cell)
        ]
    ]
    sign_table = Table(sign_data, colWidths=[240 * pt, USABLE_WIDTH - 240 * pt])
    sign_table.setStyle(TableStyle([
        ('TOPPADDING', (0, 0), (-1, -1), 6 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 6 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6 * pt),
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(sign_table)

    # Build the document using NumberedCanvas
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Successfully generated proposal PDF: {output_path}")

if __name__ == '__main__':
    out_file = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'docs',
        'NESFIC_D36_Project_Proposal_Technical_Report.pdf'
    )
    build_pdf(out_file)
