import math

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    total = sum(math.factorial(int(digit)) for digit in str(number))

    if total == number:
        print(number, "is a strong number.")
    else:
        print(number, "is not a strong number.")
