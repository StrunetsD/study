import math


def factorial(num):
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        exit()
    else:
        fac = 1
        for i in range(1, num + 1):
            fac *= i
    return fac


x = int(input("enter x:"))
result_a = 0
result_b = 0
for n in range(0, 50):
    # пример a
    temp_a = math.pow(-1, n) * (math.pow(x, (2 * n + 1))) / (factorial(2 * n + 1))
    # пример b
    temp_b = math.pow(-1, n) * (math.pow(x, 2 * n)) / factorial(2 * n)
    result_a += temp_a
    result_b += temp_b

print(f"result of a: {result_a}")
print(F"result of b: {result_b}")
