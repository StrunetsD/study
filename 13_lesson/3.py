class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        return (f"Pizza size: {self.size}, "
                f"Cheese: {self.cheese}, "
                f"Pepperoni: {self.pepperoni}, "
                f"Mushrooms: {self.mushrooms}, "
                f"Onions: {self.onions}, "
                f"Bacon: {self.bacon}")


class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(self.size, self.cheese, self.pepperoni, self.mushrooms, self.onions, self.bacon)



class PizzaDirector:
    def __init__(self):
        self.builder = PizzaBuilder()

    def make_pizza(self):
        return (self.builder
                .set_size(10)
                .add_cheese()
                .add_pepperoni()
                .add_bacon()
                .build())


if __name__ == "__main__":
    builder = PizzaBuilder()
    director = PizzaDirector()
    pizza = director.make_pizza()
    print(pizza)