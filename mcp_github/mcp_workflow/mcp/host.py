import mlflow
from datetime import datetime

class MCPHost:
    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}
        self.context = []

    def add_message(self, role, content):
        self.context.append({"role": role, "content": content})

    def run(self, agent):
        mlflow.set_experiment("mcp_agent_execution")

        with mlflow.start_run(run_name=f"mcp_run_{datetime.now()}"):
            mlflow.log_param("initial_user_message", self.context[0]["content"])
            step = 0

            while True:
                decision = agent.decide(self.context)

                if "final" in decision:
                    mlflow.log_metric("steps", step)
                    mlflow.log_text(decision["final"], "final_answer.txt")
                    print(decision["final"])
                    break

                tool_call = decision["tool_call"]
                tool = self.tools[tool_call["name"]]
                result = tool.run(tool_call["input"])

                mlflow.log_text(result, f"tool_{step}_output.txt")
                self.add_message("tool", result)
                step += 1
