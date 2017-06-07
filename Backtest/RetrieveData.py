import krakenex
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import datetime
import time

k = krakenex.API()

last = 1496082468000
ohlc = k.query_public("OHLC",{'pair':"XBTCZEUR",'interval':1,'since':last})
tabClose = []
tabTime = []
tabUint = []
for interval in ohlc['result']['XXBTZEUR']:
    tabClose.append(float(interval[4]))
    tabTime.append(datetime.datetime.fromtimestamp(float(interval[0])).strftime('%Y-%m-%d %H:%M:%S'))
    tabUint.append(float(interval[0]))


#OHLC = pd.DataFrame(ohlc['result']['XXBTZEUR'],index=tabTime, columns=['time', 'Open', 'High', 'Low', 'Close','vwap', 'volume', 'count'])
#df = pd.DataFrame(OHLC['Close'], index=tabTime)
#df = df.astype(float)

OHLC = pd.DataFrame(ohlc['result']['XXBTZEUR'], columns=['Time', 'Open', 'High', 'Low', 'Close','Vwap', 'Volume', 'Count'])
DF = pd.DataFrame(OHLC[['Open','High','Low','Close']])
df = DF.astype(float)

