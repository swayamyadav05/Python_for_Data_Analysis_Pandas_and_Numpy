# Check this out: https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

import pandas as pd

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)
print("-" * 75)
print("df1")
print("-" * 75)

print(df1)
print("-" * 75)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)
print("-" * 75)
print("df2")
print("-" * 75)

print(df2)
print("-" * 75)

df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)
print("-" * 75)
print("df3")
print("-" * 75)

print(df3)
print("-" * 75)

frames = [df1, df2, df3]

result = pd.concat(frames)

print("-" * 75)
print("Concatenated df")
print("-" * 75)
print(result)
print("-" * 75)

# frames_1 = [process_your_file(f) for f in files]
# result_1 = pd.concat(frame_1)
