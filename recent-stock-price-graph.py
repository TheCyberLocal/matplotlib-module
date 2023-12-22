"""
The script is designed for users who want to visualize stock price trends without complex analysis tools.
It provides a way to view the recent performance of a stock by simply inputting its ticker symbol,
 making it accessible for both casual observers and seasoned investors.
"""

import yfinance as yf  # yfinance is used to fetch financial data from Yahoo Finance.
import matplotlib.pyplot as plt  # matplotlib.pyplot is used for plotting data.

# Define a function to graph stock data based on ticker symbol.
def graph_stock(ticker):
    # Fetch stock data using yfinance for the given ticker.
    stock = yf.Ticker(ticker)  # Create a Ticker object for the specified stock.
    data = stock.history(period="1mo")  # Retrieve stock history for the last month.

    # Plotting the data.
    plt.figure(figsize=(10, 5))  # Set the size of the plot.
    data['Close'].plot(title=f"{ticker} Stock Price - Last Month")  # Plot the closing price.
    plt.xlabel('Date')  # Label for the x-axis.
    plt.ylabel('Price (USD)')  # Label for the y-axis.

    plt.show()  # Display the plot.

# Prompt the user for a ticker symbol.
ticker = input("Enter the stock ticker symbol: ")
graph_stock(ticker)  # Call the function with the user input.
