words = ['abc', 'nice', 'level']
print(list(filter(lambda word: word ==  word[::-1], words)))