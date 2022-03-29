
def buy(exchange, symbol, amount):
    x = exchange.create_order(symbol=symbol,side = "buy", type="market", amount=amount)
    return x

def sell(exchange, symbol, amount):
    x = exchange.create_order(symbol=symbol,side = "sell", type="market", amount=amount)
    return x