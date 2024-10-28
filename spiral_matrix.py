def spiral_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    left, right = 0, m - 1
    top, bottom = 0, n - 1
    spiral_order = []

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            spiral_order.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            spiral_order.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral_order.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral_order.append(matrix[i][left])
            left += 1

    return spiral_order

matrix = [
    [1, 2, 0, 6],
    [4, 0, 6, 2],
    [7, 8, 9, 9],
    [2, 3, 4, 6]
]

spiral_result = spiral_matrix(matrix)
print(spiral_result)
