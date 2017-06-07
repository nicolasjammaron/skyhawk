import krakenex
from matplotlib import pyplot as plt
import Backtest.Indicators as bin
import Backtest.RetrieveData as rd
from pandas import *
import datetime
import time

ema10 = bin.EMA(rd.df,10)
ema10.plot()
bin.MACD(rd.df,10,15).plot()
bin.ADX(rd.df,10,15).plot()
plt.show()