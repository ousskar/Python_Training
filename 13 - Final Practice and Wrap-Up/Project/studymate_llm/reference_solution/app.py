from pathlib import Path
import os

from studymate_llm.reference_solution.cleaner import clean_text
from studymate_llm.reference_solution.chunker import chunk_text
from studymate_llm.reference_solution.llm_client import LLMClient
from studymate_llm.reference_solution.loader import load_text_file
from studymate_llm.reference_solution.models import SessionRecord
from studymate_llm.reference_solution.prompts import (
    build_flashcard_prompt,
    build_quiz_prompt,
    build_summary_prompt,
)
from studymate_llm.reference_solution.quiz import (
    build_flashcards_from_lines,
    build_questions_from_lines,
)
from studymate_llm.reference_solution.storage import save_session
from studymate_llm.reference_solution.utils import timed


DATA_DIR = Path(__file__).resolve().parents[1] / "data"
SESSIONS_DIR = Path(__file__).parent / "sessions"


def load_env_file(path: Path) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


def _load_sample_text() -> tuple[str, list[str], str]:
    document = load_text_file(str(DATA_DIR / "sample_notes.txt"))
    cleaned = clean_text(document.content)
    chunks = chunk_text(cleaned, chunk_size=80)
    source_text = chunks[0] if chunks else cleaned
    return document.title, chunks, source_text


@timed
def summarize_sample() -> SessionRecord:
    topic, _chunks, source_text = _load_sample_text()
    client = LLMClient()
    summary = client.generate(build_summary_prompt(source_text))
    session = SessionRecord(topic=topic, summary=summary)
    save_session(str(SESSIONS_DIR / "latest_summary_session.json"), session)
    return session


@timed
def generate_flashcards_from_sample() -> SessionRecord:
    topic, _chunks, source_text = _load_sample_text()
    client = LLMClient()
    raw_response = client.generate(build_flashcard_prompt(source_text))

    fallback_lines = [
        "What is Python used for?: Automation, data, web, and AI tasks.",
        "Why are functions useful?: They help organize reusable logic.",
        "Why does testing matter?: It helps catch regressions early.",
    ]
    flashcards = build_flashcards_from_lines(raw_response.splitlines())
    if not flashcards:
        flashcards = build_flashcards_from_lines(fallback_lines)

    session = SessionRecord(topic=topic, flashcards=flashcards)
    save_session(str(SESSIONS_DIR / "latest_flashcards_session.json"), session)
    return session


@timed
def generate_quiz_from_sample() -> SessionRecord:
    topic, _chunks, source_text = _load_sample_text()
    client = LLMClient()
    raw_response = client.generate(build_quiz_prompt(source_text))

    fallback_lines = [
        "What is Python commonly used for? - Automation, data, web, and AI.",
        "What is the purpose of a function? - To reuse logic.",
        "Why should developers write tests? - To catch regressions early.",
    ]
    questions = build_questions_from_lines(raw_response.splitlines())
    if not questions:
        questions = build_questions_from_lines(fallback_lines)

    session = SessionRecord(topic=topic, questions=questions)
    save_session(str(SESSIONS_DIR / "latest_quiz_session.json"), session)
    return session


def main() -> None:
    SESSIONS_DIR.mkdir(exist_ok=True)
    load_env_file(Path(__file__).resolve().parents[1] / ".env")

    print("StudyMate LLM Solution")
    print("1. Summarize sample notes")
    print("2. Generate flashcards from sample notes")
    print("3. Generate quiz from sample notes")
    print("4. Show active provider")
    print("5. Exit")

    choice = input("Choose an option: ").strip()
    if choice == "1":
        session = summarize_sample()
        print(session.summary)
    elif choice == "2":
        session = generate_flashcards_from_sample()
        print(session.flashcards)
    elif choice == "3":
        session = generate_quiz_from_sample()
        print(session.questions)
    elif choice == "4":
        provider = os.getenv("LLM_PROVIDER", "fake")
        model = os.getenv("LLM_MODEL", "study-small")
        print(f"Provider: {provider}")
        print(f"Model: {model}")
    else:
        print("Goodbye")


if __name__ == "__main__":
    main()
