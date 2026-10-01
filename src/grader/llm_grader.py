import json
from src.llm.llm_client import LLMClient


class LLMGrader:

    def __init__(self):
        self.llm = LLMClient()

    def grade(self, task, solution):

        prompt = f"""
You are an objective evaluator.

Evaluate the following solution to the given task.

TASK:
{task}

SOLUTION:
{solution}

Score the solution from 0.0 to 1.0 based on:

- Correctness
- Completeness
- Reasoning
- Efficiency
- Code quality

Return ONLY valid JSON in this format:

{{
    "correctness": 0.0,
    "completeness": 0.0,
    "reasoning": 0.0,
    "efficiency": 0.0,
    "code_quality": 0.0,
    "overall": 0.0,
    "feedback": "short explanation"
}}
"""

        response = self.llm.generate(prompt)

        try:
            result = json.loads(response)
            return result

        except json.JSONDecodeError:
            return {
                "correctness": 0.0,
                "completeness": 0.0,
                "reasoning": 0.0,
                "efficiency": 0.0,
                "code_quality": 0.0,
                "overall": 0.0,
                "feedback": "Unable to parse grader response."
            }

