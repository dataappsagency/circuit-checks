import chromadb
from llama_index.core import Document, MockEmbedding, StorageContext, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
def check():
    coll = chromadb.EphemeralClient().get_or_create_collection("circuit_check")
    index = VectorStoreIndex.from_documents([Document(text="circuit checks integrations")], storage_context=StorageContext.from_defaults(vector_store=ChromaVectorStore(chroma_collection=coll)), embed_model=MockEmbedding(embed_dim=16))
    nodes = index.as_retriever(similarity_top_k=1).retrieve("integrations")
    assert nodes and "circuit" in nodes[0].get_content(), f"nothing retrieved: {nodes}"
    return "indexed 1 document in Chroma, retrieved it"
