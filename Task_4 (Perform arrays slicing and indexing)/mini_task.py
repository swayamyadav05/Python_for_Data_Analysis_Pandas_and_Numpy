import numpy as np


my_numpy_array = np.array([3, 5, 6, 2, 8, 10, 20, 50])
print(my_numpy_array)
print("-" * 75)

# Access specific index from the numpy array
print(my_numpy_array[-1])
print("-" * 75)

# Starting from the first index 0 up until and NOT including the last element
print(my_numpy_array[0:3])
print("-" * 75)

# Broadcasting, altering several values in a numpy array at once
my_numpy_array[0:4] = 7
print(my_numpy_array)
print("-" * 75)


# Let's define a two dimensional numpy array
matrix = np.random.randint(1, 10, (4, 4))
print(matrix)
print("-" * 75)


# Get a row from a mtrix
matrix[1]
print(matrix)
print("-" * 75)


# Get one element
matrix[0, 1]
matrix[0][1]
print(matrix)
print("-" * 75)


"""
MINI CHALLENGE #4:

In the following matrix, replace the last row with 0
X = [2 30 20 -2 -4]
    [3 4  40 -3 -2]
    [-3 4 -6 90 10]
    [25 45 34 22 12]
    [13 24 22 32 37]
"""

X = np.array(
    [
        [2, 30, 20, -2, -4],
        [3, 4, 40, -3, -2],
        [-3, 4, -6, 90, 10],
        [25, 45, 34, 22, 12],
        [13, 24, 22, 32, 37],
    ]
)
X[4] = 0
print(X)
print("-" * 75)
