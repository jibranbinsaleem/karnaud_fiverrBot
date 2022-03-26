import datetime
import config
import ccxt
import time
from functions import buy, sell

exchange = "binance"
symbol = "BTC/USDT"

if exchange == "binance":
    exchange = ccxt.binance({
    'apiKey' : config.BINANCE_APIKEY,
    'secret' : config.BINANCE_SECRET,
    })

elif exchange == "coinbasepro":
    coinbasepro = ccxt.coinbasepro({
        'apiKey': config.COINBASE_APIKEY,
        'secret': config.COINBASE_SECRET,
        'password': config.COINBASE_PASSPHRASE,
        
    })
elif exchange == "bittrex":
    bittrex = ccxt.bittrex({
        'proxies': {
            'http': config.HTTP_PROXY,  
            'https': config.HTTPS_PROXY,
        },
    })

exchange.set_sandbox_mode(True)
symbol = "BTC/USDT"
x = buy(binance, symbol, 0.1)
print(x)



ohlc_data = binance.fetch_ohlcv(symbol=symbol, timeframe = "30m", limit=1) #time, o,h,l,c
counter = 0
for ohlc in ohlc_data:
    #print(ohlc)
    percentage_change = ((ohlc[1] - ohlc[4]) / ohlc[1]) * 100 
    counter += 1
    print(percentage_change)
    if percentage_change <= -15.0 :
        buy()
#print(counter)