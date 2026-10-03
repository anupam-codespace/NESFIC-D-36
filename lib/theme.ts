import type { ThemeConfig } from 'antd';

export const designTokens = {
  colors: {
    // TaskAssist exact palette
    background: '#F7F3EB', // Warm cream paper background
    foreground: '#191B1D', // Deep charcoal / slate
    card: '#FFFFFF',
    cardForeground: '#191B1D',
    popover: '#FFFFFF',
    primary: '#191B1D', // Main dark interactive elements
    primaryForeground: '#F7F3EB',
    secondary: '#EFEBE2',
    secondaryForeground: '#191B1D',
    muted: '#EDE9E1',
    mutedForeground: '#52565A', // Elegant slate-grey text
    accent: '#DB7A58', // Signature TaskAssist warm terracotta
    accentForeground: '#FAF8F5',
    accentLight: '#FDF3EE',
    border: '#E7E4DF',
    input: '#E7E4DF',
    ring: '#52565A',

    // Status colors from TaskAssist
    statusSuccessBg: '#D5F5DA',
    statusSuccessFg: '#005824',
    statusWarnBg: '#FFECC1',
    statusWarnFg: '#885800',
    statusErrorBg: '#FFE2DF',
    statusErrorFg: '#B32228',
    statusNeutralBg: '#EAE7E2',
    statusNeutralFg: '#44484C',
  },
  radius: {
    sm: 6,
    md: 8,
    lg: 12,
    xl: 16,
    full: 9999,
  },
  shadows: {
    soft: '0 1px 0 0 rgba(0, 0, 0, 0.04), 0 1px 3px 0 rgba(0, 0, 0, 0.04)',
    card: '0 2px 8px -2px rgba(25, 27, 29, 0.05), 0 1px 3px 0 rgba(25, 27, 29, 0.03)',
    cardHover: '0 0 24px -6px rgba(25, 27, 29, 0.1), 0 8px 24px -4px rgba(25, 27, 29, 0.06)',
    insetDark: 'inset 0 1px 0 0 rgba(255, 255, 255, 0.18), inset 0 -1px 0 0 rgba(0, 0, 0, 0.4), 0 1px 2px 0 rgba(0, 0, 0, 0.2)',
  },
  fonts: {
    heading: 'var(--font-sora), "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
    body: 'var(--font-inter), -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
  },
};

export const antdTheme: ThemeConfig = {
  token: {
    colorPrimary: designTokens.colors.primary,
    borderRadius: designTokens.radius.lg,
    fontFamily: designTokens.fonts.body,
    colorTextHeading: designTokens.colors.foreground,
    colorText: designTokens.colors.foreground,
    colorTextSecondary: designTokens.colors.mutedForeground,
    colorBorder: designTokens.colors.border,
    colorBorderSecondary: designTokens.colors.muted,
    colorBgBase: designTokens.colors.background,
    colorBgContainer: designTokens.colors.card,
    colorBgElevated: designTokens.colors.card,
    colorBgLayout: designTokens.colors.background,
  },
  components: {
    Typography: {
      colorTextHeading: designTokens.colors.foreground,
    },
    Button: {
      controlHeight: 44,
      borderRadius: designTokens.radius.md,
      colorPrimary: designTokens.colors.primary,
    },
    Card: {
      borderRadiusLG: designTokens.radius.xl,
    },
    Tag: {
      borderRadiusSM: 6,
      fontSize: 12,
    },
    Collapse: {
      borderRadiusLG: designTokens.radius.lg,
      contentPadding: '16px 20px',
      headerPadding: '16px 20px',
    },
    Steps: {
      colorPrimary: designTokens.colors.primary,
    },
    Alert: {
      borderRadiusLG: designTokens.radius.md,
    },
  },
};
