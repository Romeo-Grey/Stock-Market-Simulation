def MovingAverage(sp500_data, short = 20, long = 100):
    returnlength = len(sp500_data['Returns'].tolist())
    sp500_hourly_data = yf.download("SPY", period=f"{returnlength*2}d", interval="1d")
    
    

    close_PricesMA = sp500_hourly_data['Close']  
    close_Price = sp500_data['Close']
    short_ma = close_PricesMA.rolling(short).mean().dropna()
    long_ma = close_PricesMA.rolling(long).mean().dropna()
    short_ma = short_ma.iloc[-returnlength:,0]
    long_ma = long_ma.iloc[-returnlength:,0]

    ma_df = pd.DataFrame({'short': short_ma, 'long': long_ma}).dropna()

    signal = (ma_df['short'] > ma_df['long']).astype(int).tolist()

    portfolioValue = [close_Price.iloc[0]]

    for i in range(1, len(close_Price)):
        if signal[i] == 1: 
            portfolioValue.append(portfolioValue[-1] * (close_Price.iloc[i] / close_Price.iloc[i-1]))
        else:
            portfolioValue.append(portfolioValue[-1])

    return portfolioValue