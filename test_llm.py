from fastapi import FastAPI
from pydantic import BaseModel
from src.llm.llm_client import LLMClient

app = FastAPI()

llm = LLMClient()


class Request(BaseModel):
    prompt: str


@app.post("/generate")
def generate(request: Request):
    response = llm.generate(request.prompt)

    return {
        "response": response
    }