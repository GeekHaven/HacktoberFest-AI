# Importing Libraries
import yfinance as yf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Enter ticker for a particular stock ( Default ticker of google)
ticker = input("Enter ticker: (Enter 'x' for default ticker (GOOGLE) ")


if ticker == 'x':
    ticker = 'GOOGL'


# Enter initial date
# As we want 1m interval date must be from last 30 days
d1 = input(
    "Enter intial date: (yyyy-mm-dd) (Date must be from last 30 days )")

# Enter final date
d2 = input(
    "Enter intial date: (yyyy-mm-dd) (Date must be from last 30 days )")


# Download the data
data = yf.download(ticker, start=d1, end=d2, interval='1m')

# Check the downlaod
print(data)

# Convert the downloaded data in a csv file
data.to_csv("Intradata.csv")


# Reading and printing first few columns of the created csv file
dataset = pd.read_csv("Intradata.csv")
dataset.head()
