class Math:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b == 0:
            return "Ошибка: Деление на ноль!"
        return a / b

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("0. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == "0":
            break
        
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        if choice == "1":
            result = Math.addition(a, b)
            print(f"{a} + {b} = {result}")
        elif choice == "2":
            result = Math.subtraction(a, b)
            print(f"{a} - {b} = {result}")
        elif choice == "3":
            result = Math.multiplication(a, b)
            print(f"{a} * {b} = {result}")
        elif choice == "4":
            result = Math.division(a, b)
            print(f"{a} / {b} = {result}")
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
