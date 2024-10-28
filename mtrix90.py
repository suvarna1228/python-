def matrix_90(matrix):
     n = len(matrix)
     rotated = [[0] * n for _ in range(n)]
     for i in range(n):
        for j in range(n):
           rotated[j][n - 1 - i] = matrix[i][j]
     return rotated

matrix = [
    [1, 2, 0],
    [4, 0, 6],
    [7, 8, 9]
]
rotated = matrix_90(matrix)
for row in rotated:
    print(row)