from abc import  ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Gaw"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def create_animal(type_of_animal):
        if type_of_animal.lower() == "dog":
            return Dog()
        if type_of_animal.lower() == "cat":
            return Cat()
        else:
            raise ValueError("there is no type")


def main():
    factory = AnimalFactory()
    dog = factory.create_animal("dog")
    print(dog.speak())
    cat = factory.create_animal("cat")
    print(cat.speak())

if __name__=="__main__":
    main()