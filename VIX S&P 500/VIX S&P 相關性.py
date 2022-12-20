# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:57:59 2022

@author: stran
"""

#%% import package
from pandas_datareader import data as pddata
from datetime import date
from datetime import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
#%% import data 股市崩盤
#透過 yfinance 抓取 VIX 以及 S&P 資料
# S&P 500
data_SP = yf.download('^GSPC', start="2008-04-01", end="2008-10-30")
# VIX index
data_VIX = yf.download('^VIX', start="2008-04-01", end="2008-10-30")
#%% draw plot
# S&P 500
mc = mpf.make_marketcolors(up='r',down='g',inherit=True) #針對線圖的外觀微調，將上漲設定為紅色，下跌設定為綠色
s  = mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mc) #接著把自訂的marketcolors放到自訂的style中
kwargs = dict(type='candle', mav=(5,20,60), figratio=(10,8), figscale=0.75, title='S&P 500 collapse', style=s) #設定可變參數kwargs，並在變數中填上繪圖時會用到的設定值
mpf.plot(data_SP, **kwargs) #選擇資料來源，帶入kwargs參數，畫出目標股票的走勢圖
# VIX index
mc = mpf.make_marketcolors(up='r',down='g',inherit=True) 
s  = mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mc) 
kwargs = dict(type='candle', mav=(5,20,60), figratio=(10,8), figscale=0.75, title='VIX index collapse', style=s) 
mpf.plot(data_VIX, **kwargs)
#%% correlative
data = pd.DataFrame()
data['SP'] = data_SP["Close"]
data['VIX'] = data_VIX["Close"]
print(data.corr())

fig, plt1 = plt.subplots() # 利用 subplot 進行疊圖
plt.title('S&P 500 , VIX market collapse , correlation = ' + str(round(data.corr().loc['VIX','SP'],4)) + '(market collapse)')
plt1.set_ylabel('S&P 500', color='blue')
plt1.plot(range(1, data_SP.shape[0]+1), data_SP['Close'], label='S&P 500', color='blue')
plt1.tick_params(axis='y', labelcolor='blue')
plt2 = plt1.twinx() # 複製第二個 subplot
plt2.set_ylabel('VIX index', color='black')
plt2.plot(list(range(1, data_VIX.shape[0]+1)), data_VIX['Close'], label='VIX index', color='black')
plt2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()
plt.show()

# plt.plot(list(range(1, data_SP.shape[0]+1)), data_SP['Close'], label='S&P 500')
# plt.plot(list(range(1, data_VIX.shape[0]+1)), data_VIX['Close'], label='VIX index')
# plt.title('S&P 500 , VIX market collapse , correlation = ' + str(round(data.corr().loc['VIX','SP'],4)) + '(market collapse)')
# plt.legend(loc = 'right')
#%% import data 股市平穩
#透過 yfinance 抓取 VIX 以及 S&P 資料
# S&P 500
data_SP1 = yf.download('^GSPC', start="2013-04-01", end="2013-10-30")
# VIX index
data_VIX1 = yf.download('^VIX', start="2013-04-01", end="2013-10-30")
#%% draw plot
# S&P 500
mc = mpf.make_marketcolors(up='r',down='g',inherit=True) #針對線圖的外觀微調，將上漲設定為紅色，下跌設定為綠色
s  = mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mc) #接著把自訂的marketcolors放到自訂的style中
kwargs = dict(type='candle', mav=(5,20,60), figratio=(10,8), figscale=0.75, title='S&P 500 stable', style=s) #設定可變參數kwargs，並在變數中填上繪圖時會用到的設定值
mpf.plot(data_SP1, **kwargs) #選擇資料來源，帶入kwargs參數，畫出目標股票的走勢圖
# VIX index
mc = mpf.make_marketcolors(up='r',down='g',inherit=True) 
s  = mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mc) 
kwargs = dict(type='candle', mav=(5,20,60), figratio=(10,8), figscale=0.75, title='VIX index stable', style=s) 
mpf.plot(data_VIX1, **kwargs) 
#%% correlative
data1 = pd.DataFrame()
data1['SP'] = data_SP1["Close"]
data1['VIX'] = data_VIX1["Close"]
print(data1.corr())

fig, plt1 = plt.subplots() # 利用 subplot 進行疊圖
plt.title('S&P 500 , VIX market collapse , correlation = ' + str(round(data1.corr().loc['VIX','SP'],4)) + '(market collapse)')
plt1.set_ylabel('S&P 500', color='blue')
plt1.plot(range(1, data_SP1.shape[0]+1), data_SP1['Close'], label='S&P 500', color='blue')
plt1.tick_params(axis='y', labelcolor='blue')
plt2 = plt1.twinx() # 複製第二個 subplot
plt2.set_ylabel('VIX index', color='black')
plt2.plot(list(range(1, data_VIX1.shape[0]+1)), data_VIX1['Close'], label='VIX index', color='black')
plt2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()
plt.show()

# plt.plot(list(range(1, data_SP1.shape[0]+1)), data_SP1['Close'], label='S&P 500')
# plt.plot(list(range(1, data_VIX1.shape[0]+1)), data_VIX1['Close'], label='VIX index')
# plt.title('S&P 500 , VIX  , correlation = ' + str(round(data1.corr().loc['VIX','SP'],4)) + '(market stable)')
# plt.legend()
