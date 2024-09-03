fibonacci_numbers = []
first_num = 0
second_num = 1
for i in range(1, 12):
    fibonacci_numbers.append(second_num)
    temp = second_num
    second_num = first_num + second_num
    first_num = temp

print(fibonacci_numbers)