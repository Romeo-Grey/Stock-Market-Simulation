import pandas as pd
import yfinance as yf
def BuyandHold(sp500_data, testperiod):
    sp500_data_trimmed = sp500_data.tail(testperiod)
    close_Prices = sp500_data_trimmed['Close']
    start_Price = close_Prices.iloc[0]
    #print(start_Price)
    end_Price = []
    end_Price.append(start_Price)
    for i in range((len(sp500_data_trimmed['Returns']) - 1)):
        #print(sp500_hourly_data['Returns'].iloc[i+1])
        end_Price.append(end_Price[i] * ((sp500_data_trimmed['Returns'].iloc[i+1] / 100) + 1))
        #print(end_Price)
        
    return end_Price

def MovingAverage(sp500_data, short, long, testperiod):
    #print(len(sp500_data['Close']))
    #print(returnlength)
    if testperiod > len(sp500_data['Close']): testperiod = len(sp500_data['Close'])
    
    close_PricesMA = sp500_data['Close']
    close_Price = sp500_data['Close']
    close_PricesMA = close_PricesMA.tail(testperiod*2)
    close_Price = close_Price.tail(testperiod)
    
    short_ma = close_PricesMA.rolling(short).mean().dropna()
    long_ma = close_PricesMA.rolling(long).mean().dropna()
    
    short_ma = short_ma.tail(testperiod)
    short_ma = short_ma.iloc[:,0]
    long_ma = long_ma.tail(testperiod)
    long_ma = long_ma.iloc[:,0]
    #print(short_ma)
    ma_df = pd.DataFrame({'short': short_ma, 'long': long_ma}).dropna()
    #print(ma_df)

    signal = (ma_df['short'] > ma_df['long']).astype(int).tolist()
    #print(close_Price.iloc[-testperiod])
    portfolioValue = [close_Price.iloc[-testperiod]]
    #print(close_Price.iloc[0])

    for i in range(1, len(signal)):
        #print(i)
        if signal[i] == 1: 
            portfolioValue.append(portfolioValue[-1] * (close_Price.iloc[i] / close_Price.iloc[i-1]))
        else:
            portfolioValue.append(portfolioValue[-1])
    #print(f"Starting ammount: {portfolioValue[0]} Ending amount: {portfolioValue[-1]}")
    return portfolioValue

def MomentumStrategy(sp500_data, lookback, testperiod):
    sp500_data_trimmed = sp500_data.tail(testperiod)
    close_PricesMomentum = sp500_data['Close']
    close_Price = sp500_data_trimmed['Close']
    momentum = close_PricesMomentum.pct_change(lookback).dropna()
    momentum = momentum.tail(testperiod)

    signal = (momentum > 0).astype(int).shift(1).fillna(0)
    signal = pd.Series(signal.iloc[:,0].astype(int))
    signal = signal.tolist()
    portfolioValue = [close_Price.iloc[0]]

    for i in range(1, len(close_Price)):
        if signal[i] == 1:
            portfolioValue.append(portfolioValue[-1] * (close_Price.iloc[i] / close_Price.iloc[i-1]))
        else:
            portfolioValue.append(portfolioValue[-1])
    return portfolioValue