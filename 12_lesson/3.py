def get_key(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None  

class Bus:
    
    def __init__(self, max_seats=15):
        self.__speed = 60
        self.__max_seats = max_seats
        self.__max_speed = 90
        self.__surnames = []
        self.__free_place = max_seats
        self.__places = {}

    def fixSpeed(self, value):
        if value > 0:
            self.__speed += value
        elif value < 0:
            self.__speed += value  # Уменьшаем скорость
        return self.__speed
    
    def landingDel(self, surnames):
        for surname in surnames:
            if surname in self.__places.values():
                key = get_key(self.__places, surname)  
                if key is not None:
                    del self.__places[key] 
                    self.__free_place += 1  # Увеличиваем количество свободных мест

    def list_of_surnames(self):
        return self.__surnames
         
    def places(self, surname):
        if self.__free_place > 0:
            position = next((i for i in range(1, self.__max_seats + 1) if i not in self.__places), None)
            if position:
                self.__places[position] = surname
                self.__surnames.append(surname)
                self.__free_place -= 1
        else:
            print("Нет свободных мест!")
        return self.__places

    def display_places(self):
        if not self.__places:
            print("Нет занятых мест.")
        else:
            print("Занятые места:")
            for place, surname in self.__places.items():
                print(f"Место {place}: {surname}")
    
    def get_places(self):
        return self.__places

def main():
    bus = Bus()
    while True:
        print("""
    1. Исправить скорость 
    2. Удалить человека
    3. Список фамилий
    4. Добавить человека 
    5. Показать занятые места
    0. Exit
          """)
        choice = input("Выберите действие: ")
        if choice == "1":
            value = int(input("Введите значение для изменения скорости: "))
            print(f"Текущая скорость: {bus.fixSpeed(value)}")
        elif choice == "2":
            surname = input("Введите фамилию для удаления: ")
            bus.landingDel([surname])  # Передаем список
            print(f"Фамилия '{surname}' удалена.")
        elif choice == "3":
            print("Список фамилий:", bus.list_of_surnames())
        elif choice == "4":
            surname = input("Введите фамилию: ")
            bus.places(surname)
            print(f"Фамилия '{surname}' добавлена.")
        elif choice == "5":
            bus.display_places()  # Вывод занятых мест
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
