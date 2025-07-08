# ai/control_layer.py

from fastapi import APIRouter
from scraper.airdrops_fetcher import fetch_airdrops_io, save_to_db
from utils.send_alert import send_telegram_alert

router = APIRouter()

@router.post("/ai/command")
async def handle_ai_command(data: dict):
    command = data.get("command", "").lower()

    if "fetch" in command and "airdrops" in command:
        drops = fetch_airdrops_io()
        save_to_db(drops)
        send_telegram_alert(f"🤖 AI triggered fetch: {len(drops)} airdrops found.")
        return {"status": "success", "message": f"{len(drops)} airdrops fetched."}

    if "status" in command or "rewards" in command:
        return {"status": "ok", "message": "💰 Rewards monitoring coming soon..."}

    return {"status": "error", "message": "Unrecognized command"}
