try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first / second
    print("Result:", result)
except ZeroDivisionError:
    print("A number cannot be divided by zero.")
except ValueError:
    print("Please enter valid numbers.")
