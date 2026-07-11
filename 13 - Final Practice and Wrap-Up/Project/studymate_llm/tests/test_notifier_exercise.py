"""Student exercise: replace the TODOs with working assertions.

This file mirrors the unit testing practice style used elsewhere in the course.
"""

from unittest.mock import Mock

from studymate_llm.notifier import notify_study_summary


def test_notify_study_summary_exercise():
    sender = Mock()

    notify_study_summary(
        topic="iterators",
        summary="Iterators yield one value at a time.",
        sender=sender,
    )

    # TODO 1: assert the sender was called exactly once.
    # TODO 2: assert the sent message contains the word "iterators".
    # TODO 3: assert the sent message contains the summary text.
