import random
import pandas as pd
from config import FEATURES_FILE, ensure_directories

def create_low_risk_row(segment_id):
    return {
        "segment_id": segment_id,
        "total_keys": random.randint(40, 120),
        "duration": random.uniform(10, 30),
        "keys_per_second": random.uniform(2.0, 5.5),
        "dwell_mean": random.uniform(0.08, 0.20),
        "dwell_std": random.uniform(0.01, 0.08),
        "flight_mean": random.uniform(0.15, 0.60),
        "flight_std": random.uniform(0.05, 0.25),
        "pause_ratio": random.uniform(0.05, 0.25),
        "special_key_ratio": random.uniform(0.02, 0.18),
        "backspace_ratio": random.uniform(0.01, 0.12),
        "uniform_timing_score": random.uniform(2, 10),
        "ctrl_alt_ratio": random.uniform(0.00, 0.05),
        "risk_label": "Low"
    }

def create_medium_risk_row(segment_id):
    return {
        "segment_id": segment_id,
        "total_keys": random.randint(30, 150),
        "duration": random.uniform(8, 35),
        "keys_per_second": random.uniform(5.0, 8.0),
        "dwell_mean": random.uniform(0.05, 0.25),
        "dwell_std": random.uniform(0.08, 0.18),
        "flight_mean": random.uniform(0.05, 0.90),
        "flight_std": random.uniform(0.20, 0.50),
        "pause_ratio": random.uniform(0.25, 0.45),
        "special_key_ratio": random.uniform(0.18, 0.35),
        "backspace_ratio": random.uniform(0.12, 0.25),
        "uniform_timing_score": random.uniform(8, 20),
        "ctrl_alt_ratio": random.uniform(0.04, 0.12),
        "risk_label": "Medium"
    }

def create_high_risk_row(segment_id):
    return {
        "segment_id": segment_id,
        "total_keys": random.randint(80, 250),
        "duration": random.uniform(5, 20),
        "keys_per_second": random.uniform(8.0, 18.0),
        "dwell_mean": random.uniform(0.02, 0.10),
        "dwell_std": random.uniform(0.00, 0.04),
        "flight_mean": random.uniform(0.01, 0.12),
        "flight_std": random.uniform(0.00, 0.05),
        "pause_ratio": random.uniform(0.00, 0.10),
        "special_key_ratio": random.uniform(0.30, 0.70),
        "backspace_ratio": random.uniform(0.00, 0.08),
        "uniform_timing_score": random.uniform(20, 80),
        "ctrl_alt_ratio": random.uniform(0.10, 0.35),
        "risk_label": "High"
    }

def create_dataset():
    ensure_directories()

    rows = []
    segment_id = 1

    for _ in range(250):
        rows.append(create_low_risk_row(segment_id))
        segment_id += 1

    for _ in range(250):
        rows.append(create_medium_risk_row(segment_id))
        segment_id += 1

    for _ in range(250):
        rows.append(create_high_risk_row(segment_id))
        segment_id += 1

    df = pd.DataFrame(rows)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df.to_csv(FEATURES_FILE, index=False)

    print("Sample training dataset created successfully.")
    print("File:", FEATURES_FILE)
    print(df["risk_label"].value_counts())

if __name__ == "__main__":
    create_dataset()
