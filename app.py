import os
import ccxt
import time
import sys
import requests
from flask import Flask
from threading import Thread

app = Flask(__name__)

api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')
exchange = ccxt.bitbank({'apiKey': api_key, 'secret': api_secret})

@app.route('/')
def home():
    return "Bot is running!"

def send_signal_to_gatekeeper(price, delta):
    url = "https://gatekeeper-api.your-domain.com/harvest"
    payload = {"price": price, "delta": delta, "timestamp": time.time()}
    try:
        response = requests.post(url, json=payload)
        print(f"信号送信完了: {response.status_code}")
    except Exception as e:
        print(f"信号送信失敗: {e}")

def run_bot():
    print("ボット起動...")
    previous_price = 0
    while True:
        try:
            ticker = exchange.fetch_ticker('BTC/JPY')
            current_price = ticker['last']
            delta = abs(current_price - previous_price)
            if previous_price != 0 and delta >= 5000:
                send_signal_to_gatekeeper(current_price, delta)
            previous_price = current_price
            print(f"現在のBTC価格: {current_price}")
            sys.stdout.flush()
            time.sleep(60)
        except Exception as e:
            print(f"エラー: {e}")
            sys.stdout.flush()
            time.sleep(60)

if __name__ == '__main__':
    Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
