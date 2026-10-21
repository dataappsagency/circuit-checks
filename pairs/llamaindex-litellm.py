from llama_index.llms.litellm import LiteLLM
from _ollama import MODEL, BASE
def check():
    text = LiteLLM(model=f"ollama/{MODEL}", api_base=BASE, max_tokens=10).complete("Reply with the word ready.").text
    assert text and text.strip(), "empty reply"
    return f"replied: {text.strip()[:60]}"
