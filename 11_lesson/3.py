class Car:
    def __init__(self):
        self.color = None
        self.car_type = None
        self.year = None

    def start_engine(self):
        print("Двигатель заведён.")

    def turn_off_engine(self):
        print("Двигатель заглушён.")

    def get_input(self):
        self.color = input("Введите цвет: ")
        self.car_type = input("Введите тип: ")
        while True:
            try:
                self.year = int(input("Введите год: "))
                break
            except ValueError:
                print("Пожалуйста, введите числовое значение для года.")

    def display_info(self):
        print(f"Цвет: {self.color}")
        print(f"Тип: {self.car_type}")
        print(f"Год: {self.year}")

    def run(self):
        self.start_engine()
        self.get_input()
        self.display_info()
        self.turn_off_engine()


def main():
    car = Car()
    car.run()


if __name__ == "__main__":
    main()
