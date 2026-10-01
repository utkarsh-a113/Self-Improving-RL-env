# optimizer.py
from src.llm.llm_client import LLMClient


class OptimizerAgent:
    def __init__(self):
        self.llm = LLMClient()

    def optimize(self, task, solution, feedback, reward):
        prompt = f"""
You are a strategy optimization agent.

Your job is to convert critic feedback into a short,
reusable behavioral rule that can help an AI agent
perform better on future tasks.

Task:
{task}

Solution:
{solution}

Reward:
{reward}

Critic feedback:
{feedback}

Create ONE clear and general behavioral rule.

The rule should:
- Be reusable on future tasks
- Be specific enough to be useful
- Not refer to this particular task
- Avoid unnecessary explanation

Return only the behavioral rule.
"""

        rule = self.llm.generate(prompt)

        return rule.strip()

