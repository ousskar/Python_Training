def build_summary_prompt(text: str) -> str:
    return (
        "Summarize the following study material in clear bullet points. "
        "Highlight the main ideas and important terminology.\n\n"
        f"{text}"
    )


def build_flashcard_prompt(text: str) -> str:
    return (
        "Create 3 to 5 flashcards from the following study material. "
        "Return each flashcard on its own line using the exact format "
        "'question: answer'.\n\n"
        f"{text}"
    )


def build_quiz_prompt(text: str) -> str:
    return (
        "Create a quiz with at least 3 questions from the following "
        "study material. After each question, include the answer using "
        "the format 'Question - Answer'.\n\n"
        f"{text}"
    )
