# memory_store.py

import json
import os


class MemoryStore:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path
        self.memories = self._load()

    def _load(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_lesson(self, lesson, reward=None):
        memory = {
            "lesson": lesson,
            "reward": reward
        }

        self.memories.append(memory)

        with open(self.file_path, "w") as file:
            json.dump(self.memories, file, indent=4)

    def get_lessons(self):
        return [memory["lesson"] for memory in self.memories]

