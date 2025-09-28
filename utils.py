import pandas as pd
def ReturnPercentage(strat_return):
    return strat_return.pct_change() * 100
def StrategyReturns(strat_return):
    return_pct = ReturnPercentage(strat_return)
    total_returns = pd.Series([0])

    for i in range((len(return_pct) -1)):
        #print(return_pct_list[i])
        total_returns.loc[i+1] = total_returns.loc[i] + (return_pct.iloc[i + 1])
    return total_returns