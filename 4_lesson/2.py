import math


x = int(input("Enter value x:"))
first_y = math.pow(math.pow(math.cos(math.pow(x,2)), 2) + math.pow(math.sin(2 * x - 1), 2), 1/3)
second_y = math.cos(x) + math.sin(x)
third_y = 5 * x + 3 * math.pow(x, 2) * math.pow(1 + math.pow(math.sin(x), 2), 1/3)
print("Second formula:", first_y)
print("Third formula:", second_y)
print("Fourth formula:", third_y)