import random


def create_matrix():
    m = int(input("rows: "))
    n = int(input("cols: "))
    matrix = []

    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(0, 100))
        matrix.append(row)

    return matrix


matrix = create_matrix()
for row in matrix:
    print(row)
