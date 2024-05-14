import numpy as np

matrix = np.random.randint(1, 10, (5, 5))
print(matrix)
print("-" * 30)

new_matrix = matrix[matrix > 7]
print(new_matrix)
print("-" * 30)

# Obtain odd elements only
new_matrix = matrix[matrix % 2 == 0]
print(new_matrix)
print("-" * 30)


"""
MINI CHALLENGE #5:
- In the following matrix, replace negative elements by 0 and replace odd elements with -2


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
X[X < 0] = 0
X[X % 2 == 1] = -2
print(X)
print("-" * 30)
