from typing import TypedDict
from langgraph.graph import END, StateGraph
from langgraph.checkpoint.postgres import PostgresSaver
DSN = "postgresql://postgres:postgres@localhost:5432/postgres"
class S(TypedDict):
    n: int
def check():
    g = StateGraph(S)
    g.add_node("inc", lambda s: {"n": s["n"] + 1})
    g.set_entry_point("inc"); g.add_edge("inc", END)
    with PostgresSaver.from_conn_string(DSN) as saver:
        saver.setup()
        app = g.compile(checkpointer=saver)
        cfg = {"configurable": {"thread_id": "circuit-check"}}
        out = app.invoke({"n": 1}, cfg)
        saved = app.get_state(cfg).values
    assert out["n"] == 2 and saved.get("n") == 2, f"state {out} / {saved}"
    return "ran a graph and read its checkpoint back from Postgres"
