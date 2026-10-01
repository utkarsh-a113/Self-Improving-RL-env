import re
class ProgrammaticGrader:

    def grade(self, task, solution):
        """
        Calculate a basic programmatic reward between 0 and 1.
        """

        if not solution or not solution.strip():
            return 0.0

        reward = 0.0

        # -------------------------------------------------
        # 1. Basic response check
        # -------------------------------------------------

        reward += 0.2

        # -------------------------------------------------
        # 2. Check whether the response contains Python
        # -------------------------------------------------

        if "def " in solution:
            reward += 0.2

        # -------------------------------------------------
        # 3. Check for explanation
        # -------------------------------------------------

        explanation_words = [
            "because",
            "complexity",
            "explain",
            "time",
            "space"
        ]

        explanation_score = sum(
            word in solution.lower()
            for word in explanation_words
        )

        if explanation_score >= 2:
            reward += 0.2

        # -------------------------------------------------
        # 4. Check for duplicate-detection concepts
        # -------------------------------------------------

        concepts = [
            "set",
            "hash",
            "duplicate",
            "seen"
        ]

        concept_score = sum(
            concept in solution.lower()
            for concept in concepts
        )

        if concept_score >= 2:
            reward += 0.2

        # -------------------------------------------------
        # 5. Check for reasonable complexity
        # -------------------------------------------------

        if re.search(r"O\s*\(\s*n\s*\)", solution):
            reward += 0.2

        return min(reward, 1.0)

