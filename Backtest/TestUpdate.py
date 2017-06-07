import krakenex
from matplotlib import pyplot as plt
import pandas as pd
import datetime
import numpy as np
import time
import talib as tb
import Backtest.Indicators as id
import schedule

global data
data = pd.DataFrame( np.random.randint( 0, 100, size=(100, 1)))

def datafetching():
    df2 = pd.DataFrame(np.random.randint(0, 100, size=(1, 1)))
    data.append(df2, ignore_index=True)
    print(df2)

schedule.every(5).seconds.do(datafetching)

while True:
    schedule.run_pending()