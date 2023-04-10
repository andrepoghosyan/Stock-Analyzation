#!/usr/bin/env python
# coding: utf-8

# In[12]:


"""This code uses the yfinance library to download historical stock data for the specified symbol (in this case, "AAPL") for the specified date range (2010 to 2022). It then computes the 20-day simple moving average for the closing prices of the stock and adds that as a column in the dataframe. Finally, it plots the stock data and the SMA on a graph, with the stock prices on the y-axis and the x-axis showing the date range. The graph is then displayed with a title and y-axis label."""


# In[9]:


import datetime
import matplotlib.pyplot as plt
import yfinance as yf

# Define the stock symbol and the date range for the data
symbol = 'AAPL'
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2022, 1, 1)

# Retrieve the stock data
data = yf.download(symbol, start=start, end=end, progress = False)

# Compute the 20-day simple moving average
sma_20 = data['Close'].rolling(window=20).mean()

# Add the SMA column to the dataframe
data['SMA_20'] = sma_20

# Plot the stock data and the SMA
data[['Close','SMA_20']].plot(grid=True)
plt.title("Stock price")
plt.ylabel("Price ($)")
plt.show()

