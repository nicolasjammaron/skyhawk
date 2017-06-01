import krakenex
from matplotlib import pyplot as plt
import numpy as np


k = krakenex.API()

ohlc = k.query_public("OHLC",{'pair':"XBTCZEUR",'interval':5,'since':1496082468000})

print(ohlc)

tabClose = []
tabTime = []
for interval in ohlc['result']['XXBTZEUR']:
    tabClose.append(float(interval[4]))
    tabTime.append(float(interval[0]))


def sma(length,prices):
    smaY = np.zeros(len(prices))
    for k in range(0,length):
        smaY[length-1] = smaY[length-1] + prices[k]/length
    for i in range(length,len(prices)):
        smaY[i] = smaY[i-1]+prices[i]/length - prices[i-length]/length
    for i in range(0,length):
        smaY[i] = smaY[length]
    return smaY


def ema(length,prices):
    emaY = np.zeros(len(prices))
    multiplier = 2/(length-1)
    for k in range(0, length):
        emaY[length - 1] = emaY[length - 1] + prices[k] / length
    for i in range(length, len(prices)):
        emaY[i] = (prices[i]-emaY[i - 1])*multiplier + emaY[i-1]
    for i in range(0, length):
        emaY[i] = emaY[length]
    return emaY


ema5 = ema(5,tabClose)
ema8 = ema(8,tabClose)
print(tabClose)

plt.plot(tabTime,tabClose,tabTime,ema5,tabTime,ema8)
plt.axis([1496126400,1496341800,1900,2200])

plt.show()
