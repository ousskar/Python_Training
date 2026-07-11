from pathlib import Path
import csv
import json

from studymate_llm.models import Document


def load_text_file(path: str) -> Document:
    file_path = Path(path)
    content = file_path.read_text(encoding="utf-8")
    return Document(
        title=file_path.stem,
        content=content,
        source=str(file_path),
    )


def load_csv_file(path: str) -> list[dict[str, str]]:
    file_path = Path(path)
    with file_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader)


def load_json_file(path: str) -> dict:
    file_path = Path(path)
    return json.loads(file_path.read_text(encoding="utf-8"))
