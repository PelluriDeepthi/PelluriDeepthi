import numpy as np
my_list = [10, 20, 30, 40]
arr = np.array(my_list)
for ele in arr:
    print(ele)


#Two dimensional array
my_list1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
matrix = np.array(my_list1)
print("\n", matrix)
for row in matrix:
    print("\n", row)
for row in matrix:
    for ele in row:
        print("\n", ele)
for row in matrix:
    for ele in row:
        print("\n", ele, end=' ')
    print()