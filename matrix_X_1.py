# put your python code here

n = int(input())

matrix = [[0] * n for _ in range(n)]

for r in range(n):
    for c in range(n):
        if r == c or r == n - c - 1:
            matrix[r][c] = 1

for r in range(n):
    for c in range(n:
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()