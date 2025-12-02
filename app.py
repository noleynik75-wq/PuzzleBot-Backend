import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from openai import OpenAI

app = FastAPI()

# читаем API KEY из переменной окружения
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend is running!"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    # PuzzleBot формирует сообщение в поле "message"
    user_message = data.get("message", "")

    if not user_message:
        return JSONResponse({"reply": "Я не получила текст сообщения."})

    # OpenAI запрос
    response = client.responses.create(
        model="gpt-4o-mini",
        input=user_message
    )

    bot_reply = response.output_text

    return JSONResponse({"reply": bot_reply})
