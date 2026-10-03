# GitHub Student Developer Pack Innovations for VidhiAI

This document outlines how VidhiAI leverages the **GitHub Student Developer Pack** to build, test, automate, and deploy a verified AI knowledge assistant for the Government of Assam (NESFIC 2026 Challenge D-36).

---

## 1. Automated Continuous Integration via GitHub Actions
- **Pack Benefit**: Unlimited private repository runner minutes for student developers.
- **Implementation**: [`.github/workflows/vidhiai-ci.yml`](file:///.github/workflows/vidhiai-ci.yml)
- **Workflow Highlights**:
  1. Cryptographic verification of SHA-256 digests for all 10 Assam Government gazettes in `corpus/manifest.json`.
  2. Automatic SQLite database seeding with 64 extracted statutory chunks.
  3. Execution of pytest suite across 12 verifier and API integration tests.
  4. Execution of the 20-query evaluation benchmark ([`eval/run_eval.py`](file:///eval/run_eval.py)) ensuring 100% accuracy and 0% hallucinations on every commit.
  5. Next.js lint and production build validation.

---

## 2. API Testing with Postman Student License
- **Pack Benefit**: Postman Pro workspace and API test automation for students.
- **Implementation**: [`docs/vidhiai_postman_collection.json`](file:///docs/vidhiai_postman_collection.json)
- **Included Requests**:
  - `GET /api/health` — System status and chunk inventory
  - `GET /api/documents` — Ingested gazettes with cryptographic checksums
  - `POST /api/ask` (Pension - Officer File Noting) — Generates formal administrative noting
  - `POST /api/ask` (ARTPS - Citizen Guide) — Generates plain language checklist & SLA timeline
  - `POST /api/ask` (Basundhara - Land Ceiling) — Retrieves 1-bigha urban ceiling
  - `POST /api/ask` (Safe-Failure Refusal) — Verifies zero-hallucination refusal on out-of-corpus queries
  - `POST /api/documents/{id}/approve` — Administrative approval of pending gazettes
- **How to Use**:
  1. Open Postman.
  2. Click **Import** and select `docs/vidhiai_postman_collection.json`.
  3. Run the collection to verify all 7 endpoints in under 2 seconds.

---

## 3. Production Cloud Hosting ($100-$200 Free Credits)
- **Pack Benefits**:
  - **DigitalOcean**: $100 student credit for Droplets and Managed Databases.
  - **Microsoft Azure**: $100 student credit for Azure App Services and Linux VMs.
  - **Heroku**: Dyno credits for student apps.
- **Implementation**:
  - [`Dockerfile`](file:///Dockerfile): Containerizes the FastAPI knowledge engine with pre-seeded Assam gazettes.
  - [`docker-compose.yml`](file:///docker-compose.yml): Unified container orchestration for Next.js frontend and FastAPI backend.
- **1-Click Deploy on DigitalOcean Droplet**:
  ```bash
  # SSH into your DigitalOcean Droplet
  git clone https://github.com/<your-username>/NESFIC-D-36.git vidhiai
  cd vidhiai
  docker compose up -d --build
  ```

---

## 4. Custom Government Subdomain (Namecheap / .tech / .me)
- **Pack Benefit**: 1 free year of domain registration (.me or .tech) and free SSL certificates.
- **Recommended Subdomain**: `vidhiai.me` or `assam-rules.tech`
- **DNS Setup**:
  - `A` Record: `@` -> Droplet Public IP
  - `CNAME` Record: `www` -> `vidhiai.me`

---

## 5. Mobile-First Optimization Architecture
- **Responsive Workspace**:
  - On desktop (`> 992px`): Side-by-side verification grid (Answer Card + Gazette Sheet).
  - On mobile (`<= 992px`): 1-tap segmented toggle between `Drafting Studio` and `Gazette Proof`, with stacked cards and zero horizontal overflow.
- **Touch Ergonomics**: All buttons, role toggles, and query pills adhere to minimum 44px touch targets.
- **Zero Emojis**: Preserves formal government dignity using vector SVG icons from `@ant-design/icons`.
