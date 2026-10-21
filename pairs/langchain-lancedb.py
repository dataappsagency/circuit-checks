from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_community.vectorstores import LanceDB
def check():
    store = LanceDB(uri="/tmp/circuit_lc_lancedb", embedding=DeterministicFakeEmbedding(size=16), table_name="circuit_check", mode="overwrite")
    store.add_texts(["circuit checks integrations", "an unrelated sentence"])
    hits = store.similarity_search("circuit checks integrations", k=1)
    assert hits and hits[0].page_content == "circuit checks integrations", f"wrong hit: {hits}"
    return "wrote 2 vectors to LanceDB, found the right one"
