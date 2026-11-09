import csv
import time
import uuid
from pathlib import Path

try:
    from pynput import keyboard
except ImportError:
    print("Missing package: pynput")
    print("Install it using: pip install pynput")
    exit()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_FILE = DATA_DIR / "raw_keystrokes.csv"

DATA_DIR.mkdir(parents=True, exist_ok=True)

SESSION_ID = str(uuid.uuid4())
USER_ID = input("Enter authorized employee/user ID: ").strip()

print("\nAuthorized Keystroke Timing Metadata Collector")
print("This tool records timing metadata only.")
print("It does NOT store typed text or passwords.")
print("Press ESC to stop collection.\n")

fieldnames = [
    "session_id",
    "user_id",
    "event_type",
    "key_category",
    "timestamp"
]

if not RAW_FILE.exists():
    with open(RAW_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


def categorize_key(key):
    """
    This function protects privacy by not storing the real typed key.
    It stores only the key type/category.
    """
    try:
        if key.char is None:
            return "special"
        if key.char.isalpha():
            return "letter"
        if key.char.isdigit():
            return "digit"
        return "symbol"
    except AttributeError:
        key_name = str(key).lower()

        if "space" in key_name:
            return "space"
        if "backspace" in key_name:
            return "backspace"
        if "ctrl" in key_name:
            return "ctrl"
        if "alt" in key_name:
            return "alt"
        if "shift" in key_name:
            return "shift"
        if "enter" in key_name:
            return "enter"

        return "special"


def save_event(event_type, key_category):
    with open(RAW_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({
            "session_id": SESSION_ID,
            "user_id": USER_ID,
            "event_type": event_type,
            "key_category": key_category,
            "timestamp": time.time()
        })


def on_press(key):
    if key == keyboard.Key.esc:
        print("\nCollection stopped.")
        return False

    save_event("press", categorize_key(key))


def on_release(key):
    if key != keyboard.Key.esc:
        save_event("release", categorize_key(key))


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
