def binary_search(numbers, key):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (right + left) // 2
        if numbers[mid] == key:
            return mid
        elif numbers[left] <= numbers[mid]:
            if numbers[left] <= key < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if numbers[mid] < key <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def get_num():
    while True:
        num = input("enter key:")
        if num.isdigit():
            return int(num)
        else:
            print("try again")


numbers = [5, 6, 7, 1, 2, 3, 4]
key = get_num()
index = binary_search(numbers, key)

if index != -1:
    print(f"index: {index}")
else:
    print(f"num {key} not found.")
