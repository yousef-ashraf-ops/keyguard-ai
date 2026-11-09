import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

FEATURES_FILE = DATA_DIR / "features.csv"
PREDICTIONS_FILE = DATA_DIR / "predictions.csv"

MODEL_FILE = MODELS_DIR / "risk_model.pkl"
ENCODER_FILE = MODELS_DIR / "label_encoder.pkl"

FEATURE_COLUMNS = [
    "typing_speed",
    "avg_dwell_time",
    "avg_flight_time",
    "pause_ratio",
    "special_key_ratio",
    "backspace_ratio",
    "ctrl_alt_ratio"
]


def predict():
    if not FEATURES_FILE.exists():
        print("features.csv not found.")
        return

    if not MODEL_FILE.exists() or not ENCODER_FILE.exists():
        print("Model files not found. Run train_model.py first.")
        return

    df = pd.read_csv(FEATURES_FILE)

    if df.empty:
        print("No features found.")
        return

    model = joblib.load(MODEL_FILE)
    encoder = joblib.load(ENCODER_FILE)

    X = df[FEATURE_COLUMNS]
    pred_encoded = model.predict(X)
    pred_labels = encoder.inverse_transform(pred_encoded)

    pred_proba = model.predict_proba(X)

    predictions = df.copy()
    predictions["predicted_risk"] = pred_labels

    risk_scores = []
    for i, label in enumerate(pred_labels):
        max_prob = round(max(pred_proba[i]) * 100)
        risk_scores.append(max_prob)

    predictions["risk_score"] = risk_scores

    final_reasons = []

    for _, row in predictions.iterrows():
        reasons = []

        if row["typing_speed"] > 12:
            reasons.append("Very high typing speed")
        if row["ctrl_alt_ratio"] > 0.30:
            reasons.append("High Ctrl/Alt usage")
        if row["special_key_ratio"] > 0.60:
            reasons.append("High special key usage")
        if row["backspace_ratio"] > 0.25:
            reasons.append("High backspace ratio")
        if row["pause_ratio"] > 0.40:
            reasons.append("Unusual pause ratio")
        if row["typing_speed"] > 5 and row["predicted_risk"] == "Medium":
            reasons.append("Above average typing speed")

        if not reasons:
            reasons.append("Normal behavioral pattern")

        final_reasons.append("; ".join(reasons))

    predictions["prediction_reason"] = final_reasons
    predictions.to_csv(PREDICTIONS_FILE, index=False)

    print(f"Predictions saved successfully: {PREDICTIONS_FILE}")


if __name__ == "__main__":
    predict()
