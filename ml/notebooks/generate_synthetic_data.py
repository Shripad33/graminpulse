"""
Generates realistic synthetic UPI/transaction data for rural micro-enterprises,
since live UPI/NPCI data isn't accessible during the hackathon.

Simulates:
- Seasonal cycles (agricultural calendar, festivals)
- Irregular / sparse transaction history (some enterprises have gaps)
- A mix of enterprise types (SHG, FPO, individual entrepreneur)

Output: CSV files in /data/synthetic/
"""

import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "data" / "synthetic"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

ENTERPRISE_TYPES = ["SHG", "FPO", "Individual"]
NUM_ENTERPRISES = 20
NUM_MONTHS = 24
RNG = np.random.default_rng(seed=42)


def seasonal_multiplier(month_index: int, enterprise_type: str) -> float:
    """Rough agricultural/festival seasonality by month index (0-based from Jan)."""
    month = month_index % 12
    # Harvest months tend to boost inflow for FPOs; festival months boost all types.
    harvest_months = {9, 10}       # Oct-Nov
    festival_months = {8, 9, 2}    # Sep-Oct (festive season), Mar (Holi)
    multiplier = 1.0
    if enterprise_type == "FPO" and month in harvest_months:
        multiplier *= 1.6
    if month in festival_months:
        multiplier *= 1.25
    if month in {5, 6}:  # monsoon slack season
        multiplier *= 0.75
    return multiplier


def generate_enterprise_series(enterprise_id: str, enterprise_type: str) -> pd.DataFrame:
    base_inflow = RNG.uniform(15000, 60000)
    rows = []
    data_completeness = RNG.choice(["low", "medium", "high"], p=[0.3, 0.4, 0.3])

    for m in range(NUM_MONTHS):
        mult = seasonal_multiplier(m, enterprise_type)
        noise = RNG.normal(1.0, 0.12)
        inflow = max(0, base_inflow * mult * noise)
        outflow = max(0, inflow * RNG.uniform(0.65, 0.95))

        # Simulate sparse data: some months missing entirely for low-completeness enterprises
        if data_completeness == "low" and RNG.random() < 0.35:
            continue
        if data_completeness == "medium" and RNG.random() < 0.12:
            continue

        rows.append({
            "enterprise_id": enterprise_id,
            "enterprise_type": enterprise_type,
            "month_index": m,
            "upi_inflow": round(inflow, 2),
            "upi_outflow": round(outflow, 2),
            "net_cash_flow": round(inflow - outflow, 2),
            "data_completeness_tier": data_completeness,
        })

    return pd.DataFrame(rows)


def main():
    all_rows = []
    for i in range(NUM_ENTERPRISES):
        enterprise_id = f"ent_{i+1:03d}"
        enterprise_type = RNG.choice(ENTERPRISE_TYPES)
        df = generate_enterprise_series(enterprise_id, enterprise_type)
        all_rows.append(df)

    full_df = pd.concat(all_rows, ignore_index=True)
    out_path = OUTPUT_DIR / "synthetic_transactions.csv"
    full_df.to_csv(out_path, index=False)
    print(f"Wrote {len(full_df)} rows for {NUM_ENTERPRISES} enterprises to {out_path}")


if __name__ == "__main__":
    main()
