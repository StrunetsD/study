def search_number(matrix, H):
    col_with_H = []
    col_without_H = []
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        has_num = False
        for row in range(rows):
            if matrix[row][col] == H:
                has_num = True
                break

        if not has_num:
            col_with_H.append(col)
        else:
            col_without_H.append(col)
    return col_without_H, col_with_H


matrix = [
    [1, 2, 3],
    [0, 3, 4],
    [4, 5, 6],
    [10, 11, 2]
]


col_with_H, col_without_H = search_number(matrix, 0)
print(col_with_H)
print(col_without_H)
