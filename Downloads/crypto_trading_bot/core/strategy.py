import numpy as np

def rsi(prices, period=14):
    delta = np.diff(prices)
    gain = (delta > 0) * delta
    loss = (delta < 0) * -delta
    avg_gain = np.mean(gain[-period:])
    avg_loss = np.mean(loss[-period:])
    rs = avg_gain / avg_loss if avg_loss != 0 else 0
    return 100 - (100 / (1 + rs))
