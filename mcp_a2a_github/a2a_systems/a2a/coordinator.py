from agents.developer_agent import DeveloperAgent
from agents.architect_agent import ArchitectAgent

def run_a2a_pipeline():
    code_path = "output/generated_code.py"
    explanation_path = "output/code_explanation.txt"
    
    developer = DeveloperAgent()
    architect = ArchitectAgent()
    print('Developing Code')
    # Agent 1: Build code
    developer.generate_code(code_path)
    print('Explaning the Code')
    # Agent 2: Explain code
    architect.explain_code(code_path, explanation_path)

    print("A2A pipeline completed successfully using llama3 and the code is stored in .py file while the explanation is tored in .txtx file i  outputs folder.")
