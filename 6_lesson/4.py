def nod(first_num, second_num):
    while second_num:
        first_num, second_num = second_num, first_num % second_num
    return first_num


print(nod(40, 16))
