from src.llm.llm_client import LLMClient


class CriticAgent:
    def __init__(self):
        self.llm = LLMClient()

    def critique(self, task, solution, reward):
        prompt = f"""
You are a critical evaluation agent.

Analyze the solution below and identify:
1. What was done correctly
2. What was done incorrectly
3. Why the mistakes happened
4. How the agent can improve
5. One reusable lesson for future tasks

Task:
{task}

Solution:
{solution}

Reward:
{reward}

Be specific and constructive.
"""

        feedback = self.llm.generate(prompt)

        return feedback