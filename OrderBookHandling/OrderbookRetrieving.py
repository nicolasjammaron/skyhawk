import pickle
import time

import GDAX as gdax

from OrderBookHandling.OrderbookPersonnalisedClass import OrderBookPersonnalised

publicClient = gdax.PublicClient(product_id="BTC-EUR")
temps = time.time()
temps2 = temps
tmp = temps2

list_orderbooks = []

while (temps2-temps < 30):
    book1 = publicClient.getProductOrderBook()
    orderbook = OrderBookPersonnalised(book1,temps2-tmp)
    list_orderbooks.append(orderbook)
    tmp = temps2
    temps2 = time.time()

print(temps2-temps)

with open("orderbook.txt",mode='wb') as file:
    pickler = pickle.Pickler(file=file)
    pickler.dump(list_orderbooks)




