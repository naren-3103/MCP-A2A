class MCPHost:
    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}
        self.context = []

    def add_message(self, role, content):
        self.context.append({
            "role": role,
            "content": content
        })

    def run(self, agent):
        while True:
            decision = agent.decide(self.context)

            if "final" in decision:
                print("\n✅ FINAL ANSWER:\n")
                print(decision["final"])
                break

            tool_call = decision["tool_call"]
            tool = self.tools[tool_call["name"]]

            print(f"\n🔧 MCP executing tool: {tool.name}")

            result = tool.run(tool_call["input"])

            self.add_message(
                role="tool",
                content=f"Tool {tool.name} output:\n{result}"
            )
