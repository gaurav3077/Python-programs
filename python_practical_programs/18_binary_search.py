numbers = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the number to search for: "))

left = 0
right = len(numbers) - 1
position = -1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        position = middle
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1

if position == -1:
    print("Element not found.")
else:
    print("Element found at index:", position)
