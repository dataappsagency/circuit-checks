from llama_index.core import Document, MockEmbedding, StorageContext, VectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
def check():
    store = QdrantVectorStore(client=QdrantClient(url="http://localhost:6333"), collection_name="circuit_check_li")
    index = VectorStoreIndex.from_documents([Document(text="circuit checks integrations")], storage_context=StorageContext.from_defaults(vector_store=store), embed_model=MockEmbedding(embed_dim=16))
    nodes = index.as_retriever(similarity_top_k=1).retrieve("integrations")
    assert nodes and "circuit" in nodes[0].get_content(), f"nothing retrieved: {nodes}"
    return "indexed 1 document, retrieved it"
