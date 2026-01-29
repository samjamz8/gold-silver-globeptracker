import os
import requests
import sys

GOLD_API_KEY = os.getenv("GOLD_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not all([GOLD_API_KEY, TELEGRAM_TOKEN, CHAT_ID]):
    print("Missing environment variables")
    sys.exit(0)

HEADERS = {
    "x-access-token": GOLD_API_KEY,
    "Content-Type": "application/json"
}

URLS = {
    "Gold USD": "https://www.goldapi.io/api/XAU/USD",
    "Gold INR": "https://www.goldapi.io/api/XAU/INR",
    "Silver USD": "https://www.goldapi.io/api/XAG/USD",
    "Silver INR": "https://www.goldapi.io/api/XAG/INR"
}

def get_price(url):
    r = requests.get(url, headers=HEADERS, timeout=15)
    data = r.json()
    price = data.get("price")
    if price is None:
        print("API error:", data)
        return "N/A"
    return price

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload, timeout=15)

lines = ["📊 Gold & Silver Prices\n"]

for name, url in URLS.items():
    price = get_price(url)
    lines.append(f"{name}: {price}")

message = "\n".join(lines)
send_telegram(message)
