def sum_main_diagonal(matrix):
    result = 0
    for i in range(len(matrix)):
        result += matrix[i][i]
    return result


def sum_side_diagonal(matrix):
    result = 0
    for i in range(len(matrix)):
        result += matrix[i][len(matrix[0]) - i - 1]
    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
main_sum = sum_main_diagonal(matrix)
side_sum = sum_side_diagonal(matrix)
print(main_sum)
print(side_sum)
