import pandas as pd
def BuyandHold(sp500_data):
    close_Prices = sp500_data['Close']
    start_Price = close_Prices.iloc[0]
    #print(start_Price)
    end_Price = []
    end_Price.append(start_Price)
    for i in range((len(sp500_data['Returns']) - 1)):
        #print(sp500_hourly_data['Returns'].iloc[i+1])
        end_Price.append(end_Price[i] * ((sp500_data['Returns'].iloc[i+1] / 100) + 1))
        #print(end_Price)
        
    return end_Price