n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

nm = 0
for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                nm += 1
                matrix[i][j] = nm

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()