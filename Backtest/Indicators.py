import numpy as np

class Indicators :

    def sma(self,length,prices):
        smaY = np.zeros(len(prices))
        for k in range(0,length):
            smaY[length-1] = smaY[length-1] + prices[k]/length
        for i in range(length,len(prices)):
            smaY[i] = smaY[i-1]+prices[i]/length - prices[i-length]/length
        for i in range(0,length):
            smaY[i] = smaY[length]
        return smaY
    
    def ema(self,length,prices):
        emaY = np.zeros(len(prices))
        multiplier = 2/(length-1)
        for k in range(0, length):
            emaY[length - 1] = emaY[length - 1] + prices[k] / length
        for i in range(length, len(prices)):
            emaY[i] = (prices[i]-emaY[i - 1])*multiplier + emaY[i-1]
        for i in range(0, length):
            emaY[i] = emaY[length]
        return emaY