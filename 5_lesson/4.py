def summa_of_numbers(numbers):
    summa = 0
    for num in numbers:
        summa += num
    return summa


def minimum(numbers):
    buff = numbers[0]
    for num in numbers:
        if num < buff:
            buff = num
    return buff


def maximum(numbers):
    buff = numbers[0]
    for num in numbers:
        if num > buff:
            buff = num
    return buff


numbers = [1, 2, 3, 4, 0, -1]
print(f"Sum of elements {summa_of_numbers(numbers)}; max: {maximum(numbers)}, minimum: {minimum(numbers)}")
