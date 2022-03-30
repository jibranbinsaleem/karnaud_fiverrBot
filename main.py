import datetime
import config
import ccxt
import time
import csv
from functions import buy, sell
import pandas as pd

def bot(exchange_name, symbol, amount):
    position = ""
    print(exchange_name)
    profit = 0
    bought = False
    exchange = None

    if exchange_name == "binance":
        exchange = ccxt.binance({
        'apiKey' : config.BINANCE_APIKEY,
        'secret' : config.BINANCE_SECRET,
        })
        symbol = "BTC/USDT"

    elif exchange_name == "coinbasepro":
        exchange = ccxt.coinbasepro({
            'apiKey': config.COINBASE_APIKEY,
            'secret': config.COINBASE_SECRET,
            'password': config.COINBASE_PASSPHRASE,

        })
        symbol = "BTC/USD"


    elif exchange_name == "bittrex":
        exchange = ccxt.bittrex({
            'proxies': {
                'http': config.HTTP_PROXY,
                'https': config.HTTPS_PROXY,
            },
        })

    exchange.set_sandbox_mode(True)

    # x = sell(exchange, symbol, amount)
    # df = pd.DataFrame.from_dict(x["info"])
    # df.to_csv ('info.csv', index = None, mode = "a", header = False)
    # price = x["info"]["fills"][0]["price"]
    # print(x)
    # print(price)


    while True:
        if exchange_name == "binance" or "bittrex":
            ohlc_data = exchange.fetch_ohlcv(symbol=symbol, timeframe = "30m", limit=1) #time, o,h,l,c
        elif exchange_name == "coinbasepro":
            ohlc_data = exchange.fetch_ohlcv(symbol = symbol, timeframe = "1h", limit = 1 )
        #counter =
        for ohlc in ohlc_data:
            #print(ohlc)
            percentage_change = ((ohlc[1] - ohlc[4]) / ohlc[1]) * 100
            cur_price = ohlc[4]
            #counter += 1
            #print(percentage_change)
            if percentage_change <= -15.0 and bought == False :
                position = buy(exchange, symbol, amount)
                df = pd.DataFrame.from_dict(position["info"])
                df.to_csv ('info.csv', index = None, mode = "a", header = False)
                price = position["info"]["fills"][0]["price"]
                bought == True
                profit = price * 1.15 #price with 15% profit
            elif cur_price > profit and bought == True:
                position = sell(exchange, symbol, amount)
                bought = False
        return position

    #print(counter)
if __name__ == "__main__":
    bot("binance", "BTC/USDT", 0.1)