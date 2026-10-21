import asyncio, os, sys
from langchain_mcp_adapters.client import MultiServerMCPClient
SERVER = os.path.join(os.path.dirname(__file__), "_mcp_server.py")
async def run():
    client = MultiServerMCPClient({"check": {"command": sys.executable, "args": [SERVER], "transport": "stdio"}})
    tools = {t.name: t for t in await client.get_tools()}
    assert "add" in tools, f"tools: {list(tools)}"
    return await tools["add"].ainvoke({"a": 2, "b": 3})
def check():
    out = asyncio.run(run())
    assert "5" in str(out), f"got {out!r}"
    return "LangChain loaded and called a tool from an MCP server (2+3=5)"
