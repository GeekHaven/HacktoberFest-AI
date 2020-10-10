# Importing Libraries
import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os


import mplfinance as mpf

# Download the data
data = yf.download("SPY", start="2020-07-09", end="2020-10-09")
#Used the data of last 3 months.

# Plot the data

# Type : used to tell graph type. We can use bar , line , candlestick
# volume : to show the volume at bottom of graph
# show_nontrading : if True day where there is no trading
#                   are also displeayed in the graph
# mav : used to plot the movig average in the graph

mpf.plot(data, type='ohlc', volume=True, show_nontrading=True, mav=5)
