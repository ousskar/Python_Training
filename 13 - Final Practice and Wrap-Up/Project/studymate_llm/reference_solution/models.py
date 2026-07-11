from dataclasses import dataclass, field


@dataclass
class Document:
    title: str
    content: str
    source: str


@dataclass
class SessionRecord:
    topic: str
    summary: str = ""
    questions: list[str] = field(default_factory=list)
    flashcards: list[dict[str, str]] = field(default_factory=list)
