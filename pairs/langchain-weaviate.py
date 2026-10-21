import weaviate
from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_weaviate import WeaviateVectorStore
def check():
    client = weaviate.connect_to_local()
    try:
        store = WeaviateVectorStore.from_texts(["circuit checks integrations", "an unrelated sentence"], DeterministicFakeEmbedding(size=16), client=client, index_name="CircuitCheck")
        hits = store.similarity_search("circuit checks integrations", k=1)
        assert hits and hits[0].page_content == "circuit checks integrations", f"wrong hit: {hits}"
    finally:
        client.close()
    return "wrote 2 vectors to Weaviate, found the right one"
