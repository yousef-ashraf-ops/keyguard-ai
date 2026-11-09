import subprocess
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent

steps = [
    "segmentation.py",
    "feature_extraction.py",
    "train_model.py",
    "predict.py"
]

for step in steps:
    print(f"\nRunning {step} ...")

    result = subprocess.run(
        [sys.executable, str(SRC_DIR / step)],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        print(f"Pipeline stopped at {step}")
        sys.exit(result.returncode)

print("\nFull AI pipeline completed successfully.")
