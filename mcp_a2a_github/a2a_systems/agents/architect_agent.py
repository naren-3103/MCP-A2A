import ollama

class ArchitectAgent:
    """
    Explains OOP concepts used in the generated code.
    Writes ONLY explanation to a .txt file.
    """

    def __init__(self, model="llama3"):
        self.model = model

    def explain_code(self, code_path: str, output_path: str):
        with open(code_path, "r", encoding="utf-8") as f:
            code = f.read()

        prompt = f"""
You are a software architect.

Explain the Object-Oriented Programming concepts used
in the following Python code.

Focus on:
- Classes
- Encapsulation
- Constructors
- Methods
- Reusability

Do NOT rewrite the code.

CODE:
{code}
"""

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        explanation = response["message"]["content"]

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(explanation.strip())
