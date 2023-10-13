# Sorting dictionary by key or value
def mydict():
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print("Task 1: \n", key_value)

    for i in sorted(key_value.keys()):
        print(i, end=' ')

def main():
    mydict()

if __name__ == "__main__":
    main()



# Sorting one list with another
def sortlist(list2, list1):
    ziplist = zip(list2, list1)
    z = [x for _, x in sorted(ziplist)]
    return z

x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]
print("\n\n", sortlist(x, y))

x = ["p", "e", "l", "l", "u", "r", "i", "d", "e", "e", "p", "t", "i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]
print(sortlist(x, y))



# Sorting
import numpy as np
matrix = np.array([[15.24, 33.68, 73.59], [32.54, 45.68, 63.59], [51.54, 28.39, 9.29]])
print("\nThe original matrix is:\n", matrix)
print("Sorting the array by row:\n", np.sort(matrix, axis=1))
print("Sorting the array by column:\n", np.sort(matrix, axis=0))