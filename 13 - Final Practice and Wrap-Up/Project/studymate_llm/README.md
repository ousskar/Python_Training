# StudyMate LLM Capstone

This folder is now self-contained. It includes the student exercise, the instructions, the sample data, the tests, and an in-folder reference solution.

This is the main folder students should use.

## Goal

Build a local study assistant that can:

- load notes from text, CSV, or JSON files
- clean and chunk content
- build prompts for an LLM
- generate summaries, flashcards, and quizzes
- save sessions to disk

## Quick Start

1. Create a virtual environment if you want isolation.
2. Install the starter dependency with `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` if you want to try the environment-based client stub.
4. Read `EXERCISE_GUIDE.md` before changing the code.
5. Run `python -m studymate_llm.app` from the parent `Project` folder.
6. Run `pytest tests` from this folder.

## Student TODO Areas

- `app.py`: finish the flashcard and quiz commands.
- `prompts.py`: make the flashcard and quiz prompts more precise.
- `tests/test_notifier_exercise.py`: complete the mock assertions.
- Add at least one new test for a prompt or CLI behavior.

## Single-Folder Layout

- `app.py`: student starter CLI
- `EXERCISE_GUIDE.md`: student task list and acceptance criteria
- `tests/`: starter tests and TODO exercises
- `data/`: shared sample inputs
- `reference_solution/`: completed reference implementation for instructors

If you opened the `Project` folder first, this is the correct student project to continue with.

Run the student project with `python -m studymate_llm.app`.
Run the in-folder solution with `python -m studymate_llm.reference_solution.app`.

## Starter Structure

- `app.py`: command-line entry point
- `loader.py`: file reading helpers
- `cleaner.py`: content cleanup helpers
- `chunker.py`: text chunking helpers
- `prompts.py`: prompt builders
- `llm_client.py`: fake LLM interface for development
- `notifier.py`: small function used for mocking practice
- `quiz.py`: quiz and flashcard helpers
- `storage.py`: save and load sessions
- `models.py`: lightweight data models
- `utils.py`: shared utility helpers
- `tests/`: starter tests
- `data/`: sample input files
- `sessions/`: saved session output

## Environment-Based Client Stub

The project now supports two development modes:

- `LLM_PROVIDER=fake`: returns a local fake response and needs no API key.
- `LLM_PROVIDER=env`: routes the prompt through a stub gateway that reads `LLM_MODEL` and `LLM_API_KEY` from environment variables.

This is intentionally a safe teaching step before students integrate a real provider.

## Milestone Guide

### Milestone 1: Local Data Flow

- Load the sample text file.
- Clean the text.
- Split it into chunks.
- Save a generated session file.

### Milestone 2: Prompt Design

- Improve the summary prompt.
- Finish the flashcard command in the CLI.
- Finish the quiz command in the CLI.

### Milestone 3: LLM Integration Layer

- Configure `.env`.
- Replace `EchoGateway` with a real API implementation.
- Keep the rest of the application isolated from provider details.

### Milestone 4: Testing and Reliability

- Add tests for prompt builders.
- Add more storage tests.
- Complete the mocking exercise in `tests/test_notifier_exercise.py`.

## Exercise Workflow

1. Run the CLI and inspect the TODO menu options.
2. Open `EXERCISE_GUIDE.md` and implement the required tasks one by one.
3. Run `pytest tests` after each task.
4. Keep the summary feature working while adding the missing parts.

## Where The Solution Lives

The completed reference implementation is in `reference_solution/`. This keeps the capstone material in a single folder while still separating the student workspace from the solved version.

## Mocking Exercise

The file `tests/test_notifier_exercise.py` contains a small TODO-based test. Students should complete it by asserting how a mocked sender is used.

## Suggested Extensions

1. Load multiple study files and merge them into one session.
2. Let users choose between summary, flashcards, and quiz output.
3. Add JSON session history browsing.
4. Replace the stub gateway with a real LLM provider.
5. Add more TODO-style exercises for testing and debugging.
