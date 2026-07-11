import os
from typing import Optional


class PromptGateway:
    def send(self, prompt: str, *, model: str, api_key: str) -> str:
        raise NotImplementedError


class EchoGateway(PromptGateway):
    def send(self, prompt: str, *, model: str, api_key: str) -> str:
        preview = prompt[:120].replace("\n", " ")
        return (
            f"ENV LLM STUB [{model}] using key '{api_key[:4]}***': "
            f"{preview}..."
        )


class LLMClient:
    def __init__(self, gateway: Optional[PromptGateway] = None):
        self.gateway = gateway or EchoGateway()

    def generate(self, prompt: str) -> str:
        provider = os.getenv("LLM_PROVIDER", "fake").strip().lower()
        if provider == "env":
            model = os.getenv("LLM_MODEL", "study-small")
            api_key = os.getenv("LLM_API_KEY", "replace-me")
            return self.gateway.send(prompt, model=model, api_key=api_key)

        preview = prompt[:120].replace("\n", " ")
        return f"FAKE LLM RESPONSE: {preview}..."
