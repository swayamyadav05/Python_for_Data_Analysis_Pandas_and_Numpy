import pandas as pd

# Let's define a dataframe as follows:
bank_client_df = pd.DataFrame(
    {
        "Bank client ID": [111, 222, 333, 444],
        "Bank Client Name": ["Chanel", "Steve", "Mitch", "Ryan"],
        "Net worth [$]": [3500, 29000, 10000, 2000],
        "Years with bank": [3, 4, 9, 5],
    }
)
print(bank_client_df)
print("-" * 75)
print("-" * 75)


# Define a function that increases all clients networth (stocks) by a fixed value of 20% (for simplicity sake)
def networth_update(balance):
    return balance * 1.2


# You can apply a function to the DataFrame
print(bank_client_df["Net worth [$]"].apply(networth_update))
print("-" * 75)

print(bank_client_df["Bank Client Name"].apply(len))
print("-" * 75)

"""
MINI CHALLENGE #9:

Define a function that triples the stock prices and adds $200
Apply the function to the DataFrame
Calculate the updated total networth of all clients combined
"""

bank_client_df = pd.DataFrame(
    {
        "Bank client ID": [111, 222, 333, 444],
        "Bank Client Name": ["Chanel", "Steve", "Mitch", "Ryan"],
        "Net worth [$]": [3500, 29000, 10000, 2000],
        "Years with bank": [3, 4, 9, 5],
    }
)
print(bank_client_df)
print("-" * 75)


def networth_increase(balance):
    return balance * 3 + 200


print(bank_client_df["Net worth [$]"].apply(networth_increase))
print("-" * 75)
