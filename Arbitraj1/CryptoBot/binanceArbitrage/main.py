from binance.client import Client
from binance.enums import *
import time 
from datetime import datetime
# from listSymbols import list as ls
import pprint
import math

api_key = ""
api_secret = ""
client = Client(api_key, api_secret)

BNB = 'BNB'
BTC = 'BTC'
ETH = 'ETH'
BTCcoin = [100]
BNBcoin = [100]
ETHcoin = [100]
main_Sembol = [BNB,ETH,BTC]
listBNB = []
listBTC = []
listETH = []

BNBBTC = BNB+BTC
BNBETH = BNB+ETH
ETHBTC = ETH+BTC

fee = 0.1*3


tickers = client.get_orderbook_tickers()
for sym in tickers:
    sembol = sym["symbol"]
    if BNB in sembol:
        if (sembol[len(sembol)-1] == 'B') & (sembol[len(sembol)-2] == 'N') & (sembol[len(sembol)-3] == 'B'):
            listBNB.append(sembol)
    elif BTC in sembol:
        if (sembol[len(sembol)-1] == 'C') & (sembol[len(sembol)-2] == 'T') & (sembol[len(sembol)-3] == 'B'):
            listBTC.append(sembol)
    elif ETH in sembol:
        if (sembol[len(sembol)-1] == 'H') & (sembol[len(sembol)-2] == 'T') & (sembol[len(sembol)-3] == 'E'):
            listETH.append(sembol)

# print(client.get_order_book(symbol='VENBNB'))
# office = "Word"
# print (office.split("rd")[0])
#BNB/BTC
for ms in listBNB:
    for listbtc in listBTC:
        s2 = ms.split(BNB)[0]
        s3 = listbtc.split(BTC)[0]
        if s2 == s3:
            sembol1 = BNBBTC
            sembol2 = s2 + BNB
            sembol3 = s3 + BTC

            s1 = s3 + BTC
            s2 = s2 + BNB
            s3 = BNBBTC

            depth1 = client.get_order_book(symbol=sembol1)
            depth2 = client.get_order_book(symbol=sembol2)
            depth3 = client.get_order_book(symbol=sembol3)

            d1 = client.get_order_book(symbol=sembol3)
            d2 = client.get_order_book(symbol=sembol2)
            d3 = client.get_order_book(symbol=sembol1)

            print("************************************************************")
            if (len(depth1['bids']) != 0) & (len(depth2['asks']) != 0) & (len(depth3['bids']) != 0):
                #Sıra1
                price1 = depth1['bids'][0][0]
                price2 = depth2['asks'][0][0]
                price3 = depth3['bids'][0][0]

                rate1 = float(price1)
                rate2 = float(price3)/float(price2)
                if float(rate1)<float(rate2):
                    arb_profit = ((rate2-rate1)/rate1)*100
                    arb_profit_adjust = float(arb_profit) - float(fee)
                    if arb_profit_adjust > 0:
                        print("Alınan Coinler : "+sembol1+" -> "+sembol2+" -> "+ sembol3)
                        print("Baslangic : "+BTCcoin[-1]+"\nSonunda : "+(BTCcoin[-1]*arb_profit_adjust)+BTCcoin[-1]+"\n Kar : %"+arb_profit_adjust)
                        BTCcoin.append((BTCcoin[-1]*arb_profit_adjust)+BTCcoin[-1])
                    else:
                        print("Semboller : "+sembol1+" -> "+sembol2+" -> "+ sembol3)
                        print("Kar oranı yetersiz")
                else:
                    print("Semboller : "+sembol1+" -> "+sembol2+" -> "+ sembol3)
                    print("Kar oranı yok")

                #Sıra2
                price1 = d1['bids'][0][0]
                price2 = d2['asks'][0][0]
                price3 = d3['bids'][0][0]

                rate1 = float(price1)
                rate2 = float(price3)/float(price2)
                if float(rate1)<float(rate2):
                    arb_profit = ((rate2-rate1)/rate1)*100
                    arb_profit_adjust = float(arb_profit) - float(fee)
                    if arb_profit_adjust > 0:
                        print("Alınan Coinler : "+s1+" -> "+s2+" -> "+ s3)
                        print("Baslangic : "+BTCcoin[-1]+"\nSonunda : "+(BTCcoin[-1]*arb_profit_adjust)+BTCcoin[-1]+"\n Kar : %"+arb_profit_adjust)
                        BTCcoin.append((BTCcoin[-1]*arb_profit_adjust)+BTCcoin[-1])
                    else:
                        print("Semboller : "+s1+" -> "+s2+" -> "+ s3)
                        print("Kar oranı yetersiz")
                else:
                    print("Semboller : "+s1+" -> "+s2+" -> "+ s3)
                    print("Kar oranı yok")

                

            else:
                print("Semboller : "+sembol1+" -> "+sembol2+" -> "+ sembol3)
                print("Sembol karsiligi yok")
    print("BTC Son Durum: "+str(BTCcoin[-1]))


for ms in listBNB:
    for listbtc in listETH:
        s2 = ms.split(BNB)[0]
        s3 = listbtc.split(ETH)[0]
        if s2 == s3:
            sembol1 = BNBETH
            sembol2 = s2 + BNB
            sembol3 = s3 + ETH

            depth1 = client.get_order_book(symbol=sembol1)
            depth2 = client.get_order_book(symbol=sembol2)
            depth3 = client.get_order_book(symbol=sembol3)

            print("************************************************************")
            if (len(depth1['bids']) != 0) & (len(depth2['asks']) != 0) & (len(depth3['bids']) != 0):
                price1 = depth1['bids'][0][0]
                price2 = depth2['asks'][0][0]
                price3 = depth3['bids'][0][0]

                rate1 = float(price1)
                rate2 = float(price3)/float(price2)
                if float(rate1)<float(rate2):
                    arb_profit = ((rate2-rate1)/rate2)*100
                    arb_profit_adjust = float(arb_profit) - float(fee)
                    if arb_profit_adjust > 0:
                        print("Alınan Coinler : "+sembol1+" -> "+sembol2+" -> "+ sembol3)
                        print("Baslangic : "+ETHcoin[-1]+"\nSonunda : "+(ETHcoin[-1]*arb_profit_adjust)+ETHcoin[-1]+"\n Kar : %"+arb_profit_adjust)
                        BTCcoin.append((ETHcoin[-1]*arb_profit_adjust)+ETHcoin[-1])
                    else:
                        print("Semboller : "+sembol1+" -> "+sembol2+" -> "+ sembol3)
                        print("Kar oranı yetersiz")
                else:
                    print("Semboller : "+sembol1+" -> "+sembol2+" -> "+ sembol3)
                    print("Kar oranı yok")
            else:
                print("Semboller : "+sembol1+" -> "+sembol2+" -> "+ sembol3)
                print("Sembol karsiligi yok")
    print("ETH Son Durum: "+str(ETHcoin[-1]))

print("ETH Son Durum: "+str(ETHcoin[-1]))
print("BTC Son Durum: "+str(BTCcoin[-1]))


