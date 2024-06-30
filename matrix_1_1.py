# put your python code here

n, m = int(input()), int(input())

matrix = []

for i in range(n):
    row = [input() for _ in range(m)]
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# [print(*[input() for i in range(m)]) for i in range(n)]
