import krakenex
from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
import time
import talib as tb
import Backtest.Indicators as id
import schedule


def datafetching():
    k = krakenex.API()
    last = 1496082468000

    ohlc = k.query_public("OHLC", {'pair': "XBTCZEUR", 'interval': 1, 'since': last})
    tabClose = []
    tabTime = []
    for interval in ohlc['result']['XXBTZEUR']:
        tabClose.append(float(interval[4]))
        tabTime.append(datetime.datetime.fromtimestamp(float(interval[0])).strftime('%Y-%m-%d %H:%M:%S'))

    OHLC = pd.DataFrame(ohlc['result']['XXBTZEUR'],
                        columns=['Time', 'Open', 'High', 'Low', 'Close', 'Vwap', 'Volume', 'Count'])
    df = OHLC.astype(float)
    # ppsr = id.PPSR(df)
    # pprplot = ppsr[['Close','S1','S2','S3','R1','R2','R3']]
    # pprplot.plot()
    # plt.show()
    DF = df[['Close']]
    #DF.plot()
    df2 = pd.DataFrame(np.random.randint(0, 100, size=(100, 1)))
    graph1 = df2.plot()
    plt.show()

schedule.every(5).seconds.do(datafetching)

while True:
    schedule.run_pending()
