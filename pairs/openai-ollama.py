from openai import OpenAI
from _ollama import MODEL, BASE
def check():
    r = OpenAI(base_url=f"{BASE}/v1", api_key="ollama").chat.completions.create(model=MODEL, messages=[{"role": "user", "content": "Reply with the word ready."}], max_tokens=10)
    text = r.choices[0].message.content
    assert text and text.strip(), "empty reply"
    return f"replied: {text.strip()[:60]}"
