from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_chroma import Chroma
def check():
    store = Chroma(collection_name="circuit_check", embedding_function=DeterministicFakeEmbedding(size=16))
    store.add_texts(["circuit checks integrations", "an unrelated sentence"])
    hits = store.similarity_search("circuit checks integrations", k=1)
    assert hits and hits[0].page_content == "circuit checks integrations", f"wrong hit: {hits}"
    return "wrote 2 vectors to Chroma, found the right one"
