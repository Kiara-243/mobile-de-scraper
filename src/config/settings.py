thonpython
import json
from pathlib import Path

def load_settings():
    file_path = Path(__file__).parent / "settings.example.json"
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)