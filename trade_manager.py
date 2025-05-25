import os
from binance.client import Client
from dotenv import load_dotenv
from record import record_to_notion
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
client = Client(API_KEY, API_SECRET)

def run_trade_logic():
    klines = client.get_klines(symbol='BTCUSDT', interval='15m', limit=100)
    close_prices = [float(k[4]) for k in klines]

    # 假設符合策略，模擬交易資料
    sample_trade = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "symbol": "BTCUSDT",
        "side": "LONG",
        "entry_price": 67000.0,
        "exit_price": 73700.0,
        "profit": 10.0,
        "strategy": "RSI-Buy-Dip"
    }

    record_to_notion(sample_trade)
    print("已寫入 Notion:", sample_trade)