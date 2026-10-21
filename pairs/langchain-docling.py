from langchain_docling import DoclingLoader
from _doc import sample
def check():
    docs = DoclingLoader(file_path=sample()).load()
    text = " ".join(d.page_content for d in docs)
    assert "integrations run" in text, f"text not found: {text[:200]!r}"
    return f"converted a document into {len(docs)} LangChain document(s)"
