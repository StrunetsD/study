class Soda:

    def __init__(self):
        self.name = None

    def __str__(self):
        if self.name:
            return f"У вас газировка с {self.name} вкусом"
        else:
            return "У вас обычная газировка"


def main():
    soda = Soda()
    soda.name = "red"
    result = str(soda)
    print(result)


if __name__ == "__main__":
    main()
