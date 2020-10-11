#!/usr/bin/env python
# coding: utf-8

# In[50]:


#Importing the required libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import warnings


# In[21]:


df=pd.read_csv("bitstampUSD_1-min_data_2012-01-01_to_2020-09-14.csv")
df.head()
df


# In[16]:


df.info()


# In[23]:


df['Timestamp'] = [datetime.fromtimestamp(x) for x in df['Timestamp']]


# In[24]:


df.head()


# In[25]:


df.describe()


# In[26]:


df.corr()


# In[27]:


df.isnull().sum()


# In[43]:


df['Open'] = df['Open'].interpolate()
df['Close'] = df['Close'].interpolate()
df['Weighted_Price'] = df['Weighted_Price'].interpolate()

df['Volume_(BTC)'] = df['Volume_(BTC)'].interpolate()
df['Volume_(Currency)'] = df['Volume_(Currency)'].interpolate()
df['High'] = df['High'].interpolate()
df['Low'] = df['Low'].interpolate()


# In[49]:


df.isnull().sum()


# In[47]:


df


# In[48]:


df


# In[ ]:




