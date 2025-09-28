import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import utils
import strategies

sp500_hourly_data = yf.download("SPY", period="1y", interval="1d")
sp500_hourly_data['Returns'] = sp500_hourly_data['Close'].pct_change() * 100
returnsBH = pd.Series(strategies.BuyandHold(sp500_hourly_data))
BH_returns = utils.StrategyReturns(returnsBH)
print(f"{BH_returns.iloc[-1]}")
plt.plot(utils.StrategyReturns(returnsBH))
#plt.plot(returnsBH, color = 'blue') # Show BH value
plt.show()
