import ollama
import re

class DeveloperAgent:
    """
    Generates Python OOP code using llama3.
    Writes ONLY valid Python code to a .py file.
    """

    def __init__(self, model="llama3"):
        self.model = model

    def generate_code(self, output_path: str):
        prompt = """
You are a Python developer.

Task:
1. Write Python code demonstrating Object-Oriented Programming
2. After the code, explain the OOP concepts used

Output format:
- Code first
- Explanation after
"""

        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        full_output = response["message"]["content"]

        code = self._extract_python_code(full_output)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(code)

        return full_output  # passed to ArchitectAgent if needed

    def _extract_python_code(self, text: str) -> str:
        """
        Extracts only executable Python code from mixed LLM output.
        """

        # Remove markdown fences if present
        text = text.replace("```python", "").replace("```", "")

        lines = text.splitlines()
        code_lines = []

        for line in lines:
            if (
                line.startswith("class ")
                or line.startswith("def ")
                or line.startswith("import ")
                or line.startswith("from ")
                or code_lines
            ):
                # Stop if explanation clearly starts
                if re.match(r"^\s*[A-Z][a-z].*:", line):
                    break
                code_lines.append(line)

        return "\n".join(code_lines).strip()
