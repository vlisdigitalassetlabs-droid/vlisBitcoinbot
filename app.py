import os
import ccxt
import time
import sys
from flask import Flask
from threading import Thread

app = Flask(__name__)

# Bitbankの設定
api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

exchange = ccxt.bitbank({
    'apiKey': api_key,
    'secret': api_secret,
})

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    print("ボット起動...")
    sys.stdout.flush()  # ログを強制出力
    while True:
        try:
            ticker = exchange.fetch_ticker('BTC/JPY')
            print(f"現在のBTC価格: {ticker['last']}")
            sys.stdout.flush()  # ログを強制出力
            time.sleep(60)
        except Exception as e:
            print(f"エラー: {e}")
            sys.stdout.flush()
            time.sleep(60)

if __name__ == '__main__':
    # Flaskとボットを同時起動
    Thread(target=run_bot, daemon=True).start()
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
