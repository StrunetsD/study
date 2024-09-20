from abc import  ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, first_num, second_num):
        pass

class Addition(Strategy):
    def execute(self, first_num, second_num):
        return first_num + second_num

class Subtraction(Strategy):
    def execute(self, first_num, second_num):
        return first_num - second_num

class Multiplication(Strategy):
    def execute(self, first_num, second_num):
        return first_num * second_num

class Division(Strategy):
    def execute(self, first_num, second_num):
        if second_num == 0:
            raise ZeroDivisionError("error")
        else:
          return first_num / second_num

class Calculator:
    def __init__(self, strategy : Strategy):
        self._strategy = strategy
    def set_strategy(self, strategy : Strategy):
        self._strategy = strategy
    def calculate(self, first_num,second_num):
       return  self._strategy.execute(first_num, second_num)

def main():
    calculator = Calculator(Addition())
    print(f"sum: {calculator.calculate(1,2)}")
    calculator.set_strategy(Multiplication())
    print(f"mul: {calculator.calculate(1, 2)}")
    calculator.set_strategy(Subtraction())
    print(f"mul: {calculator.calculate(1, 2)}")
    calculator.set_strategy(Division())
    print(f"mul: {calculator.calculate(4, 2)}")

if __name__=="__main__":
    main()