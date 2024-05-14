# Pandas is a data manipulation and analysis tool that is built on Numpy.
# Pandas uses a data structure known as DataFrame (think of it as Microsoft excel in Python).
# DataFrames empower programmers to store and manipulate data in a tabular fashion (rows and columns).
# Series Vs. DataFrame? Series is considered a single column of a DataFrame.

import pandas as pd

# Let's define a two-dimensional Pandas DataFrame
# Note that you can create a pandas dataframe from a python dictionary

bank_client_df = pd.DataFrame(
    {
        "Bank Client ID": [111, 222, 333, 444],
        "Bank Client Name": ["Chanel", "Steave", "Ryan", "Swayam"],
        "Net Worth [$]": [3500, 29000, 10000, 38000],
        "Years with bank": [3, 4, 8, 5],
    }
)
print(bank_client_df)
print("-" * 80)

# Let's obtain the data type
print(type(bank_client_df))


# you can only view the first couple of rows using .head()
print(bank_client_df.head(2))
print("-" * 80)


# you can only view the last couple of rows using .tail()
print(bank_client_df.tail(2))
print("-" * 80)


"""
MINI CHALLENGE #6:

A porfolio contains a collection of securities such as stocks, bonds and ETFs. Define a dataframe named 'portfolio_df' that holds 3 different stock ticker symbols, number of shares, and price per share (feel free to choose any stocks)
Calculate the total value of the porfolio including all stocks
"""

portfolio_df = pd.DataFrame(
    {
        "Stock ticker symbol": ["APPL", "AMZN", "T"],
        "Price per shares": [2300, 4900, 5030],
        "Number of shares": [3, 9, 4],
    }
)
print(portfolio_df)
print("-" * 80)


portfolio_df = portfolio_df["Price per shares"] * portfolio_df["Number of shares"]
print(portfolio_df)
print("-" * 80)
