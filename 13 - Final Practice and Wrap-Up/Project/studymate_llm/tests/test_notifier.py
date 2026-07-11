from unittest.mock import Mock

from studymate_llm.notifier import notify_study_summary


def test_notify_study_summary_passes_formatted_message():
    sender = Mock()

    notify_study_summary(
        topic="functions",
        summary="Functions help reuse logic.",
        sender=sender,
    )

    sender.assert_called_once_with(
        "Study summary for functions: Functions help reuse logic."
    )
