numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter the number to search for: "))

position = -1

for index, value in enumerate(numbers):
    if value == target:
        position = index
        break

if position == -1:
    print("Element not found.")
else:
    print("Element found at index:", position)
