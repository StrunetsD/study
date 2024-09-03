import re


def get_sum_numbers():
    with  open("numbers.txt", "r", encoding="utf-8") as file:
        data = file.read()
        numbers = re.findall(r'\d+', data)
        summ = sum(int(num) for num in numbers)
        return summ


def main():
    result = get_sum_numbers()
    print(result)


if __name__ == "__main__":
    main()
