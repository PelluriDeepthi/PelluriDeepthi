import numpy as np

# Create matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Create identity matrix B
#B = np.identity(3)
B = np.eye(3)

# Addition of matrices A and B
sum_matrix = A + B

# Multiplication of matrices A and B
product_matrix = np.dot(A, B)
#product_matrix = A * B

# Printing the result matrices
print("Matrix A:\n",A)

print("\nIdentity Matrix B:")
print(B)

print("\nSum of A and B:")
print(sum_matrix)

print("\nProduct of A and B:")
print(product_matrix)