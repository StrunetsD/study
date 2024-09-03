def IMT():
    try:
        height = float(input('height(m): '))
        weight = float(input('weight(kg): '))

        if height <= 0 and weight <= 0:
            raise ValueError('please enter correct data')

        imt = weight / (height ** 2)
        print(imt)
        if imt < 18.5:
            print("You are in the range of underweight.")
        elif 18.5 <= imt < 25:
            print("Your weight is normal.")
        elif 25 <= imt < 30:
            print("You are in the range of overweight.")
        elif 30 <= imt < 35:
            print("You are in the range of obesity grade 1.")
        elif 35 <= imt < 40:
            print("You are in the range of obesity grade 2.")
        else:
            print("You are in the range of obesity grade 3.")

    except ValueError:
        print("please enter correct data")


IMT()
