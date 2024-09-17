class SuperStr(str):
    
    def is_palindrom(self):
        return self == self[::-1]

    def is_repeatance(self, s):
        repeats = len(self) // len(s)
        return repeats * s == self


def main():
    super_str = SuperStr("abcabcabc")

    if super_str.is_repeatance("abc"):
        print(True)
    else:
        print(False)

    if super_str.is_palindrom():
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()
