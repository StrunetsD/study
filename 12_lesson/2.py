class BeeAndElephant:
    def __init__(self, bee_num, elephant_num):
        self.bee_num = bee_num  
        self.elephant_num = elephant_num

    @property
    def bee_num(self):
        return self.__bee_num

    @bee_num.setter
    def bee_num(self, value):
        if 0 <= value <= 100:
            self.__bee_num = value
        else:
            raise ValueError("bee_num must be between 0 and 100")

    @property
    def elephant_num(self):
        return self.__elephant_num

    @elephant_num.setter
    def elephant_num(self, value):
        if 0 <= value <= 100:
            self.__elephant_num = value
        else:
            raise ValueError("elephant_num must be between 0 and 100")

    def fly(self):
        return self.bee_num >= self.elephant_num

    def trumpet(self):
        return "tu-tu-doo-doo" if self.elephant_num >= self.bee_num else "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant_num = max(0, self.elephant_num - value)
            self.bee_num = min(100, self.bee_num + value)
        elif meal == "grass":
            self.bee_num = max(0, self.bee_num - value)
            self.elephant_num = min(100, self.elephant_num + value)
        else:
            raise ValueError("Invalid meal type")
        return self.elephant_num, self.bee_num

def main():
    bee_and_elephant = BeeAndElephant(10, 20)
    print(bee_and_elephant.fly())
    print(bee_and_elephant.trumpet())
    print(bee_and_elephant.eat("nectar", 5))
    print(bee_and_elephant.eat("grass", 5))

if __name__ == "__main__":
    main()
