from studymate_llm.reference_solution.app import (
    generate_flashcards_from_sample,
    generate_quiz_from_sample,
)


def test_generate_flashcards_from_sample_returns_flashcards():
    session = generate_flashcards_from_sample()

    assert session.flashcards
    assert "question" in session.flashcards[0]
    assert "answer" in session.flashcards[0]


def test_generate_quiz_from_sample_returns_questions():
    session = generate_quiz_from_sample()

    assert len(session.questions) >= 3
