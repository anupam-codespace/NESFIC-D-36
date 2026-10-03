'use client';

import React, { useState } from 'react';
import { Row, Col, Button, Alert, Space, Modal } from 'antd';
import {
  FileTextOutlined,
  StopOutlined,
  SearchOutlined,
  FormOutlined,
  SafetyCertificateFilled,
  InfoCircleOutlined,
  CheckCircleFilled,
} from '@ant-design/icons';
import { motion, useReducedMotion } from 'framer-motion';
import { CONTENT } from '@/lib/content';

export default function Showcase() {
  const shouldReduceMotion = useReducedMotion();
  const [reviewSubmitted, setReviewSubmitted] = useState(false);
  const [searchKnowledgeModal, setSearchKnowledgeModal] = useState(false);

  return (
    <section
      className="section-wrapper"
      style={{
        backgroundColor: '#EDE9E1',
        borderTop: '1px solid var(--border)',
        borderBottom: '1px solid var(--border)',
      }}
      aria-labelledby="showcase-heading"
    >
      <div className="landing-container">
        {/* Section Header */}
        <div style={{ maxWidth: 760, marginBottom: 48 }}>
          <span className="section-eyebrow-ta">{CONTENT.showcase.eyebrow}</span>
          <h2 id="showcase-heading" className="section-title-ta">
            {CONTENT.showcase.title}
          </h2>
          <p className="section-subtitle-ta" style={{ marginTop: 14 }}>
            {CONTENT.showcase.caption}
          </p>
        </div>

        {/* Two-Column Comparison */}
        <Row gutter={[28, 28]}>
          {/* Column 1: Evidence Panel Open (Verified Path) */}
          <Col xs={24} lg={12}>
            <motion.div
              initial={{ opacity: 0, x: shouldReduceMotion ? 0 : -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, margin: '-50px' }}
              transition={{ duration: 0.6 }}
              style={{ height: '100%' }}
            >
              <div
                className="card-glow-hover"
                style={{
                  backgroundColor: '#FFFFFF',
                  borderRadius: 16,
                  border: '1px solid var(--border)',
                  padding: 28,
                  height: '100%',
                  display: 'flex',
                  flexDirection: 'column',
                }}
              >
                {/* Header */}
                <div
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    paddingBottom: 16,
                    borderBottom: '1px solid var(--border)',
                    marginBottom: 18,
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <CheckCircleFilled style={{ color: '#005824', fontSize: 18 }} />
                    <span
                      style={{
                        fontFamily: 'var(--font-sora)',
                        fontWeight: 600,
                        fontSize: 15,
                        color: '#191B1D',
                      }}
                    >
                      Case A: Grounded Answer with Evidence
                    </span>
                  </div>
                  <span
                    style={{
                      fontSize: 11,
                      padding: '2px 8px',
                      backgroundColor: '#FFFBEB',
                      color: '#92400E',
                      borderRadius: 6,
                      border: '1px solid #FDE68A',
                      fontWeight: 500,
                    }}
                  >
                    {CONTENT.showcase.verifiedCard.tag}
                  </span>
                </div>

                {/* Question */}
                <div
                  style={{
                    backgroundColor: '#F7F3EB',
                    borderRadius: 8,
                    padding: '12px 16px',
                    border: '1px solid var(--border)',
                    marginBottom: 16,
                  }}
                >
                  <div style={{ fontSize: 11, color: '#52565A', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                    User Query
                  </div>
                  <div style={{ fontSize: 14, color: '#191B1D', fontWeight: 600, marginTop: 4 }}>
                    {CONTENT.showcase.verifiedCard.query}
                  </div>
                </div>

                {/* AI Synthesized Answer */}
                <div
                  style={{
                    backgroundColor: '#D5F5DA',
                    borderRadius: 10,
                    border: '1px solid #A7F3D0',
                    padding: '14px 16px',
                    marginBottom: 18,
                  }}
                >
                  <div
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 6,
                      fontSize: 11,
                      fontWeight: 700,
                      color: '#005824',
                      letterSpacing: '0.06em',
                      marginBottom: 6,
                      fontFamily: 'var(--font-sora)',
                    }}
                  >
                    <SafetyCertificateFilled style={{ color: '#005824' }} /> VERIFIED RESPONSE
                  </div>
                  <p style={{ margin: 0, fontSize: 13.5, lineHeight: 1.6, color: '#005824' }}>
                    {CONTENT.showcase.verifiedCard.aiAnswer}
                  </p>
                </div>

                {/* Evidence Panel (Excerpt with Highlighted Clause) */}
                <div
                  style={{
                    backgroundColor: '#191B1D',
                    borderRadius: 10,
                    padding: 18,
                    color: '#F7F3EB',
                    flex: 1,
                    display: 'flex',
                    flexDirection: 'column',
                    boxShadow: 'var(--shadow-inset-dark)',
                  }}
                >
                  <div
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      marginBottom: 10,
                      borderBottom: '1px solid rgba(255, 255, 255, 0.12)',
                      paddingBottom: 8,
                      flexWrap: 'wrap',
                      gap: 6,
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                      <FileTextOutlined style={{ color: '#DB7A58' }} />
                      <span style={{ fontSize: 12, fontWeight: 600, color: '#F7F3EB' }}>
                        {CONTENT.showcase.verifiedCard.ruleName}
                      </span>
                    </div>
                    <span style={{ fontSize: 11, color: '#A1A1AA' }}>
                      {CONTENT.showcase.verifiedCard.page}
                    </span>
                  </div>

                  <div style={{ fontSize: 11, color: '#DB7A58', marginBottom: 6, fontFamily: 'monospace' }}>
                    {CONTENT.showcase.verifiedCard.section}
                  </div>

                  {/* Highlighted text block */}
                  <div
                    style={{
                      backgroundColor: 'rgba(219, 122, 88, 0.18)',
                      borderLeft: '3px solid #DB7A58',
                      padding: '10px 12px',
                      borderRadius: 4,
                      fontSize: 12.5,
                      lineHeight: 1.6,
                      color: '#FAF8F5',
                      fontFamily: 'monospace',
                      marginTop: 4,
                    }}
                  >
                    {CONTENT.showcase.verifiedCard.highlightedText}
                  </div>

                  <div
                    style={{
                      marginTop: 'auto',
                      paddingTop: 12,
                      fontSize: 11,
                      color: '#A1A1AA',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                    }}
                  >
                    <span>Exact paragraph provenance verified</span>
                    <span style={{ color: '#86EFAC', fontWeight: 600 }}>SHA-256 Validated</span>
                  </div>
                </div>
              </div>
            </motion.div>
          </Col>

          {/* Column 2: Safe Failure (Refusal when no source exists) */}
          <Col xs={24} lg={12}>
            <motion.div
              initial={{ opacity: 0, x: shouldReduceMotion ? 0 : 20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true, margin: '-50px' }}
              transition={{ duration: 0.6 }}
              style={{ height: '100%' }}
            >
              <div
                className="card-glow-hover"
                style={{
                  backgroundColor: '#FFFFFF',
                  borderRadius: 16,
                  border: '1px solid var(--border)',
                  padding: 28,
                  height: '100%',
                  display: 'flex',
                  flexDirection: 'column',
                }}
              >
                {/* Header */}
                <div
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    paddingBottom: 16,
                    borderBottom: '1px solid var(--border)',
                    marginBottom: 18,
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <StopOutlined style={{ color: '#B32228', fontSize: 18 }} />
                    <span
                      style={{
                        fontFamily: 'var(--font-sora)',
                        fontWeight: 600,
                        fontSize: 15,
                        color: '#191B1D',
                      }}
                    >
                      Case B: Safe Refusal &amp; Boundary Enforcement
                    </span>
                  </div>
                  <span
                    style={{
                      fontSize: 11,
                      padding: '2px 8px',
                      backgroundColor: '#FFE2DF',
                      color: '#B32228',
                      borderRadius: 6,
                      border: '1px solid #FECACA',
                      fontWeight: 700,
                    }}
                  >
                    {CONTENT.showcase.safeFailureCard.badge}
                  </span>
                </div>

                {/* Question */}
                <div
                  style={{
                    backgroundColor: '#F7F3EB',
                    borderRadius: 8,
                    padding: '12px 16px',
                    border: '1px solid var(--border)',
                    marginBottom: 16,
                  }}
                >
                  <div style={{ fontSize: 11, color: '#52565A', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                    Unsupported Query
                  </div>
                  <div style={{ fontSize: 14, color: '#191B1D', fontWeight: 600, marginTop: 4 }}>
                    {CONTENT.showcase.safeFailureCard.query}
                  </div>
                </div>

                {/* Safe Failure Alert Card with TaskAssist Status Error Colors */}
                <div
                  style={{
                    backgroundColor: '#FFE2DF',
                    border: '1px solid #FECACA',
                    borderRadius: 10,
                    padding: 18,
                    marginBottom: 16,
                  }}
                >
                  <div
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: 8,
                      color: '#B32228',
                      fontFamily: 'var(--font-sora)',
                      fontWeight: 700,
                      fontSize: 12,
                      letterSpacing: '0.08em',
                      marginBottom: 8,
                    }}
                  >
                    <InfoCircleOutlined /> ZERO HALLUCINATION SHIELD ENGAGED
                  </div>
                  <p
                    style={{
                      fontSize: 14,
                      lineHeight: 1.6,
                      color: '#7F1D1D',
                      margin: '0 0 10px 0',
                    }}
                  >
                    {CONTENT.showcase.safeFailureCard.text}
                  </p>
                  <p
                    style={{
                      fontSize: 12.5,
                      lineHeight: 1.55,
                      color: '#991B1B',
                      margin: 0,
                    }}
                  >
                    {CONTENT.showcase.safeFailureCard.reasoning}
                  </p>
                </div>

                {/* Controlled Next Actions */}
                <div
                  style={{
                    backgroundColor: '#F7F3EB',
                    borderRadius: 10,
                    padding: 16,
                    border: '1px solid var(--border)',
                    marginTop: 'auto',
                  }}
                >
                  <div style={{ fontSize: 12, fontWeight: 600, color: '#191B1D', marginBottom: 12 }}>
                    Authoritative Officer Actions Available:
                  </div>

                  <Space size="middle" wrap>
                    <Button
                      icon={<SearchOutlined />}
                      onClick={() => setSearchKnowledgeModal(true)}
                      className="btn-card-outline"
                      style={{ borderRadius: 8, height: 38 }}
                    >
                      {CONTENT.showcase.safeFailureCard.buttons.search}
                    </Button>

                    <Button
                      icon={<FormOutlined />}
                      onClick={() => setReviewSubmitted(true)}
                      disabled={reviewSubmitted}
                      className="btn-dark-inset"
                      style={{ borderRadius: 8, height: 38 }}
                    >
                      {reviewSubmitted ? 'Submitted for Review' : CONTENT.showcase.safeFailureCard.buttons.submit}
                    </Button>
                  </Space>

                  {reviewSubmitted && (
                    <div style={{ marginTop: 10, fontSize: 12, color: '#005824', fontWeight: 500, display: 'flex', alignItems: 'center', gap: 6 }}>
                      <CheckCircleFilled style={{ color: '#005824' }} />
                      <span>Question queued for departmental nodal officer review and gazette ingestion.</span>
                    </div>
                  )}
                </div>
              </div>
            </motion.div>
          </Col>
        </Row>
      </div>

      {/* Search Knowledge Dialog */}
      <Modal
        title={
          <span style={{ fontFamily: 'var(--font-sora)', fontWeight: 600, color: '#191B1D' }}>
            Search Active Government Knowledge Base
          </span>
        }
        open={searchKnowledgeModal}
        onCancel={() => setSearchKnowledgeModal(false)}
        footer={[
          <Button key="close" onClick={() => setSearchKnowledgeModal(false)} className="btn-dark-inset" style={{ height: 36, borderRadius: 8 }}>
            Close
          </Button>,
        ]}
      >
        <p style={{ fontSize: 14, color: '#52565A', lineHeight: 1.6 }}>
          In the full deployment, this opens the semantic catalog covering all indexed Acts, circulars,
          and Gazettes for manual keyword matching and cross-department queries.
        </p>
        <Alert
          type="info"
          showIcon
          message="Prototype Scope"
          description="In this Phase 1 prototype, retrieval is constrained to approved sample demonstration documents."
          style={{ backgroundColor: '#F7F3EB', border: '1px solid var(--border)' }}
        />
      </Modal>
    </section>
  );
}
