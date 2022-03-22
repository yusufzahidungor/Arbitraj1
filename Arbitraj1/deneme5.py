from binance.client import Client
from binance.enums import *

api_key = ""
api_secret = ""
client = Client(api_key, api_secret)


# info = client.get_order_book(symbol='BCSCBTC')

# print(info)


info = client.get_all_tickers()
listUSDT = []
for sym in info:
    if (sym['symbol'][-1] == 'T') & (sym['symbol'][-2] == 'D') & (sym['symbol'][-3] == 'S') & (sym['symbol'][-4] == 'U'): #'USDT' in sym["symbol"]:
        listUSDT.append(sym["symbol"])



for sym in info:
    if (sym['symbol'][-1] == 'C') & (sym['symbol'][-2] == 'T') & (sym['symbol'][-3] == 'B'): #'USDT' in sym["symbol"]:
        symbol = sym["symbol"]
        info = client.get_order_book(symbol=sym["symbol"])
        if len(info['bids']) != 0:
            info1 = client.get_symbol_info(symbol)
            a1 = info1['baseAsset']
            if (a1+'USDT') in listUSDT:
                # print("BTCUSDT - "+symbol+" - "+(a1+'USDT'))
                s1 = 'BTCUSDT'
                s2 = symbol
                s3 = a1+'USDT'
                depth1 = client.get_order_book(symbol=s1)
                depth2 = client.get_order_book(symbol=s2)
                depth3 = client.get_order_book(symbol=s3)
                price1 = float(depth1['bids'][0][0])
                price2 = float(depth2['asks'][0][0])
                price3 = float(depth3['bids'][0][0])
                a = 100/price1
                b = a/price2
                c = b*price3

                perc = c-0.15

                # if float(price1)<float(price3/price2):
                if (perc>100):
                    print(s1 + "- "+str(price1))
                    print(s2 + "- "+str(price2))
                    print(s3 + "- "+str(price3))
                    print("%"+perc-100)
                    print("*************************")