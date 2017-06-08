import krakenex
import numpy as np
import talib
from matplotlib import pyplot as plt
import time
import sched

import matplotlib.animation as anim

k = krakenex.API()
s = sched.scheduler(time.time,time.sleep)
prices = []
xtime = []
def update_chart():
    print("new minute")
    listPrices = k.query_public("OHLC", {'since':time.time()-59, 'pair': 'XXBTZEUR', 'interval': 1})
    prices.append(listPrices['result']['XXBTZEUR'][0][4])
    xtime.append(xtime[len(xtime)-1]+1)
    print(prices)
    s.enter(60,1,update_chart)

listPrices = k.query_public("OHLC", {'since':time.time()-59, 'pair': 'XXBTZEUR', 'interval': 1})
prices.append(listPrices['result']['XXBTZEUR'][0][4])
xtime.append(0)
print(prices)
s.enter(60,1,update_chart)
s.run()