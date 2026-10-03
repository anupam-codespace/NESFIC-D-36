'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import {
  Type,
  Accessibility,
  Volume2,
  Globe,
  House,
  ShieldCheck,
  MessageSquareWarning,
  Moon,
  Sun,
  LogIn,
  Menu,
  X,
  BookOpen,
  ArrowRight,
} from 'lucide-react';
import { Drawer, message } from 'antd';

export default function Navbar() {
  const [mobileDrawerOpen, setMobileDrawerOpen] = useState(false);
  const [isDark, setIsDark] = useState(false);
  const [fontSizeLevel, setFontSizeLevel] = useState(100);
  const [lang, setLang] = useState<'EN' | 'AS'>('EN');
  const [isSpeaking, setIsSpeaking] = useState(false);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const hasDark = document.documentElement.classList.contains('dark');
      setIsDark(hasDark);
    }
  }, []);

  const toggleTheme = () => {
    if (typeof document !== 'undefined') {
      const willBeDark = !isDark;
      setIsDark(willBeDark);
      if (willBeDark) {
        document.documentElement.classList.add('dark');
        try {
          localStorage.setItem('theme', 'dark');
        } catch {
          // ignore
        }
      } else {
        document.documentElement.classList.remove('dark');
        try {
          localStorage.setItem('theme', 'light');
        } catch {
          // ignore
        }
      }
    }
  };

  const handleFontSize = (delta: number) => {
    const newLevel = Math.min(125, Math.max(85, fontSizeLevel + delta));
    setFontSizeLevel(newLevel);
    if (typeof document !== 'undefined') {
      document.documentElement.style.fontSize = `${(newLevel / 100) * 16}px`;
    }
  };

  const handleHear = () => {
    if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
      message.info('Speech synthesis is not supported on this browser.');
      return;
    }
    if (isSpeaking) {
      window.speechSynthesis.cancel();
      setIsSpeaking(false);
      return;
    }
    const textToSpeak =
      lang === 'EN'
        ? 'Government of Assam. Trusted Government Knowledge, Rules and Document Assistant. Problem statement forty-six, NESFIC 2026. Joint initiative by Administrative Reforms, Assam Administrative Staff College, Department of Science and Technology, Pension and Public Grievances Department, together with Assam State Space Application Centre.'
        : 'অসম চৰকাৰ। বিশ্বাসযোগ্য চৰকাৰী নিয়ম আৰু নথিপত্ৰ সহায়ক। প্ৰশাসনীয় সংস্কাৰ, অসম প্ৰশাসনীয় পদাধিকাৰী মহাবিদ্যালয়, বিজ্ঞান আৰু প্ৰযুক্তিবিদ্যা বিভাগ, পেঞ্চন আৰু ৰাজহুৱা ওজৰ-আপত্তি বিভাগ আৰু আছাক।';
    const utterance = new SpeechSynthesisUtterance(textToSpeak);
    utterance.rate = 0.95;
    utterance.onend = () => setIsSpeaking(false);
    utterance.onerror = () => setIsSpeaking(false);
    setIsSpeaking(true);
    window.speechSynthesis.speak(utterance);
  };

  const toggleLang = () => {
    const nextLang = lang === 'EN' ? 'AS' : 'EN';
    setLang(nextLang);
    message.success(
      nextLang === 'EN'
        ? 'Language switched to English'
        : 'ভাষা সলনি কৰা হ’ল: অসমীয়া'
    );
  };

  const skipToMain = () => {
    const el = document.getElementById('main-content');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <header className="gov-navbar">
      {/* 1. Top Government Utility Strip */}
      <div className="gov-top-banner">
        <div className="gov-top-banner-inner">
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, minWidth: 0 }}>
            <span style={{ fontWeight: 600, whiteSpace: 'nowrap' }}>Government of Assam</span>
            <span className="gov-show-sm" style={{ opacity: 0.8, whiteSpace: 'nowrap' }}>অসম চৰকাৰ</span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <button
              type="button"
              onClick={skipToMain}
              className="gov-top-btn gov-show-md"
              aria-label="Skip to main content"
            >
              <Type style={{ width: 12, height: 12 }} />
              <span>Skip to main content</span>
            </button>

            <button
              type="button"
              onClick={() => message.info('Screen reader optimization: WCAG 2.1 AAA aria landmarks active.')}
              className="gov-top-btn gov-show-sm"
              aria-label="Screen reader access"
            >
              <Accessibility style={{ width: 12, height: 12 }} />
              <span>Screen Reader</span>
            </button>

            <button
              type="button"
              onClick={() => handleFontSize(-5)}
              className="gov-top-btn"
              aria-label="Decrease text size"
              title="Decrease font size"
            >
              <Type style={{ width: 12, height: 12 }} />
              <span>A-</span>
            </button>

            <button
              type="button"
              onClick={() => handleFontSize(5)}
              className="gov-top-btn"
              aria-label="Increase text size"
              title="Increase font size"
            >
              <Type style={{ width: 14, height: 14 }} />
              <span>A+</span>
            </button>

            <button
              type="button"
              onClick={handleHear}
              className={`gov-top-btn gov-show-sm ${isSpeaking ? 'bg-white/30 text-amber-200' : ''}`}
              aria-label="Hear page description"
              title="Listen to page summary"
            >
              <Volume2 style={{ width: 12, height: 12 }} />
              <span>{isSpeaking ? 'Playing...' : 'Hear'}</span>
            </button>

            <button
              type="button"
              onClick={toggleLang}
              className="gov-top-btn"
              aria-label="Language selector"
              title="Switch English / অসমীয়া"
            >
              <Globe style={{ width: 12, height: 12 }} />
              <span>{lang}</span>
            </button>
          </div>
        </div>
      </div>

      {/* 2. Main Navigation Header */}
      <div className="gov-navbar-inner">
        <Link
          href="/"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 10,
            minWidth: 0,
            flexShrink: 0,
            textDecoration: 'none',
          }}
          aria-label="Go to home page"
        >
          <div style={{ flexShrink: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Image
              src="/emblem/seal-of-assam.png"
              alt="Government of Assam Seal"
              width={36}
              height={36}
              priority
              style={{ objectFit: 'contain', width: 34, height: 34 }}
            />
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', lineHeight: 1.2, minWidth: 0 }}>
            <p style={{ fontWeight: 700, letterSpacing: '-0.02em', fontSize: 14, color: '#0F172A', margin: 0, whiteSpace: 'nowrap' }}>
              Government of Assam
            </p>
            <p
              className="gov-show-md"
              style={{
                fontSize: 10.5,
                color: '#64748B',
                margin: 0,
                overflow: 'hidden',
                textOverflow: 'ellipsis',
                whiteSpace: 'nowrap',
                maxWidth: 320,
              }}
            >
              অসম চৰকাৰ · Administrative Reforms Department
            </p>
          </div>
        </Link>

        {/* Center / Desktop Navigation Links */}
        <nav className="gov-nav-links" aria-label="Main navigation">
          <a href="#hero" className="gov-nav-link">
            <House style={{ width: 14, height: 14, color: '#64748B' }} />
            <span>Home</span>
          </a>
          <a href="#features" className="gov-nav-link">
            <BookOpen style={{ width: 14, height: 14, color: '#64748B' }} />
            <span>What Portal Does</span>
          </a>
          <a href="#roles" className="gov-nav-link">
            <ShieldCheck style={{ width: 14, height: 14, color: '#64748B' }} />
            <span>Tailored Roles</span>
          </a>
          <a href="#transparency" className="gov-nav-link">
            <MessageSquareWarning style={{ width: 14, height: 14, color: '#64748B' }} />
            <span>Public Transparency</span>
          </a>
        </nav>

        {/* Right Action Controls */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 6, flexShrink: 0 }}>
          {/* Theme Toggle Button */}
          <button
            type="button"
            onClick={toggleTheme}
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              justifyContent: 'center',
              height: 32,
              width: 32,
              borderRadius: 6,
              border: '1px solid #E2E8F0',
              backgroundColor: '#FFFFFF',
              color: '#334155',
              cursor: 'pointer',
              flexShrink: 0,
            }}
            aria-label="Toggle color theme"
          >
            {isDark ? <Sun style={{ width: 15, height: 15, color: '#F59E0B' }} /> : <Moon style={{ width: 15, height: 15 }} />}
          </button>

          {/* Primary Sign In Button */}
          <Link
            href="/login"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: 5,
              height: 32,
              padding: '0 10px',
              borderRadius: 6,
              backgroundColor: '#005824',
              color: '#FFFFFF',
              fontSize: 12,
              fontWeight: 600,
              textDecoration: 'none',
              boxShadow: '0 1px 2px rgba(0,0,0,0.05)',
              whiteSpace: 'nowrap',
              flexShrink: 0,
            }}
          >
            <LogIn style={{ width: 13, height: 13 }} />
            <span>Sign in</span>
          </Link>

          {/* Mobile Menu Toggle Button */}
          <button
            type="button"
            onClick={() => setMobileDrawerOpen(true)}
            className="gov-hide-lg"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              justifyContent: 'center',
              height: 32,
              width: 32,
              borderRadius: 6,
              border: '1px solid #E2E8F0',
              backgroundColor: '#FFFFFF',
              color: '#334155',
              cursor: 'pointer',
              flexShrink: 0,
            }}
            aria-label="Open mobile navigation menu"
          >
            <Menu style={{ width: 16, height: 16 }} />
          </button>
        </div>
      </div>

      {/* Mobile Drawer Navigation */}
      <Drawer
        title={
          <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
            <Image
              src="/emblem/seal-of-assam.png"
              alt="Government of Assam Seal"
              width={34}
              height={34}
              style={{ objectFit: 'contain' }}
            />
            <div style={{ display: 'flex', flexDirection: 'column' }}>
              <span style={{ fontWeight: 700, fontSize: 14, color: '#0F172A' }}>Government of Assam</span>
              <span style={{ fontSize: 11, color: '#64748B' }}>Administrative Reforms Department</span>
            </div>
          </div>
        }
        placement="right"
        onClose={() => setMobileDrawerOpen(false)}
        open={mobileDrawerOpen}
        closeIcon={<X style={{ width: 16, height: 16, color: '#475569' }} />}
        styles={{
          body: {
            padding: '20px 16px',
            display: 'flex',
            flexDirection: 'column',
            gap: 16,
            backgroundColor: '#FFFFFF',
          },
        }}
      >
        <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          <p style={{ fontSize: 11, textTransform: 'uppercase', letterSpacing: '0.1em', color: '#94A3B8', fontWeight: 600, margin: '0 0 8px 8px' }}>
            Navigation
          </p>
          <a
            href="#hero"
            onClick={() => setMobileDrawerOpen(false)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '10px 12px',
              borderRadius: 8,
              fontSize: 14,
              fontWeight: 500,
              color: '#1E293B',
              textDecoration: 'none',
            }}
          >
            <House style={{ width: 16, height: 16, color: '#005824' }} />
            <span>Home</span>
          </a>
          <a
            href="#features"
            onClick={() => setMobileDrawerOpen(false)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '10px 12px',
              borderRadius: 8,
              fontSize: 14,
              fontWeight: 500,
              color: '#1E293B',
              textDecoration: 'none',
            }}
          >
            <BookOpen style={{ width: 16, height: 16, color: '#005824' }} />
            <span>What This Portal Does</span>
          </a>
          <a
            href="#roles"
            onClick={() => setMobileDrawerOpen(false)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '10px 12px',
              borderRadius: 8,
              fontSize: 14,
              fontWeight: 500,
              color: '#1E293B',
              textDecoration: 'none',
            }}
          >
            <ShieldCheck style={{ width: 16, height: 16, color: '#005824' }} />
            <span>Tailored To Your Role</span>
          </a>
          <a
            href="#transparency"
            onClick={() => setMobileDrawerOpen(false)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '10px 12px',
              borderRadius: 8,
              fontSize: 14,
              fontWeight: 500,
              color: '#1E293B',
              textDecoration: 'none',
            }}
          >
            <MessageSquareWarning style={{ width: 16, height: 16, color: '#005824' }} />
            <span>Public Transparency</span>
          </a>
          <a
            href="#inquiry"
            onClick={() => setMobileDrawerOpen(false)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 10,
              padding: '10px 12px',
              borderRadius: 8,
              fontSize: 14,
              fontWeight: 500,
              color: '#1E293B',
              textDecoration: 'none',
            }}
          >
            <ArrowRight style={{ width: 16, height: 16, color: '#005824' }} />
            <span>Statutory Inquiry</span>
          </a>
        </div>

        <div style={{ marginTop: 'auto', paddingTop: 16, borderTop: '1px solid #E2E8F0', display: 'flex', flexDirection: 'column', gap: 10 }}>
          <Link
            href="/login"
            onClick={() => setMobileDrawerOpen(false)}
            className="gov-btn-primary"
            style={{ width: '100%', justifyContent: 'center' }}
          >
            <LogIn style={{ width: 16, height: 16 }} />
            <span>Sign in</span>
          </Link>
          <Link
            href="/login"
            onClick={() => setMobileDrawerOpen(false)}
            className="gov-btn-outline"
            style={{ width: '100%', justifyContent: 'center' }}
          >
            <span>Sign in to Access Dashboard</span>
          </Link>
        </div>
      </Drawer>
    </header>
  );
}
