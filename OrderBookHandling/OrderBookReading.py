import pickle
import GDAX as gdax

with open("orderbook.txt",'rb') as file:
    unpickler = pickle.Unpickler(file)
    list_orderbooks = unpickler.load()


ordrbook1=list_orderbooks[0]
print(ordrbook1.time)
print(ordrbook1.orderbook)


#1 orderbook toutes les 416.6 millisecondes environ