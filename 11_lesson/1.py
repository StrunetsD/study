class Soda:

    def __init__(self):
        self.name = None

    def representations(self):
        if self.name is not None:
            return f"soda with {self.name} taste"
        else:
            return "default soda"


def main():
    soda = Soda()
    soda.name = "red"
    result = soda.representations()
    print(result)


if __name__ == "__main__":
    main()
