from haystack import Document
from haystack_integrations.document_stores.chroma import ChromaDocumentStore
def check():
    store = ChromaDocumentStore()
    store.write_documents([Document(content="circuit checks integrations")])
    n = store.count_documents()
    assert n == 1, f"expected 1 document, found {n}"
    return "wrote 1 document to Chroma, counted it back"
