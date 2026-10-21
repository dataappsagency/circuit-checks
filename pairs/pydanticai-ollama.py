from pydantic_ai import Agent
from _ollama import MODEL, BASE
def model():
    try:
        from pydantic_ai.models.openai import OpenAIChatModel as M
    except ImportError:
        from pydantic_ai.models.openai import OpenAIModel as M
    from pydantic_ai.providers.openai import OpenAIProvider
    return M(MODEL, provider=OpenAIProvider(base_url=f"{BASE}/v1", api_key="ollama"))
def check():
    r = Agent(model()).run_sync("Reply with the word ready.")
    text = getattr(r, "output", None) or getattr(r, "data", "")
    assert text and str(text).strip(), "empty reply"
    return f"replied: {str(text).strip()[:60]}"
