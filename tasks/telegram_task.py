# backend/tasks/telegram_task.py

from telethon.sync import TelegramClient
import os

api_id = os.getenv("TG_API_ID")
api_hash = os.getenv("TG_API_HASH")
phone = os.getenv("TG_PHONE")

def perform_telegram_task(link: str):
    print(f"📲 Joining Telegram airdrop: {link}")
    with TelegramClient("session", api_id, api_hash) as client:
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input("Enter code: "))
        client(JoinChannelRequest(link))
