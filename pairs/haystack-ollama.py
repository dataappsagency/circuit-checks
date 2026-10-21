from haystack.dataclasses import ChatMessage
from _ollama import MODEL, BASE
def check():
    # ollama-haystack ships a chat generator; older releases also had OllamaGenerator.
    from haystack_integrations.components.generators.ollama import OllamaChatGenerator
    r = OllamaChatGenerator(model=MODEL, url=BASE, generation_kwargs={"num_predict": 10}).run(messages=[ChatMessage.from_user("Reply with the word ready.")])
    text = r["replies"][0].text if r.get("replies") else ""
    assert text and text.strip(), "empty reply"
    return f"replied: {text.strip()[:60]}"
