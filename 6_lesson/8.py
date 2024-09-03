import random


def matrix(n, m):
    matrix = []

    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(0, 100))
        matrix.append(row)

    return matrix


def min_in_matrix(matrix):
    temp = matrix[0][0]
    min_index = (0, 0)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < temp:
                temp = matrix[i][j]
                min_index = (i, j)

    return min_index


def max_in_matrix(matrix, m):
    temp = matrix[0][0]
    max_index = (0, 0)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > temp:
                temp = matrix[i][j]
                max_index = (i, j)

    return max_index


m = int(input("rows: "))
n = int(input("cols: "))

matrix = matrix(m, n)
for row in matrix:
    print(row)

min_index = min_in_matrix(matrix)
max_index = max_in_matrix(matrix, m)
print(f"min index: {min_index}, max index {max_index}")
