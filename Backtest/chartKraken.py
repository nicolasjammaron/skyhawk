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

def macd(ema1,ema2,sline, prices):
    macdY = np.zeros(len(prices))
    Ema1 = ema(ema1, prices)
    Ema2 = ema(ema2, prices)
    macdY = Ema2 - Ema1
    signalline = ema(sline, macdY)
    return macdY - signalline

ema5 = ema(5,tabClose)
ema8 = ema(8,tabClose)
print(ema5)
plt.plot(tabTime,tabClose,tabTime,ema5,tabTime,ema8)
plt.axis([1496469300,1496684700,2150,2350])

plt.show()
