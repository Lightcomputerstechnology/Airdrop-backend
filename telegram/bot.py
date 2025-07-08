# backend/telegram/bot.py

from fastapi import APIRouter, Request
import os

router = APIRouter()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
USER_ID = os.getenv("TELEGRAM_USER_ID")

@router.post(f"/telegram/{TELEGRAM_TOKEN}")
async def telegram_webhook(req: Request):
    data = await req.json()
    print("📩 Incoming Telegram Message:", data)

    # Optional: respond to commands if needed
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        if text == "/start":
            return {"text": "Welcome! This is your airdrop bot."}

    return {"ok": True}
