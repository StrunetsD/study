def decimal_to_binary(num):
    if num == 0:
        return "0"

    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    return binary


number = 169
binary_num = decimal_to_binary(number)
print(binary_num)
