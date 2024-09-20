class SuperStr(str):
    
   def is_palindrom(self):
        lower_self = self.lower()  
        return lower_self == lower_self[::-1]

    def is_repeatance(self, s):
        lower_self = self.lower()  
        lower_s = s.lower() 
        repeats = len(lower_self) // len(lower_s)
        return repeats * lower_s == lower_self


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
