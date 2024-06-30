n = int(input())

matrix = []

for i in range(n):
    row = input().split()
    matrix.append(row)

for r in range(n):
    for c in range(n):
        if r == c:
            matrix[r][c], matrix[n - 1 - r][c] = matrix[n - 1 - r][c], matrix[r][c]

for r in range(n):
    for c in range(n):
        print(str(matrix[r][c]), end=' ')
    print()


# int(input())
# matrix = [input().split() for _ in range(n)]
#
# for i in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# for row in matrix:
#     print(*row)