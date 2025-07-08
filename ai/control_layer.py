# ai/control_layer.py

from fastapi import APIRouter
from scraper.airdrops_fetcher import fetch_airdrops_io, save_to_db, notify_new_drops
from scripts.automation_runner import run_automation
from utils.send_alert import send_telegram_alert

router = APIRouter()

@router.post("/ai/command")
async def handle_ai_command(data: dict):
    command = data.get("command", "").lower()

    if "fetch" in command and "airdrops" in command:
        drops = fetch_airdrops_io()
        save_to_db(drops)
        notify_new_drops(drops)
        send_telegram_alert(f"🤖 AI triggered fetch: {len(drops)} airdrops found.")
        return {"status": "success", "message": f"{len(drops)} airdrops fetched."}

    if "run" in command and "tasks" in command:
        run_automation()
        return {"status": "success", "message": "✅ Tasks automation completed."}

    if "status" in command:
        return {"status": "ok", "message": "System is live 🔋"}

    return {"status": "error", "message": "Unrecognized command"}


# ✅ NEW: GET Endpoint to trigger fetch externally
@router.get("/run/fetch")
async def run_fetch_public():
    drops = fetch_airdrops_io()
    save_to_db(drops)
    notify_new_drops(drops)
    send_telegram_alert(f"🌐 External trigger: {len(drops)} airdrops fetched.")
    return {"status": "success", "message": f"{len(drops)} airdrops fetched via public URL."}


# ✅ NEW: GET Endpoint to trigger bot automation externally
@router.get("/run/automation")
async def run_tasks_public():
    run_automation()
    return {"status": "success", "message": "✅ Airdrop task automation complete (external trigger)"}
