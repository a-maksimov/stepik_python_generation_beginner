# put your python code here

# put your python code here

n = int(input())

matrix = []
matrix_t = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for _ in range(n):
    row = [[0] * n for _ in range(n)]
    matrix_t.append(row)

for row in matrix:
    for i in range(1, n + 1):
        if row.count(i) > 0:
            res_row = 'YES'
        else:
            res_row = 'NO'
            break

# транспонируем матрицу
for r in range(n):
    for c in range(n):
        matrix_t[r][c] = matrix[n - 1 - c][r]

for row in matrix_t:
    for i in range(1, n + 1):
        if row.count(i) > 0:
            res_col = 'YES'
        else:
            res_col = 'NO'
            break

if res_row == 'YES' and res_col == 'YES':
    res = 'YES'
else:
    res = 'NO'

print(res)