from studymate_llm.llm_client import LLMClient, PromptGateway


class FakeGateway(PromptGateway):
    def __init__(self, response: str):
        self.response = response
        self.calls = []

    def send(self, prompt: str, *, model: str, api_key: str) -> str:
        self.calls.append(
            {
                "prompt": prompt,
                "model": model,
                "api_key": api_key,
            }
        )
        return self.response


def test_generate_uses_gateway_when_provider_is_env(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "env")
    monkeypatch.setenv("LLM_MODEL", "course-model")
    monkeypatch.setenv("LLM_API_KEY", "test-key")
    gateway = FakeGateway("gateway response")

    client = LLMClient(gateway=gateway)
    result = client.generate("Summarize decorators")

    assert result == "gateway response"
    assert gateway.calls == [
        {
            "prompt": "Summarize decorators",
            "model": "course-model",
            "api_key": "test-key",
        }
    ]


def test_generate_returns_fake_response_by_default(monkeypatch):
    monkeypatch.delenv("LLM_PROVIDER", raising=False)
    client = LLMClient()

    result = client.generate("Python functions are reusable")

    assert result.startswith("FAKE LLM RESPONSE:")
