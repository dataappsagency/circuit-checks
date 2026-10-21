from llama_index.readers.docling import DoclingReader
from _doc import sample
def check():
    docs = DoclingReader().load_data(file_path=sample())
    text = " ".join(d.text for d in docs)
    assert "integrations run" in text, f"text not found: {text[:200]!r}"
    return f"converted a document into {len(docs)} LlamaIndex document(s)"
