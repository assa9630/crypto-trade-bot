import os
from binance.client import Client
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
client = Client(API_KEY, API_SECRET)

def run_trade_logic():
    klines = client.get_klines(symbol='BTCUSDT', interval='15m', limit=100)
    close_prices = [float(k[4]) for k in klines]
    print("檢查策略並執行交易")