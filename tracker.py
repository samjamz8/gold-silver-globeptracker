import requests
import os

GOLD_API_KEY = os.getenv("goldapi-3ckgqsmkzisjgv-io")
TELEGRAM_TOKEN = os.getenv("8345977870:AAGOh5PRosI_HtgeFLX5nv4zFaKm6GaVQKk")
CHAT_ID = os.getenv("947264440")

GOLD_URL = "https://www.goldapi.io/api/XAU/USD"
SILVER_URL = "https://www.goldapi.io/api/XAG/USD"

HEADERS = {
    "x-access-token": GOLD_API_KEY,
    "Content-Type": "application/json"
}

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

def get_price(url):
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    return data["price"]

gold_price = get_price(GOLD_URL)
silver_price = get_price(SILVER_URL)

send_telegram(f"📊 Gold: ${gold_price}\nSilver: ${silver_price}")
