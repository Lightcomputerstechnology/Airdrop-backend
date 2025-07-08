# backend/utils/send_alert.py

import requests
import os

def send_telegram_alert(message: str):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_USER_ID")

    if not token or not chat_id:
        print("[⚠️] Telegram credentials missing.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("[✅] Telegram alert sent.")
    else:
        print("[❌] Failed to send Telegram alert:", response.text)
