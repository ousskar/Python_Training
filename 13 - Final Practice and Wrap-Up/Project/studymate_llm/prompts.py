def build_summary_prompt(text: str) -> str:
    return (
        "Summarize the following study material in clear bullet points:\n\n"
        f"{text}"
    )


def build_flashcard_prompt(text: str) -> str:
    # TODO(student): make this prompt more specific.
    # Requirement: ask for 3-5 flashcards and require a clear
    # "question: answer" line format so the output is easier to parse.
    return (
        "Create short flashcards from the following material. "
        "Return question and answer pairs.\n\n"
        f"{text}"
    )


def build_quiz_prompt(text: str) -> str:
    # TODO(student): make this prompt stricter.
    # Requirement: ask for at least 3 questions and include the answer
    # after each question in a consistent format.
    return (
        "Create a short quiz based on the following material. "
        "Include questions and expected answers.\n\n"
        f"{text}"
    )
