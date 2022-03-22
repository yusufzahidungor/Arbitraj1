import ccxt
import pandas as pd
from globalArbitrage import switchExchange as se


def run():
    list_Exchange = []

    for exc in ccxt.exchanges:
        list_Exchange.append(exc)

    for i in range(len(list_Exchange)):
        print(str(i)+"-"+str(list_Exchange[i]))

    ExchangeId1 = input("1. Borsayı Secin :")
    ExchangeId2 = input("2. Borsayı Secin :")

    BorsaName1 = se.switchExchangeFunction.get(ExchangeId1)
    markets1 = BorsaName1.load_markets()
    name1 = se.switchExchangeName.get(ExchangeId1)

    BorsaName2 = se.switchExchangeFunction.get(ExchangeId2)
    markets2 = BorsaName2.load_markets()
    name2 = se.switchExchangeName.get(ExchangeId2)

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
                a = BorsaName1.fetch_ticker(i)["bid"]
                b = BorsaName2.fetch_ticker(j)["bid"]
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

    print(df.sort_values('Kar',ascending=False))