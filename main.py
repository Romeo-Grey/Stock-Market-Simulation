import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import utils
import strategies

sp500_hourly_data = yf.download("SPY", period="1y", interval="1d")
sp500_hourly_data['Returns'] = sp500_hourly_data['Close'].pct_change() * 100
returnsBH = pd.Series(strategies.BuyandHold(sp500_hourly_data))
returnsMA = pd.Series(strategies.MovingAverage(sp500_hourly_data, 20, 100))
returnsMOM = pd.Series(strategies.MomentumStrategy(sp500_hourly_data, 5))
BH_returns = utils.StrategyReturns(returnsBH)
#print(f"{BH_returns.iloc[-1]}")
#print(utils.ReturnPercentage(returnsBH))

print(f"Total BH Volatility {utils.Volitility(returnsBH)}")
print(f"Total MA Volatility {utils.Volitility(returnsMA)}")
print(f"Total MOM Volatility {utils.Volitility(returnsMOM)}")

print(f"Total Annualized Return For BH {round(utils.AnnualizedReturn(returnsBH) * 100, 4)}%")
print(f"Total Annualized Return For MA {round(utils.AnnualizedReturn(returnsMA) * 100, 4)}%")
print(f"Total Annualized Return For MOM {round(utils.AnnualizedReturn(returnsMOM) * 100, 4)}%")

print(f"Sharpe Ratio For BH {utils.SharpeRatio(returnsBH)}")
print(f"Sharpe Ratio For MA {utils.SharpeRatio(returnsMA)}")
print(f"Sharpe Ratio For MOM {utils.SharpeRatio(returnsMOM)}")

print(f"Max Drawdown for BH {round(utils.MaxDrawDown(returnsBH) * 100, 4)}%")
print(f"Max Drawdown for MA {round(utils.MaxDrawDown(returnsMA) * 100, 4)}%")
print(f"Max Drawdown for MOM {round(utils.MaxDrawDown(returnsMOM) * 100, 4)}%")

plt.subplot(1,3,1)
plt.plot(utils.ReturnPercentage(returnsBH), color = 'blue', label = 'BH Strategy') # Show Daily Return Percentage for BH Strategy
plt.plot(utils.ReturnPercentage(returnsMA), color = 'red', label = 'MA Strategy') # Show Daily Return Percentage for MA Strategy
plt.plot(utils.ReturnPercentage(returnsMOM), color = 'green', label = 'MOM Strategy') # Show Daily Return Percentage For MOM Strategy
plt.legend()
plt.title("Daily Return Percentage")

plt.subplot(1,3,2)
plt.plot(utils.StrategyReturns(returnsBH), color = 'blue', label='BH Strategy') # Show Total Return Percentage for BH Stratety
plt.plot(utils.StrategyReturns(returnsMA), color = 'red', label = 'MA Strategy') # Show Total Return Percentage for MA Strategy
plt.plot(utils.StrategyReturns(returnsMOM), color = 'green', label = 'MOM Strategy') # Show Total Return Percentage for MOM Strategy
plt.legend()
plt.title("Total Return Percentage")

plt.subplot(1,3,3)
plt.plot(returnsBH, color = 'blue', label = 'BH Strategy') # Show BH value
plt.plot(returnsMA, color = 'red', label = 'MA Strategy') # Show MA value
plt.plot(returnsMOM, color = 'green', label = 'MOM Strategy') # Show MOM value
plt.legend()
plt.title("Strat values")

plt.show()
