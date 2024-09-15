class BeeAndElephant:

    def __init__(self,bee_num,elephant_num):
        self.__bee_num = bee_num
        self.__elephant_num = elephant_num

    def fly(self):
        if self.__bee_num >= self.__elephant_num:
            return True
        return False

    def trumpet(self):
        if self.__elephant_num >= self.__bee_num:
           return "tu-tu-doo-doo"
        return "wzzzz"
    
    def eat(self, meal, value):
        if meal == "nectar":
            if 0 <= self.__elephant_num < 100:
                self.__elephant_num = max(0, self.__elephant_num - value)
            else:
                raise ValueError("elephant_num is out of range")
            
            if 0 <= self.__bee_num < 100: 
                self.__bee_num = min(100, self.__bee_num + value)
            else:
                raise ValueError("bee_num is out of range")

        elif meal == "grass":
            if 0 <= self.__bee_num < 100: 
                self.__bee_num = max(0, self.__bee_num - value)
            else:
                raise ValueError("bee_num is out of range")
            
            if 0 <= self.__elephant_num < 100:
                self.__elephant_num = min(100, self.__elephant_num + value)
            else:
                raise ValueError("elephant_num is out of range")
        else:
            raise ValueError("Invalid meal type")
        return self.__elephant_num, self.__bee_num

def main():
    beeAndElephant = BeeAndElephant(10, 20)
    print(beeAndElephant.fly())
    print(beeAndElephant.trumpet())
    print(beeAndElephant.eat("nectar", 5))
    print(beeAndElephant.eat("grass", 5))

if __name__ == "__main__":
    main()