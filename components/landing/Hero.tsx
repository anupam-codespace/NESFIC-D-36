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
          <div style={{ minWidth: 0, maxWidth: '100%', width: '100%', overflow: 'hidden' }}>
            {/* Government Department Lockup with Official Assam Seal */}
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 12,
                marginBottom: 20,
                paddingBottom: 14,
                borderBottom: '1px solid rgba(167, 243, 208, 0.6)',
                width: '100%',
              }}
            >
              <div
                style={{
                  width: 52,
                  height: 52,
                  borderRadius: 12,
                  backgroundColor: '#FFFFFF',
                  border: '1px solid #CBD5E1',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  padding: 4,
                  flexShrink: 0,
                  boxShadow: '0 2px 6px rgba(0, 0, 0, 0.04)',
                }}
              >
                <Image
                  src="/emblem/seal-of-assam.png"
                  alt="Government of Assam Seal"
                  width={44}
                  height={44}
                  priority
                  style={{ objectFit: 'contain', width: '100%', height: '100%' }}
                />
              </div>
              <div style={{ minWidth: 0, flex: 1 }}>
                <p style={{ fontSize: 16, fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: 0, wordBreak: 'break-word' }}>
                  Government of Assam
                </p>
                <p style={{ fontSize: 11, color: '#64748B', margin: 0, wordBreak: 'break-word' }}>
                  অসম চৰকাৰ · Government of Assam
                </p>
                <p style={{ fontSize: 11.5, color: '#047857', fontWeight: 600, marginTop: 2, margin: 0, wordBreak: 'break-word' }}>
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
              A sovereign administrative intelligence platform delivering verbatim statutory grounding, multi-department gazette synthesis, regulatory scrutiny, and audit-ready secretariat file notings across the Government of Assam.
            </p>

            {/* Action Buttons */}
            <div className="gov-hero-actions">
              <Link
                href="/login"
                className="gov-btn-primary"
              >
                <LogIn style={{ width: 16, height: 16 }} />
                <span>Sign in</span>
              </Link>

              <Link
                href="/login"
                className="gov-btn-outline"
              >
                <FileText style={{ width: 16, height: 16, color: '#059669' }} />
                <span>Explore Official Gazettes</span>
              </Link>
            </div>
          </div>

          {/* Right Column: Distinct Individual Metric Boxes */}
          <div
            style={{
              minWidth: 0,
              maxWidth: '100%',
              width: '100%',
              overflow: 'hidden',
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
            }}
          >
            {/* Desktop View: Clean 2-column Grid of Individual Boxes */}
            <div className="gov-hero-boxes-desktop">
              {[
                { label: 'Gazettes Ingested', value: '46+', icon: Table2 },
                { label: 'Pages Indexed', value: '1,420+', icon: FileText },
                { label: 'Line Departments', value: '5 Depts', icon: Building2 },
                { label: 'Verifier Pass Rate', value: '100.0%', valueColor: '#005824', icon: ShieldCheck },
                { label: 'Statutory Grounding', value: '100.0%', valueColor: '#005824', icon: ShieldCheck },
                { label: 'Citation Precision', value: '100% Verbatim', icon: CircleCheck },
              ].map((b, idx) => {
                const IconComponent = b.icon;
                return (
                  <div key={`desktop-box-${idx}`} className="gov-hero-card">
                    <div>
                      <p style={{ fontSize: 12, color: '#64748B', margin: 0, fontWeight: 500 }}>
                        {b.label}
                      </p>
                      <p
                        style={{
                          fontSize: 22,
                          fontWeight: 700,
                          letterSpacing: '-0.02em',
                          color: b.valueColor || '#0F172A',
                          margin: '4px 0 0',
                          lineHeight: 1.2,
                        }}
                      >
                        {b.value}
                      </p>
                    </div>
                    <div
                      style={{
                        width: 38,
                        height: 38,
                        borderRadius: '50%',
                        backgroundColor: 'rgba(16, 185, 129, 0.12)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        color: '#059669',
                        flexShrink: 0,
                      }}
                    >
                      <IconComponent style={{ width: 18, height: 18 }} />
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Mobile & Small Screens View: Individual boxes move continuously from left to right */}
            <div className="gov-hero-boxes-mobile-wrapper">
              <div className="gov-hero-boxes-mobile-track">
                {[
                  { label: 'Gazettes Ingested', value: '46+', icon: Table2 },
                  { label: 'Pages Indexed', value: '1,420+', icon: FileText },
                  { label: 'Line Departments', value: '5 Depts', icon: Building2 },
                  { label: 'Verifier Pass Rate', value: '100.0%', valueColor: '#005824', icon: ShieldCheck },
                  { label: 'Statutory Grounding', value: '100.0%', valueColor: '#005824', icon: ShieldCheck },
                  { label: 'Citation Precision', value: '100% Verbatim', icon: CircleCheck },
                  { label: 'Gazettes Ingested', value: '46+', icon: Table2 },
                  { label: 'Pages Indexed', value: '1,420+', icon: FileText },
                  { label: 'Line Departments', value: '5 Depts', icon: Building2 },
                  { label: 'Verifier Pass Rate', value: '100.0%', valueColor: '#005824', icon: ShieldCheck },
                  { label: 'Statutory Grounding', value: '100.0%', valueColor: '#005824', icon: ShieldCheck },
                  { label: 'Citation Precision', value: '100% Verbatim', icon: CircleCheck },
                ].map((b, idx) => {
                  const IconComponent = b.icon;
                  return (
                    <div key={`mobile-box-${idx}`} className="gov-hero-card">
                      <div>
                        <p style={{ fontSize: 11.5, color: '#64748B', margin: 0, fontWeight: 500 }}>
                          {b.label}
                        </p>
                        <p
                          style={{
                            fontSize: 20,
                            fontWeight: 700,
                            letterSpacing: '-0.02em',
                            color: b.valueColor || '#0F172A',
                            margin: '3px 0 0',
                            lineHeight: 1.2,
                          }}
                        >
                          {b.value}
                        </p>
                      </div>
                      <div
                        style={{
                          width: 36,
                          height: 36,
                          borderRadius: '50%',
                          backgroundColor: 'rgba(16, 185, 129, 0.12)',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          color: '#059669',
                          flexShrink: 0,
                        }}
                      >
                        <IconComponent style={{ width: 17, height: 17 }} />
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

