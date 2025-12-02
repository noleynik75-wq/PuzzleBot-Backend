from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Request(BaseModel):
    input: str

@app.post("/webhook")
async def webhook(req: Request):
    # Запрос к ChatGPT
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": req.input}]
    )

    answer = completion.choices[0].message["content"]

    # Возвращаем в формате PuzzleBot
    return {
        "commands": [
            {
                "type": "set_variable",
                "name": "gpt_answer",
                "value": answer
            }
        ]
    }
