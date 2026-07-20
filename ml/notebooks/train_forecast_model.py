"""
Trains the cash flow forecasting model on synthetic (or real) transaction data.

Run generate_synthetic_data.py first if /data/synthetic/synthetic_transactions.csv
does not exist yet.

This is a starter scaffold — extend with:
- Confidence scoring based on data_completeness_tier / row count per enterprise
- SHAP explainability for the risk/action recommendation layer
- Model serialization to /ml/models for the backend to load
"""

import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "synthetic" / "synthetic_transactions.csv"
MODEL_DIR = Path(__file__).resolve().parents[1] / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)


def load_data() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"{DATA_PATH} not found. Run generate_synthetic_data.py first."
        )
    return pd.read_csv(DATA_PATH)


def main():
    df = load_data()
    print(f"Loaded {len(df)} rows across {df['enterprise_id'].nunique()} enterprises")

    # TODO: feature engineering (rolling averages, seasonality flags, etc.)
    # TODO: train forecasting model (Prophet per-enterprise or XGBoost on engineered features)
    # TODO: train risk/action classifier + SHAP explainability
    # TODO: joblib.dump(model, MODEL_DIR / "forecast_model.pkl")

    print("Scaffold only — implement model training steps above.")


if __name__ == "__main__":
    main()
