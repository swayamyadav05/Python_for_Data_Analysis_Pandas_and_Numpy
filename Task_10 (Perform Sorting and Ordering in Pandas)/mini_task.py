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
print("-" * 75)
print("Dataframe of the Bank Clients")
print("-" * 75)

print(bank_client_df)
print("-" * 75)
print("-" * 75)

# You can sort the values in the dataframe according to number of years with bank
sort_by_years = bank_client_df.sort_values(by="Years with bank")
print("Sorted by number of years with the bank")
print("-" * 75)

print(sort_by_years)
print("-" * 75)
print("-" * 75)

# Note that nothing changed in memory! you have to make sure that inplace is set to True
print("Dataframe of the Bank Clients after sorting")
print("-" * 75)

print(bank_client_df)
print("-" * 75)

print("Note that nothing changed in memory!")
print("-" * 75)
print("-" * 75)

# Set inplace = True to ensure that change has taken place in memory
bank_client_df.sort_values(by="Years with bank", inplace=True)
print("Dataframe of the Bank Clients after sorting and using inplace = True")
print("-" * 75)

print(bank_client_df)
print("-" * 75)

print("Change has taken place in memory")
print("-" * 75)
