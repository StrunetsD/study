def get_key(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return None  

class Bus:
    
    def __init__(self,max_seats = 15):
        self.__speed = 60
        self.__max_seats = max_seats
        self.__max_speed = 90
        self.__surnames = []
        self.__free_place = max_seats
        self.__places = {}

    def fixSpeed(self,value):
        if value > 0:
             self.__speed + value
        elif value < 0:
            self.__speed - value
        else :
            self.__speed
        return self.__speed
    
    def landingDel(self, surnames):
        for surname in surnames:
            if surname in self.__places.values():
                key = get_key(self.__places, surname)  
                if key is not None:
                    del self.__places[key] 

    def list_of_surnames(self,surnames):
        for surname in surnames:
            self.__surnames.append(surname)
        return self.__surnames
         
    def places(self,surnames):
        position = 1
        for surname in surnames:
                self.__places[position] = surname
                position+=1
        return self.__places
    def get_places(self):
        return self.__places
def main():
    bus = Bus()
    surnames = ["vova", "dima"]
    landing = ["vova"]
    print(bus.fixSpeed(-10))

    print("Список фамилий:", bus.list_of_surnames(surnames))
    bus.places(surnames)  
    print("Места перед посадкой:", bus.get_places())
    bus.landingDel(landing)  
    print("Места после посадки:", bus.get_places())

if __name__ == "__main__":
    main()