import numpy as np

zeroDarray = np.array(9)
oneDarray = np.array([9])
twoDarray = np.array([ [9,9],[9,9] ])
threeDarray = np.array([ [[9,9],[9,9] ], [[9,9],[9,9] ] ])
fourDarray = np.array([ [ [[9,9],[9,9]], [[9,9],[9,9]], [[9,9],[9,9]] ] ])

print(zeroDarray.ndim)
print(zeroDarray.size)
print(zeroDarray.shape)

print("\n",oneDarray.ndim)
print(oneDarray.size)
print(oneDarray.shape)

print("\n",twoDarray.ndim)
print(twoDarray.size)
print(twoDarray.shape)

print("\n",threeDarray.ndim)
print(threeDarray.size)
print(threeDarray.shape)

print("\n",fourDarray.ndim)
print(fourDarray.size)
print(fourDarray.shape)