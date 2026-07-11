from studymate_llm.models import SessionRecord
from studymate_llm.storage import load_session, save_session


def test_save_and_load_session(tmp_path):
    session_path = tmp_path / "session.json"
    session = SessionRecord(topic="python", summary="short summary")

    save_session(str(session_path), session)
    loaded = load_session(str(session_path))

    assert loaded["topic"] == "python"
    assert loaded["summary"] == "short summary"
