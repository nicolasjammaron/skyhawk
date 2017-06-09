import talib

class CalculIndicateurs :
    def __init__(self):
        super().__init__()
        self.emaNumbers = [5,8,13]
        self.data
        self.emaDico = {'5':None,'8':None,'13':None}
        self.macd = {'macd':None,'signal':None,'hist':None}


    def updateMACD(self):
        macdvalues = talib.MACD(self.data, )
        self.macd['macd'] = macdvalues[0]
        self.macd['signal'] = macdvalues[1]
        self.macd['hist'] = macdvalues[2]


    def updateIndicators(self):
        for key in self.emaDico.keys():
            self.emaDico[key] = talib.EMA(self.data,key)
        self.updateMACD()

    def printEMA(self):
        print("EMAs : ")
        for ema in self.emaDico:
            print(ema)

    def printMACD(self):
        print("MACD :")
        print(self.macd)

    def updateData(self,Data):
        self.data = Data
        self.updateIndicators()
        self.printEMA()
        self.printMACD()




