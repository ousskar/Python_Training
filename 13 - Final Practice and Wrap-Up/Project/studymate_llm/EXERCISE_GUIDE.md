# StudyMate LLM Student Exercise Guide

This capstone is now a guided build exercise, not just a finished starter.

## What Students Must Complete

1. Implement `generate_flashcards_from_sample()` in `app.py`.
2. Implement `generate_quiz_from_sample()` in `app.py`.
3. Improve `build_flashcard_prompt()` in `prompts.py`.
4. Improve `build_quiz_prompt()` in `prompts.py`.
5. Complete the TODO assertions in `tests/test_notifier_exercise.py`.
6. Add at least one new test for prompt generation.

## Acceptance Criteria

- The CLI should support summary, flashcards, and quiz generation.
- Flashcards should be saved inside the session record.
- Quiz output should include at least three questions.
- Prompt builders should clearly describe the expected output format.
- The existing tests should still pass.

## Stretch Goals

1. Load more than one file from the `data` folder.
2. Save multiple named sessions.
3. Add a menu option to list previous sessions.
4. Replace the echo gateway with a real API implementation.
