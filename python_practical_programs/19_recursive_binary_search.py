def binary_search(numbers, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle
    if numbers[middle] < target:
        return binary_search(numbers, target, middle + 1, right)
    return binary_search(numbers, target, left, middle - 1)


numbers = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter the number to search for: "))

position = binary_search(numbers, target, 0, len(numbers) - 1)

if position == -1:
    print("Element not found.")
else:
    print("Element found at index:", position)
