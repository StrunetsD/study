def sequence(nums):
    while True:
        for num in nums:
            yield num


def main():
    input_number = int(input("enter the number up to which the repetition will occur:"))
    nums = [i for i in range(1,input_number+1)]
    gen = sequence(nums)
    input_num = int(input("enter number of iterations: "))
    for _ in range(1,input_num+1):
        for num in nums:
            num = next(gen)
            print(num)


if __name__ == "__main__":
    main()
