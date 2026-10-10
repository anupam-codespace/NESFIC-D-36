'use client';

import React from 'react';
import Link from 'next/link';
import { FileText, MessageSquareWarning, Table2 } from 'lucide-react';


export default function FinalCta() {
  return (
    <section id="inquiry" style={{ backgroundColor: 'rgba(236, 253, 245, 0.75)', borderBottom: '1px solid #A7F3D0', padding: '56px 0', textAlign: 'center' }}>
      <div className="gov-container">
        <div
          style={{
            width: 48,
            height: 48,
            borderRadius: '50%',
            backgroundColor: '#DCFCE7',
            color: '#065F46',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            margin: '0 auto 16px',
            border: '1px solid #A7F3D0',
          }}
        >
          <FileText style={{ width: 24, height: 24, color: '#047857' }} />
        </div>

        <h2 style={{ fontSize: 'clamp(24px, 3.5vw, 32px)', fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: 0 }}>
          Have a question on official Assam rules or gazettes?
        </h2>

        <p style={{ marginTop: 12, fontSize: 14.5, color: '#475569', maxWidth: 640, margin: '12px auto 0', lineHeight: 1.6 }}>
          Query the verified statutory repository of Administrative Reforms, AASC, Science & Technology, Pension & Public Grievances, and ASSAC. Every answer is backed by verbatim gazette evidence.
        </p>

        <div
          style={{
            marginTop: 24,
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'center',
            gap: 12,
          }}
        >
          <Link
            href="/login"
            className="gov-btn-primary"
            style={{ height: 42, padding: '0 20px', minWidth: 200 }}
          >
            <MessageSquareWarning style={{ width: 16, height: 16 }} />
            <span>Sign in to Ask Assistant</span>
          </Link>

          <Link
            href="/login"
            className="gov-btn-outline"
            style={{ height: 42, padding: '0 20px', minWidth: 200 }}
          >
            <Table2 style={{ width: 16, height: 16, color: '#64748B' }} />
            <span>Sign in to Browse Rules</span>
          </Link>
        </div>
      </div>
    </section>
  );
}
