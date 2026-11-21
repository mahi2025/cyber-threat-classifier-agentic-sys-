
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "threats.json"

def load_knowledge_base(file_path=DEFAULT_DATA_PATH):

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
