import React from 'react';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'RAAH Prototype Workspace · Dashboard Shell',
  description: 'Evidence-grounded government knowledge assistant prototype workspace.',
};

export default function AppLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
