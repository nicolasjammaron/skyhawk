import krakenex
import numpy as np
import talib
from matplotlib import pyplot as plt
import time
import sched

k = krakenex.API()
xtime = []
ema = []

listPrices = k.query_public( "OHLC", {'since': time.time( ) - 60*60, 'pair': 'XXBTZEUR', 'interval': 1} )
#prices = [item[1] for item in listPrices['result']['XXBTZEUR']]
a = np.array((listPrices['result']['XXBTZEUR']), dtype=float)
time = a[:,0]
open = a[:,1]
high = a[:,2]
low = a[:,3]
close = a[:,4]

prices = np.array([])
#listPrices2 = k.query_public("OHLC", {'since':time.time()-59, 'pair': 'XXBTZEUR', 'interval': 1})
np.append(prices,[listPrices['result']['XXBTZEUR'][0][4]])
print(listPrices['result']['XXBTZEUR'][0][4])
print(prices)
#print(prices)
#print(prices2)
#print(talib.EMA(prices2,2))