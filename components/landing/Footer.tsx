import React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { ShieldCheck } from 'lucide-react';

export default function Footer() {
  return (
    <footer style={{ backgroundColor: '#F8FAFC', borderTop: '1px solid #E2E8F0', padding: '24px 0', marginTop: 'auto' }} role="contentinfo">
      <div className="gov-container" style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
        {/* Top Accreditation Bar */}
        <div
          style={{
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexWrap: 'wrap',
            gap: 12,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, maxWidth: 840 }}>
            <div
              style={{
                width: 28,
                height: 28,
                borderRadius: 6,
                backgroundColor: '#FFFFFF',
                border: '1px solid #CBD5E1',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                padding: 2,
                flexShrink: 0,
              }}
            >
              <Image
                src="/emblem/seal-of-assam.png"
                alt="Government of Assam Seal"
                width={22}
                height={22}
                style={{ objectFit: 'contain' }}
              />
            </div>
            <span style={{ fontSize: 12, color: '#475569', lineHeight: 1.5 }}>
              Administrative Reforms Department — Government of Assam.
            </span>
          </div>

          <p style={{ fontSize: 11.5, color: '#64748B', fontWeight: 600, margin: 0, whiteSpace: 'nowrap' }}>
            Government Knowledge, Rules & Document Assistant
          </p>
        </div>

        {/* Bottom Compliance & Links Strip */}
        <div
          style={{
            paddingTop: 14,
            borderTop: '1px solid #E2E8F0',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexWrap: 'wrap',
            gap: 10,
            fontSize: 11.5,
            color: '#94A3B8',
          }}
        >
          <span>
            © 2026 Government of Assam · North East Seva First Innovation Challenge 2026 (NESFIC 2026) · Seva Sankalp Abhiyan
          </span>

          <div style={{ display: 'flex', alignItems: 'center', gap: 16, color: '#64748B' }}>
            <Link href="/login" style={{ color: 'inherit', textDecoration: 'none' }}>
              Officer Portal
            </Link>
            <Link href="/login" style={{ color: 'inherit', textDecoration: 'none' }}>
              Sign in / Workspace
            </Link>
            <a href="#features" style={{ color: 'inherit', textDecoration: 'none' }}>
              Features
            </a>
            <a href="#transparency" style={{ color: 'inherit', textDecoration: 'none' }}>
              Audit Benchmarks
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}
