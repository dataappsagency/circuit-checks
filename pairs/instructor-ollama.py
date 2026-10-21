import instructor
from openai import OpenAI
from pydantic import BaseModel
from _ollama import MODEL, BASE
class City(BaseModel):
    name: str
def check():
    client = instructor.from_openai(OpenAI(base_url=f"{BASE}/v1", api_key="ollama"), mode=instructor.Mode.JSON)
    c = client.chat.completions.create(model=MODEL, response_model=City, max_retries=3, messages=[{"role": "user", "content": "The capital of France, as JSON with a name field."}])
    assert isinstance(c, City) and c.name.strip(), f"no object: {c}"
    return f"structured reply: City(name={c.name[:30]!r})"
