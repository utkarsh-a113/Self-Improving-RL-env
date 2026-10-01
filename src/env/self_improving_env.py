from src.agents.solver import SolverAgent
from src.agents.critic import CriticAgent
from src.agents.optimizer import OptimizerAgent
from src.grader.programmatic import ProgrammaticGrader
from src.grader.llm_grader import LLMGrader
from src.memory.memory_store import MemoryStore


class SelfImprovingEnv:

    def __init__(self):
        self.solver = SolverAgent()
        self.grader = ProgrammaticGrader()
        self.llm_grader = LLMGrader()
        self.critic = CriticAgent()
        self.optimizer = OptimizerAgent()
        self.memory = MemoryStore()

    def run_episode(self, task):

        print("\n" + "=" * 60)
        print("STARTING EPISODE")
        print("=" * 60)

        print("\n[1] SOLVING TASK...")
        solution = self.solver.solve(task)

        print("\nSOLUTION:")
        print(solution)

        print("\n[2] GRADING...")

        programmatic_reward = self.grader.grade(
            task,
            solution
        )

        llm_result = self.llm_grader.grade(
            task,
            solution
        )

        llm_reward = llm_result["overall"]

        reward = (
            0.3 * programmatic_reward
            + 0.7 * llm_reward
        )

        print(f"PROGRAMMATIC REWARD: {programmatic_reward}")
        print(f"LLM REWARD: {llm_reward}")
        print(f"FINAL REWARD: {reward}")

        print("\n[3] CRITIC ANALYSIS...")

        feedback = self.critic.critique(
            task,
            solution,
            reward
        )

        print("\nFEEDBACK:")
        print(feedback)

        print("\n[4] OPTIMIZING...")

        rule = self.optimizer.optimize(
            task,
            solution,
            feedback,
            reward
        )

        print("\nNEW BEHAVIORAL RULE:")
        print(rule)

        print("\n[5] SAVING TO MEMORY...")

        self.memory.save_lesson(
            rule,
            reward
        )

        print("Lesson saved.")

        return {
            "task": task,
            "solution": solution,
            "reward": reward,
            "feedback": feedback,
            "rule": rule
        }