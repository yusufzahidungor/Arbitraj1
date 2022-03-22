from selenium import webdriver
import pandas as pd
import sqlite3
  
  

# driver.get("https://coinarbitragebot.com/tr/market.php?ex=binance")
# list_Exchange = ["binance","hitbtc","bithumb","coinbase","crypto.com","kucoin","kraken","bitfinex","huobi","gate.io","btcturk","bittrex","ascendex","ftx"]
# deneme = pd.DataFrame(columns=["sembol","al_Borsa","al","sat_Borsa","sat","kar"])
# for i in range(2,250):
#     j=1
#     old_Sembol = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#     new_Sembol = ""
#     for harf in old_Sembol:
#         if harf == "-":
#             harf = "/"
#         if harf == " ":
#             if (new_Sembol[len(new_Sembol)-3] == "U") & (new_Sembol[len(new_Sembol)-2] == "S") & (new_Sembol[len(new_Sembol)-1] == "D"):
#                 harf = "T"
#                 new_Sembol = new_Sembol + harf
#             break
#         new_Sembol = new_Sembol + harf
#     j+=1
#     al_Borsa =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#     if al_Borsa != "binance":
#         continue
#     j+=1
#     al_Fiyat =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#     j+=1
#     sat_Borsa =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#     for exc in list_Exchange:
#         a=0
#         if sat_Borsa == exc:
#             a = 1
#             break
#     j+=1
#     sat_Fiyat =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#     j+=1
#     kar =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
#     # if a == 1:
#     #     print(new_Sembol)
#     #     print(al_Borsa)
#     #     print(al_Fiyat)
#     #     print(sat_Borsa)
#     #     print(sat_Fiyat)
#     #     print(kar)
#     #     break
#     if a == 1:
#         with sqlite3.connect('vst.sqlite') as vt:
#             im = vt.cursor()
#             im.execute("""CREATE TABLE IF NOT EXISTS Exchange
#                 (new_Sembol, al_Borsa, al_Fiyat, sat_Borsa, sat_Fiyat, kar)""")
#             im.execute("""INSERT INTO Exchange VALUES
#                 (?, ?, ?, ?, ?, ?)""",(new_Sembol,al_Borsa,al_Fiyat,sat_Borsa,sat_Fiyat,kar))
#             vt.commit()
#             # vt.close()

# with sqlite3.connect('vst.sqlite') as vt:
#     im = vt.cursor()
#     im.execute("""SELECT * FROM Exchange""")
#     print("All the data")
#     output = im.fetchall()
#     for row in output:
#       print(row)
#     vt.commit()
#     vt.close()

# driver.close()

df = pd.DataFrame(columns=['Sembol','Al Borsa','Al Fiyat','Sat Borsa','Sat Fiyat','Kar'])
    

def switchh(id1,id2):
    switch = {
        1 : "binance",
        2 : "btcTurk"
    }

    Borsa1Name = switch.get(id1)
    Borsa2Name = switch.get(id2)
    return Borsa1Name,Borsa2Name

def borsaName():
    print("1-Binance\n2-Btcturk\n3-Paribu\n4-coinbase\n5-gate.io")
    print("----------------------------------")
    Borsa1id = input("1.Borsayı seçin :")
    Borsa2id = input("2.Borsayı seçin :")

    switcher = {
        "1" : "binance",
        "2" : "btcturk",
        "3" : "paribu",
        "4" : "coinbase",
        "5" : "gate.io"
    }

    Borsa1Name = switcher.get(Borsa1id)
    Borsa2Name = switcher.get(Borsa2id)
    
    return Borsa1Name,Borsa2Name
    

def selenium(Borsa1Name,Borsa2Name):
    driver = webdriver.Edge()
    url = 'https://coinarbitragebot.com/tr/market.php?ex='+str(Borsa1Name)
    driver.get(url)

    for i in range(2,250):
        j=1
        old_Sembol = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        new_Sembol = ""
        for harf in old_Sembol:
            if harf == "-":
                harf = "/"
            if harf == " ":
                if (new_Sembol[len(new_Sembol)-3] == "U") & (new_Sembol[len(new_Sembol)-2] == "S") & (new_Sembol[len(new_Sembol)-1] == "D"):
                    harf = "T"
                    new_Sembol = new_Sembol + harf
                break
            new_Sembol = new_Sembol + harf
        j+=1
        al_Borsa =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        if (al_Borsa == Borsa1Name) | (al_Borsa == Borsa2Name):
            j+=1
            al_Fiyat =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
            j+=1
            sat_Borsa =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
            if (sat_Borsa == Borsa1Name) | (sat_Borsa == Borsa2Name):                
                j+=1
                sat_Fiyat =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
                j+=1
                kar =  driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[3]/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text

                # df = pd.DataFrame(columns=['Sembol','Al_Borsa','Al_Fiyat','Sat_Borsa','Sat_Fiyat','Kar'])
                # print(i)
                # df = df.append({'Sembol':new_Sembol,'Al_Borsa':al_Borsa,'Al_Fiyat':al_Fiyat,'Sat_Borsa':sat_Borsa,'Sat_Fiyat':sat_Fiyat,'Kar':kar})
                
                print("***"+new_Sembol+"***"+al_Borsa+"---"+al_Fiyat+"---"+sat_Borsa+"---"+sat_Fiyat+"---"+kar)

    print(df)
    driver.close()

if __name__ == "__main__":
    # print("1-Binance\n2-Btcturk")
    # print("----------------------------------")
    # Borsa1id = input("1.Borsayı seçin :")
    # Borsa2id = input("2.Borsayı seçin :")

    Name1,Name2 = borsaName()
    selenium(Name1,Name2)
    