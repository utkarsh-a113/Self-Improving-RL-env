import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()


class LLMClient:
    def __init__(self, model="openai/gpt-oss-20b", provider="auto"):
        token = os.getenv("HF_TOKEN")

        if not token:
            raise ValueError(
                "HF_TOKEN is missing. Add it to your .env file."
            )

        self.client = InferenceClient(
            api_key=token,
            provider=provider
        )

        self.model = model

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000
        )

        return response.choices[0].message.content