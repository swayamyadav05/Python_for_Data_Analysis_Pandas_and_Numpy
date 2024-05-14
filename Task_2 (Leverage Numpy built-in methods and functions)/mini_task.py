import numpy as np

# "rand()" uniform distribution between 0 and 1
x = np.random.rand(20)
print(x)
print("*" * 75)


# "rand()" uniform distribution between 0 and 1
x = np.random.rand(20)
print(x)
print("*" * 75)


# "randint" is used to generate random integers between upper and lower bounds
x = np.random.randint(1, 50)
print(x)
print("*" * 75)


# "randint" can be used to generate a certain number of random integers as follows
x = np.random.randint(1, 100, 50)
print(x)
print("*" * 75)


# np.arange creates an evenly spaced values within a given interval
x = np.arange(1, 30)
print(x)
print("*" * 75)


# create a diagonal of ones and zeros everywhere else
x = np.eye(7)
print(x)
print("*" * 75)


# Array of zeros
x = np.zeros(9)
print(x)
print("*" * 75)


"""

MINI CHALLENGE #2:

Write a code that takes in a positive integer "x" from the user and creates a 1x10 array with random numbers ranging from 0 to "x"

"""

# x = int(input("Enter a positive integer: "))
x = 5
my_array = np.random.randint(0, x, 10)
# my_array

print(my_array)
print("*" * 75)


"""

MINI CHALLENGE #2:

Write a code that takes in a positive integer "x" from the user and creates a 2x10 array with random numbers ranging from 0 to "x"

"""

# x = int(input("Enter a positive integer: "))
x = 10
my_array = np.random.randint(0, x, (2, 10))
# my_array

print(my_array)
print("*" * 75)
