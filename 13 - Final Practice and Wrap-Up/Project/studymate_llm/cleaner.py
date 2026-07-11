def clean_text(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def normalize_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    normalized = []
    for row in rows:
        cleaned_row = {
            key.strip(): (value or "").strip()
            for key, value in row.items()
        }
        normalized.append(cleaned_row)
    return normalized
