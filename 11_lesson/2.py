class Math:

    def input(self):
        x = float(input("enter first num: "))
        y = float(input("enter second num: "))
        return x, y

    def addition(self, x, y):
        return print(f"addition: {x + y}")

    def subtraction(self, x, y):
        return print(f"subtraction: {x - y}")

    def multiplication(self, x, y):
        return print(f"multiplication: {x * y}")

    def division(self, x, y):
        return print(f"division: {x / y}")

    def run(self):
        x, y = self.input()
        self.addition(x, y)
        self.subtraction(x, y)
        self.multiplication(x, y)
        self.division(x, y)


def main():
    calculator = Math()
    calculator.run()


if __name__ == "__main__":
    main()
