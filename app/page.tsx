import React from 'react';
import Navbar from '@/components/landing/Navbar';
import Hero from '@/components/landing/Hero';
import Solution from '@/components/landing/Solution';
import Problem from '@/components/landing/Problem';
import Status from '@/components/landing/Status';
import FinalCta from '@/components/landing/FinalCta';
import Footer from '@/components/landing/Footer';

export default function LandingPage() {
  return (
    <div
      style={{
        minHeight: '100vh',
        display: 'flex',
        flexDirection: 'column',
        backgroundColor: '#FFFFFF',
        color: '#0F172A',
        overflowX: 'hidden',
        width: '100%',
      }}
    >
      {/* 1. Top Government Utility Strip & Official Navbar */}
      <Navbar />

      {/* 2. Main Page Content */}
      <main id="main-content" style={{ flex: '1 0 auto', width: '100%', overflowX: 'hidden' }}>
        {/* Hero Section: Official Emblem, Department Header, Title, CTAs & 6-card KPI Grid */}
        <Hero />

        {/* What This Portal Does: 6 Core Feature Cards */}
        <Solution />

        {/* Tailored To Your Role: State Admin / Desk Officer / Citizen */}
        <Problem />

        {/* Public Transparency: Aggregate Telemetry Benchmarks */}
        <Status />

        {/* Inquiry Callout Banner */}
        <FinalCta />
      </main>

      {/* Official Government of Assam Footer */}
      <Footer />
    </div>
  );
}
