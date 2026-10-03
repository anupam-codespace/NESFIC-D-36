'use client';

import React from 'react';
import { Row, Col, Timeline } from 'antd';
import {
  SafetyOutlined,
  ControlOutlined,
  AuditOutlined,
} from '@ant-design/icons';
import { motion, useReducedMotion } from 'framer-motion';
import { CONTENT } from '@/lib/content';

const PRINCIPLE_ICONS = [
  <SafetyOutlined key="source" style={{ fontSize: 24, color: '#191B1D' }} />,
  <ControlOutlined key="controlled" style={{ fontSize: 24, color: '#DB7A58' }} />,
  <AuditOutlined key="traceable" style={{ fontSize: 24, color: '#005824' }} />,
];

export default function Governance() {
  const shouldReduceMotion = useReducedMotion();

  const timelineItems = CONTENT.governance.lifecycle.map((item, idx) => ({
    color: idx === 5 ? '#005824' : idx >= 2 ? '#DB7A58' : '#52565A',
    children: (
      <div style={{ marginBottom: 12 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 2 }}>
          <span
            style={{
              fontSize: 11,
              fontFamily: 'var(--font-sora)',
              fontWeight: 700,
              color: '#DB7A58',
              letterSpacing: '0.06em',
            }}
          >
            STEP {item.step}
          </span>
          <span
            style={{
              fontFamily: 'var(--font-sora)',
              fontWeight: 600,
              fontSize: 15,
              color: '#191B1D',
            }}
          >
            {item.title}
          </span>
        </div>
        <p style={{ fontSize: 13.5, color: '#52565A', margin: 0, lineHeight: 1.55 }}>
          {item.desc}
        </p>
      </div>
    ),
  }));

  return (
    <section
      id="governance"
      className="section-wrapper"
      style={{ backgroundColor: '#F7F3EB' }}
      aria-labelledby="governance-heading"
    >
      <div className="landing-container">
        {/* Header */}
        <div style={{ maxWidth: 760, marginBottom: 56 }}>
          <span className="section-eyebrow-ta">{CONTENT.governance.eyebrow}</span>
          <h2 id="governance-heading" className="section-title-ta">
            {CONTENT.governance.title}
          </h2>
          <p className="section-subtitle-ta" style={{ marginTop: 14 }}>
            {CONTENT.governance.description}
          </p>
        </div>

        {/* 6-Step Ingestion & Review Lifecycle */}
        <div
          className="card-glow-hover"
          style={{
            backgroundColor: '#FFFFFF',
            borderRadius: 16,
            border: '1px solid var(--border)',
            padding: '36px 32px',
            marginBottom: 44,
          }}
        >
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              marginBottom: 28,
              borderBottom: '1px solid var(--border)',
              paddingBottom: 16,
              flexWrap: 'wrap',
              gap: 12,
            }}
          >
            <div>
              <span
                style={{
                  fontFamily: 'var(--font-sora)',
                  fontSize: 11,
                  fontWeight: 700,
                  color: '#DB7A58',
                  letterSpacing: '0.12em',
                  textTransform: 'uppercase',
                }}
              >
                TRUST VERIFICATION PIPELINE
              </span>
              <h3
                style={{
                  fontFamily: 'var(--font-sora)',
                  fontSize: 18,
                  fontWeight: 600,
                  color: '#191B1D',
                  margin: '4px 0 0 0',
                }}
              >
                The 6-Stage Government Document Lifecycle
              </h3>
            </div>
            <span
              style={{
                borderRadius: 9999,
                padding: '4px 12px',
                fontSize: 12,
                backgroundColor: '#EDE9E1',
                color: '#191B1D',
                fontWeight: 600,
                border: '1px solid var(--border)',
              }}
            >
              Human-in-the-Loop Signoff Required
            </span>
          </div>

          <Timeline items={timelineItems} style={{ marginTop: 24 }} />
        </div>

        {/* Three Principles Row */}
        <Row gutter={[24, 24]}>
          {CONTENT.governance.principles.map((pr, idx) => (
            <Col xs={24} md={8} key={pr.title}>
              <motion.div
                initial={{ opacity: 0, y: shouldReduceMotion ? 0 : 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: '-50px' }}
                transition={{ duration: 0.5, delay: idx * 0.1 }}
                style={{ height: '100%' }}
              >
                <div
                  className="card-glow-hover"
                  style={{
                    backgroundColor: '#FFFFFF',
                    border: '1px solid var(--border)',
                    borderRadius: 12,
                    padding: '28px',
                    height: '100%',
                  }}
                >
                  <div
                    style={{
                      width: 48,
                      height: 48,
                      borderRadius: 10,
                      backgroundColor: '#F7F3EB',
                      border: '1px solid var(--border)',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      marginBottom: 18,
                    }}
                  >
                    {PRINCIPLE_ICONS[idx]}
                  </div>

                  <h3
                    style={{
                      fontFamily: 'var(--font-sora)',
                      fontSize: 18,
                      fontWeight: 600,
                      color: '#191B1D',
                      marginBottom: 10,
                      letterSpacing: '-0.02em',
                    }}
                  >
                    {pr.title}
                  </h3>

                  <p style={{ fontSize: 14, color: '#52565A', lineHeight: 1.6, margin: 0 }}>
                    {pr.desc}
                  </p>
                </div>
              </motion.div>
            </Col>
          ))}
        </Row>
      </div>
    </section>
  );
}
