str = 'TEST-STR'
print("Третий символ:", str[2:3])
print("Предпоследний символ:", str[len(str)-2])
print("Первые пять символов:", str[:5])
print("До последних двух символов:", str[0:len(str)-2])
print("Символы с четными индексами:", str[::2])
print("Символы с нечетными индексами:", str[1::2])
print("Cимволы в обратном порядке:", str[::-1])
print("Cимволы строки через один в обратном порядке, начиная с последнего:", str[-1::-2])
print("Длина строки:", len(str))