from core import binance_api, strategy
import json
import os

def run_bot():
    candles = binance_api.client.get_klines(symbol="BTCUSDT", interval="1h", limit=50)
    close_prices = [float(candle[4]) for candle in candles]
    rsi_value = strategy.rsi(close_prices)

    if rsi_value < 30:
        order = binance_api.place_order("BTCUSDT", "BUY", 0.001)
        save_log("BUY", order)
    elif rsi_value > 70:
        order = binance_api.place_order("BTCUSDT", "SELL", 0.001)
        save_log("SELL", order)

def save_log(action, data):
    path = "data/logs.json"
    logs = []
    if os.path.exists(path):
        with open(path, 'r') as f:
            logs = json.load(f)
    logs.append({"action": action, "data": data})
    with open(path, 'w') as f:
        json.dump(logs, f, indent=2)
