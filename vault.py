import json
import os
from datetime import datetime

FILE = "clipboard_history.json"

def load():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def save_clipboard(text):
    history = load()

    history.append({
        "text": text,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save(history)
    print("✅ Saved!")

def view_history():
    history = load()

    if not history:
        print("No history found.")
        return

    print("\n📋 Clipboard History\n")

    for item in history:
        print(f"[{item['time']}] {item['text']}")
