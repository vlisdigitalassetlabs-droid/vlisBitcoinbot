import os
import ccxt
import time
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    print("ボット起動...")
    # (ここに以前のAPIキー設定とwhileループのコードをそのまま入れてください)

if __name__ == '__main__':
    # WebサーバーとBotを同時に動かす
    Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
