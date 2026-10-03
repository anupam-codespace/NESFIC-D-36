'use client';

import React from 'react';
import Link from 'next/link';
import {
  LayoutDashboard,
  ScanLine,
  Table2,
  FileEdit,
  Users,
  ShieldCheck,
  ArrowRight,
} from 'lucide-react';

interface FeatureItem {
  icon: React.ReactNode;
  title: string;
  description: string;
  href: string;
}

const FEATURES: FeatureItem[] = [
  {
    icon: <LayoutDashboard style={{ width: 20, height: 20, color: '#059669' }} />,
    title: 'Verbatim Citation Grounding',
    description:
      'Every statutory query produces direct, byte-accurate quotes citing gazette notifications, section numbers, and exact page numbers. If evidence is missing, the response is blocked.',
    href: '/app/dashboard',
  },
  {
    icon: <ScanLine style={{ width: 20, height: 20, color: '#059669' }} />,
    title: 'Dual-Layer 300 DPI OCR Ingestion',
    description:
      'Scans and extracts historical and modern notifications with automated contrast enhancement, skew correction, and bilingual Assamese/English text layer extraction.',
    href: '/login',
  },
  {
    icon: <Table2 style={{ width: 20, height: 20, color: '#059669' }} />,
    title: 'Scoped Departmental Scrutiny',
    description:
      'Enforces strict boundaries across Administrative Reforms, AASC training guidelines, Science & Technology policies, Pension & PG rules, and ASSAC geodata.',
    href: '/app/dashboard',
  },
  {
    icon: <FileEdit style={{ width: 20, height: 20, color: '#059669' }} />,
    title: 'Audit-Ready Officer Noting Generator',
    description:
      'Drafts official green-sheet government notings following standard Assam Secretariat Manual conventions, complete with statutory precedents and verification signatures.',
    href: '/app/dashboard',
  },
  {
    icon: <Users style={{ width: 20, height: 20, color: '#059669' }} />,
    title: 'Citizen & Pension Entitlement Guides',
    description:
      'Plain-language statutory summaries explaining pension qualification, gratuity formulas, service regularisation, and public service rights without bureaucratic jargon.',
    href: '/app/dashboard',
  },
  {
    icon: <ShieldCheck style={{ width: 20, height: 20, color: '#059669' }} />,
    title: 'SHA-256 Cryptographic Audit Ledger',
    description:
      'Every ingested document chunk and every generated administrative noting is timestamped and cryptographically hashed to guarantee zero tampering and full accountability.',
    href: '/app/dashboard',
  },
];

export default function Solution() {
  return (
    <section id="features" style={{ width: '100%', padding: '56px 0', borderBottom: '1px solid #E2E8F0' }}>
      <div className="gov-container">
        <div style={{ textAlign: 'center', marginBottom: 40 }}>
          <p style={{ fontSize: 11, textTransform: 'uppercase', letterSpacing: '0.12em', color: '#047857', fontWeight: 700, margin: 0 }}>
            What this portal does
          </p>
          <h2 style={{ fontSize: 'clamp(24px, 3.5vw, 34px)', fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: '8px 0 0' }}>
            One platform for statutory intelligence
          </h2>
          <p style={{ marginTop: 12, fontSize: 14.5, color: '#64748B', maxWidth: 640, margin: '12px auto 0', lineHeight: 1.6 }}>
            Built for NESFIC 2026 Problem Statement 46, connecting field officers, secretariat desks, and citizens with verifiable administrative truth.
          </p>
        </div>

        <div className="gov-features-grid">
          {FEATURES.map((item, idx) => (
            <Link key={idx} href={item.href} style={{ textDecoration: 'none', color: 'inherit' }}>
              <div className="gov-feature-card">
                <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 12 }}>
                  <div
                    style={{
                      width: 40,
                      height: 40,
                      borderRadius: 8,
                      backgroundColor: 'rgba(16, 185, 129, 0.12)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      flexShrink: 0,
                    }}
                  >
                    {item.icon}
                  </div>
                  <h3
                    style={{
                      fontSize: 15,
                      fontWeight: 600,
                      color: '#0F172A',
                      margin: 0,
                      display: 'flex',
                      alignItems: 'center',
                      gap: 6,
                    }}
                  >
                    <span>{item.title}</span>
                    <ArrowRight style={{ width: 14, height: 14, color: '#059669' }} />
                  </h3>
                </div>
                <p style={{ fontSize: 13.5, color: '#64748B', lineHeight: 1.6, margin: 0 }}>
                  {item.description}
                </p>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}
