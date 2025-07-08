# scripts/automation_runner.py

import json
import time
from utils.send_alert import send_telegram_alert
from tasks.twitter_task import perform_twitter_task
from tasks.telegram_task import perform_telegram_task
import os

def load_airdrops():
    file_path = os.path.join("data", "airdrops.json")
    with open(file_path, "r") as f:
        return json.load(f)

def run_automation():
    print("⚙️ Running airdrop automation...")
    drops = load_airdrops()
    count = 0

    for drop in drops:
        for task in drop.get("tasks", []):
            task_type = task.get("type")
            url = task.get("actionURL")

            if task_type == "twitter":
                perform_twitter_task(url)
                count += 1
            elif task_type == "telegram":
                perform_telegram_task(url)
                count += 1

        time.sleep(2)  # Delay between drops

    send_telegram_alert(f"✅ Completed {count} automated tasks.")

if __name__ == "__main__":
    run_automation()
