import numpy as np

# Create matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Create a matrix filled with ones, having the same dimensions as A
B = np.ones_like(A)

# Addition of matrices A and B
sum_matrix = A + B

# Element-wise multiplication of matrices A and B
product_matrix = A * B
#product_matrix = np.dot(A, B)

# Printing the result matrices
print("Matrix A:")
print(A)

print("\nMatrix B (Filled with Ones):")
print(B)

print("\nSum of A and B:")
print(sum_matrix)

print("\nProduct of A and B:")
print(product_matrix)