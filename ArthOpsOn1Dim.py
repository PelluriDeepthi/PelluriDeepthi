import numpy as np

zeroDarray1 = np.array([3,4])
zeroDarray2 = np.array([1,2])

#To perform operations, we need to have same shape either 2*2 or 3*3
resultarray = zeroDarray1 + zeroDarray2
print("The addition of",zeroDarray1, "and", zeroDarray2 ,"is:", resultarray)

resultarray = zeroDarray1 - zeroDarray2
print("\nThe Subtraction of",zeroDarray1, "and", zeroDarray2 ,"is:", resultarray)

resultarray = zeroDarray1 * zeroDarray2
print("\nThe Multiplication of",zeroDarray1, "and", zeroDarray2 ,"is:", resultarray)

resultarray = zeroDarray1 / zeroDarray2
print("\nThe Division of",zeroDarray1, "and", zeroDarray2 ,"is:", resultarray)

resultarray = zeroDarray1 % zeroDarray2
print("\nThe Remainder of",zeroDarray1, "and", zeroDarray2 ,"is:", resultarray)

resultarray = zeroDarray1 // zeroDarray2
print("\nThe FloorDivision of",zeroDarray1, "and", zeroDarray2 ,"is:", resultarray)

print("The square of",zeroDarray1, "is:", zeroDarray1**3)
