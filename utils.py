import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
def ReturnPercentage(strat_return):
    return strat_return.pct_change() * 100
def StrategyReturns(strat_return):
    return_pct = ReturnPercentage(strat_return)
    total_returns = pd.Series([0])

    for i in range((len(return_pct) -1)):
        #print(return_pct_list[i])
        total_returns.loc[i+1] = total_returns.loc[i] + (return_pct.iloc[i + 1])
    return total_returns
def Volitility(priceData):
    returns = priceData.pct_change().dropna()
    daily_vol = returns.std()
    annual_vol = daily_vol * (252**0.5)
    return annual_vol
def AnnualizedReturn(priceData):
    annualizedReturn = ((priceData.iloc[-1] / priceData.iloc[0])**(1/(len(priceData.tolist())/252)) - 1).tolist()
    #print(annualizedReturn)
    return annualizedReturn[0]
  
def SharpeRatio(priceData):
    return (AnnualizedReturn(priceData) - 0.02) / Volitility(priceData)

def MaxDrawdown(priceData):
    price = pd.Series(priceData.astype(float))
    running_max = price.cummax()
    drawdown = (price / running_max) - 1
    max_dd = drawdown.min()

    return max_dd, running_max, drawdown