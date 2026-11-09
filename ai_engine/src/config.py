import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "models")

RAW_KEYSTROKES_FILE = os.path.join(DATA_DIR, "raw_keystrokes.csv")
SEGMENTS_FILE = os.path.join(DATA_DIR, "segments.csv")
FEATURES_FILE = os.path.join(DATA_DIR, "features.csv")
PREDICTIONS_FILE = os.path.join(DATA_DIR, "predictions.csv")
ALERTS_FILE = os.path.join(DATA_DIR, "alerts.csv")

MODEL_FILE = os.path.join(MODEL_DIR, "risk_model.pkl")
ENCODER_FILE = os.path.join(MODEL_DIR, "label_encoder.pkl")

SEGMENT_SECONDS = 10

RISK_LABELS = ["Low", "Medium", "High"]

FEATURE_COLUMNS = [
    "total_keys",
    "duration",
    "keys_per_second",
    "dwell_mean",
    "dwell_std",
    "flight_mean",
    "flight_std",
    "pause_ratio",
    "special_key_ratio",
    "backspace_ratio",
    "uniform_timing_score",
    "ctrl_alt_ratio"
]

def ensure_directories():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(MODEL_DIR, exist_ok=True)
