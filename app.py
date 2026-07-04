import ccxt
import os
import time

api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('API_SECRET')

exchange = ccxt.bitbank({
    'apiKey': api_key,
    'secret': api_secret,
})

def run_bot():
    print("ボット起動...")
    while True:
        try:
            ticker = exchange.fetch_ticker('BTC/JPY')
            print(f"現在のBTC価格: {ticker['last']}")
            time.sleep(60)
        except Exception as e:
            print(f"エラー: {e}")
            time.sleep(60)

if __name__ == '__main__':
    run_bot()
