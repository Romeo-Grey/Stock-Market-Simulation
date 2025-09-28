import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

sp500_hourly_data = yf.download("SPY", period="5y", interval="1d")
sp500_hourly_data['Returns'] = sp500_hourly_data['Close'].pct_change() * 100

def BuyandHold():
    close_Prices = sp500_hourly_data['Close']
    start_Price = close_Prices.iloc[0]
    print(start_Price)
    end_Price = []
    end_Price.append(start_Price)
    for i in range((len(sp500_hourly_data['Returns']) - 1)):
        #print(sp500_hourly_data['Returns'].iloc[i+1])
        end_Price.append(end_Price[i] * ((sp500_hourly_data['Returns'].iloc[i+1] / 100) + 1))
        #print(end_Price)
        
    return end_Price

returns = BuyandHold()
returns = pd.Series(returns)
return_pct = returns.pct_change()
print(returns)
plt.plot(returns, color = 'blue')
plt.show()
