import numpy as np
my_list = (10, 20, 30, 40, 50, 60, 70, 80)
arr = np.array(my_list)
print("Array:", arr)
arrayreshape = arr.reshape(2,2, 2)
print("\n", arrayreshape)
print("\nsize:", arrayreshape.size)
print("shape:", arrayreshape.shape)
print("dimension:", arrayreshape.ndim)