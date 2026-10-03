'use client';

import React, { useState } from 'react';
import Image from 'next/image';
import { useRouter } from 'next/navigation';
import { App } from 'antd';
import {
  CheckOutlined,
  EyeInvisibleOutlined,
  EyeOutlined,
} from '@ant-design/icons';

type UserRole = 'employee' | 'admin';

interface RolePreset {
  role: UserRole;
  label: string;
  email: string;
  password: string;
  designation: string;
}

const ROLE_PRESETS: Record<UserRole, RolePreset> = {
  employee: {
    role: 'employee',
    label: 'Employee',
    email: 'employee@assam.gov.in',
    password: 'Password@2026',
    designation: 'Desk Officer (Pension & ARTPS Scrutiny)',
  },
  admin: {
    role: 'admin',
    label: 'Super Admin',
    email: 'admin@assam.gov.in',
    password: 'Password@2026',
    designation: 'System Registrar & Gazette Custodian',
  },
};

export default function LoginPage() {
  return (
    <App>
      <LoginContent />
    </App>
  );
}

function LoginContent() {
  const router = useRouter();
  const { message } = App.useApp();

  const [selectedRole, setSelectedRole] = useState<UserRole>('employee');
  const [email, setEmail] = useState<string>(ROLE_PRESETS.employee.email);
  const [password, setPassword] = useState<string>(ROLE_PRESETS.employee.password);
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleRoleToggle = (newRole: UserRole) => {
    setSelectedRole(newRole);
    setEmail(ROLE_PRESETS[newRole].email);
    setPassword(ROLE_PRESETS[newRole].password);
  };

  const handleSignIn = () => {
    if (!email.trim() || !password.trim()) {
      message.warning('Please enter your official ID and password.');
      return;
    }

    setLoading(true);
    message.loading({ content: 'Authenticating credentials...', key: 'auth' });

    setTimeout(() => {
      message.success({
        content: `Authenticated successfully as ${ROLE_PRESETS[selectedRole].designation}`,
        key: 'auth',
        duration: 2,
      });
      router.push(`/app/dashboard?role=${selectedRole}`);
    }, 400);
  };

  return (
    <div
      style={{
        minHeight: '100vh',
        backgroundColor: '#16181A', // Neutral dark backdrop matching design
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '32px 20px',
        fontFamily: 'var(--font-inter), -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      }}
      className="signup-page-wrapper"
    >
      {/* Outer Card Container with Inset Padding */}
      <div
        style={{
          maxWidth: 980,
          width: '100%',
          backgroundColor: '#FFFFFF',
          borderRadius: 32,
          padding: 16,
          display: 'flex',
          flexDirection: 'row',
          boxShadow: '0 25px 60px -15px rgba(0, 0, 0, 0.45)',
          minHeight: 560,
          position: 'relative',
        }}
        className="signup-card-container"
      >
        {/* ============================================================== */}
        {/* LEFT COLUMN: CLEAN VIDEO DISPLAY CONTAINER (DESKTOP ONLY)      */}
        {/* ============================================================== */}
        <div
          style={{
            flex: '1 1 50%',
            borderRadius: 24,
            background: 'linear-gradient(145deg, #0A4228 0%, #13633C 50%, #08291A 100%)',
            position: 'relative',
            overflow: 'hidden',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            padding: 32,
            minHeight: 480,
          }}
          className="signup-left-panel"
        >
          {/* Decorative Subtle Grid Pattern */}
          <div
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: '100%',
              backgroundImage: 'radial-gradient(rgba(255, 255, 255, 0.12) 1px, transparent 1px)',
              backgroundSize: '24px 24px',
              opacity: 0.5,
              zIndex: 1,
              pointerEvents: 'none',
            }}
          />

          {/* Ambient Glow */}
          <div
            style={{
              position: 'absolute',
              top: '-15%',
              right: '-15%',
              width: '280px',
              height: '280px',
              borderRadius: '50%',
              background: 'radial-gradient(circle, rgba(16, 185, 129, 0.25) 0%, rgba(10, 66, 40, 0) 70%)',
              zIndex: 1,
              pointerEvents: 'none',
            }}
          />

          {/* Top Brand Seal */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, zIndex: 3, position: 'relative' }}>
            <div
              style={{
                width: 36,
                height: 36,
                borderRadius: '50%',
                backgroundColor: 'rgba(255, 255, 255, 0.15)',
                border: '1px solid rgba(255, 255, 255, 0.25)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                backdropFilter: 'blur(8px)',
              }}
            >
              <Image src="/icon.png" alt="VidhiAI" width={22} height={22} style={{ objectFit: 'contain' }} />
            </div>
            <div style={{ display: 'flex', flexDirection: 'column' }}>
              <span style={{ fontFamily: 'var(--font-sora)', fontWeight: 700, fontSize: 17, letterSpacing: '-0.01em', color: '#FFFFFF' }}>
                VidhiAI
              </span>
            </div>
          </div>
        </div>

        {/* ============================================================== */}
        {/* RIGHT COLUMN: SIGN IN FORM (CLEAN & MINIMAL)                   */}
        {/* ============================================================== */}
        <div
          style={{
            flex: '1 1 50%',
            backgroundColor: '#FFFFFF',
            padding: '40px 48px',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
          }}
          className="signup-right-panel"
        >
          {/* Mobile Brand Header - Displayed on mobile when left panel is hidden */}
          <div className="signup-mobile-brand">
            <div
              style={{
                width: 44,
                height: 44,
                borderRadius: '50%',
                backgroundColor: '#F7F3EB',
                border: '1px solid #ECE7DE',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
              }}
            >
              <Image src="/icon.png" alt="VidhiAI Emblem" width={26} height={26} style={{ objectFit: 'contain' }} />
            </div>
            <div style={{ textAlign: 'center' }}>
              <div style={{ fontFamily: 'var(--font-sora)', fontWeight: 700, fontSize: 18, color: '#191B1D', letterSpacing: '-0.01em' }}>
                VidhiAI
              </div>
            </div>
          </div>

          {/* Header */}
          <div style={{ textAlign: 'center', marginBottom: 24 }}>
            <h1
              style={{
                fontFamily: 'var(--font-sora)',
                fontSize: 26,
                fontWeight: 700,
                color: '#191B1D',
                margin: 0,
                letterSpacing: '-0.02em',
              }}
            >
              Sign In
            </h1>
          </div>

          {/* 2-Button Toggle (Employee & Super Admin) */}
          <div style={{ marginBottom: 24 }}>
            <div
              style={{
                display: 'grid',
                gridTemplateColumns: '1fr 1fr',
                gap: 6,
                backgroundColor: '#F4F5F7',
                padding: 4,
                borderRadius: 14,
                border: '1px solid #ECEEF2',
              }}
            >
              <button
                type="button"
                id="role-toggle-employee"
                onClick={() => handleRoleToggle('employee')}
                style={{
                  padding: '10px 14px',
                  borderRadius: 10,
                  border: 'none',
                  fontSize: 13.5,
                  fontWeight: selectedRole === 'employee' ? 700 : 500,
                  cursor: 'pointer',
                  backgroundColor: selectedRole === 'employee' ? '#191B1D' : 'transparent',
                  color: selectedRole === 'employee' ? '#FFFFFF' : '#52565A',
                  boxShadow: selectedRole === 'employee' ? '0 2px 8px rgba(0, 0, 0, 0.12)' : 'none',
                  transition: 'all 0.2s ease',
                }}
              >
                Employee
              </button>
              <button
                type="button"
                id="role-toggle-admin"
                onClick={() => handleRoleToggle('admin')}
                style={{
                  padding: '10px 14px',
                  borderRadius: 10,
                  border: 'none',
                  fontSize: 13.5,
                  fontWeight: selectedRole === 'admin' ? 700 : 500,
                  cursor: 'pointer',
                  backgroundColor: selectedRole === 'admin' ? '#191B1D' : 'transparent',
                  color: selectedRole === 'admin' ? '#FFFFFF' : '#52565A',
                  boxShadow: selectedRole === 'admin' ? '0 2px 8px rgba(0, 0, 0, 0.12)' : 'none',
                  transition: 'all 0.2s ease',
                }}
              >
                Super Admin
              </button>
            </div>
          </div>

          {/* Form Fields Container */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 18 }}>
            {/* Official ID / Username */}
            <div>
              <label
                htmlFor="signin-id"
                style={{
                  display: 'block',
                  fontSize: 12.5,
                  fontWeight: 600,
                  color: '#191B1D',
                  marginBottom: 6,
                }}
              >
                Official ID
              </label>
              <div
                style={{
                  backgroundColor: '#F8F9FA',
                  border: '1px solid #ECEEF2',
                  borderRadius: 12,
                  padding: '4px 14px',
                  height: 48,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                }}
              >
                <input
                  id="signin-id"
                  type="text"
                  placeholder="name@assam.gov.in"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  style={{
                    border: 'none',
                    backgroundColor: 'transparent',
                    outline: 'none',
                    fontSize: 14,
                    color: '#191B1D',
                    width: '90%',
                    fontFamily: 'inherit',
                  }}
                />
                {/* Verified Checkmark Badge */}
                <div
                  style={{
                    width: 20,
                    height: 20,
                    borderRadius: '50%',
                    backgroundColor: '#D5F5DA',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: '#005824',
                    fontSize: 10.5,
                    flexShrink: 0,
                  }}
                >
                  <CheckOutlined />
                </div>
              </div>
            </div>

            {/* Password */}
            <div>
              <label
                htmlFor="signin-password"
                style={{
                  display: 'block',
                  fontSize: 12.5,
                  fontWeight: 600,
                  color: '#191B1D',
                  marginBottom: 6,
                }}
              >
                Password
              </label>
              <div
                style={{
                  backgroundColor: '#F8F9FA',
                  border: '1px solid #ECEEF2',
                  borderRadius: 12,
                  padding: '4px 14px',
                  height: 48,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                }}
              >
                <input
                  id="signin-password"
                  type={showPassword ? 'text' : 'password'}
                  placeholder="••••••••••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === 'Enter') handleSignIn();
                  }}
                  style={{
                    border: 'none',
                    backgroundColor: 'transparent',
                    outline: 'none',
                    fontSize: 14,
                    color: '#191B1D',
                    width: '90%',
                    fontFamily: 'inherit',
                  }}
                />
                <button
                  type="button"
                  aria-label="Toggle password visibility"
                  onClick={() => setShowPassword(!showPassword)}
                  style={{
                    border: 'none',
                    background: 'transparent',
                    color: '#A1A1AA',
                    cursor: 'pointer',
                    padding: 0,
                    fontSize: 16,
                    display: 'flex',
                    alignItems: 'center',
                  }}
                >
                  {showPassword ? <EyeOutlined /> : <EyeInvisibleOutlined />}
                </button>
              </div>
            </div>

            {/* Primary Action Button */}
            <button
              type="button"
              id="signin-continue-btn"
              onClick={handleSignIn}
              disabled={loading}
              style={{
                width: '100%',
                height: 48,
                backgroundColor: '#005824', // Website theme dark green
                color: '#FFFFFF',
                border: 'none',
                borderRadius: 12,
                fontSize: 14.5,
                fontWeight: 600,
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                marginTop: 8,
                boxShadow: '0 4px 14px rgba(0, 88, 36, 0.25)',
                transition: 'all 0.2s ease',
              }}
              onMouseEnter={(e) => (e.currentTarget.style.backgroundColor = '#00481D')}
              onMouseLeave={(e) => (e.currentTarget.style.backgroundColor = '#005824')}
            >
              {loading ? 'Authenticating...' : 'Sign In'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

