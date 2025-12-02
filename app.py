from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Request(BaseModel):
    message: str

@app.post("/chat")
def chat(req: Request):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": req.message}
        ]
    )

    answer = response.choices[0].message["content"]
    return {"answer": answer}


@app.get("/")
def root():
    return {"status": "ok", "message": "Backend is running!"}
