class SuperStr(str):

    def __init__(self, current):
        self.current = current

    def is_palindrom(self, string):
        return string == string[::-1]

    def is_repeatance(self, s):
        repeats = len(self.current) // len(s)
        if repeats * s == self.current:
            return True
        else:
            return False


def main():
    super_str = SuperStr("bacasdf")

    if super_str.is_repeatance("abc"):
        print(True)
    else:
        print(False)
    if super_str.is_palindrom("abccba"):
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()
