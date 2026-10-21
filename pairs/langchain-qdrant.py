from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_qdrant import QdrantVectorStore
def check():
    store = QdrantVectorStore.from_texts(["circuit checks integrations", "an unrelated sentence"], DeterministicFakeEmbedding(size=16),
                                         url="http://localhost:6333", collection_name="circuit_check", force_recreate=True)
    hits = store.similarity_search("circuit checks integrations", k=1)
    assert hits and hits[0].page_content == "circuit checks integrations", f"wrong hit: {hits}"
    return "wrote 2 vectors, found the right one"
