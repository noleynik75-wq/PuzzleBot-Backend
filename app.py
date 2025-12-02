from fastapi import FastAPI, Request
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend is running!"}


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    if not user_message:
        return {"reply": "Сообщение пустое"}

    # Запрос к OpenAI
    response = client.responses.create(
        model="gpt-4o-mini",
        input=user_message
    )

    bot_reply = response.output_text

    return {
        "reply": bot_reply
    }
