import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

RAW_FILE = DATA_DIR / "raw_keystrokes.csv"
SEGMENTS_FILE = DATA_DIR / "segments.csv"
FEATURES_FILE = DATA_DIR / "features.csv"


def safe_mean(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


def extract_features():
    if not RAW_FILE.exists() or not SEGMENTS_FILE.exists():
        print("Required files not found. Run collector and segmentation first.")
        return

    raw = pd.read_csv(RAW_FILE)
    segments = pd.read_csv(SEGMENTS_FILE)

    raw["timestamp"] = pd.to_numeric(raw["timestamp"], errors="coerce")
    raw = raw.dropna(subset=["timestamp"])

    feature_rows = []

    for _, segment in segments.iterrows():
        session_id = segment["session_id"]
        user_id = segment["user_id"]
        start_time = segment["start_time"]
        end_time = segment["end_time"]

        seg_raw = raw[
            (raw["session_id"] == session_id) &
            (raw["timestamp"] >= start_time) &
            (raw["timestamp"] <= end_time)
        ].sort_values("timestamp")

        press_events = seg_raw[seg_raw["event_type"] == "press"].copy()
        release_events = seg_raw[seg_raw["event_type"] == "release"].copy()

        duration = max(end_time - start_time, 1)
        press_count = len(press_events)

        typing_speed = press_count / duration

        dwell_times = []
        press_times = press_events["timestamp"].tolist()
        release_times = release_events["timestamp"].tolist()

        pair_count = min(len(press_times), len(release_times))
        for i in range(pair_count):
            dwell = release_times[i] - press_times[i]
            if 0 <= dwell <= 5:
                dwell_times.append(dwell)

        avg_dwell_time = safe_mean(dwell_times)

        flight_times = []
        for i in range(1, len(press_times)):
            diff = press_times[i] - press_times[i - 1]
            if 0 <= diff <= 10:
                flight_times.append(diff)

        avg_flight_time = safe_mean(flight_times)

        long_pauses = [x for x in flight_times if x > 2]
        pause_ratio = len(long_pauses) / len(flight_times) if len(flight_times) > 0 else 0

        # Only count truly special keys
        # Space, Enter, Shift are NOT counted as suspicious
        special_key_count = len(press_events[
            press_events["key_category"] == "special"
        ])
        backspace_count = len(press_events[
            press_events["key_category"] == "backspace"
        ])
        ctrl_alt_count = len(press_events[
            press_events["key_category"].isin(["ctrl", "alt"])
        ])

        special_key_ratio = special_key_count / press_count if press_count > 0 else 0
        backspace_ratio = backspace_count / press_count if press_count > 0 else 0
        ctrl_alt_ratio = ctrl_alt_count / press_count if press_count > 0 else 0

        # Risk labeling with realistic thresholds
        risk_label = "Low"

        if (
            typing_speed > 12 or
            ctrl_alt_ratio > 0.30 or
            special_key_ratio > 0.60
        ):
            risk_label = "High"
        elif (
            typing_speed > 5 or
            backspace_ratio > 0.25 or
            pause_ratio > 0.40 or
            ctrl_alt_ratio > 0.15 or
            special_key_ratio > 0.40
        ):
            risk_label = "Medium"

        reason = []

        if typing_speed > 12:
            reason.append("Very high typing speed")
        if ctrl_alt_ratio > 0.30:
            reason.append("High Ctrl/Alt usage")
        if special_key_ratio > 0.60:
            reason.append("High special key usage")
        if backspace_ratio > 0.25:
            reason.append("High backspace ratio")
        if pause_ratio > 0.40:
            reason.append("Unusual pause pattern")
        if typing_speed > 5 and risk_label == "Medium":
            reason.append("Above average typing speed")

        if not reason:
            reason.append("Normal typing behavior")

        feature_rows.append({
            "segment_id": segment["segment_id"],
            "session_id": session_id,
            "user_id": user_id,
            "duration": round(duration, 4),
            "press_count": press_count,
            "typing_speed": round(typing_speed, 4),
            "avg_dwell_time": round(avg_dwell_time, 4),
            "avg_flight_time": round(avg_flight_time, 4),
            "pause_ratio": round(pause_ratio, 4),
            "special_key_ratio": round(special_key_ratio, 4),
            "backspace_ratio": round(backspace_ratio, 4),
            "ctrl_alt_ratio": round(ctrl_alt_ratio, 4),
            "risk_label": risk_label,
            "reason": "; ".join(reason)
        })

    features_df = pd.DataFrame(feature_rows)
    features_df.to_csv(FEATURES_FILE, index=False)

    print(f"Features extracted successfully: {FEATURES_FILE}")


if __name__ == "__main__":
    extract_features()
