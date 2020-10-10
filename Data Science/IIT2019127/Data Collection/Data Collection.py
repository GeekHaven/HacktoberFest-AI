# Importing Libraries
import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os


# List of assets
ticker = ['^NSEI', 'MCX.NS', 'ETH-INR', '^DJI', '^BSESN']


# Enter initial date
# As we want 1m interval date must be from last 30 days
d1 = input(
    "Enter intial date: (yyyy-mm-dd) (Date must be from last 30 days )")

# Enter final date
d2 = input(
    "Enter intial date: (yyyy-mm-dd) (Date must be from last 30 days )")


# Download the data
data_NSEI = yf.download(ticker[0], start=d1, end=d2, interval='1m')
data_MCX = yf.download(ticker[1], start=d1, end=d2, interval='1m')
data_ETH = yf.download(ticker[2], start=d1, end=d2, interval='1m')
data_DJI = yf.download(ticker[3], start=d1, end=d2, interval='1m')
data_BSEN = yf.download(ticker[4], start=d1, end=d2, interval='1m')


# Convert the downloaded data in a csv file
data_NSEI.to_csv("NSEI.csv")
data_MCX.to_csv("MCX.csv")
data_ETH.to_csv("ETH-INR.csv")
data_DJI.to_csv("DJI.csv")
data_BSEN.to_csv("BSESN.csv")

# Reading and printing first few columns of the created csv files.
dataset = pd.read_csv("ETH-INR.csv")
dataset.head()
