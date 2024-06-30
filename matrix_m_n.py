# put your python code here

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for r in range(n):
    add = 0
    for c in range(m):
        matrix[r][c] = r + add + 1
        add += n

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
