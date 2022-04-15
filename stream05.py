#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:07:16 2021

@author: leoprimero
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2, linregress

import stream_functions
importlib.reload(stream_functions)
import stream_classes
importlib.reload(stream_classes)

#imput parameters          inflacion
ric = 'portfolioIdealCroux'    #  ^IXIC ARS=X DBK.DE ^VIX SPY SGRE.MC SAN.MC FMS ^GDAXI ^STOXX50E
benchmark = 'SPY'       #  ^STOXX   ^STOXX50E'    portafolioIdealCroux    portafolioRealCroux
# file_extension = 'xlsx'  
capm = stream_classes.capm_manager(benchmark, ric)
capm.load_timeseries()
capm.compute()
capm.scatterplot()
capm.plot_normalized()
capm.plot_dual_axes()
print(capm)



