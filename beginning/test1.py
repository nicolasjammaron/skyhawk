import GDAX as gdax
import json
import time


wsclient = gdax.WebsocketClient(url="wss://ws-feed.gdax.com",products="BTC-EUR")
temps = time.time()
temps2 =temps
wsclient.start()
while (temps2-temps <60):
    time.sleep(1)
    temps2=time.time()

wsclient.close()