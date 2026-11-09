import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

FEATURES_FILE = DATA_DIR / "features.csv"
COMPARISON_FILE = DATA_DIR / "model_comparison.csv"

MODEL_FILE = MODELS_DIR / "risk_model.pkl"
ENCODER_FILE = MODELS_DIR / "label_encoder.pkl"

MODELS_DIR.mkdir(parents=True, exist_ok=True)

FEATURE_COLUMNS = [
    "typing_speed",
    "avg_dwell_time",
    "avg_flight_time",
    "pause_ratio",
    "special_key_ratio",
    "backspace_ratio",
    "ctrl_alt_ratio"
]


def add_training_samples(df):
    extra_rows = []
    sample_user = df["user_id"].iloc[0] if "user_id" in df.columns and len(df) > 0 else 1

    # Low risk — slow normal human typing (speed 1-4)
    for i in range(10):
        extra_rows.append({
            "segment_id": f"synthetic_low_{i}",
            "session_id": "synthetic",
            "user_id": sample_user,
            "duration": 60,
            "press_count": 80,
            "typing_speed": 2.5,
            "avg_dwell_time": 0.15,
            "avg_flight_time": 0.30,
            "pause_ratio": 0.08,
            "special_key_ratio": 0.05,
            "backspace_ratio": 0.05,
            "ctrl_alt_ratio": 0.00,
            "risk_label": "Low",
            "reason": "Normal typing behavior"
        })

    # Medium risk — speed between 5 and 12
    for i in range(10):
        extra_rows.append({
            "segment_id": f"synthetic_medium_{i}",
            "session_id": "synthetic",
            "user_id": sample_user,
            "duration": 60,
            "press_count": 150,
            "typing_speed": 7.0,
            "avg_dwell_time": 0.08,
            "avg_flight_time": 0.12,
            "pause_ratio": 0.35,
            "special_key_ratio": 0.35,
            "backspace_ratio": 0.22,
            "ctrl_alt_ratio": 0.12,
            "risk_label": "Medium",
            "reason": "Suspicious typing behavior"
        })

    # High risk — automated or scripted (speed above 12)
    for i in range(10):
        extra_rows.append({
            "segment_id": f"synthetic_high_{i}",
            "session_id": "synthetic",
            "user_id": sample_user,
            "duration": 60,
            "press_count": 600,
            "typing_speed": 20.0,
            "avg_dwell_time": 0.02,
            "avg_flight_time": 0.01,
            "pause_ratio": 0.00,
            "special_key_ratio": 0.65,
            "backspace_ratio": 0.01,
            "ctrl_alt_ratio": 0.35,
            "risk_label": "High",
            "reason": "High-risk keyboard behavior"
        })

    extra_df = pd.DataFrame(extra_rows)
    return pd.concat([df, extra_df], ignore_index=True)


def train_model():
    if not FEATURES_FILE.exists():
        print("features.csv not found. Run feature_extraction.py first.")
        return

    df = pd.read_csv(FEATURES_FILE)

    if df.empty:
        print("features.csv is empty.")
        return

    df = df.dropna(subset=FEATURE_COLUMNS + ["risk_label"])

    existing_classes = df["risk_label"].nunique()

    if existing_classes < 3:
        print("Less than 3 classes found in collected data.")
        print("Adding controlled synthetic samples for Low, Medium, and High classes.")
        df = add_training_samples(df)
        df.to_csv(FEATURES_FILE, index=False)

    X = df[FEATURE_COLUMNS]
    y = df["risk_label"]

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    class_counts = pd.Series(y_encoded).value_counts()
    total_samples = len(X)

    if total_samples < 12:
        test_size = 0.10
    else:
        test_size = 0.25

    can_stratify = class_counts.min() >= 2 and total_samples >= 12

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_encoded,
        test_size=test_size,
        random_state=42,
        stratify=y_encoded if can_stratify else None
    )

    candidate_models = {
        "Random Forest": RandomForestClassifier(
            n_estimators=150,
            random_state=42,
            class_weight="balanced"
        ),
        "Decision Tree": DecisionTreeClassifier(
            random_state=42,
            class_weight="balanced"
        ),
        "Gradient Boosting": GradientBoostingClassifier(
            random_state=42
        ),
        "KNN": KNeighborsClassifier(n_neighbors=3),
        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        )
    }

    results = []

    for model_name, model in candidate_models.items():
        try:
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)

            accuracy = accuracy_score(y_test, predictions)
            precision = precision_score(
                y_test, predictions, average="weighted", zero_division=0
            )
            recall = recall_score(
                y_test, predictions, average="weighted", zero_division=0
            )
            f1 = f1_score(
                y_test, predictions, average="weighted", zero_division=0
            )

            results.append({
                "algorithm": model_name,
                "accuracy": round(accuracy, 4),
                "precision": round(precision, 4),
                "recall": round(recall, 4),
                "f1_score": round(f1, 4),
                "training_split": "75%",
                "testing_split": "25%"
            })

        except Exception as e:
            results.append({
                "algorithm": model_name,
                "accuracy": "Failed",
                "precision": "Failed",
                "recall": "Failed",
                "f1_score": "Failed",
                "training_split": "75%",
                "testing_split": "25%",
                "error": str(e)
            })

    comparison_df = pd.DataFrame(results)
    comparison_df.to_csv(COMPARISON_FILE, index=False)

    final_model = RandomForestClassifier(
        n_estimators=150,
        random_state=42,
        class_weight="balanced"
    )

    final_model.fit(X_train, y_train)

    joblib.dump(final_model, MODEL_FILE)
    joblib.dump(label_encoder, ENCODER_FILE)

    print("Model training completed.")
    print("Selected model: Random Forest")
    print("Training split: 75%")
    print("Testing split: 25%")
    print("Classes used:", list(label_encoder.classes_))
    print("Model saved to:", MODEL_FILE)
    print("Comparison saved to:", COMPARISON_FILE)


if __name__ == "__main__":
    train_model()
