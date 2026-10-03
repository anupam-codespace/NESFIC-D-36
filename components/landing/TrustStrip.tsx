'use client';

import React from 'react';
import { CONTENT } from '@/lib/content';

export default function TrustStrip() {
  return (
    <section className="press-strip" aria-label="Core Governance Principles">
      <div className="landing-container">
        <p
          style={{
            fontFamily: 'var(--font-sora)',
            fontSize: 12,
            fontWeight: 700,
            letterSpacing: '0.18em',
            color: '#191B1D',
            textTransform: 'uppercase',
            margin: '0 0 6px 0',
          }}
        >
          {CONTENT.trustStrip.principles}
        </p>
        <p style={{ fontSize: 12, color: '#52565A', margin: 0, letterSpacing: '0.04em' }}>
          {CONTENT.trustStrip.footnote}
        </p>
      </div>
    </section>
  );
}
