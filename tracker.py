import requests
import time

GOLD_API_KEY = "goldapi-3ckgqsmkzisjgv-io"
TELEGRAM_TOKEN = "8345977870:AAGOh5PRosI_HtgeFLX5nv4zFaKm6GaVQKk"
CHAT_ID = "947264440"

GOLD_URL = "https://www.goldapi.io/api/XAU/USD"
SILVER_URL = "https://www.goldapi.io/api/XAG/USD"

HEADERS = {
    "x-access-token": GOLD_API_KEY,
    "Content-Type": "application/json"
}

last_gold_price = None
last_silver_price = None

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def get_price(url):
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    return data["price"]

while True:
    try:
        gold_price = get_price(GOLD_URL)
        silver_price = get_price(SILVER_URL)

        if last_gold_price:
            if abs(gold_price - last_gold_price) > 5:
                send_telegram(f"🚨 Gold price changed! Now: ${gold_price}")

        if last_silver_price:
            if abs(silver_price - last_silver_price) > 0.2:
                send_telegram(f"🚨 Silver price changed! Now: ${silver_price}")

        last_gold_price = gold_price
        last_silver_price = silver_price

        time.sleep(600)

    except Exception as e:
        time.sleep(60)
