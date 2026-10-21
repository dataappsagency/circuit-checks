from langchain_ollama import ChatOllama
from _ollama import MODEL, BASE
def check():
    text = ChatOllama(model=MODEL, base_url=BASE, num_predict=10).invoke("Reply with the word ready.").content
    assert text and text.strip(), "empty reply"
    return f"replied: {text.strip()[:60]}"
