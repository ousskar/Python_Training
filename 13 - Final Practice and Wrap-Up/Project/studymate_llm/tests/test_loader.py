from studymate_llm.loader import load_text_file


def test_load_text_file(tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("hello world", encoding="utf-8")

    document = load_text_file(str(file_path))

    assert document.title == "notes"
    assert document.content == "hello world"
