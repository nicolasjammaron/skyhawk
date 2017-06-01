import json
import matplotlib.pyplot as plot
import numpy as np

with open("5days5min.json",'r') as file:
    listPrices = json.load(file)

listX = []
listY = []
i = 0


for dico in listPrices:
    listX.append(float(dico['Timestamp'])-41419)
    try:
        float(dico['Close'])
        listY.append(float(dico['Close']))
    except :
        listY.append(listY[len(listY)-1])


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

sma5 = sma(5,listY)


sma13 = sma(13,listY)

ema5=ema(5,listY)

ema13 = ema(13,listY)

plot.plot(listX,listY,'black',listX,ema5,'g--',listX,ema13,'r--')
plot.axis([0,4,1500,2500])
plot.draw()

plot.figure()
plot.plot(listX,listY,'black',listX,sma5,'g--',listX,sma13,'r--')
plot.axis([0,4,1500,2500])
plot.draw()

plot.show()