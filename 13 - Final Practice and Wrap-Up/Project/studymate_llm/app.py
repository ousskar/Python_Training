from pathlib import Path
import os

from studymate_llm.cleaner import clean_text
from studymate_llm.chunker import chunk_text
from studymate_llm.llm_client import LLMClient
from studymate_llm.loader import load_text_file
from studymate_llm.prompts import build_summary_prompt
from studymate_llm.storage import save_session
from studymate_llm.models import SessionRecord
from studymate_llm.utils import timed


DATA_DIR = Path(__file__).parent / "data"
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


@timed
def summarize_sample() -> SessionRecord:
    document = load_text_file(str(DATA_DIR / "sample_notes.txt"))
    cleaned = clean_text(document.content)
    chunks = chunk_text(cleaned, chunk_size=80)
    client = LLMClient()
    prompt = build_summary_prompt(chunks[0] if chunks else cleaned)
    summary = client.generate(prompt)

    session = SessionRecord(topic=document.title, summary=summary)
    save_session(str(SESSIONS_DIR / "latest_session.json"), session)
    return session


def generate_flashcards_from_sample() -> SessionRecord:
    # TODO(student): follow the same pipeline used in summarize_sample.
    # Suggested steps:
    # 1. Load and clean the sample notes.
    # 2. Build a flashcard prompt.
    # 3. Call the LLM client.
    # 4. Save the result inside SessionRecord.flashcards.
    # 5. Save the session to the sessions folder.
    raise NotImplementedError("TODO: implement flashcard generation")


def generate_quiz_from_sample() -> SessionRecord:
    # TODO(student): implement quiz generation.
    # Suggested steps:
    # 1. Reuse the sample loading flow.
    # 2. Build a quiz prompt with build_quiz_prompt.
    # 3. Call the LLM client.
    # 4. Save quiz questions inside SessionRecord.questions.
    # 5. Save the session to disk.
    raise NotImplementedError("TODO: implement quiz generation")


def main() -> None:
    SESSIONS_DIR.mkdir(exist_ok=True)
    load_env_file(Path(__file__).parent / ".env")

    print("StudyMate LLM Starter")
    print("1. Summarize sample notes")
    print("2. Generate flashcards from sample notes (TODO)")
    print("3. Generate quiz from sample notes (TODO)")
    print("4. Show active provider")
    print("5. Exit")

    choice = input("Choose an option: ").strip()
    if choice == "1":
        session = summarize_sample()
        print(session.summary)
    elif choice == "2":
        print("TODO for students: implement generate_flashcards_from_sample()")
        generate_flashcards_from_sample()
    elif choice == "3":
        print("TODO for students: implement generate_quiz_from_sample()")
        generate_quiz_from_sample()
    elif choice == "4":
        provider = os.getenv("LLM_PROVIDER", "fake")
        model = os.getenv("LLM_MODEL", "study-small")
        print(f"Provider: {provider}")
        print(f"Model: {model}")
    else:
        print("Goodbye")


if __name__ == "__main__":
    main()
