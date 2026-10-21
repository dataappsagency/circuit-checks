from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_redis import RedisConfig, RedisVectorStore
def check():
    store = RedisVectorStore(DeterministicFakeEmbedding(size=16), config=RedisConfig(index_name="circuit_check", redis_url="redis://localhost:6379"))
    store.add_texts(["circuit checks integrations", "an unrelated sentence"])
    hits = store.similarity_search("circuit checks integrations", k=1)
    assert hits and hits[0].page_content == "circuit checks integrations", f"wrong hit: {hits}"
    return "wrote 2 vectors to Redis, found the right one"
