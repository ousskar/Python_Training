def chunk_text(text: str, chunk_size: int = 200) -> list[str]:
    words = text.split()
    if not words:
        return []

    chunks = []
    for index in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[index:index + chunk_size]))
    return chunks
