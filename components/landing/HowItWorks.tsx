'use client';

import React, { useState, useEffect } from 'react';
import { Steps } from 'antd';
import {
  EditOutlined,
  SearchOutlined,
  FileDoneOutlined,
  SafetyCertificateOutlined,
} from '@ant-design/icons';
import { CONTENT } from '@/lib/content';

const STEP_ICONS = [
  <EditOutlined key="1" style={{ fontSize: 20 }} />,
  <SearchOutlined key="2" style={{ fontSize: 20 }} />,
  <FileDoneOutlined key="3" style={{ fontSize: 20 }} />,
  <SafetyCertificateOutlined key="4" style={{ fontSize: 20 }} />,
];

export default function HowItWorks() {
  const [currentStep, setCurrentStep] = useState(0);
  const [isMobile, setIsMobile] = useState(false);

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768);
    };
    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const stepItems = CONTENT.howItWorks.steps.map((st, idx) => ({
    title: (
      <span
        style={{
          fontFamily: 'var(--font-sora)',
          fontWeight: 600,
          fontSize: 15,
          color: currentStep === idx ? '#191B1D' : '#52565A',
        }}
      >
        <span style={{ color: '#DB7A58', marginRight: 6, fontWeight: 700 }}>{st.number}</span>
        {st.title}
      </span>
    ),
    description: (
      <span style={{ fontSize: 13, color: '#52565A', lineHeight: 1.6, display: 'block', maxWidth: 220, marginTop: 4 }}>
        {st.description}
      </span>
    ),
    icon: (
      <span
        style={{
          width: 40,
          height: 40,
          borderRadius: '50%',
          backgroundColor: currentStep === idx ? '#191B1D' : '#EDE9E1',
          color: currentStep === idx ? '#F7F3EB' : '#191B1D',
          display: 'inline-flex',
          alignItems: 'center',
          justifyContent: 'center',
          boxShadow: currentStep === idx ? 'var(--shadow-inset-dark)' : 'none',
          transition: 'all 0.3s ease',
        }}
      >
        {STEP_ICONS[idx]}
      </span>
    ),
  }));

  return (
    <section id="how" className="section-wrapper" style={{ backgroundColor: '#F7F3EB' }} aria-labelledby="how-heading">
      <div className="landing-container">
        {/* Section Header matching TaskAssist */}
        <div style={{ maxWidth: 720, marginBottom: 56 }}>
          <span className="section-eyebrow-ta">{CONTENT.howItWorks.eyebrow}</span>
          <h2 id="how-heading" className="section-title-ta">
            {CONTENT.howItWorks.title}
          </h2>
          <p className="section-subtitle-ta" style={{ marginTop: 14 }}>
            A four-stage deterministic pipeline engineered so that no hallucinated or unverified statement passes to the user.
          </p>
        </div>

        {/* TaskAssist-styled Steps Container */}
        <div
          className="card-glow-hover"
          style={{
            backgroundColor: '#FFFFFF',
            padding: '40px 36px',
            borderRadius: 16,
            border: '1px solid var(--border)',
          }}
        >
          <Steps
            direction={isMobile ? 'vertical' : 'horizontal'}
            current={currentStep}
            onChange={(step) => setCurrentStep(step)}
            items={stepItems}
            style={{ marginBottom: 36 }}
          />

          {/* Interactive Step Detail Card */}
          <div
            style={{
              padding: '24px 28px',
              backgroundColor: '#F7F3EB',
              borderRadius: 10,
              border: '1px solid var(--border)',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              flexWrap: 'wrap',
              gap: 16,
            }}
          >
            <div>
              <div
                style={{
                  fontSize: 11,
                  fontFamily: 'var(--font-sora)',
                  fontWeight: 700,
                  color: '#DB7A58',
                  textTransform: 'uppercase',
                  letterSpacing: '0.1em',
                  marginBottom: 6,
                }}
              >
                PHASE {CONTENT.howItWorks.steps[currentStep].number} IN DETAIL
              </div>
              <h3
                style={{
                  fontFamily: 'var(--font-sora)',
                  fontSize: 18,
                  fontWeight: 600,
                  color: '#191B1D',
                  margin: '0 0 6px 0',
                }}
              >
                {CONTENT.howItWorks.steps[currentStep].title}
              </h3>
              <p style={{ fontSize: 14, color: '#52565A', margin: 0, maxWidth: 640, lineHeight: 1.6 }}>
                {CONTENT.howItWorks.steps[currentStep].description}
              </p>
            </div>

            <div
              style={{
                padding: '6px 14px',
                backgroundColor: '#EDE9E1',
                borderRadius: 9999,
                fontSize: 12,
                color: '#191B1D',
                fontWeight: 600,
                border: '1px solid var(--border)',
              }}
            >
              Strict Verification Gate
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
