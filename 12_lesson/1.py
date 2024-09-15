class Product:
    
    def __init__(self,name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price
    
    def name(self):
        return self.__name
    
    def store(self):
        return self.__store
    
    def price(self):
        return self.__price
    
    def __add__(self, other):
        return self.__price + other.__price



class Warehouse:

    def __init__(self):
        self.__products = []
    def add(self,products):
        self.__products.append(products)

    def print_by_index(self,index):
        if 0<=index<=len(self.__products):
            return self.__products[index]
    
    def print_by_name(self,name):
        for name in self.__products:
            if name.__name == name:
                  return name
            
            
    def sort_by_name(self):
        self.__products.sort(key= lambda n: n.name())

    def sort_by_price(self):
        self.__products.sort(key=lambda p: p.price())

    def sort_by_store(self):
        self.__products.sort(key=lambda s: s.store())
    
    def products(self):
        return self.__products


def main():
    warehouse = Warehouse()
    product_1 = Product("Яблоко", "Магазин А", 100)
    product_2 = Product("Груша", "Магазин Б", 150)
    warehouse.add(product_1)
    warehouse.add(product_2)
    warehouse.sort_by_name()
    

    print(product_1 + product_2)
    warehouse.sort_by_name()
    for i in warehouse.products():
        print(f"{i.name()}, {i.store()},{i.price()}")
    
if __name__=="__main__":
    main()