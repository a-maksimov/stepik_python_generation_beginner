n = int(input())

matrix = [[0] * n for _ in range(n)]

for r in range(n):
    for c in range(n):
        if r < n - 1 - c:
            matrix[r][c] = 0
        elif r > n - 1 - c:
            matrix[r][c] = 2
        else:
            matrix[r][c] = 1

for row in range(n):
    print(*matrix[row])