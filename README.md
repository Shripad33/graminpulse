# GraminPulse

**Confidence-Aware Cash Flow Forecasting & Action Recommendation for Rural Micro Enterprises**

Built for the NABARD Hackathon — Global Fintech Fest 2026

Theme: *AI for Rural Finance*
Problem Statement: *AI-Driven Cash Flow Prediction & Risk Flagging System for Rural Micro Enterprises*

---

## Problem

Rural micro-enterprises — Self-Help Groups (SHGs), Farmer Producer Organizations (FPOs), and individual entrepreneurs — largely lack formal credit histories, so lenders and field officers currently monitor their financial health manually. This doesn't scale, and early signs of financial stress are often missed until a liquidity crisis or default has already happened.

Meanwhile, the rapid adoption of digital payments (UPI), along with market intelligence and other proxy indicators, has created a rich data ecosystem reflecting real-time rural economic activity — but this data remains largely underutilised.

## Our Idea

Most cash-flow AI tools assume clean, complete transaction data. Rural India doesn't have that — UPI adoption is uneven and cash-heavy activity persists.

**GraminPulse** forecasts 3–6 month cash flow using whatever data is available for a given enterprise, explicitly states its **confidence level** based on data completeness (rather than presenting false precision), and outputs a **specific recommended action** — not just a risk score — so a field officer with limited time and patchy data still knows exactly what to do next.

| Typical AI Approach | GraminPulse Approach |
|---|---|
| Assumes clean, complete transaction data | Works with sparse, irregular, partial data — and says so |
| Outputs a single opaque risk score | Outputs a specific recommended action, not just a score |
| Confidence in the prediction is never stated | Every forecast carries a transparent confidence level |
| Same model logic for every enterprise | Explains the reasoning behind every flag in plain language |

## How It Works

```
Data Sources (UPI trends, financial records*, market/seasonal signals)
        │   *used only where available — system degrades gracefully
        ▼
Ingestion & Preprocessing
(cleaning, aggregation, feature engineering)
        │
        ├──────────────────────────────┐
        ▼                              ▼
Forecasting Model                Confidence Estimator
(Prophet / XGBoost)              (based on data completeness)
        │                              │
        └──────────────┬───────────────┘
                        ▼
        Risk & Action Recommendation Engine
           (SHAP-based reasoning + rule layer)
                        ▼
                   API Layer (FastAPI)
                        ▼
   Dashboard (enterprise view, forecast chart,
   confidence indicator, recommended action, alerts)
                        ▼
        Field Officer / Institution Admin
```

## Tech Stack

| Layer | Technology | Why |
|---|---|---|
| Frontend | React + Tailwind CSS + Recharts | Fast to build, strong data visualization |
| Backend | FastAPI (Python) | Shares language with the ML layer, auto-generated API docs |
| Database | PostgreSQL (SQLite for local dev) | Simple, relational, easy to prototype with |
| AI/ML | XGBoost / Prophet + SHAP | Fast to train, explainable, no GPU required |
| Synthetic Data | Custom generator (`/data`) | Realistic rural transaction seasonality without needing live API access |
| Deployment | Docker + Render/Vercel | Quick, shareable, demo-ready |

## Repository Structure

```
graminpulse/
├── frontend/          # React dashboard (enterprise view, forecasts, alerts)
├── backend/           # FastAPI service, API routes, DB models
├── ml/                # Forecasting model, risk classifier, training notebooks
│   ├── notebooks/
│   └── models/
├── data/              # Synthetic data generator + sample datasets
│   └── synthetic/
├── .gitignore
└── README.md
```

## Getting Started

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### ML / Data
```bash
cd ml
pip install -r requirements.txt
python notebooks/generate_synthetic_data.py   # produces sample data in /data/synthetic
python notebooks/train_forecast_model.py
```

## Team

- Shripad Dhongadi — Frontend & Product Manager
- Karan N B — Backend & AI/ML

## Roadmap / Future Scope

- Real UPI/financial data integration via India's Account Aggregator (AA) / DEPA framework
- Peer-cluster benchmarking — compare an enterprise against similar regional peers, not just its own history
- Vernacular language + voice interface for field-officer usability
- Direct integration with NABARD's existing loan management systems
