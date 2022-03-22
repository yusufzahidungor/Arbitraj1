import ccxt
from ccxt.base import exchange
import pandas as pd
import time

list_Exchange = []

for exc in ccxt.exchanges:
    list_Exchange.append(exc)

for i in range(len(list_Exchange)):
    print(str(i)+"-"+str(list_Exchange[i]))

ExchangeId1 = input("1. Borsayı Secin :")
ExchangeId2 = input("2. Borsayı Secin :")

switchExchangeName = {
    "0" : "aax",
    "1" : "aofex",
    "2" : "ascendex",
    "3" : "bequant",
    "4" : "bibox",
    "5" : "bigone",
    "6" : "binance",
    "7" : "binancecoinm",
    "8" : "binanceus",
    "9" : "binanceusdm",
    "10" : "bit2c",
    "11" : "bitbank",
    "12" : "bitbay",
    "13" : "bitbns",
    "14" : "bitcoincom",
    "15" : "bitfinex",
    "16" : "bitfinex2",
    "17" : "bitflyer",
    "18" : "bitforex",
    "19" : "bitget",
    "20" : "bithumb",
    "21" : "bitmart",
    "22" : "bitmex",
    "23" : "bitpanda",
    "24" : "bitrue",
    "25" : "bitso",
    "26" : "bitstamp",
    "27" : "bitstamp1",
    "28" : "bittrex",
    "29" : "bitvavo",
    "30" : "bl3p",
    "31" : "btcalpha",
    "32" : "btcbox",
    "33" : "btcmarkets",
    "34" : "btctradeua",
    "35" : "btcturk",
    "36" : "buda",
    "37" : "bw",
    "38" : "bybit",
    "39" : "bytetrade",
    "40" : "cdax",
    "41" : "cex",
    "42" : "coinbase",
    "43" : "coinbaseprime",
    "44" : "coinbasepro",
    "45" : "coincheck",
    "46" : "coinex",
    "47" : "coinfalcon",
    "48" : "coinmarketcap",
    "49" : "coinmate",
    "50" : "coinone",
    "51" : "coinspot",
    "52" : "crex24",
    "53" : "currencycom",
    "54" : "delta",
    "55" : "deribit",
    "56" : "digifinex",
    "57" : "eqonex",
    "58" : "equos",
    "59" : "exmo",
    "60" : "flowbtc",
    "61" : "ftx",
    "62" : "ftxus",
    "63" : "gateio",
    "64" : "gemini",
    "65" : "hitbtc",
    "66" : "hitbtc3",
    "67" : "hollaex",
    "68" : "huobi",
    "69" : "huobijp",
    "70" : "huobipro",
    "71" : "idex",
    "72" : "independentreserve",
    "73" : "indodax",
    "74" : "itbit",
    "75" : "kraken",
    "76" : "kucoin",
    "77" : "kuna",
    "78" : "latoken",
    "79" : "latoken1",
    "80" : "lbank",
    "81" : "liquid",
    "82" : "luno",
    "83" : "lykke",
    "84" : "mercado",
    "85" : "mexc",
    "86" : "ndax",
    "87" : "novadax",
    "88" : "oceanex",
    "89" : "okcoin",
    "90" : "okex",
    "91" : "okex3",
    "92" : "okex5",
    "93" : "paymium",
    "94" : "phemex",
    "95" : "poloniex",
    "96" : "probit",
    "97" : "qtrade",
    "98" : "ripio",
    "99" : "stex",
    "100" : "therock",
    "101" : "tidebit",
    "102" : "tidex",
    "103" : "timex",
    "104" : "upbit",
    "105" : "vcc",
    "106" : "wavesexchange",
    "107" : "whitebit",
    "108" : "xena",
    "109" : "yobit",
    "110" : "zaif",
    "111" : "zb"
}

switchExchangeFunction = {
    "0" : ccxt.aax(),
    "1" : ccxt.ascendex(),
    "2" : ccxt.ascendex(),
    "3" : ccxt.bequant(),
    "4" : ccxt.bibox(),
    "5" : ccxt.bigone(),
    "6" : ccxt.binance(),
    "7" : ccxt.binancecoinm(),
    "8" : ccxt.binanceus(),
    "9" : ccxt.binanceusdm(),
    "10" : ccxt.bit2c(),
    "11" : ccxt.bitbank(),
    "12" : ccxt.bitbay(),
    "13" : ccxt.bitbns(),
    "14" : ccxt.bitcoincom(),
    "15" : ccxt.bitfinex(),
    "16" : ccxt.bitfinex2(),
    "17" : ccxt.bitflyer(),
    "18" : ccxt.bitforex(),
    "19" : ccxt.bitget(),
    "20" : ccxt.bithumb(),
    "21" : ccxt.bitmart(),
    "22" : ccxt.bitmex(),
    "23" : ccxt.bitpanda(),
    "24" : ccxt.bitrue(),
    "25" : ccxt.bitso(),
    "26" : ccxt.bitstamp(),
    "27" : ccxt.bitstamp1(),
    "28" : ccxt.bittrex(),
    "29" : ccxt.bitvavo(),
    "30" : ccxt.bl3p(),
    "31" : ccxt.btcalpha(),
    "32" : ccxt.btcbox(),
    "33" : ccxt.btcmarkets(),
    "34" : ccxt.btctradeua(),
    "35" : ccxt.btcturk(),
    "36" : ccxt.buda(),
    "37" : ccxt.bw(),
    "38" : ccxt.bybit(),
    "39" : ccxt.bytetrade(),
    "40" : ccxt.cdax(),
    "41" : ccxt.cex(),
    "42" : ccxt.coinbase(),
    "43" : ccxt.coinbaseprime(),
    "44" : ccxt.coinbasepro(),
    "45" : ccxt.coincheck(),
    "46" : ccxt.coinex(),
    "47" : ccxt.coinfalcon(),
    # "48" : ccxt.coinma(),
    "49" : ccxt.coinmate(),
    "50" : ccxt.coinone(),
    "51" : ccxt.coinspot(),
    "52" : ccxt.crex24(),
    "53" : ccxt.currencycom(),
    "54" : ccxt.delta(),
    "55" : ccxt.deribit(),
    "56" : ccxt.digifinex(),
    "57" : ccxt.eqonex(),
    "58" : ccxt.equos(),
    "59" : ccxt.exmo(),
    "60" : ccxt.flowbtc(),
    "61" : ccxt.ftx(),
    "62" : ccxt.ftxus(),
    "63" : ccxt.gateio(),
    "64" : ccxt.gemini(),
    "65" : ccxt.hitbtc(),
    "66" : ccxt.hitbtc3(),
    "67" : ccxt.hollaex(),
    "68" : ccxt.huobi(),
    "69" : ccxt.huobijp(),
    "70" : ccxt.huobipro(),
    "71" : ccxt.idex(),
    "72" : ccxt.independentreserve(),
    "73" : ccxt.indodax(),
    "74" : ccxt.itbit(),
    "75" : ccxt.kraken(),
    "76" : ccxt.kucoin(),
    "77" : ccxt.kuna(),
    "78" : ccxt.latoken(),
    # "79" : ccxt.latoken1(),
    "80" : ccxt.lbank(),
    "81" : ccxt.liquid(),
    "82" : ccxt.luno(),
    "83" : ccxt.lykke(),
    "84" : ccxt.mercado(),
    "85" : ccxt.mexc(),
    "86" : ccxt.ndax(),
    "87" : ccxt.novadax(),
    "88" : ccxt.oceanex(),
    "89" : ccxt.okcoin(),
    "90" : ccxt.okex(),
    # "91" : ccxt.okex3(),
    "92" : ccxt.okex5(),
    "93" : ccxt.paymium(),
    "94" : ccxt.phemex(),
    "95" : ccxt.poloniex(),
    "96" : ccxt.probit(),
    "97" : ccxt.qtrade(),
    "98" : ccxt.ripio(),
    "99" : ccxt.stex(),
    "100" : ccxt.therock(),
    "101" : ccxt.tidebit(),
    "102" : ccxt.tidex(),
    "103" : ccxt.timex(),
    "104" : ccxt.upbit(),
    "105" : ccxt.vcc(),
    "106" : ccxt.wavesexchange(),
    "107" : ccxt.whitebit(),
    "108" : ccxt.xena(),
    "109" : ccxt.yobit(),
    "110" : ccxt.zaif(),
    "111" : ccxt.zb()
}


# print(switcher.get(ExchangeId1))
# BorsaName1 = switchExchangeFunction.get(ExchangeId1)
markets1 = ccxt.kucoin().load_markets()
name1 = 'Kucoin'

# BorsaName2 = switchExchangeFunction.get(ExchangeId2)
markets2 = ccxt.gateio().load_markets()
name2 = 'GateIo'

list_Borsa1 = []
for crypto in markets1:
    if ("U" == crypto[len(crypto)-4]) & ("S" == crypto[len(crypto)-3]) & ("D" == crypto[len(crypto)-2]) & ("T" == crypto[len(crypto)-1]):
        list_Borsa1.append(crypto)

list_Borsa2 = []
for crypto in markets2:
    if ("U" == crypto[len(crypto)-4]) & ("S" == crypto[len(crypto)-3]) & ("D" == crypto[len(crypto)-2]) & ("T" == crypto[len(crypto)-1]):
        list_Borsa2.append(crypto)

df = pd.DataFrame(columns=["Sembol","Al_Borsa","Al","Sat_Borsa","Sat","Kar"])
items = list(range(0, 57))
l = len(list_Borsa1)
for i in list_Borsa1:
    for j in list_Borsa2:
        # aaa = "C3S/USDT"
        aaa = 0
        for n in j:
            if n.isnumeric() == True:
                aaa = 1
        if (i == j) & (aaa == 0):
            a = ccxt.kucoin().fetch_ticker(i)["bid"]
            b = ccxt.gateio().fetch_ticker(j)["bid"]
            if (a==0) | (b==0):
                break
            elif a>b:
                min=b
                minBorsa = name2
                max = a
                maxBorsa = name1
            elif a<b:
                min = a
                minBorsa = name1
                max = b
                maxBorsa = name2
            
            kar = ((max-min)/min)*100
            print(i)
            df = df.append({"Sembol":i,"Al_Borsa":minBorsa,"Al":min,"Sat_Borsa":maxBorsa,"Sat":max,"Kar":kar}, ignore_index=True)
    # printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    # for i, item in enumerate(items):
    #     # Do stuff...
    #     time.sleep(0.1)
    #     # Update Progress Bar
    #     printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
            

print(df.sort_values('Kar',ascending=False))

