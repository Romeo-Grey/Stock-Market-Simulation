import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import strategies
testperiod = 250
sp500_hourly_data = yf.download("SPY", period="5y", interval="1d")
sp500_hourly_dataBH = sp500_hourly_data.tail(testperiod).copy()
sp500_hourly_dataBH['Returns'] = sp500_hourly_dataBH['Close'].pct_change() * 100
short_range = range(43, 48, 1)
long_range = range(60, 63, 1)
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
best = results_df.sort_values("Sharpe", ascending=False).head(10)
print(best)

returnsBH = pd.Series(strategies.BuyandHold(sp500_hourly_dataBH, testperiod))
plt.plot(returnsBH, color = 'red', linewidth = 3, label = 'BH')
plt.legend()
plt.show()





















# def MovingAverageOptimization(sp500_dataMA, sp500_data , minshort = 5, maxshort = 20, minlong = 50, maxlong = 200, amounttests = 3):
#     shortTimes = []
#     longTimes = []
#     total_returns = []
    
#     for i in range(amounttests):
#         shortTimes.append(randint(minshort, maxshort))
#         longTimes.append(randint(minlong, maxlong))
#     short_ma = pd.DataFrame()
#     long_ma = pd.DataFrame()

    
    
#     close_PricesMA = sp500_dataMA['Close'].astype(float)
#     close_Price = sp500_data['Close'].astype(float)
#     returnlength = len(close_Price)


#     for i in range(len(shortTimes)):
#         short_ma[f"{i}"] = close_PricesMA.rolling(shortTimes[i]).mean().dropna()
#         short_ma = short_ma.copy()

#     for i in range(len(longTimes)): 
#         long_ma[f"{i}"] = close_PricesMA.rolling(longTimes[i]).mean().dropna()
#         long_ma = long_ma.copy()
#     short_ma = short_ma.iloc[-returnlength:,:]
#     long_ma = long_ma.iloc[-returnlength:,:]
    

    
#     for i in range(amounttests):
#         signal = (short_ma.iloc[:,i] > long_ma.iloc[:,i]).astype(int).tolist()

#         portfolioValue = [close_Price.iloc[0]]

#         for i in range(1, len(close_Price)):
#             if signal[i] == 1: 
#                 portfolioValue.append(portfolioValue[-1] * (close_Price.iloc[i] / close_Price.iloc[i-1]))
#             else:
#                 portfolioValue.append(portfolioValue[-1])
#         plt.plot(portfolioValue)
#         total_returns.append(portfolioValue[-1])
#     plt.show()
#     total_returns = pd.Series(total_returns).astype(float)
#     maxProfit = max(total_returns)
#     best_index = total_returns.idxmax()
    
#     print("\nStrategy Results:")
#     print("=================")
#     print(f"Best Profit: {maxProfit:.2f}")
#     print(f"Best Return Percentage: {maxProfit / close_Price.iloc[0].astype(float) * 100}%")
#     print(f"Best Short MA Period: {shortTimes[best_index]}")
#     print(f"Best Long MA Period: {longTimes[best_index]}")
#     print(f"Average Return: {total_returns.mean()}")
#     print(f"Average Percentage: {total_returns.mean() / close_Price.iloc[0].astype(float) * 100}%")
    
#     return shortTimes[best_index], longTimes[best_index]
# sp500_hourly_data = yf.download("SPY", period=f"{1500+ 200}d", interval="1d")
# sp500_hourly_data1 = yf.download("SPY", period="5y", interval="1d")

# MovingAverageOptimization(sp500_hourly_data, sp500_hourly_data1, 5, 20, 50, 200, 100)
