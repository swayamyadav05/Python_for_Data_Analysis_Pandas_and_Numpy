import numpy as np

# np.arange() returns an evenly spaced values within a given interval
x = np.arange(1, 10)
print(x)
print("*" * 75)

y = np.arange(1, 10)
print(y)
print("*" * 75)

# Add 2 numpy arrays together
sum = x + y
print(sum)
print("*" * 75)

# square
square = x**2
print(square)
print("*" * 75)

# sqrt
sqrt = np.sqrt(square)
print(sqrt)
print("*" * 75)

z = np.exp(y)
print(z)
print("*" * 75)

"""
MINI CHALLENGE #3:

Given the X and Y values below, obtain the distance between them
X = [5, 7, 20]
Y = [9, 15, 4]

"""

X = np.array([5, 7, 20])
Y = np.array([9, 15, 4])

Z = np.sqrt(X**2 + Y**2)
print(Z)
