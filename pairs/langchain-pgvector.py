from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_postgres import PGVector
def check():
    store = PGVector(embeddings=DeterministicFakeEmbedding(size=16), collection_name="circuit_check",
                     connection="postgresql+psycopg://postgres:postgres@localhost:5432/postgres", pre_delete_collection=True)
    store.add_texts(["circuit checks integrations", "an unrelated sentence"])
    hits = store.similarity_search("circuit checks integrations", k=1)
    assert hits and hits[0].page_content == "circuit checks integrations", f"wrong hit: {hits}"
    return "wrote 2 vectors with PGVector, found the right one"
