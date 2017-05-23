import GDAX as gdax
import json
import time

publicCLient = gdax.PublicClient(product_id="BTC-EUR")
orderbook = publicCLient.getProductOrderBook(level=1)
infos = (orderbook['asks'][0][0],orderbook['bids'][0][0])
print(infos)

