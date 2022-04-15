#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:44:07 2021

@author: leoprimero
"""

from pandas_datareader import data as pdr
import datetime as date





def get_Data(index):
    data = pdr.get_data_yahoo(index,start=startdate,end=enddate)
    return data

startdate = date.datetime(2020, 3, 24)
enddate = date.datetime(2021, 7, 2)





# DEn=get_Data("DE")
# BNG=get_Data("BNG")
# DEМОЙ = DEn.to_csv("DE.csv")
# BNGМОЙ = BNG.to_csv("BNG.csv")












#  SIMON'S PORTFOLIO USD NEW
         
MSFT=get_Data("MSFT")
AAPL=get_Data("AAPL")         
INTC=get_Data("INTC")              
AMZN=get_Data("AMZN")         
JNJ=get_Data("JNJ")           
PFE=get_Data("PFE")           
WMT=get_Data("WMT")           
PG=get_Data("PG")             
KO=get_Data("KO")             
C=get_Data("C")    
GOOGL=get_Data("GOOGL")            
JPM=get_Data("JPM")           
GE=get_Data("GE")             
XOM=get_Data("XOM")           
X=get_Data("X") 
RIO=get_Data("RIO") 
PKX=get_Data("PKX")
SQ=get_Data("SQ")
DE=get_Data("DE")
BG=get_Data("BG")
FCX=get_Data("FCX")
VALE=get_Data("VALE")
NVDA=get_Data("NVDA")
INTC=get_Data("INTC")
QCOM=get_Data("QCOM")



MSFTМОЙ = MSFT.to_csv("MSFT.csv")
AAPLМОЙ = AAPL.to_csv("AAPL.csv")
INTCМОЙ = INTC.to_csv("INTC.csv")
AMZNМОЙ = AMZN.to_csv("AMZN.csv")
JNJМОЙ = JNJ.to_csv("JNJ.csv")
PFEМОЙ = PFE.to_csv("PFE.csv")
WMTМОЙ = WMT.to_csv("WMT.csv")
PGМОЙ = PG.to_csv("PG.csv")
KOМОЙ = KO.to_csv("KO.csv")
CМОЙ = C.to_csv("C.csv")
GOOGLМОЙ = GOOGL.to_csv("GOOGL.csv")
JPMМОЙ = JPM.to_csv("JPM.csv")
GEМОЙ = GE.to_csv("GE.csv")
XOMМОЙ = XOM.to_csv("XOM.csv")
XМОЙ = X.to_csv("X.csv")
RIOМОЙ = RIO.to_csv("RIO.csv")
PKXМОЙ = PKX.to_csv("PKX.csv")
SQМОЙ = SQ.to_csv("SQ.csv")
DEМОЙ = DE.to_csv("DE.csv")
BGМОЙ = BG.to_csv("BG.csv")
FCXМОЙ = FCX.to_csv("FCX.csv")
VALEМОЙ = VALE.to_csv("VALE.csv")
NVDAМОЙ = NVDA.to_csv("NVDA.csv")
INTCМОЙ = INTC.to_csv("INTC.csv")
QCOMМОЙ = QCOM.to_csv("QCOM.csv")








#  SIMON'S PORTFOLIO USD
# AAPLBA=get_Data("AAPL.BA")                           
# MSFT=get_Data("MSFT")         
# INTC=get_Data("INTC")         
# GOOGL=get_Data("GOOGL")       
# AMZN=get_Data("AMZN")         
# JNJ=get_Data("JNJ")           
# PFE=get_Data("PFE")           
# WMT=get_Data("WMT")           
# PG=get_Data("PG")             
# KO=get_Data("KO")             
# C=get_Data("C")               
# JPM=get_Data("JPM")           
# GE=get_Data("GE")             
# XOM=get_Data("XOM")           
# X=get_Data("X") 

# AAPLBAМОЙ = AAPLBA.to_csv("AAPLBA.csv")
# MSFTМОЙ = MSFT.to_csv("MSFT.csv")
# INTCМОЙ = INTC.to_csv("INTC.csv")
# GOOGLМОЙ = GOOGL.to_csv("GOOGL.csv")
# AMZNМОЙ = AMZN.to_csv("AMZN.csv")
# JNJМОЙ = JNJ.to_csv("JNJ.csv")
# PFEМОЙ = PFE.to_csv("PFE.csv")
# WMTМОЙ = WMT.to_csv("WMT.csv")
# PGМОЙ = PG.to_csv("PG.csv")
# KOМОЙ = KO.to_csv("KO.csv")
# CМОЙ = C.to_csv("C.csv")
# JPMМОЙ = JPM.to_csv("JPM.csv")
# GEМОЙ = GE.to_csv("GE.csv")
# XOMМОЙ = XOM.to_csv("XOM.csv")
# XМОЙ = X.to_csv("X.csv")



### EUROPEAN BANKS
    
# SAN_MC=get_Data("SAN.MC")
# BBVA_MC=get_Data("BBVA.MC")
# GLE_PA=get_Data("GLE.PA")
# BNP_PA=get_Data("BNP.PA")
# INGA_AS=get_Data("INGA")
# KBC_BR=get_Data("KBC.BR")
# UCG_MI=get_Data("UCG.MI")
# ISP_MI=get_Data("ISP.MI")
# DBK_DE=get_Data("DBK.DE")
# CBK_DE=get_Data("CBK.DE")

# SAN_MCМОЙ = SAN_MC.to_csv("SAN.MC.csv")
# BBVA_MCМОЙ = BBVA_MC.to_csv("BBVA.MC.csv")
# GLE_PAМОЙ = GLE_PA.to_csv("GLE.PA.csv")
# BNP_PAМОЙ = BNP_PA.to_csv("BNP.PA.csv")
# INGA_ASМОЙ = INGA_AS.to_csv("INGA.AS.csv")
# KBC_BRМОЙ = KBC_BR.to_csv("KBC.BR.csv")
# UCG_MIМОЙ = UCG_MI.to_csv("UCG.MI.csv")
# ISP_MIМОЙ = ISP_MI.to_csv("ISP.MI.csv")
# DBK_DEМОЙ = DBK_DE.to_csv("DBK.DE.csv")
# CBK_DEМОЙ = CBK_DE.to_csv("CBK.DE.csv")

## INDEXS 
# SPY=get_Data("SPY")       
# SPYGSPC=get_Data('^GSPC')
# VIX=get_Data('^VIX')
# NASDAQ=get_Data('^IXIC')
# QQQ=get_Data('QQQ')
# DJI=get_Data('^DJI')

# SPYМОЙ = SPY.to_csv("SPY.csv")
# SPYGSPCМОЙ = SPYGSPC.to_csv("^GSPC.csv")
# VIXМОЙ = VIX.to_csv("^VIX.csv")
# NASDAQМОЙ = NASDAQ.to_csv("^IXIC.csv")
# QQQМОЙ = QQQ.to_csv("QQQ.csv")
# DJIМОЙ = DJI.to_csv("^DJI.csv")


## MINERS UK
# AAL_L=get_Data('AAL.L')
# ANTO_L=get_Data('ANTO.L')
# GLEN_L=get_Data('GLEN.L')
# MT_AS=get_Data('MT.AS')
# RIO_L=get_Data('RIO.L')

# AAL_LМОЙ = AAL_L.to_csv('AAL.L.csv')
# ANTO_LМОЙ = ANTO_L.to_csv('ANTO.L.csv') 
# GLEN_LМОЙ = GLEN_L.to_csv('GLEN.L.csv')
# MT_ASМОЙ = MT_AS.to_csv('MT.AS.csv')
# RIO_LМОЙ = RIO_L.to_csv('RIO.L.csv')

# # Petroleros 
# TOTAL_PA = get_Data('FP.PA')
# REP_MC = get_Data('REP.MC')   

# TOTAL_PAМОЙ = TOTAL_PA.to_csv('FP.PA.csv')
# REP_MCМОЙ = REP_MC.to_csv('REP_MC.csv')

# ##   CRYPTOS 
# BTC=get_Data('BTC-USD')
# BNB=get_Data('BNB-USD')
# ETH=get_Data('ETH-USD')
# ADA=get_Data('ADA-USD')
# DOGE=get_Data('DOGE-USD')
# DOT=get_Data('DOT1-USD')

# BTCМОЙ = BTC.to_csv('BTC.csv')
# BNBМОЙ = BNB.to_csv('BNB.csv')
# ETHМОЙ = ETH.to_csv('ETH.csv')
# ADAМОЙ = ADA.to_csv('ADA.csv')
# DOGEМОЙ = DOGE.to_csv('DOGE.csv')
# DOTМОЙ = DOT.to_csv('DOT.csv')



# SQ=get_Data("SQ")         
# RIO=get_Data("RIO")         
# TSM=get_Data("TSM")         
# SHOP=get_Data("SHOP")           
# DIS=get_Data("DIS")         
# MCD=get_Data("MCD")         
# V=get_Data("V")       
# AUY=get_Data("AUY")         
# AZN=get_Data("AZN")           
# BIIB=get_Data("BIIB")           
# WMT=get_Data("WMT")           
# PG=get_Data("PG")             
# KO=get_Data("KO")             
# C=get_Data("C")               
# JPM=get_Data("JPM")           
# GE=get_Data("GE")             
# XOM=get_Data("XOM")           
# X=get_Data("X") 

# SQМОЙ = SQ.to_csv("SQ.csv")
# RIOМОЙ = RIO.to_csv("RIO.csv")
# TSMМОЙ = TSM.to_csv("TSM.csv")
# SHOPМОЙ = SHOP.to_csv("SHOP.csv")
# DISМОЙ = DIS.to_csv("DIS.csv")
# MCDМОЙ = MCD.to_csv("MCD.csv")
# VМОЙ = V.to_csv("V.csv")
# AUYМОЙ = AUY.to_csv("AUY.csv")
# AZNМОЙ = AZN.to_csv("AZN.csv")
# BIIBМОЙ = BIIB.to_csv("BIIB.csv")
# WMTМОЙ = WMT.to_csv("WMT.csv")
# PGМОЙ = PG.to_csv("PG.csv")
# KOМОЙ = KO.to_csv("KO.csv")
# CМОЙ = C.to_csv("C.csv")
# JPMМОЙ = JPM.to_csv("JPM.csv")
# GEМОЙ = GE.to_csv("GE.csv")
# XOMМОЙ = XOM.to_csv("XOM.csv")
# XМОЙ = X.to_csv("X.csv")




