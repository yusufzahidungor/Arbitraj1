from math import pi
from os import system
import time
from binance.client import Client
from binance.enums import *
from datetime import datetime
import pandas as pd
from globalArbitrage import ccxt as gac
from binanceArbitrage import main as bam

api_key = "NPQ64sO3Lo8y8o9W3hNeIp8YggRCx6zg6p41NxHBvY4wvBdapdkZqZxYk7uajhlS"
api_secret = "zWGaBT5zA2Nk6c2EgzlFCYUctSKxizexPC7dJHs4m9yc4uur7ENHBa3mEBOckOZD"
client = Client(api_key, api_secret)
# print(client.get_server_time())
# print(client.get_exchange_info())
# print(client.get_account_snapshot(type='SPOT'))
# print(client.get_trade_fee(symbol='BTCUSDT'))
# print(client.get_asset_balance(asset='BTC'))
# print(client.get_account_status())
# print(client.get_my_trades(symbol='BNBBTC'))
# print(client.get_avg_price(symbol='BTCUSDT'))



def startMenu():
    print("*****************************************")
    print(nowTime("Saat"))
    print("1-Binance bagli mi ?")
    print("2-Toplam varlik ne kadar ?")
    print("3-BINANCE Arbitraj botunu baslat !!!")
    print("4-Global Arbitrai baslat")
    print("*-Cikis")
    print()

    startMenuResult = input("Lutfen bir deger girin : ")

    if startMenuResult == "1":
        isConnect()
    elif startMenuResult == "2":
        account()
    elif startMenuResult == "3":
        bam.run()
    elif startMenuResult == "4":
        gac.run()
    elif startMenuResult == "*":
        pass
    else:
        print("Yanlis tusa bastiniz. Lutfen tekrar deneyin.")
        startMenu()

def nowTime(contex):
    print(contex+": {}".format(str(datetime.now())))

def account():
    try:
        account = client.get_account()
        sum = 0
        df = pd.DataFrame(columns=["SEMBOL","Varlik","USD Karsiligi"])
        for crypto in account["balances"]:
            if float(crypto["free"]) != 0:
                price = client.get_orderbook_ticker(symbol=crypto["asset"]+"USDT")
                usd = float(price["bidPrice"])*float(crypto["free"])
                df = df.append({"SEMBOL":crypto["asset"],"Varlik":crypto["free"],"USD Karsiligi":usd},ignore_index=True)
                sum = sum + usd
        print(df)
        price_TRY = client.get_orderbook_ticker(symbol="USDTTRY")
        print("Toplam Varlık = $"+str(sum)+"~ ₺"+str(sum*float(price_TRY["bidPrice"])))
    except Exception as e:
        print("!!!HATA!!! : "+ e)
        startMenu()

def isConnect():
    try:
        ping = client.ping()
        systemStatus = client.get_system_status()
        a = systemStatus["status"]
        if (ping == {}) & (systemStatus["status"] == 0):
            print("Binance Basarili Sekilde Bagli\n Ping=Var & Statu=Normal(0)")
            startMenu()
        elif (ping != "") & (systemStatus["status"] == 1):
            print("BINANCE BASARILI SEKILDE BAGLANMADI\n")
            print("PING :"+ping)
            print("STATU :"+systemStatus["msg"])
            startMenu()
        else:
            print("!!!Beklenmedik Hata!!!")
            startMenu()
    except Exception as e:
        print("!!!HATA!!! : "+ e)
        startMenu()

if __name__ == "__main__":
    startMenu()
