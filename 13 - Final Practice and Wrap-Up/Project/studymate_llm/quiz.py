def build_flashcards_from_lines(lines: list[str]) -> list[dict[str, str]]:
    flashcards = []
    for line in lines:
        if ":" not in line:
            continue
        question, answer = line.split(":", 1)
        flashcards.append(
            {
                "question": question.strip(),
                "answer": answer.strip(),
            }
        )
    return flashcards


def score_quiz(expected: list[str], given: list[str]) -> int:
    score = 0
    for exp, got in zip(expected, given):
        if exp.strip().lower() == got.strip().lower():
            score += 1
    return score
