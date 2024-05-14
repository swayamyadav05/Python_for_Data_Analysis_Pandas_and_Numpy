import pandas as pd

#  Let's define a dataframe as follows:
bank_client_df = pd.DataFrame(
    {
        "Bank Client ID": [111, 222, 333, 444],
        "Bank Client Name": ["Chanel", "Steave", "Ryan", "Swayam"],
        "Net Worth [$]": [3500, 29000, 10000, 38000],
        "Years with bank": [3, 4, 9, 5],
    }
)
print(bank_client_df)
print("-" * 75)
print("-" * 75)


# Pick certain rows that satisfy a certain criteria
df_loyal = bank_client_df[bank_client_df["Years with bank"] >= 5]
print(df_loyal)
print("-" * 75)

# Delete a column from a DataFrame
del bank_client_df["Bank Client ID"]
print(bank_client_df)
print("-" * 75)

"""
MINI CHALLENGE #8:

Using "bank_client_df" DataFrame, leverage pandas operations to only select high networth individuals with minimum $5000
What is the combined networth for all customers with 5000+ networth? 
"""

bank_client_df = pd.DataFrame(
    {
        "Bank Client ID": [111, 222, 333, 444],
        "Bank Client Name": ["Chanel", "Steave", "Ryan", "Swayam"],
        "Net Worth [$]": [3500, 29000, 10000, 38000],
        "Years with bank": [3, 4, 9, 5],
    }
)
print(bank_client_df)
print("-" * 75)
print("-" * 75)

df_high_salary = bank_client_df[bank_client_df["Net Worth [$]"] >= 5000]
print(df_high_salary)
print("-" * 75)

total_networth = sum(df_high_salary["Net Worth [$]"])
print(total_networth)
print("-" * 75)
total_networth = df_high_salary["Net Worth [$]"].sum()
print(total_networth)
print("-" * 75)

# To find standard deviation of the Net Worth
sd_deviation = bank_client_df["Net Worth [$]"].std()
print(sd_deviation)
print("-" * 75)
