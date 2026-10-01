from src.llm.llm_client import LLMClient
from src.memory.memory_store import MemoryStore


class SolverAgent:
    def __init__(self):
        self.llm = LLMClient()
        self.memory = MemoryStore()

    def solve(self, task):
        lessons = self.memory.get_lessons()

        if lessons:
            previous_lessons = "\n".join(
                f"- {lesson}" for lesson in lessons
            )
        else:
            previous_lessons = "No previous lessons available."

        prompt = f"""
You are a problem-solving agent that improves over time.

Here are lessons learned from previous tasks:

{previous_lessons}

Use these lessons when they are relevant to the current task.

Current task:
{task}

Provide:
1. Your solution
2. Your reasoning
3. Any important assumptions
"""

        response = self.llm.generate(prompt)

        return response