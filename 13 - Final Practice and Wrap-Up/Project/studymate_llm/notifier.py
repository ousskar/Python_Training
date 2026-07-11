def notify_study_summary(topic: str, summary: str, sender) -> None:
    message = f"Study summary for {topic}: {summary}"
    sender(message)
