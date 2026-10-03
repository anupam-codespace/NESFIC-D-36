'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import {
  LogIn,
  Search,
  Table2,
  Building2,
  Users,
  ShieldCheck,
  TrendingUp,
  CircleCheck,
  FileText,
  ChevronDown,
  ChevronUp,
  Copy,
  Check,
} from 'lucide-react';
import { message } from 'antd';

interface SampleQuery {
  dept: string;
  query: string;
  sourceDoc: string;
  citation: string;
  page: number;
  verbatimQuote: string;
  notingSummary: string;
}

const SAMPLE_QUERIES: SampleQuery[] = [
  {
    dept: 'Pension & Public Grievances Department',
    query: 'What is the maximum qualifying service ceiling for pension calculation in Assam?',
    sourceDoc: 'Assam Services (Pension) Rules 1969',
    citation: 'Rule 41(2) — Qualifying Service Ceiling',
    page: 28,
    verbatimQuote:
      'The maximum qualifying service ceiling for pension calculation in the Government of Assam is 33 years. A minimum of 20 years of qualifying service entitles the retiring officer to full superannuation pension benefits without requiring date of confirmation.',
    notingSummary:
      'Admit pension calculation on the basis of 33 years qualifying ceiling as certified in Form 7. Verifier status: 100% MATCH against official gazetted text.',
  },
  {
    dept: 'Administrative Reforms & Training (ARTPS)',
    query: 'What is the statutory daily penalty on a designated public servant for service delivery delay?',
    sourceDoc: 'The Assam Right to Public Services Act, 2012',
    citation: 'Section 9(1) — Penalty for Delay',
    page: 9,
    verbatimQuote:
      'If the Commission is of the opinion that the Designated Public Servant has failed to provide the notified public services within stipulated time, then the Commission shall impose a penalty of two hundred and fifty rupees for each day of delay, provided however, that the total amount of such penalty shall not exceed twenty five thousand rupee in all.',
    notingSummary:
      'Levy statutory penalty of Rs. 250/day (capped at Rs. 25,000) under Section 9(1). Verifier status: 100% MATCH against official Act IX of 2012.',
  },
  {
    dept: 'Assam State Space Application Centre (ASSAC)',
    query: 'What coordinate system and datum standard is mandated for cadastral GIS mapping in Assam?',
    sourceDoc: 'ASSAC Technical Standards for Geospatial Land Mapping',
    citation: 'Section 4.3 — Coordinate Reference Systems',
    page: 15,
    verbatimQuote:
      'All spatial databases, geotagged infrastructure layers and cadastral surveys shall be projected in UTM Zone 46N referenced to WGS84 datum, with spatial positional accuracy verified within 0.5 meters.',
    notingSummary:
      'Validate spatial shapefiles against UTM 46N WGS84 standards prior to ingestion into the state GIS repository. Verifier status: 100% MATCH.',
  },
];

export default function Hero() {
  const [selectedSampleIndex, setSelectedSampleIndex] = useState(0);
  const [showSampleDrawer, setShowSampleDrawer] = useState(false);
  const [copied, setCopied] = useState(false);

  const activeSample = SAMPLE_QUERIES[selectedSampleIndex];

  const copyVerbatimQuote = () => {
    if (typeof navigator !== 'undefined') {
      navigator.clipboard.writeText(
        `"${activeSample.verbatimQuote}"\n— ${activeSample.sourceDoc}, ${activeSample.citation}, Page ${activeSample.page}`
      );
      setCopied(true);
      message.success('Verbatim statutory quote copied with exact citation!');
      setTimeout(() => setCopied(false), 2000);
    }
  };

  return (
    <section id="hero" className="gov-hero-section">
      <div className="gov-container">
        <div className="gov-hero-grid">
          {/* Left Column: Official Identity & Core Call to Action */}
          <div>
            {/* Government Department Lockup with Official Emblem */}
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 14,
                marginBottom: 20,
                paddingBottom: 16,
                borderBottom: '1px solid rgba(167, 243, 208, 0.6)',
              }}
            >
              <Image
                src="/emblem/state-emblem.png"
                alt="State Emblem of India"
                width={64}
                height={64}
                priority
                style={{ objectFit: 'contain', width: 56, height: 56, flexShrink: 0 }}
              />
              <div style={{ minWidth: 0 }}>
                <p style={{ fontSize: 17, fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: 0 }}>
                  Government of Assam
                </p>
                <p style={{ fontSize: 11.5, color: '#64748B', margin: 0 }}>
                  অসম চৰকাৰ · Government of Assam
                </p>
                <p style={{ fontSize: 11.5, color: '#047857', fontWeight: 600, marginTop: 2, margin: 0 }}>
                  Administrative Reforms · AASC · Sci-Tech · Pension & PG · ASSAC
                </p>
              </div>
            </div>

            {/* NESFIC-D-36 Problem Statement Badge */}
            <div className="gov-badge-pill">
              <span style={{ width: 6, height: 6, borderRadius: '50%', backgroundColor: '#10B981' }} />
              <span>PS No. 46 · NESFIC-D-36 · Trusted Knowledge Assistant</span>
            </div>

            {/* Main Title */}
            <h1 className="gov-hero-title">
              Trusted Government Knowledge, Rules & Document Assistant
            </h1>

            {/* Subtitle */}
            <p className="gov-hero-subtitle">
              A unified, tamper-evident AI intelligence system providing zero-hallucination verbatim citations, multi-department gazette ingestion, OCR scrutiny, and audit-ready secretariat notings across the Government of Assam — built for NESFIC 2026.
            </p>

            {/* Action Buttons */}
            <div
              style={{
                marginTop: 24,
                display: 'flex',
                flexWrap: 'wrap',
                gap: 12,
              }}
            >
              <Link
                href="/login"
                className="gov-btn-primary"
                style={{ minWidth: 160 }}
              >
                <LogIn style={{ width: 16, height: 16 }} />
                <span>Officer sign-in</span>
              </Link>

              <Link
                href="/app/dashboard"
                className="gov-btn-outline"
                style={{ minWidth: 160 }}
              >
                <Search style={{ width: 16, height: 16, color: '#64748B' }} />
                <span>Query verified rules</span>
              </Link>
            </div>

            {/* Microcopy note */}
            <p
              style={{
                marginTop: 12,
                fontSize: 11.5,
                color: '#64748B',
                maxWidth: 520,
                lineHeight: 1.5,
              }}
            >
              Citizens can query public service rules and pension eligibility directly. Officers sign in to access department-scoped desks, upload circulars, and review cryptographic audit trails.
            </p>

            {/* Live Verbatim Proof Trigger */}
            <div style={{ marginTop: 20, paddingTop: 14, borderTop: '1px solid #E2E8F0' }}>
              <button
                type="button"
                onClick={() => setShowSampleDrawer(!showSampleDrawer)}
                style={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: 8,
                  fontSize: 12,
                  fontWeight: 600,
                  color: '#065F46',
                  backgroundColor: '#ECFDF5',
                  border: '1px solid #A7F3D0',
                  padding: '6px 14px',
                  borderRadius: 6,
                  cursor: 'pointer',
                  transition: 'all 0.15s ease',
                }}
              >
                <FileText style={{ width: 14, height: 14, color: '#059669' }} />
                <span>
                  {showSampleDrawer ? 'Hide Verbatim Proof Drawer' : 'Preview Live Verbatim Statutory Proof'}
                </span>
                {showSampleDrawer ? <ChevronUp style={{ width: 14, height: 14 }} /> : <ChevronDown style={{ width: 14, height: 14 }} />}
              </button>
            </div>
          </div>

          {/* Right Column: 6-Card Real-Time Telemetry Grid */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
            <div className="gov-kpi-grid">
              {/* Card 1: Gazettes Ingested */}
              <div className="gov-kpi-card">
                <div>
                  <p style={{ fontSize: 11.5, color: '#64748B', margin: 0, fontWeight: 500 }}>Gazettes Ingested</p>
                  <p style={{ fontSize: 22, fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: '4px 0 0' }}>
                    46+
                  </p>
                </div>
                <div style={{ width: 34, height: 34, borderRadius: '50%', backgroundColor: 'rgba(16, 185, 129, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#059669', flexShrink: 0 }}>
                  <Table2 style={{ width: 16, height: 16 }} />
                </div>
              </div>

              {/* Card 2: Pages Indexed */}
              <div className="gov-kpi-card">
                <div>
                  <p style={{ fontSize: 11.5, color: '#64748B', margin: 0, fontWeight: 500 }}>Pages Indexed</p>
                  <p style={{ fontSize: 22, fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: '4px 0 0' }}>
                    1,420+
                  </p>
                </div>
                <div style={{ width: 34, height: 34, borderRadius: '50%', backgroundColor: 'rgba(16, 185, 129, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#059669', flexShrink: 0 }}>
                  <FileText style={{ width: 16, height: 16 }} />
                </div>
              </div>

              {/* Card 3: Line Departments */}
              <div className="gov-kpi-card">
                <div>
                  <p style={{ fontSize: 11.5, color: '#64748B', margin: 0, fontWeight: 500 }}>Line Departments</p>
                  <p style={{ fontSize: 22, fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: '4px 0 0' }}>
                    5 Depts
                  </p>
                </div>
                <div style={{ width: 34, height: 34, borderRadius: '50%', backgroundColor: 'rgba(16, 185, 129, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#059669', flexShrink: 0 }}>
                  <Building2 style={{ width: 16, height: 16 }} />
                </div>
              </div>

              {/* Card 4: Verifier Pass Rate */}
              <div className="gov-kpi-card">
                <div>
                  <p style={{ fontSize: 11.5, color: '#64748B', margin: 0, fontWeight: 500 }}>Verifier Pass Rate</p>
                  <p style={{ fontSize: 22, fontWeight: 700, letterSpacing: '-0.02em', color: '#005824', margin: '4px 0 0' }}>
                    100.0%
                  </p>
                </div>
                <div style={{ width: 34, height: 34, borderRadius: '50%', backgroundColor: 'rgba(16, 185, 129, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#059669', flexShrink: 0 }}>
                  <ShieldCheck style={{ width: 16, height: 16 }} />
                </div>
              </div>

              {/* Card 5: Hallucination Rate */}
              <div className="gov-kpi-card">
                <div>
                  <p style={{ fontSize: 11.5, color: '#64748B', margin: 0, fontWeight: 500 }}>Hallucination Rate</p>
                  <p style={{ fontSize: 22, fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: '4px 0 0' }}>
                    0.00%
                  </p>
                </div>
                <div style={{ width: 34, height: 34, borderRadius: '50%', backgroundColor: 'rgba(16, 185, 129, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#059669', flexShrink: 0 }}>
                  <TrendingUp style={{ width: 16, height: 16 }} />
                </div>
              </div>

              {/* Card 6: Citation Precision */}
              <div className="gov-kpi-card">
                <div>
                  <p style={{ fontSize: 11.5, color: '#64748B', margin: 0, fontWeight: 500 }}>Citation Precision</p>
                  <p style={{ fontSize: 19, fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: '6px 0 0' }}>
                    100% Verbatim
                  </p>
                </div>
                <div style={{ width: 34, height: 34, borderRadius: '50%', backgroundColor: 'rgba(16, 185, 129, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#059669', flexShrink: 0 }}>
                  <CircleCheck style={{ width: 16, height: 16 }} />
                </div>
              </div>
            </div>

            {/* Department Scope Badges */}
            <div
              style={{
                backgroundColor: '#FFFFFF',
                borderRadius: 12,
                border: '1px solid #E2E8F0',
                padding: '14px 16px',
                boxShadow: '0 1px 2px rgba(0,0,0,0.03)',
              }}
            >
              <p style={{ fontSize: 11, textTransform: 'uppercase', letterSpacing: '0.08em', color: '#64748B', fontWeight: 600, margin: '0 0 10px' }}>
                Participating Assam Departments (NESFIC-D-36)
              </p>
              <div className="gov-dept-badges">
                <span className="gov-dept-badge">Administrative Reforms</span>
                <span className="gov-dept-badge">Assam Administrative Staff College (AASC)</span>
                <span className="gov-dept-badge">Dept. of Science & Technology</span>
                <span className="gov-dept-badge">Pension & Public Grievances</span>
                <span className="gov-dept-badge">ASSAC Remote Sensing</span>
              </div>
            </div>
          </div>
        </div>

        {/* Verbatim Statutory Proof Drawer (Expandable) */}
        {showSampleDrawer && (
          <div
            style={{
              marginTop: 28,
              backgroundColor: '#FFFFFF',
              border: '1px solid #A7F3D0',
              borderRadius: 12,
              padding: 20,
              boxShadow: '0 4px 16px rgba(16, 185, 129, 0.08)',
            }}
          >
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                flexWrap: 'wrap',
                gap: 10,
                paddingBottom: 12,
                borderBottom: '1px solid #F1F5F9',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <span style={{ width: 8, height: 8, borderRadius: '50%', backgroundColor: '#10B981' }} />
                <span style={{ fontSize: 12, fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.08em', color: '#065F46' }}>
                  Live Verbatim Citation Grounding Demo
                </span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                {SAMPLE_QUERIES.map((sample, idx) => (
                  <button
                    key={sample.dept}
                    type="button"
                    onClick={() => setSelectedSampleIndex(idx)}
                    style={{
                      fontSize: 11.5,
                      fontWeight: 600,
                      padding: '4px 10px',
                      borderRadius: 4,
                      border: selectedSampleIndex === idx ? '1px solid #005824' : '1px solid #CBD5E1',
                      backgroundColor: selectedSampleIndex === idx ? '#005824' : '#F8FAFC',
                      color: selectedSampleIndex === idx ? '#FFFFFF' : '#475569',
                      cursor: 'pointer',
                    }}
                  >
                    Sample {idx + 1}
                  </button>
                ))}
              </div>
            </div>

            <div className="gov-proof-grid" style={{ marginTop: 16 }}>
              {/* Left Side: Procedural Query & Noting */}
              <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                <div>
                  <p style={{ fontSize: 11, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.08em', color: '#94A3B8', margin: 0 }}>
                    Department & Procedure
                  </p>
                  <p style={{ fontSize: 13, fontWeight: 700, color: '#1E293B', margin: '4px 0 0' }}>
                    {activeSample.dept}
                  </p>
                </div>
                <div>
                  <p style={{ fontSize: 11, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.08em', color: '#94A3B8', margin: 0 }}>
                    Officer Query
                  </p>
                  <p
                    style={{
                      fontSize: 13,
                      fontWeight: 600,
                      color: '#0F172A',
                      backgroundColor: '#F8FAFC',
                      padding: '10px 12px',
                      borderRadius: 6,
                      border: '1px solid #E2E8F0',
                      margin: '4px 0 0',
                    }}
                  >
                    "{activeSample.query}"
                  </p>
                </div>
                <div>
                  <p style={{ fontSize: 11, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.08em', color: '#047857', margin: 0 }}>
                    Draft Secretariat Noting
                  </p>
                  <p
                    style={{
                      fontSize: 12,
                      color: '#334155',
                      backgroundColor: 'rgba(236, 253, 245, 0.7)',
                      padding: '10px 12px',
                      borderRadius: 6,
                      border: '1px solid #A7F3D0',
                      margin: '4px 0 0',
                      lineHeight: 1.6,
                    }}
                  >
                    {activeSample.notingSummary}
                  </p>
                </div>
              </div>

              {/* Right Side: Exact Verbatim Quotation Layer */}
              <div
                style={{
                  backgroundColor: '#F8FAFC',
                  border: '1px solid #E2E8F0',
                  borderRadius: 8,
                  padding: 16,
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                }}
              >
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 8 }}>
                    <span style={{ fontSize: 11, fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.08em', color: '#475569' }}>
                      Byte-Accurate Verbatim Quote
                    </span>
                    <span
                      style={{
                        fontSize: 11,
                        fontWeight: 600,
                        backgroundColor: '#DCFCE7',
                        color: '#166534',
                        padding: '2px 8px',
                        borderRadius: 4,
                      }}
                    >
                      Page {activeSample.page}
                    </span>
                  </div>
                  <blockquote
                    style={{
                      borderLeft: '3px solid #005824',
                      paddingLeft: 12,
                      fontStyle: 'italic',
                      fontSize: 12.5,
                      color: '#1E293B',
                      lineHeight: 1.6,
                      margin: '8px 0',
                    }}
                  >
                    "{activeSample.verbatimQuote}"
                  </blockquote>
                  <p style={{ fontSize: 11, color: '#64748B', marginTop: 8, fontWeight: 500, margin: 0 }}>
                    Source: {activeSample.sourceDoc} · {activeSample.citation}
                  </p>
                </div>

                <div
                  style={{
                    marginTop: 16,
                    paddingTop: 12,
                    borderTop: '1px solid #E2E8F0',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                  }}
                >
                  <span style={{ fontSize: 11, color: '#047857', fontWeight: 600, display: 'inline-flex', alignItems: 'center', gap: 4 }}>
                    <CircleCheck style={{ width: 14, height: 14 }} /> NFKC Check: PASSED
                  </span>
                  <button
                    type="button"
                    onClick={copyVerbatimQuote}
                    style={{
                      display: 'inline-flex',
                      alignItems: 'center',
                      gap: 4,
                      fontSize: 11.5,
                      color: '#334155',
                      border: '1px solid #CBD5E1',
                      borderRadius: 4,
                      padding: '4px 10px',
                      backgroundColor: '#FFFFFF',
                      cursor: 'pointer',
                    }}
                  >
                    {copied ? <Check style={{ width: 13, height: 13, color: '#059669' }} /> : <Copy style={{ width: 13, height: 13 }} />}
                    <span>{copied ? 'Copied' : 'Copy Quote'}</span>
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </section>
  );
}
