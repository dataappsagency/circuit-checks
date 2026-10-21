from llama_index.llms.ollama import Ollama
from _ollama import MODEL, BASE
def check():
    text = Ollama(model=MODEL, base_url=BASE, request_timeout=300).complete("Reply with the word ready.").text
    assert text and text.strip(), "empty reply"
    return f"replied: {text.strip()[:60]}"
