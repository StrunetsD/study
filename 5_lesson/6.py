def get_num():
    while True:
        num = input("enter key:")
        if num.isdigit():
            return int(num)
        else:
            print("try again")


def binary_search(numbers, key):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (right + left) // 2
        if numbers[mid] == key:
            return mid
        elif numbers[mid] < key:
            left = mid + 1
        elif numbers[mid] > key:
            right = mid - 1
    return -1


numbers = [1, 2, 4, 6, 9]
numbers.sort()
key = get_num()
index = binary_search(numbers, key)
if index == -1:
    print("NONE")
else:
    print(f"Index: {index}")
