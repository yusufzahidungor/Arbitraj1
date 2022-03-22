from binance.client import Client
from binance.enums import *

api_key = ""
api_secret = ""
client = Client(api_key, api_secret)

info = client.get_all_tickers()
listUSDT = []
for sym in info:
    if (sym['symbol'][-1] == 'T') & (sym['symbol'][-2] == 'D') & (sym['symbol'][-3] == 'S') & (sym['symbol'][-4] == 'U'): #'USDT' in sym["symbol"]:
        listUSDT.append(sym["symbol"])
        
for sym in info:
    if (sym['symbol'][-1] == 'C') & (sym['symbol'][-2] == 'T') & (sym['symbol'][-3] == 'B'): #'USDT' in sym["symbol"]:
        # listUSDT.append(sym["symbol"])
        print(sym["symbol"])

list_of_symbols1 = ['BTCUSDT', 'ETHBTC', 'ETHUSDT']
list_of_symbols2 = ['BTCUSDT', 'LTCBTC', 'LTCUSDT']
list_of_symbols2 = ['BTCUSDT', 'BNBBTC', 'BNBUSDT']
list_of_symbols2 = ['BTCUSDT', 'NEOBTC', 'NEOUSDT']
list_of_symbols2 = ['BTCUSDT', 'BCCBTC', 'BCCUSDT']
list_of_symbols2 = ['BTCUSDT', 'GASBTC', 'LTCUSDT']
list_of_symbols2 = ['BTCUSDT', 'LTCBTC', 'LTCUSDT']
list_of_symbols2 = ['BTCUSDT', 'LTCBTC', 'LTCUSDT']
list_of_symbols2 = ['BTCUSDT', 'LTCBTC', 'LTCUSDT']
list_of_symbols2 = ['BTCUSDT', 'LTCBTC', 'LTCUSDT']
list_of_symbols2 = ['BTCUSDT', 'LTCBTC', 'LTCUSDT']



