import litellm
from _ollama import MODEL, BASE
def check():
    r = litellm.completion(model=f"ollama/{MODEL}", api_base=BASE, messages=[{"role": "user", "content": "Reply with the word ready."}], max_tokens=10)
    text = r.choices[0].message.content
    assert text and text.strip(), "empty reply"
    return f"replied: {text.strip()[:60]}"
