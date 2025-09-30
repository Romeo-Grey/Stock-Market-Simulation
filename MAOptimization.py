import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import strategies
testperiod = 250
sp500_hourly_data = yf.download("SPY", period="5y", interval="1d")
sp500_hourly_dataBH = sp500_hourly_data.tail(testperiod).copy()
sp500_hourly_dataBH['Returns'] = sp500_hourly_dataBH['Close'].pct_change() * 100
short_range = range(20, 50, 1)
long_range = range(50, 250, 5)
results = []
for short in short_range:
    for long in long_range:
        if short >= long:
            continue
        portfolio = strategies.MovingAverage(sp500_hourly_data, short, long, testperiod)
        
        plt.plot(portfolio)
        returns = pd.Series(portfolio).pct_change().dropna()
        returns = returns.astype(float)
        annual_return = ((portfolio[-1] / portfolio[0])**(252/len(portfolio))) - 1
        volatility = returns.std() * (252**0.5)
        sharpe = (annual_return - 0.02) / volatility

        results.append((short, long, annual_return.astype(float), volatility, sharpe))

results_df = pd.DataFrame(results, columns=["Short", "Long", "Return", "Volatility", "Sharpe"])
results_df = results_df.astype(float)
best = results_df.sort_values("Sharpe", ascending=False)
#best.to_csv("MABruteForceResults.csv")
print(best.head(10))

returnsBH = pd.Series(strategies.BuyandHold(sp500_hourly_dataBH, testperiod))
plt.plot(returnsBH, color = 'red', linewidth = 3, label = 'BH')
plt.legend()
plt.show()