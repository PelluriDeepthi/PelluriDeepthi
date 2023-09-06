import numpy as np

size = 3  # Adjust the size of the matrix as needed

# Create a diagonal matrix with ones using NumPy's eye function
diagonal_matrix = np.eye(size)
#diagonal_matrix = np.identity(size)

print("Diagonal matrix with ones:")
print(diagonal_matrix)
