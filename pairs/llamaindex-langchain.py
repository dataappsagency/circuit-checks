from langchain_core.language_models.fake import FakeListLLM
from llama_index.llms.langchain import LangChainLLM
def check():
    text = LangChainLLM(llm=FakeListLLM(responses=["ready"])).complete("Reply with the word ready.").text
    assert text.strip() == "ready", f"got {text!r}"
    return "LlamaIndex called a LangChain LLM and got its answer"
