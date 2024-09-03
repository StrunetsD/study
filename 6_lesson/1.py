def binary_search(numbers, key, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if numbers[mid] == key:
        return mid
    elif numbers[mid] > key:
        return binary_search(numbers, key, left, mid - 1)
    else:
        return binary_search(numbers, key, mid + 1, right)


numbers = [1, 2, 3, 4, 5]
index = binary_search(numbers, 1, 0, len(numbers) - 1)
print(index)
