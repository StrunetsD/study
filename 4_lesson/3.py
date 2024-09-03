import math


def calculate_year_length(R, V):
    L = 2 * math.pi * R / V
    return L


print("Введите информацию о двух планетах:")
print("Первая планета:")
first_R = float(input("Радиус (в км): "))
first_V = float(input("Орбитальная скорость (в км/с): "))
first_L = calculate_year_length(first_R, first_V)
print(f"Длина года на второй планете:", first_L, "дней")
print("Вторая планета:")
second_R = float(input("Радиус (в км): "))
second_V = float(input("Орбитальная скорость (в км/с): "))
second_L = calculate_year_length(second_R, second_V)
print(f"Длина года на второй планете:", second_L, "дней")

if first_L > second_L :
    print("Год на первой планете длиннее, чем на второй.")
else:
    print("Год на первой планете меньше, чем на второй.")