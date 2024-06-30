# put your python code here

# Матрица симметрична (относительно главной диагонали), если она равна транспонированной.
#
# Матрица симметрична (относительной побочной диагонали), если она равна транспонированной,
# но начинать надо с элемента n,n (где n - размерность матрицы), то есть с последнего элемента

n = int(input())

matrix = []
matrix_t = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for _ in range(n):
    row = [[0] * n for _ in range(n)]
    matrix_t.append(row)

# транспонируем матрицу
for r in range(n):
    for c in range(n):
        matrix_t[r][c] = matrix[n - 1 - c][r]

for r in range(n):
    for c in range(n):
        if matrix[r][c] == matrix_t[n - 1 - r][c]:
            sym = 'YES'
        else:
            sym = 'NO'
            break
print(sym)