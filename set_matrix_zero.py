def matrix_zero(a, n, m):
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                markRow(a, i, m)
                markCol(a, j, n)
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                a[i][j] = 0

def markRow(a, i, m):
    for j in range(m):
        if a[i][j] != 0:
            a[i][j] = -1

def markCol(a, j, n):
    for i in range(n):
        if a[i][j] != 0:
            a[i][j] = -1

matrix = [
    [1, 2, 0],
    [4, 0, 6],
    [7, 8, 9]
]

n = len(matrix)
m = len(matrix)

matrix_zero(matrix, n, m)

for row in matrix:
    print(row)
