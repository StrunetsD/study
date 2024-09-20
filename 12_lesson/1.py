class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def store(self):
        return self.__store

    @property
    def price(self):
        return self.__price

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price + other.price
        raise TypeError("Can only add Product to Product")


class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_product_by_index(self, index):
        if 0 <= index < len(self.__products):  
            return self.__products[index]
        return None  

    def get_product_by_name(self, name):
        for product in self.__products:
            if product.name == name:
                return product
        return None  # Если продукт не найден

    def sort_by_name(self):
        self.__products.sort(key=lambda p: p.name)

    def sort_by_price(self):
        self.__products.sort(key=lambda p: p.price)

    def sort_by_store(self):
        self.__products.sort(key=lambda p: p.store)

    def get_all_products(self):
        return self.__products


def main():
    warehouse = Warehouse()
    product_1 = Product("Яблоко", "Магазин А", 100)
    product_2 = Product("Груша", "Магазин Б", 150)

    warehouse.add_product(product_1)
    warehouse.add_product(product_2)
    
    total_price = product_1 + product_2
    print(f"Суммарная цена: {total_price}")

    warehouse.sort_by_name()
    for product in warehouse.get_all_products():
        print(f"{product.name}, {product.store}, {product.price}")


if __name__ == "__main__":
    main()
