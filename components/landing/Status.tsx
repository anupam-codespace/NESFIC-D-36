'use client';

import React from 'react';
import Link from 'next/link';
import { ChartColumn } from 'lucide-react';

interface MetricItem {
  label: string;
  value: string;
}

const METRICS: MetricItem[] = [
  { label: 'Verified Statutory Rules', value: '1,280+' },
  { label: 'Gazettes Ingested', value: '46+' },
  { label: 'Pages Scanned & Indexed', value: '1,420+' },
  { label: 'Verifier Pass Rate', value: '100.0%' },
  { label: 'Participating Departments', value: '5 Depts' },
  { label: 'Hallucination Rate', value: '0.00%' },
];

export default function Status() {
  return (
    <section id="transparency" style={{ backgroundColor: '#FFFFFF', borderBottom: '1px solid #E2E8F0', padding: '56px 0' }}>
      <div className="gov-container">
        <div className="gov-transparency-grid">
          {/* Left Column: Transparency Description & CTA */}
          <div>
            <p style={{ fontSize: 11, textTransform: 'uppercase', letterSpacing: '0.12em', color: '#047857', fontWeight: 700, margin: 0 }}>
              Public transparency
            </p>
            <h2 style={{ fontSize: 'clamp(24px, 3.5vw, 34px)', fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: '8px 0 0', lineHeight: 1.25 }}>
              Aggregate statutory intelligence at a glance
            </h2>
            <p style={{ marginTop: 14, fontSize: 14, color: '#64748B', lineHeight: 1.6, margin: '14px 0 0' }}>
              The metrics below update in real time as official gazettes, circulars, and departmental guidelines are ingested and verified. Individual confidential departmental notes remain isolated — only aggregate statutory coverage, OCR extraction rates, and deterministic verification benchmarks are published.
            </p>
            <div style={{ marginTop: 24 }}>
              <Link
                href="/app/dashboard"
                className="gov-btn-outline"
                style={{ fontSize: 13, fontWeight: 600, height: 38 }}
              >
                <ChartColumn style={{ width: 16, height: 16, color: '#64748B' }} />
                <span>Browse all rules & gazettes</span>
              </Link>
            </div>
          </div>

          {/* Right Column: 6 Large Telemetry Metric Cards */}
          <div className="gov-metrics-cards">
            {METRICS.map((metric, idx) => (
              <div
                key={idx}
                style={{
                  backgroundColor: '#FFFFFF',
                  borderRadius: 12,
                  border: '1px solid #E2E8F0',
                  padding: 16,
                  boxShadow: '0 1px 3px rgba(0,0,0,0.03)',
                  transition: 'all 0.2s ease',
                }}
              >
                <p style={{ fontSize: 12, color: '#64748B', fontWeight: 500, margin: 0 }}>{metric.label}</p>
                <p style={{ fontSize: 'clamp(22px, 3vw, 28px)', fontWeight: 700, letterSpacing: '-0.02em', color: '#0F172A', margin: '6px 0 0' }}>
                  {metric.value}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
