class Calculator:

    def get_numbers(self):
        try:
            self.x = float(input("enter first num: "))
            self.y = float(input("enter second num: "))
        except ValueError:
            print("error data")


    def operations(self):
        print('operations:')
        print('1. +')
        print('2. -')
        print('3. /')
        print('4. *')
        print('5. exit')


    def count(self):
        while True:
            try:
                choice = int(input('enter op: '))
                if choice == 1:
                    print(self.x + self.y)
                elif choice == 2:
                    print(self.x - self.y)
                elif choice == 3:
                    print(self.x / self.y)
                elif choice == 4:
                    print(self.x * self.y)
                elif choice == 5:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("error data")


    def run_functions(self):
      Calculator.get_numbers(self)
      Calculator.operations(self)
      Calculator.count(self)


calculator = Calculator()
calculator.run_functions()
