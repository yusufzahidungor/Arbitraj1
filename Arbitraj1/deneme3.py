import ccxt 
import pandas as pd
import talib

exc = ccxt.gateio()

OHLCV = exc.fetchOHLCV('BTC/USDT', timeframe='15m', limit=21)
df = pd.DataFrame(columns=["Open","High","Low","Close","Volume"])

for i in range(len(OHLCV)-1):
    a = OHLCV[i][1]
    b = OHLCV[i][2]
    c = OHLCV[i][3]
    d = OHLCV[i][4]
    e = OHLCV[i][5]
    df = df.append({"Open":a,"High":b,"Low":c,"Close":d,"Volume":e},ignore_index=True)

ccc = df["Close"].to_numpy()
print(df["Close"])
print(df["Close"][len(df)-1])