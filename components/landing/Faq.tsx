'use client';

import React from 'react';
import { Collapse } from 'antd';
import { CaretRightOutlined } from '@ant-design/icons';
import { CONTENT } from '@/lib/content';

export default function Faq() {
  const items = CONTENT.faq.items.map((item) => ({
    key: item.key,
    label: (
      <span
        style={{
          fontFamily: 'var(--font-sora)',
          fontWeight: 600,
          fontSize: 16,
          color: '#191B1D',
        }}
      >
        {item.question}
      </span>
    ),
    children: (
      <p style={{ fontSize: 14.5, lineHeight: 1.7, color: '#52565A', margin: 0 }}>
        {item.answer}
      </p>
    ),
  }));

  return (
    <section id="faq" className="section-wrapper" style={{ backgroundColor: '#F7F3EB' }} aria-labelledby="faq-heading">
      <div className="landing-container" style={{ maxWidth: 840 }}>
        {/* Header */}
        <div style={{ textAlign: 'center', marginBottom: 48 }}>
          <span className="section-eyebrow-ta">{CONTENT.faq.eyebrow}</span>
          <h2 id="faq-heading" className="section-title-ta" style={{ textAlign: 'center' }}>
            {CONTENT.faq.title}
          </h2>
          <p className="section-subtitle-ta" style={{ margin: '14px auto 0 auto', textAlign: 'center' }}>
            Direct answers on architecture, document boundaries, and prototype scope for evaluators and officers.
          </p>
        </div>

        {/* TaskAssist Styled Collapse Accordion */}
        <div
          className="card-glow-hover"
          style={{
            backgroundColor: '#FFFFFF',
            borderRadius: 16,
            border: '1px solid var(--border)',
            overflow: 'hidden',
          }}
        >
          <Collapse
            accordion
            defaultActiveKey={['1']}
            bordered={false}
            items={items}
            expandIcon={({ isActive }) => (
              <CaretRightOutlined
                rotate={isActive ? 90 : 0}
                style={{ color: '#DB7A58', fontSize: 13 }}
              />
            )}
            style={{
              backgroundColor: 'transparent',
            }}
          />
        </div>
      </div>
    </section>
  );
}
