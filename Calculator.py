num1=float(input("Enter first num:"))
operator=input("Enter operator one:")
num2=float(input("Enter second num:"))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "%":
    print(num1/num2)
elif operator == "//":
    print(num1/num2)
else:
    print("invalid operator")