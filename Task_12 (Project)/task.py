"""
Define a dataframe named 'Bank_df_1' that contains the first and last names for 5 bank clients with IDs = 1, 2, 3, 4, 5
Assume that the bank got 5 new clients, define another dataframe named 'Bank_df_2' that contains a new clients with IDs = 6, 7, 8, 9, 10
Let's assume we obtained additional information (Annual Salary) about all our bank customers (10 customers)
Concatenate both 'bank_df_1' and 'bank_df_2' dataframes
Merge client names and their newly added salary information using the 'Bank Client ID'
Let's assume that you became a new client to the bank
Define a new DataFrame that contains your information such as client ID (choose 11), first name, last name, and annual salary.
Add this new dataframe to the original dataframe 'Bank_df_all'.
"""

import pandas as pd

Bank_df_1 = pd.DataFrame(
    {
        "Bank Client ID": ["1", "2", "3", "4", "5"],
        "First Name": ["Swayam", "John", "Alex", "Salvi", "Loki"],
        "Last Name": ["Yadav", "Camber", "Xender", "Tate", "Oddinson"],
    }
)

print(Bank_df_1)
print("-" * 75)

# Let's define another dataframe for a seperate list of clients (IDs = 6, 7, 8, 9, 10)

Bank_df_2 = pd.DataFrame(
    {
        "Bank Client ID": ["6", "7", "8", "9", "10"],
        "First Name": ["Abc", "Aab", "Abb", "Acc", "Aba"],
        "Last Name": ["Bba", "Bbb", "Bbc", "Baa", "Bcc"],
    }
)

print(Bank_df_2)
print("-" * 75)

# Let's assume we obtained additional information (Annual Salary) about our bank customers
# Note that data obtained is for all clients with IDs 1 to 10

Bank_df_salary = pd.DataFrame(
    {
        "Bank Client ID": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        "Annual Salary [$/year]": [
            25000,
            35000,
            45000,
            40000,
            34000,
            50000,
            29000,
            44000,
            47000,
            36000,
        ],
    }
)
print(Bank_df_salary)
print("-" * 75)


# Let's concatenate both dataframes #1 and #2
# Note that we now have client IDs from 1 to 10

Bank_df_all = pd.concat([Bank_df_1, Bank_df_2])
print(Bank_df_all)
print("-" * 75)

# Let's merge all data on 'Bank Client ID'

Bank_df_all = pd.merge(Bank_df_all, Bank_df_salary, on="Bank Client ID")
print(Bank_df_all)
print("-" * 75)

# Let's assume new data frame of new client as

new_client_df = pd.DataFrame(
    {
        "Bank Client ID": ["11"],
        "First Name": ["Sway"],
        "Last Name": ["Yad"],
        "Annual Salary [$/year]": [43000],
    }
)

print(new_client_df)
print("-" * 75)

# Concatenate with the original Bank_df_all

Bank_df_all = pd.concat([Bank_df_all, new_client_df], axis=0)
print(Bank_df_all)
print("-" * 75)

list_of_names_of_columns = Bank_df_all.columns
print(list_of_names_of_columns)
