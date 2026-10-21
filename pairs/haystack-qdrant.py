from haystack import Document
from haystack_integrations.document_stores.qdrant import QdrantDocumentStore
def check():
    store = QdrantDocumentStore(url="http://localhost:6333", index="circuit_check_hs", embedding_dim=4, recreate_index=True)
    store.write_documents([Document(content="circuit checks integrations", embedding=[0.1, 0.2, 0.3, 0.4])])
    n = store.count_documents()
    assert n == 1, f"expected 1 document, found {n}"
    return "wrote 1 document, counted it back"
