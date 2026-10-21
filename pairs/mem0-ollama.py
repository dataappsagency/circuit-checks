from mem0 import Memory
from _ollama import MODEL, BASE, EMBED
def check():
    m = Memory.from_config({
        "llm": {"provider": "ollama", "config": {"model": MODEL, "ollama_base_url": BASE}},
        "embedder": {"provider": "ollama", "config": {"model": EMBED, "ollama_base_url": BASE}},
        "vector_store": {"provider": "qdrant", "config": {"host": "localhost", "port": 6333, "collection_name": "circuit_check_mem0", "embedding_model_dims": 768}},
    })
    m.add("I prefer tea to coffee.", user_id="circuit", infer=False)
    hits = m.search("What do I drink?", filters={"user_id": "circuit"})
    items = hits.get("results", hits) if isinstance(hits, dict) else hits
    assert items, "nothing found"
    return f"stored a memory and found it ({len(items)} result)"
