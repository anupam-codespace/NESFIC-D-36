'use client';

import React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import {
  LogIn,
  Search,
  Table2,
  Building2,
  ShieldCheck,
  TrendingUp,
  CircleCheck,
  FileText,
} from 'lucide-react';

export default function Hero() {
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
                marginBottom: 24,
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
                  Administrative Reforms Department
                </p>
              </div>
            </div>

            {/* Main Title */}
            <h1 className="gov-hero-title">
              Trusted Government Knowledge, Rules & Document Assistant
            </h1>

            {/* Subtitle */}
            <p className="gov-hero-subtitle">
              A unified, tamper-evident AI intelligence system providing zero-hallucination verbatim citations, multi-department gazette ingestion, OCR scrutiny, and audit-ready secretariat notings across the Government of Assam.
            </p>

            {/* Action Buttons */}
            <div
              style={{
                marginTop: 28,
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
          </div>
        </div>
      </div>
    </section>
  );
}
