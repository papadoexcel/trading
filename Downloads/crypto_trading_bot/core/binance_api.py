import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")

client = Client(api_key, api_secret)

def get_balance():
    return client.get_account()

def place_order(symbol, side, quantity):
    return client.order_market(symbol=symbol, side=side, quantity=quantity)
