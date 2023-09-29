def covert_to_words(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 0 <= number <= 19:
        return ones[number]
    elif 20 <= number <= 99:
        tens_digit = number // 10
        ones_digit = number % 10
        return tens[tens_digit] + " " + ones[ones_digit]
    else:
        return "Number out of range"

number = int(input("Enter a number (0-99)"))
if 0 <= number <= 99:
    words = covert_to_words(number)
    print(f"The word representation of {number} is: {words}")
else:
    print("Number out of range")