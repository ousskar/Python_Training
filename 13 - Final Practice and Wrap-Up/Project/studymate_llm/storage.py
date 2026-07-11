from pathlib import Path
import json

from studymate_llm.models import SessionRecord


def save_session(path: str, session: SessionRecord) -> None:
    payload = {
        "topic": session.topic,
        "summary": session.summary,
        "questions": session.questions,
        "flashcards": session.flashcards,
    }
    Path(path).write_text(json.dumps(payload, indent=2), encoding="utf-8")


def load_session(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))
