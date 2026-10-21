from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_milvus import Milvus
def check():
    store = Milvus(embedding_function=DeterministicFakeEmbedding(size=16), connection_args={"uri": "./circuit_lc_milvus.db"}, collection_name="circuit_check", drop_old=True, auto_id=True)
    store.add_texts(["circuit checks integrations", "an unrelated sentence"])
    hits = store.similarity_search("circuit checks integrations", k=1)
    assert hits and hits[0].page_content == "circuit checks integrations", f"wrong hit: {hits}"
    return "wrote 2 vectors to Milvus Lite, found the right one"
