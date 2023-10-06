from functools import reduce
def findremainder(arr, n):
    sum1 = reduce(lambda x, y: x * y, arr)
    remainder = sum1 % n
    print(remainder)
arr = [100, 10, 5, 26, 35, 14]
n = 11
findremainder(arr, n)