# run_demo.py


from src.env.self_improving_env import SelfImprovingEnv


env = SelfImprovingEnv()


task = """
Write a Python function that finds duplicate numbers
in a list. Explain the time and space complexity.
"""


result = env.run_episode(task)


print("\n" + "=" * 60)
print("EPISODE COMPLETE")
print("=" * 60)

print(f"\nFinal Reward: {result['reward']}")
print(f"\nLearned Rule: {result['rule']}")

