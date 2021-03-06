#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:08:35 2022

@author: leonardo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:46:36 2022

@author: leoprimero
"""

import pandas as pd
from pandas_datareader import data as pdr
import datetime as date
import matplotlib.pyplot as plt
import pyfolio


def get_Data(index):
    data = pdr.get_data_yahoo(index,start=startdate,end=enddate)
    return data

startdate = date.datetime(2020, 12, 30)
enddate = date.datetime(2022, 4, 13)




AAPL = get_Data('AAPL')
KO = get_Data('KO')
GLD = get_Data('GLD')
SPY = get_Data('SPY')
# DIA = get_Data('DIA')
XLF = get_Data('XLF')
XLE = get_Data('XLE')
BRK = get_Data('BRK-B')


# KO.set_index('Date',inplace=True)



# MERVAL=get_Data('M.BA')

# tickers = (KO, AAPL, PFE, XOM, GOLD, SPY, XLF)
#  2
# tickers = (KO, PFE, GOLD, SPY)
#  3
# tickers = (KO, AAPL, PFE)
#  4
tickers = (AAPL, KO, GLD,SPY, XLF, XLE, BRK)


pond_2= [0.27,0.14,0.09,0.51]
pond_3= [0.26, 0.55, 0.19]
pond_marko= [0.22,0.06,0.25,0.18,0.13,0.15]
pond_anual= [0.02,0.36,0.20,0.02,]
pond_markoTSLA= [0.08,0.01,0.38,0.09,0.05,0.37,0.01,0.01]
pind_nueva = [0.1,0.1,0.1,0.2,0.2,0.2,0.2]
pond_nueva2 =[0.09,0.1,0.09,0.22,0.21,0.12,0.17]

equi_weighs= [1/(len(tickers))for n in tickers]

for stock in (tickers):
    stock["Returns"]=stock["Close"]/stock["Close"].iloc[0]
    
for stock, allocation in zip((tickers), pond_nueva2):
                            
    stock["Allocation"]= stock["Returns"]* allocation
    
for stock in (tickers):
    stock["Position"]= stock["Allocation"]*100
    
portafolio = pd.concat([x  ['Position'] for x in tickers],axis=1)

# portafolio.columns = ['KO', 'AAPL', 'PFE', 'XOM', 'GOLD', 'SPY', 'XLF']

# portafolio.columns = ['KO','PFE', 'GOLD', 'SPY']
portafolio.columns =  [ 'AAPL', 'KO', 'GLD', 'SPY', 'XLF', 'XLE', 'BRK']

# portafolio.columns = ['KO','AAPL', 'PFE']


portafolio_total = portafolio.sum(axis=1)
 
# plt.style.use('dark_background')
portafolio_total.plot(figsize=(9,7.5))
plt.grid(alpha=0.3, color='SteelBlue', linewidth=1)
plt.title ("Cartera Modelo",fontsize = 20)
plt.xlabel('Fecha')
plt.ylabel('%')

portafolio_returns = portafolio_total.pct_change().dropna()
portafolio_returns.plot (figsize=(9,7.5))
plt.grid(alpha=0.3, color='SteelBlue', linewidth=1)
plt.title ("Retornos diarios Cartera Cartera Modelo",fontsize = 20)
plt.xlabel('Fecha')
plt.ylabel('%')

portafolio.plot(figsize=(12,9))
plt.title ("Evoluci??n de activos individuales",fontsize = 20)
plt.xlabel('Fecha')
plt.ylabel('%')

retornos= portafolio.pct_change().dropna()
retornos.plot(figsize=(19,17))
plt.grid(alpha=0.3, color='SteelBlue', linewidth=1)
plt.title ("Rendimiento diario por activos",fontsize = 30)
plt.xlabel('Fecha')
plt.ylabel('%')

retornosacumulado= (retornos/100+1).cumprod()
retornosacumulado.plot(figsize=(15,13))
plt.title ("Rendimientos diarios acumulados por activos",fontsize = 30)
plt.xlabel('Fecha')
plt.ylabel('%')

portafolio_totalexcel= portafolio_total.to_csv('portfolioIdealCroux.csv')


benchmark = SPY["Adj Close"]
bench = benchmark.pct_change().dropna()
bench.rename("Benchmark SP500")
pyfolio.create_returns_tear_sheet(portafolio_returns)
