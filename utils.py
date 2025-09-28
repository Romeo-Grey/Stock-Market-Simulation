import pandas as pd
def StrategyReturns(strat_return):
    return_pct = strat_return.pct_change()
    total_returns = pd.Series([0])

    for i in range((len(return_pct) -1)):
        #print(return_pct_list[i])
        total_returns.loc[i+1] = total_returns.loc[i] + (return_pct.iloc[i + 1] * 100)
    return total_returns