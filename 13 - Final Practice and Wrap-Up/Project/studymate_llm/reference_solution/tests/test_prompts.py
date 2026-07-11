from studymate_llm.reference_solution.prompts import (
    build_flashcard_prompt,
    build_quiz_prompt,
)


def test_flashcard_prompt_mentions_question_answer_format():
    prompt = build_flashcard_prompt("Decorators wrap functions.")

    assert "question: answer" in prompt


def test_quiz_prompt_requests_at_least_three_questions():
    prompt = build_quiz_prompt("Functions make code reusable.")

    assert "at least 3 questions" in prompt
