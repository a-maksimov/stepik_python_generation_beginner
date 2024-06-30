n, m = [int(i) for i in input().split()]
matrix = []

ls = list(range(1, n * m + 1))

for r in range(n):
    row = ls[:m]
    if r % 2 != 0:
        row.reverse()
    matrix.append(row)
    ls = ls[m:]

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()