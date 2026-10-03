#!/usr/bin/env python3
"""
NESFIC 2026 - Problem Statement 46 (NESFIC-D-36)
Project Proposal & Technical Report PDF Generator
Produces a submission-ready, print-perfect 7-PAGE PDF matching the exact visual style,
typography, dark green header banner, 5-milestone structure, and page flow of teammate submissions.
"""

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm, mm
pt = 1
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Page dimensions for A4
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 44 * pt  # ~0.61 inch margins matching the reference PDF exactly
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
        self.drawString(MARGIN, 22 * pt, footer_text)
        
        # Right footer
        page_str = f"Page {page_num}"
        self.drawRightString(PAGE_WIDTH - MARGIN, 22 * pt, page_str)
        
        # Thin divider line above footer
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.5)
        self.line(MARGIN, 32 * pt, PAGE_WIDTH - MARGIN, 32 * pt)
        
        # On Page 1, draw the top dark green header banner box
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
            dept_text = "Transformation & Innovations · Administrative Reforms · AASC · DST · Pension · ASSAC"
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
        bottomMargin=42 * pt
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
        fontSize=10,
        leading=14.5,
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
        fontSize=8.5,
        leading=12,
        textColor=BODY_TEXT,
        spaceAfter=6
    )

    style_body_bold = ParagraphStyle(
        'BodyBoldCustom',
        fontName=FONT_BOLD,
        fontSize=8.5,
        leading=12,
        textColor=DARK_TEXT,
        spaceAfter=6
    )

    style_disclaimer = ParagraphStyle(
        'DisclaimerText',
        fontName=FONT_ITALIC,
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor('#475569'),
        spaceBefore=4,
        spaceAfter=4
    )

    style_table_header = ParagraphStyle(
        'TableHeader',
        fontName=FONT_BOLD,
        fontSize=7.8,
        leading=10.5,
        textColor=DARK_TEXT
    )

    style_table_cell = ParagraphStyle(
        'TableCell',
        fontName=FONT_REGULAR,
        fontSize=7.8,
        leading=10.5,
        textColor=BODY_TEXT
    )

    style_table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName=FONT_BOLD,
        fontSize=7.8,
        leading=10.5,
        textColor=DARK_TEXT
    )

    elements = []

    # ==========================================
    # PAGE 1: COVER & EXECUTIVE METADATA
    # ==========================================
    elements.append(Spacer(1, 10 * pt))
    elements.append(Paragraph("Project Proposal & Technical Report", style_label))
    elements.append(Paragraph("Trusted Government Knowledge, Rules & Document Assistant", style_title))
    elements.append(Paragraph(
        "A Sovereign Administrative Intelligence Platform Delivering Verbatim Statutory Grounding, Multi-Department Rule Synthesis, and Decision-Support for the Government of Assam",
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
            Paragraph("Functional Deep-Tech Prototype · Production-Ready", style_table_cell)
        ],
        [
            Paragraph("<b>Applicant / Project Lead</b>", style_table_cell_bold),
            Paragraph("NESFIC-D-36 Innovation Initiative", style_table_cell)
        ],
        [
            Paragraph("<b>Date</b>", style_table_cell_bold),
            Paragraph("October 2026", style_table_cell)
        ]
    ]

    meta_table = Table(meta_data, colWidths=[130 * pt, USABLE_WIDTH - 130 * pt])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5.5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5.5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(meta_table)

    elements.append(Spacer(1, 20 * pt))

    # Notice & Disclaimer Box
    disclaimer_html = (
        "<b>Notice & Disclaimer:</b> <i>This document represents an independent technical proposal and "
        "functional prototype submitted in response to challenge problem statement PS No. 46 / NESFIC-D-36 "
        "issued under the North East Seva First Innovation Challenge 2026 (NESFIC 2026) under the Seva Sankalp Abhiyan. "
        "It is designed to demonstrate technical feasibility, deterministic statutory grounding, "
        "and administrative decision-support workflows. It is not an officially commissioned, endorsed, or operational system of the "
        "Government of Assam or any department thereof.</i>"
    )
    disc_data = [[Paragraph(disclaimer_html, style_disclaimer)]]
    disc_table = Table(disc_data, colWidths=[USABLE_WIDTH])
    disc_table.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0, 0), (-1, -1), 8 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 6 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6 * pt),
    ]))
    elements.append(disc_table)

    elements.append(PageBreak())

    # ==========================================
    # PAGE 2: PROJECT OVERVIEW & GOVERNANCE SCOPE
    # ==========================================
    elements.append(Paragraph("1. Project Overview & Challenge Alignment", style_h1))
    c1_data = [
        [Paragraph("<b>Project Title</b>", style_table_cell_bold), Paragraph("VidhiAI — Trusted Government Knowledge, Rules & Document Assistant", style_table_cell)],
        [Paragraph("<b>Problem Statement</b>", style_table_cell_bold), Paragraph("PS No. 46 · NESFIC-D-36 (Government of Assam)", style_table_cell)],
        [Paragraph("<b>National Challenge</b>", style_table_cell_bold), Paragraph("North East Seva First Innovation Challenge 2026 (NESFIC 2026) under Seva Sankalp Abhiyan", style_table_cell)],
        [Paragraph("<b>Production Link</b>", style_table_cell_bold), Paragraph("https://nesfic-d-36.vercel.app", style_table_cell)]
    ]
    t_c1 = Table(c1_data, colWidths=[140 * pt, USABLE_WIDTH - 140 * pt])
    t_c1.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_c1)
    elements.append(Spacer(1, 10 * pt))

    elements.append(Paragraph("2. Innovation Track & Maturity Status", style_h1))
    c2_data = [
        [Paragraph("<b>Challenge Grant Track</b>", style_table_cell_bold), Paragraph("Deep Tech Prototype Grant (Category B — IT, ITeS & Artificial Intelligence)", style_table_cell)],
        [Paragraph("<b>Current Project Status</b>", style_table_cell_bold), Paragraph("Functional Deep-Tech Prototype · Production & Demonstration-Ready to date", style_table_cell)],
        [Paragraph("<b>Statutory Grounding Proof</b>", style_table_cell_bold), Paragraph("100% Deterministic NFKC String Grounding (Zero Speculation Engine)", style_table_cell)]
    ]
    t_c2 = Table(c2_data, colWidths=[150 * pt, USABLE_WIDTH - 150 * pt])
    t_c2.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_c2)
    elements.append(Spacer(1, 10 * pt))

    elements.append(Paragraph("3. Operational Deployment & Target Architecture", style_h1))
    c3_data = [
        [Paragraph("<b>Sovereign Hosting Perimeter</b>", style_table_cell_bold), Paragraph("Assam State Data Centre (SDC) / MeitY-Empanelled Sovereign Cloud", style_table_cell)],
        [Paragraph("<b>Administrative Perimeter</b>", style_table_cell_bold), Paragraph("Assam Secretariat, Line Department Desks, Directorate Offices, District Commissionerates", style_table_cell)],
        [Paragraph("<b>Data Security & Isolation</b>", style_table_cell_bold), Paragraph("100% On-premise State data perimeter; air-gapped secretariat compatibility", style_table_cell)]
    ]
    t_c3 = Table(c3_data, colWidths=[150 * pt, USABLE_WIDTH - 150 * pt])
    t_c3.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_c3)
    elements.append(Spacer(1, 10 * pt))

    elements.append(Paragraph("4. Participating Departments & Governance Scope", style_h1))
    c4_data = [
        [Paragraph("<b>Nodal Line Departments</b>", style_table_cell_bold), Paragraph("Administrative Reforms & Training, Assam Administrative Staff College (AASC), Department of Science & Technology (DST), Pension & Public Grievances Department, and Assam State Space Application Centre (ASSAC)", style_table_cell)],
        [Paragraph("<b>Source Code Repository</b>", style_table_cell_bold), Paragraph("https://github.com/anupam-codespace/NESFIC-D-36.git", style_table_cell)],
        [Paragraph("<b>Primary Functional Scope</b>", style_table_cell_bold), Paragraph("Multi-department gazette ingestion, regulatory scrutiny, verbatim statutory citations, and automated secretariat green-sheet notings", style_table_cell)]
    ]
    t_c4 = Table(c4_data, colWidths=[150 * pt, USABLE_WIDTH - 150 * pt])
    t_c4.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_c4)
    elements.append(Spacer(1, 10 * pt))

    # Innovation Mandate box for Page 2
    corp_mandate_html = (
        "<b>Innovation Mandate & Prototype Objectives:</b> VidhiAI has been engineered as a functional, demonstration-ready "
        "GovTech intelligence prototype to solve critical administrative bottlenecks across the Government of Assam. "
        "The system combines multimodal gazette ingestion, layout segmentation, deterministic statutory grounding, "
        "and automated secretariat file noting generation into a cohesive operational workflow for Assam's civil administration."
    )
    corp_table = Table([[Paragraph(corp_mandate_html, style_table_cell)]], colWidths=[USABLE_WIDTH])
    corp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), TABLE_BG_ALT),
        ('BOX', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 7 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 9 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9 * pt),
    ]))
    elements.append(corp_table)

    # Clean Page Break so Section 5 starts on Page 3
    elements.append(PageBreak())

    # ==========================================
    # PAGE 3: PROBLEM STATEMENT & SOLUTION OVERVIEW
    # ==========================================
    elements.append(Paragraph("5. Problem Statement", style_h1))
    elements.append(Paragraph(
        "Administrative governance in Assam is operationalised through a large portfolio of gazettes, notifications, service rules, executive guidelines, and office memoranda across multiple nodal line departments — <b>Administrative Reforms & Training</b>, <b>Assam Administrative Staff College (AASC)</b>, <b>Department of Science & Technology (DST)</b>, <b>Pension & Public Grievances Department</b>, and <b>Assam State Space Application Centre (ASSAC)</b>. Each department manages critical statutory mandates, qualifying service determinations, and citizen-facing services. Yet an operational gap exists between legislative intent and administrative disposal:",
        style_body
    ))
    elements.append(Paragraph(
        "<b>1. For Department Desk Officers & Secretariat Branches:</b> Official rules, amendments, and executive circulars reside scattered across scanned historical PDF archives, legacy paper records, and disparate departmental desks. Desk officers spend hours manually searching for prevailing clauses and verifying whether an earlier rule has been superseded by a subsequent circular, leading to file pendency and procedural delays.",
        style_body
    ))
    elements.append(Paragraph(
        "<b>2. For State Administrators & Civil Service Training (AASC):</b> When inducting and training Assam Civil Services (ACS) and departmental personnel, curricula rely on static digests that quickly fall out of sync with real-time statutory amendments. Supervisory authorities lack a centralized, searchable intelligence platform to monitor knowledge utilization and ensure uniformity across departments.",
        style_body
    ))
    elements.append(Paragraph(
        "<b>3. For Technical & Spatial Governance (DST & ASSAC):</b> Complex technical guidelines for remote sensing, geospatial land demarcation, and digital infrastructure require strict adherence to statutory specifications. Non-technical officers frequently struggle to locate and interpret specialized norms without inter-departmental referrals.",
        style_body
    ))
    elements.append(Paragraph(
        "<b>4. For Retiring Employees & Public Pensioners:</b> Retiring government servants and citizens face significant bureaucratic friction understanding pension eligibility, qualifying service calculations, and requisite forms (e.g., Form 7, No Demand Certificates) under the <i>Assam Services (Pension) Rules 1969</i>, often resulting in avoidable grievances.",
        style_body
    ))

    elements.append(Spacer(1, 8 * pt))
    elements.append(Paragraph("6. Solution Overview", style_h1))
    elements.append(Paragraph(
        "We present <b>Trusted Government Knowledge, Rules & Document Assistant</b> — a sovereign, deep-tech administrative intelligence platform that transitions administrative knowledge management from periodic manual search to continuous operational intelligence. The platform comprises five interconnected operational layers:",
        style_body
    ))

    sol_layers = [
        "<b>1. Multimodal Document Intelligence & Ingestion Pipeline:</b> High-throughput document processor featuring adaptive contrast enhancement, layout-aware segmentation, and dual-layer analysis. Extracts structured text from both digital gazettes and legacy archives, with bilingual support for Assamese and English administrative fonts.",
        "<b>2. Structural Chunking & Statutory Rule Parsing Layer:</b> Custom algorithmic chunker that detects statutory section boundaries (e.g., <i>Rule 41(2)</i>, <i>Section 9(1)</i>) and consolidates structured lists, preventing broken clauses and preserving legal context.",
        "<b>3. Deterministic Hybrid RAG Engine & Operative Quote Extractor:</b> High-performance retrieval engine pairing BM25 sparse keyword matching with dense semantic embeddings and reciprocal rank fusion. A substantive sentence extractor isolates operative legal provisions to eliminate administrative boilerplate.",
        "<b>4. Strict Character-Level Verifier Guardrail:</b> Mathematical character-level NFKC string grounding validator. Every statement synthesized by the system is cross-referenced against the verbatim text layer of the cited gazette. If a claim lacks exact substring grounding, the response is safely withheld.",
        "<b>5. Secretariat Green-Sheet Noting & Cryptographic Audit Layer:</b> Formats verified statutory answers directly into standard Assam Secretariat Manual notings. Every ingested document chunk and generated noting is timestamped and cryptographically hashed (SHA-256), establishing a continuous audit trail."
    ]
    for s in sol_layers:
        elements.append(Paragraph(s, style_body))

    # Clean Page Break so Section 7 starts on Page 4
    elements.append(PageBreak())

    # ==========================================
    # PAGE 4: CORE ARCHITECTURE & TECHNOLOGY STACK
    # ==========================================
    elements.append(Paragraph("7. Core Architectural Capabilities", style_h1))
    elements.append(Paragraph(
        "The platform introduces the following architectural innovations tailored to Assam's administrative framework:",
        style_body
    ))

    arch_points = [
        "<b>1. Character-Level NFKC String Grounding (Verbatim Accuracy Guarantee):</b> The verifier normalizes unicode characters and verifies that every statutory citation is an exact, byte-level substring of the official gazette. Extrapolations and ungrounded statements are strictly prohibited.",
        "<b>2. Role-Based Access Control with Server-Side Enforcement:</b> Dedicated workspaces for STATE_ADMIN (full statewide visibility), DEPT_OFFICER (department-scoped with instant noting generation), and CITIZEN (plain-language eligibility summaries with transparent document page viewers).",
        "<b>3. Safe Refusal & Administrative Escalation Protocol:</b> When queried on matters outside the active statutory index, the platform refuses to synthesize ungrounded speculation, instead logging the query for departmental nodal officer review.",
        "<b>4. Bilingual Script Ingestion Readiness:</b> Foundational tokenization pipeline architected for seamless processing of Assamese script (Asomiya) alongside English administrative gazettes.",
        "<b>5. Sovereign On-Premise Deployability:</b> Designed for deployment within the Assam State Data Centre (SDC) or MeitY-empanelled sovereign cloud infrastructure, ensuring confidential government files remain within state-controlled perimeters."
    ]
    for a in arch_points:
        elements.append(Paragraph(a, style_body))

    elements.append(Spacer(1, 6 * pt))
    elements.append(Paragraph("8. Technology Stack & Implementation Status", style_h1))
    elements.append(Paragraph("<b>Implemented Prototype Features</b>", style_h2))

    tech_impl_data = [
        [
            Paragraph("<b>Frontend Framework</b>", style_table_cell_bold),
            Paragraph("Next.js 16 (App Router, Turbopack), React 19, TypeScript 5, Tailwind CSS 4, shadcn/ui, Lucide React icons, Framer Motion", style_table_cell)
        ],
        [
            Paragraph("<b>Accessibility & UI</b>", style_table_cell_bold),
            Paragraph("GIGW 3.0 compliant, Screen Reader ARIA landmarks, A-/A+ font resizer, SpeechSynthesis audio narrator (Hear), Bilingual selector (EN/AS)", style_table_cell)
        ],
        [
            Paragraph("<b>Backend & Database</b>", style_table_cell_bold),
            Paragraph("FastAPI / Python 3.9+ asynchronous REST API, SQLite3 relational metadata index, PyMuPDF (fitz) dual-layer document extraction engine", style_table_cell)
        ],
        [
            Paragraph("<b>Retrieval & Grounding</b>", style_table_cell_bold),
            Paragraph("Hybrid sparse-dense retrieval (BM25 + vector embeddings), substantive sentence extractor, character-level NFKC verifier engine", style_table_cell)
        ],
        [
            Paragraph("<b>Access Control</b>", style_table_cell_bold),
            Paragraph("Role-scoped session handling (State Admin, Desk Officer, Citizen), scoped document filtering via dept_scope", style_table_cell)
        ],
        [
            Paragraph("<b>Audit Ledger</b>", style_table_cell_bold),
            Paragraph("SHA-256 cryptographic document chunk hashing, immutable noting timestamps, CSV telemetry export", style_table_cell)
        ]
    ]

    t_tech_impl = Table(tech_impl_data, colWidths=[130 * pt, USABLE_WIDTH - 130 * pt])
    t_tech_impl.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_tech_impl)
    elements.append(Spacer(1, 6 * pt))

    elements.append(Paragraph("<b>Proposed Production Architecture</b>", style_h2))
    tech_prod_data = [
        [
            Paragraph("<b>Advanced Agentic RAG Engine</b>", style_table_cell_bold),
            Paragraph("Multi-stage retrieval combining hybrid BM25 + dense vector embeddings (BGE-Large-EN/Indic), cross-encoder re-ranking, and dynamic chunk synthesis for zero-loss statutory cross-referencing", style_table_cell)
        ],
        [
            Paragraph("<b>Sovereign Deep Tech Legal LLM</b>", style_table_cell_bold),
            Paragraph("Fine-tuned 14B/70B parameter Indian Legal Language Model (Llama-3 / IndicLegal architecture) deployed on dedicated SDC GPU nodes (vLLM / TensorRT-LLM) with strict hallucination-suppression guardrails", style_table_cell)
        ],
        [
            Paragraph("<b>High-Precision Layout-Aware OCR</b>", style_table_cell_bold),
            Paragraph("Multi-pass document intelligence pipeline capable of extracting complex legal tables, stamp seals, gazette margins, and bilingual historical records", style_table_cell)
        ],
        [
            Paragraph("<b>Enterprise IAM & State SSO</b>", style_table_cell_bold),
            Paragraph("Integration with official State SSO (Jan Parichay / e-Pramaan) with Multi-Factor Authentication (MFA)", style_table_cell)
        ],
        [
            Paragraph("<b>Direct e-Gazette Ingestion</b>", style_table_cell_bold),
            Paragraph("Automated sync connector with the Assam Government e-Gazette repository and departmental MIS portals", style_table_cell)
        ],
        [
            Paragraph("<b>NIC e-Office Integration</b>", style_table_cell_bold),
            Paragraph("Automated green-sheet file noting dispatch directly into official e-Office file records", style_table_cell)
        ]
    ]

    t_tech_prod = Table(tech_prod_data, colWidths=[140 * pt, USABLE_WIDTH - 140 * pt])
    t_tech_prod.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4 * pt),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
    ]))
    elements.append(t_tech_prod)

    # Clean Page Break so Section 9 starts on Page 5
    elements.append(PageBreak())

    # ==========================================
    # PAGE 5: CURRENT STAGE & STAKEHOLDERS
    # ==========================================
    elements.append(Paragraph("9. Current Stage & Production Deployment", style_h1))
    elements.append(Paragraph(
        "<b>Functional Deep-Tech Prototype · Production-Ready.</b> A working full-stack platform is deployed using official Assam gazettes "
        "across Pension Rules 1969, ARTPS Act 2012, Mission Basundhara guidelines, and DST circulars. The system includes multi-route navigation, "
        "role-based desk isolation, dual-layer document extraction, character-level verification, automated green-sheet noting generation, "
        "and a continuous audit trail.",
        style_body
    ))
    elements.append(Paragraph("<b>Production Link:</b> https://nesfic-d-36.vercel.app", style_body))
    elements.append(Paragraph("<b>Source Code Repository:</b> https://github.com/anupam-codespace/NESFIC-D-36.git", style_body))
    elements.append(Spacer(1, 4 * pt))

    feat_matrix_data = [
        [
            Paragraph("<b>Feature</b>", style_table_header),
            Paragraph("<b>Status</b>", style_table_header),
            Paragraph("<b>Production Scope</b>", style_table_header)
        ],
        [
            Paragraph("Multi-Route Navigation", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Integration with State portal master navigation", style_table_cell)
        ],
        [
            Paragraph("Accessibility Suite (TTS & Font Resizer)", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("STQC certified WCAG 2.1 AAA compliance", style_table_cell)
        ],
        [
            Paragraph("Multi-Department Gazette Ingestion", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Automated e-Gazette webhook listener", style_table_cell)
        ],
        [
            Paragraph("Dual-Layer Document Extraction", style_table_cell),
            Paragraph("Implemented", style_table_cell_bold),
            Paragraph("Distributed GPU-accelerated ingestion workers", style_table_cell)
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
        ('TOPPADDING', (0, 0), (-1, -1), 2.6 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.6 * pt),
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
        "<b>1. Primary Regulatory & Administrative Bodies (B2G):</b> Administrative Reforms Department (statutory compliance), Assam Administrative Staff College (ACS civil service training), Department of Science & Technology & ASSAC (geospatial/technical guidelines), and Pension & Public Grievances Department.",
        "<b>2. Internal Administrative Cadre:</b> Joint Secretaries, Deputy Secretaries, Under Secretaries, Section Officers, and Senior Assistants across line departments responsible for file drafting and statutory approvals.",
        "<b>3. Public Beneficiaries:</b> Retiring government employees, pensioners, and citizens who benefit from transparent entitlement interpretations and verified eligibility calculations."
    ]
    for sp in stk_points:
        elements.append(Paragraph(sp, style_body))

    elements.append(Paragraph("<b>Contextual Differentiation</b>", style_h2))
    elements.append(Paragraph(
        "Existing administrative workflows rely on manual circular physical files and static digests. Generic AI and ticketing platforms lack awareness of Assam's statutory workflows, secretariat green-sheet noting hierarchies, and departmental jurisdictions. VidhiAI is purpose-built for the Assam context — it models the exact statutory relationships between principal acts and amending notifications, ensures 100% evidence-grounded answers, and formats results directly into the green-sheet notings officers already know.",
        style_body
    ))

    # Clean Page Break so Section 11 starts on Page 6
    elements.append(PageBreak())

    # ==========================================
    # PAGE 6: IP, FUNDING / MILESTONES (₹40 LAKHS) & IMPACT (P1)
    # ==========================================
    elements.append(Paragraph("11. Intellectual Property & Licensing", style_h1))
    ip_points = [
        "<b>• IP Status:</b> Proprietary software architecture developed for the challenge; the source code for the platform is provided for evaluation purposes.",
        "<b>• Patent Strategy:</b> Provisional domestic patent planned covering the method and architecture for real-time statutory verification, automated green-sheet noting generation, and cryptographic provenance tracking in administrative governance.",
        "<b>• Deployment Model:</b> Proposed as an indigenous SaaS / GovTech model deployable on the State Data Centre (SDC) or MeitY-empanelled cloud infrastructure, with the option of an on-premise deployment for air-gapped secretariats."
    ]
    for ip in ip_points:
        elements.append(Paragraph(ip, style_body))

    elements.append(Spacer(1, 8 * pt))
    elements.append(Paragraph("12. Funding & Staged Milestones", style_h1))
    elements.append(Paragraph("<b>Requested Grant:</b> ₹40,00,000 (Rupees Forty Lakhs) — Deep Tech Grant / Assam Startup Scheme.", style_body_bold))
    elements.append(Spacer(1, 4 * pt))

    # Milestones Table: Exactly 5 Milestones matching Reference PDF
    ms_headers = [
        Paragraph("<b>#</b>", style_table_header),
        Paragraph("<b>Milestone</b>", style_table_header),
        Paragraph("<b>Budget</b>", style_table_header),
        Paragraph("<b>Share</b>", style_table_header),
        Paragraph("<b>Prerequisites</b>", style_table_header),
        Paragraph("<b>Deliverables</b>", style_table_header)
    ]

    ms_rows = [
        [
            Paragraph("1", style_table_cell_bold),
            Paragraph("Multi-Department Data & Gazette Corpus Engineering", style_table_cell_bold),
            Paragraph("₹6,40,000", style_table_cell_bold),
            Paragraph("16%", style_table_cell),
            Paragraph("Gazette archives from AASC, Pension, ARTPS, DST, ASSAC", style_table_cell),
            Paragraph("Comprehensive Assam statutory ontology; structured JSON schema; multimodal ingestion pipeline", style_table_cell)
        ],
        [
            Paragraph("2", style_table_cell_bold),
            Paragraph("Bilingual Assamese Document Intelligence & Ingestion Engine", style_table_cell_bold),
            Paragraph("₹10,40,000", style_table_cell_bold),
            Paragraph("26%", style_table_cell),
            Paragraph("Historical gazettes corpuses; State Data Centre sandbox", style_table_cell),
            Paragraph("Custom vision-language model fine-tuned on Assamese ligatures (98%+ benchmark); dual-layer connector with retry logic", style_table_cell)
        ],
        [
            Paragraph("3", style_table_cell_bold),
            Paragraph("Sovereign Legal SLM & Zero-Hallucination Grounding Engine", style_table_cell_bold),
            Paragraph("₹10,80,000", style_table_cell_bold),
            Paragraph("27%", style_table_cell),
            Paragraph("Secretariat Manual precedents; annotated green-sheet notings", style_table_cell),
            Paragraph("Domain-adapted 7B/14B parameter Legal SLM; character-level NFKC verifier engine; automated statutory conflict graph", style_table_cell)
        ],
        [
            Paragraph("4", style_table_cell_bold),
            Paragraph("Multi-Department Secretariat Pilot & Security Hardening", style_table_cell_bold),
            Paragraph("₹7,60,000", style_table_cell_bold),
            Paragraph("19%", style_table_cell),
            Paragraph("Pilot clearance (Administrative Reforms, AASC, Pension); MeitY staging cloud", style_table_cell),
            Paragraph("60-day live pilot across 3 nodal departments (100+ officers); CERT-In VAPT audit report; GIGW 3.0 accessibility verification", style_table_cell)
        ],
        [
            Paragraph("5", style_table_cell_bold),
            Paragraph("Legal & Scale Readiness, Provenance Ledger & SDC Deployment", style_table_cell_bold),
            Paragraph("₹4,80,000", style_table_cell_bold),
            Paragraph("12%", style_table_cell),
            Paragraph("Pilot telemetry data; SDC production container clearance", style_table_cell),
            Paragraph("Evaluation report; statewide rollout blueprint; SHA-256 cryptographic provenance ledger; SDC bare-metal deployment", style_table_cell)
        ],
        [
            Paragraph("", style_table_cell_bold),
            Paragraph("<b>Total</b>", style_table_cell_bold),
            Paragraph("<b>₹40,00,000</b>", style_table_cell_bold),
            Paragraph("<b>100%</b>", style_table_cell_bold),
            Paragraph("", style_table_cell),
            Paragraph("", style_table_cell)
        ]
    ]

    t_ms_data = [ms_headers] + ms_rows
    col_w = [16 * pt, 110 * pt, 56 * pt, 36 * pt, 115 * pt, USABLE_WIDTH - (16+110+56+36+115) * pt]
    t_ms = Table(t_ms_data, colWidths=col_w)
    t_ms.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_BG_ALT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5 * pt),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5 * pt),
        ('LEFTPADDING', (0, 0), (-1, -1), 3 * pt),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3 * pt),
        ('LINEBELOW', (0, 0), (-1, -2), 0.5, BORDER_COLOR),
        ('LINEBELOW', (0, 0), (-1, 0), 1.0, PRIMARY_GREEN),
        # Highlight total row in soft yellow
        ('BACKGROUND', (0, -1), (-1, -1), TOTAL_YELLOW),
        ('LINEABOVE', (0, -1), (-1, -1), 1.0, PRIMARY_GREEN),
        ('LINEBELOW', (0, -1), (-1, -1), 1.0, PRIMARY_GREEN),
        ('TOPPADDING', (0, -1), (-1, -1), 4 * pt),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 4 * pt),
    ]))
    elements.append(t_ms)
    elements.append(Spacer(1, 8 * pt))

    elements.append(Paragraph("13. Projected Impact & Evaluation", style_h1))
    elements.append(Paragraph("<i>Targeted estimates based on pilot benchmarks.</i>", style_body))
    elements.append(Paragraph("<b>Administrative Impacts</b>", style_h2))

    admin_impacts = [
        "<b>1. Accelerated Evidence Retrieval:</b> Reduces evidence-assembly and rule cross-referencing time for file reviews from hours to minutes, dramatically accelerating Secretariat decision-making.",
        "<b>2. Proactive Operational Triage:</b> Surfaces operative clauses, qualifying service rules, and entitlement ceilings within seconds of query submission — eliminating the lag between file intake and supervisory disposal."
    ]
    for ai in admin_impacts:
        elements.append(Paragraph(ai, style_body))

    # Clean Page Break so Section 13 cont. and Section 14 are on Page 7
    elements.append(PageBreak())

    # ==========================================
    # PAGE 7: IMPACT (P2) & STARTUP POLICY ALIGNMENT
    # ==========================================
    admin_impacts_p2 = [
        "<b>3. Objective Merit Recognition:</b> Continuous per-scheme progress and audit-logged noting records establish an objective basis for recognizing high-performing officers and departments.",
        "<b>4. Citizen-Centric Transparency:</b> Plain-language entitlement summaries and transparent source document inspections restore citizen trust in government pension and public service delivery."
    ]
    for ai in admin_impacts_p2:
        elements.append(Paragraph(ai, style_body))

    elements.append(Spacer(1, 4 * pt))
    elements.append(Paragraph("<b>Employment & Capacity Targets</b>", style_h2))
    emp_points = [
        "<b>• Direct Technical Roles:</b> 6–10 engineering, AI/ML research, legal ontology, and GIS data roles based in Assam (Guwahati branch office).",
        "<b>• Ecosystem Support Roles:</b> 25–40 indirect technical and training support positions across districts (nodal officers, digitization operators, field trainers)."
    ]
    for ep in emp_points:
        elements.append(Paragraph(ep, style_body))

    elements.append(Spacer(1, 10 * pt))
    elements.append(Paragraph("14. Alignment with Assam Startup Policy 2025–2030", style_h1))
    elements.append(Paragraph("<b>Primary Category:</b> Category B — IT, ITeS & Artificial Intelligence (Deep Tech Specialization)", style_body_bold))
    elements.append(Spacer(1, 2 * pt))
    elements.append(Paragraph("The proposal aligns with the \"Innovate Assam 2030\" key strategic focus areas:", style_body))

    align_points = [
        "<b>1. Domestic GovTech Innovation:</b> Indigenous technology built for Government of Assam needs, addressing the specific statutory workflows of Administrative Reforms, AASC, DST, Pension & PG, and ASSAC.",
        "<b>2. Data Governance:</b> High-performance web tools, deterministic verification algorithms, RBAC, and audit trails engineered by regional talent based at the Guwahati branch office.",
        "<b>3. Citizen-Centric Governance:</b> Supports the statutory objectives of transparent pension processing, entitlement verification, and grievance redressal under the Assam Right to Public Services Act (ARTPS).",
        "<b>4. Employment Generation:</b> Direct and indirect technical roles based in Assam, with specialized AI training programs for secretariat staff and departmental nodal officers."
    ]
    for ap in align_points:
        elements.append(Paragraph(ap, style_body))

    # Note: Signature & Seal block has been intentionally removed matching teammate reference PDF

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
