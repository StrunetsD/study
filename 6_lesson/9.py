def sum_of_elements(matrix):
    summa = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            summa += matrix[i][j]
    return summa


def percent_of_sum(matrix):
    total_sum = sum_of_elements(matrix)
    cols = len(matrix[0])
    col_summ = [0] * cols

    for row in matrix:
        for j in range(cols):
            col_summ[j] += row[j]

    result_percent = []
    for num in col_summ:
        result = num / total_sum * 100
        result_percent.append(result)
    return result_percent


matrix = [
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6],
    [10, 11, 2]
]

result_total = percent_of_sum(matrix)
print(result_total)
