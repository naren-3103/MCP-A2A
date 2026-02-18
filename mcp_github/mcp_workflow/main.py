from agent.llm_agent import LLMAgent
from mcp.host import MCPHost
from tools.document_reader import DocumentReaderTool

tools = [DocumentReaderTool()]
host = MCPHost(tools)

host.add_message("user", "Read the MCP overview document and explain MCP.")
agent = LLMAgent()

host.run(agent)
