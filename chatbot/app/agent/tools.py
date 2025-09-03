from langchain_mcp_adapters.client import MultiServerMCPClient
from app.core.config import  settings

zahub_mcp_host= settings.zahub_mcp_host
zahub_mcp_port= settings.zahub_mcp_port

async def load_tools():
    client = MultiServerMCPClient(
        {
             "zahub-pizza": {
                 "url": f"http://{zahub_mcp_host}:{zahub_mcp_port}/zahub-pizza-mcp/mcp/",
                "transport": "streamable_http",
            },
        }
    )
    # It is possible to create a session for each mcp server and list tools independently.
    tools = await client.get_tools()
    return tools


