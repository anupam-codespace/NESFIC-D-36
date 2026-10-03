import { CAPABILITIES, ROADMAP_STAGES, STATUS_ITEMS } from './status';

export interface EndorsementItem {
  id: string;
  quote: string;
  author: string;
  designation: string;
  organization: string;
}

export const CONTENT = {
  meta: {
    title: 'Trusted Government Knowledge, Rules & Document Assistant — Government of Assam',
    description:
      'Official AI assistant for verbatim statutory search, multi-department gazette ingestion, OCR scrutiny, and audit-ready secretariat notings across the Government of Assam — built for NESFIC 2026 (Problem Statement 46 · NESFIC-D-36).',
  },
  hero: {
    badge: 'PS No. 46 · NESFIC-D-36 · Trusted Government Knowledge Assistant',
    stateDept: 'Administrative Reforms · AASC · Sci-Tech · Pension & PG · ASSAC',
    eyebrow: 'GOVERNMENT OF ASSAM · NESFIC 2026',
    title: 'Trusted Government Knowledge, Rules & Document Assistant',
    subtitle:
      'A unified, tamper-evident AI intelligence system providing zero-hallucination verbatim citations, multi-department gazette ingestion, OCR scrutiny, and audit-ready secretariat notings across the Government of Assam — built for NESFIC 2026.',
    primaryCta: 'Officer sign-in',
    primaryCtaHref: '/login',
    secondaryCta: 'Query verified rules',
    secondaryCtaAnchor: '/app/dashboard',
    microcopy:
      'Citizens can query public service rules and pension eligibility directly. Officers sign in to access department-scoped desks and audit trails.',
    sampleBadge: 'PS No. 46 · NESFIC-D-36',
    preview: {
      query: 'What is the maximum qualifying service ceiling for pension calculation in Assam?',
      verifiedAnswerTitle: 'VERIFIED STATUTORY ANSWER',
      verifiedAnswerText:
        'Under Rule 41(2) of the Assam Services (Pension) Rules 1969 (Page 28), pension calculation is subject to a statutory ceiling of 33 years qualifying service. A minimum of 20 years entitles the employee to full superannuation pension.',
      sourceChip: 'Assam Pension Rules · Rule 41(2) · Page 28',
      sourceAction: 'View evidence',
    },
  },
  trustStrip: {
    principles: 'VERBATIM-GROUNDED · MULTI-DEPARTMENT OCR · AUDITABLE LEDGER · ZERO HALLUCINATION',
    footnote: 'Official Government of Assam Knowledge Infrastructure',
  },
  problem: {
    eyebrow: 'HOW IT WORKS FOR YOU',
    title: 'Tailored to your role',
    roles: [
      {
        id: 'admin',
        title: 'For State Administrators & AASC',
        points: [
          'Full visibility across every department gazette and circular',
          'Standardize training curricula and administrative rule updates',
          'Tamper-evident cryptographic ledger and aggregate CSV exports',
          'Cryptographic audit trail attributed to every signed-in officer',
        ],
        ctaText: 'Sign in as State Admin',
        ctaHref: '/login',
      },
      {
        id: 'officer',
        title: 'For Department Desk Officers',
        points: [
          'Scoped to Pension, Administrative Reforms, Sci-Tech, or ASSAC',
          'Instant statutory quote lookup to resolve file disputes in minutes',
          'Draft official green-sheet secretariat notings with citations',
          'Secure PDF upload and automated 300 DPI OCR chunking pipeline',
        ],
        ctaText: 'Sign in as Desk Officer',
        ctaHref: '/login',
      },
      {
        id: 'citizen',
        title: 'For Citizens & Pensioners',
        points: [
          'Query pension eligibility, gratuity formulas, and service rules',
          '100% zero misinformation — every response backed by verified PDFs',
          'Direct page references with transparent source drawer viewer',
          'Plain-language Assamese and English procedural explanations',
        ],
        ctaText: 'Ask Public Rules Assistant',
        ctaHref: '/app/dashboard',
      },
    ],
    cards: [
      {
        tag: 'SCATTERED',
        title: 'Fragmented Departmental Archives',
        description:
          'Rules, office memoranda, gazette notifications, and amendments live across siloed PDFs, legacy archives, and departmental desks.',
      },
      {
        tag: 'HARD TO INTERPRET',
        title: 'Complex & Superseded Circulars',
        description:
          'Finding the exact prevailing clause and confirming whether a newer circular has amended or repealed it requires hours of cross-referencing.',
      },
      {
        tag: 'HIGH LIABILITY',
        title: 'Generic AI Hallucinations',
        description:
          'Generic AI produces plausible, fluent answers that it cannot ground or substantiate. In administrative law and public governance, unverified text creates genuine liability.',
      },
    ],
  },
  solution: {
    eyebrow: 'WHAT THIS PORTAL DOES',
    title: 'One platform for statutory intelligence',
    description:
      'Track, query, and verify official administrative knowledge across departments with deterministic source grounding, OCR ingestion, and secretariat notings.',
    cards: [
      {
        key: 'ask',
        step: '01',
        title: 'ASK',
        description:
          'Pose natural-language procedural queries in English or Assamese. The system maps everyday departmental intent directly to statutory provisions.',
      },
      {
        key: 'understand',
        step: '02',
        title: 'UNDERSTAND',
        description:
          'Transforms archaic legal clauses and bureaucratic terminology into clear, sequential action steps without distorting legal obligations.',
        statusNote: 'Deterministic summarization grounded in retrieved text',
      },
      {
        key: 'verify',
        step: '03',
        title: 'VERIFY',
        description:
          'Inspect the exact circular number, issuing date, section number, and physical page cited for every statement. Nothing is accepted on faith.',
        statusNote: '100% Citation traceability required for generation',
      },
    ],
    capabilities: CAPABILITIES,
  },
  howItWorks: {
    eyebrow: 'WORKFLOW & VERIFICATION PIPELINE',
    title: 'From question to verified answer.',
    steps: [
      {
        number: '01',
        title: 'ASK',
        description: 'Type your question in plain language without needing legal section references.',
      },
      {
        number: '02',
        title: 'RETRIEVE',
        description:
          'VidhiAI searches only approved documents in the active index using hybrid keyword (BM25) and semantic vector matching.',
      },
      {
        number: '03',
        title: 'ANSWER',
        description:
          'AI synthesizes an answer using strictly the retrieved evidence fragments. Unsupported extrapolation is forbidden.',
      },
      {
        number: '04',
        title: 'VERIFY',
        description:
          'Inspect the source document, section, and page side-by-side. If evidence is missing, the response is blocked.',
      },
    ],
  },
  showcase: {
    eyebrow: 'EVIDENCE-GROUNDED INFERENCE VS SAFE FAILURE',
    title: 'AI that shows its work. And knows when to stop.',
    caption:
      'VidhiAI prefers an incomplete verified answer over a confident unsupported one.',
    verifiedCard: {
      tag: 'Official Assam Rules',
      query: 'What documents are required for pension processing under Section 7.2?',
      ruleName: 'Assam Services (Pension) Rules, 1969',
      section: 'Section 7.2 — Submission of Formal Documents',
      page: 'Page 28 · Rule 41(2)',
      highlightedText:
        'Clause 7.2(b): Every retiring employee shall submit Form 7 alongside an up-to-date No Demand Certificate issued by the Directorate of Estates, accompanied by two attested passport photographs.',
      aiAnswer:
        'Under Section 7.2(b), the applicant must furnish: (1) Form 7 (Service Verification Certificate), (2) No Demand Certificate from the Estate Directorate, and (3) Two attested photographs certified by the Head of Office.',
    },
    safeFailureCard: {
      badge: 'NO VERIFIED SOURCE FOUND',
      title: 'Safe Refusal Mechanism',
      query: 'Can a contractual employee claim LTC entitlement after 6 months?',
      text: "We couldn't find an authoritative document supporting this question in the current knowledge base.",
      reasoning:
        'Because no approved circular or rule in the repository explicitly defines LTC entitlement for contractual staff under 6 months, VidhiAI refuses to extrapolate or synthesize an unverified claim.',
      buttons: {
        search: 'Search knowledge',
        submit: 'Submit for review',
      },
    },
  },
  governance: {
    eyebrow: 'DOCUMENT GOVERNANCE & CONTROL',
    title: 'AI answers. Government controls the knowledge.',
    description:
      'Uploading a document does not make it trusted. Only reviewed, approved, version-tracked documents become answerable. Superseded versions are flagged, not served.',
    lifecycle: [
      { step: '01', title: 'Upload', desc: 'Secure PDF/gazette intake via authenticated departmental desk.' },
      { step: '02', title: 'Process', desc: 'OCR verification, structural chunking & statutory metadata tagging.' },
      { step: '03', title: 'Review', desc: 'Authorized nodal officer reviews extracted clauses & lineage.' },
      { step: '04', title: 'Approve', desc: 'Cryptographic digital signature locks document authenticity.' },
      { step: '05', title: 'Publish', desc: 'Incorporated into the active vector retrieval catalog.' },
      { step: '06', title: 'Trusted Knowledge', desc: 'Searchable by citizen & officer query interfaces.' },
    ],
    principles: [
      {
        title: 'Source-grounded',
        desc: 'Zero generation without direct quotation anchors from approved official notifications.',
      },
      {
        title: 'Controlled',
        desc: 'Department administrators hold complete authority over which circulars are active, updated, or archived.',
      },
      {
        title: 'Traceable',
        desc: 'Every generated word maps directly back to an authentic clause, gazette issue, and page timestamp.',
      },
    ],
  },
  status: {
    eyebrow: 'OFFICIAL CAPABILITIES & BENCHMARKS',
    title: "What works today, and what's next.",
    subtitle:
      'Strict adherence to honest prototype guidelines. No synthetic claims or placeholder metrics.',
    items: STATUS_ITEMS,
    roadmapTitle: 'Roadmap, not yet built',
    roadmap: ROADMAP_STAGES,
  },
  faq: {
    eyebrow: 'CLARIFICATIONS & ARCHITECTURE',
    title: 'Frequently asked questions',
    items: [
      {
        key: '1',
        question: 'Is this just ChatGPT with a government skin?',
        answer:
          'No. Generic conversational bots synthesize text from broad internet training without verifiable boundaries. VidhiAI answers only from approved documents retrieved in real-time, displays explicit statutory citations for every claim, and halts execution when no source exists in the knowledge base.',
      },
      {
        key: '2',
        question: "What happens if the answer isn't in the documents?",
        answer:
          'It says "No verified source found" and prompts the user to either widen the search or submit the question to departmental officers for formal review. It does not speculate, approximate, or hallucinate.',
      },
      {
        key: '3',
        question: 'Which documents does it use?',
        answer:
          'Only documents explicitly verified, approved, and indexed in the knowledge base. This prototype operates exclusively on sample government documents clearly tagged as illustrative.',
      },
      {
        key: '4',
        question: 'Is this an official government product?',
        answer:
          'No. It is an engineering prototype designed and built for trusted government knowledge, rules and document assistance.',
      },
      {
        key: '5',
        question: 'Where does the data live?',
        answer:
          'VidhiAI is architected for on-premise government cloud or sovereign data center deployment (NIC/MeitY certified environments). In this prototype stage, mock data is bundled locally without third-party telemetries.',
      },
      {
        key: '6',
        question: 'Does it support Assamese?',
        answer:
          'Assamese natural language processing and bilingual retrieval is currently in the Planned phase of our development roadmap. The foundational tokenization pipeline is designed to support Assamese script alongside English.',
      },
      {
        key: '7',
        question: 'How does it handle outdated rules?',
        answer:
          'Documents carry strict effective dates, issuing authorities, and amendment statuses. When a subsequent circular or amendment is ingested, earlier conflicting provisions are flagged as superseded and prevented from being cited as current law.',
      },
    ],
  },
  finalCta: {
    title: 'Have a question on official Assam rules or gazettes?',
    subtitle:
      'Access verified service rules, pension regulations, AASC executive guidelines, and science & technology department circulars with 100% verbatim accuracy.',
    primaryButton: 'Ask Government Assistant',
    primaryButtonHref: '/app/dashboard',
    secondaryLink: 'Officer Sign-in',
    secondaryLinkAnchor: '/login',
    badge: 'NESFIC 2026 · Problem Statement 46',
  },
  footer: {
    brand: 'Government of Assam',
    tagline:
      'Administrative Reforms · Assam Administrative Staff College (AASC) · Department of Science & Technology · Pension & Public Grievances Department together with Assam State Space Application Centre (ASSAC)',
    challengeTag: 'North East Seva First Innovation Challenge 2026 (NESFIC 2026) · Seva Sankalp Abhiyan',
    problemStatement: 'PS No. 46 · NESFIC-D-36 · Trusted Government Knowledge, Rules & Document Assistant',
    competition: 'NESFIC 2026',
    disclaimer: 'Official Prototype developed under Seva Sankalp Abhiyan for the Government of Assam.',
    links: [
      { label: 'Home', href: '/' },
      { label: 'Ask Assistant', href: '/app/dashboard' },
      { label: 'Officer Sign-in', href: '/login' },
      { label: 'Role Scopes', href: '#roles' },
      { label: 'What This Portal Does', href: '#features' },
      { label: 'Transparency Benchmarks', href: '#transparency' },
    ],
  },
  // Strictly empty array per non-negotiable honesty rules:
  endorsements: [] as EndorsementItem[],
};
