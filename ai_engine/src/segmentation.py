import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

RAW_FILE = DATA_DIR / "raw_keystrokes.csv"
SEGMENTS_FILE = DATA_DIR / "segments.csv"

SEGMENT_SECONDS = 30

REQUIRED_COLUMNS = [
    "session_id",
    "user_id",
    "event_type",
    "key_category",
    "timestamp"
]


def segment_keystrokes():
    if not RAW_FILE.exists():
        print("ERROR: raw_keystrokes.csv not found.")
        print("Run keystroke_collector.py first.")
        return

    df = pd.read_csv(RAW_FILE)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    print("Detected CSV columns:", list(df.columns))

    missing_columns = []

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            missing_columns.append(col)

    if missing_columns:
        print("ERROR: raw_keystrokes.csv has missing columns:")
        print(missing_columns)
        print("\nThe first row must be:")
        print(",".join(REQUIRED_COLUMNS))
        return

    if df.empty:
        print("ERROR: raw_keystrokes.csv is empty.")
        return

    df["timestamp"] = pd.to_numeric(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])

    if df.empty:
        print("ERROR: timestamp column exists but contains no valid numeric values.")
        return

    segments = []

    for session_id, session_data in df.groupby("session_id"):

        session_data = session_data.sort_values("timestamp")
        start_time = session_data["timestamp"].min()

        session_data["segment_number"] = (
            (session_data["timestamp"] - start_time) // SEGMENT_SECONDS
        ).astype(int)

        for segment_number, seg in session_data.groupby("segment_number"):

            segment_id = f"{session_id}_{segment_number}"

            segments.append({
                "segment_id": segment_id,
                "session_id": session_id,
                "user_id": seg["user_id"].iloc[0],
                "start_time": seg["timestamp"].min(),
                "end_time": seg["timestamp"].max(),
                "total_events": len(seg),
                "press_count": len(seg[seg["event_type"] == "press"]),
                "release_count": len(seg[seg["event_type"] == "release"])
            })

    if len(segments) == 0:
        print("ERROR: No segments were created.")
        return

    segments_df = pd.DataFrame(segments)
    segments_df.to_csv(SEGMENTS_FILE, index=False)

    print("Segments created successfully.")
    print("Output file:", SEGMENTS_FILE)


if __name__ == "__main__":
    segment_keystrokes()
