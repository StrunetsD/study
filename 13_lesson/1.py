def fibonacci_gen():
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        first_num, second_num = second_num, first_num + second_num


def main():
    input_num = int(input("enter your num: "))
    gen = fibonacci_gen()
    for num in gen:
        if num <= input_num:
            print(num)


if __name__ == "__main__":
    main()
