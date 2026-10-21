from langchain_litellm import ChatLiteLLM
from _ollama import MODEL, BASE
def check():
    text = ChatLiteLLM(model=f"ollama/{MODEL}", api_base=BASE, max_tokens=10).invoke("Reply with the word ready.").content
    assert text and text.strip(), "empty reply"
    return f"replied: {text.strip()[:60]}"
