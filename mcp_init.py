import mcp_client
from pydantic_ai import Agent

async def get_pydantic_ai_agent():
    client = mcp_client.MCPClient()
    client.load_servers("mcp_config.json")
    tools = await client.start()
    return client, Agent(model='your-llm-here', tools=tools)