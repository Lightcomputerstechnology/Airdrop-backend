# backend/scraper/airdrops_fetcher.py

import requests
from bs4 import BeautifulSoup
import json

def fetch_airdrops_io():
    url = "https://airdrops.io/latest/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    drops = []
    for card in soup.select(".airdrops .card"):
        title = card.select_one(".card-title").text.strip()
        link = card.select_one("a")["href"]
        description = card.select_one(".card-text").text.strip()
        blockchain = "Ethereum" if "ETH" in description else "Multi-chain"
        reward_info = card.select_one(".reward").text.strip() if card.select_one(".reward") else "Unknown"

        drops.append({
            "title": title,
            "link": link,
            "description": description,
            "blockchain": blockchain,
            "reward": reward_info,
        })

    return drops

def save_to_db(airdrops):
    with open("backend/data/airdrops.json", "w") as f:
        json.dump(airdrops, f, indent=4)
    print(f"[✓] {len(airdrops)} real airdrops saved.")

if __name__ == "__main__":
    print("Fetching verified airdrops from airdrops.io...")
    real_drops = fetch_airdrops_io()
    save_to_db(real_drops)
