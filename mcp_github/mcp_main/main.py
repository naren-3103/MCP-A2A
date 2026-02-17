from agent.llm_agent import LLMAgent
from mcp.host import MCPHost
from tools.document_reader import DocumentReaderTool

# Initialize MCP tools
tools = [
    DocumentReaderTool()
]

# MCP Host
host = MCPHost(tools)

# User query
host.add_message(
    role="user",
    content=(
        "Read the document at path data/sample_doc.txt "
        "and explain what MCP is."
    )
)


# Real LLM Agent
agent = LLMAgent(model="llama3")

# Run MCP loop
host.run(agent)
 