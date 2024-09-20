class Soda:
    def __init__(self, name=None):
        self._name = name  

    @property
    def name(self):
        return self._name

    def __str__(self):
        if self._name:
            return f"У вас газировка с {self._name} вкусом"
        else:
            return "У вас обычная газировка"


def main():
    soda = Soda(name="red")  
    result = str(soda)
    print(result)

if __name__ == "__main__":
    main()
