def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum/len(numbers))
average(6, 6)