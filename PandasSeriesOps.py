import pandas as pd
a = pd.Series([10, 20, 30, 40, 50])
b = pd.Series([5, 4, 3, 2, 1])
print("Elements in a series:\n", a)
print("Elements in b series:\n", b)
#Mathematical operators
print("Addition of a and b series:\n", a + b)
print("subtraction of a and b series:\n", b - a)
print("Multiplication of a and b series:\n", a * b)
print("Division of a and b series:\n", a / b)
print("Modulus of a and b series:\n", a % b)
#Relational operators
print(a < b)
print(a > b)
print(a ** b)