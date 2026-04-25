# PhishGuard — Quick Reference Guide

## 🎯 Project at a Glance

**Name:** PhishGuard (formerly SafeNetAI)  
**Type:** Full-stack cybersecurity platform for phishing/scam detection  
**Stage:** Advanced prototype, production-ready with enhancements  
**Stack:** Next.js 15, FastAPI (Python), PostgreSQL, Scikit-Learn, Chrome Extension  

---

## 🏗️ Component Map

```
safenetai7/
├── email/                    ← Gmail Pub/Sub ingestion + pipeline
│   ├── main.py              ← FastAPI webhook listener
│   ├── config.py            ← Environment variable registry
│   ├── gmail_client.py      ← OAuth + Gmail API
│   ├── label_manager.py     ← Apply Gmail labels
│   └── pipeline/            ← Multi-stage analysis
│       ├── orchestrator.py  ← Main coordinator
│       ├── email_parser.py  ← MIME parsing
│       ├── l1_authentication.py
│       ├── l2_heuristics.py
│       ├── l2_nlp.py
│       ├── l3_threat_intel.py
│       ├── scoring.py       ← SCL aggregation
│       └── mcp_client.py    ← VirusTotal integration
│
├── mlmodel/                  ← ML classification API
│   ├── app/main.py          ← FastAPI router setup
│   ├── app/routers/         ← Email/link/doc/offer/unified scanners
│   ├── app/models/          ← Pre-trained .pkl files
│   └── train/               ← Model training scripts
│
├── safenetai/               ← Next.js dashboard + tRPC backend
│   ├── src/app/             ← Next.js pages (dashboard, auth)
│   ├── src/server/api/      ← tRPC routers (scan, report, admin, auth)
│   ├── src/components/      ← React components
│   ├── prisma/              ← Database schema + ORM
│   └── extension/           ← Chrome extension source
│
├── whatsapp-bot/            ← Twilio message scanning
│
└── ARCHITECTURE_ANALYSIS.md ← This document
```

---

## 🔄 Key Flows

### 1. Real-Time Email Scanning (Gmail Pub/Sub)

```
User receives email in Gmail
    ↓
Google Cloud Pub/Sub publishes message
    ↓
POST /webhook/gmail (FastAPI)
    ↓
Fetch raw MIME from Gmail API
    ↓
run_pipeline():
  1. Parse MIME → EmailContext
  2. Check authentication → L1 score (0–4)
  3. Check heuristics → L2H score (0–4)
  4. Check NLP classifier → L2N score (0–3)
  5. Check VirusTotal → L3 score (0–5) [ASYNC]
  6. Aggregate & verdict → SCL 0–10
    ↓
Apply Gmail label (CLEAN/SUSPICIOUS/PHISHING)
    ↓
Broadcast to dashboard via SSE
    ↓
HTTP 200 ✓ (always, even on error)
```

### 2. On-Demand Scan (Web UI / Extension)

```
User submits text/URL/file
    ↓
tRPC: trpc.scan.submit.mutate(input)
    ↓
POST /scan/{type} (FastAPI ML backend)
    ↓
Load model (email/link/doc/offer/unified)
    ↓
Extract features → predict
    ↓
Return risk score + explanation
    ↓
Prisma: create Scan record
    ↓
Display in UI
```

### 3. Report Submission

```
User clicks "Report Scam"
    ↓
Fill form (title, type, evidence)
    ↓
tRPC: trpc.report.create.mutate(input)
    ↓
Create Report record (status=pending)
    ↓
Store evidence in FileUpload
    ↓
Admin dashboard notified
    ↓
Admin approves/rejects → public feed
```

---

## 📊 Scoring System (Spam Confidence Level)

| Stage | Contribution | Score Range |
|-------|--------------|-------------|
| L1 Authentication | SPF/DKIM/DMARC/spoofing | 0–4 |
| L2 Heuristics | Urgency, credentials, payment | 0–4 |
| L2 NLP | TF-IDF + LogRegression | 0–3 |
| L3 Threat Intel | VirusTotal + URL/domain checks | 0–5 |
| **Total (capped)** | | **0–10** |

**Verdict Mapping:**
- **0–3:** CLEAN (no action)
- **4–6:** SUSPICIOUS (label + notify)
- **7–8:** LIKELY_PHISH (label + log)
- **9–10:** PHISH (label + move to SPAM)

---

## 🔐 Technology Decisions & Why

| Decision | Why | Trade-offs |
|----------|-----|-----------|
| **tRPC for API** | Type-safe end-to-end, zero contract drift | Learning curve, requires TypeScript |
| **Prisma ORM** | Type-safe queries, auto migrations, strong DX | SQL performance harder to tune |
| **FastAPI** | Async ASGI, auto OpenAPI docs, fast | Python-only ecosystem |
| **Scikit-Learn** | Mature, well-documented, production-grade | CPU-bound (but models are small) |
| **Gmail Pub/Sub** | Real-time push, no polling overhead | Requires Google Cloud setup |
| **Render + Vercel** | Serverless, pay-per-use, auto-scaling | Vendor lock-in, cold starts possible |

---

## 🚨 Critical Design Principles

1. **Never-Failing Pipeline**
   - Webhook MUST return HTTP 200, even on error
   - Pub/Sub redelivery storms = disaster
   - Solution: Try-catch in orchestrator, return CLEAN verdict on exception

2. **Async-First**
   - L3 VirusTotal checks run concurrently with `asyncio.gather()`
   - Better throughput, don't block on external APIs

3. **Graceful Degradation**
   - If VirusTotal down: Use L1–L2 scores (still effective)
   - If NLP model missing: Use L1, L2H, L3 scores
   - Result: Degraded but functional system

4. **Type Safety Throughout**
   - Frontend ↔ Backend: tRPC (zero runtime surprises)
   - Database: Prisma (generated, type-checked)
   - ML inputs/outputs: Pydantic (validated schemas)

5. **Separation of Concerns**
   - Each pipeline stage is independent (testable, replaceable)
   - Email parser ≠ scorer ≠ label applier
   - Makes code maintainable and modular

---

## 📁 Key File Locations

| File | Purpose |
|------|---------|
| `email/config.py` | Central config registry (env vars) |
| `email/pipeline/orchestrator.py` | Master pipeline coordinator |
| `email/pipeline/scoring.py` | SCL aggregation + verdict |
| `mlmodel/app/main.py` | ML API router setup |
| `mlmodel/app/routers/email_scan.py` | Email + offer classification |
| `safenetai/src/server/api/root.ts` | tRPC router aggregator |
| `safenetai/src/server/api/routers/scan.ts` | Scan submission logic |
| `safenetai/prisma/schema.prisma` | Data models (User, Scan, Report) |
| `safenetai/src/app/dashboard/page.tsx` | Main dashboard UI |
| `safenetai/extension-build/content-gmail.js` | Gmail content script |

---

## 🔌 External Dependencies

| Service | Purpose | Critical? | Fallback |
|---------|---------|-----------|----------|
| Gmail API | Email ingestion | ✅ Yes | Manual upload (lower priority) |
| Google Pub/Sub | Real-time push | ✅ Yes | Polling (slower) |
| VirusTotal API | Threat intel (L3) | ❌ No | L1–L2 scores sufficient |
| Supabase | Data storage | ✅ Yes | Local SQLite (dev only) |
| Render | ML backend hosting | ✅ Yes | Alternative container platform |
| Vercel | Frontend hosting | ✅ Yes | Alternative (Netlify, etc.) |

---

## 🐛 Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Pub/Sub not receiving messages | Gmail watch not registered | Call `register_watch()` on startup |
| Models not loading | Path incorrect | Check `NLP_MODEL_DIR` in config.py |
| tRPC calls return 404 | Missing router in `root.ts` | Register new router in aggregator |
| Prisma type mismatch | Schema changed, client not regenerated | Run `prisma generate` or `postinstall` |
| Extension not detecting emails | Content script not injected | Check manifest permissions + refresh page |
| High latency on scans | VirusTotal rate limit hit | Cache results, add exponential backoff |

---

## 📈 Metrics to Monitor

1. **Email Pipeline**
   - Messages processed per minute
   - Pipeline latency (L1–L6)
   - Error rate (should be <1%)
   - Pub/Sub lag (subscription age)

2. **ML Models**
   - Average confidence per stage
   - False positive / false negative rate
   - Model prediction latency
   - Memory usage (model size)

3. **API Health**
   - tRPC endpoint latency
   - Database connection pool usage
   - VirusTotal API quota remaining
   - Uptime (target: 99.9%)

4. **User Activity**
   - Scans per day
   - Reports submitted
   - Admin approvals vs rejections
   - User engagement (dashboard views)

---

## 🚀 Quick Start (Dev Environment)

```bash
# Email service
cd email
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload

# ML backend
cd mlmodel
pip install -r requirements.txt
python -m uvicorn app.main:app --reload

# Frontend
cd safenetai
npm install
npm run dev  # http://localhost:3000

# Set .env vars in each service before running
```

---

## 📞 Getting Help

- **Architecture questions:** See [ARCHITECTURE_ANALYSIS.md](./ARCHITECTURE_ANALYSIS.md)
- **Email service:** Check `email/README.md`
- **ML models:** See `mlmodel/datasets/` for training data
- **Frontend:** Read `safenetai/README.md`
- **Extension:** Check `safenetai/extension/manifest.json`

---

## 🎓 Learning Resources by Role

### For Backend Engineers
- Learn `pipeline/orchestrator.py` → understand multi-stage design
- Explore `email/l3_threat_intel.py` → async + MCP patterns
- Study `mlmodel/app/routers/` → FastAPI REST design

### For Frontend Engineers
- Explore `safenetai/src/server/api/` → tRPC architecture
- Study `src/components/` → React component structure
- Review `prisma/schema.prisma` → data model design

### For ML Engineers
- Explore `mlmodel/train/` → model training pipeline
- Check `mlmodel/datasets/` → training data
- Review `pipeline/l2_nlp.py` → feature engineering

### For DevOps Engineers
- Review Render + Vercel deployment configs
- Check `mlmodel/Dockerfile` → containerization
- Study `.env` handling → secrets management

---

Last updated: April 25, 2026
