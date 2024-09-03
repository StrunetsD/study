def multiply_rows_with_k(matrix, k):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result_matrix = []

    K = matrix[k]

    for i in range(num_rows):
        new_row = []
        for j in range(num_cols):
            new_value = matrix[i][j] * K[j]
            new_row.append(new_value)
        result_matrix.append(new_row)
    return result_matrix



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

k = 1

result = multiply_rows_with_k(matrix, k)
for row in result:
    print(row)
