from crewai import Agent, Crew, LLM, Task
from _ollama import MODEL, BASE
def check():
    llm = LLM(model=f"ollama/{MODEL}", base_url=BASE)
    agent = Agent(role="Greeter", goal="Say ready", backstory="You reply in one word.", llm=llm, allow_delegation=False, verbose=False)
    task = Task(description="Reply with the word ready.", expected_output="One word.", agent=agent)
    out = str(Crew(agents=[agent], tasks=[task], verbose=False).kickoff())
    assert out.strip(), "empty crew output"
    return f"crew replied: {out.strip()[:60]}"
