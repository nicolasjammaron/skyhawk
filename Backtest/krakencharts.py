import time
import matplotlib.pyplot as plot
import krakenex
import talib

import numpy as np



from Backtest.Indicators import Indicators as ind

k = krakenex.API()
temps1 = time.time()
listPrices = k.query_public("OHLC",{'since':temps1-60*60*24,'pair':'XXBTZEUR','interval':5})
print(listPrices)
listX = []
listY = []

# a modifier
for dico in listPrices['result']['XXBTZEUR']:
    listX.append(float(dico[0])-1496365181)
    try:
        float(dico[4])
        listY.append(float(dico[4]))
    except :
        listY.append(listY[len(listY)-1])

print(listY)
print(listX)
#
# def sma(length,prices):
#     smaY = np.zeros(len(prices))
#     for k in range(0,length):
#         smaY[length-1] = smaY[length-1] + prices[k]/length
#     for i in range(length,len(prices)):
#         smaY[i] = smaY[i-1]+prices[i]/length - prices[i-length]/length
#     for i in range(0,length):
#         smaY[i] = smaY[length]
#     return smaY
#
#
# def ema(length,prices):
#     emaY = np.zeros(len(prices))
#     multiplier = 2/(length-1)
#     for k in range(0, length):
#         emaY[length - 1] = emaY[length - 1] + prices[k] / length
#     for i in range(length, len(prices)):
#         emaY[i] = (prices[i]-emaY[i - 1])*multiplier + emaY[i-1]
#     for i in range(0, length):
#         emaY[i] = emaY[length]
#     return emaY

smaTalib = talib.SMA(np.asarray(listY),10)
print(smaTalib)

indicator = ind()
sma5 = indicator.sma(5,listY)


sma13 = indicator.sma(13,listY)

ema5 = indicator.ema(5,listY)

ema13 = indicator.ema(13,listY)

plot.plot(listX,listY,'black',listX,ema5,'g--',listX,ema13,'r--')
plot.axis([0,listPrices['result']['last']-1496365181,1500,2500])
plot.draw()

plot.figure()
plot.plot(listX,listY,'black',listX,sma5,'g--',listX,sma13,'r--')
plot.axis([0,listPrices['result']['last']-1496365181,1500,2500])
plot.draw()

plot.show()