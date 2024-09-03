def add_col(matrix):
    for i in matrix:
        counter = i.count(1)
        if counter % 2 == 0:
            i.append(0)
        else:
            i.append(1)


matrix = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
    [1, 0, 1]
]
add_col(matrix)
for row in matrix:
    print(row)
