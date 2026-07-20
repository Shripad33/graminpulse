"""
GraminPulse backend — FastAPI service.

Exposes the enterprise forecast, risk flag, and alert endpoints
that the dashboard consumes. This is a starter scaffold — wire in
the real ML model outputs from /ml as they become available.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="GraminPulse API", version="0.1.0")

# Allow the local frontend dev server to call this API during the hackathon.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "service": "GraminPulse API"}


@app.get("/enterprises")
def list_enterprises():
    """Return the list of enterprises available for monitoring."""
    # TODO: replace with a real DB query
    return [
        {"id": "ent_001", "name": "Sample SHG - Thrissur", "risk": "green"},
        {"id": "ent_002", "name": "Sample FPO - Kolhapur", "risk": "amber"},
        {"id": "ent_003", "name": "Sample Entrepreneur - Bikaner", "risk": "red"},
    ]


@app.get("/forecast/{enterprise_id}")
def get_forecast(enterprise_id: str):
    """Return the 3-6 month cash flow forecast for one enterprise."""
    # TODO: call the trained model in /ml/models
    return {
        "enterprise_id": enterprise_id,
        "horizon_months": 6,
        "forecast": [],       # list of {month, expected, best_case, stress_case}
        "confidence": None,   # 0-1, based on data completeness
    }


@app.get("/risk/{enterprise_id}")
def get_risk(enterprise_id: str):
    """Return the risk flag + recommended action for one enterprise."""
    return {
        "enterprise_id": enterprise_id,
        "risk_level": None,        # green / amber / red
        "reason": None,            # plain-language explanation
        "recommended_action": None,
    }


@app.get("/alerts")
def get_alerts():
    """Return the prioritized list of enterprises needing attention."""
    return []
