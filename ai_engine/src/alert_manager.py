import pandas as pd
from datetime import datetime
from config import PREDICTIONS_FILE, ALERTS_FILE

def generate_alerts():
    df = pd.read_csv(PREDICTIONS_FILE)

    alert_rows = []

    for _, row in df.iterrows():
        if row["predicted_risk"] in ["Medium", "High"]:
            alert_rows.append({
                "alert_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "segment_id": row["segment_id"],
                "session_id": row["session_id"],
                "user_id": row["user_id"],
                "predicted_risk": row["predicted_risk"],
                "risk_score": row["risk_score"],
                "prediction_reason": row["prediction_reason"],
                "status": "Open"
            })

    alerts_df = pd.DataFrame(alert_rows)
    alerts_df.to_csv(ALERTS_FILE, index=False)

    print("Alerts generated.")
    print("Alerts saved to:", ALERTS_FILE)
    print("Number of alerts:", len(alerts_df))

if __name__ == "__main__":
    generate_alerts()
