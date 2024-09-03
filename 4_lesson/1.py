import math


a = int(input("Enter value a:"))
b = int(input("Enter value b:"))
y = math.pow(a,2) / 3 + (math.pow(a,2) + 4) / b + (math.sqrt(math.pow(a, 2) + 4))/ 4 + (math.pow(math.pow(a, 2) + 4, 1/3))  / 4
print("First formula:", y)
