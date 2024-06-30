n, m = [int(i) for i in input().split()]
matrix = []

ls = list(range(1, m + 1))

for r in range(n):
    matrix.append(ls[r % m:] + ls[:-len(ls) + r % m])

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
