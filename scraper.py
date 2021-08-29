import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from pandas import DataFrame

def scraper():
    r = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')
    soup = BeautifulSoup(r.text,'html.parser')
    df = pd.DataFrame()
    
    for article in soup.find_all('div', class_='sc-1g6z4xm-0 hXyplo'):
        hash = article.a.text # = stukje code dat onder 'Hash' staat
        for times in article.find_all('div', class_='sc-1au2w4e-0 emaUuf'):
            tijd = times.find('span', class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC').text # = de tijd
            amounts = article.find_all('div', class_='sc-1au2w4e-0 fTyXWG')
            amountBTC = amounts[0].text # print amount(btc) + bedrag + BTC
            amountBTC = amountBTC.split(')')[1] # print laatste deel: bedrag + BTC
            amountUSD = amounts[1].text # doet hetzelfde als bij BTC
            amountUSD = amountUSD.split(')')[1] # doet hetzelfde als bij BTC

            df2 = pd.DataFrame([hash, tijd, amountBTC, amountUSD])
            df2 = df2.transpose()
            df2.columns = ['Hash', 'Time', 'Amount(BTC)', 'Amount(USD)']

            df = df.append(df2) 
    
    for i in df["Amount(USD)"]:
        df["Amount(USD)"] = df["Amount(USD)"].replace("$","").replace(",","")   
    for item in df["Amount(USD)"]:
        df["Amount(USD)"] = item.replace("$","").replace(",","")
    df["Amount(USD)"] = df["Amount(USD)"].astype(float)
    with open("logfile.txt", 'a') as logfile:
        print(df.max(), file=logfile)
    time.sleep(60)

while True:
    scraper()