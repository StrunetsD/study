def calculate():
    try:
        x = float(input('enter x: '))
        y = float(input('enter y: '))
        print('operations:')
        print('1. +')
        print('2. -')
        print('3. /')
        print('4. *')
        print('5. exit')
        while True:
            try:
                choice = int(input('enter op: '))
                if choice == 1:
                    print(x + y)
                elif choice == 2:
                    print(x - y)
                elif choice == 3:
                    print(x / y)
                elif choice == 4:
                    print(x * y)
                elif choice == 5:
                    exit("ty for using")
            except ValueError:
                print("error data")
                break
    except ValueError:
        print('error data')


calculate()
