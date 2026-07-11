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


def build_questions_from_lines(lines: list[str]) -> list[str]:
    questions = []
    for line in lines:
        if "-" not in line:
            continue
        question, _answer = line.split("-", 1)
        questions.append(question.strip())
    return questions


def score_quiz(expected: list[str], given: list[str]) -> int:
    score = 0
    for exp, got in zip(expected, given):
        if exp.strip().lower() == got.strip().lower():
            score += 1
    return score
