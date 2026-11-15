def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


values = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
search_value = int(input("Enter the value to find: "))
result = binary_search(values, search_value)

if result == -1:
    print("Value not found.")
else:
    print("Value found at index:", result)
