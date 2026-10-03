'use client';

import React from 'react';
import Link from 'next/link';
import {
  Building2,
  Briefcase,
  Users,
  CircleCheck,
  ArrowRight,
} from 'lucide-react';

interface RoleCard {
  id: string;
  icon: React.ReactNode;
  title: string;
  points: string[];
  ctaLabel: string;
  ctaHref: string;
}

const ROLES: RoleCard[] = [
  {
    id: 'admin',
    icon: <Building2 style={{ width: 20, height: 20, color: '#059669' }} />,
    title: 'For State Administrators & AASC',
    points: [
      'Full visibility across every department gazette, circular, and order',
      'Standardize administrative training curricula and rule revisions',
      'Aggregate CSV export of currently indexed gazettes and queries',
      'Cryptographic SHA-256 audit trail attributed to every officer noting',
    ],
    ctaLabel: 'Sign in as State Admin',
    ctaHref: '/login',
  },
  {
    id: 'officer',
    icon: <Briefcase style={{ width: 20, height: 20, color: '#059669' }} />,
    title: 'For Department Desk Officers',
    points: [
      'Scoped to Pension, Administrative Reforms, Sci-Tech, or ASSAC',
      'Instant statutory quote lookup to resolve file disputes in minutes',
      'Draft official green-sheet secretariat notings with citations',
      'Secure PDF intake with automated 300 DPI OCR chunking pipeline',
    ],
    ctaLabel: 'Sign in as Officer',
    ctaHref: '/login',
  },
  {
    id: 'citizen',
    icon: <Users style={{ width: 20, height: 20, color: '#059669' }} />,
    title: 'For Citizens & Pensioners',
    points: [
      'Query pension eligibility, qualifying service, and gratuity formulas',
      '100% zero misinformation — every response backed by verified PDFs',
      'Direct page references with transparent source viewer',
      'Plain-language Assamese and English procedural explanations',
    ],
    ctaLabel: 'Ask Public Rules Assistant',
    ctaHref: '/app/dashboard',
  },
];

export default function Problem() {
  return (
    <section id="roles" style={{ backgroundColor: '#F8FAFC', borderBottom: '1px solid #E2E8F0', padding: '56px 0' }}>
      <div className="gov-container">
        <div style={{ textAlign: 'center', marginBottom: 40 }}>
          <p style={{ fontSize: 11, textTransform: 'uppercase', letterSpacing: '0.12em', color: '#047857', fontWeight: 700, margin: 0 }}>
            How it works for you
          </p>
          <h2 style={{ fontSize: 'clamp(24px, 3.5vw, 34px)', fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: '8px 0 0' }}>
            Tailored to your role
          </h2>
        </div>

        <div className="gov-roles-grid">
          {ROLES.map((role) => (
            <div key={role.id} className="gov-role-card">
              <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 16 }}>
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
                  {role.icon}
                </div>
                <h3 style={{ fontSize: 15.5, fontWeight: 700, color: '#0F172A', margin: 0 }}>
                  {role.title}
                </h3>
              </div>

              <ul style={{ margin: 0, padding: 0, listStyle: 'none', display: 'flex', flexDirection: 'column', gap: 10, flex: 1, marginBottom: 24 }}>
                {role.points.map((pt, idx) => (
                  <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: 8, fontSize: 13.5, color: '#334155', lineHeight: 1.5 }}>
                    <CircleCheck style={{ width: 16, height: 16, color: '#059669', flexShrink: 0, marginTop: 2 }} />
                    <span>{pt}</span>
                  </li>
                ))}
              </ul>

              <Link
                href={role.ctaHref}
                className="gov-btn-outline"
                style={{ width: '100%', justifyContent: 'center', height: 38, fontSize: 13, fontWeight: 600 }}
              >
                <span>{role.ctaLabel}</span>
                <ArrowRight style={{ width: 14, height: 14, color: '#64748B' }} />
              </Link>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
