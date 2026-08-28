import yfinance as yf
from datetime import datetime
import time

try:
    while True:
        current_time = datetime.now().strftime("%m-%d %H:%M")
        print(f"\n[{current_time}]\n")

        apple = yf.Ticker("AAPL")

        price = apple.info.get("currentPrice")
        print(f"Apple Stock Price is at ${price}")

        google = yf.Ticker("GOOG")

        price = google.info.get("currentPrice")
        print(f"\nAlphabet/Google stock is at ${price}")

        meta = yf.Ticker("META")

        price = meta.info.get("currentPrice")
        print(f"\nMeta stock is at ${price}\n")

        time.sleep(600)
except KeyboardInterrupt:
    print("stopping")