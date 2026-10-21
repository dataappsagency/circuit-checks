from haystack_integrations.components.generators.ollama import OllamaGenerator
from _ollama import MODEL, BASE
def check():
    r = OllamaGenerator(model=MODEL, url=BASE, generation_kwargs={"num_predict": 10}).run(prompt="Reply with the word ready.")
    text = (r.get("replies") or [""])[0]
    assert text.strip(), "empty reply"
    return f"replied: {text.strip()[:60]}"
