# put your python code here

n, m = int(input()), int(input())

matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * j