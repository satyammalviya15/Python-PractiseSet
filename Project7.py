import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to fetch stock data from Alpha Vantage API
def fetch_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'Time Series (5min)' in data:
        time_series = data['Time Series (5min)']
        df = pd.DataFrame.from_dict(time_series, orient='index')
        df = df[['1. open', '2. high', '3. low', '4. close', '5. volume']]
        df = df.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. volume': 'Volume'})
        df.index = pd.to_datetime(df.index)
        return df
    else:
        print("Error: Could not retrieve data. Please check the stock symbol or API key.")
        return None

# Function to display the stock price graph
def plot_stock_data(df, symbol):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Close'], label=f'{symbol} Closing Price')
    plt.title(f'Real-Time Stock Price for {symbol}')
    plt.xlabel('Time')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.show()

# Main function to fetch, display, and track stock prices
def main():
    symbol = input("Enter the stock symbol (e.g., AAPL for Apple): ").upper()
    api_key = 'your_alpha_vantage_api_key'  # Replace with your API key
    
    print(f"Fetching real-time data for {symbol}...")
    stock_data = fetch_stock_data(symbol, api_key)
    
    if stock_data is not None:
        print(f"Displaying real-time stock data for {symbol}...\n")
        print(stock_data.tail())  # Show the latest 5 records
        
        plot_stock_data(stock_data, symbol)
    
    else:
        print("Failed to fetch data.")

if __name__ == '__main__':
    main()