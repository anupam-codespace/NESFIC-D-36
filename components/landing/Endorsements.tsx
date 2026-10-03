'use client';

import React from 'react';
import { CONTENT } from '@/lib/content';

/**
 * Endorsements Component
 * Per NESFIC 2026 Non-negotiable Honesty Rules:
 * "Add placeholder component <Endorsements /> that renders NOTHING unless real
 * entries exist in content.ts. Do not render fake logos or quotes."
 */
export default function Endorsements() {
  if (!CONTENT.endorsements || CONTENT.endorsements.length === 0) {
    return null;
  }

  return (
    <section className="section-wrapper" style={{ backgroundColor: '#F8FAFC' }}>
      <div className="landing-container">
        <div style={{ textAlign: 'center', marginBottom: 32 }}>
          <span className="section-eyebrow">TESTIMONIALS</span>
          <h2 className="section-title" style={{ fontSize: 32 }}>
            What Officers Say
          </h2>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 20 }}>
          {CONTENT.endorsements.map((item) => (
            <div
              key={item.id}
              style={{
                backgroundColor: '#FFFFFF',
                borderRadius: 12,
                padding: 24,
                border: '1px solid #E2E8F0',
              }}
            >
              <p style={{ fontStyle: 'italic', color: '#334155', marginBottom: 12 }}>
                &ldquo;{item.quote}&rdquo;
              </p>
              <div style={{ fontWeight: 600, color: '#0F172A', fontSize: 14 }}>{item.author}</div>
              <div style={{ fontSize: 12, color: '#64748B' }}>
                {item.designation}, {item.organization}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
