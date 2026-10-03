export type FeatureStatus = 'working' | 'in_progress' | 'planned';

export interface StatusItem {
  id: string;
  title: string;
  category: 'Query & Verification' | 'Governance & Ingestion' | 'Platform & Security';
  status: FeatureStatus;
  description: string;
  phase: string;
}

export interface CapabilityItem {
  title: string;
  description: string;
  status: FeatureStatus;
}

export const CAPABILITIES: CapabilityItem[] = [
  {
    title: 'Explain a rule',
    description: 'Translates formal clause syntax into clear, step-by-step guidance.',
    status: 'in_progress',
  },
  {
    title: 'Compare versions',
    description: 'Highlights amendments, superseded clauses, and effective notification dates.',
    status: 'planned',
  },
  {
    title: 'Build a procedure',
    description: 'Synthesizes sequential checklist requirements across interconnected circulars.',
    status: 'planned',
  },
];

export const STATUS_ITEMS: StatusItem[] = [
  {
    id: 'citations',
    title: 'Ask questions with citations',
    category: 'Query & Verification',
    status: 'in_progress',
    description: 'Prototype citation engine linking drafted answers to extracted document chunks.',
    phase: 'Phase 1 Demo / Phase 2 Backend',
  },
  {
    id: 'evidence-viewer',
    title: 'Evidence viewer & clause highlighter',
    category: 'Query & Verification',
    status: 'working',
    description: 'Direct modal & split-view pane highlighting matching text in sample government documents.',
    phase: 'Phase 1 Prototype',
  },
  {
    id: 'doc-upload',
    title: 'Document upload & OCR parsing',
    category: 'Governance & Ingestion',
    status: 'planned',
    description: 'Gazette and notification PDF ingestion pipeline with table parsing.',
    phase: 'Phase 2',
  },
  {
    id: 'review-workflow',
    title: 'Review/approval workflow',
    category: 'Governance & Ingestion',
    status: 'planned',
    description: 'Two-officer signoff required before documents enter the retrieval index.',
    phase: 'Phase 2',
  },
  {
    id: 'version-tracking',
    title: 'Version & amendment tracking',
    category: 'Governance & Ingestion',
    status: 'planned',
    description: 'Automated lineage linking original acts to subsequent corrigenda and amendments.',
    phase: 'Phase 2',
  },
  {
    id: 'assamese-support',
    title: 'Assamese natural language support',
    category: 'Query & Verification',
    status: 'planned',
    description: 'Bilingual retrieval & generation for Assamese queries against translated circulars.',
    phase: 'Phase 3',
  },
  {
    id: 'audit-log',
    title: 'Immutable audit log',
    category: 'Platform & Security',
    status: 'planned',
    description: 'Cryptographically verifiable record of questions asked, retrieved chunks, and officer actions.',
    phase: 'Phase 3',
  },
  {
    id: 'rbac',
    title: 'Role-based access control (RBAC)',
    category: 'Platform & Security',
    status: 'planned',
    description: 'Granular permissions for department reviewers, verifiers, and public citizens.',
    phase: 'Phase 3',
  },
  {
    id: 'dept-integrations',
    title: 'Department API integrations',
    category: 'Platform & Security',
    status: 'planned',
    description: 'Connectors to state e-office, legislative portals, and gazette archives.',
    phase: 'Phase 3',
  },
];

export const ROADMAP_STAGES = [
  {
    stage: 'NOW',
    title: 'Trusted Knowledge Search',
    description: 'Source-anchored retrieval with refusal on missing citations and clause verification.',
    status: 'Current Focus (Phase 1 & 2)',
  },
  {
    stage: 'NEXT',
    title: 'Knowledge Management Lifecycle',
    description: 'Officer review desk, superseded notification flagging, and OCR gazette intake.',
    status: 'Upcoming (Phase 2)',
  },
  {
    stage: 'THEN',
    title: 'Administrative Procedure Assistant',
    description: 'Multi-document workflow synthesis, cross-department eligibility checklists.',
    status: 'Planned',
  },
  {
    stage: 'VISION',
    title: 'Shared Government Knowledge Layer',
    description: 'State-wide federated knowledge registry with public API and regional language parity.',
    status: 'Long-term',
  },
];
