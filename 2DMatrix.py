# Creating a 2D array (matrix) A
import numpy as np
rows = 3
columns = 4
matrix_A = [[0 for j in range(columns)] for i in range(rows)]
for i in range(rows):
    for j in range(columns):
        matrix_A[i][j] = i * columns + j + 1
print("Matrix A:")
for row in matrix_A:
    print(row)

'''
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Matrix A:\n",A)
'''

'''
rows = 3
cols = 3

# Using a nested list comprehension to create the matrix
A = [[3 for _ in range(cols)] for _ in range(rows)]

# Printing the matrix A
for row in A:
    print(row)
'''