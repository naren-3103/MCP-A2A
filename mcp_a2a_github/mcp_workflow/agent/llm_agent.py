import ollama
import json

class LLMAgent:
    def __init__(self, model="llama3"):
        self.model = model

    def decide(self, context):
        prompt = f"""
You are an AI agent using Model Context Protocol.

Context:
{context}

If a document needs to be read, respond ONLY with JSON:
{{
  "tool_call": {{
    "name": "read_document",
    "input": {{ "path": "data/mcp_overview.txt" }}
  }}
}}

Otherwise respond:
{{ "final": "<your answer>" }}
"""

        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        content = response["message"]["content"]
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"final": content}
