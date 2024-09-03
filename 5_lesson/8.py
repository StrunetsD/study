str = " k dima of  privet radmila"
str = str.split()
temp = str[0]
for word in str:
    if word < temp:
        temp = word

print(temp)
