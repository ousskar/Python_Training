from studymate_llm.chunker import chunk_text


def test_chunk_text_splits_long_text():
    text = "word " * 10
    chunks = chunk_text(text, chunk_size=3)
    assert len(chunks) == 4


def test_chunk_text_empty_string():
    assert chunk_text("", chunk_size=3) == []
